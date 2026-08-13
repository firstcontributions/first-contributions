"""행동 인식 시퀀스 모델 — 프레임 하나가 아니라 **구간**을 본다.

기존 모델은 프레임 단위 기하 피처로 acc 0.516 / MF1 0.386 이다. 그런데
행동은 정의상 시간에 걸쳐 있다 — `walk` 와 `standing` 은 한 프레임만
보면 같은 상자이고, 갈리는 건 **다음 프레임에 움직였는가**다. 롤링 윈도우
피처를 붙였을 때 +0.042 가 나온 것도 같은 이유다(temporal_features).

여기서는 요약 통계 대신 **원시 시퀀스를 그대로** 1D CNN 에 넣는다.
프레임당 5개 기하값 × 앞뒤 W프레임 창 → (채널, 시간) 텐서.

## 검증

개체(individual_id)를 통째로 나누는 GroupKFold(5). 기존 행동 모델과 같은
규약이라 숫자를 나란히 놓을 수 있다. **같은 개체가 학습·검증에 걸치면
그 돼지의 생김새를 외운다.**

라벨은 기존과 같이 100건 미만 클래스를 `other` 로 묶는다(chase 1건,
jumpontopof 6건 같은 걸 그대로 두면 폴드마다 있고 없고가 갈린다).

    python competition/src/train_behavior_seq.py --quick
    python competition/src/train_behavior_seq.py --epochs 25
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

CSV = os.path.join(ROOT, "data", "edinburgh_frames.csv")
OUT_JSON = os.path.join(ROOT, "data", "behavior_seq.json")
GEOM = ["bbox_w", "bbox_h", "aspect_ratio", "centroid_x", "centroid_y"]
WIN = 15                # 앞뒤로 볼 프레임 수(홀수). 15 ≈ 0.5~1초 구간.
MIN_COUNT = 100         # 기존 모델과 같은 기준 — 미만은 other 로 묶는다
MAX_GAP = 5             # 프레임 간격이 이보다 크면 다른 구간으로 본다


def load() -> pd.DataFrame:
    d = pd.read_csv(CSV, encoding="utf-8-sig")
    d = d[d["visible"] & d["behavior"].notna()].copy()
    d = d.dropna(subset=GEOM)
    vc = d["behavior"].value_counts()
    keep = set(vc[vc >= MIN_COUNT].index)
    d["behavior"] = d["behavior"].where(d["behavior"].isin(keep), "other")
    return d.sort_values(["individual_id", "frame_idx"]).reset_index(drop=True)


def sequences(d: pd.DataFrame) -> np.ndarray:
    """각 행 주변 ±WIN//2 프레임의 기하값 → (N, 채널, 시간).

    **끊긴 구간을 이어 붙이지 않는다.** 프레임 간격이 MAX_GAP 을 넘으면
    다른 장면이므로, 그 너머는 가장자리 프레임으로 채운다(복제 패딩).
    이걸 안 하면 150프레임 떨어진 장면이 한 창에 들어온다 — 실제로 간격
    150인 구간이 있다.
    """
    half = WIN // 2
    # 개체별 위치 좌표를 그 개체 기준으로 중심화 → 우리 안 절대 위치를
    # 외우지 못하게 한다. 크기(bbox)는 그대로 둔다(원근 정보).
    d = d.copy()
    for c in ("centroid_x", "centroid_y"):
        d[c] = d[c] - d.groupby("individual_id")[c].transform("median")
    F = d[GEOM].to_numpy(np.float32)
    idx = d["frame_idx"].to_numpy()
    gid = d["individual_id"].to_numpy()
    out = np.zeros((len(d), len(GEOM), WIN), np.float32)
    start = 0
    for i in range(1, len(d) + 1):
        if i == len(d) or gid[i] != gid[start]:
            seg = np.arange(start, i)
            # 개체 안에서도 간격이 크면 끊는다
            brk = [0] + list(np.where(np.diff(idx[seg]) > MAX_GAP)[0] + 1) \
                + [len(seg)]
            for a, b in zip(brk[:-1], brk[1:]):
                sub = seg[a:b]
                for k, r in enumerate(sub):
                    lo, hi = k - half, k + half + 1
                    take = np.clip(np.arange(lo, hi), 0, len(sub) - 1)
                    out[r] = F[sub[take]].T
            start = i
    return out


def make_net(n_ch: int, n_cls: int):
    import torch.nn as nn
    def blk(i, o, k=5):
        return nn.Sequential(nn.Conv1d(i, o, k, padding=k // 2),
                             nn.BatchNorm1d(o), nn.ReLU(inplace=True))
    return nn.Sequential(
        blk(n_ch, 48), blk(48, 64), nn.MaxPool1d(2),
        blk(64, 96), nn.AdaptiveAvgPool1d(1), nn.Flatten(),
        nn.Dropout(0.25), nn.Linear(96, n_cls))


def train_fold(Xtr, ytr, Xte, n_cls, epochs: int, seed: int = 0,
               bs: int = 128, lr: float = 4e-3):
    import torch
    import torch.nn as nn
    torch.manual_seed(seed)
    torch.set_num_threads(os.cpu_count() or 4)

    # 표준화는 **학습 폴드 통계로만** 한다. 검증 폴드 통계를 쓰면 누수다.
    mu = Xtr.mean((0, 2), keepdims=True)
    sd = Xtr.std((0, 2), keepdims=True) + 1e-6
    xt = torch.from_numpy((Xtr - mu) / sd)
    xe = torch.from_numpy((Xte - mu) / sd)
    yt = torch.from_numpy(ytr).long()

    net = make_net(Xtr.shape[1], n_cls)
    opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
    cnt = np.bincount(ytr, minlength=n_cls).astype(np.float32)
    w = torch.tensor((cnt.sum() / np.maximum(cnt, 1)) ** 0.5, dtype=torch.float32)
    lossf = nn.CrossEntropyLoss(weight=w / w.mean())
    sched = torch.optim.lr_scheduler.OneCycleLR(
        opt, max_lr=lr, total_steps=max(1, epochs * (len(xt) // bs + 1)))

    for _ep in range(epochs):
        net.train()
        perm = torch.randperm(len(xt))
        for i in range(0, len(perm), bs):
            idx = perm[i:i + bs]
            opt.zero_grad()
            loss = lossf(net(xt[idx]), yt[idx])
            loss.backward()
            opt.step()
            if sched.last_epoch < sched.total_steps - 1:
                sched.step()
    net.eval()
    with torch.no_grad():
        return net(xe).argmax(1).numpy()


def run(epochs: int = 25, k: int = 5, quick: bool = False) -> dict:
    import ml_core as mc
    d = load()
    if quick:
        keep = d["individual_id"].drop_duplicates().head(30)
        d = d[d["individual_id"].isin(keep)].reset_index(drop=True)
    X = sequences(d)
    classes = sorted(d["behavior"].unique())
    c2i = {c: i for i, c in enumerate(classes)}
    y = d["behavior"].map(c2i).to_numpy()
    d = d.assign(_row=np.arange(len(d)))
    print(f"  행 {len(d):,} · 개체 {d.individual_id.nunique()} · "
          f"클래스 {len(classes)} · 창 {WIN}프레임")

    t0 = time.time()

    def fp(tr, te):
        return train_fold(X[tr["_row"].to_numpy()], y[tr["_row"].to_numpy()],
                          X[te["_row"].to_numpy()], len(classes), epochs)

    model = mc.group_kfold(d, "behavior", "individual_id",
                           lambda tr, te: [classes[i] for i in fp(tr, te)], k)
    base = mc.majority_baseline_kfold(d, "behavior", "individual_id", k)
    return {"seq_cnn": model, "baseline": base, "classes": classes,
            "window": WIN, "epochs": epochs, "n_rows": int(len(d)),
            "n_individuals": int(d.individual_id.nunique()),
            "prev_frame_model": {"acc": 0.516, "mf1": 0.386},
            "seconds": round(time.time() - t0)}


def report(r: dict) -> None:
    import ml_core as mc
    print("\n" + "=" * 74)
    print("  행동 인식 — 프레임 하나 vs 구간(시퀀스)")
    print("=" * 74)
    mc.report(f"시퀀스 1D-CNN ({r['window']}프레임 창)", r["seq_cnn"],
              r["baseline"])
    p = r["prev_frame_model"]
    m = r["seq_cnn"]
    print(f"\n  기존 프레임 단위 모델   acc {p['acc']:.3f} · MF1 {p['mf1']:.3f}")
    print(f"  시퀀스 모델            acc {m['acc']:.3f} · MF1 {m['mf1']:.3f}"
          f"   ({m['acc']-p['acc']:+.3f} / {m['mf1']-p['mf1']:+.3f})")
    print(f"\n  학습 {r['seconds']}s · {m.get('scheme','')} · "
          f"{r['epochs']}에폭 · CPU")
    print("  ※ 기존 모델은 외형 피처도 썼다. 여기 시퀀스 모델은 기하 5개만")
    print("    보므로 완전한 동일 조건 비교는 아니다.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="train_behavior_seq")
    ap.add_argument("--epochs", type=int, default=25)
    ap.add_argument("--folds", type=int, default=5)
    ap.add_argument("--quick", action="store_true")
    a = ap.parse_args(argv)
    r = run(epochs=a.epochs, k=a.folds, quick=a.quick)
    report(r)
    if not a.quick:
        json.dump(r, open(OUT_JSON, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\n저장: {os.path.relpath(OUT_JSON, ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
