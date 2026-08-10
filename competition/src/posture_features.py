"""자세 인식 피처 강화 — 교배사(스톨) 발정 판정의 기반.

왜 자세인가: 교배사·임신사는 **스톨(개별 사육틀)** 이라 돼지가 이동하지 못한다.
군사 사육에서 쓰던 **활동량 신호가 구조적으로 없다**(실측: 스톨 8.7px vs 군사 14.0px).
스톨에서 남는 관찰 가능 신호는 **자세와 그 변화**다 —
기립/기좌/횡와의 전환 빈도, 기립 지속시간, 부동자세(기립반사).
따라서 **자세 인식 정확도가 곧 교배사 발정 판정의 상한**이 된다.

기존 구현은 피처가 **2개**(종횡비, 면적 순위)뿐이었다. 이 모듈은 같은 데이터에서
뽑을 수 있는 정보를 최대한 쓴다:

  · 기본 형태    : 종횡비, log 면적, 폭/높이(이미지 정규화)
  · 화면 내 위치 : cx/W, cy/H, 가장자리까지 거리
  · **프레임 상대**: 같은 이미지 안 다른 돼지 대비 면적·폭·높이 비율과 순위
                    → 카메라 거리·원근 차이를 상쇄한다(핵심)
  · **원근 보정**  : 세로 위치(cy)가 비슷한 개체들의 크기로 나눈 값
                    (부감 시점에서 cy 는 카메라와의 거리에 대응)
  · 밀집도       : 프레임 내 개체 수, 최근접 이웃까지 거리

⚠️ **누수 경고(실측)**: 원 프로토콜(train1 학습 → train2 검증)은 두 파일이 뷰 5개와
**이미지 3,090장을 공유**해 누수가 있다. 그 분할에서는 강화 피처가 0.955 까지 나오지만
위치(cx/cy)를 외운 결과다. 분할별 정직한 수치:

    train1→train2(누수)  0.686 → 0.955
    이미지 분리          0.328 → 0.517
    **뷰 분리(못 본 카메라)  0.363 → 0.401**   ← 새 농장 설치 시 실제로 기대할 값

프로젝트가 이전에 보고한 자세 정확도 0.642 도 누수된 분할에서 나온 값이다.

⚠️ 위 0.401 은 **뷰 2개만 held-out 한 한 번의 임의 분할** 결과다. 그 둘이 전체의
42% 라 표본도 치우쳐 있다. 더 엄정한 뷰별 leave-one-out(7폴드)과 개선 결과는
`posture_crossview.py` 에 있다. 요약:

    다수 클래스만 찍기(기준선)      5클래스 0.423 / MF1 0.119
    기하만(이 모듈)                5클래스 0.414 / MF1 0.228   ← 정확도는 기준선 이하
    기하 + 크롭 외형 + 뷰 정규화      5클래스 0.467 / MF1 0.249

즉 bbox 기하만으로는 카메라가 바뀌면 일반화가 어렵고, **정확도로 보면 다수 클래스
찍기보다도 못하다**(클래스 치우침 때문). 이미지 내용이 필요하다 → `posture_crop_feats`.

    python competition/src/posture_features.py [view|image|naive]
"""
from __future__ import annotations

import ast
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

COMP = ("/root/.cache/kagglehub/competitions/multi-view-pig-posture-recognition"
        "/multiview_pig_posture_recognition")

RICH_COLS = [
    "aspect", "log_area", "w_norm", "h_norm", "cx_norm", "cy_norm",
    "edge_dist", "area_ratio_med", "w_ratio_med", "h_ratio_med",
    "area_rank", "aspect_ratio_med", "persp_area", "n_pigs", "nn_dist",
]


def load_split(fn: str) -> pd.DataFrame:
    """train1/train2 CSV → bbox 분해 + 이미지 식별자."""
    d = pd.read_csv(os.path.join(COMP, fn))
    bb = d["bbox"].apply(ast.literal_eval)
    d["x"] = bb.apply(lambda b: float(b[0])); d["y"] = bb.apply(lambda b: float(b[1]))
    d["w"] = bb.apply(lambda b: float(b[2])); d["h"] = bb.apply(lambda b: float(b[3]))
    # 뷰(pen·cam) — 누수 방지 그룹 키로 쓸 수 있다
    d["view"] = d["image_id"].str.rsplit("_", n=2).str[0]
    return d


def add_rich(d: pd.DataFrame) -> pd.DataFrame:
    """프레임 맥락을 포함한 자세 피처 추가."""
    d = d.copy()
    W = d["width"].astype(float); H = d["height"].astype(float)
    d["aspect"] = d["w"] / d["h"].replace(0, np.nan)
    d["area"] = d["w"] * d["h"]
    d["log_area"] = np.log1p(d["area"])
    d["w_norm"] = d["w"] / W
    d["h_norm"] = d["h"] / H
    d["cx_norm"] = (d["x"] + d["w"] / 2) / W
    d["cy_norm"] = (d["y"] + d["h"] / 2) / H
    d["edge_dist"] = np.minimum.reduce([
        d["cx_norm"], 1 - d["cx_norm"], d["cy_norm"], 1 - d["cy_norm"]])

    g = d.groupby("image_id", sort=False)
    # 프레임 상대 — 카메라 거리·원근 차이를 상쇄하는 핵심 피처
    for col, name in (("area", "area_ratio_med"), ("w", "w_ratio_med"),
                      ("h", "h_ratio_med"), ("aspect", "aspect_ratio_med")):
        med = g[col].transform("median").replace(0, np.nan)
        d[name] = d[col] / med
    d["area_rank"] = g["area"].rank(pct=True)
    d["n_pigs"] = g["image_id"].transform("size").astype(float)

    # 원근 보정: 세로 위치가 비슷한 개체들의 크기로 나눈다.
    # 부감·사각 시점에서 cy 는 카메라와의 거리에 대응하므로, 같은 띠(band)의
    # 개체 크기를 기준으로 삼으면 "멀어서 작은 것"과 "누워서 작은 것"이 구분된다.
    d["_band"] = (d["cy_norm"] * 5).astype(int).clip(0, 4)
    band_med = d.groupby(["image_id", "_band"])["area"].transform("median").replace(0, np.nan)
    d["persp_area"] = d["area"] / band_med

    # 최근접 이웃 거리(정규화) — 밀집 시 자세가 제약된다
    nn = []
    for _img, sub in d.groupby("image_id", sort=False):
        c = np.column_stack([(sub["x"] + sub["w"] / 2) / sub["width"],
                             (sub["y"] + sub["h"] / 2) / sub["height"]])
        if len(c) < 2:
            nn.extend([1.0] * len(c)); continue
        dist = np.linalg.norm(c[:, None, :] - c[None, :, :], axis=2)
        np.fill_diagonal(dist, np.inf)
        nn.extend(dist.min(axis=1).tolist())
    d["nn_dist"] = nn
    for c in RICH_COLS:
        d[c] = pd.to_numeric(d[c], errors="coerce").fillna(0.0)
    return d.drop(columns=["_band"])


def evaluate(split: str = "view") -> dict:
    """기존 2피처 vs 강화 피처 비교.

    split="naive" : train1 → train2 (원 프로토콜)
        ⚠️ 이 분할은 **누수가 있다** — 두 파일이 뷰 5개와 **이미지 3,090장을 공유**한다.
           같은 프레임이 학습·검증에 모두 들어가면 위치 피처가 정답을 외워버린다.
    split="image" : 겹치는 이미지를 제거
    split="view"  : **뷰(pen·cam) 분리** — 못 본 카메라로 검증(기본, 가장 엄정)
    """
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, f1_score
    import posture_eval
    classes = open(os.path.join(COMP, "pig_posture_classes.txt")).read().split()
    a, b = add_rich(load_split("train1.csv")), add_rich(load_split("train2.csv"))
    if split == "view":
        allv = sorted(set(a["view"]) | set(b["view"]))
        hold = set(allv[-2:])                     # 마지막 2개 뷰를 held-out
        full = pd.concat([a, b], ignore_index=True).drop_duplicates(
            subset=["image_id", "bbox"])
        tr = full[~full["view"].isin(hold)].copy()
        te = full[full["view"].isin(hold)].copy()
    elif split == "image":
        te = b[~b["image_id"].isin(set(a["image_id"]))].copy()
        tr = a.copy()
    else:
        tr, te = a.copy(), b.copy()
    for d in (tr, te):
        d["cls"] = d["class_id"].apply(lambda i: classes[i])
    ytr, yte = tr["cls"].to_numpy(), te["cls"].to_numpy()

    def run(Xtr, Xte, tag, n_feat):
        clf = RandomForestClassifier(n_estimators=300, min_samples_leaf=3,
                                     class_weight="balanced", n_jobs=-1,
                                     random_state=42)
        clf.fit(Xtr, ytr); p = clf.predict(Xte)
        return {"tag": tag, "n_feat": n_feat,
                "acc": round(accuracy_score(yte, p), 3),
                "mf1": round(f1_score(yte, p, average="macro", zero_division=0), 3)}

    base = run(posture_eval._feats(tr["w"], tr["h"], tr["area"]),
               posture_eval._feats(te["w"], te["h"], te["area"]), "기존(종횡비·면적순위)", 2)
    rich = run(tr[RICH_COLS], te[RICH_COLS], "강화(프레임 상대·원근 보정)", len(RICH_COLS))
    # 어떤 피처가 기여했나
    clf = RandomForestClassifier(n_estimators=300, min_samples_leaf=3,
                                 class_weight="balanced", n_jobs=-1, random_state=42)
    clf.fit(tr[RICH_COLS], ytr)
    imp = sorted(zip(RICH_COLS, clf.feature_importances_), key=lambda t: -t[1])[:6]
    return {"n_train": len(tr), "n_test": len(te), "classes": classes,
            "split": split, "base": base, "rich": rich,
            "d_acc": round(rich["acc"] - base["acc"], 3),
            "d_mf1": round(rich["mf1"] - base["mf1"], 3),
            "top_features": [(k, round(float(v), 3)) for k, v in imp]}


def main() -> int:
    split = sys.argv[1] if len(sys.argv) > 1 else "view"
    r = evaluate(split)
    tag = {"naive": "train1→train2 (누수 있음)", "image": "이미지 분리",
           "view": "뷰 분리 — 못 본 카메라"}[r["split"]]
    print(f"[{tag}] 학습 {r['n_train']:,} → 검증 {r['n_test']:,} "
          f"({len(r['classes'])}클래스)")
    for k in ("base", "rich"):
        x = r[k]
        print(f"  {x['tag']:26s} 피처 {x['n_feat']:2d}  정확도 {x['acc']}  Macro-F1 {x['mf1']}")
    print(f"  → 정확도 {r['d_acc']:+.3f} · Macro-F1 {r['d_mf1']:+.3f}")
    print("  기여 상위 피처: " + ", ".join(f"{k} {v}" for k, v in r["top_features"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
