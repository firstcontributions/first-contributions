"""개체 추적 → 개체별 발정 타임라인 (실영상).

탐지 bbox 에 IoU 추적으로 개체 ID 를 부여하고(GT ID 로 검증), 개체별 활동·행동을
AI Hub 71471 발정 표준으로 점수화해 '어느 돼지가 언제부터 발정 행동'을 타임라인으로
낸다. 영상엔 추적 ID + 발정 수준 색을 입힌다.

    python competition/src/build_estrus_timeline.py [녹화폴더] [color.mp4]
출력: competition/dashboard/estrus_timeline.html
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
sys.path.insert(0, HERE)
import aihub_estrus_reference as ref  # noqa: E402
import iou_tracker as trk  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "estrus_timeline.html")
EDIN = os.path.join(ROOT, "competition", "data", "edinburgh")
_ff = glob.glob("/opt/pw-browsers/ffmpeg*/ffmpeg-linux")
FFMPEG = _ff[0] if _ff else "ffmpeg"
STEP = 3
WIN = 10            # 발정 점수 윈도우
VID_FRAMES = 220
VID_FPS = 10
VID_W = 600


def load_frames(folder):
    d = json.load(open(os.path.join(folder, "output.json"), encoding="utf-8"))
    per_fn = {}
    for o in d["objects"]:
        for f in o["frames"]:
            if not f.get("visible", True):
                continue
            bb = f["bbox"]
            per_fn.setdefault(f["frameNumber"], []).append(
                ((bb["x"], bb["y"], bb["width"], bb["height"]),
                 {"gt": o["id"], "behavior": f.get("behaviour")}))
    seq = []
    for fn in sorted(per_fn):
        boxes = [b for b, _ in per_fn[fn]]
        metas = [m for _, m in per_fn[fn]]
        seq.append((fn, boxes, metas))
    return seq


def per_track_estrus(members, act_ref, reference):
    """트랙 멤버(시간순) → 프레임별 발정 원점수 시계열."""
    members = sorted(members, key=lambda m: m["frame"])
    frames = [m["frame"] for m in members]
    cx = [m["box"][0] + m["box"][2] / 2 for m in members]
    cy = [m["box"][1] + m["box"][3] / 2 for m in members]
    behs = [m["meta"].get("behavior") for m in members]
    act = [0.0]
    for i in range(1, len(members)):
        act.append(((cx[i] - cx[i-1])**2 + (cy[i] - cy[i-1])**2) ** 0.5)
    scores = []
    for i in range(len(members)):
        lo = max(0, i - WIN + 1)
        a_norm = min(np.mean(act[lo:i+1]) / act_ref, 1.0) if act_ref else 0
        frac = {}
        w = behs[lo:i+1]
        for b in w:
            cat = ref.to_reference(b)
            if cat:
                frac[cat] = frac.get(cat, 0) + 1 / len(w)
        scores.append(reference.score(frac, a_norm))
    return frames, scores


def build(folder, video):
    seq = load_frames(folder)
    tracks = trk.track_sequence(seq, iou_thr=0.3, max_age=5)  # ID 일관성 우선
    ev = trk.evaluate_vs_gt(tracks)
    reference = ref.EstrusReference()

    # 활동 정규화 기준
    alldisp = []
    for members in tracks.values():
        ms = sorted(members, key=lambda m: m["frame"])
        for i in range(1, len(ms)):
            a, b = ms[i-1]["box"], ms[i]["box"]
            alldisp.append((((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5))
    act_ref = float(np.percentile(alldisp, 80)) if alldisp else 25.0

    MIN_LEN = 30       # 지속 트랙만 타임라인에 표시
    tl = []
    for tid, members in tracks.items():
        if len(members) < MIN_LEN:
            continue
        frames, scores = per_track_estrus(members, act_ref, reference)
        tl.append({"tid": tid, "frames": frames, "scores": scores,
                   "n": len(members)})
    # 전 트랙 점수 minmax → 0~1
    alls = [s for t in tl for s in t["scores"]]
    lo, hi = (min(alls), max(alls)) if alls else (0, 1)
    rng = (hi - lo) or 1
    frame_track_score = {}
    for t in tl:
        t["scores"] = [round((s - lo) / rng, 3) for s in t["scores"]]
        t["peak_score"] = max(t["scores"]) if t["scores"] else 0
        t["peak_frame"] = t["frames"][int(np.argmax(t["scores"]))] if t["scores"] else 0
        t["onset"] = next((f for f, s in zip(t["frames"], t["scores"]) if s >= 0.6), None)
        for f, s in zip(t["frames"], t["scores"]):
            frame_track_score[(f, t["tid"])] = s
    tl.sort(key=lambda t: -t["peak_score"])

    # 프레임별 (box→track id) 역맵 (영상 색칠용)
    box_tid = {}
    for tid, members in tracks.items():
        for m in members:
            box_tid[(m["frame"], m["box"])] = tid

    video_uri = build_video(folder, video, box_tid, frame_track_score)
    return {
        "meta": {"rec": os.path.basename(folder.rstrip("/")),
                 "n_tracks": ev["n_tracks"], "n_long": len(tl), "n_gt": ev["n_gt"],
                 "id_consistency": ev["id_consistency"], "fragments": ev["fragments"],
                 "n_suspect": sum(1 for t in tl if t["peak_score"] >= 0.6)},
        "tracks": tl, "video": video_uri,
    }


def est_color(s):
    if s >= 0.6:
        return (208, 59, 59)      # red
    if s >= 0.4:
        return (236, 131, 90)     # orange
    if s >= 0.25:
        return (250, 178, 25)     # yellow
    return (12, 163, 12)          # green


def build_video(folder, video, box_tid, fts):
    cap = cv2.VideoCapture(video)
    fns = sorted({fn for (fn, _) in box_tid})[:VID_FRAMES]
    needed = {fn * STEP: fn for fn in fns}
    frames_jpeg = []
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx in needed:
            fn = needed[idx]
            im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            W0, H0 = im.size; sc = VID_W / W0; hh = (int(H0*sc)//2)*2
            im = im.resize((VID_W, hh)); dr = ImageDraw.Draw(im)
            for (ffn, box), tid in box_tid.items():
                if ffn != fn:
                    continue
                s = fts.get((fn, tid), 0)
                c = est_color(s)
                x, y, w, h = box[0]*sc, box[1]*sc, box[2]*sc, box[3]*sc
                dr.rectangle([x, y, x+w, y+h], outline=c, width=2)
                dr.text((x+2, y+1), f"#{tid} {int(s*100)}%", fill=c)
            buf = io.BytesIO(); im.save(buf, "JPEG", quality=78)
            frames_jpeg.append(buf.getvalue())
        idx += 1
    cap.release()
    if not frames_jpeg:
        return None
    tmp = tempfile.mkdtemp(); webm = os.path.join(tmp, "o.webm")
    p = subprocess.Popen([FFMPEG, "-y", "-framerate", str(VID_FPS), "-f",
                          "image2pipe", "-vcodec", "mjpeg", "-i", "pipe:0",
                          "-c:v", "libvpx", "-b:v", "700k", "-pix_fmt", "yuv420p", webm],
                         stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    p.communicate(b"".join(frames_jpeg))
    if os.path.exists(webm) and os.path.getsize(webm) > 0:
        return "data:video/webm;base64," + base64.b64encode(open(webm, "rb").read()).decode()
    return None


def spark(frames, scores, w=280, h=54):
    if not frames:
        return ""
    x0, x1 = frames[0], frames[-1]; rng = (x1 - x0) or 1
    X = lambda f: 4 + (f - x0) / rng * (w - 8)
    Y = lambda s: h - 4 - s * (h - 10)
    thr = Y(0.6)
    path = " ".join(("M" if i == 0 else "L") + f"{X(f):.1f} {Y(s):.1f}"
                    for i, (f, s) in enumerate(zip(frames, scores)))
    g = (f'<line x1="4" y1="{thr:.1f}" x2="{w-4}" y2="{thr:.1f}" stroke="#d03b3b" '
         f'stroke-width="1" stroke-dasharray="3 3"/>')
    peak_i = int(np.argmax(scores))
    g += (f'<line x1="{X(frames[peak_i]):.1f}" y1="4" x2="{X(frames[peak_i]):.1f}" '
          f'y2="{h-4}" stroke="#ec835a" stroke-width="1"/>')
    g += f'<path d="{path}" fill="none" stroke="#2a78d6" stroke-width="1.6"/>'
    return f'<svg viewBox="0 0 {w} {h}" style="width:{w}px;max-width:100%;height:auto">{g}</svg>'


def main() -> int:
    if len(sys.argv) >= 3:
        folder, video = sys.argv[1], sys.argv[2]
    else:
        folder = os.path.join(EDIN, "2019_11_05", "000009")
        video = next((c for c in ["/tmp/edvid/color.mp4",
                     "/tmp/edin_vids/2019_11_05_000009/color.mp4"]
                     if os.path.exists(c)), None)
    if not (video and os.path.isdir(folder)):
        print("영상/폴더 없음. build_estrus_timeline.py <folder> <color.mp4>"); return 1
    data = build(folder, video)
    m = data["meta"]
    rows = ""
    for t in data["tracks"][:18]:
        onset = f'F{t["onset"]}' if t["onset"] is not None else "—"
        band = "#d03b3b" if t["peak_score"] >= 0.6 else ("#ec835a" if t["peak_score"] >= 0.4 else "#0ca30c")
        rows += (f'<div class="trow"><div class="tid">#{t["tid"]}</div>'
                 f'<div class="sp">{spark(t["frames"], t["scores"])}</div>'
                 f'<div class="tm"><b style="color:{band}">{t["peak_score"]*100:.0f}%</b>'
                 f'<span>발정시작 {onset}</span></div></div>')
    vid = (f'<video src="{data["video"]}" controls autoplay muted loop playsinline '
           f'style="width:100%;max-width:600px;border-radius:10px;border:1px solid var(--border);background:#000"></video>'
           if data["video"] else "<p>영상 없음</p>")
    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0"><title>개체별 발정 타임라인</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#f2f2ee;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12)}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--border:rgba(255,255,255,.14)}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--border:rgba(255,255,255,.14)}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:20px}}
.wrap{{max-width:1000px;margin:0 auto}}h1{{font-size:1.5rem}}.sub{{color:var(--ink2);font-size:.9rem;margin:4px 0 14px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:14px}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:11px;padding:11px 14px}}.kpi .v{{font-size:1.5rem;font-weight:700}}.kpi .l{{font-size:.73rem;color:var(--muted)}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px;margin-bottom:14px}}.card h2{{font-size:1rem;margin-bottom:10px}}
.trow{{display:grid;grid-template-columns:52px 1fr 120px;align-items:center;gap:10px;padding:6px 0;border-bottom:1px solid var(--surface2)}}
.tid{{font-weight:700;font-size:.9rem}}.tm{{font-size:.78rem;color:var(--ink2);display:flex;flex-direction:column}}.tm b{{font-size:1rem}}
.note{{font-size:.72rem;color:var(--muted);margin-top:10px;line-height:1.6}}
.lg{{font-size:.75rem;color:var(--ink2);margin-top:6px}}
</style></head><body><div class="wrap">
<h1>🐖 개체별 발정 타임라인 <span style="font-size:.8rem;color:var(--muted)">{m['rec']} · IoU 추적</span></h1>
<div class="sub">탐지 bbox 에 개체 ID 부여(IoU 추적) → 개체별 활동·행동을 AI Hub 71471 표준으로 점수화 → 발정 타임라인.</div>
<div class="kpis">
<div class="kpi"><div class="v">{m['n_long']}</div><div class="l">지속 트랙(≥30프레임)</div></div>
<div class="kpi"><div class="v">{m['id_consistency']:.2f}</div><div class="l">ID 일관성(vs GT)</div></div>
<div class="kpi"><div class="v">{m['n_gt']}</div><div class="l">실제 개체(GT)</div></div>
<div class="kpi"><div class="v">{m['n_suspect']}</div><div class="l">발정 의심(≥60%)</div></div>
</div>
<div class="card"><h2>📹 추적 영상 (개체 ID + 발정 수준 색)</h2>{vid}
<div class="lg">박스 색 = 발정 점수: <b style="color:#0ca30c">낮음</b> → <b style="color:#fab219">주의</b> → <b style="color:#ec835a">경계</b> → <b style="color:#d03b3b">높음</b>. 라벨 #ID %발정.</div></div>
<div class="card"><h2>개체별 발정 타임라인 (발정 점수↓순)</h2>{rows}
<div class="note">각 선 = 한 개체의 발정 점수(0~1) 시계열, 빨강 점선 = 임계(0.6), 주황 세로선 = 최고점.
발정시작 = 점수가 0.6 을 처음 넘는 프레임.</div></div>
<div class="note">※ IoU 추적은 탐지만으로 개체 ID 를 부여한다(GT ID 로 일관성 검증). 발정 점수는 71471 표준(활동·행동 가중치)
기반 규칙값 — 71471 정답으로 보정 시 확정. 데이터: Edinburgh(CC BY-NC 4.0).</div>
</div></body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"발정 타임라인 생성: {OUT} ({os.path.getsize(OUT)/1e6:.1f}MB)")
    print(f"  추적 {m['n_tracks']}개 · ID일관성 {m['id_consistency']} · GT {m['n_gt']} · 발정의심 {m['n_suspect']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
