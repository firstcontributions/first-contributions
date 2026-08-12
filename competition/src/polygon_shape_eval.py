"""폴리곤 실루엣이 bbox 보다 얼마나 더 주는가 — **이미지 없이** 잰다.

원천 이미지(TS06 10GB)를 받지 않고도 답할 수 있는 질문이 있다. 622 라벨에는
폴리곤 좌표가 들어 있으므로 **모양 자체는 픽셀 없이 계산된다**. 지금 자세
인식은 bbox 기하로 3클래스 0.636 에서 막혀 있는데, 그 병목이 "상자로는 원리상
구분이 안 돼서"인지 확인할 수 있다.

  bbox 만          w · h · 종횡비 · 면적 · 위치          ← 지금 쓰는 것
  + 폴리곤 모양     충실도 · 원형도 · 신장도 · 방향 ·
                   반경 프로파일 · 볼록결손               ← 폴리곤에서만 나오는 것

두 구성의 차이가 곧 **분할 모델을 붙였을 때의 상한**이다. 차이가 작으면 10GB 를
받아 14시간 학습할 이유가 없고, 크면 근거가 생긴다.

## 누수 주의

CVAT interpolation 모드로 10프레임마다 뽑은 영상이라 **인접 프레임이 거의 같다**.
프레임 단위로 나누면 같은 장면이 학습·검증 양쪽에 들어가 점수가 부풀려진다.
**세션(=영상) 단위 leave-one-out** 으로만 잰다.

    python competition/src/polygon_shape_eval.py <라벨디렉터리>
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import finetune_polygon as fp  # noqa: E402

OUT = os.path.join(ROOT, "competition", "data", "polygon_shape_eval.json")

# 자세 3클래스 — 발정 판정에 쓰는 응용 지표(좌/우 구분은 무의미).
# Suckling 은 포유 중인 모돈이므로 횡와로 본다.
POSTURE = {
    "Lying": "lying", "Resting": "lying", "Suckling": "lying",
    "Sitting": "sitting",
    "Standing": "standing", "Walking": "standing", "Eating": "standing",
    "Drinking": "standing", "Searching": "standing", "Scrubbing": "standing",
    "Running": "standing",
}
MIN_PER_CLASS = 30      # 이보다 적은 클래스는 빼고 센다(Parturition 2건 등)


# -- 모양 기술자 -----------------------------------------------------------
def polygon_feats(pts, w: float, h: float) -> dict:
    """폴리곤 하나 → 모양 특징. 좌표만 쓰므로 이미지가 필요 없다."""
    p = np.asarray(pts, dtype=float)
    if len(p) < 3:
        return {}
    # 프레임 크기로 정규화 — 해상도가 2종(2560×1944, 1920×1080)이라 필수
    s = np.array([max(w, 1.0), max(h, 1.0)])
    q = p / s
    x, y = q[:, 0], q[:, 1]

    # 신발끈 공식. 부호로 방향을 알 수 있지만 여기선 크기만 쓴다.
    area = 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))
    d = np.diff(np.vstack([q, q[:1]]), axis=0)
    perim = float(np.hypot(d[:, 0], d[:, 1]).sum())

    bw, bh = x.max() - x.min(), y.max() - y.min()
    bbox_area = max(bw * bh, 1e-12)

    # 2차 모멘트 고윳값 → 신장도·방향. bbox 는 축에 묶여 있어 **기울어 누운
    # 돼지의 가늘고 긴 모양을 못 잡는다**. 폴리곤에서만 나오는 정보다.
    c = q - q.mean(axis=0)
    cov = np.cov(c.T) if len(c) > 2 else np.eye(2) * 1e-12
    ev = np.linalg.eigvalsh(cov)
    ev = np.clip(ev, 1e-12, None)
    elong = float(np.sqrt(ev[1] / ev[0]))
    ang = 0.5 * np.arctan2(2 * cov[0, 1], cov[0, 0] - cov[1, 1])

    # 중심에서 각 꼭짓점까지의 거리 — 윤곽의 울퉁불퉁함
    r = np.hypot(c[:, 0], c[:, 1])
    rm = max(r.mean(), 1e-12)

    try:
        import cv2
        hull = cv2.convexHull((p).astype(np.float32))
        ha = float(cv2.contourArea(hull)) / float(s[0] * s[1])
        solidity = area / max(ha, 1e-12)
    except Exception:                                            # noqa: BLE001
        solidity = float("nan")

    return {
        "poly_area": area,
        "poly_perim": perim,
        # 원형도 4πA/P² — 뭉친 몸(엎드림) vs 늘어진 몸(옆으로 누움)
        "circularity": float(4 * np.pi * area / max(perim ** 2, 1e-12)),
        # 충실도 = 폴리곤 / 볼록껍질. 다리를 뻗으면 내려간다.
        "solidity": solidity,
        # 채움률 = 폴리곤 / bbox. **bbox 가 같아도 이게 다르면 자세가 다르다.**
        "extent": float(area / bbox_area),
        "elongation": elong,
        "orient_sin": float(abs(np.sin(2 * ang))),
        "r_std_norm": float(r.std() / rm),
        "r_minmax": float(r.min() / max(r.max(), 1e-12)),
        "n_pts": float(len(p)),
    }


def bbox_feats(pts, w: float, h: float) -> dict:
    """지금 쓰고 있는 것과 같은 수준의 상자 특징(비교 기준선)."""
    p = np.asarray(pts, dtype=float)
    s = np.array([max(w, 1.0), max(h, 1.0)])
    q = p / s
    x, y = q[:, 0], q[:, 1]
    bw, bh = float(x.max() - x.min()), float(y.max() - y.min())
    return {
        "bw": bw, "bh": bh,
        "aspect": bw / max(bh, 1e-9),
        "bbox_area": bw * bh,
        "cx": float(x.mean()), "cy": float(y.mean()),
    }


BBOX_KEYS = ["bw", "bh", "aspect", "bbox_area", "cx", "cy"]
POLY_KEYS = ["poly_area", "poly_perim", "circularity", "solidity", "extent",
             "elongation", "orient_sin", "r_std_norm", "r_minmax", "n_pts"]


def build(df, verbose: bool = True):
    """행동 폴리곤 → 특징 행렬. 세션 라벨을 함께 돌려준다."""
    import pandas as pd
    rows = []
    for r in df.itertuples(index=False):
        f = bbox_feats(r.points, r.img_w, r.img_h)
        g = polygon_feats(r.points, r.img_w, r.img_h)
        if not g:
            continue
        f.update(g)
        f["label"] = r.label
        f["session"] = r.session
        rows.append(f)
    out = pd.DataFrame(rows)
    if verbose:
        print(f"  특징 {len(out):,}개 · 세션 {out['session'].nunique()}")
    return out


def _eval(X, y, groups, seed: int = 0) -> dict:
    """세션 단위 leave-one-group-out. 프레임 단위로 나누면 안 된다."""
    from sklearn.ensemble import HistGradientBoostingClassifier
    from sklearn.metrics import accuracy_score, f1_score
    from sklearn.model_selection import LeaveOneGroupOut

    accs, f1s, n_tot, n_hit = [], [], 0, 0
    for tr, te in LeaveOneGroupOut().split(X, y, groups):
        if len(np.unique(y[tr])) < 2 or len(te) < 20:
            continue
        m = HistGradientBoostingClassifier(max_iter=120, random_state=seed)
        m.fit(X[tr], y[tr])
        p = m.predict(X[te])
        accs.append(accuracy_score(y[te], p))
        f1s.append(f1_score(y[te], p, average="macro", zero_division=0))
        n_tot += len(te)
        n_hit += int((p == y[te]).sum())
    return {"acc_w": n_hit / max(1, n_tot), "acc_mean": float(np.mean(accs)),
            "mf1_mean": float(np.mean(f1s)), "folds": len(accs), "n": n_tot}


def majority(y, groups) -> dict:
    """다수 클래스만 찍는 기준선 — 정확도만 보면 안 된다는 근거."""
    from sklearn.metrics import f1_score
    from sklearn.model_selection import LeaveOneGroupOut
    accs, f1s = [], []
    for tr, te in LeaveOneGroupOut().split(np.zeros(len(y)), y, groups):
        if len(np.unique(y[tr])) < 2 or len(te) < 20:
            continue
        vals, cnt = np.unique(y[tr], return_counts=True)
        p = np.full(len(te), vals[cnt.argmax()])
        accs.append((p == y[te]).mean())
        f1s.append(f1_score(y[te], p, average="macro", zero_division=0))
    return {"acc_mean": float(np.mean(accs)), "mf1_mean": float(np.mean(f1s)),
            "folds": len(accs)}


def run(label_dir: str, verbose: bool = True) -> dict:
    df = fp.load_labels(label_dir, verbose=verbose)
    df = fp.select_labels(df, "behavior", verbose=verbose)
    F = build(df, verbose=verbose)

    res = {"n_polygons": int(len(F)), "n_sessions": int(F["session"].nunique())}
    for task, mapper in (("behavior", None), ("posture", POSTURE)):
        G = F.copy()
        if mapper:
            G["y"] = G["label"].map(mapper)
            G = G[G["y"].notna()]
        else:
            G["y"] = G["label"]
        keep = G["y"].value_counts()
        keep = keep[keep >= MIN_PER_CLASS].index
        G = G[G["y"].isin(keep)]
        y = G["y"].to_numpy()
        grp = G["session"].to_numpy()
        if verbose:
            print(f"\n  [{task}] 클래스 {len(keep)}종 · 표본 {len(G):,}")
            print("   ", dict(G["y"].value_counts()))
        base = majority(y, grp)
        block = {"classes": sorted(keep.tolist()), "n": int(len(G)),
                 "baseline": base}
        # **기준선을 먼저 찍는다.** 이걸 빼면 0.6 이 좋아 보이는데, 다수 클래스만
        # 찍어도 0.636 이 나오는 데이터다. 실제로 처음에 계산만 하고 출력을
        # 빠뜨려서 결과를 잘못 읽을 뻔했다.
        if verbose:
            print(f"    {'다수클래스 기준선':<14} acc {base['acc_mean']:.3f} · "
                  f"MF1 {base['mf1_mean']:.3f}")
        for name, cols in (("bbox", BBOX_KEYS),
                           ("bbox+poly", BBOX_KEYS + POLY_KEYS),
                           ("poly", POLY_KEYS)):
            X = G[cols].to_numpy(dtype=float)
            X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
            block[name] = _eval(X, y, grp)
            if verbose:
                b = block[name]
                print(f"    {name:<14} acc {b['acc_mean']:.3f} "
                      f"({b['acc_mean'] - base['acc_mean']:+.3f}) · "
                      f"MF1 {b['mf1_mean']:.3f} "
                      f"({b['mf1_mean'] - base['mf1_mean']:+.3f}) "
                      f"[{b['folds']} 폴드]")
        gain = block["bbox+poly"]["mf1_mean"] - block["bbox"]["mf1_mean"]
        block["mf1_gain"] = gain
        block["bbox_beats_baseline_mf1"] = bool(
            block["bbox"]["mf1_mean"] > base["mf1_mean"])
        block["bbox_beats_baseline_acc"] = bool(
            block["bbox"]["acc_mean"] > base["acc_mean"])
        res[task] = block
        if verbose:
            print(f"    → 폴리곤 추가 이득 MF1 {gain:+.3f}"
                  + ("  (해롭다)" if gain < 0 else ""))
            if not block["bbox_beats_baseline_acc"]:
                print("    ※ 정확도가 기준선보다 낮다 — 클래스가 치우쳐 정확도가"
                      " 신호를 가린다. 판별력은 Macro-F1 로 본다.")
    return res


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="polygon_shape_eval")
    ap.add_argument("label_dir")
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args(argv)
    print("=" * 72)
    print("  폴리곤 실루엣 vs bbox — 이미지 없이, 세션 단위 LOO")
    print("=" * 72)
    r = run(a.label_dir)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(r, open(a.out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"\n저장: {a.out}")
    g = r["posture"]["mf1_gain"]
    print(f"\n결론: 자세 3클래스에서 폴리곤이 bbox 대비 MF1 {g:+.3f}")
    print("  이 값은 **상한**이다 — 정답 폴리곤을 그대로 준 셈이라, 실제 분할")
    print("  모델이 예측한 폴리곤은 이보다 낮다.")
    if g <= 0.02:
        print("  → 이득이 없다. 원천 이미지(10GB)를 받아 분할 모델을 학습할")
        print("     이유가 없다. 상한에서 안 나오는 것이 실제에서 나올 수 없다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
