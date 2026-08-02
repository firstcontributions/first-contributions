"""통합 파이프라인: CCTV 발정관찰 → 후보돈 무발정 위험 + 개선 처방.

경로
  ① CCTV 키프레임(71471 스키마) → 개체 시계열 집계(활동량·행동 비율·자세)
     = '발정 행동 신호'                              [model_71471_estrus 재사용]
  ② 개체별 관리요인(사료·음수·시설·웅돈접촉·질병력·환경) 결합
  ③ ①+② 를 융합해 무발정(초교배 일령까지 미발정) 위험을 예측하고,
     개체별 '개선 가능한' 요인을 처방                [model_gilt_anestrus 재사용]

설계 포인트: CCTV 신호와 무발정 결과는 **공통 잠재변수(번식 준비도 readiness)**
를 공유한다. readiness 는 관리요인이 좋을수록 높고, readiness 가 높으면 CCTV
에서 뚜렷한 발정행동(활동↑·기립·꼬리세움)이 관찰되며 무발정 위험은 낮다.
따라서 CCTV 행동 신호는 무발정의 '관찰 가능한 증거', 관리요인은 '개선 지렛대'.

실행:
    python yangdon/src/pipeline_gilt.py                 # 합성 시연
    python yangdon/src/pipeline_gilt.py <cctv_라벨디렉터리> <gilt_mgmt.csv>
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
import model_71471_estrus as estrus  # noqa: E402
import model_gilt_anestrus as anestrus  # noqa: E402
import parse_aihub  # noqa: E402
import train as train_mod  # noqa: E402

BEHAVIORS = estrus.BEHAVIORS


# --------------------------------------------------------------------------
# 공통 잠재변수(readiness)를 공유하는 조인트 합성 데이터
# --------------------------------------------------------------------------
def generate_joint(n_gilts: int = 600, frames: int = 20, seed: int = 11):
    """(cctv_frames_df, mgmt_df) 반환. 개체 id 로 결합 가능."""
    rng = np.random.default_rng(seed)

    # 관리요인
    feed = rng.uniform(0.4, 1.0, n_gilts)
    water = rng.uniform(0.4, 1.0, n_gilts)
    facility = rng.uniform(0.3, 1.0, n_gilts)
    boar = rng.normal(15, 7, n_gilts).clip(0, 40)
    disease = rng.poisson(1.2, n_gilts).clip(0, 8)
    nh3 = rng.normal(16, 7, n_gilts).clip(2, 45)
    temp = rng.normal(23, 4, n_gilts).clip(12, 34)
    humidity = rng.normal(65, 10, n_gilts).clip(35, 95)
    backfat = rng.normal(14, 2.5, n_gilts).clip(8, 22)
    weight = rng.normal(130, 12, n_gilts).clip(95, 170)
    age_over = rng.normal(5, 18, n_gilts).clip(-30, 60)

    # 번식 준비도(0~1): 관리요인이 좋을수록↑
    z = (
        2.2 * (feed - 0.7) + 1.8 * (water - 0.7) + 1.8 * (facility - 0.65)
        + 0.08 * (boar - 15) - 0.45 * disease
        - 0.08 * np.maximum(0, nh3 - 25) - 0.22 * np.maximum(0, temp - 28)
        + 0.18 * (backfat - 12) + rng.normal(0, 0.35, n_gilts)
    )
    readiness = 1 / (1 + np.exp(-z))

    # 무발정(결과): readiness 낮을수록↑ (+ 이미 지연된 개체 가중)
    p_anestrus = 1 / (1 + np.exp(-(-0.3 - 5.0 * (readiness - 0.5)
                                   + 0.02 * np.maximum(0, age_over))))
    anestrus_y = (rng.random(n_gilts) < p_anestrus).astype(int)

    mgmt = pd.DataFrame({
        "individual_id": [f"G{ i:04d}".replace(" ", "") for i in range(n_gilts)],
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
        "anestrus": anestrus_y,
    })

    # CCTV 프레임: readiness 높으면 활동↑·기립/꼬리세움↑ (발정행동), 낮으면 눕기↑
    rows = []
    for i in range(n_gilts):
        gid = mgmt.loc[i, "individual_id"]
        r = readiness[i]
        move = (4 + 26 * r) + rng.normal(0, 1.5)  # 활동량: readiness에 비례
        move = max(2.0, move)
        # 행동 분포: readiness 높을수록 standing/tailing↑, lying↓
        probs = {
            "standing": 0.12 + 0.18 * r, "tailing": 0.05 + 0.16 * r,
            "eating": 0.18, "head shaking": 0.08,
            "sitting": 0.12, "lying": 0.45 - 0.30 * r,
        }
        behs = list(probs); wts = np.array(list(probs.values()))
        wts = wts.clip(0.01); wts = wts / wts.sum()
        bx, by = rng.uniform(200, 800), rng.uniform(200, 600)
        for f in range(frames):
            behavior = rng.choice(behs, p=wts)
            cx = bx + rng.normal(0, move); cy = by + rng.normal(0, move)
            w = rng.uniform(120, 300); h = rng.uniform(70, 180)
            rows.append({
                "file": f"{gid}_f{f:03d}.json",
                "individual_id": gid, "frame_idx": f,
                "species": "pig", "behavior": behavior,
                "estrus": np.nan,  # CCTV 원천엔 결과 라벨 없음(관찰만)
                "bbox_w": round(w, 1), "bbox_h": round(h, 1),
                "aspect_ratio": round(w / h, 3),
                "centroid_x": round(cx, 2), "centroid_y": round(cy, 2),
                "kp_spread": round(rng.uniform(20, 40), 2),
            })
    return pd.DataFrame(rows), mgmt


# --------------------------------------------------------------------------
def build_cctv_signals(frames: pd.DataFrame) -> pd.DataFrame:
    """CCTV 프레임 → 개체별 발정행동 신호(활동량·행동비율·자세)."""
    feat = estrus.build_estrus_features(frames)
    return feat.drop(columns=[c for c in ("estrus", "species") if c in feat])


def run(frames: pd.DataFrame, mgmt: pd.DataFrame) -> None:
    signals = build_cctv_signals(frames)
    df = mgmt.merge(signals, on="individual_id", how="inner")
    print(f"결합 완료: 후보돈 {len(df)}두 "
          f"(CCTV 신호 {signals.shape[1]-1}개 + 관리요인 결합)")

    y = df["anestrus"].astype(int).to_numpy()
    print(f"무발정/발정지연 {y.sum()}두 ({y.mean():.0%})")

    drop = {"anestrus", "individual_id"}
    feats = [c for c in df.columns if c not in drop]
    num = [c for c in feats if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in feats if c not in num]
    X = df[num + cat]

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    def evaluate(cols, title):
        pipe = train_mod.make_pipeline(
            [c for c in cols if c in num], [c for c in cols if c in cat],
            GradientBoostingClassifier(random_state=42))
        proba = cross_val_predict(pipe, df[cols], y, cv=cv,
                                  method="predict_proba")[:, 1]
        pred = (proba >= 0.5).astype(int)
        print(f"  {title:22s} AUC {roc_auc_score(y, proba):.3f} | "
              f"F1 {f1_score(y, pred):.3f} | 재현율 {recall_score(y, pred):.3f}"
              f" | 정밀도 {precision_score(y, pred):.3f}")
        return proba

    cctv_cols = [c for c in signals.columns if c != "individual_id"]
    mgmt_cols = [c for c in mgmt.columns if c not in drop]

    print("\n=== 무발정 위험 예측: 입력 구성별 비교 (5-fold) ===")
    evaluate(cctv_cols, "CCTV 신호만")
    evaluate(mgmt_cols, "관리요인만")
    proba = evaluate(num + cat, "CCTV + 관리요인(융합)")

    # 융합 모델 특성중요도
    pipe = train_mod.make_pipeline(
        num, cat, GradientBoostingClassifier(random_state=42))
    pipe.fit(X, y)
    train_mod.save_importances(pipe, num, cat, "pipeline_gilt")

    # 처방: CCTV로 무발정 위험 높다고 관찰된 개체 → 개선요인
    df = df.copy(); df["risk"] = proba
    print("\n=== CCTV 관찰 기반 위험 상위 개체 → 개선 처방 ===")
    for _, r in df.sort_values("risk", ascending=False).head(4).iterrows():
        flags = anestrus.prescribe(r)
        act = r.get("activity_mean", float("nan"))
        print(f"  {r['individual_id']} 위험 {r['risk']:.0%} "
              f"(활동량 {act:.1f}) → 개선: "
              f"{', '.join(flags) if flags else '관리요인 양호(질병력/성성숙 검토)'}")


def main() -> int:
    os.makedirs("yangdon/outputs", exist_ok=True)
    if len(sys.argv) >= 3 and os.path.isdir(sys.argv[1]):
        frames = parse_aihub.parse_71471(sys.argv[1])
        mgmt = pd.read_csv(sys.argv[2])
        print(f"실데이터: CCTV {sys.argv[1]} + 관리 {sys.argv[2]}")
    else:
        frames, mgmt = generate_joint()
        print("(합성 시연) CCTV 프레임 + 관리요인 조인트 생성 — "
              "실행: pipeline_gilt.py <cctv_dir> <mgmt.csv>")
    run(frames, mgmt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
