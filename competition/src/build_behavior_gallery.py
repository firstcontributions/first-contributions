"""행동 확인 프론트 — Edinburgh 실영상 프레임에 행동 bbox 오버레이.

output.json(주석)과 color.mp4(영상)를 결합해, 각 프레임의 돼지별 행동을
실제 영상 위에 표시하는 자체완결 HTML 을 만든다.
  - 행동 갤러리: 영상 프레임 + SVG bbox(행동별 색) 오버레이, 행동 필터·확대
  - 주석 영상: 연속 프레임에 bbox+행동을 그려 webm 인코딩

매핑: 영상프레임 = frameNumber × (fps × stepSize)  (여기선 ×3)

    python competition/src/build_behavior_gallery.py <녹화폴더> <color.mp4>
    예) ... competition/data/edinburgh/2019_11_05/000009  /tmp/edvid/color.mp4
"""
from __future__ import annotations

import base64
import glob
import io
import json
import os
import subprocess
import sys
import tempfile

import cv2
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
TEMPLATE = os.path.join(ROOT, "competition", "dashboard", "behavior_gallery_template.html")
OUT = os.path.join(ROOT, "competition", "dashboard", "behavior_gallery.html")
_ff = glob.glob("/opt/pw-browsers/ffmpeg*/ffmpeg-linux")
FFMPEG = _ff[0] if _ff else "ffmpeg"

# 행동 → 카테고리 → 색 (RGB). 활동=발정 신호 강조.
CATS = {
    "활동": (["walk", "run", "investigating", "chase", "playwithtoy",
            "nose-poke-elsewhere"], (42, 120, 214)),      # blue
    "휴식": (["standing", "sitting", "lying", "sleep"], (27, 175, 122)),  # green
    "섭식": (["eat", "drink"], (237, 161, 0)),             # orange
    "사회/번식": (["nose-to-nose", "jumpontopof", "fight"], (232, 123, 164)),  # magenta
}
BEH_COLOR = {b: c for _, (bs, c) in CATS.items() for b in bs}
GALLERY_N = 16
VID_FRAMES = 48
VIEW_W = 760
VID_W = 640


def hexc(rgb):
    return "#%02x%02x%02x" % rgb


def load_ann(folder):
    d = json.load(open(os.path.join(folder, "output.json"), encoding="utf-8"))
    fps_step = 3  # 30fps × 0.1s
    per_fn = {}   # frameNumber -> list of boxes
    beh_count = {}
    for o in d["objects"]:
        oid = o["id"]
        for f in o["frames"]:
            if not f.get("visible", True):
                continue
            fn = f["frameNumber"]; bb = f["bbox"]; b = f.get("behaviour")
            per_fn.setdefault(fn, []).append(
                {"id": oid, "x": bb["x"], "y": bb["y"], "w": bb["width"],
                 "h": bb["height"], "behavior": b})
            beh_count[b] = beh_count.get(b, 0) + 1
    return per_fn, beh_count, fps_step


def _uri(im, q=75):
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def pick_gallery_frames(per_fn, beh_count):
    """행동 다양성이 큰 프레임 우선 선택(희소 행동 가점)."""
    rare = {b for b, c in beh_count.items() if c < 60}
    scored = []
    for fn, boxes in per_fn.items():
        behs = {b["behavior"] for b in boxes}
        score = len(behs) + 2 * len(behs & rare)
        scored.append((score, fn))
    scored.sort(reverse=True)
    picked, seen = [], set()
    for _, fn in scored:
        if any(abs(fn - p) < 8 for p in seen):   # 간격 확보
            continue
        picked.append(fn); seen.add(fn)
        if len(picked) >= GALLERY_N:
            break
    return sorted(picked)


def build(folder, video):
    per_fn, beh_count, step = load_ann(folder)
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    n_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 갤러리
    gallery = []
    for fn in pick_gallery_frames(per_fn, beh_count):
        cap.set(cv2.CAP_PROP_POS_FRAMES, fn * step)
        ok, frame = cap.read()
        if not ok:
            continue
        im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        W0, H0 = im.size; sc = VIEW_W / W0
        im = im.resize((VIEW_W, int(H0 * sc)))
        boxes = [{"x": round(b["x"] * sc, 1), "y": round(b["y"] * sc, 1),
                  "w": round(b["w"] * sc, 1), "h": round(b["h"] * sc, 1),
                  "behavior": b["behavior"], "id": b["id"],
                  "color": hexc(BEH_COLOR.get(b["behavior"], (140, 140, 140)))}
                 for b in per_fn[fn]]
        gallery.append({"frame_no": fn, "w": VIEW_W, "h": int(H0 * sc),
                        "img": _uri(im), "boxes": boxes})

    # 주석 영상: 연속 구간
    start = min(per_fn) if per_fn else 0
    seq = [fn for fn in sorted(per_fn) if start <= fn < start + VID_FRAMES]
    frames_jpeg = []
    for fn in seq:
        cap.set(cv2.CAP_PROP_POS_FRAMES, fn * step)
        ok, frame = cap.read()
        if not ok:
            continue
        im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        W0, H0 = im.size; sc = VID_W / W0
        h_even = (int(H0 * sc) // 2) * 2
        im = im.resize((VID_W, h_even)); dr = ImageDraw.Draw(im)
        for b in per_fn[fn]:
            x, y, w, h = b["x"]*sc, b["y"]*sc, b["w"]*sc, b["h"]*sc
            c = BEH_COLOR.get(b["behavior"], (140, 140, 140))
            dr.rectangle([x, y, x+w, y+h], outline=c, width=2)
            dr.text((x+2, y+1), b["behavior"], fill=c)
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=80)
        frames_jpeg.append(buf.getvalue())
    cap.release()

    video_uri = None
    if frames_jpeg:
        tmp = tempfile.mkdtemp(); webm = os.path.join(tmp, "o.webm")
        p = subprocess.Popen(
            [FFMPEG, "-y", "-framerate", "6", "-f", "image2pipe", "-vcodec",
             "mjpeg", "-i", "pipe:0", "-c:v", "libvpx", "-b:v", "800k",
             "-pix_fmt", "yuv420p", webm],
            stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        p.communicate(b"".join(frames_jpeg))
        if os.path.exists(webm) and os.path.getsize(webm) > 0:
            video_uri = "data:video/webm;base64," + base64.b64encode(open(webm, "rb").read()).decode()

    legend = [{"cat": cat, "color": hexc(c), "behaviors": bs}
              for cat, (bs, c) in CATS.items()]
    data = {
        "meta": {"recording": os.path.basename(folder.rstrip("/")),
                 "fps": fps, "n_video": n_video,
                 "n_pigs": len({b["id"] for bs in per_fn.values() for b in bs}),
                 "n_gallery": len(gallery), "n_vidframes": len(frames_jpeg)},
        "behavior_dist": sorted(([b, c] for b, c in beh_count.items()),
                                key=lambda x: -x[1]),
        "legend": legend, "gallery": gallery, "video": video_uri,
    }
    return data


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__); return 1
    data = build(sys.argv[1], sys.argv[2])
    html = open(TEMPLATE, encoding="utf-8").read().replace(
        "/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    m = data["meta"]
    print(f"행동 프론트 생성: {OUT} ({os.path.getsize(OUT)/1e6:.1f}MB)")
    print(f"  녹화 {m['recording']} · 갤러리 {m['n_gallery']}장 · 영상 {m['n_vidframes']}프레임 · 돼지 {m['n_pigs']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
