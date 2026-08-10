"""교차-뷰 자세 인식 — 병목 해부와 개선.

교배사 발정 판정은 자세 시계열 위에 서 있으므로 **자세 정확도가 곧 상한**이다.
그런데 못 본 카메라에서 5클래스 정확도가 0.401 밖에 안 나온다. 이 모듈은 그
숫자를 셋으로 쪼개 무엇이 진짜 병목인지 가린 다음, 고칠 수 있는 것만 고친다.

병목 해부(실측 혼동행렬):
  1) **좌횡와/우횡와는 bbox 로 원리상 구분 불가**. 둘 다 옆으로 누운 같은 모양의
     상자다. 실제로 모델은 동전 던지기를 한다(좌 157/210, 우 272/87).
     전체의 27.7% 가 이 두 클래스이므로 여기서만 약 0.14 를 잃는다.
     → 그런데 **발정 판정에는 좌우가 아무 의미가 없다**. stall_estrus 는 어차피
       기립/기좌/횡와로 뭉친다. 즉 이 손실은 과제 정의의 문제이지 모델의 한계가
       아니다. 응용에 맞는 지표를 따로 봐야 한다.
  2) **횡와/기립 혼동**(1,231건)은 진짜 문제다. 카메라 각도가 바뀌면 같은 자세의
     종횡비·면적이 통째로 달라진다. → 크롭 외형으로 메운다.
  3) **평가 자체가 불안정**. 기존 코드는 뷰 8개 중 마지막 2개만 held-out 으로
     썼는데 그 둘이 전체의 42% 다. 한 번의 임의 분할로 낸 숫자라 개선을 재기
     어렵다. → 뷰별 leave-one-out 으로 바꾼다.

개선 수단:
  · 크롭 외형 피처(posture_crop_feats) — 상자 안을 본다
  · **뷰 단위 무감독 정규화** — 새 카메라를 달면 라벨 없이 그 카메라 영상만
    모을 수 있다. 그 뷰 자체의 평균·표준편차로 표준화하면 카메라별 오프셋이
    사라진다. 라벨을 쓰지 않으므로 누수가 아니고, 현장 절차와도 맞는다
    (설치 후 하루치 녹화 → 정규화 통계 산출 → 판정 시작).

    python competition/src/posture_crossview.py            # 전체 비교
    python competition/src/posture_crossview.py --quick    # 폴드 3개만
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import posture_crop_feats as pcf  # noqa: E402
import posture_features as pf  # noqa: E402

# 발정 판정이 실제로 쓰는 3클래스. stall_estrus 의 STAND/SIT/LIE 와 같다.
TO_ESTRUS = {
    "Lateral_lying_left": "lying", "Lateral_lying_right": "lying",
    "Sternal_lying": "lying", "Sitting": "sitting", "Standing": "standing",
}
MIN_FOLD = 150          # 이보다 작은 뷰는 폴드로 쓰기엔 표본이 부족하다


def load(rebuild: bool = False):
    classes = open(os.path.join(pf.COMP, "pig_posture_classes.txt")).read().split()
    full, X = pcf.load_all(rebuild)
    full["cls"] = full["class_id"].map(lambda i: classes[i])
    full["cls3"] = full["cls"].map(TO_ESTRUS)
    # 돈방(pen) — 카메라를 빼도 같은 돈방의 다른 카메라가 같은 돼지를 비춘다.
    # '새 농장'에 가장 가까운 조건은 돈방째 빼는 것이다.
    full["pen"] = full["view"].str.split("_").str[0]
    return full, X, classes


def view_normalize(F: np.ndarray, views: np.ndarray) -> np.ndarray:
    """뷰마다 그 뷰의 통계로 표준화(라벨 미사용).

    학습 뷰든 검증 뷰든 **각자 자기 통계**로 정규화한다. 검증 뷰의 라벨은 쓰지
    않으므로 누수가 아니다. 현장에서도 새 카메라 영상만 모으면 바로 계산된다.
    """
    out = np.array(F, dtype=np.float64, copy=True)
    for v in np.unique(views):
        m = views == v
        blk = out[m]
        mu = blk.mean(axis=0)
        sd = blk.std(axis=0)
        sd[sd < 1e-8] = 1.0
        out[m] = (blk - mu) / sd
    return np.nan_to_num(out, nan=0.0, posinf=0.0, neginf=0.0)


def _fit_eval(Xtr, ytr, Xte, yte, seed=42):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, f1_score
    clf = RandomForestClassifier(n_estimators=300, min_samples_leaf=3,
                                 class_weight="balanced", n_jobs=-1,
                                 random_state=seed)
    clf.fit(Xtr, ytr)
    p = clf.predict(Xte)
    return (accuracy_score(yte, p),
            f1_score(yte, p, average="macro", zero_division=0), p)


def lovo(full: pd.DataFrame, X: np.ndarray, feature_set: str = "geom",
         label: str = "cls", view_norm: bool = False,
         folds: list | None = None, verbose: bool = False,
         group: str = "view") -> dict:
    """그룹별 leave-one-out 교차검증.

    feature_set: geom(bbox 기하 15) | crop(외형) | both
    label: cls(5클래스) | cls3(발정용 3클래스)
    group: view(카메라 단위) | pen(돈방 단위 — 새 농장에 더 가까움)

    뷰 정규화는 group 과 무관하게 **항상 뷰(카메라) 단위**로 한다. 현장에서
    보정 통계를 뽑는 단위가 카메라이기 때문이다.
    """
    G = full[pf.RICH_COLS].to_numpy(dtype=np.float64)
    if feature_set == "geom":
        F = G
    elif feature_set == "crop":
        F = X.astype(np.float64)
    else:
        F = np.hstack([G, X.astype(np.float64)])
    if view_norm:
        F = view_normalize(F, full["view"].to_numpy())
    views = full[group].to_numpy()
    y = full[label].to_numpy()

    counts = full[group].value_counts()
    use = folds if folds else [v for v in sorted(counts.index)
                               if counts[v] >= MIN_FOLD]
    rows = []
    for v in use:
        m = views == v
        if len(np.unique(y[~m])) < 2:
            continue
        acc, mf1, _p = _fit_eval(F[~m], y[~m], F[m], y[m])
        rows.append({"view": v, "n_test": int(m.sum()),
                     "acc": round(acc, 3), "mf1": round(mf1, 3)})
        if verbose:
            print(f"    {v:<16} n={int(m.sum()):>5} acc={acc:.3f} mf1={mf1:.3f}",
                  flush=True)
    r = pd.DataFrame(rows)
    w = r["n_test"] / r["n_test"].sum()
    return {"folds": r,
            "acc_w": round(float((r["acc"] * w).sum()), 3),
            "acc_m": round(float(r["acc"].mean()), 3),
            "mf1_w": round(float((r["mf1"] * w).sum()), 3),
            "mf1_m": round(float(r["mf1"].mean()), 3),
            "n_folds": len(r)}


def majority_baseline(full: pd.DataFrame, label: str = "cls",
                      group: str = "view") -> dict:
    """학습 폴드의 다수 클래스를 그대로 찍는 기준선.

    이 기준선을 같이 보지 않으면 정확도를 완전히 잘못 읽는다. 실측에서 기존
    기하 전용 모델은 5클래스 0.414 인데 **다수 클래스만 찍어도 0.423** 이다 —
    즉 정확도만 보면 모델이 기준선보다 못하다. 클래스가 치우쳐 있어서 그렇다.
    실제 신호는 Macro-F1 에서 드러난다(기준선 0.119 vs 모델 0.228).
    """
    from sklearn.metrics import accuracy_score, f1_score
    vs = full[group].value_counts()
    use = [v for v in sorted(vs.index) if vs[v] >= MIN_FOLD]
    rows = []
    for v in use:
        m = full[group].to_numpy() == v
        maj = full.loc[~m, label].value_counts().idxmax()
        yte = full.loc[m, label]
        p = np.full(len(yte), maj)
        rows.append({"n": int(m.sum()),
                     "acc": accuracy_score(yte, p),
                     "mf1": f1_score(yte, p, average="macro", zero_division=0)})
    r = pd.DataFrame(rows)
    w = r["n"] / r["n"].sum()
    return {"acc_w": round(float((r["acc"] * w).sum()), 3),
            "mf1_w": round(float((r["mf1"] * w).sum()), 3)}


def ceiling_from_lr(full: pd.DataFrame) -> dict:
    """좌/우 횡와를 못 가른다고 가정할 때 5클래스 정확도의 상한.

    두 클래스를 완전히 맞히는 대신 **동전 던지기**를 한다고 두면, 나머지를 전부
    맞혀도 그 절반은 틀린다. 상한 = 1 − (좌우 비중)/2.
    """
    share = float(full["cls"].isin(("Lateral_lying_left",
                                    "Lateral_lying_right")).mean())
    return {"lr_share": round(share, 3), "ceiling": round(1.0 - share / 2, 3)}


def main() -> int:
    quick = "--quick" in sys.argv
    full, X, classes = load("--rebuild" in sys.argv)
    print(f"데이터 {len(full):,}박스 · 이미지 {full['image_id'].nunique():,} · "
          f"뷰 {full['view'].nunique()}")
    counts = full["view"].value_counts()
    use = [v for v in sorted(counts.index) if counts[v] >= MIN_FOLD]
    if quick:
        use = use[:3]
    print(f"폴드로 쓰는 뷰 {len(use)}개 (표본 {MIN_FOLD} 이상): {', '.join(use)}")

    c = ceiling_from_lr(full)
    print(f"\n=== 병목 1: 좌/우 횡와는 bbox 로 원리상 구분 불가 ===")
    print(f"  좌우 횡와 비중 {c['lr_share']:.1%} → 동전 던지기 가정 시 "
          f"5클래스 상한 {c['ceiling']:.3f}")
    print("  즉 0.401 을 1.0 과 비교하는 것 자체가 틀렸다. 그리고 발정 판정에는"
          "\n  좌우가 아무 의미가 없다 — 응용 지표는 3클래스로 봐야 한다.")

    print(f"\n=== 뷰별 leave-one-out ({len(use)}폴드) ===")
    print(f"  {'구성':<34} {'5클래스':>16}   {'발정 3클래스':>16}")
    print(f"  {'':<34} {'가중acc':>7} {'MacroF1':>8}   {'가중acc':>7} {'MacroF1':>8}")
    m5 = majority_baseline(full, "cls")
    m3 = majority_baseline(full, "cls3")
    print(f"  {'다수 클래스만 찍기(기준선)':<30} {m5['acc_w']:>7.3f} {m5['mf1_w']:>8.3f}   "
          f"{m3['acc_w']:>7.3f} {m3['mf1_w']:>8.3f}")
    results = {}
    for tag, fs, vn in (("기하만 (기존)", "geom", False),
                        ("기하 + 뷰 정규화", "geom", True),
                        ("기하 + 크롭 외형", "both", False),
                        ("기하 + 크롭 + 뷰 정규화", "both", True)):
        r5 = lovo(full, X, fs, "cls", vn, folds=use)
        r3 = lovo(full, X, fs, "cls3", vn, folds=use)
        results[tag] = (r5, r3)
        print(f"  {tag:<34} {r5['acc_w']:>7.3f} {r5['mf1_w']:>8.3f}   "
              f"{r3['acc_w']:>7.3f} {r3['mf1_w']:>8.3f}", flush=True)

    base5, base3 = results["기하만 (기존)"]
    best_tag = max(results, key=lambda k: results[k][1]["acc_w"])
    b5, b3 = results[best_tag]
    print(f"\n  → 최선 구성: {best_tag}")
    print(f"     5클래스     acc {base5['acc_w']:.3f} → {b5['acc_w']:.3f} "
          f"({b5['acc_w'] - base5['acc_w']:+.3f}) · "
          f"MF1 {base5['mf1_w']:.3f} → {b5['mf1_w']:.3f} "
          f"({b5['mf1_w'] - base5['mf1_w']:+.3f})")
    print(f"     발정 3클래스 acc {base3['acc_w']:.3f} → {b3['acc_w']:.3f} "
          f"({b3['acc_w'] - base3['acc_w']:+.3f}) · "
          f"MF1 {base3['mf1_w']:.3f} → {b3['mf1_w']:.3f} "
          f"({b3['mf1_w'] - base3['mf1_w']:+.3f})")
    print("\n  ※ 정확도만 보면 안 된다. 기존 기하 전용 모델은 5클래스 "
          f"{base5['acc_w']:.3f} 인데"
          f"\n    **다수 클래스만 찍어도 {m5['acc_w']:.3f}** 이다 — 기준선보다 못하다."
          "\n    클래스가 치우쳐 있어 정확도가 신호를 가린다. 실제 판별력은"
          f"\n    Macro-F1 에서 드러난다(기준선 {m5['mf1_w']:.3f} vs 개선 {b5['mf1_w']:.3f})."
          "\n    3클래스도 마찬가지다: 기준선 "
          f"{m3['acc_w']:.3f}/{m3['mf1_w']:.3f} vs 개선 {b3['acc_w']:.3f}/{b3['mf1_w']:.3f}.")

    print(f"\n=== 폴드별 상세 (최선 구성, 발정 3클래스) ===")
    print(f"  {'뷰':<16} {'검증수':>7} {'정확도':>7} {'MacroF1':>8}")
    for r in b3["folds"].itertuples(index=False):
        print(f"  {r.view:<16} {r.n_test:>7,} {r.acc:>7.3f} {r.mf1:>8.3f}")
    sp = b3["folds"]["acc"]
    print(f"  분산이 크다: {sp.min():.3f} ~ {sp.max():.3f}. 카메라마다 난이도가"
          "\n  다르므로 한 번의 분할로 낸 수치는 신뢰하기 어렵다.")

    print(f"\n=== 더 엄정한 조건: 돈방(pen)째 held-out — '새 농장'에 가장 가깝다 ===")
    print("  카메라만 빼면 같은 돈방의 다른 카메라가 같은 돼지를 비춘다.")
    print(f"  {'구성':<34} {'5클래스':>9} {'발정 3클래스':>13}")
    for tag, fs, vn in (("기하만 (기존)", "geom", False),
                        ("기하 + 크롭 + 뷰 정규화", "both", True)):
        p5 = lovo(full, X, fs, "cls", vn, group="pen")
        p3 = lovo(full, X, fs, "cls3", vn, group="pen")
        print(f"  {tag:<34} {p5['acc_w']:>9.3f} {p3['acc_w']:>13.3f}", flush=True)

    print("\n※ 검증 뷰의 라벨은 어디에도 쓰지 않았다. 뷰 정규화는 그 뷰의 입력"
          "\n  분포만 쓰는 무감독 보정이며, 현장 절차와 같다 — 카메라 설치 후"
          "\n  녹화만 모으면 계산된다. 다만 통계를 안정적으로 뽑을 만큼의 프레임이"
          "\n  필요하므로, 단발 이미지 추론에는 쓸 수 없다(CCTV 상시 녹화 전제).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
