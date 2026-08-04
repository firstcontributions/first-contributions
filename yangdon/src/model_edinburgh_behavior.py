"""Edinburgh 실데이터 — 돼지 행동 인식 모델.

bbox 시계열에서 모션 피처(속도·가속도·면적변화)를 만들어 프레임 단위 행동을
분류한다. 같은 개체가 train/test에 섞이지 않도록 GroupKFold(individual_id).

행동은 발정 관찰의 기반 신호다: 활동(walk/run/investigating)↑·정지(lying/
sleep)↓ 패턴, 승가(jumpontopof) 등은 번식행동 지표로 이어진다.

    python yangdon/src/model_edinburgh_behavior.py [frames.csv 또는 라벨디렉터리]
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import GroupKFold, cross_val_predict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parse_edinburgh  # noqa: E402

MIN_COUNT = 100      # 이보다 적은 행동은 'other'로 통합


def add_motion(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["individual_id", "frame_idx"]).copy()
    g = df.groupby("individual_id")
    df["area"] = df["bbox_w"] * df["bbox_h"]
    dx = g["centroid_x"].diff()
    dy = g["centroid_y"].diff()
    step = g["frame_idx"].diff().replace(0, 1)
    df["speed"] = (np.sqrt(dx ** 2 + dy ** 2) / step).fillna(0)
    df["accel"] = g_apply_diff(df, "speed").fillna(0)
    df["darea"] = (g["area"].diff() / step).fillna(0)
    return df


def g_apply_diff(df: pd.DataFrame, col: str) -> pd.Series:
    return df.groupby("individual_id")[col].diff()


def load(arg: str | None) -> pd.DataFrame:
    if arg and os.path.isfile(arg):
        return pd.read_csv(arg)
    root = arg if (arg and os.path.isdir(arg)) else "yangdon/data/edinburgh"
    return parse_edinburgh.parse_edinburgh(root)


def run(df: pd.DataFrame) -> None:
    df = df[df["behavior"].notna() & df["centroid_x"].notna()].copy()
    # 희소 행동 통합
    vc = df["behavior"].value_counts()
    keep = set(vc[vc >= MIN_COUNT].index)
    df["behavior"] = df["behavior"].where(df["behavior"].isin(keep), "other")
    df = add_motion(df)

    feats = ["bbox_w", "bbox_h", "aspect_ratio", "area",
             "speed", "accel", "darea", "centroid_x", "centroid_y"]
    df = df.dropna(subset=feats)
    X = df[feats].to_numpy()
    y = df["behavior"].to_numpy()
    groups = df["individual_id"].to_numpy()
    print(f"프레임 {len(df)} | 개체 {df['individual_id'].nunique()} | "
          f"행동 {df['behavior'].nunique()}종")
    print("클래스:", ", ".join(sorted(set(y))))

    clf = RandomForestClassifier(n_estimators=250, min_samples_leaf=2,
                                 class_weight="balanced", n_jobs=-1,
                                 random_state=42)
    cv = GroupKFold(n_splits=5)
    pred = cross_val_predict(clf, X, y, cv=cv, groups=groups, n_jobs=-1)

    acc = (pred == y).mean()
    macro = f1_score(y, pred, average="macro")
    print(f"\n=== 행동 인식 (GroupKFold, 개체 분리) ===")
    print(f"  정확도 {acc:.3f} | Macro-F1 {macro:.3f}")
    print("\n" + classification_report(y, pred, zero_division=0, digits=3))

    clf.fit(X, y)
    imp = pd.Series(clf.feature_importances_, index=feats).sort_values(ascending=False)
    print("특성 중요도:\n" + imp.round(3).to_string())
    os.makedirs("yangdon/outputs", exist_ok=True)
    imp.round(4).to_csv("yangdon/outputs/importance_edinburgh_behavior.csv",
                        header=["importance"], encoding="utf-8-sig")


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    run(load(arg))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
