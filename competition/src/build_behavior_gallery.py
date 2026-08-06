"""행동 확인 프론트 — 여러 농장 CCTV 피드(장척 영상) + 프레임 갤러리.

output.json(주석)과 color.mp4(영상)를 결합해, 각 프레임의 돼지별 행동을 실제
영상 위에 표시한다. 여러 녹화를 '카메라 피드'처럼 전환하며 보고, 각 피드는
장척(수십 초) 주석 영상으로 인코딩한다. (미래 농장 CCTV 를 가정)

매핑: 영상프레임 = frameNumber × (fps × stepSize) = ×3

    python competition/src/build_behavior_gallery.py            # 캐시 영상 자동탐색
    python competition/src/build_behavior_gallery.py <folder> <color.mp4>  # 단일 지정
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
EDIN = os.path.join(ROOT, "competition", "data", "edinburgh")
VIDCACHE = "/tmp/edin_vids"
_ff = glob.glob("/opt/pw-browsers/ffmpeg*/ffmpeg-linux")
FFMPEG = _ff[0] if _ff else "ffmpeg"

CATS = {
    "활동": (["walk", "run", "investigating", "chase", "playwithtoy",
            "nose-poke-elsewhere"], (42, 120, 214)),
    "휴식": (["standing", "sitting", "lying", "sleep"], (27, 175, 122)),
    "섭식": (["eat", "drink"], (237, 161, 0)),
    "사회/번식": (["nose-to-nose", "jumpontopof", "fight"], (232, 123, 164)),
}
BEH_COLOR = {b: c for _, (bs, c) in CATS.items() for b in bs}
STEP = 3
MAX_FEEDS = 6          # 카메라 피드 수
VID_FRAMES = 200       # 피드당 최대 프레임(장척)
VID_FPS = 10           # 재생 fps
VID_W = 560
GALLERY_PER_FEED = 6


def hexc(rgb):
    return "#%02x%02x%02x" % rgb


def discover():
    """output.json + 캐시 영상이 있는 녹화들 → (rec_id, folder, video)."""
    feeds = []
    for date in sorted(os.listdir(EDIN)):
        dpath = os.path.join(EDIN, date)
        if not os.path.isdir(dpath):
            continue
        for vid in sorted(os.listdir(dpath)):
            folder = os.path.join(dpath, vid)
            rec = f"{date}_{vid}"
            if not os.path.exists(os.path.join(folder, "output.json")):
                continue
            cands = [os.path.join(VIDCACHE, rec, "color.mp4")]
            if rec == "2019_11_05_000009":
                cands.append("/tmp/edvid/color.mp4")
            v = next((c for c in cands if os.path.exists(c) and os.path.getsize(c) > 1e6), None)
            if v:
                feeds.append((rec, folder, v))
    return feeds[:MAX_FEEDS]


def load_ann(folder):
    d = json.load(open(os.path.join(folder, "output.json"), encoding="utf-8"))
    per_fn, beh = {}, {}
    for o in d["objects"]:
        for f in o["frames"]:
            if not f.get("visible", True):
                continue
            fn = f["frameNumber"]; bb = f["bbox"]; b = f.get("behaviour")
            per_fn.setdefault(fn, []).append(
                {"id": o["id"], "x": bb["x"], "y": bb["y"], "w": bb["width"],
                 "h": bb["height"], "behavior": b})
            beh[b] = beh.get(b, 0) + 1
    return per_fn, beh


def _uri(im, q=72):
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def build_feed(rec, folder, video):
    per_fn, beh = load_ann(folder)
    cap = cv2.VideoCapture(video)
    fns = sorted(per_fn)[:VID_FRAMES]          # 앞에서부터 장척(연속)
    needed = {fn * STEP: fn for fn in fns}
    rgb = {b: c for b, c in BEH_COLOR.items()}
    frames_jpeg, gallery = [], []
    # 갤러리용: 행동 다양성 큰 프레임 선별
    div = sorted(fns, key=lambda fn: -len({b["behavior"] for b in per_fn[fn]}))[:GALLERY_PER_FEED]
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx in needed:
            fn = needed[idx]
            # 영상 프레임(주석 burn-in)
            im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            W0, H0 = im.size; sc = VID_W / W0; hh = (int(H0 * sc) // 2) * 2
            imv = im.resize((VID_W, hh)); dr = ImageDraw.Draw(imv)
            for b in per_fn[fn]:
                x, y, w, h = b["x"]*sc, b["y"]*sc, b["w"]*sc, b["h"]*sc
                c = BEH_COLOR.get(b["behavior"], (150, 150, 150))
                dr.rectangle([x, y, x+w, y+h], outline=c, width=2)
                dr.text((x+2, y+1), b["behavior"], fill=c)
            buf = io.BytesIO(); imv.save(buf, "JPEG", quality=78)
            frames_jpeg.append(buf.getvalue())
            # 갤러리(원본+좌표)
            if fn in div:
                gW = 720; gsc = gW / W0
                gim = im.resize((gW, int(H0*gsc)))
                gallery.append({"feed": rec, "frame_no": fn, "w": gW, "h": int(H0*gsc),
                                "img": _uri(gim),
                                "boxes": [{"x": round(b["x"]*gsc,1), "y": round(b["y"]*gsc,1),
                                           "w": round(b["w"]*gsc,1), "h": round(b["h"]*gsc,1),
                                           "behavior": b["behavior"],
                                           "color": hexc(BEH_COLOR.get(b["behavior"], (150,150,150)))}
                                          for b in per_fn[fn]]})
        idx += 1
    cap.release()
    video_uri = None
    if frames_jpeg:
        tmp = tempfile.mkdtemp(); webm = os.path.join(tmp, "o.webm")
        p = subprocess.Popen([FFMPEG, "-y", "-framerate", str(VID_FPS), "-f",
                              "image2pipe", "-vcodec", "mjpeg", "-i", "pipe:0",
                              "-c:v", "libvpx", "-b:v", "600k", "-pix_fmt",
                              "yuv420p", webm],
                             stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        p.communicate(b"".join(frames_jpeg))
        if os.path.exists(webm) and os.path.getsize(webm) > 0:
            video_uri = "data:video/webm;base64," + base64.b64encode(open(webm, "rb").read()).decode()
    dur = round(len(frames_jpeg) / VID_FPS, 1)
    return {"rec": rec, "video": video_uri, "n_frames": len(frames_jpeg),
            "dur": dur, "beh": beh}, gallery


def build_multi(feeds):
    feed_data, gallery, beh_total = [], [], {}
    for rec, folder, video in feeds:
        print(f"  피드 {rec} 인코딩 중...")
        fd, g = build_feed(rec, folder, video)
        feed_data.append(fd); gallery += g
        for b, c in fd["beh"].items():
            beh_total[b] = beh_total.get(b, 0) + c
    legend = [{"cat": cat, "color": hexc(c), "behaviors": bs}
              for cat, (bs, c) in CATS.items()]
    return {
        "meta": {"n_feeds": len(feed_data),
                 "n_gallery": len(gallery),
                 "total_dur": round(sum(f["dur"] for f in feed_data), 1)},
        "feeds": [{"rec": f["rec"], "video": f["video"], "n_frames": f["n_frames"],
                   "dur": f["dur"]} for f in feed_data],
        "behavior_dist": sorted(([b, c] for b, c in beh_total.items()), key=lambda x: -x[1]),
        "legend": legend, "gallery": gallery,
    }


def main() -> int:
    if len(sys.argv) >= 3:
        rec = os.path.basename(sys.argv[1].rstrip("/"))
        feeds = [(rec, sys.argv[1], sys.argv[2])]
    else:
        feeds = discover()
    if not feeds:
        print("영상 캐시 없음 (/tmp/edin_vids). 영상 다운로드 후 실행."); return 1
    data = build_multi(feeds)
    html = open(TEMPLATE, encoding="utf-8").read().replace(
        "/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    m = data["meta"]
    print(f"행동 프론트 생성: {OUT} ({os.path.getsize(OUT)/1e6:.1f}MB)")
    print(f"  카메라 피드 {m['n_feeds']}개 · 총 {m['total_dur']}s · 갤러리 {m['n_gallery']}장")
    for f in data["feeds"]:
        print(f"    - {f['rec']}: {f['n_frames']}프레임 {f['dur']}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
