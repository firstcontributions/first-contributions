"""자세 인식 프론트 생성 — 사진 갤러리 + 주석 영상.

대회 실이미지에 bbox+자세(정답/예측)를 얹은 프론트엔드(HTML)를 만든다.
  - 사진 갤러리: 이미지 위 SVG bbox 오버레이(정답 색 + 예측 오답 표시)
  - 영상: 한 카메라의 연속 프레임에 bbox를 그려 mp4 로 인코딩(주석 영상)

이미지/영상은 축소·압축해 data URI 로 임베드(자체완결 HTML).

    python competition/src/build_posture_gallery.py [대회경로]
"""
from __future__ import annotations

import ast
import base64
import io
import json
import os
import re
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from sklearn.ensemble import RandomForestClassifier

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
TEMPLATE = os.path.join(ROOT, "competition", "dashboard", "posture_gallery_template.html")
OUT_HTML = os.path.join(ROOT, "competition", "dashboard", "posture_gallery.html")
import glob as _glob
_ff = _glob.glob("/opt/pw-browsers/ffmpeg*/ffmpeg-linux")
FFMPEG = _ff[0] if _ff else "ffmpeg"

COMMON = {"Standing": "standing", "Sitting": "sitting",
          "Lateral_lying_left": "lying", "Lateral_lying_right": "lying",
          "Sternal_lying": "lying"}
COLOR = {"standing": "#2a78d6", "sitting": "#eda100", "lying": "#1baf7a"}
GALLERY_N = 18
VIDEO_FRAMES = 24
VIEW_W = 760          # 갤러리 이미지 폭
VID_W = 640           # 영상 폭


def load(path):
    if not path:
        import kagglehub
        base = kagglehub.competition_download("multi-view-pig-posture-recognition")
        path = os.path.join(base, "multiview_pig_posture_recognition")
    classes = open(os.path.join(path, "pig_posture_classes.txt")).read().split()
    d = pd.read_csv(os.path.join(path, "train1.csv"))
    bb = d["bbox"].apply(ast.literal_eval)
    d["bx"] = bb.apply(lambda b: b[0]); d["by"] = bb.apply(lambda b: b[1])
    d["bw"] = bb.apply(lambda b: b[2]); d["bh"] = bb.apply(lambda b: b[3])
    d["cls"] = d["class_id"].apply(lambda i: classes[i])
    d["common"] = d["cls"].map(COMMON)
    d["view"] = d["image_id"].str.extract(r'(pen\d+_[a-z]+_cam\d+)')[0]
    d["aspect"] = d["bw"] / d["bh"]
    return path, d


def train_model(d):
    g = d.groupby("view")
    d = d.copy()
    d["aspect_z"] = g["aspect"].transform(lambda s: (s - s.mean()) / (s.std() or 1))
    d["area_pct"] = g.apply(lambda s: (s["bw"] * s["bh"]).rank(pct=True)).reset_index(level=0, drop=True)
    X = d[["aspect_z", "area_pct"]].to_numpy()
    clf = RandomForestClassifier(n_estimators=200, min_samples_leaf=3,
                                 class_weight="balanced", random_state=42, n_jobs=-1)
    clf.fit(X, d["cls"])
    d["pred"] = clf.predict(X)
    d["pred_common"] = d["pred"].map(COMMON)
    return d


def _img_data_uri(im, quality=72):
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=quality)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def build_gallery(path, d):
    imgdir = os.path.join(path, "train1_images")
    # 뷰·자세 다양하게 샘플 이미지 선택
    sample_imgs = (d.groupby("view")["image_id"].apply(lambda s: s.drop_duplicates().head(5))
                   .reset_index(drop=True).drop_duplicates().tolist())
    items = []
    for img_id in sample_imgs:
        fp = os.path.join(imgdir, img_id)
        if not os.path.exists(fp):
            continue
        im = Image.open(fp).convert("RGB")
        W0, H0 = im.size
        scale = VIEW_W / W0
        im2 = im.resize((VIEW_W, int(H0 * scale)))
        rows = d[d["image_id"] == img_id]
        boxes = [{"x": round(r.bx * scale, 1), "y": round(r.by * scale, 1),
                  "w": round(r.bw * scale, 1), "h": round(r.bh * scale, 1),
                  "cls": r.cls, "common": r.common, "pred": r.pred,
                  "ok": bool(r.pred == r.cls)} for r in rows.itertuples()]
        items.append({"image_id": img_id, "view": rows["view"].iloc[0],
                      "w": VIEW_W, "h": int(H0 * scale),
                      "img": _img_data_uri(im2), "boxes": boxes})
        if len(items) >= GALLERY_N:
            break
    return items


def build_video(path, d):
    """한 카메라 연속 프레임에 bbox를 그려 mp4(base64) 생성."""
    imgdir = os.path.join(path, "train1_images")
    view = d["view"].value_counts().idxmax()
    seq = (d[d["view"] == view]["image_id"].drop_duplicates().sort_values()
           .head(VIDEO_FRAMES).tolist())
    rgb = {"standing": (42, 120, 214), "sitting": (237, 161, 0),
           "lying": (27, 175, 122)}
    frames_jpeg = []
    for img_id in seq:
        fp = os.path.join(imgdir, img_id)
        if not os.path.exists(fp):
            continue
        im = Image.open(fp).convert("RGB")
        W0, H0 = im.size; scale = VID_W / W0
        h_even = (int(H0 * scale) // 2) * 2
        im = im.resize((VID_W, h_even))
        dr = ImageDraw.Draw(im)
        for r in d[d["image_id"] == img_id].itertuples():
            x, y = r.bx * scale, r.by * scale
            w, h = r.bw * scale, r.bh * scale
            c = rgb.get(r.common, (255, 255, 255))
            dr.rectangle([x, y, x + w, y + h], outline=c, width=3)
            dr.text((x + 2, y + 2), r.common, fill=c)
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=80)
        frames_jpeg.append(buf.getvalue())
    n = len(frames_jpeg)
    if n == 0:
        return None, view, 0
    # 이 ffmpeg 빌드는 VP8/webm + image2pipe 만 지원 → JPEG 파이프로 webm 인코딩
    tmp = tempfile.mkdtemp(); webm = os.path.join(tmp, "out.webm")
    proc = subprocess.Popen(
        [FFMPEG, "-y", "-framerate", "3", "-f", "image2pipe", "-vcodec", "mjpeg",
         "-i", "pipe:0", "-c:v", "libvpx", "-b:v", "700k", "-pix_fmt", "yuv420p", webm],
        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    proc.communicate(b"".join(frames_jpeg))
    if not os.path.exists(webm) or os.path.getsize(webm) == 0:
        return None, view, n
    data = "data:video/webm;base64," + base64.b64encode(open(webm, "rb").read()).decode()
    return data, view, n


def main() -> int:
    path, d = load(sys.argv[1] if len(sys.argv) > 1 else None)
    d = train_model(d)
    acc = float((d["pred"] == d["cls"]).mean())
    gallery = build_gallery(path, d)
    video, vview, vframes = build_video(path, d)
    data = {
        "meta": {"n_images": d["image_id"].nunique(), "n_boxes": len(d),
                 "train_acc": round(acc, 3),
                 "classes": list(COLOR), "video_view": vview,
                 "video_frames": vframes},
        "gallery": gallery, "video": video,
    }
    tpl = open(TEMPLATE, encoding="utf-8").read()
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
    open(OUT_HTML, "w", encoding="utf-8").write(html)
    size = os.path.getsize(OUT_HTML) / 1e6
    print(f"프론트 생성: {OUT_HTML} ({size:.1f}MB)")
    print(f"  갤러리 {len(gallery)}장 · 영상 {vframes}프레임({vview}) · "
          f"학습정확도(참고) {acc:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
