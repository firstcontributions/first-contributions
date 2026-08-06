"""발정 실측 검증 — 71471 발정 정답으로 EstrusReference 를 보정·평가.

핵심 공백을 메운다: 지금까지 발정 점수는 규칙(수의학 가중치)일 뿐, **발정 정답으로
검증한 실측 AUC** 가 없었다. 이 모듈이 그 다리다.

  71471 라벨(발정 정답) → 개체 단위 (표준 카테고리 비율 + 활동량) → estrus 0/1
    → EstrusReference.calibrate() → 실측 발정 AUC/ROC/PR/보정곡선

데이터 위치(우선순위):
  1) $AIHUB_71471_DIR  (환경변수로 라벨 디렉터리 지정)
  2) competition/data/aihub/71471  (국내망에서 받아 놓은 실파일)
  3) 없으면 → 합성 시연(is_real=False). 실측이 아님을 명시.

71471 은 국내 IP 전용이라 이 원격 환경에서는 직접 못 받는다. 국내망에서 라벨
파일(bbox/keypoints, 수십 MB)만 받아 위 경로에 두면, 아래가 자동으로 실측 AUC 를
채운다(build_eval_report.py 의 D 섹션). 그 전까지는 규칙 baseline 만 보고한다.

    python competition/src/validate_estrus_reference.py [라벨디렉터리]
"""
from __future__ import annotations

import os
import sys
import tempfile

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import aihub_estrus_reference as ref  # noqa: E402
import parse_aihub  # noqa: E402

REAL_DIR = os.path.join(ROOT, "competition", "data", "aihub", "71471")


def resolve_dir(arg: str | None) -> str | None:
    """실데이터 라벨 디렉터리를 찾는다(없으면 None)."""
    for cand in (arg, os.environ.get("AIHUB_71471_DIR"), REAL_DIR):
        if cand and os.path.isdir(cand):
            return cand
    return None


def load_frames(arg: str | None):
    """(frames, is_real) 반환. 실파일 없으면 합성 시연으로 대체."""
    d = resolve_dir(arg)
    if d:
        df = parse_aihub.parse_71471(d)
        if len(df) and df["estrus"].notna().any():
            return df, True
    tmp = tempfile.mkdtemp()
    parse_aihub.generate_synthetic_71471(tmp, n_individuals=140, frames=22)
    return parse_aihub.parse_71471(tmp), False


def to_individual_table(frames: pd.DataFrame) -> pd.DataFrame:
    """프레임 → 개체 단위: 표준 카테고리 비율 + 활동량(0~1) + estrus.

    반환 컬럼: individual_id, estrus, activity_norm, 그리고 표준 카테고리별 비율.
    활동량은 전체 개체의 95퍼센타일로 정규화(이상치 완화, 0~1 clip).
    """
    rows = []
    for indiv, g in frames.groupby("individual_id"):
        g = g.sort_values("frame_idx")
        dx = g["centroid_x"].astype(float).diff()
        dy = g["centroid_y"].astype(float).diff()
        disp = np.sqrt(dx ** 2 + dy ** 2).dropna()
        beh_frac = g["behavior"].value_counts(normalize=True).to_dict()
        ref_frac = ref.map_fractions(beh_frac)   # 표준 카테고리로 합산
        est = (int(g["estrus"].dropna().iloc[0])
               if g["estrus"].notna().any() else np.nan)
        row = {"individual_id": indiv, "estrus": est,
               "_activity_raw": float(disp.mean()) if len(disp) else 0.0}
        for c in ref.REFERENCE_BEHAVIORS:
            row[c] = float(ref_frac.get(c, 0.0))
        rows.append(row)
    tbl = pd.DataFrame(rows)
    scale = np.percentile(tbl["_activity_raw"], 95) or 1.0
    tbl["activity_norm"] = (tbl["_activity_raw"] / scale).clip(0, 1)
    return tbl.drop(columns="_activity_raw")


def evaluate(arg: str | None = None) -> dict:
    """실측(또는 시연) 발정 검증 결과 dict.

    반환: is_real, n, pos_rate, auc_calibrated(지도 보정 AUC),
          auc_rule(규칙 점수만으로의 AUC — baseline), rows(개체표).
    """
    from sklearn.metrics import roc_auc_score
    frames, is_real = load_frames(arg)
    tbl = to_individual_table(frames)
    tbl = tbl[tbl["estrus"].notna()].copy()
    y = tbl["estrus"].astype(int).to_numpy()
    out = {"is_real": is_real, "n": int(len(tbl)),
           "pos_rate": round(float(y.mean()), 3) if len(y) else 0.0,
           "auc_calibrated": None, "auc_rule": None}
    if len(tbl) < 20 or len(set(y)) < 2:
        out["note"] = "표본 부족/단일 클래스 — 검증 불가"
        return out
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_predict
    ref_rows = tbl[ref.REFERENCE_BEHAVIORS].to_dict("records")
    act = tbl["activity_norm"].to_numpy()
    R = ref.EstrusReference()
    out["auc_calibrated"] = round(R.calibrate(ref_rows, act, y), 3)
    # 곡선용: 동일 보정모델의 개체 분리 없는 5-fold 확률(리포트 ROC/PR/보정)
    X = np.array([[r.get(c, 0.0) for c in ref.REFERENCE_BEHAVIORS] + [a]
                  for r, a in zip(ref_rows, act)])
    clf = LogisticRegression(max_iter=1000, class_weight="balanced")
    out["proba"] = cross_val_predict(clf, X, y, cv=5,
                                     method="predict_proba")[:, 1]
    out["y"] = y
    # 규칙(무학습) baseline: 표준 가중치 점수의 AUC
    rule = np.array([R.score(r, a) for r, a in zip(ref_rows, act)])
    out["auc_rule"] = round(float(roc_auc_score(y, rule)), 3)
    return out


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    r = evaluate(arg)
    tag = "실측(71471)" if r["is_real"] else "합성 시연(국내망 파일 도착 전)"
    print(f"발정 검증 [{tag}] — 개체 {r['n']}두, 발정 {r['pos_rate']:.0%}")
    if r.get("auc_calibrated") is not None:
        print(f"  보정 AUC {r['auc_calibrated']}  |  규칙 baseline AUC {r['auc_rule']}")
    else:
        print(f"  {r.get('note','')}")
    if not r["is_real"]:
        print(f"  ※ 실측하려면 국내망에서 71471 라벨을 {REAL_DIR} 에 두거나 "
              f"AIHUB_71471_DIR 지정.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
