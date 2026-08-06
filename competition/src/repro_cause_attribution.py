"""번식 문제 유형 분류 + 원인 귀인(cause attribution).

블랙박스 무발정 확률 하나를, 농장이 바로 행동할 수 있는 구조로 바꾼다:

  문제 유형(3종) — 관찰(CCTV)로 구분
    · 이유후 발정지연 : 초교배/이유 후 목표일 지났는데 발정 늦음(타이밍 문제)
    · 무발정          : 발정 징후가 사실상 없음(활동↓·기립/꼬리세움 거의 0)
    · 미약(둔성) 발정 : 징후는 있으나 약해 육안 관찰이 놓치기 쉬움 → CCTV 최대 가치

  원인(4종) — 관리/환경 요인으로 귀인
    · 영양 부족        : 등지방(성성숙)·사료 적정도
    · 더위 스트레스    : 기온·습도(THI)
    · 수퇘지 자극 부족 : 일일 웅돈 접촉 시간
    · 사양 관리 불량   : 시설·음수·암모니아·질병 이력

수의학 근거로 각 요인의 '나쁜 방향·임계·기여 가중'을 인코딩한다(recalibratable).
71471/71763 실데이터가 오면 가중치를 지도학습으로 교체할 수 있게 구조를 맞춘다.

    python competition/src/repro_cause_attribution.py   # 합성 시연
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

# 원인 4종: 각 요인의 (나쁜 방향, 임계, 포화 스케일, 가중). severity 0~1.
#   bad="low": 임계 미만이 문제,  bad="high": 임계 초과가 문제
CAUSE_GROUPS = {
    "영양 부족": [
        ("backfat_mm", "low", 12.0, 4.0, 1.0),      # 성성숙 지표
        ("feed_adequacy", "low", 0.6, 0.4, 0.8),
    ],
    "더위 스트레스": [
        ("thi", "high", 74.0, 12.0, 1.0),           # THI 74↑ 경증, 78↑ 중등
    ],
    "수퇘지 자극 부족": [
        ("boar_exposure_min", "low", 10.0, 10.0, 1.0),
    ],
    "사양 관리 불량": [
        ("facility_score", "low", 0.6, 0.4, 0.7),
        ("water_adequacy", "low", 0.6, 0.4, 0.6),
        ("nh3_ppm", "high", 25.0, 20.0, 0.5),
        ("growth_disease_cnt", "high", 2.0, 4.0, 0.6),
    ],
}

PROBLEMS = ["정상", "이유후 발정지연", "무발정", "미약(둔성) 발정"]


def thi(temp_c: float, humidity_pct: float) -> float:
    """돼지 온습도지수(THI). 74↑ 경증·78↑ 중등·82↑ 심각 열스트레스."""
    rh = float(humidity_pct) / 100.0
    return 0.8 * float(temp_c) + rh * (float(temp_c) - 14.4) + 46.4


def _severity(value: float, bad: str, thr: float, scale: float) -> float:
    """요인 하나의 문제 심각도 0~1(임계 초과분을 스케일로 포화)."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return 0.0
    dev = (thr - value) if bad == "low" else (value - thr)
    return float(np.clip(dev / scale, 0.0, 1.0))


def attribute(row) -> dict:
    """개체 한 마리 → 원인별 심각도(0~1)와 기여 비율.

    반환: {"severity": {원인:0~1}, "share": {원인:비율}, "top": (원인, 심각도)}
    """
    r = dict(row)
    if "thi" not in r and "temp_c" in r and "humidity_pct" in r:
        r["thi"] = thi(r["temp_c"], r["humidity_pct"])
    sev = {}
    for cause, feats in CAUSE_GROUPS.items():
        s = 0.0
        for feat, bad, thr, scale, w in feats:
            s += w * _severity(r.get(feat), bad, thr, scale)
        total_w = sum(w for *_, w in feats)
        sev[cause] = round(s / total_w, 3) if total_w else 0.0
    tot = sum(sev.values())
    share = {c: round(v / tot, 3) for c, v in sev.items()} if tot > 0 else \
        {c: 0.0 for c in sev}
    top = max(sev.items(), key=lambda kv: kv[1]) if tot > 0 else ("원인 불명확", 0.0)
    return {"severity": sev, "share": share, "top": top}


def signal_context(df: pd.DataFrame) -> dict:
    """개체군에서 활동·발정징후의 상대 분위수 컷을 산출(스케일 무관 판정용)."""
    act = df["activity_mean"].astype(float) if "activity_mean" in df else pd.Series(dtype=float)
    sign = (df.get("frac_standing", 0.0).astype(float)
            + df.get("frac_tailing", 0.0).astype(float)) if "frac_standing" in df else pd.Series(dtype=float)
    q = lambda s, p: float(np.percentile(s, p)) if len(s) else np.nan
    return {"act_lo": q(act, 30), "act_verylo": q(act, 12),
            "sign_lo": q(sign, 30), "sign_verylo": q(sign, 12),
            "act_hi": q(act, 55), "sign_ok": q(sign, 60)}


def classify_problem(row, risk: float, ctx: dict | None = None) -> str:
    """CCTV 관찰 신호 + 위험도 → 문제 유형(3종+정상).

    ctx(signal_context)를 주면 개체군 상대 분위수로 판정(농장·카메라 스케일 무관).
    없으면 활동은 activity_norm(0~1) 또는 절대 임계로 대체.
    - 위험 낮고 징후 뚜렷 → 정상
    - 활동 최하위·징후 최하위 → 무발정(징후 자체가 사실상 없음)
    - 징후 약함(활동 중하·기립/꼬리 미약) → 미약(둔성) 발정
    - 목표일령 크게 초과인데 위험 있음 → 이유후 발정지연(타이밍)
    """
    r = dict(row)
    act = float(r.get("activity_mean", np.nan))
    sign = float(r.get("frac_standing", 0.0)) + float(r.get("frac_tailing", 0.0))
    age_over = float(r.get("age_over_target", 0.0))
    if ctx:
        act_ok = np.isnan(act) or act >= ctx["act_hi"]
        low = (not np.isnan(act)) and act < ctx["act_lo"]
        verylow = (not np.isnan(act)) and act < ctx["act_verylo"]
        sign_weak = sign < ctx["sign_lo"]
        sign_absent = sign < ctx["sign_verylo"]
        sign_clear = sign >= ctx["sign_ok"]
    else:
        an = (float(r["activity_norm"]) if "activity_norm" in r
              and not pd.isna(r["activity_norm"])
              else (np.nan if np.isnan(act) else float(np.clip(act / 30.0, 0, 1))))
        act_ok = np.isnan(an) or an >= 0.45
        low = (not np.isnan(an)) and an < 0.30
        verylow = (not np.isnan(an)) and an < 0.18
        sign_weak = sign < 0.20
        sign_absent = sign < 0.12
        sign_clear = sign >= 0.22
    if risk < 0.4 and act_ok and sign_clear:
        return "정상"
    if verylow and sign_absent:
        return "무발정"
    if age_over > 12 and not sign_absent:
        return "이유후 발정지연"
    if low or sign_weak:
        return "미약(둔성) 발정"
    if age_over > 8:
        return "이유후 발정지연"
    return "미약(둔성) 발정"


# 원인별 표준 처방(현장 조치)
PRESCRIPTION = {
    "영양 부족": "플러싱(발정 2주 전 증량 급여)·에너지 강화, 등지방 14mm 목표",
    "더위 스트레스": "쿨링(송풍·점적)·환기 강화, 사료 급여시간 서늘한 때로 이동",
    "수퇘지 자극 부족": "성숙 웅돈 1일 2회·10분↑ 직접 대면 노출(격리사육 지양)",
    "사양 관리 불량": "시설(바닥·채광)·음수 점검, 암모니아 25ppm↓ 환기, 질병 이력 관리",
}


def diagnose(row, risk: float, ctx: dict | None = None) -> dict:
    """개체 종합 진단: 문제 유형 + 주원인 + 처방."""
    a = attribute(row)
    problem = classify_problem(row, risk, ctx)
    cause, sev = a["top"]
    return {"problem": problem, "cause": cause, "cause_severity": sev,
            "share": a["share"],
            "action": PRESCRIPTION.get(cause, "질병력·성성숙(등지방) 정밀 검토")}


def run_demo() -> None:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import pipeline_gilt
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.model_selection import StratifiedKFold, cross_val_predict
    import train as train_mod

    frames, mgmt = pipeline_gilt.generate_joint(n_gilts=400)
    signals = pipeline_gilt.build_cctv_signals(frames)
    df = mgmt.merge(signals, on="individual_id", how="inner")
    y = df["anestrus"].astype(int).to_numpy()
    drop = {"anestrus", "individual_id", "farm"}
    feats = [c for c in df.columns if c not in drop]
    num = [c for c in feats if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in feats if c not in num]
    pipe = train_mod.make_pipeline(num, cat, GradientBoostingClassifier(random_state=42))
    cv = StratifiedKFold(5, shuffle=True, random_state=42)
    df = df.copy()
    df["risk"] = cross_val_predict(pipe, df[num + cat], y, cv=cv,
                                   method="predict_proba")[:, 1]
    # 개체군 상대 분위수 컨텍스트(스케일 무관 판정)
    ctx = signal_context(df)

    # 문제 유형 분포
    df["problem"] = [classify_problem(r, r["risk"], ctx) for _, r in df.iterrows()]
    print("=== 번식 문제 유형 분포(관찰+위험 기반) ===")
    for p in PROBLEMS:
        n = int((df["problem"] == p).sum())
        print(f"  {p:14s} {n:3d}두 ({n/len(df):.0%})")

    # 위험 상위 개체 종합 진단
    print("\n=== 위험 상위 5두 종합 진단(문제유형 · 주원인 · 처방) ===")
    for _, r in df.sort_values("risk", ascending=False).head(5).iterrows():
        d = diagnose(r, r["risk"], ctx)
        print(f"  {r['individual_id']} 위험 {r['risk']:.0%} | {d['problem']:14s}"
              f" | 주원인 {d['cause']}({d['cause_severity']:.0%}) → {d['action']}")

    # 원인별 평균 기여(전 개체)
    print("\n=== 무발정 위험군 원인 기여 평균 ===")
    hi = df[df["risk"] >= 0.5]
    if len(hi):
        agg = {c: np.mean([attribute(r)["share"][c] for _, r in hi.iterrows()])
               for c in CAUSE_GROUPS}
        for c, v in sorted(agg.items(), key=lambda kv: -kv[1]):
            print(f"  {c:14s} 기여 {v:.0%}")


if __name__ == "__main__":
    run_demo()
