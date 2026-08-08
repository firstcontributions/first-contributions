"""자세(keypoints) vs 행동라벨(bbox) — 같은 과제·같은 설계로 정보량 비교.

배경: [Bbox] 서브셋의 행동 라벨 4종으로는 발정 판정이 불가했다(개체 내 대조
AUC 0.465, docs/AIHUB.md). 그렇다면 **관절 좌표(자세)** 에는 더 많은 정보가
있는가? 이를 재게 하는 실험.

과제: 돈방 단위 ESTRUS(ch1~8 발정돈방 / ch9~16 비발정돈방) 판별.
설계: **채널 분리 GroupKFold** — 여러 카메라로 학습하고 **못 본 카메라**로 검증.
      카메라를 암기하면 held-out 에서 무너지므로, 전이되는 신호만 점수를 받는다.

⚠️ 해석 주의: 이 라벨은 개체가 아니라 돈방 단위이므로 **절대값은 발정 판정
성능이 아니다**. 그러나 자세와 행동이 **동일한 교락·동일한 검증 설계**를 공유하므로
**상대 비교는 유효**하다. 자세가 유의하게 높다면 "관절 정보가 4종 행동 라벨보다
많은 정보를 담는다"는 근거가 되고, 향후 데이터 확보 방향(포즈 기반)을 지지한다.

    python competition/src/pose_vs_behavior_eval.py <keypoints_dir>
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import parse_71471_keypoints as kpp  # noqa: E402


def _auc(X, y, groups, label, k=4, seed=42):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import GroupKFold, cross_val_predict
    if len(set(y)) < 2 or len(set(groups)) < 2:
        return None
    k = min(k, len(set(groups)))
    clf = RandomForestClassifier(n_estimators=300, min_samples_leaf=5,
                                 class_weight="balanced", n_jobs=-1,
                                 random_state=seed)
    p = cross_val_predict(clf, X, y, cv=GroupKFold(k), groups=groups,
                          method="predict_proba", n_jobs=-1)[:, 1]
    return round(float(roc_auc_score(y, p)), 3)


def evaluate(kp_dir: str) -> dict:
    """자세 피처 vs 행동 라벨의 교차-카메라 판별력 비교."""
    df = kpp.parse_dir(kp_dir)
    if not len(df) or df["estrus"].isna().all():
        return {"ok": False, "reason": "keypoints 파싱 결과 없음/라벨 없음"}
    df = df[df["estrus"].notna()].copy()
    y = df["estrus"].astype(int).to_numpy()
    g = df["channel"].to_numpy()
    per = df.groupby("channel")["estrus"].mean()
    out = {"ok": True, "n": int(len(df)), "n_channels": int(df["channel"].nunique()),
           "n_files": int(df["file"].nunique()),
           "pos_rate": round(float(y.mean()), 3),
           "n_pos_ch": int((per == 1).sum()), "n_neg_ch": int((per == 0).sum()),
           "pure_channels": int(((per == 0) | (per == 1)).sum())}
    if out["n_pos_ch"] < 2 or out["n_neg_ch"] < 2:
        out["ok"] = False
        out["reason"] = "클래스별 채널이 2개 미만 — 교차-카메라 검증 불가"
        return out
    # A) 행동 라벨만 (bbox 서브셋과 동일 조건)
    Xb = pd.get_dummies(df["behavior"].fillna("unknown"), prefix="beh")
    out["auc_behavior"] = _auc(Xb, y, g, "behavior")
    out["n_behaviors"] = int(df["behavior"].nunique())
    # B) 자세 기술자만 (회전·크기 불변 44개)
    Xp = df[kpp.FEATURES].apply(pd.to_numeric, errors="coerce").fillna(0.0)
    out["auc_pose"] = _auc(Xp, y, g, "pose")
    out["n_pose_feats"] = len(kpp.FEATURES)
    # C) 둘 다
    out["auc_both"] = _auc(pd.concat([Xb, Xp], axis=1), y, g, "both")
    # 자세 하위 그룹별 기여
    sub = {"쌍거리(28)": kpp.PAIR_COLS, "형태지표(8)": kpp.POSE_COLS,
           "가시성(8)": kpp.VIS_COLS}
    out["auc_pose_parts"] = {
        k: _auc(df[v].apply(pd.to_numeric, errors="coerce").fillna(0.0), y, g, k)
        for k, v in sub.items()}
    return out


def verdict(r: dict) -> str:
    if not r.get("ok"):
        return r.get("reason", "평가 불가")
    b, p = r.get("auc_behavior"), r.get("auc_pose")
    if b is None or p is None:
        return "비교 불가"
    d = p - b
    if d >= 0.08:
        return (f"자세가 행동 라벨보다 뚜렷하게 우세(+{d:.3f}). 관절 정보에 더 많은 "
                f"신호가 있으므로, 향후 발정 판정은 **포즈 기반**으로 가는 것이 옳다.")
    if d >= 0.03:
        return f"자세가 소폭 우세(+{d:.3f}). 포즈가 유망하나 결정적이진 않다."
    if d > -0.03:
        return (f"자세와 행동 라벨이 대등({d:+.3f}). 정지 프레임 자세만으로는 추가 "
                f"이득이 크지 않다 — 시간 축(활동량 변화)이 필요하다는 방증.")
    return f"자세가 오히려 열세({d:+.3f}). 이 표본에서 포즈 이점은 확인되지 않는다."


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    r = evaluate(sys.argv[1])
    if not r.get("ok"):
        print(r.get("reason")); return 1
    print(f"인스턴스 {r['n']:,} | 파일 {r['n_files']:,} | 채널 {r['n_channels']} "
          f"(발정 {r['n_pos_ch']} · 비발정 {r['n_neg_ch']}, 순수 {r['pure_channels']}) "
          f"| 양성률 {r['pos_rate']:.0%}")
    print("\n=== 채널 분리 GroupKFold — 못 본 카메라로 검증 ===")
    print(f"  행동 라벨 {r['n_behaviors']}종            AUC {r['auc_behavior']}")
    print(f"  자세 기술자 {r['n_pose_feats']}개          AUC {r['auc_pose']}")
    print(f"  행동 + 자세                  AUC {r['auc_both']}")
    print("\n  자세 하위 그룹:")
    for k, v in r["auc_pose_parts"].items():
        print(f"    {k:14s} AUC {v}")
    print(f"\n결론: {verdict(r)}")
    print("\n※ 돈방 단위 라벨이므로 절대값은 발정 판정 성능이 아니다. 두 피처가 동일한"
          "\n  교락·설계를 공유하므로 상대 비교만 유효하다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
