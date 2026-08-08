"""멀티뷰 자세 인식 — 뷰 정합(view alignment) 전/후 정확도 비교.

이 대회는 test 세트가 train에 없는 카메라 뷰로 구성된 **교차-뷰 일반화** 과제다.
라벨이 있는 train1+train2에서 test와 같은 뷰들을 held-out 으로 떼어, 뷰 정합
전/후 성능을 정직하게 비교한다.

뷰 정합 = 카메라별 시점 차이를 없애기 위해 기하 피처를 **뷰 단위로 정규화**:
  - aspect_z  : 뷰 내 aspect(w/h) z-점수 (뷰별 평균/표준편차 제거)
  - area_pct_v: 뷰 내 면적 백분위
(라벨을 쓰지 않는 무감독 정규화 — 누수 아님)

    python competition/src/view_align.py [대회경로]
"""
from __future__ import annotations

import ast
import os
import re
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

HELD_OUT_VIEWS = {"pen2_tur_cam2", "pen1_tur_cam1", "pen2_orb_cam2"}  # test 뷰


def load(path: str | None) -> pd.DataFrame:
    if not path:
        import kagglehub
        base = kagglehub.competition_download("multi-view-pig-posture-recognition")
        path = os.path.join(base, "multiview_pig_posture_recognition")
    classes = open(os.path.join(path, "pig_posture_classes.txt")).read().split()
    dfs = []
    for f in ("train1.csv", "train2.csv"):
        d = pd.read_csv(os.path.join(path, f))
        dfs.append(d)
    df = pd.concat(dfs, ignore_index=True)
    bb = df["bbox"].apply(ast.literal_eval)
    df["w"] = bb.apply(lambda b: b[2]); df["h"] = bb.apply(lambda b: b[3])
    df["aspect"] = df["w"] / df["h"]
    df["area"] = df["w"] * df["h"]
    df["view"] = df["image_id"].str.extract(r'(pen\d+_[a-z]+_cam\d+)')[0]
    df["cls"] = df["class_id"].apply(lambda i: classes[i])
    return df


def baseline_feats(df: pd.DataFrame) -> np.ndarray:
    area_pct = df["area"].rank(pct=True).to_numpy()
    return np.column_stack([df["aspect"].to_numpy(), area_pct])


def view_aligned_feats(df: pd.DataFrame) -> np.ndarray:
    g = df.groupby("view")
    aspect_z = g["aspect"].transform(lambda s: (s - s.mean()) / (s.std() or 1))
    area_pct_v = g["area"].transform(lambda s: s.rank(pct=True))
    return np.column_stack([aspect_z.to_numpy(), area_pct_v.to_numpy()])


def run(df: pd.DataFrame) -> None:
    test_mask = df["view"].isin(HELD_OUT_VIEWS)
    tr, te = df[~test_mask], df[test_mask]
    print(f"학습(그 외 뷰) {len(tr)}행 | 검증(held-out 뷰 {sorted(HELD_OUT_VIEWS)}) {len(te)}행")
    print(f"검증 뷰 분포: {dict(te['view'].value_counts())}")

    def fit_eval(feat_fn, title):
        X = feat_fn(df)                       # 정규화는 전체(뷰별)로 계산
        clf = RandomForestClassifier(n_estimators=300, min_samples_leaf=3,
                                     class_weight="balanced", random_state=42, n_jobs=-1)
        clf.fit(X[~test_mask.to_numpy()], tr["cls"])
        pred = clf.predict(X[test_mask.to_numpy()])
        acc = accuracy_score(te["cls"], pred)
        mf1 = f1_score(te["cls"], pred, average="macro", zero_division=0)
        print(f"  {title:16s} 정확도 {acc:.3f} | Macro-F1 {mf1:.3f}")
        return acc, mf1

    print("\n=== 교차-뷰 검증: 뷰 정합 전/후 ===")
    b = fit_eval(baseline_feats, "뷰 정합 전")
    a = fit_eval(view_aligned_feats, "뷰 정합 후")
    print(f"\n  변화: 정확도 {b[0]:.3f} → {a[0]:.3f} ({a[0]-b[0]:+.3f}) | "
          f"Macro-F1 {b[1]:.3f} → {a[1]:.3f} ({a[1]-b[1]:+.3f})")


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else None
    run(load(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
