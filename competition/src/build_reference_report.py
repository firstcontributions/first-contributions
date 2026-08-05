"""AI Hub 71471 발정 표준 기반 케글 분석 — 웹 리포트(HTML).

analyze_kaggle_by_reference 의 결과를 한 페이지 리포트로 렌더한다.
  - 71471 발정 표준(행동→발정 가중치)
  - 케글 Edinburgh: 표준 기준 발정 의심 랭킹·분포·유발 카테고리
  - 케글 탐지(multiview): 표준 활동 기준 세션 요약
  - 보정 상태(71471 정답 있으면 지도보정 AUC)

    python competition/src/build_reference_report.py [71471_frames.csv]
출력: competition/dashboard/reference_report.html
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import aihub_estrus_reference as ref  # noqa: E402
import analyze_kaggle_by_reference as akr  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "reference_report.html")


def bars(rows, fmt, color="var(--accent)", neg=False):
    mx = max((abs(v) for _, v in rows), default=1) or 1
    out = []
    for label, v in rows:
        c = "var(--bad)" if (neg and v < 0) else color
        out.append(f'<div class="hbar"><span title="{label}">{label}</span>'
                   f'<div class="track"><div class="fill" style="width:{abs(v)/mx*100:.0f}%;background:{c}"></div></div>'
                   f'<b>{fmt(v)}</b></div>')
    return "".join(out)


def detection_summary():
    try:
        import build_activity_analysis as act
        root = act.DEFAULT
        if not os.path.isdir(root):
            return []
        sess = act.sessions(root)
        top = sorted(sess.items(), key=lambda kv: -len(kv[1]))[:5]
        rows = []
        for (pen, cam, date), fr in top:
            counts, activity, _ = act.analyze(fr)
            rows.append((f"{pen}·{cam}·{date}", len(fr), round(float(np.mean(counts)), 1),
                         round(float(max(activity)), 3),
                         int(np.argmax(activity)) if activity else 0))
        return rows
    except Exception:  # noqa: BLE001
        return []


def main() -> int:
    reference = ref.EstrusReference()
    cal = sys.argv[1] if len(sys.argv) > 1 else None
    cal_note = "규칙 기준(수의학 가중치)"
    if cal and os.path.isfile(cal):
        akr.calibrate_from_71471(reference, cal)
        cal_note = "71471 정답 지도보정됨"

    res = akr.analyze_edinburgh(reference)
    n = len(res); n_hi = int((res["estrus_index"] >= 0.6).sum())

    # 표준 가중치(발정 시사 순)
    wrows = sorted(reference.weights.items(), key=lambda kv: -kv[1])
    # 발정 의심 분포(5구간)
    bins = [0, .2, .4, .6, .8, 1.01]; labels = ["0–20%", "20–40%", "40–60%", "60–80%", "80–100%"]
    hist = np.histogram(res["estrus_index"], bins=bins)[0]
    dist_rows = list(zip(labels, [int(x) for x in hist]))
    # 상위 10두
    top = res.head(10)[["individual_id", "estrus_index", "activity_norm", "ref_drivers"]].values.tolist()
    det = detection_summary()

    kpi = lambda v, l: f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div></div>'
    suspect_rows = "".join(
        f'<tr><td>{i}</td><td><b>{idx:.0%}</b></td><td>{a:.2f}</td><td>{d}</td></tr>'
        for i, idx, a, d in top)
    det_rows = "".join(
        f'<tr><td>{s}</td><td>{f}f</td><td>{c}</td><td>{pa}</td><td>F{pk}</td></tr>'
        for s, f, c, pa, pk in det) or '<tr><td colspan="5" style="color:var(--muted)">탐지 데이터 없음</td></tr>'

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Hub 71471 발정 표준 · 케글 분석 리포트</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#f2f2ee;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--accent:#2a78d6;--bad:#d03b3b;--good:#0ca30c}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5;--bad:#e66767}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5;--bad:#e66767}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:22px}}
.wrap{{max-width:1000px;margin:0 auto}}h1{{font-size:1.5rem}}h2{{font-size:1.02rem;margin:20px 0 10px}}.sub{{color:var(--ink2);font-size:.9rem;margin:4px 0 8px}}
.pill{{display:inline-block;padding:2px 10px;border-radius:999px;font-size:.78rem;font-weight:600;background:color-mix(in srgb,var(--accent) 16%,transparent);color:var(--accent)}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:10px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:11px;padding:12px 14px}}.kpi .v{{font-size:1.5rem;font-weight:700}}.kpi .l{{font-size:.73rem;color:var(--muted)}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px;margin-bottom:14px}}
.hbar{{display:grid;grid-template-columns:120px 1fr 54px;align-items:center;gap:8px;margin:4px 0;font-size:.8rem}}.hbar .track{{background:var(--surface2);border-radius:6px;height:13px;overflow:hidden}}.hbar .fill{{height:100%;border-radius:6px}}
table{{width:100%;border-collapse:collapse;font-size:.82rem}}td,th{{text-align:left;padding:6px 9px;border-bottom:1px solid var(--surface2)}}th{{color:var(--ink2);font-size:.76rem}}
.insight{{background:color-mix(in srgb,var(--accent) 8%,transparent);border-left:3px solid var(--accent);padding:9px 12px;border-radius:6px;font-size:.85rem;margin-top:8px}}
.note{{font-size:.73rem;color:var(--muted);margin-top:10px;line-height:1.6}}
</style></head><body><div class="wrap">
<h1>🐖 AI Hub 71471 발정 표준 · 케글 분석 리포트</h1>
<div class="sub">AI Hub 71471(돼지 발정행동)의 행동·발정 기준을 <b>표준</b>으로, 케글 데이터를 발정 관점에서 분석. <span class="pill">{cal_note}</span></div>

<h2>1. 발정 표준 (71471 기준 · 행동→발정 가중치)</h2>
<div class="card">{bars([(k, v) for k, v in wrows], lambda v: f'{v:+.1f}', neg=True)}
<div class="insight">승가(mounting)·꼬리세움(tailing)·기립(standing)·서성임(restless)이 발정(+), 눕기·앉음이 휴식(−). 다른 데이터의 행동은 이 표준 카테고리로 매핑해 점수화한다.</div></div>

<h2>2. 케글 Edinburgh — 표준 기준 발정 분석</h2>
<div class="kpis">{kpi(n,'개체(pig)')}{kpi(n_hi,'발정 의심(지수≥0.6)')}{kpi(f'{res["estrus_index"].mean():.2f}','평균 발정지수')}</div>
<div class="card"><b style="font-size:.85rem">발정 의심 지수 분포</b>{bars(dist_rows, lambda v: str(v))}</div>
<div class="card"><b style="font-size:.85rem">발정 의심 상위 10두 (표준 기준)</b>
<table><tr><th>개체</th><th>발정지수</th><th>활동량</th><th>표준 유발 카테고리</th></tr>{suspect_rows}</table></div>

<h2>3. 케글 탐지(multiview) — 표준 활동 기준 요약</h2>
<div class="card"><table><tr><th>세션(축사·카메라·날짜)</th><th>프레임</th><th>평균 마릿수</th><th>최대 활동</th><th>급증 시점</th></tr>{det_rows}</table>
<div class="insight">활동 급증 시점(F#)은 표준상 <b>발정·이상행동 의심 시점 후보</b>. 탐지엔 개체ID가 없어 집단 활동 수준.</div></div>

<div class="note">※ 표준 = AI Hub 71471 발정행동. 현재 {cal_note}. 71471 실데이터(발정 정답)를 로컬에서 받아
<code>build_reference_report.py &lt;71471_frames.csv&gt;</code> 로 실행하면 정답으로 표준을 지도보정한 리포트가 생성됩니다.
데이터: Kaggle Edinburgh Pig Behaviour(CC BY-NC 4.0), pig-detection-yolo. 생성 리포트는 커밋 제외.</div>
</div></body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"리포트 생성: {OUT} ({os.path.getsize(OUT)/1024:.0f}KB)")
    print(f"  {cal_note} · 개체 {n} · 발정의심 {n_hi} · 탐지세션 {len(det)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
