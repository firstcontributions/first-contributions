"""행동 → 발정 연계 (behavior-to-estrus linkage).

발정(heat)은 행동으로 나타난다(수의학적 근거):
  - 승가(mounting) 시도                     ← 가장 강한 행동 신호
  - 활동량 증가(서성임·보행·달리기)          ← restlessness
  - 탐색·사회적 접촉 증가(냄새맡기, 코-코)    ← 후각/사회 관심
  - 눕기·수면 등 휴식 감소

정답 발정 라벨이 없는 실데이터(Edinburgh)에서는 도메인 가중치로 **행동 기반
발정 의심 지수**(0~1)를 산출한다. 발정 정답(estrus)이 있는 데이터(AI Hub 71471)
에서는 로지스틱 회귀로 지도 보정하고 AUC 를 보고한다(연계의 타당성 검증).

    python competitive/src/estrus_link.py [frames.csv|라벨디렉터리]
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model_71471_estrus as est  # build_estrus_features 재사용

# 행동별 발정 연관 가중치(+ 발정 시사, - 휴식). Edinburgh·71471 어휘 모두 포함.
ESTRUS_WEIGHT = {
    "jumpontopof": 1.0, "mounting": 1.0,      # 승가 = 최강 신호
    "tailing": 0.6,                            # 꼬리세움(71471)
    "run": 0.6, "chase": 0.5, "walk": 0.4,     # 활동성
    "investigating": 0.35, "nose-to-nose": 0.35, "nose-poke-elsewhere": 0.2,
    "fight": 0.2, "standing": 0.15, "playwithtoy": 0.1,
    "eat": -0.1, "eating": -0.1, "drink": 0.0,
    "sitting": -0.3, "lying": -0.5, "sleep": -0.6,
}
ACTIVITY_W = 0.5   # 활동량(정규화) 기여


def behavior_estrus_index(frames: pd.DataFrame) -> pd.DataFrame:
    """개체별 행동 구성 + 활동량 → 발정 의심 지수(0~1).

    frames: 프레임 단위(individual_id, frame_idx, behavior, centroid_x/y ...).
    데이터셋의 모든 행동을 반영한다(71471 6종에 국한하지 않음).
    """
    # 활동량은 기존 집계 재사용(individual_id 기준)
    feat = est.build_estrus_features(frames)[["individual_id", "activity_mean",
                                              "activity_std", "activity_max"]]
    feat = feat.set_index("individual_id")
    a = feat["activity_mean"].to_numpy(dtype=float)
    a_norm = (a - a.min()) / ((a.max() - a.min()) or 1)
    feat["activity_norm"] = np.round(a_norm, 3)

    # 모든 행동의 개체별 비율(전체 어휘)
    bf = (frames.groupby("individual_id")["behavior"]
          .value_counts(normalize=True).unstack(fill_value=0.0))
    bf = bf.reindex(feat.index).fillna(0.0)

    raw = ACTIVITY_W * a_norm.copy()
    contrib = pd.DataFrame(0.0, index=feat.index, columns=list(ESTRUS_WEIGHT))
    for b, w in ESTRUS_WEIGHT.items():
        if b in bf.columns:
            c = bf[b].to_numpy() * w
            raw += c
            contrib[b] = c

    idx = (raw - raw.min()) / ((raw.max() - raw.min()) or 1)
    feat["estrus_index"] = np.round(idx, 3)

    # 개체별 발정 기여 상위 행동(양의 기여만)
    drivers = []
    for iid in feat.index:
        row = contrib.loc[iid]
        pos = row[row > 0.02].sort_values(ascending=False)
        drivers.append(", ".join(pos.index[:3]) if len(pos) else "-")
    feat["estrus_drivers"] = drivers
    return feat.reset_index().sort_values("estrus_index", ascending=False)


def supervised_calibrate(frames: pd.DataFrame) -> None:
    """발정 정답(estrus)이 있으면 지도 보정 + AUC 로 연계 타당성 검증."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import cross_val_predict

    feat = est.build_estrus_features(frames)
    if "estrus" not in feat or feat["estrus"].notna().sum() < 20 \
            or feat["estrus"].nunique() < 2:
        print("발정 정답 없음 → 지도 보정 생략(규칙 기반 지수만 사용)")
        return
    y = feat["estrus"].astype(int).to_numpy()
    fcols = [c for c in feat.columns if c.startswith("frac_")] + \
            ["activity_mean", "activity_std", "activity_max"]
    X = feat[fcols].fillna(0).to_numpy()
    clf = LogisticRegression(max_iter=1000, class_weight="balanced")
    proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    print(f"[지도 보정] 행동→발정 로지스틱 AUC {roc_auc_score(y, proba):.3f} "
          f"(개체 {len(y)}, 발정 {y.mean():.0%}) — 행동으로 발정 예측 타당성")


def load(arg):
    if arg and os.path.isfile(arg):
        return pd.read_csv(arg)
    import parse_edinburgh
    root = arg if (arg and os.path.isdir(arg)) else "competitive/data/edinburgh"
    return parse_edinburgh.parse_edinburgh(root)


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else "competitive/data/edinburgh_frames.csv"
    frames = load(arg)
    res = behavior_estrus_index(frames)
    n_hi = int((res["estrus_index"] >= 0.6).sum())
    print(f"개체 {len(res)}두 | 발정 의심(지수≥0.6) {n_hi}두\n")
    print("=== 발정 의심 상위 8두 ===")
    cols = ["individual_id", "estrus_index", "activity_norm", "estrus_drivers"]
    print(res[cols].head(8).to_string(index=False))
    print("\n=== 하위 4두(휴식 위주) ===")
    print(res[cols].tail(4).to_string(index=False))
    supervised_calibrate(frames)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
