"""Pig_Polygon(분만행위 폴리곤) 데이터셋 수집 경로.

제공된 학습 지침의 데이터셋은 지금까지 쓰던 71471 [Bbox] **발정** 데이터와
축이 다르다 — **분만행위** 개체를 폴리곤(인스턴스 분할)으로 라벨한 것이고,
Detectron2 기반으로 학습해 **Pascal-VOC AP50 = 60** 을 낸다고 보고돼 있다.

이 프로젝트에 왜 중요한가: 배치(올인/올아웃) 운영에서 **분만 감독이 최대
노동 피크**다. 배치 간격이 넓을수록 분만이 한 날에 몰리고(5주 배치는 주 평균의
5배), 현장 권장은 분만 시 모돈 300두당 최소 1인이다. 야간 분만을 카메라가
잡아주면 그 피크가 곧바로 완화된다. 즉 분만행위 인식은 batch_flow 의
노동 피크 문제와 직접 맞물린다.

**환경 제약을 먼저 밝힌다.** 지침은 Pig_Polygon.tar 도커 이미지 + GPU
(`--gpus all`) + Detectron2 를 전제한다. 이 세션은 CPU 4코어이고 해당 tar
파일도 없으므로 **그 학습을 재현하지 않았다.** 대신 이 모듈은

  1) 데이터가 도착하면 바로 먹일 수 있도록 **CVAT XML 파서**를 제공하고,
  2) 지침 파이프라인(data_parsing → split)에 대응하는 변환·분할을 하며,
  3) GPU 없이 갈 수 있는 대안 경로(YOLO-seg)로 내보낸다.

지침의 AP50 60 은 **비교 기준선**으로 기록해 둔다. 우리 경로가 그보다 낮으면
낮다고 적을 것이지, 다른 지표로 바꿔 유리하게 보이게 하지 않는다.

    python competition/src/parse_pig_polygon.py            # 자체 점검(합성)
    python competition/src/parse_pig_polygon.py <디렉터리>   # 실데이터 파싱
"""
from __future__ import annotations

import os
import sys
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

# 지침이 보고한 기준선 — 우리 결과를 여기에 대조한다
BASELINE = {"metric": "AP50 (Pascal-VOC)", "value": 60.0,
            "model": "Detectron2 폴리곤(인스턴스 분할)",
            "source": "제공된 학습 지침 그림 4"}

# 지침 파이프라인의 분할 비율(split.py 대응). 지침에 비율이 명시돼 있지 않아
# 통상값을 쓴다 — 실제 값이 확인되면 맞춰야 한다.
SPLIT = {"train": 0.7, "val": 0.15, "test": 0.15}


def parse_cvat(xml_path: str) -> pd.DataFrame:
    """CVAT `annotations.xml` → 폴리곤 테이블.

    지침의 1.rawdata 는 `images/` + `annotations.xml` 구조이고, 이는 CVAT
    for images 포맷이다. 폴리곤은 points="x1,y1;x2,y2;..." 로 들어온다.
    box 태그가 섞여 있는 경우도 있어 함께 받아 사각형 폴리곤으로 바꾼다.
    """
    root = ET.parse(xml_path).getroot()
    rows = []
    for im in root.iter("image"):
        name = im.get("name")
        W = float(im.get("width") or 0)
        H = float(im.get("height") or 0)
        for el in list(im):
            if el.tag == "polygon":
                pts = [tuple(map(float, p.split(",")))
                       for p in (el.get("points") or "").split(";") if p]
            elif el.tag == "box":
                x1, y1 = float(el.get("xtl")), float(el.get("ytl"))
                x2, y2 = float(el.get("xbr")), float(el.get("ybr"))
                pts = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
            else:
                continue
            if len(pts) < 3:
                continue
            attrs = {a.get("name"): (a.text or "") for a in el.iter("attribute")}
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            rows.append({
                "image": name, "img_w": W, "img_h": H,
                "label": el.get("label"), "points": pts,
                "n_points": len(pts),
                "x": min(xs), "y": min(ys),
                "w": max(xs) - min(xs), "h": max(ys) - min(ys),
                "area": polygon_area(pts),
                **{f"attr_{k}": v for k, v in attrs.items()},
            })
    return pd.DataFrame(rows)


def polygon_area(pts) -> float:
    """신발끈 공식. 폴리곤 면적이 0 이면 라벨이 깨진 것이다."""
    n = len(pts)
    if n < 3:
        return 0.0
    s = 0.0
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


def audit(df: pd.DataFrame) -> dict:
    """받은 폴리곤이 쓸 만한지 — 학습 전에 먼저 본다.

    면적 0·점 3개 미만·화면 밖 좌표는 학습을 조용히 망친다. 71471 에서
    카메라 교락을 늦게 발견한 전례가 있어, 이번엔 먹이기 전에 감사한다.
    """
    if not len(df):
        return {"n": 0}
    out_of_frame = int(((df["x"] < -1) | (df["y"] < -1)
                        | (df["x"] + df["w"] > df["img_w"] + 1)
                        | (df["y"] + df["h"] > df["img_h"] + 1)).sum())
    per_img = df.groupby("image").size()
    return {
        "n": int(len(df)), "n_images": int(df["image"].nunique()),
        "labels": df["label"].value_counts().to_dict(),
        "zero_area": int((df["area"] <= 0).sum()),
        "degenerate": int((df["n_points"] < 3).sum()),
        "out_of_frame": out_of_frame,
        "pts_median": int(df["n_points"].median()),
        "per_image_mean": round(float(per_img.mean()), 2),
        "per_image_max": int(per_img.max()),
        "label_purity": _label_purity(df),
    }


def _label_purity(df: pd.DataFrame) -> dict:
    """이미지 단위로 라벨이 한 종류뿐인지 — 71471 교락과 같은 함정 점검.

    한 이미지 안에 분만/비분만이 섞여 있어야 모델이 **개체 차이**를 배운다.
    모든 이미지가 한 라벨로만 채워져 있으면 이미지(=카메라·시점)를 외우게 된다.
    """
    if df["label"].nunique() < 2:
        return {"single_label": True}
    per = df.groupby("image")["label"].nunique()
    return {"single_label": False,
            "images_mixed": int((per > 1).sum()),
            "images_pure": int((per == 1).sum()),
            "mixed_rate": round(float((per > 1).mean()), 3)}


def split_images(df: pd.DataFrame, ratios: dict | None = None,
                 seed: int = 0) -> dict:
    """이미지 단위 분할 — **폴리곤 단위로 나누면 안 된다**.

    같은 이미지의 폴리곤이 train 과 test 에 갈라지면 누수다. 71471 자세
    데이터에서 이미지 공유로 0.955 라는 허수를 본 적이 있으므로 여기서는
    처음부터 이미지를 쪼갠다.
    """
    r = dict(ratios or SPLIT)
    imgs = sorted(df["image"].unique())
    rng = np.random.default_rng(seed)
    rng.shuffle(imgs)
    n = len(imgs)
    n_tr = int(round(n * r["train"]))
    n_va = int(round(n * r["val"]))
    parts = {"train": imgs[:n_tr], "val": imgs[n_tr:n_tr + n_va],
             "test": imgs[n_tr + n_va:]}
    return {k: df[df["image"].isin(v)].copy() for k, v in parts.items()}


def to_coco(df: pd.DataFrame, categories: list | None = None) -> dict:
    """COCO 인스턴스 분할 JSON (Detectron2 기본 입력)."""
    cats = categories or sorted(df["label"].dropna().unique())
    cat_id = {c: i + 1 for i, c in enumerate(cats)}
    images, anns = [], []
    img_id = {}
    for i, (name, g) in enumerate(df.groupby("image", sort=True), start=1):
        img_id[name] = i
        images.append({"id": i, "file_name": name,
                       "width": int(g["img_w"].iloc[0]),
                       "height": int(g["img_h"].iloc[0])})
    for j, r in enumerate(df.itertuples(index=False), start=1):
        seg = [c for p in r.points for c in p]
        anns.append({"id": j, "image_id": img_id[r.image],
                     "category_id": cat_id.get(r.label, 1),
                     "segmentation": [seg], "area": float(r.area),
                     "bbox": [float(r.x), float(r.y), float(r.w), float(r.h)],
                     "iscrowd": 0})
    return {"images": images, "annotations": anns,
            "categories": [{"id": v, "name": k} for k, v in cat_id.items()]}


def to_yolo_seg(df: pd.DataFrame, out_dir: str,
                categories: list | None = None) -> int:
    """YOLOv8-seg 라벨(.txt) — GPU 없이 갈 수 있는 대안 경로.

    지침은 Detectron2 + GPU 를 전제하지만 이 환경은 CPU 4코어다. 같은
    폴리곤을 YOLO-seg 형식으로 내보내 두면 가용한 자원에서 학습을 시도할 수
    있다. 좌표는 이미지 크기로 정규화한다.
    """
    cats = categories or sorted(df["label"].dropna().unique())
    cat_id = {c: i for i, c in enumerate(cats)}
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for name, g in df.groupby("image"):
        lines = []
        for r in g.itertuples(index=False):
            W, H = r.img_w or 1, r.img_h or 1
            flat = []
            for x, y in r.points:
                flat += [f"{min(max(x / W, 0), 1):.6f}",
                         f"{min(max(y / H, 0), 1):.6f}"]
            lines.append(f"{cat_id.get(r.label, 0)} " + " ".join(flat))
        stem = os.path.splitext(os.path.basename(name))[0]
        with open(os.path.join(out_dir, stem + ".txt"), "w") as f:
            f.write("\n".join(lines) + "\n")
        n += 1
    return n


# --------------------------------------------------------------------------
def synth_cvat(path: str, n_images: int = 6, seed: int = 0) -> str:
    """자체 점검용 CVAT XML — 실데이터 없이 파서를 검증한다."""
    rng = np.random.default_rng(seed)
    root = ET.Element("annotations")
    ET.SubElement(root, "version").text = "1.1"
    for i in range(n_images):
        im = ET.SubElement(root, "image", id=str(i),
                           name=f"frame_{i:04d}.jpg",
                           width="1920", height="1080")
        for k in range(int(rng.integers(1, 4))):
            cx, cy = rng.uniform(300, 1600), rng.uniform(200, 900)
            rr = rng.uniform(60, 140)
            pts = [(cx + rr * np.cos(t), cy + rr * 0.6 * np.sin(t))
                   for t in np.linspace(0, 2 * np.pi, 9)[:-1]]
            el = ET.SubElement(
                im, "polygon",
                label=("farrowing" if (i + k) % 3 == 0 else "pig"),
                points=";".join(f"{x:.1f},{y:.1f}" for x, y in pts),
                occluded="0", z_order="0")
            a = ET.SubElement(el, "attribute", name="posture")
            a.text = "lateral"
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)
    return path


def main() -> int:
    import tempfile
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    print("=== Pig_Polygon (분만행위 폴리곤) 수집 경로 ===")
    print(f"  지침 기준선: {BASELINE['metric']} = {BASELINE['value']:.0f} "
          f"({BASELINE['model']})")
    print("  지침 환경: Pig_Polygon.tar 도커 + GPU + Detectron2")
    print("  이 세션: CPU 4코어 · tar 파일 없음 → **그 학습은 재현하지 않았다**")
    print("  이 모듈이 하는 일: CVAT 파싱 · 감사 · 이미지 단위 분할 · "
          "COCO/YOLO-seg 내보내기")

    if arg and os.path.isdir(arg):
        xmls = [os.path.join(r, f) for r, _d, fs in os.walk(arg)
                for f in fs if f.endswith(".xml")]
        if not xmls:
            print(f"\n  {arg} 에서 annotations.xml 을 찾지 못했다.")
            return 0
        print(f"\n  실데이터: XML {len(xmls)}개")
        df = pd.concat([parse_cvat(x) for x in xmls], ignore_index=True)
    else:
        if arg:
            print(f"\n  경로 {arg} 없음 — 합성 XML 로 자체 점검한다.")
        else:
            print("\n  (실데이터 경로 미지정 — 합성 XML 로 자체 점검)")
        tmp = tempfile.mkdtemp()
        df = parse_cvat(synth_cvat(os.path.join(tmp, "annotations.xml"), 8))

    a = audit(df)
    print(f"\n=== 데이터 감사 (먹이기 전에 먼저 본다) ===")
    print(f"  폴리곤 {a['n']} · 이미지 {a['n_images']} · "
          f"이미지당 평균 {a['per_image_mean']} (최대 {a['per_image_max']})")
    print(f"  라벨 {a['labels']}")
    print(f"  꼭짓점 중앙값 {a['pts_median']} · 면적 0 인 것 {a['zero_area']} · "
          f"화면 밖 {a['out_of_frame']}")
    lp = a["label_purity"]
    if lp.get("single_label"):
        print("  ⚠ 라벨이 한 종류뿐 — 개체 구분 학습이 아니라 검출만 가능하다.")
    else:
        print(f"  라벨 혼재 이미지 {lp['images_mixed']}/{a['n_images']} "
              f"({lp['mixed_rate']:.0%})")
        if lp["mixed_rate"] < 0.2:
            print("    ⚠ 대부분의 이미지가 한 라벨로만 채워져 있다 — 모델이 개체가")
            print("      아니라 이미지(카메라·시점)를 외울 위험. 71471 에서 겪은 함정이다.")

    sp = split_images(df)
    print(f"\n=== 분할 (이미지 단위 — 폴리곤 단위로 나누면 누수) ===")
    for k, v in sp.items():
        print(f"  {k:<6} 이미지 {v['image'].nunique():>4} · 폴리곤 {len(v):>5}")
    overlap = (set(sp["train"]["image"]) & set(sp["test"]["image"]))
    print(f"  train∩test 이미지 {len(overlap)}개 " +
          ("— 누수 없음" if not overlap else "⚠ 누수!"))

    coco = to_coco(sp["train"])
    print(f"\n=== 내보내기 ===")
    print(f"  COCO(Detectron2): 이미지 {len(coco['images'])} · "
          f"주석 {len(coco['annotations'])} · 카테고리 {len(coco['categories'])}")
    tmp2 = tempfile.mkdtemp()
    n = to_yolo_seg(sp["train"], tmp2)
    print(f"  YOLO-seg(대안 경로): 라벨 파일 {n}개 → {tmp2}")

    print("\n=== 이 데이터가 앱 어디에 붙는가 ===")
    print("  분만행위 인식 → 분만 감독 자동화. 배치 운영에서 **분만은 최대 노동")
    print("  피크**이고(5주 배치는 주 평균의 5배가 한 날에 몰린다), 현장 권장은")
    print("  분만 시 모돈 300두당 최소 1인이다. 야간 분만을 카메라가 잡으면")
    print("  batch_flow 가 계산한 그 피크가 실제로 완화된다.")
    print("\n※ 지침의 AP50 60 은 비교 기준선으로만 기록했다. 우리 경로 성능이")
    print("  나오면 그 값과 같은 지표(AP50)로 비교할 것이고, 낮으면 낮다고 적는다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
