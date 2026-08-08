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
import parse_71471_real  # noqa: E402
import parse_aihub  # noqa: E402

REAL_DIR = os.path.join(ROOT, "competition", "data", "aihub", "71471")
GEOM = ["bbox_w", "bbox_h", "aspect_ratio", "area", "centroid_x", "centroid_y"]


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


def evaluate_real_schema(label_dir: str) -> dict | None:
    """71471 **실제 배포 스키마**(ANNOTATION_INFO/ESTRUS) 인스턴스 단위 실측 검증.

    각 bbox 에 ESTRUS(Y/N) 정답이 있으므로 개체 집계 없이 바로 지도 검증한다.
    누수 방지: 세션(농장+채널+일시) 단위 GroupKFold.
      · auc_rule       : 71471 표준 가중치(무학습) 점수의 AUC — baseline
      · auc_calibrated : 행동 원핫 + bbox 기하로 학습한 보정 모델의 AUC
    """
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import GroupKFold, cross_val_predict
    df = parse_71471_real.parse_dir(label_dir)
    if not len(df) or df["estrus"].isna().all():
        return None
    df = df[df["estrus"].notna()].copy()
    y = df["estrus"].astype(int).to_numpy()
    out = {"is_real": True, "schema": "71471-real", "n": int(len(df)),
           "pos_rate": round(float(y.mean()), 3),
           "n_sessions": int(df["session"].nunique()),
           "n_files": int(df["file"].nunique()),
           "auc_rule": None, "auc_calibrated": None}
    # 규칙 baseline: 행동 → 71471 표준 카테고리 → 수의학 가중치
    R = ref.EstrusReference()
    rule = np.array([R.score({ref.to_reference(b): 1.0} if ref.to_reference(b)
                             else {}, 0.0) for b in df["behavior"]])
    if len(set(y)) < 2:
        out["note"] = "단일 클래스 — 검증 불가(발정 라벨이 한 종류)"
        return out
    out["auc_rule"] = round(float(roc_auc_score(y, rule)), 3)
    out["behavior_top"] = df["behavior"].value_counts().head(8).to_dict()
    out["estrus_behavior"] = (df[df["estrus"] == 1]["behavior"]
                              .value_counts().head(6).to_dict())

    # ---- 교락(confound) 진단: 발정 라벨이 카메라/세션과 1:1로 붙어 있는가 ----
    # 71471 은 발정 모돈을 특정 돈방/카메라에서 촬영하는 구성이라, 채널이
    # 라벨을 그대로 결정하면 bbox 위치(카메라 화각)만으로 완벽 분리된다.
    # 이때의 높은 AUC 는 '발정 인식'이 아니라 '카메라 식별'이므로 무효로 본다.
    conf = {}
    for key in ("channel", "session", "farm"):
        if key not in df or df[key].isna().all():
            continue
        per = df.groupby(key)["estrus"].mean()
        conf[key] = {"n_groups": int(len(per)),
                     "pure_groups": int(((per == 0) | (per == 1)).sum())}
    out["confound"] = conf
    ch = conf.get("channel", {})
    confounded = bool(ch and ch["pure_groups"] == ch["n_groups"])
    out["confounded_by_channel"] = confounded
    out["group_key"] = "channel" if "channel" in df else "session"
    groups = df[out["group_key"]].to_numpy()
    n_g = len(set(groups))

    if confounded:
        # 기하 피처는 카메라를 그대로 노출하므로 사용 금지 → 행동만으로 평가
        out["cv"] = (f"검증 불가(교락) — 발정이 채널과 1:1 대응"
                     f"(순수 그룹 {ch['pure_groups']}/{ch['n_groups']})")
        out["auc_calibrated"] = None
        out["note"] = (
            "이 표본에서는 ESTRUS 가 카메라(채널)와 완전히 교락되어, bbox 기하를 "
            "쓰면 '발정'이 아니라 '카메라'를 학습한다(AUC≈1.0 은 누수). "
            "채널을 그룹으로 분리하면 학습 폴드에 한 클래스만 남아 지도검증 자체가 "
            "구조적으로 불가능하다. 유효 검증에는 같은 돈방에서 발정/비발정이 함께 "
            "관측된 표본(또는 같은 개체의 시간적 전이)이 필요하다.")
        # 교락 상황에서 유일하게 정직한 수치 = 무학습 규칙 baseline(행동만 사용)
        out["auc_behavior_only"] = out["auc_rule"]
        out["behavior_estrus_rate"] = (
            df.groupby("behavior")["estrus"].mean().round(3).to_dict())
        return out

    # ---- 교락 없음: 행동 + bbox 기하로 정상 검증 ----
    X = pd.get_dummies(df["behavior"].fillna("unknown"), prefix="beh")
    for c in GEOM:
        X[c] = pd.to_numeric(df[c], errors="coerce")
    X = X.fillna(0.0)
    clf = LogisticRegression(max_iter=2000, class_weight="balanced")
    if n_g >= 2 and len(df) >= 20:
        cv = GroupKFold(n_splits=min(5, n_g))
        proba = cross_val_predict(clf, X, y, cv=cv, groups=groups,
                                  method="predict_proba")[:, 1]
        out["cv"] = f"GroupKFold({min(5, n_g)}) by {out['group_key']}"
    else:
        from sklearn.model_selection import StratifiedKFold
        proba = cross_val_predict(clf, X, y, cv=StratifiedKFold(5, shuffle=True,
                                  random_state=42), method="predict_proba")[:, 1]
        out["cv"] = "StratifiedKFold(5) — 그룹이 1개라 그룹 분리 불가"
    out["auc_calibrated"] = round(float(roc_auc_score(y, proba)), 3)
    out["proba"] = proba
    out["y"] = y
    return out


def evaluate(arg: str | None = None) -> dict:
    """실데이터가 있으면 실측, 없으면 합성 시연.

    실제 배포 스키마(ANNOTATION_INFO/ESTRUS)를 먼저 시도하고, 아니면 기존
    (소문자 키) 스키마 경로로 폴백한다.
    """
    d = resolve_dir(arg)
    if d:
        real = evaluate_real_schema(d)
        if real is not None:
            return real
    return _evaluate_legacy(arg)


def _evaluate_legacy(arg: str | None = None) -> dict:
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
    if r.get("schema") == "71471-real":
        print(f"발정 검증 [{tag}] — 인스턴스 {r['n']:,}개(bbox), "
              f"발정 {r['pos_rate']:.1%} | 파일 {r['n_files']:,} · "
              f"세션 {r['n_sessions']}")
        print(f"  검증: {r.get('cv','-')}")
        if r.get("estrus_behavior"):
            print("  발정 개체 행동: " + ", ".join(
                f"{k} {v}" for k, v in r["estrus_behavior"].items()))
        if r.get("confounded_by_channel"):
            print(f"  ⚠️ 교락 경고: {r.get('note','')}")
            print(f"  행동 라벨만의 AUC: {r.get('auc_behavior_only')} "
                  f"| 규칙 baseline AUC {r.get('auc_rule')}")
            return 0
    else:
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
