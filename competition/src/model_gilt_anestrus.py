"""후보돈(replacement gilt) 무발정·발정지연 위험 예측 + 개선요인 진단.

도메인 근거(한돈뉴스, http://www.pignpork.com):
  "초교배 일령이 지났는데 발정이 오지 않거나 강도가 약하다면, 후보돈 성장과정의
   질병 이력이나 후보돈사 내의 시설·질병·사료·음수 등을 체크하여 반드시 개선."

즉 무발정/발정지연은 **관리 가능한 요인**에 크게 좌우된다. 이 모델은
  (1) 예측  : 어느 후보돈이 초교배 일령까지 발정을 못 보일 위험이 높은가
  (2) 처방  : 그 위험을 만드는 '개선 가능한' 요인이 무엇인가(개체별 플래그)
를 함께 낸다.

피처와 데이터 출처(실데이터 연결 시 대조):
  - age_over_target   : (현재일령 - 초교배 목표일령)      ← 사양관리 대장
  - growth_disease_cnt: 성장기 질병 이력 횟수             ← 진료/투약 기록
  - backfat_mm        : 등지방두께(성성숙 지표)           ← 초음파 측정
  - facility_score    : 후보돈사 시설 점수(바닥·스톨·채광) ← 시설 점검표
  - feed_adequacy     : 사료 영양·급이 적정도(0~1)        ← 71763 feedstuff/영양
  - water_adequacy    : 음수 급수량·수질 적정도(0~1)      ← 71763 watersupply
  - nh3_ppm, temp_c, humidity : 후보돈사 공기·열환경       ← 71763 SensorData
  - boar_exposure_min : 일일 웅돈 접촉 시간(발정 자극 핵심) ← 사양관리 기록
  - weight_kg
타깃 anestrus(0/1): 초교배 일령까지 정상 발정 미발현(무발정/발정미약).

실데이터가 없으면 도메인 관계를 심은 합성 데이터로 전체 흐름을 시연한다.
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (f1_score, precision_score, recall_score,
                             roc_auc_score)
from sklearn.model_selection import StratifiedKFold, cross_val_predict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import train as train_mod  # noqa: E402

# 개선 가능한(관리) 요인과 '양호' 방향. 처방 플래그에 사용.
MODIFIABLE = {
    "feed_adequacy": ("low", 0.6),      # 낮으면 문제
    "water_adequacy": ("low", 0.6),
    "facility_score": ("low", 0.6),
    "boar_exposure_min": ("low", 10),   # 웅돈 접촉 부족
    "nh3_ppm": ("high", 25),            # 높으면 문제
    "temp_c": ("high", 28),             # 고온 스트레스
    "growth_disease_cnt": ("high", 2),
}


def generate_synthetic(n: int = 1500, seed: int = 7) -> pd.DataFrame:
    """도메인 관계를 심은 후보돈 합성 데이터."""
    rng = np.random.default_rng(seed)
    age_over = rng.normal(5, 18, n).clip(-30, 60)          # 목표일령 대비
    disease = rng.poisson(1.2, n).clip(0, 8)               # 성장기 질병 이력
    backfat = rng.normal(14, 2.5, n).clip(8, 22)           # 등지방(mm)
    facility = rng.uniform(0.3, 1.0, n)                    # 시설 점수
    feed = rng.uniform(0.4, 1.0, n)                        # 사료 적정도
    water = rng.uniform(0.4, 1.0, n)                       # 음수 적정도
    nh3 = rng.normal(16, 7, n).clip(2, 45)                 # 암모니아
    temp = rng.normal(23, 4, n).clip(12, 34)               # 기온
    humidity = rng.normal(65, 10, n).clip(35, 95)
    boar = rng.normal(15, 7, n).clip(0, 40)                # 웅돈 접촉(분/일)
    weight = rng.normal(130, 12, n).clip(95, 170)

    # 무발정 위험 로짓: 관리요인이 나쁠수록↑ (도메인 방향 반영)
    logit = (
        -2.7
        + (feed < 0.6) * 0.9 + (1 - feed) * 0.8
        + (water < 0.6) * 0.7 + (1 - water) * 0.6
        + (facility < 0.6) * 0.7 + (1 - facility) * 0.6
        + disease * 0.35
        + np.maximum(0, nh3 - 25) * 0.05
        + np.maximum(0, temp - 28) * 0.18
        + np.maximum(0, 10 - boar) * 0.09          # 웅돈 접촉 부족
        + np.maximum(0, 12 - backfat) * 0.15       # 성성숙 미달
        + np.maximum(0, age_over) * 0.015          # 이미 지연된 경우 위험↑
        + rng.normal(0, 0.5, n)
    )
    prob = 1 / (1 + np.exp(-logit))
    anestrus = (rng.random(n) < prob).astype(int)

    return pd.DataFrame({
        "age_over_target": age_over.round(0),
        "growth_disease_cnt": disease,
        "backfat_mm": backfat.round(1),
        "facility_score": facility.round(2),
        "feed_adequacy": feed.round(2),
        "water_adequacy": water.round(2),
        "nh3_ppm": nh3.round(1),
        "temp_c": temp.round(1),
        "humidity_pct": humidity.round(1),
        "boar_exposure_min": boar.round(0),
        "weight_kg": weight.round(1),
        "anestrus": anestrus,
    })


def prescribe(row: pd.Series) -> list[str]:
    """개체의 '개선 필요' 요인 목록(관리 가능한 것만)."""
    flags = []
    for feat, (bad, thr) in MODIFIABLE.items():
        v = row.get(feat)
        if v is None or pd.isna(v):
            continue
        if (bad == "low" and v < thr) or (bad == "high" and v > thr):
            flags.append(feat)
    return flags


def load(path: str | None) -> pd.DataFrame:
    if path and os.path.isfile(path):
        df = pd.read_csv(path)
        print(f"실데이터: {path} → {len(df)}행")
    else:
        df = generate_synthetic()
        print(f"(합성 데이터 시연) {len(df)}행 — 실행: model_gilt_anestrus.py <csv>")
    return df


def run(df: pd.DataFrame) -> None:
    if "anestrus" not in df.columns:
        print("타깃 'anestrus' 없음"); return
    y = df["anestrus"].astype(int).to_numpy()
    print(f"후보돈 {len(df)}두 | 무발정/발정지연 {y.sum()}두 ({y.mean():.0%})")

    feats = [c for c in df.columns if c != "anestrus"]
    num = [c for c in feats if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in feats if c not in num]
    X = df[num + cat]

    pipe = train_mod.make_pipeline(
        num, cat, GradientBoostingClassifier(random_state=42))
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    proba = cross_val_predict(pipe, X, y, cv=cv, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)

    print("\n=== 무발정 위험 예측 (StratifiedKFold) ===")
    print(f"  ROC-AUC {roc_auc_score(y, proba):.3f} | F1 {f1_score(y, pred):.3f}"
          f" | 정밀도 {precision_score(y, pred):.3f}"
          f" | 재현율 {recall_score(y, pred):.3f}")

    pipe.fit(X, y)
    train_mod.save_importances(pipe, num, cat, "gilt_anestrus")

    # 처방 시연: 위험 상위 3두의 개선 필요 요인
    df = df.copy()
    df["risk"] = proba
    print("\n=== 개선 처방 예시 (위험 상위 3두) ===")
    for _, r in df.sort_values("risk", ascending=False).head(3).iterrows():
        flags = prescribe(r)
        print(f"  위험 {r['risk']:.0%} → 개선필요: "
              f"{', '.join(flags) if flags else '뚜렷한 관리요인 없음(질병력/성성숙 검토)'}")

    # 관리요인 개선 시 기대효과: 나쁜 요인 하나라도 있는 그룹의 무발정률
    bad_any = df.apply(lambda r: len(prescribe(r)) > 0, axis=1)
    if bad_any.any() and (~bad_any).any():
        print(f"\n  관리요인 불량군 무발정률 {df[bad_any]['anestrus'].mean():.0%} "
              f"vs 양호군 {df[~bad_any]['anestrus'].mean():.0%}")


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else None
    os.makedirs("competition/outputs", exist_ok=True)
    run(load(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
