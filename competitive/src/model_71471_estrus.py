"""71471 발정 탐지(estrus detection) 모델.

발정은 시간에 걸친 행동·활동 변화로 나타난다. 따라서 프레임 단위 라벨을
**개체(individual_id) 단위로 집계**해 시계열/행동 피처를 만든 뒤 이진 분류한다.

집계 피처
  - 행동 분포: standing/lying/eating/tailing/sitting/head-shaking 비율
  - 활동량   : 프레임 간 중심(centroid) 이동 거리의 평균·표준편차
  - 자세     : bbox 종횡비·면적, keypoint 산포
개체당 1행 → StratifiedKFold 로 교차검증(AUC/F1/정밀도/재현율).

실데이터:
    python competitive/src/model_71471_estrus.py competitive/data/aihub/71471
없이 실행하면 문서 스키마대로 합성 라벨을 만들어 전체 흐름을 시연한다.
"""
from __future__ import annotations

import os
import sys
import tempfile

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (f1_score, precision_score, recall_score,
                             roc_auc_score)
from sklearn.model_selection import StratifiedKFold, cross_val_predict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parse_aihub  # noqa: E402
import train as train_mod  # noqa: E402

BEHAVIORS = ["standing", "lying", "eating", "head shaking", "tailing", "sitting"]


def build_estrus_features(frames: pd.DataFrame) -> pd.DataFrame:
    """프레임 테이블 → 개체 단위 피처 테이블."""
    rows = []
    for indiv, g in frames.groupby("individual_id"):
        g = g.sort_values("frame_idx")
        # 활동량: 연속 프레임 중심 이동거리
        dx = g["centroid_x"].astype(float).diff()
        dy = g["centroid_y"].astype(float).diff()
        disp = np.sqrt(dx ** 2 + dy ** 2).dropna()
        beh = g["behavior"].value_counts(normalize=True)

        row = {
            "individual_id": indiv,
            "species": g["species"].iloc[0],
            "n_frames": len(g),
            "activity_mean": float(disp.mean()) if len(disp) else 0.0,
            "activity_std": float(disp.std()) if len(disp) > 1 else 0.0,
            "activity_max": float(disp.max()) if len(disp) else 0.0,
            "aspect_mean": float(g["aspect_ratio"].astype(float).mean()),
            "bbox_area_mean": float((g["bbox_w"].astype(float)
                                     * g["bbox_h"].astype(float)).mean()),
            "kp_spread_mean": float(g["kp_spread"].astype(float).mean()),
            "estrus": int(g["estrus"].dropna().iloc[0])
            if g["estrus"].notna().any() else np.nan,
        }
        for b in BEHAVIORS:
            row[f"frac_{b.replace(' ', '_')}"] = float(beh.get(b, 0.0))
        rows.append(row)
    return pd.DataFrame(rows)


def load_frames(label_dir: str | None) -> pd.DataFrame:
    if label_dir and os.path.isdir(label_dir):
        df = parse_aihub.parse_71471(label_dir)
        print(f"실데이터 파싱: {label_dir} → 프레임 {len(df)}행")
    else:
        tmp = tempfile.mkdtemp()
        parse_aihub.generate_synthetic_71471(tmp, n_individuals=120, frames=20)
        df = parse_aihub.parse_71471(tmp)
        print(f"(합성 데이터 시연) 프레임 {len(df)}행 — "
              f"실행: model_71471_estrus.py <라벨디렉터리>")
    return df


def run(frames: pd.DataFrame) -> None:
    feat = build_estrus_features(frames)
    feat = feat[feat["estrus"].notna()].copy()
    print(f"개체 {len(feat)}두 | 발정 {int(feat['estrus'].sum())}두 "
          f"({feat['estrus'].mean():.0%})")
    if feat["estrus"].nunique() < 2 or len(feat) < 20:
        print("표본/클래스 부족 — 모델 학습 건너뜀")
        return

    y = feat["estrus"].astype(int).to_numpy()
    drop = {"estrus", "individual_id"}
    cols = [c for c in feat.columns if c not in drop]
    num = [c for c in cols if pd.api.types.is_numeric_dtype(feat[c])]
    cat = [c for c in cols if c not in num]
    X = feat[num + cat]

    pipe = train_mod.make_pipeline(
        num, cat, GradientBoostingClassifier(random_state=42))
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    proba = cross_val_predict(pipe, X, y, cv=cv, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)

    print("\n=== 발정 탐지 (개체 단위, StratifiedKFold) ===")
    print(f"  ROC-AUC   : {roc_auc_score(y, proba):.3f}")
    print(f"  F1        : {f1_score(y, pred):.3f}")
    print(f"  정밀도    : {precision_score(y, pred):.3f}")
    print(f"  재현율    : {recall_score(y, pred):.3f}")

    # 재현율 우선(발정 놓치면 21일 손실) — 임계값 낮춰 재현율↑ 예시
    for thr in (0.4, 0.3):
        p = (proba >= thr).astype(int)
        print(f"  [thr={thr}] 재현율 {recall_score(y, p):.3f} / "
              f"정밀도 {precision_score(y, p):.3f}")

    pipe.fit(X, y)
    train_mod.save_importances(pipe, num, cat, "71471_estrus")


def main() -> int:
    label_dir = sys.argv[1] if len(sys.argv) > 1 else None
    os.makedirs("competitive/outputs", exist_ok=True)
    run(load_frames(label_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
