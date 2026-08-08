"""번식 문제 진단 · 발정 조기경보 대시보드 (자체완결 HTML, 연결 불필요).

repro_cause_attribution(진단) + estrus_early_warning(조기경보)의 결과를 한 화면에:
  1) 번식 문제 유형 분포(정상·이유후지연·무발정·미약)
  2) 위험군 원인 4종 기여(영양·더위·수퇘지자극·사양관리)
  3) 발정 조기경보 타임라인(유형별 일별 준비도 궤적 + D-day/경보)
  4) 위험 상위 개체 종합 진단표(문제유형·주원인·처방)

외부 연결·라이브러리 없이 SVG로 그린다. 합성 시연 데이터(도메인 관계 반영);
71471/71763 실데이터가 오면 동일 파이프라인에 그대로 연결된다.

    python competition/src/build_repro_dashboard.py
출력: competition/dashboard/repro_dashboard.html
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import estrus_early_warning as ew  # noqa: E402
import pipeline_gilt  # noqa: E402
import repro_cause_attribution as rca  # noqa: E402
import train as train_mod  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "repro_dashboard.html")
PROB_COLORS = {"정상 진행": "#1baf7a", "이유후 발정지연": "#e8a33d",
               "무발정": "#d03b3b", "미약(둔성) 발정": "#e07b39",
               "정상": "#1baf7a"}
TYPE_COLOR = {"normal": "#1baf7a", "delayed": "#e8a33d",
              "silent": "#e07b39", "anestrus": "#d03b3b"}
TYPE_KO = {"normal": "정상 발정", "delayed": "이유후 지연",
           "silent": "미약(둔성)", "anestrus": "무발정"}


# ---------------------------------------------------------------- 데이터 준비
def build_diagnosis():
    """진단(문제유형·원인) 결과 DataFrame."""
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.model_selection import StratifiedKFold, cross_val_predict
    frames, mgmt = pipeline_gilt.generate_joint(n_gilts=400)
    signals = pipeline_gilt.build_cctv_signals(frames)
    df = mgmt.merge(signals, on="individual_id", how="inner")
    y = df["anestrus"].astype(int).to_numpy()
    drop = {"anestrus", "individual_id", "farm"}
    feats = [c for c in df.columns if c not in drop]
    num = [c for c in feats if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in feats if c not in num]
    pipe = train_mod.make_pipeline(num, cat, GradientBoostingClassifier(random_state=42))
    cv = StratifiedKFold(5, shuffle=True, random_state=42)
    df = df.copy()
    df["risk"] = cross_val_predict(pipe, df[num + cat], y, cv=cv,
                                   method="predict_proba")[:, 1]
    ctx = rca.signal_context(df)
    diags = [rca.diagnose(r, r["risk"], ctx) for _, r in df.iterrows()]
    df["problem"] = [d["problem"] for d in diags]
    df["cause"] = [d["cause"] for d in diags]
    df["cause_sev"] = [d["cause_severity"] for d in diags]
    df["action"] = [d["action"] for d in diags]
    df["_diag"] = diags
    return df


def build_warning():
    """조기경보 타임라인 + 지표."""
    long, truth = ew.generate_daily(n_sows=300)
    rows = []
    for gid, g in long.groupby("individual_id"):
        g = g.sort_values("day")
        t = ew.timeline(g["day"].tolist(), g["score"].tolist())
        t["individual_id"] = gid
        rows.append(t)
    rdf = pd.DataFrame(rows).merge(truth, on="individual_id")
    y_true = ((rdf["onset_true"].isna()) | (rdf["onset_true"] > ew.NORMAL_WEI)).astype(int)
    y_pred = rdf["alert_day"].notna().astype(int)
    from sklearn.metrics import precision_score, recall_score
    got = rdf[rdf["onset_actual"].notna() & rdf["imminent_day"].notna()].copy()
    lead = None
    if len(got):
        lead = float((got["onset_actual"] - got["imminent_day"]).mean())
    metrics = {
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "n_problem": int(y_true.sum()), "lead": lead,
    }
    # 유형별 대표 궤적(그래프용)
    examples = {}
    for t in ["normal", "delayed", "silent", "anestrus"]:
        gid = truth[truth["type"] == t]["individual_id"].iloc[0]
        g = long[long["individual_id"] == gid].sort_values("day")
        tl = rdf[rdf["individual_id"] == gid].iloc[0]
        examples[t] = {"days": g["day"].tolist(), "scores": g["score"].tolist(),
                       "onset": tl["onset_actual"], "imminent": tl["imminent_day"],
                       "alert": tl["alert_day"]}
    return rdf, metrics, examples


# ---------------------------------------------------------------- SVG 헬퍼
def hbar(rows, w=580, rh=30, gap=8, maxv=None, val_w=110):
    """rows=[(label, value, color, right_text)] → 수평 막대 SVG."""
    maxv = maxv or (max((v for _, v, *_ in rows), default=1) or 1)
    lab_w = 130
    bw = w - lab_w - val_w
    h = len(rows) * (rh + gap)
    out = [f'<svg viewBox="0 0 {w} {h}" width="100%" role="img">']
    for i, (lab, v, col, rt) in enumerate(rows):
        y = i * (rh + gap)
        ln = max(2, bw * v / maxv)
        out.append(f'<text x="0" y="{y+rh*0.68}" font-size="13" fill="var(--ink2)">{lab}</text>')
        out.append(f'<rect x="{lab_w}" y="{y}" width="{bw}" height="{rh}" rx="5" fill="var(--surface2)"/>')
        out.append(f'<rect x="{lab_w}" y="{y}" width="{ln:.1f}" height="{rh}" rx="5" fill="{col}"/>')
        out.append(f'<text x="{lab_w+bw+8}" y="{y+rh*0.68}" font-size="13" font-weight="700" fill="var(--ink)">{rt}</text>')
    out.append('</svg>')
    return "".join(out)


def line_chart(examples, thr=ew.ONSET_THR, w=680, h=300):
    """유형별 일별 준비도 궤적 + 임계선 + 발정/경보 마커."""
    pad_l, pad_b, pad_t, pad_r = 38, 28, 14, 12
    maxd = max(max(e["days"]) for e in examples.values())
    px = lambda d: pad_l + (w - pad_l - pad_r) * d / maxd
    py = lambda s: pad_t + (h - pad_t - pad_b) * (1 - s)
    out = [f'<svg viewBox="0 0 {w} {h}" width="100%" role="img">']
    # 격자·축
    for gy in (0, 0.25, 0.5, 0.75, 1.0):
        yy = py(gy)
        out.append(f'<line x1="{pad_l}" y1="{yy:.1f}" x2="{w-pad_r}" y2="{yy:.1f}" stroke="var(--border)" stroke-width="1"/>')
        out.append(f'<text x="4" y="{yy+4:.1f}" font-size="10" fill="var(--muted)">{gy:.2f}</text>')
    for gx in range(0, int(maxd) + 1, 3):
        out.append(f'<text x="{px(gx)-4:.1f}" y="{h-8}" font-size="10" fill="var(--muted)">{gx}</text>')
    # 임계선
    out.append(f'<line x1="{pad_l}" y1="{py(thr):.1f}" x2="{w-pad_r}" y2="{py(thr):.1f}" stroke="#888" stroke-dasharray="5 4" stroke-width="1.3"/>')
    out.append(f'<text x="{w-pad_r-2}" y="{py(thr)-4:.1f}" font-size="10" text-anchor="end" fill="#888">발정 임계 {thr}</text>')
    # 궤적
    for t, e in examples.items():
        col = TYPE_COLOR[t]
        pts = " ".join(f"{px(d):.1f},{py(s):.1f}" for d, s in zip(e["days"], e["scores"]))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.2" opacity="0.9"/>')
        # 발정 확인일 마커(●)
        if e["onset"] is not None and not pd.isna(e["onset"]):
            d = e["onset"]; s = e["scores"][min(int(d), len(e["scores"])-1)]
            out.append(f'<circle cx="{px(d):.1f}" cy="{py(max(s,thr)):.1f}" r="4.5" fill="{col}" stroke="#fff" stroke-width="1.3"/>')
        # 경보일 마커(▲) — 지연/무발정
        if e["alert"] is not None and not pd.isna(e["alert"]):
            d = e["alert"]; s = e["scores"][min(int(d), len(e["scores"])-1)]
            xx, yy = px(d), py(s)
            out.append(f'<path d="M{xx:.1f},{yy-7:.1f} l5,9 l-10,0 z" fill="{col}" stroke="#fff" stroke-width="1"/>')
    out.append('</svg>')
    # 범례
    leg = "".join(
        f'<span class="lg"><i style="background:{TYPE_COLOR[t]}"></i>{TYPE_KO[t]}</span>'
        for t in examples)
    return "".join(out), leg


# ---------------------------------------------------------------- 렌더
def main() -> int:
    print("진단 파이프라인..."); dg = build_diagnosis()
    print("조기경보 타임라인..."); rdf, mets, ex = build_warning()

    n = len(dg)
    prob_counts = dg["problem"].value_counts()
    prob_rows = [(p, int(prob_counts.get(p, 0)),
                  PROB_COLORS.get(p, "#888"),
                  f"{int(prob_counts.get(p,0))}두 ({prob_counts.get(p,0)/n:.0%})")
                 for p in ["정상", "이유후 발정지연", "미약(둔성) 발정", "무발정"]]
    prob_svg = hbar(prob_rows, maxv=n)

    hi = dg[dg["risk"] >= 0.5]
    cause_rows = []
    if len(hi):
        agg = {c: float(np.mean([rca.attribute(r)["share"][c] for _, r in hi.iterrows()]))
               for c in rca.CAUSE_GROUPS}
        cmax = max(agg.values()) or 1
        cols = {"영양 부족": "#3987e5", "더위 스트레스": "#d03b3b",
                "수퇘지 자극 부족": "#9b59b6", "사양 관리 불량": "#e8a33d"}
        for c, v in sorted(agg.items(), key=lambda kv: -kv[1]):
            cause_rows.append((c, v, cols.get(c, "#888"), f"{v:.0%}"))
    cause_svg = hbar(cause_rows, maxv=cmax if cause_rows else 1)

    chart_svg, legend = line_chart(ex)

    # 위험 상위 진단표
    trows = ""
    for _, r in dg.sort_values("risk", ascending=False).head(8).iterrows():
        pc = PROB_COLORS.get(r["problem"], "#888")
        trows += (f'<tr><td>{r["individual_id"]}</td>'
                  f'<td><b>{r["risk"]:.0%}</b></td>'
                  f'<td><span class="pill" style="background:color-mix(in srgb,{pc} 18%,transparent);color:{pc}">{r["problem"]}</span></td>'
                  f'<td>{r["cause"]} <span style="color:var(--muted)">({r["cause_sev"]:.0%})</span></td>'
                  f'<td style="color:var(--ink2)">{r["action"]}</td></tr>')

    lead_txt = "—" if mets["lead"] is None else f"+{mets['lead']:.1f}일"
    kpis = [
        (f"{n}", "관리 후보돈(두)", "합성 시연 코호트"),
        (f"{(dg['problem']!='정상').mean():.0%}", "번식 문제 의심율", "지연·무발정·미약 합계"),
        (f"{mets['recall']:.0%}", "문제 조기 포착 재현율", f"WEI>{ew.NORMAL_WEI}·무발정 {mets['n_problem']}두"),
        (lead_txt, "발정 임박 리드타임", "실제 발정 전 선제 경보"),
    ]
    kpi_html = "".join(
        f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div><div class="d">{d}</div></div>'
        for v, l, d in kpis)

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>번식 문제 진단·발정 조기경보</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#eeeeea;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--accent:#2a78d6}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:1000px;margin:0 auto}}h1{{font-size:1.55rem;letter-spacing:-.02em}}.sub{{color:var(--ink2);font-size:.92rem;margin:5px 0 4px}}
h2{{font-size:1.02rem;margin:22px 0 4px}}.h2d{{font-size:.8rem;color:var(--muted);margin-bottom:12px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:16px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:13px 15px}}
.kpi .v{{font-size:1.7rem;font-weight:700;letter-spacing:-.02em}}.kpi .l{{font-size:.8rem;font-weight:600;margin-top:1px}}.kpi .d{{font-size:.7rem;color:var(--muted);margin-top:3px}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:13px;padding:17px 18px;margin-bottom:14px}}
.lg{{display:inline-flex;align-items:center;gap:5px;font-size:.78rem;color:var(--ink2);margin-right:14px}}.lg i{{width:12px;height:12px;border-radius:3px;display:inline-block}}
table{{width:100%;border-collapse:collapse;font-size:.83rem;margin-top:4px}}td,th{{text-align:left;padding:7px 9px;border-bottom:1px solid var(--surface2);vertical-align:top}}th{{color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.03em}}
.pill{{font-size:.72rem;font-weight:700;padding:2px 8px;border-radius:999px;white-space:nowrap}}
.note{{font-size:.73rem;color:var(--muted);margin-top:10px;line-height:1.6}}
.legend{{margin-top:8px}}
</style></head><body><div class="wrap">
<h1>🩺 번식 문제 진단 · 발정 조기경보</h1>
<div class="sub">CCTV 관찰을 <b>문제 유형(3종) 진단 → 원인(4종) 귀인 → 발정 예상일·경보</b>로 연결. 육안 관찰 전에 선제 포착.</div>
<div class="kpis">{kpi_html}</div>

<h2>1. 번식 문제 유형 분포</h2>
<div class="h2d">활동량·기립/꼬리세움 비율(개체군 상대) + 위험도로 판정. 미약발정이 많을수록 CCTV의 가치가 큼(육안으로 놓치기 쉬움).</div>
<div class="card">{prob_svg}</div>

<h2>2. 위험군 원인 기여 (무발정 위험 ≥ 50%)</h2>
<div class="h2d">각 개체의 관리·환경 요인을 4대 원인으로 귀인해 평균. 농장 개선 우선순위를 지목한다.</div>
<div class="card">{cause_svg}</div>

<h2>3. 발정 조기경보 타임라인</h2>
<div class="h2d">이유 후 일별 발정 준비도 궤적. ● 발정 확인일 · ▲ 지연/무발정 경보일. 추세를 외삽해 발정 예상일(D-day)을 선제 경보.</div>
<div class="card">{chart_svg}<div class="legend">{legend}</div>
<div class="note">정상(초록)은 4~7일 발정, 이유후지연(주황)·미약(연주황)은 늦거나 낮게 상승, 무발정(빨강)은 임계 미도래 → 21일차 경보.</div></div>

<h2>4. 위험 상위 개체 종합 진단</h2>
<div class="card"><table>
<tr><th>개체</th><th>무발정 위험</th><th>문제 유형</th><th>주원인(심각도)</th><th>처방</th></tr>
{trows}</table>
<div class="note">위험·문제유형은 CCTV 관찰 기반, 원인·처방은 관리/환경 요인 귀인. 실데이터(71471/71763) 연결 시 동일 파이프라인에서 실측으로 교체.</div></div>

<div class="note">※ 합성 시연 데이터(도메인 관계 반영). 외부 연결·라이브러리 없이 생성. 커밋 제외(로컬 생성).</div>
</div></body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"번식 대시보드 생성: {OUT} ({os.path.getsize(OUT)/1024:.0f}KB)")
    print(f"  문제 의심율 {(dg['problem']!='정상').mean():.0%} · 조기포착 재현율 "
          f"{mets['recall']:.0%} · 리드타임 {lead_txt}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
