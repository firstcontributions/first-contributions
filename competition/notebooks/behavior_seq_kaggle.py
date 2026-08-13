# ========================================================================
# 행동 인식 시퀀스 모델 — 프레임 하나가 아니라 구간을 본다
# 캐글: New Notebook → Add Input 으로 데이터 붙이고
#       Accelerator = GPU → 이 전체를 셀 하나에 붙여넣고 실행
# ========================================================================


# # 행동 인식 시퀀스 모델 — 프레임 하나가 아니라 **구간**을 본다
#
# ## 실행 전 설정 (오른쪽 패널)
#
# | 설정 | 값 |
# |---|---|
# | **Add Input** | Dataset `jackbyte/edinburgh-pig-behaviour-annotated` (CC BY-NC 4.0) |
# | **Accelerator** | **GPU** |
#
# 인터넷은 꺼도 된다 — 사전학습 가중치를 쓰지 않는다.
#
# `walk` 와 `standing` 은 한 프레임만 보면 같은 상자다. 갈리는 건 **다음
# 프레임에 움직였는가**다. 기존 프레임 단위 모델은 acc 0.516 / MF1 0.386
# 이고, 롤링 윈도우 요약을 붙였을 때 +0.042 가 나왔다. 여기서는 요약 대신
# **원시 시퀀스를 1D CNN 에 그대로** 넣는다.
#
# ## 검증
#
# 개체(individual_id)를 통째로 나누는 **GroupKFold(5)**. 같은 개체가
# 학습·검증에 걸치면 그 돼지의 생김새를 외운다. 기존 모델과 같은 규약이라
# 숫자를 나란히 놓을 수 있다.
#
# 100건 미만 클래스는 `other` 로 묶는다 — chase 1건·jumpontopof 6건을
# 그대로 두면 폴드마다 있고 없고가 갈린다.

import os, json, time, glob
import numpy as np, pandas as pd, torch
IN = "/kaggle/input/edinburgh-pig-behaviour-annotated"

def show_input_tree():
    base = "/kaggle/input"
    if not os.path.isdir(base):
        print("/kaggle/input 자체가 없다 — 캐글 노트북이 아닌 환경이다.")
        return
    items = sorted(os.listdir(base))
    if not items:
        print("=" * 62)
        print("  /kaggle/input 이 비어 있다 — **데이터가 하나도 안 붙었다.**")
        print("=" * 62)
        print("  오른쪽 패널 위 [+ Add Input] 을 누르고:")
        print("   · 자세 → 상단 탭 'Competitions' →")
        print("            multi-view-pig-posture-recognition")
        print("            (대회 규칙 동의를 안 했으면 검색에 안 뜬다.")
        print("             대회 페이지에서 'Join Competition' 먼저)")
        print("   · 행동 → 상단 탭 'Datasets' →")
        print("            jackbyte/edinburgh-pig-behaviour-annotated")
        print("  붙이면 세션이 재시작되니, 그 뒤 셀을 다시 실행한다.")
        print("  ※ 가속기를 바꾸면 새 세션이라 입력이 안 따라올 때가 있다.")
        return
    print("붙어 있는 입력:", items)
    print("찾는 파일이 없다 — 아래 구조에서 경로를 확인할 것:")
    # 캐글은 notebooks/<user>/ · datasets/<user>/<slug>/ 로 감쌀 때가 있어
    # 두 단계로는 실제 데이터가 안 보인다. 네 단계까지 판다.
    for dp, ds, fs in os.walk(base):
        rel = os.path.relpath(dp, base)
        depth = 0 if rel == "." else rel.count(os.sep) + 1
        if depth > 4:
            continue
        mark = "  " * depth
        if fs:
            print(f"  {mark}{rel}/  →  파일 {len(fs)}개: {sorted(fs)[:4]}")
        elif ds:
            print(f"  {mark}{rel}/  →  {sorted(ds)[:6]}")
        else:
            print(f"  {mark}{rel}/  →  (비어 있음)")
    print()
    print("  ※ 'notebooks/<이름>/' 이 비어 있으면 데이터셋이 아니라")
    print("    **노트북을 붙인 것**이다. Add Input 의 'Datasets' 탭에서")
    print("    다시 붙일 것.")

# P100(sm_60)은 최신 PyTorch 빌드가 못 쓴다. 미리 잡아 CPU 로 넘긴다.
def pick_device():
    if not torch.cuda.is_available():
        return "cpu"
    cap = torch.cuda.get_device_capability(0)
    name, sm = torch.cuda.get_device_name(0), f"sm_{cap[0]}{cap[1]}"
    if sm in torch.cuda.get_arch_list():
        print(f"장치: cuda · {name} ({sm})")
        return "cuda"
    print(f"⚠️ {name} ({sm}) 는 이 PyTorch 빌드가 못 쓴다 "
          f"→ Accelerator 를 'GPU T4 x2' 로 바꿀 것. 지금은 CPU 로 계속.")
    return "cpu"

DEV = pick_device()
GEOM = ["bbox_w", "bbox_h", "aspect_ratio", "centroid_x", "centroid_y"]
WIN, MIN_COUNT, MAX_GAP = 15, 100, 5
print("녹화:", sum("output.json" in f for _d, _s, f in os.walk(IN)))

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

# ── 데이터 뿌리 자동 탐색 ────────────────────────────────────────────────
# 캐글은 데이터셋을 한 단계 더 깊은 폴더에 넣을 때가 있다. 경로를 고정하면
# rows 가 비고, 빈 DataFrame 은 컬럼이 없어서 dropna 가 KeyError 를 낸다 —
# 원인과 상관없는 에러라 디버깅이 어렵다. 찾아서 쓰고, 못 찾으면 구조를 찍는다.
def find_jsons(base):
    return [dp for dp, _s, fs in os.walk(base) if "output.json" in fs]

hits = find_jsons(IN) or find_jsons("/kaggle/input")
if not hits:
    show_input_tree()
    raise RuntimeError("Edinburgh 데이터셋이 안 붙어 있다 — 위 안내대로 Add Input")
print(f"output.json {len(hits)}개 발견 · 예: "
      f"{os.path.relpath(hits[0], '/kaggle/input')}")

# ── output.json → 프레임 표 ──────────────────────────────────────────────
# 구조: { objects: [ { id, frames: [ {frameNumber, bbox:{x,y,width,height},
#                                     visible, behaviour}, ... ] }, ... ] }
rows = []
for dp in hits:
    try:
        j = json.load(open(os.path.join(dp, "output.json"), encoding="utf-8"))
    except Exception as e:
        print("  읽기 실패:", dp, type(e).__name__)
        continue
    # 녹화 이름은 **마지막 두 단계**로 짓는다(<날짜>/<녹화>). 중첩 깊이가
    # 달라져도 같은 이름이 나오도록.
    rec = "_".join(dp.rstrip(os.sep).split(os.sep)[-2:])
    for obj in j.get("objects", []):
        uid = f"{rec}#{obj.get('id')}"      # 녹화+개체로 유일 식별
        for fr in obj.get("frames", []):
            if not fr.get("visible", True) or fr.get("behaviour") is None:
                continue
            bb = fr.get("bbox") or {}
            x, y = bb.get("x"), bb.get("y")
            w, h = bb.get("width"), bb.get("height")
            if not w or not h or x is None or y is None:
                continue
            rows.append({"recording": rec, "individual_id": uid,
                         "frame_idx": int(fr["frameNumber"]),
                         "behavior": str(fr["behaviour"]),
                         "bbox_w": float(w), "bbox_h": float(h),
                         "aspect_ratio": float(w) / float(h),
                         "centroid_x": float(x) + float(w) / 2,
                         "centroid_y": float(y) + float(h) / 2})
# **비었는지를 먼저 본다.** 빈 DataFrame 은 컬럼이 없어서 dropna 가
# KeyError 를 내고, 그러면 진짜 원인(파싱 0건)이 안 보인다.
if not rows:
    j = json.load(open(os.path.join(hits[0], "output.json"), encoding="utf-8"))
    print("JSON 최상위 키:", list(j.keys()))
    o = (j.get("objects") or [{}])[0]
    print("object 키:", list(o.keys()))
    print("frame 키:", list((o.get("frames") or [{}])[0].keys()))
    raise SystemExit("파싱 0건 — 위 키 구조가 objects[].frames[] 와 다르다")
d = pd.DataFrame(rows).dropna(subset=GEOM)
vc = d["behavior"].value_counts()
d["behavior"] = d["behavior"].where(d["behavior"].isin(vc[vc >= MIN_COUNT].index),
                                    "other")
d = d.sort_values(["individual_id", "frame_idx"]).reset_index(drop=True)
print(d.shape, "· 개체", d.individual_id.nunique(), "· 클래스", d.behavior.nunique())
print(d.behavior.value_counts().to_dict())

# ── 시퀀스 창 ────────────────────────────────────────────────────────────
# **끊긴 구간을 이어 붙이지 않는다.** 간격이 MAX_GAP 을 넘으면 다른 장면이라
# 가장자리로 복제 패딩한다. 안 그러면 150프레임 떨어진 장면이 한 창에 들어온다.
dd = d.copy()
for c in ("centroid_x", "centroid_y"):        # 개체 기준 중심화 → 우리 안
    dd[c] = dd[c] - dd.groupby("individual_id")[c].transform("median")  # 절대
F = dd[GEOM].to_numpy(np.float32)             # 위치를 외우지 못하게
idx, gid = dd["frame_idx"].to_numpy(), dd["individual_id"].to_numpy()
half = WIN // 2
X = np.zeros((len(dd), len(GEOM), WIN), np.float32)
s = 0
for i in range(1, len(dd) + 1):
    if i == len(dd) or gid[i] != gid[s]:
        seg = np.arange(s, i)
        brk = [0] + list(np.where(np.diff(idx[seg]) > MAX_GAP)[0] + 1) + [len(seg)]
        for a, b in zip(brk[:-1], brk[1:]):
            sub = seg[a:b]
            for k, r in enumerate(sub):
                take = np.clip(np.arange(k - half, k + half + 1), 0, len(sub) - 1)
                X[r] = F[sub[take]].T
        s = i
print("시퀀스", X.shape)

# ── 모델 + GroupKFold(5) ────────────────────────────────────────────────
import torch.nn as nn
from sklearn.model_selection import GroupKFold

def make_net(n_ch, n_cls):
    def blk(i, o, k=5):
        return nn.Sequential(nn.Conv1d(i, o, k, padding=k//2),
                             nn.BatchNorm1d(o), nn.ReLU(inplace=True))
    return nn.Sequential(blk(n_ch, 64), blk(64, 96), nn.MaxPool1d(2),
                         blk(96, 128), nn.AdaptiveAvgPool1d(1), nn.Flatten(),
                         nn.Dropout(0.25), nn.Linear(128, n_cls))

def train_fold(Xtr, ytr, Xte, n_cls, epochs=40, bs=256, lr=4e-3, seed=0):
    torch.manual_seed(seed)
    # 표준화는 **학습 폴드 통계로만**. 검증 폴드 통계를 쓰면 누수다.
    mu, sd = Xtr.mean((0, 2), keepdims=True), Xtr.std((0, 2), keepdims=True) + 1e-6
    xt = torch.from_numpy((Xtr - mu) / sd).to(DEV)
    xe = torch.from_numpy((Xte - mu) / sd).to(DEV)
    yt = torch.from_numpy(ytr).long().to(DEV)
    net = make_net(Xtr.shape[1], n_cls).to(DEV)
    cnt = np.bincount(ytr, minlength=n_cls).astype(np.float32)
    w = torch.tensor((cnt.sum()/np.maximum(cnt,1))**0.5, dtype=torch.float32, device=DEV)
    lossf = nn.CrossEntropyLoss(weight=w / w.mean())
    opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
    steps = epochs * (len(xt) // bs + 1)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=lr, total_steps=steps)
    for _ in range(epochs):
        net.train(); perm = torch.randperm(len(xt), device=DEV)
        for i in range(0, len(perm), bs):
            b = perm[i:i+bs]
            opt.zero_grad(set_to_none=True)
            lossf(net(xt[b]), yt[b]).backward(); opt.step(); sched.step()
    net.eval()
    with torch.no_grad():
        return net(xe).argmax(1).cpu().numpy()

classes = sorted(d["behavior"].unique())
c2i = {c: i for i, c in enumerate(classes)}
y = d["behavior"].map(c2i).to_numpy()
g = d["individual_id"].to_numpy()

rows, brows = [], []
t0 = time.time()
for tr, te in GroupKFold(n_splits=5).split(X, y, g):
    p = train_fold(X[tr], y[tr], X[te], len(classes))
    rows.append(score(y[te], p))
    maj = np.bincount(y[tr], minlength=len(classes)).argmax()
    brows.append(score(y[te], np.full(len(te), maj)))
    print(f"  폴드 acc {rows[-1]['acc']:.3f} · MF1 {rows[-1]['mf1']:.3f}")

m, b = weighted(rows), weighted(brows)
report(f"시퀀스 1D-CNN ({WIN}프레임 창)", m, b)
print(f"\n  기존 프레임 단위 모델   acc 0.516 · MF1 0.386")
print(f"  시퀀스 모델            acc {m['acc']:.3f} · MF1 {m['mf1']:.3f}"
      f"   ({m['acc']-0.516:+.3f} / {m['mf1']-0.386:+.3f})")
print("  ※ 기존 모델은 외형 피처도 썼다. 여기는 기하 5개만 — 동일 조건 비교가 아니다.")
print(f"  {time.time()-t0:.0f}s")
json.dump({"seq_cnn": m, "baseline": b, "classes": classes, "window": WIN},
          open("/kaggle/working/behavior_seq.json", "w"),
          ensure_ascii=False, indent=1)

