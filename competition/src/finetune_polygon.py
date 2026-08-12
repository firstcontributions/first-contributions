"""622 폴리곤 → YOLO-seg 파인튜닝. **시작 전에 소요시간부터 알려준다.**

지침은 Detectron2 + GPU 를 전제하지만 이 환경은 CPU 4코어다. 같은 폴리곤을
YOLO-seg 로 내보내 학습한다. 문제는 CPU 로는 몇 시간이 아니라 며칠이 걸릴 수
있다는 것이고, 그걸 **돌려 보고 알면 늦다**. 그래서 이 스크립트는 학습 전에
실측 처리속도로 예상시간을 내고, 예산을 넘으면 멈춰 세운다.

## 라벨만 받으면 학습을 못 한다

AI Hub 622 의 라벨(TL01 77MB)에는 폴리곤 좌표만 있고 **이미지가 없다**.
원천은 TS01~05 가 80~89GB 씩인데 TS06 만 10GB 다. 현실적인 조합:

    라벨   TL01.zip  77MB  filekey 533708   ← 전체 라벨
    이미지 TS06.zip  10GB  filekey 533695   ← 가장 작은 원천 하나
    검증   VL01.zip   8MB  filekey 533718

라벨은 전부 받아 두고 **이미지가 있는 것만 골라 쓴다**. pair() 가 매칭률을
보고하므로, TS06 이 라벨의 몇 %를 덮는지 보고 다음 zip 을 받을지 정하면 된다.

## CPU 실측 (batch 8 · cache=ram · 4코어 · 2 epoch 평균)

    yolo11n-seg 320 freeze   153 ms/장/ep
    yolo11n-seg 416 freeze   197          ← 기본값
    yolo11n-seg 416 전체학습  346
    yolo11n-seg 640 freeze   544
    yolo11n-seg 640 전체학습  650

**backbone freeze 가 416 에서 1.76배 빠르다**(346→197). 데이터가 수천 장
규모일 때는 속도만이 아니라 과적합 방지에도 낫다. 640 에서 이득이 1.2배로
주는 것은 해상도가 커질수록 neck/head 연산 비중이 커지기 때문이다.

이 기본값(416·freeze)에서 5,000장 × 50epoch 이 13.7시간 — 하룻밤에 들어온다.
전체학습·640 으로 올리면 같은 양이 사흘이 되므로 GPU 로 옮기는 편이 맞다.

    # 1) 데이터 점검 — 매칭률·소요시간만 보고 끝
    python competition/src/finetune_polygon.py prep <라벨디렉터리> <이미지디렉터리>

    # 2) 학습 (예상시간 확인 후)
    python competition/src/finetune_polygon.py train <라벨디렉터리> <이미지디렉터리> \
        --max-images 5000 --imgsz 416 --epochs 50
"""
from __future__ import annotations

import argparse
import glob
import os
import random
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import parse_pig_polygon as ppp  # noqa: E402

IMG_EXT = (".jpg", ".jpeg", ".png", ".bmp")
# 실측 ms/장/epoch — CPU 4코어 · batch 8 · cache=ram.
# **2 epoch 평균**을 쓴다. 1 epoch 만 재면 초기화·워밍업이 통째로 섞여 40~50%
# 과대추정된다(같은 조건에서 439 vs 346 이 나왔다).
#   키: (모델, imgsz, freeze 여부)
SPEED_MS = {
    ("yolo11n-seg", 320, True): 153,
    ("yolo11n-seg", 416, True): 197,
    ("yolo11n-seg", 416, False): 346,
    ("yolo11n-seg", 640, True): 544,
    ("yolo11n-seg", 640, False): 650,
    ("yolo11s-seg", 640, False): 2167,
}
# backbone 을 얼리면 416 에서 1.76배 빨라진다(346→197). 640 에서는 1.2배에
# 그치는데, 해상도가 커질수록 neck/head 연산이 비중을 차지하기 때문이다.
FREEZE_LAYERS = 10
DEFAULT_BUDGET_H = 14.0     # 하룻밤. 넘으면 멈춰 세운다.


def find_xml(label_dir: str) -> list:
    return sorted(glob.glob(os.path.join(label_dir, "**", "*.xml"),
                            recursive=True))


def index_images(image_dir: str) -> dict:
    """basename(확장자 제외) → 실제 경로. 라벨과 이름으로 맞춘다."""
    out = {}
    for p in glob.glob(os.path.join(image_dir, "**", "*"), recursive=True):
        if p.lower().endswith(IMG_EXT):
            out.setdefault(os.path.splitext(os.path.basename(p))[0], p)
    return out


def load_labels(label_dir: str, verbose: bool = True):
    """CVAT XML 을 전부 읽어 하나의 DataFrame 으로."""
    import pandas as pd
    xmls = find_xml(label_dir)
    if not xmls:
        raise SystemExit(f"{label_dir} 에 XML 이 없다. zip 을 풀었는지 확인할 것.")
    frames = []
    for x in xmls:
        try:
            frames.append(ppp.parse_cvat(x))
        except Exception as e:                                    # noqa: BLE001
            if verbose:
                print(f"  ! {os.path.basename(x)} 파싱 실패: {e}")
    if not frames:
        raise SystemExit("파싱된 XML 이 하나도 없다.")
    df = pd.concat(frames, ignore_index=True)
    if verbose:
        print(f"  XML {len(xmls)}개 → 폴리곤 {len(df):,}개 · "
              f"이미지 {df['image'].nunique():,}장")
    return df


def pair(df, images: dict, verbose: bool = True):
    """라벨과 실제 이미지를 이름으로 맞춘다.

    **매칭률이 이 작업의 핵심 지표다.** 라벨은 전체(TL01)인데 이미지는 일부
    (TS06)만 받았으므로 대부분이 안 맞는 것이 정상이다. 몇 %가 맞는지 알아야
    다음 zip 을 받을지 판단할 수 있다.
    """
    stems = df["image"].map(lambda s: os.path.splitext(os.path.basename(s))[0])
    have = stems.map(lambda s: s in images)
    n_all, n_hit = stems.nunique(), stems[have].nunique()
    if verbose:
        rate = n_hit / max(1, n_all)
        print(f"  라벨 이미지 {n_all:,}장 중 실제 파일 있는 것 "
              f"{n_hit:,}장 ({rate:.1%})")
        if n_hit == 0:
            print("  ! 하나도 안 맞는다 — 라벨과 원천이 다른 세트이거나 "
                  "파일명 규칙이 다르다. 아래 예시를 대조할 것:")
            print(f"      라벨 쪽: {list(stems[:3])}")
            print(f"      이미지 쪽: {list(images)[:3]}")
    out = df[have].copy()
    out["path"] = stems[have].map(images)
    return out


def estimate_hours(n_images: int, epochs: int, model: str, imgsz: int,
                   freeze: bool = True) -> float:
    ms = SPEED_MS.get((model, imgsz, freeze))
    if ms is None:
        # 실측에 없는 조합은 픽셀 수 비례로 외삽한다. 완전 비례는 아니지만
        # (고정비가 있어 작은 해상도에서 과소추정) 자릿수 판단에는 충분하다.
        cands = [(sz, v) for (m, sz, fr), v in SPEED_MS.items()
                 if m == model and fr == freeze]
        if not cands:
            cands = [(sz, v) for (m, sz, _f), v in SPEED_MS.items() if m == model]
        if not cands:
            cands = [(640, 650)]
        sz, base = min(cands, key=lambda x: abs(x[0] - imgsz))
        ms = base * (imgsz / sz) ** 2
    return n_images * epochs * ms / 1000.0 / 3600.0


def subsample(df, max_images: int, seed: int = 0):
    """이미지 단위로 줄인다 — 폴리곤 단위로 자르면 한 장이 반만 라벨된다."""
    imgs = sorted(df["image"].unique())
    if len(imgs) <= max_images:
        return df
    rng = random.Random(seed)
    keep = set(rng.sample(imgs, max_images))
    return df[df["image"].isin(keep)].copy()


def build_dataset(df, out_dir: str, ratios=None, seed: int = 0,
                  link: bool = True) -> dict:
    """YOLO-seg 디렉터리 구조로 내보낸다. 분할은 **이미지 단위**."""
    ratios = ratios or ppp.SPLIT
    parts = ppp.split_images(df, ratios=ratios, seed=seed)
    shutil.rmtree(out_dir, ignore_errors=True)
    cats = sorted(df["label"].dropna().unique().tolist()) or ["pig"]
    counts = {}
    for split, sdf in parts.items():
        idir = os.path.join(out_dir, "images", split)
        ldir = os.path.join(out_dir, "labels", split)
        os.makedirs(idir, exist_ok=True)
        for src in sorted(sdf["path"].unique()):
            dst = os.path.join(idir, os.path.basename(src))
            if os.path.exists(dst):
                continue
            if link:
                try:
                    os.symlink(os.path.abspath(src), dst)
                    continue
                except OSError:
                    pass
            shutil.copy2(src, dst)
        ppp.to_yolo_seg(sdf, ldir, categories=cats)
        counts[split] = sdf["image"].nunique()
    names = "\n".join(f"  {i}: {c}" for i, c in enumerate(cats))
    yml = os.path.join(out_dir, "data.yaml")
    with open(yml, "w", encoding="utf-8") as f:
        f.write(f"path: {os.path.abspath(out_dir)}\ntrain: images/train\n"
                f"val: images/val\nnames:\n{names}\n")
    return {"yaml": yml, "counts": counts, "categories": cats}


def prep(label_dir: str, image_dir: str, max_images: int, epochs: int,
         model: str, imgsz: int, out_dir: str | None = None,
         build: bool = False, freeze: bool = True) -> dict:
    print(f"\n{'=' * 72}\n  622 폴리곤 파인튜닝 준비\n{'=' * 72}")
    print("1) 라벨 읽기")
    df = load_labels(label_dir)
    print("2) 이미지 매칭")
    images = index_images(image_dir)
    print(f"  이미지 파일 {len(images):,}개 발견")
    df = pair(df, images)
    n = df["image"].nunique() if len(df) else 0
    if n == 0:
        raise SystemExit("\n학습할 이미지가 없다. 원천 zip(TS06 = filekey 533695)을 "
                         "받아 같은 위치에 풀 것.")

    print("3) 라벨 품질")
    try:
        a = ppp.audit(df)
        for k, v in list(a.items())[:8]:
            print(f"  {k}: {v}")
    except Exception as e:                                        # noqa: BLE001
        print(f"  (audit 생략: {e})")

    use = min(n, max_images)
    hours = estimate_hours(use, epochs, model, imgsz, freeze)
    print(f"\n4) 소요시간 추정 — {model} · imgsz {imgsz} · CPU"
          + (" · freeze" if freeze else " · 전체학습"))
    print(f"  학습 대상 {use:,}장 × {epochs} epoch")
    print(f"  예상 **{hours:.1f}시간** ({hours / 24:.1f}일)")
    if hours > DEFAULT_BUDGET_H:
        print(f"  ⚠️  하룻밤({DEFAULT_BUDGET_H:.0f}h)을 넘는다. 아래 중 하나를 택할 것:")
        if not freeze:
            print(f"      · backbone freeze  →  "
                  f"{estimate_hours(use, epochs, model, imgsz, True):.1f}h")
        for tgt in (416, 320):
            if tgt < imgsz:
                h2 = estimate_hours(use, epochs, model, tgt, freeze)
                print(f"      · imgsz {imgsz}→{tgt}  →  {h2:.1f}h")
        per = SPEED_MS.get((model, imgsz, freeze)) or 650
        fit = int(DEFAULT_BUDGET_H * 3600 * 1000 / (epochs * per))
        print(f"      · --max-images {fit:,} 로 줄이기  →  {DEFAULT_BUDGET_H:.0f}h")
        print(f"      · GPU 로 옮기기 (같은 data.yaml 그대로, device=0)")

    info = {"n_matched": n, "n_use": use, "hours": hours, "df": df}
    if build:
        out_dir = out_dir or "/tmp/pigseg"
        print(f"\n5) 데이터셋 생성 → {out_dir}")
        sub = subsample(df, max_images)
        built = build_dataset(sub, out_dir)
        print(f"  {built['counts']} · 클래스 {built['categories']}")
        info.update(built)
    return info


def train(label_dir: str, image_dir: str, max_images: int, epochs: int,
          model: str, imgsz: int, out_dir: str, batch: int, force: bool,
          freeze: bool = True, cache: bool = True) -> int:
    info = prep(label_dir, image_dir, max_images, epochs, model, imgsz,
                out_dir, build=True, freeze=freeze)
    if info["hours"] > DEFAULT_BUDGET_H and not force:
        print(f"\n중단 — 예상 {info['hours']:.1f}h 가 예산 {DEFAULT_BUDGET_H:.0f}h 초과. "
              f"그래도 돌리려면 --force.")
        return 2
    from ultralytics import YOLO
    print(f"\n6) 학습 시작 — {model} · imgsz {imgsz} · batch {batch} · CPU"
          + (f" · freeze {FREEZE_LAYERS}" if freeze else " · 전체학습")
          + (" · cache" if cache else ""))
    t0 = time.time()
    m = YOLO(model if model.endswith(".pt") else model + ".pt")
    kw = dict(data=info["yaml"], epochs=epochs, imgsz=imgsz, batch=batch,
              workers=2, device="cpu", project=os.path.join(out_dir, "runs"),
              name="seg", exist_ok=True, patience=10, plots=True)
    if freeze:
        kw["freeze"] = FREEZE_LAYERS
    if cache:
        kw["cache"] = "ram"
    m.train(**kw)
    dt = time.time() - t0
    print(f"\n완료 — {dt / 3600:.2f}시간 (추정 {info['hours']:.1f}h)")
    print(f"가중치: {out_dir}/runs/seg/weights/best.pt")
    print("공식 기준선은 Detectron2 AP50 60 이다. YOLO-seg 의 mAP50(mask)와는")
    print("측정 방식이 달라 직접 비교하면 안 된다 — 같은 지표로 재려면")
    print("동일 test 분할에서 Pascal-VOC AP50 을 따로 계산할 것.")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="finetune_polygon")
    ap.add_argument("mode", choices=["prep", "train"])
    ap.add_argument("label_dir", help="TL01/VL01 을 푼 디렉터리 (XML 포함)")
    ap.add_argument("image_dir", help="TS06 등 원천 이미지를 푼 디렉터리")
    ap.add_argument("--max-images", type=int, default=5000)
    ap.add_argument("--epochs", type=int, default=40)
    ap.add_argument("--model", default="yolo11n-seg")
    ap.add_argument("--imgsz", type=int, default=416)
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--no-freeze", action="store_true",
                    help="backbone 까지 전부 학습(느리고 소량 데이터에선 과적합)")
    ap.add_argument("--no-cache", action="store_true",
                    help="이미지를 RAM 에 안 올림(메모리 부족할 때)")
    ap.add_argument("--out", default="/tmp/pigseg")
    ap.add_argument("--force", action="store_true",
                    help="예상시간이 예산을 넘어도 강행")
    a = ap.parse_args(argv)
    if a.mode == "prep":
        prep(a.label_dir, a.image_dir, a.max_images, a.epochs, a.model,
             a.imgsz, a.out, build=False, freeze=not a.no_freeze)
        return 0
    return train(a.label_dir, a.image_dir, a.max_images, a.epochs, a.model,
                 a.imgsz, a.out, a.batch, a.force,
                 freeze=not a.no_freeze, cache=not a.no_cache)


if __name__ == "__main__":
    raise SystemExit(main())
