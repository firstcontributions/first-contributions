"""교차 데이터셋 자세 검증 도구.

목적: 행동/자세 라벨로 **학습한 모델**을, 독립된 **Kaggle 대회
'multi-view-pig-posture-recognition'** 데이터로 검증한다(일반화 성능).

  학습 소스(자세 라벨 보유):
    - 기본: Edinburgh 실데이터(behavior)   [원격에서 가능]
    - 대체: AI Hub 71471 파싱 프레임 CSV(behavior)  [국내 로컬에서]
  검증 타깃:
    - 대회 데이터(bbox → 자세 5클래스)

공통 자세공간으로 매핑: {standing, sitting, lying}
  대회:   Standing→standing, Sitting→sitting,
          Lateral_lying_left/right·Sternal_lying → lying
  행동:   standing→standing, sitting→sitting, lying·sleep → lying (그 외 제외)

교차 데이터셋 비교 가능한 척도로 스케일/해상도 불변 피처만 사용:
  - aspect_ratio = w/h
  - area_pct     = 데이터셋 내 bbox 면적 백분위(0~1)

사용:
  python yangdon/src/posture_eval.py                  # 소스=Edinburgh
  python yangdon/src/posture_eval.py <frames.csv>     # 소스=AI Hub 등 behavior CSV
"""
from __future__ import annotations

import ast
import os
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, f1_score

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parse_edinburgh  # noqa: E402

COMMON = ["standing", "sitting", "lying"]

BEHAVIOR_TO_COMMON = {
    "standing": "standing", "sitting": "sitting",
    "lying": "lying", "sleep": "lying",
}
COMP_TO_COMMON = {
    "Standing": "standing", "Sitting": "sitting",
    "Lateral_lying_left": "lying", "Lateral_lying_right": "lying",
    "Sternal_lying": "lying",
}


def _feats(w, h, area):
    w = np.asarray(w, dtype=float); h = np.asarray(h, dtype=float)
    aspect = w / h
    area_pct = pd.Series(np.asarray(area, dtype=float)).rank(pct=True).to_numpy()
    return np.column_stack([aspect, area_pct])


def load_competition(path: str | None) -> pd.DataFrame:
    if not path:
        import kagglehub
        base = kagglehub.competition_download("multi-view-pig-posture-recognition")
        path = os.path.join(base, "multiview_pig_posture_recognition")
    frames = []
    classes = open(os.path.join(path, "pig_posture_classes.txt")).read().split()
    for f in ("train1.csv", "train2.csv"):
        df = pd.read_csv(os.path.join(path, f))
        bb = df["bbox"].apply(ast.literal_eval)
        df["w"] = bb.apply(lambda b: b[2]); df["h"] = bb.apply(lambda b: b[3])
        df["posture"] = df["class_id"].apply(lambda i: COMP_TO_COMMON[classes[i]])
        df["split"] = f
        frames.append(df[["w", "h", "posture", "split"]])
    return pd.concat(frames, ignore_index=True)


def load_source(arg: str | None) -> pd.DataFrame:
    if arg and os.path.isfile(arg):
        df = pd.read_csv(arg)
    else:
        root = arg if (arg and os.path.isdir(arg)) else "yangdon/data/edinburgh"
        df = parse_edinburgh.parse_edinburgh(root)
    df = df[df["behavior"].isin(BEHAVIOR_TO_COMMON)].copy()
    df["posture"] = df["behavior"].map(BEHAVIOR_TO_COMMON)
    df = df.dropna(subset=["bbox_w", "bbox_h"])
    df = df.rename(columns={"bbox_w": "w", "bbox_h": "h"})
    return df[["w", "h", "posture"]]


def evaluate(src: pd.DataFrame, comp: pd.DataFrame) -> None:
    Xs = _feats(src["w"].to_numpy(), src["h"].to_numpy(), (src["w"] * src["h"]).to_numpy())
    ys = src["posture"].to_numpy()
    Xt = _feats(comp["w"].to_numpy(), comp["h"].to_numpy(), (comp["w"] * comp["h"]).to_numpy())
    yt = comp["posture"].to_numpy()

    print(f"학습 소스: {len(src)}행  분포={dict(pd.Series(ys).value_counts())}")
    print(f"검증 타깃(대회): {len(comp)}행  분포={dict(pd.Series(yt).value_counts())}")

    clf = RandomForestClassifier(n_estimators=200, min_samples_leaf=5,
                                 class_weight="balanced", random_state=42, n_jobs=-1)
    clf.fit(Xs, ys)
    pred = clf.predict(Xt)
    print("\n=== 교차 데이터셋 검증 (소스 학습 → 대회 평가) ===")
    print(f"  정확도 {(pred==yt).mean():.3f} | Macro-F1 "
          f"{f1_score(yt,pred,average='macro',labels=COMMON,zero_division=0):.3f}")
    print(classification_report(yt, pred, labels=COMMON, zero_division=0, digits=3))

    # 참고: 대회 내부 학습(천장) — train1→train2
    if "split" in comp:
        tr = comp[comp["split"] == "train1.csv"]; te = comp[comp["split"] == "train2.csv"]
        if len(tr) and len(te):
            Xtr = _feats(tr["w"].to_numpy(), tr["h"].to_numpy(), (tr["w"]*tr["h"]).to_numpy())
            Xte = _feats(te["w"].to_numpy(), te["h"].to_numpy(), (te["w"]*te["h"]).to_numpy())
            c2 = RandomForestClassifier(n_estimators=200, min_samples_leaf=5,
                                        class_weight="balanced", random_state=42, n_jobs=-1)
            c2.fit(Xtr, tr["posture"]); p2 = c2.predict(Xte)
            print(f"[참고] 대회 내부(train1→train2) 정확도 {(p2==te['posture']).mean():.3f} "
                  f"| Macro-F1 {f1_score(te['posture'],p2,average='macro',labels=COMMON,zero_division=0):.3f}")
            print("  → 소스 학습 결과가 이 천장에 얼마나 근접하는지가 일반화 지표")


def main() -> int:
    src_arg = sys.argv[1] if len(sys.argv) > 1 else None
    comp_arg = sys.argv[2] if len(sys.argv) > 2 else None
    src = load_source(src_arg)
    comp = load_competition(comp_arg)
    evaluate(src, comp)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
