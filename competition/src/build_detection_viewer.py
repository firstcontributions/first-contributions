"""돼지 탐지 뷰어 프론트 — 파일명/축사(pen)/소스로 검색 → 탐지 즉시 표시.

Kaggle rbbbjp/pig-detection-yolo-dataset-mixed-sources (YOLO, 0=pig).
파일명에 축사(pen1/pen2)·카메라(cam1/2)가 인코딩됨. 여러 소스(bama2d·compag·
faroseg·hogs·multiview·pigdata·rgb) 이미지를 샘플로 임베드하고, 검색창에
파일명이나 축사번호를 넣으면 즉시 해당 이미지+탐지 bbox 를 보여준다.

    python competition/src/build_detection_viewer.py [데이터셋경로]
"""
from __future__ import annotations

import base64
import io
import os
import re
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
TEMPLATE = os.path.join(ROOT, "competition", "dashboard", "detection_viewer_template.html")
OUT = os.path.join(ROOT, "competition", "dashboard", "detection_viewer.html")
DEFAULT = ("/root/.cache/kagglehub/datasets/rbbbjp/"
           "pig-detection-yolo-dataset-mixed-sources/versions/1")
SOURCES = ["bama2d", "compag2020", "compag2021", "faroseg", "hogs",
           "multiview", "pigdata", "rgb"]
PER_PEN = 10        # 축사별 샘플
PER_SOURCE = 6      # 소스별 샘플
VIEW_W = 560


def read_boxes(label_path):
    boxes = []
    if not os.path.exists(label_path):
        return boxes
    for ln in open(label_path):
        p = ln.split()
        if len(p) >= 5:
            _, xc, yc, w, h = p[:5]
            boxes.append((float(xc), float(yc), float(w), float(h)))
    return boxes


def facets(name):
    pen = (re.search(r'pen\d+', name) or [None])
    pen = re.search(r'(pen\d+)', name)
    cam = re.search(r'(cam\d+|c\d+)', name)
    return (pen.group(1) if pen else "-", cam.group(1) if cam else "-")


def collect(root):
    """이미지 인덱스(소스·축사·카메라·탐지수). 샘플 선별."""
    items = []
    stats = {"total_img": 0, "total_box": 0, "by_source": {}, "pens": {}}
    for src in SOURCES:
        for split in ("train", "test"):
            imgdir = os.path.join(root, src, split, "images")
            lbldir = os.path.join(root, src, split, "labels")
            if not os.path.isdir(imgdir):
                continue
            for fn in os.listdir(imgdir):
                if not fn.lower().endswith((".jpg", ".png", ".jpeg")):
                    continue
                pen, cam = facets(fn)
                lbl = os.path.join(lbldir, os.path.splitext(fn)[0] + ".txt")
                nb = len(read_boxes(lbl))
                stats["total_img"] += 1; stats["total_box"] += nb
                stats["by_source"][src] = stats["by_source"].get(src, 0) + 1
                if pen != "-":
                    stats["pens"][pen] = stats["pens"].get(pen, 0) + 1
                items.append({"src": src, "split": split, "file": fn,
                              "pen": pen, "cam": cam, "path": os.path.join(imgdir, fn),
                              "label": lbl, "count": nb})
    return items, stats


def sample(items):
    """축사 우선 + 소스별 다양성으로 샘플 선별."""
    picked, seen = [], set()
    def add(it):
        if it["file"] not in seen and it["count"] > 0:
            picked.append(it); seen.add(it["file"])
    # 축사(pen)별
    for pen in sorted({i["pen"] for i in items if i["pen"] != "-"}):
        cnt = 0
        for it in items:
            if it["pen"] == pen:
                add(it); cnt += 1
                if cnt >= PER_PEN:
                    break
    # 소스별
    for src in SOURCES:
        cnt = 0
        for it in items:
            if it["src"] == src and it["file"] not in seen:
                add(it); cnt += 1
                if cnt >= PER_SOURCE:
                    break
    return picked


def embed(it):
    try:
        im = Image.open(it["path"]).convert("RGB")
    except Exception:  # noqa: BLE001
        return None
    W0, H0 = im.size; sc = VIEW_W / W0
    disp = im.resize((VIEW_W, max(1, int(H0 * sc))))
    buf = io.BytesIO(); disp.save(buf, "JPEG", quality=72)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    w, h = disp.size
    boxes = []
    for xc, yc, bw, bh in read_boxes(it["label"]):
        boxes.append({"x": round((xc - bw / 2) * w, 1), "y": round((yc - bh / 2) * h, 1),
                      "w": round(bw * w, 1), "h": round(bh * h, 1)})
    return {"file": it["file"], "src": it["src"], "pen": it["pen"],
            "cam": it["cam"], "count": len(boxes), "w": w, "h": h,
            "img": uri, "boxes": boxes}


def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    items, stats = collect(root)
    picked = sample(items)
    gallery = [g for it in picked if (g := embed(it))]
    data = {
        "meta": {"total_img": stats["total_img"], "total_box": stats["total_box"],
                 "n_sample": len(gallery), "sources": SOURCES,
                 "by_source": stats["by_source"], "pens": stats["pens"]},
        "gallery": gallery,
    }
    import json
    html = open(TEMPLATE, encoding="utf-8").read().replace(
        "/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"탐지 뷰어 생성: {OUT} ({os.path.getsize(OUT)/1e6:.1f}MB)")
    print(f"  전체 {stats['total_img']}장/{stats['total_box']}탐지 · 샘플 {len(gallery)}장 · "
          f"축사 {list(stats['pens'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
