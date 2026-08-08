"""개체 내 대조 발정 검증 — 71471 [Bbox] 서브셋의 한계를 실측으로 규명.

세 단계로 점점 엄격해지는 설계를 적용해, 교락을 하나씩 제거하며 실제 신호가
남는지 본다(모두 실데이터 · 개체 분리 GroupKFold):

  ① 돈방 단위 라벨 그대로      → 카메라 교락(ch1~8 발정 / ch9~16 비발정)
  ② 개체 내 대조(발정 달력 연결) → 같은 개체의 발정일 vs 비발정일
  ③ ② + 채널 고정              → 카메라·돈방·개체 모두 통제, 발정만 변화 ⭐

③이 최상 조건이며, 여기서 무작위 수준이면 이 서브셋의 행동 라벨로는 발정을
판정할 수 없다는 뜻이다(모델 문제가 아니라 **라벨 어휘의 문제**).

입력:
  vulva_dir : 외음부 라벨 디렉터리(발정 달력 = 개체·날짜 양성 시점)
  bbox_dir  : [Bbox] 라벨 디렉터리(파일명에 개체·날짜·채널)

    python competition/src/estrus_contrast_eval.py <vulva_dir> <bbox_dir>
"""
from __future__ import annotations

import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import estrus_calendar as ec  # noqa: E402
import parse_71471_real as p71  # noqa: E402

BEH = ["lying", "standing", "sitting", "eating"]
FEAT = [f"f_{b}" for b in BEH]


def build_frames(vulva_dir: str, bbox_dir: str) -> pd.DataFrame:
    """발정 달력 × bbox → 프레임 단위 테이블[y, animal, ch, date, 행동비율...]."""
    cal = ec.load_calendar(vulva_dir)
    linked = ec.link(cal, ec.bbox_index(bbox_dir))
    if not len(linked):
        return pd.DataFrame()
    lab = (linked[["file", "estrus", "animal", "channel", "date"]]
           .rename(columns={"estrus": "Y", "animal": "AID",
                            "channel": "CH", "date": "D"}).set_index("file"))
    inst = p71.parse_dir(bbox_dir).join(lab, on="file", how="inner")
    rows = []
    for key, g in inst.groupby("file"):
        vc = g["behavior"].value_counts(normalize=True)
        r = {"key": key, "y": int(g["Y"].iloc[0]), "animal": g["AID"].iloc[0],
             "ch": g["CH"].iloc[0], "date": g["D"].iloc[0], "n_pigs": len(g),
             "area_mean": float(g["area"].mean())}
        for b in BEH:
            r[f"f_{b}"] = float(vc.get(b, 0.0))
        rows.append(r)
    return pd.DataFrame(rows)


def grouped_auc(df: pd.DataFrame, cols: list, group: str = "animal"):
    """개체(또는 지정 그룹) 분리 GroupKFold AUC. 불가하면 None."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import GroupKFold, cross_val_predict
    if not len(df) or df["y"].nunique() < 2:
        return None
    k = min(5, df[group].nunique())
    if k < 2:
        return None
    proba = cross_val_predict(
        LogisticRegression(max_iter=5000, class_weight="balanced"),
        df[cols], df["y"], cv=GroupKFold(k), groups=df[group],
        method="predict_proba")[:, 1]
    return round(float(roc_auc_score(df["y"], proba)), 3)


def evaluate(vulva_dir: str, bbox_dir: str) -> dict:
    """세 설계의 AUC + 행동 분포 비교를 담은 결과 dict."""
    F = build_frames(vulva_dir, bbox_dir)
    if not len(F):
        return {"ok": False, "reason": "연결된 프레임 없음(개체·날짜 교집합 필요)"}
    per = F.groupby("animal")["y"].nunique()
    out = {"ok": True, "n_frames": int(len(F)), "n_animals": int(F["animal"].nunique()),
           "pos_rate": round(float(F["y"].mean()), 3),
           "n_within_contrast": int((per > 1).sum()),
           "auc_behavior": grouped_auc(F, FEAT),
           "auc_behavior_plus": grouped_auc(F, FEAT + ["n_pigs", "area_mean"])}
    # ③ 채널 고정: 개체 내 대조가 성립하는 단일 채널 중 표본이 가장 큰 것
    best = None
    for ch, g in F.groupby("ch"):
        if g["y"].nunique() < 2 or g["animal"].nunique() < 2:
            continue
        if best is None or len(g) > len(best[1]):
            best = (ch, g)
    if best:
        ch, g = best
        out["fixed_channel"] = ch
        out["n_fixed"] = int(len(g))
        out["n_fixed_animals"] = int(g["animal"].nunique())
        out["auc_fixed_channel"] = grouped_auc(g, FEAT)
    dist = F.groupby("y")[FEAT + ["n_pigs"]].mean().round(3)
    out["behavior_dist"] = {int(k): v.to_dict() for k, v in dist.iterrows()}
    return out


def verdict(r: dict) -> str:
    """결과 해석 문장(정직한 결론)."""
    if not r.get("ok"):
        return r.get("reason", "평가 불가")
    a = r.get("auc_fixed_channel") or r.get("auc_behavior")
    if a is None:
        return "유효 검증 불가 — 그룹/클래스 부족"
    if a < 0.55:
        return ("이 서브셋의 행동 라벨(4종)로는 발정 판정이 **불가**하다(무작위 수준). "
                "카메라·개체를 모두 통제한 최상 조건에서도 신호가 없으므로, 모델이 아니라 "
                "**라벨 어휘의 한계**다 — 발정 지시 행동(tailing·mounting·기립반사)이 "
                "주석에 없고, 단일 프레임 자세로는 활동량 변화를 담을 수 없다.")
    if a < 0.65:
        return "약한 신호만 존재 — 실용 판정에는 부족하다."
    return "유의한 신호가 있다 — 추가 피처·시계열로 확장할 가치가 있다."


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    r = evaluate(sys.argv[1], sys.argv[2])
    if not r["ok"]:
        print(r["reason"]); return 1
    print(f"프레임 {r['n_frames']:,} | 개체 {r['n_animals']} "
          f"(개체 내 대조 {r['n_within_contrast']}두) | 발정 {r['pos_rate']:.0%}")
    print(f"  ② 개체 분리 · 행동만          AUC {r['auc_behavior']}")
    print(f"  ② 개체 분리 · 행동+마릿수/크기 AUC {r['auc_behavior_plus']}")
    if r.get("auc_fixed_channel") is not None:
        print(f"  ③ 채널 고정({r['fixed_channel']}) · 행동만   AUC "
              f"{r['auc_fixed_channel']}  (n={r['n_fixed']}, 개체 {r['n_fixed_animals']})")
    print("\n행동 분포(0=비발정 / 1=발정):")
    for k, v in r["behavior_dist"].items():
        print(f"  {k}: " + ", ".join(f"{a.replace('f_','')} {b}" for a, b in v.items()))
    print(f"\n결론: {verdict(r)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
