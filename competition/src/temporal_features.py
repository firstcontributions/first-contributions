"""시간 윈도우 피처 — 행동 인식에 '최근 맥락'을 넣는다.

근거(실측): 정지 프레임 피처를 아무리 정교하게 해도 천장이 있다. 71471 에서
관절 44차원 자세 기술자(0.596)가 행동 라벨 4종(0.619)을 못 넘었다. 반대로 **모션**을
넣은 활동/휴식 판별은 0.739 로 확실히 높다. → **투자할 곳은 시간 축**이다.

현재 `add_motion()` 은 **직전 프레임 1개**만 본다(speed·accel·darea). 이 모듈은
개체별 시계열에 **롤링 윈도우 통계**를 붙인다:

  · 속도의 이동평균·표준편차·최대   (짧게 W1, 길게 W2)
  · 면적 변화의 이동평균·표준편차   (자세 전환 빈도)
  · 이동 누적거리 / 순변위 비율     (제자리 서성임 vs 직선 이동 구분)
  · 정지 비율(속도 임계 미만 프레임 비율)
  · 속도 추세(윈도우 내 선형 기울기) — 활동 증가/감소

'서성임(restless)'과 '직선 이동'은 순간 속도가 같아도 궤적이 다르다. 누적거리/
순변위 비율이 이를 가른다(발정 징후인 서성임 포착에 직접 관계).

    python competition/src/temporal_features.py [frames.csv]   # 유무 비교 평가
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

W1, W2 = 5, 15          # 짧은/긴 윈도우(프레임)
STILL_THR = 1.0         # 정지 판정 속도 임계(px/frame)

TEMPORAL_COLS = [
    "sp_mean5", "sp_std5", "sp_max5", "sp_mean15", "sp_std15", "sp_max15",
    "da_mean5", "da_std5", "path_ratio15", "still_frac15", "sp_trend15",
]


def add_temporal(df: pd.DataFrame, id_col: str = "individual_id") -> pd.DataFrame:
    """개체별 롤링 윈도우 피처 추가. speed/darea/centroid 가 있어야 한다."""
    need = {"speed", "centroid_x", "centroid_y"}
    if not need <= set(df.columns):
        raise ValueError(f"필요 컬럼 없음: {need - set(df.columns)}")
    d = df.sort_values([id_col, "frame_idx"]).copy()
    if "darea" not in d:
        d["darea"] = 0.0
    g = d.groupby(id_col, sort=False)

    def roll(col, w, fn):
        return g[col].transform(lambda s: s.rolling(w, min_periods=1).agg(fn))

    d["sp_mean5"] = roll("speed", W1, "mean")
    d["sp_std5"] = roll("speed", W1, "std")
    d["sp_max5"] = roll("speed", W1, "max")
    d["sp_mean15"] = roll("speed", W2, "mean")
    d["sp_std15"] = roll("speed", W2, "std")
    d["sp_max15"] = roll("speed", W2, "max")
    d["da_mean5"] = roll("darea", W1, "mean")
    d["da_std5"] = roll("darea", W1, "std")
    # 누적거리 / 순변위 — 서성임(제자리 맴돎)이면 크고, 직선 이동이면 1에 가깝다.
    # 주의: 정확히 제자리로 돌아오면 순변위가 0 이 된다. 이때는 비율이 **가장 커야**
    # 하므로(완전한 서성임), 0 을 결측 처리하면 안 된다 — 하한 1px 로 눌러 큰 값이
    # 나오게 한다.
    cum = g["speed"].transform(lambda s: s.rolling(W2, min_periods=1).sum())
    dx = g["centroid_x"].transform(lambda s: s - s.shift(W2 - 1))
    dy = g["centroid_y"].transform(lambda s: s - s.shift(W2 - 1))
    net = np.sqrt(dx.fillna(0) ** 2 + dy.fillna(0) ** 2).clip(lower=1.0)
    d["path_ratio15"] = (cum / net).clip(0, 20).fillna(0)
    # 정지 비율
    d["still_frac15"] = g["speed"].transform(
        lambda s: (s < STILL_THR).rolling(W2, min_periods=1).mean())
    # 속도 추세(윈도우 내 기울기)
    def slope(s):
        n = len(s)
        if n < 3:
            return 0.0
        x = np.arange(n)
        return float(np.polyfit(x, s.to_numpy(dtype=float), 1)[0])
    d["sp_trend15"] = g["speed"].transform(
        lambda s: s.rolling(W2, min_periods=3).apply(slope, raw=False))
    for c in TEMPORAL_COLS:
        d[c] = pd.to_numeric(d[c], errors="coerce").fillna(0.0)
    return d


def evaluate(frames_csv: str | None = None) -> dict:
    """시간 윈도우 피처 유무에 따른 행동 인식 성능 비교(개체 분리 GroupKFold)."""
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, f1_score
    from sklearn.model_selection import GroupKFold, cross_val_predict
    import model_edinburgh_behavior as beh
    df = (pd.read_csv(frames_csv) if frames_csv and os.path.isfile(frames_csv)
          else beh.load(None))
    df = beh.add_motion(df)
    df = add_temporal(df)
    vc = df["behavior"].value_counts()
    keep = set(vc[vc >= 150].index)
    df["behavior"] = df["behavior"].where(df["behavior"].isin(keep), "other")
    base = ["bbox_w", "bbox_h", "aspect_ratio", "area", "speed", "accel",
            "darea", "centroid_x", "centroid_y"]
    base = [c for c in base if c in df.columns]
    df = df.dropna(subset=base)
    y = df["behavior"].to_numpy(); g = df["individual_id"].to_numpy()

    def run(cols, tag):
        clf = RandomForestClassifier(n_estimators=250, min_samples_leaf=2,
                                     class_weight="balanced", n_jobs=-1,
                                     random_state=42)
        p = cross_val_predict(clf, df[cols], y, cv=GroupKFold(5), groups=g, n_jobs=-1)
        return {"tag": tag, "n_feat": len(cols),
                "acc": round(accuracy_score(y, p), 3),
                "mf1": round(f1_score(y, p, average="macro", zero_division=0), 3)}

    a = run(base, "기하+모션(기존)")
    b = run(base + TEMPORAL_COLS, "기하+모션+시간윈도우")
    return {"n": int(len(df)), "n_ind": int(df["individual_id"].nunique()),
            "before": a, "after": b,
            "d_acc": round(b["acc"] - a["acc"], 3),
            "d_mf1": round(b["mf1"] - a["mf1"], 3)}


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    r = evaluate(arg)
    print(f"프레임 {r['n']:,} · 개체 {r['n_ind']} · 개체 분리 GroupKFold(5)")
    for k in ("before", "after"):
        x = r[k]
        print(f"  {x['tag']:24s} 피처 {x['n_feat']:3d}  정확도 {x['acc']}  Macro-F1 {x['mf1']}")
    print(f"  → 정확도 {r['d_acc']:+.3f} · Macro-F1 {r['d_mf1']:+.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
