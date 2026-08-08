"""탐지 기반 파생 행동분석 — 축사·세션별 점유 heatmap + 마릿수·활동량 추이.

pig-detection 데이터셋은 bbox(0=pig)만 있고 행동 라벨은 없다. 그러나 multiview
의 pen1/pen2 프레임은 시각(timestamp)이 있어, 탐지만으로 **공간 행동(점유
위치)** 과 **시간 행동(마릿수·활동량 변화)** 을 파생할 수 있다.
  - 점유 heatmap : 세션 동안 bbox 커버리지 누적 → 돼지가 머무는 구역
  - 마릿수 추이  : 프레임별 탐지 수
  - 활동량 추이  : 연속 프레임 간 점유격자 변화(L1) → 급증=이상행동/발정 의심

    python competition/src/build_activity_analysis.py [데이터셋경로]
출력: competition/dashboard/activity_analysis.html
"""
from __future__ import annotations

import base64
import io
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../competition
OUT = os.path.join(ROOT, "dashboard", "activity_analysis.html")
DEFAULT = ("/root/.cache/kagglehub/datasets/rbbbjp/"
           "pig-detection-yolo-dataset-mixed-sources/versions/1")
GRID_W, GRID_H = 48, 36
MIN_FRAMES = 12
MAX_SESSIONS = 6


def sessions(root):
    """(pen,cam,date) 세션별 [(time, img_path, label_path)] 정렬."""
    sess = {}
    for split in ("train", "test"):
        imgd = os.path.join(root, "multiview", split, "images")
        lbld = os.path.join(root, "multiview", split, "labels")
        if not os.path.isdir(imgd):
            continue
        for f in os.listdir(imgd):
            m = re.match(r'(pen\d+)_([a-z]+)_(cam\d+)_(\d{8})_(\d{6})', f)
            if not m:
                continue
            pen, loc, cam, date, tm = m.groups()
            key = (pen, cam, date)
            lbl = os.path.join(lbld, os.path.splitext(f)[0] + ".txt")
            sess.setdefault(key, []).append((tm, os.path.join(imgd, f), lbl))
    for k in sess:
        sess[k].sort()
    return {k: v for k, v in sess.items() if len(v) >= MIN_FRAMES}


def read_boxes(lbl):
    out = []
    if os.path.exists(lbl):
        for ln in open(lbl):
            p = ln.split()
            if len(p) >= 5:
                out.append(tuple(float(x) for x in p[1:5]))  # xc,yc,w,h norm
    return out


def occupancy(boxes):
    g = np.zeros((GRID_H, GRID_W))
    for xc, yc, w, h in boxes:
        x0 = int(max(0, (xc - w / 2) * GRID_W)); x1 = int(min(GRID_W, (xc + w / 2) * GRID_W))
        y0 = int(max(0, (yc - h / 2) * GRID_H)); y1 = int(min(GRID_H, (yc + h / 2) * GRID_H))
        g[y0:max(y1, y0 + 1), x0:max(x1, x0 + 1)] += 1
    return g


def analyze(frames):
    counts, grids = [], []
    for tm, img, lbl in frames:
        b = read_boxes(lbl)
        counts.append(len(b)); grids.append(occupancy(b))
    heat = np.sum(grids, axis=0)
    activity = [0.0]
    for i in range(1, len(grids)):
        a = grids[i] / (grids[i].sum() or 1)
        bprev = grids[i - 1] / (grids[i - 1].sum() or 1)
        activity.append(float(np.abs(a - bprev).sum()))
    return counts, activity, heat


def fig_uri(heat, counts, activity, title):
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.4))
    im = ax[0].imshow(heat, cmap="magma", aspect="auto")
    ax[0].set_title("Occupancy heatmap"); ax[0].set_xticks([]); ax[0].set_yticks([])
    fig.colorbar(im, ax=ax[0], fraction=0.046, pad=0.04)
    ax[1].plot(counts, color="#2a78d6", lw=2); ax[1].set_title("Pig count")
    ax[1].set_xlabel("frame"); ax[1].grid(alpha=.3)
    ax[2].plot(activity, color="#eb6834", lw=2); ax[2].set_title("Activity (occupancy change)")
    ax[2].set_xlabel("frame"); ax[2].grid(alpha=.3)
    peak = int(np.argmax(activity)) if activity else 0
    ax[2].axvline(peak, color="#d03b3b", ls="--", lw=1.2)
    fig.suptitle(title, fontsize=11, x=0.02, ha="left")
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    buf = io.BytesIO(); fig.savefig(buf, format="png", dpi=95); plt.close(fig)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode(), peak


def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    sess = sessions(root)
    top = sorted(sess.items(), key=lambda kv: -len(kv[1]))[:MAX_SESSIONS]
    cards = []
    for (pen, cam, date), frames in top:
        counts, activity, heat = analyze(frames)
        title = f"{pen} · {cam} · {date}  ({len(frames)} frames)"
        uri, peak = fig_uri(heat, counts, activity, title)
        cards.append({"pen": pen, "cam": cam, "date": date, "n": len(frames),
                      "img": uri, "peak": peak, "avg_count": round(np.mean(counts), 1),
                      "peak_act": round(max(activity), 3)})

    tiles = "".join(
        f'<button class="fbtn" data-i="{i}">{c["pen"]}·{c["cam"]}·{c["date"]}</button>'
        for i, c in enumerate(cards))
    figs = "".join(
        f'<div class="fig" data-i="{i}" style="display:{"block" if i==0 else "none"}">'
        f'<img src="{c["img"]}"><div class="meta">평균 마릿수 {c["avg_count"]} · '
        f'최대 활동량 {c["peak_act"]} · 활동 급증 프레임 F{c["peak"]}(빨강 점선) = '
        f'이상행동/발정 의심 시점 후보</div></div>' for i, c in enumerate(cards))
    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>탐지 기반 행동분석</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#f2f2ee;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--ink0:#0b0b0b}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--border:rgba(255,255,255,.14)}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--border:rgba(255,255,255,.14)}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:20px}}
.wrap{{max-width:1100px;margin:0 auto}}h1{{font-size:1.5rem}}.sub{{color:var(--ink2);font-size:.9rem;margin:4px 0 14px}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px;margin-bottom:14px}}
.filters{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}}
.fbtn{{font:inherit;font-size:.78rem;padding:5px 12px;border-radius:999px;cursor:pointer;border:1px solid var(--border);background:var(--surface2);color:var(--ink2)}}.fbtn.on{{background:var(--ink);color:var(--page);border-color:var(--ink)}}
.fig img{{width:100%;border-radius:8px;background:#fff}}.fig .meta{{font-size:.82rem;color:var(--ink2);margin-top:8px}}
.note{{font-size:.72rem;color:var(--muted);margin-top:10px;line-height:1.6}}
.insight{{background:color-mix(in srgb,#2a78d6 8%,transparent);border-left:3px solid #2a78d6;padding:9px 12px;border-radius:6px;font-size:.85rem;margin-top:10px}}
</style></head><body><div class="wrap">
<h1>탐지 기반 행동분석 <span style="font-size:.8rem;color:var(--muted)">pig-detection · multiview</span></h1>
<div class="sub">bbox 탐지만으로 파생한 <b>공간 행동(점유 heatmap)</b> + <b>시간 행동(마릿수·활동량 추이)</b>. 축사·세션(카메라·날짜)별.</div>
<div class="card"><div class="filters">{tiles}</div>{figs}
<div class="insight">활동량(점유 변화)이 급증하는 구간은 <b>이상행동·발정 의심 시점 후보</b>. 점유 heatmap의 집중 구역은 급이·휴식 등 <b>선호 공간</b>을 시사한다.</div>
</div>
<div class="note">※ 이 데이터셋은 탐지(bbox) 라벨만 있어 개체 추적(ID)·정식 행동 라벨은 없다. 따라서 개체별 이동이 아닌 <b>집단 점유·활동</b> 수준의 파생 분석이다. 행동 인식(walk/lie 등)은 Edinburgh 데이터(behavior_gallery)에서 수행.</div>
</div>
<script>
document.querySelectorAll(".fbtn").forEach(b=>b.onclick=()=>{{
  const i=b.dataset.i;
  document.querySelectorAll(".fbtn").forEach(x=>x.classList.toggle("on",x===b));
  document.querySelectorAll(".fig").forEach(f=>f.style.display=f.dataset.i===i?"block":"none");
}});
document.querySelector(".fbtn").classList.add("on");
</script></body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"행동분석 생성: {OUT} ({os.path.getsize(OUT)/1e6:.1f}MB)")
    print(f"  세션 {len(cards)}개: " + ", ".join(f"{c['pen']}·{c['cam']}·{c['date']}({c['n']})" for c in cards))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
