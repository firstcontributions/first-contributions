"""자세 CNN — **원리적 상한 0.861 을 넘을 수 있는 유일한 경로**를 시험한다.

좌/우 횡와는 bbox 기하로 원리상 구분 불가다. 둘 다 옆으로 누운 같은 모양의
상자라, 기존 모델은 좌횡와를 좌 157 / 우 210 으로 사실상 동전을 던진다.
두 클래스가 전체의 27.8% 이므로 **5클래스 상한이 1.0 이 아니라 0.861** 이다.

지금 쓰는 피처 캐시(posture_crops.npz)는 크롭을 60차원으로 요약한 것이라
방향 정보가 이미 뭉개져 있다. **원본 크롭 픽셀을 직접 보는 모델만이 머리
방향을 볼 수 있고**, 그래야 상한 자체가 올라간다. 이 스크립트가 그 시험이다.

## 무엇을 재는가

  1. 5클래스 정확도가 **0.861 을 넘는가** — 넘으면 좌/우를 갈랐다는 뜻
  2. 좌/우 횡와 쌍만 떼어낸 **이진 정확도** — 0.5 근처면 여전히 동전이다
  3. 발정 3클래스(기립/기좌/횡와) — 응용 지표. 기존 0.636

## 검증

뷰(카메라)를 통째로 빼는 LOVO. 같은 카메라가 학습·검증에 걸치면 배경을
외운다 — 이 프로젝트가 0.642 를 폐기한 이유가 그것이다. 규약은
`ml_core` 를 쓰고, 기준선(다수 클래스)을 **먼저** 찍는다.

## 크롭 캐시

23,450개 크롭을 매 에폭 JPEG 7,590장에서 다시 자르면 IO 로 죽는다.
한 번 추출해 uint8 로 캐시한다(64×64×3 → 288MB, RAM 에 올라간다).

    python competition/src/train_posture_cnn.py --cache      # 크롭 추출만
    python competition/src/train_posture_cnn.py --quick      # 1폴드 속도 측정
    python competition/src/train_posture_cnn.py              # 전체 LOVO
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

CROP = 64                      # 크롭 한 변(px). CPU 4스레드에 맞춘 크기.
CACHE = os.path.join(ROOT, "data", "posture_crops_img.npz")
OUT_JSON = os.path.join(ROOT, "data", "posture_cnn.json")
CEILING = 0.861                # bbox 기하의 원리적 상한 — 넘어야 의미가 있다
MIN_FOLD = 150                 # posture_crossview 와 같은 기준
PAD = 0.12                     # bbox 주변 여유. 머리 끝이 잘리면 방향이 사라진다


def build_cache(rebuild: bool = False) -> tuple:
    """bbox 로 크롭을 잘라 uint8 캐시로. 이미지당 한 번만 연다."""
    import posture_crossview as pc
    full, _X, classes = pc.load()
    if os.path.exists(CACHE) and not rebuild:
        z = np.load(CACHE, allow_pickle=True)
        if len(z["img"]) == len(full):
            return z["img"], full, classes
        print("  캐시 행 수가 안 맞는다 — 다시 만든다")

    import cv2
    src = os.path.join(_img_root(), "")
    imgs = np.zeros((len(full), CROP, CROP, 3), np.uint8)
    t0, miss = time.time(), 0
    # **이미지당 한 번만 연다.** 행 순서로 읽으면 같은 JPEG 을 수십 번 연다.
    for k, (iid, grp) in enumerate(full.groupby("image_id", sort=False)):
        p = _find(src, str(iid))
        if p is None:
            miss += len(grp)
            continue
        im = cv2.imread(p)
        if im is None:
            miss += len(grp)
            continue
        H, W = im.shape[:2]
        for i, r in zip(grp.index, grp.itertuples(index=False)):
            px, py = r.w * PAD, r.h * PAD
            x0 = max(0, int(r.x - px)); y0 = max(0, int(r.y - py))
            x1 = min(W, int(r.x + r.w + px)); y1 = min(H, int(r.y + r.h + py))
            if x1 - x0 < 4 or y1 - y0 < 4:
                miss += 1
                continue
            imgs[full.index.get_loc(i)] = cv2.resize(
                im[y0:y1, x0:x1], (CROP, CROP), interpolation=cv2.INTER_AREA)
        if k % 800 == 0 and k:
            print(f"    {k} 장 · {time.time()-t0:.0f}s")
    print(f"  크롭 {len(full):,}개 추출 {time.time()-t0:.0f}s · 실패 {miss}")
    np.savez_compressed(CACHE, img=imgs)
    return imgs, full, classes


def _img_root() -> str:
    import posture_features as pf
    return pf.COMP


def _find(root: str, iid: str) -> str | None:
    for sub in ("train1_images", "train2_images", "test_images"):
        for ext in ("", ".jpg", ".png"):
            p = os.path.join(root, sub, iid + ext)
            if os.path.exists(p):
                return p
    return None


# -- 모델 ------------------------------------------------------------------
def make_net(n_cls: int):
    """작은 CNN. CPU 4스레드에서 도는 크기로 잡는다.

    사전학습 백본을 쓰면 좋겠지만 가중치 다운로드가 필요하고, 여기서
    묻는 건 "픽셀에 방향 정보가 있는가" 라 작은 모델로도 답이 나온다.
    """
    import torch.nn as nn
    def blk(i, o):
        return nn.Sequential(nn.Conv2d(i, o, 3, padding=1), nn.BatchNorm2d(o),
                             nn.ReLU(inplace=True), nn.MaxPool2d(2))
    return nn.Sequential(
        blk(3, 24), blk(24, 48), blk(48, 96), blk(96, 128),
        nn.AdaptiveAvgPool2d(1), nn.Flatten(),
        nn.Dropout(0.3), nn.Linear(128, n_cls))


def train_fold(Xtr, ytr, Xte, n_cls, epochs: int, seed: int = 0,
               bs: int = 96, lr: float = 3e-3, log: bool = False):
    """한 폴드 학습 → 검증 예측.

    **좌우 뒤집기 증강은 쓰지 않는다.** 좌횡와를 뒤집으면 우횡와가 되므로
    라벨이 바뀐다 — 이 과제에서 가장 하기 쉬운 실수다.
    """
    import torch
    import torch.nn as nn
    torch.manual_seed(seed)
    torch.set_num_threads(os.cpu_count() or 4)

    net = make_net(n_cls)
    opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
    # 클래스가 치우쳐 있다(Standing 9,928 vs Sitting 695) → 가중 손실
    cnt = np.bincount(ytr, minlength=n_cls).astype(np.float32)
    w = torch.tensor((cnt.sum() / np.maximum(cnt, 1)) ** 0.5, dtype=torch.float32)
    lossf = nn.CrossEntropyLoss(weight=w / w.mean())
    sched = torch.optim.lr_scheduler.OneCycleLR(
        opt, max_lr=lr, total_steps=max(1, epochs * (len(Xtr) // bs + 1)))

    xt = torch.from_numpy(Xtr).permute(0, 3, 1, 2).float().div_(255)
    yt = torch.from_numpy(ytr).long()
    for ep in range(epochs):
        net.train()
        perm = torch.randperm(len(xt))
        tot = 0.0
        for i in range(0, len(perm), bs):
            idx = perm[i:i + bs]
            xb = xt[idx]
            if torch.rand(1).item() < 0.5:          # 밝기 지터(방향 보존)
                xb = (xb * (0.85 + 0.3 * torch.rand(1))).clamp_(0, 1)
            opt.zero_grad()
            out = net(xb)
            loss = lossf(out, yt[idx])
            loss.backward()
            opt.step()
            if sched.last_epoch < sched.total_steps - 1:
                sched.step()
            tot += float(loss) * len(idx)
        if log:
            print(f"      ep{ep+1} loss {tot/len(xt):.3f}")

    net.eval()
    xe = torch.from_numpy(Xte).permute(0, 3, 1, 2).float().div_(255)
    preds = []
    with torch.no_grad():
        for i in range(0, len(xe), 256):
            preds.append(net(xe[i:i + 256]).argmax(1).numpy())
    return np.concatenate(preds) if preds else np.zeros(0, int)


# -- 실행 ------------------------------------------------------------------
def run(epochs: int = 8, quick: bool = False) -> dict:
    import pandas as pd
    import ml_core as mc

    imgs, full, classes = build_cache()
    full = full.reset_index(drop=True)
    lab5 = full["cls"].to_numpy()
    c2i = {c: i for i, c in enumerate(classes)}
    y5 = np.array([c2i[c] for c in lab5])

    vs = full["view"].value_counts()
    views = [v for v in sorted(vs.index) if vs[v] >= MIN_FOLD]
    if quick:
        views = views[:1]
    print(f"\n  폴드 {len(views)}개 · 크롭 {len(full):,} · {CROP}×{CROP}px")

    rows5, rows3, lr_rows, t0 = [], [], [], time.time()
    LEFT, RIGHT = c2i["Lateral_lying_left"], c2i["Lateral_lying_right"]
    for v in views:
        m = (full["view"] == v).to_numpy()
        te = time.time()
        p5 = train_fold(imgs[~m], y5[~m], imgs[m], len(classes), epochs)
        yv = y5[m]
        rows5.append(mc.score(yv, p5))
        # 3클래스는 5클래스 예측을 접어서 낸다(같은 모델, 같은 학습)
        fold3 = np.array([pc_to3(classes[i]) for i in p5])
        true3 = full.loc[m, "cls3"].to_numpy()
        rows3.append(mc.score(true3, fold3))
        # **좌/우만 떼어낸 이진** — 이게 이 실험의 핵심 질문이다
        lr = np.isin(yv, [LEFT, RIGHT])
        if lr.sum() >= 30:
            lr_rows.append(mc.score(yv[lr], p5[lr]))
        print(f"    {v:<16} n={int(m.sum()):>5}  5cls {rows5[-1]['acc']:.3f}"
              f"  3cls {rows3[-1]['acc']:.3f}"
              f"  좌우 {(lr_rows[-1]['acc'] if lr_rows else float('nan')):.3f}"
              f"  ({time.time()-te:.0f}s)")

    out = {
        "crop_px": CROP, "epochs": epochs, "folds": len(views),
        "cnn_cls5": mc.weighted(rows5), "cnn_cls3": mc.weighted(rows3),
        "left_right_binary": mc.weighted(lr_rows),
        "ceiling_bbox": CEILING, "seconds": round(time.time() - t0),
    }
    # 기준선 — ml_core 로 같은 폴드 규약에서 낸다
    out["baseline_cls5"] = mc.majority_baseline(full, "cls", "view", MIN_FOLD)
    out["baseline_cls3"] = mc.majority_baseline(full, "cls3", "view", MIN_FOLD)
    return out


def pc_to3(c: str) -> str:
    import posture_crossview as pc
    return pc.TO_ESTRUS[c]


def report(r: dict) -> None:
    import ml_core as mc
    print("\n" + "=" * 74)
    print("  자세 CNN — 원본 크롭 픽셀로 좌/우를 가를 수 있는가")
    print("=" * 74)
    mc.report("5클래스 (원본 과제)", r["cnn_cls5"], r["baseline_cls5"])
    mc.report("발정 3클래스 (응용 지표)", r["cnn_cls3"], r["baseline_cls3"])

    a5, lr = r["cnn_cls5"]["acc"], r["left_right_binary"]
    print(f"\n  ── 이 실험의 핵심 ──")
    print(f"  bbox 기하의 원리적 상한   {r['ceiling_bbox']:.3f}")
    print(f"  CNN 5클래스 정확도        {a5:.3f}  "
          f"({'✅ 상한 돌파' if a5 > r['ceiling_bbox'] else '❌ 상한 이하'})")
    print(f"  좌/우 횡와 이진 정확도    {lr['acc']:.3f}  (동전 = 0.500, "
          f"표본 {lr['n']:,})")
    if lr["acc"] < 0.60:
        print("     → 여전히 동전에 가깝다. 크롭 픽셀에도 방향 정보가")
        print("       충분치 않거나, 이 해상도·모델로는 못 잡는다는 뜻이다.")
    else:
        print("     → 좌/우가 갈린다. bbox 로는 원리상 불가능했던 부분이다.")
    print(f"\n  학습 {r['seconds']}s · {r['folds']}폴드 · {r['epochs']}에폭 "
          f"· 크롭 {r['crop_px']}px · CPU")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="train_posture_cnn")
    ap.add_argument("--cache", action="store_true", help="크롭 추출만")
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--quick", action="store_true", help="1폴드 속도 측정")
    ap.add_argument("--epochs", type=int, default=8)
    a = ap.parse_args(argv)

    if a.cache or a.rebuild:
        imgs, full, _c = build_cache(rebuild=a.rebuild)
        print(f"  캐시: {CACHE} ({os.path.getsize(CACHE)/1e6:.0f}MB)")
        return 0
    r = run(epochs=a.epochs, quick=a.quick)
    report(r)
    if not a.quick:
        json.dump(r, open(OUT_JSON, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\n저장: {os.path.relpath(OUT_JSON, ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
