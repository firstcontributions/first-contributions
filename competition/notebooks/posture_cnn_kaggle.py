# ========================================================================
# 자세 CNN — 원리적 상한 0.861 을 넘을 수 있는가
# 캐글: New Notebook → Add Input 으로 데이터 붙이고
#       Accelerator = GPU → 이 전체를 셀 하나에 붙여넣고 실행
# ========================================================================


# # 자세 CNN — 원리적 상한 0.861 을 넘을 수 있는가
#
# ## 실행 전 설정 셋 (오른쪽 패널)
#
# | 설정 | 값 | 왜 |
# |---|---|---|
# | **Add Input** | Competition `multi-view-pig-posture-recognition` | 데이터 |
# | **Accelerator** | **GPU** (T4 ×2 또는 P100) | CPU 로는 LOVO 7폴드가 50분 |
# | **Internet** | **On** | resnet18 사전학습 가중치를 받는다 |
#
# > 인터넷을 끄면 가중치를 못 받아 **scratch 학습으로 자동 폴백**한다. 죽지는
# > 않지만 23,450장으로 밑바닥부터 배우는 셈이라 성능이 크게 떨어진다.
# > 셀 출력에 `사전학습 가중치 못 받음 → scratch` 가 찍히면 그 상태다.
#
# ## 이 노트북이 묻는 것 하나
#
# 좌/우 횡와는 **bbox 기하로 원리상 구분 불가**다. 둘 다 옆으로 누운 같은
# 모양의 상자라, 기존 모델은 좌횡와를 좌 157 / 우 210 으로 사실상 동전을
# 던진다. 두 클래스가 전체의 27.8% 이므로 **5클래스 상한이 1.0 이 아니라
# 0.861** 이다.
#
# 기존 파이프라인은 크롭을 60차원으로 요약해 쓴다 — 방향 정보가 이미
# 뭉개진다. **원본 크롭 픽셀을 직접 보는 CNN 만이 머리 방향을 볼 수 있고,
# 그래야 상한 자체가 올라간다.**
#
# 재는 것 셋:
# 1. 5클래스 정확도가 **0.861 을 넘는가**
# 2. **좌/우 횡와만 떼어낸 이진 정확도** — 0.5 근처면 여전히 동전
# 3. 발정 3클래스(기립/기좌/횡와) — 응용 지표. 기존 0.636
#
# ## 검증
#
# 카메라(뷰)를 **통째로** 빼는 LOVO. 같은 카메라가 학습·검증에 걸치면
# 배경을 외운다 — 이 프로젝트가 0.642 를 폐기한 이유가 그것이다.
#
# ## 밟기 쉬운 함정 둘 — 둘 다 아래 셀에서 막아 뒀다
#
# 1. **`train1` + `train2` 를 그냥 concat 하면 안 된다.** 두 CSV 는 이미지
#    3,090장을 공유한다. 그대로 합치면 46,384행이 되는데 실제 고유 상자는
#    23,450개다. 중복이 train/valid 로 갈리면 정답을 외운다 — 이 프로젝트가
#    자세 정확도 **0.642 를 폐기한 원인이 정확히 이것**이다.
# 2. **좌우 뒤집기 증강을 쓰면 안 된다.** 좌횡와를 뒤집으면 우횡와가 되므로
#    라벨이 바뀐다. 이 과제에서 가장 하기 쉬운 실수다.

import os, ast, time, json
import numpy as np, pandas as pd, torch
IN = "/kaggle/input/multi-view-pig-posture-recognition"
print("입력:", sorted(os.listdir(IN))[:8])
DEV = "cuda" if torch.cuda.is_available() else "cpu"
print("장치:", DEV, torch.cuda.get_device_name(0) if DEV == "cuda" else "")
CEILING, MIN_FOLD, CROP, PAD = 0.861, 150, 96, 0.12

# ── 평가 규약 (competition/src/ml_core.py 와 같은 내용을 인라인) ──────────
# 이 프로젝트가 비싸게 배운 것 넷:
#  1) 기준선(다수 클래스)을 **먼저** 찍는다 — 폴리곤 실험에서 기준선을
#     계산해 놓고 출력을 안 해 0.615 를 개선으로 읽을 뻔했다(기준선 0.636).
#  2) 정확도와 Macro-F1 을 **같이** 낸다. 클래스가 치우치면 정확도가 신호를
#     가린다 — 자세 기하 모델은 acc 0.414 로 기준선 0.423 에 못 미쳤지만
#     MF1 은 0.119 → 0.228 이었다. 그건 '미달' 이 아니다.
#  3) 그룹(카메라/개체)을 **통째로** 빼고 검증한다. train1↔train2 가 이미지
#     3,090장을 공유해 0.642 가 나왔고, 못 본 카메라로 재면 0.4 대였다.
#  4) 표본이 작은 폴드는 집계에서 뺀다 — 분산에 묻혀 순서가 뒤집힌다.
from sklearn.metrics import accuracy_score, f1_score
import numpy as np, pandas as pd

MARGIN = 0.005

def score(y_true, y_pred):
    return {"acc": float(accuracy_score(y_true, y_pred)),
            "mf1": float(f1_score(y_true, y_pred, average="macro",
                                  zero_division=0)),
            "n": int(len(y_true))}

def weighted(rows):
    """폴드별 결과를 **표본 수로 가중**해 합친다(단순 평균은 작은 폴드에 끌린다)."""
    if not rows:
        return {"acc": float("nan"), "mf1": float("nan"), "n": 0, "folds": 0}
    r = pd.DataFrame(rows); w = r["n"] / r["n"].sum()
    return {"acc": round(float((r["acc"] * w).sum()), 3),
            "mf1": round(float((r["mf1"] * w).sum()), 3),
            "n": int(r["n"].sum()), "folds": int(len(r)),
            "acc_min": round(float(r["acc"].min()), 3),
            "acc_max": round(float(r["acc"].max()), 3)}

def report(name, model, base):
    d_acc = model["acc"] - base["acc"]; d_mf1 = model["mf1"] - base["mf1"]
    if d_mf1 > MARGIN and d_acc < -MARGIN:
        v = "정확도만 미달(불균형에 가림)"
    elif d_acc < -MARGIN or d_mf1 < -MARGIN:
        v = "기준선 미달"
    elif abs(d_acc) <= MARGIN and abs(d_mf1) <= MARGIN:
        v = "기준선과 같음"
    else:
        v = "개선"
    print(f"\n=== {name} ===")
    print(f"  기준선(다수 클래스)  acc {base['acc']:.3f} · MF1 {base['mf1']:.3f}"
          f"   ← 먼저 본다")
    print(f"  모델                acc {model['acc']:.3f} · MF1 {model['mf1']:.3f}"
          f"   ({d_acc:+.3f} / {d_mf1:+.3f})   [{v}]")
    print(f"  폴드 {model.get('folds',0)}개 · 표본 {model.get('n',0):,} · "
          f"폴드별 {model.get('acc_min',0):.3f}~{model.get('acc_max',0):.3f}")
    if v == "기준선 미달":
        print("  ❌ 기준선보다 못하다. 개선이 아니다.")
    elif v.startswith("정확도만"):
        print("  ⚠️ 정확도는 아래인데 MF1 은 위 — 불균형이 정확도를 가린다.")
    return {"verdict": v, "d_acc": round(d_acc, 3), "d_mf1": round(d_mf1, 3)}

# ── 라벨 로드 ────────────────────────────────────────────────────────────
def load_split(fn):
    d = pd.read_csv(os.path.join(IN, fn))
    bb = d["bbox"].apply(ast.literal_eval)
    for i, c in enumerate(("x", "y", "w", "h")):
        d[c] = bb.apply(lambda b, i=i: float(b[i]))
    # 뷰(pen_객체_cam) — 누수 방지 그룹 키
    d["view"] = d["image_id"].str.rsplit("_", n=2).str[0]
    d["split"] = fn.split(".")[0]
    return d

a, b = load_split("train1.csv"), load_split("train2.csv")
raw = pd.concat([a, b], ignore_index=True)

# ⚠️ **train1 과 train2 는 이미지를 공유한다.** 그냥 concat 하면 같은 상자를
# 두 번 세고, 그게 train/valid 로 갈리면 정답을 외운다 — 이 프로젝트가
# 자세 정확도 0.642 를 폐기한 원인이 정확히 이것이다.
span = raw.groupby("image_id")["split"].nunique()
full = raw.drop_duplicates(subset=["image_id", "bbox"]).reset_index(drop=True)
print(f"concat {len(raw):,} → 중복 제거 {len(full):,}"
      f"  (두 split 에 걸친 이미지 {int((span > 1).sum()):,}장)")

classes = open(os.path.join(IN, "pig_posture_classes.txt")).read().split()
full["cls"] = full["class_id"].map(lambda i: classes[i])
TO3 = {"Lateral_lying_left": "lying", "Lateral_lying_right": "lying",
       "Sternal_lying": "lying", "Sitting": "sitting", "Standing": "standing"}
full["cls3"] = full["cls"].map(TO3)
print(full.shape, "· 뷰", full["view"].nunique())
print(full["cls"].value_counts().to_dict())
assert len(full) < len(raw), "중복 제거가 안 됐다"

# ── 크롭 추출 (이미지당 한 번만 연다) ────────────────────────────────────
import cv2
def find_img(iid):
    for sub in ("train1_images", "train2_images"):
        p = os.path.join(IN, sub, iid if iid.endswith((".jpg", ".png")) else iid + ".jpg")
        if os.path.exists(p):
            return p
    return None

full = full.reset_index(drop=True)
imgs = np.zeros((len(full), CROP, CROP, 3), np.uint8)
t0, miss = time.time(), 0
for k, (iid, grp) in enumerate(full.groupby("image_id", sort=False)):
    p = find_img(str(iid))
    im = cv2.imread(p) if p else None
    if im is None:
        miss += len(grp); continue
    H, W = im.shape[:2]
    for i, r in zip(grp.index, grp.itertuples(index=False)):
        px, py = r.w * PAD, r.h * PAD
        x0, y0 = max(0, int(r.x - px)), max(0, int(r.y - py))
        x1, y1 = min(W, int(r.x + r.w + px)), min(H, int(r.y + r.h + py))
        if x1 - x0 < 4 or y1 - y0 < 4:
            miss += 1; continue
        imgs[i] = cv2.resize(im[y0:y1, x0:x1], (CROP, CROP), cv2.INTER_AREA)
    if k % 1500 == 0 and k:
        print(f"  {k}장 {time.time()-t0:.0f}s")
print(f"크롭 {len(full):,} · 실패 {miss} · {time.time()-t0:.0f}s")

# ── 모델 ────────────────────────────────────────────────────────────────
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

def make_net(n_cls, pretrained=True):
    """GPU 라 resnet18 을 쓴다. 인터넷이 꺼져 있으면 자동으로 scratch."""
    from torchvision.models import resnet18
    try:
        m = resnet18(weights="IMAGENET1K_V1" if pretrained else None)
    except Exception as e:
        print("  사전학습 가중치 못 받음 → scratch:", type(e).__name__)
        m = resnet18(weights=None)
    m.fc = nn.Linear(m.fc.in_features, n_cls)
    return m

def train_fold(Xtr, ytr, Xte, n_cls, epochs=12, bs=128, lr=3e-4, seed=0):
    torch.manual_seed(seed)
    net = make_net(n_cls).to(DEV)
    cnt = np.bincount(ytr, minlength=n_cls).astype(np.float32)
    w = torch.tensor((cnt.sum() / np.maximum(cnt, 1)) ** 0.5,
                     dtype=torch.float32, device=DEV)
    lossf = nn.CrossEntropyLoss(weight=w / w.mean())
    opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
    ds = TensorDataset(torch.from_numpy(Xtr).permute(0, 3, 1, 2),
                       torch.from_numpy(ytr).long())
    dl = DataLoader(ds, batch_size=bs, shuffle=True, num_workers=2,
                    pin_memory=True, drop_last=False)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=lr,
                                                total_steps=epochs * len(dl))
    scaler = torch.amp.GradScaler("cuda", enabled=(DEV == "cuda"))
    for ep in range(epochs):
        net.train()
        for xb, yb in dl:
            xb = xb.to(DEV, non_blocking=True).float().div_(255)
            # 밝기 지터만. **좌우 뒤집기는 라벨을 바꾸므로 금지.**
            if torch.rand(1).item() < 0.5:
                xb = (xb * (0.85 + 0.3 * torch.rand(1, device=DEV))).clamp_(0, 1)
            yb = yb.to(DEV, non_blocking=True)
            opt.zero_grad(set_to_none=True)
            with torch.amp.autocast("cuda", enabled=(DEV == "cuda")):
                loss = lossf(net(xb), yb)
            scaler.scale(loss).backward(); scaler.step(opt); scaler.update()
            sched.step()
    net.eval(); out = []
    with torch.no_grad(), torch.amp.autocast("cuda", enabled=(DEV == "cuda")):
        for i in range(0, len(Xte), 512):
            xb = torch.from_numpy(Xte[i:i+512]).permute(0, 3, 1, 2)
            xb = xb.to(DEV).float().div_(255)
            out.append(net(xb).argmax(1).cpu().numpy())
    return np.concatenate(out)

# ── LOVO (카메라를 통째로 뺀다) ──────────────────────────────────────────
c2i = {c: i for i, c in enumerate(classes)}
y5 = full["cls"].map(c2i).to_numpy()
LEFT, RIGHT = c2i["Lateral_lying_left"], c2i["Lateral_lying_right"]

vs = full["view"].value_counts()
views = [v for v in sorted(vs.index) if vs[v] >= MIN_FOLD]
print("폴드:", views)

rows5, rows3, lrs, per_fold = [], [], [], []
for v in views:
    m = (full["view"] == v).to_numpy()
    t = time.time()
    p5 = train_fold(imgs[~m], y5[~m], imgs[m], len(classes))
    yv = y5[m]
    s5 = score(yv, p5); rows5.append(s5)
    p3 = np.array([TO3[classes[i]] for i in p5])
    s3 = score(full.loc[m, "cls3"].to_numpy(), p3); rows3.append(s3)
    sel = np.isin(yv, [LEFT, RIGHT])
    slr = score(yv[sel], p5[sel]) if sel.sum() >= 30 else None
    if slr: lrs.append(slr)
    per_fold.append({"view": v, "n": int(m.sum()), "cls5": s5["acc"],
                     "cls3": s3["acc"],
                     "lr": (slr["acc"] if slr else None)})
    print(f"  {v:<16} n={int(m.sum()):>5}  5cls {s5['acc']:.3f}  "
          f"3cls {s3['acc']:.3f}  좌우 {(slr['acc'] if slr else float('nan')):.3f}"
          f"  ({time.time()-t:.0f}s)")

# ── 기준선 먼저, 그다음 결과 ─────────────────────────────────────────────
def majority_lovo(df, label, group, min_fold=MIN_FOLD):
    vs = df[group].value_counts()
    rows = []
    for v in sorted(vs.index):
        if vs[v] < min_fold: continue
        m = (df[group] == v).to_numpy()
        maj = df.loc[~m, label].value_counts().idxmax()
        rows.append(score(df.loc[m, label], np.full(int(m.sum()), maj)))
    return weighted(rows)

m5, m3, mlr = weighted(rows5), weighted(rows3), weighted(lrs)
b5 = majority_lovo(full, "cls", "view")
b3 = majority_lovo(full, "cls3", "view")
report("5클래스 (원본 과제)", m5, b5)
report("발정 3클래스 (응용 지표)", m3, b3)

print(f"\n  ── 이 실험의 핵심 ──")
print(f"  bbox 기하의 원리적 상한   {CEILING:.3f}")
print(f"  CNN 5클래스 정확도        {m5['acc']:.3f}  "
      f"({'✅ 상한 돌파' if m5['acc'] > CEILING else '❌ 상한 이하'})")
print(f"  좌/우 횡와 이진 정확도    {mlr['acc']:.3f}  (동전 = 0.500, 표본 {mlr['n']:,})")
print("  폴드별 좌/우:", [(p["view"], p["lr"]) for p in per_fold])
print("""
  읽는 법:
   · 0.5 근처  → 크롭 픽셀에도 방향 정보가 없거나 이 해상도로는 못 잡는다
   · 0.5 훨씬 아래 → **체계적 반전**. 카메라가 반대편에서 찍으면 같은 자세가
     좌↔우로 보인다는 뜻이다. 그렇다면 좌/우는 '개체 기준' 라벨이고
     카메라 방향을 모르면 부호를 정할 수 없다 — 모델 문제가 아니다.
   · 0.6 이상  → 갈린다. bbox 로는 원리상 불가능했던 부분이다.
""")
json.dump({"cls5": m5, "cls3": m3, "left_right": mlr, "baseline_cls5": b5,
           "baseline_cls3": b3, "ceiling": CEILING, "per_fold": per_fold},
          open("/kaggle/working/posture_cnn.json", "w"),
          ensure_ascii=False, indent=1)
print("저장: /kaggle/working/posture_cnn.json")

