"""실시간 경보 콘솔 — 관리자 아침 점검용 우선순위 큐 + 모바일 알림 목업.

진단(repro_cause_attribution)·조기경보(estrus_early_warning) 결과를 **현장이 바로
행동할 수 있는 형태**로 바꾼다. 상용 제품 대비 비어 있던 "그래서 현장에서 어떻게
쓰나"에 답하는 뷰.

  1) 오늘의 조치 큐 : 긴급도순 정렬 — 누구를, 왜, 무엇을(처방), 언제까지
  2) 모바일 푸시 목업 : 실제 발송될 알림 문구(휴대폰 화면 형태)
  3) 경보 요약 KPI  : 오늘 발정 임박/지연/무발정 두수, 처리 대기

긴급도(priority) = 상태 가중치 + 시간 압박(D-day 임박·경과일) + 위험도.
발정 임박은 **놓치면 그날로 교배 기회가 사라지므로** 최상위로 둔다.

    python competition/src/build_alert_console.py
출력: competition/dashboard/alert_console.html  (외부 연결·라이브러리 불필요)
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
import repro_cause_attribution as rca  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "alert_console.html")

# 상태별 기본 긴급도·색·조치 문구
STATE_META = {
    "발정 임박": (100, "#d03b3b", "교배 준비 — 오늘·내일 승가허용 확인"),
    "발정 확인": (85, "#1baf7a", "적기 교배 실시(12·24시간 간격 2회)"),
    "무발정 경보": (70, "#8b3fd0", "수의 검진 — 난소 상태·성성숙 확인"),
    "발정지연 경보": (55, "#e8a33d", "웅돈 자극 강화 + 원인 요인 개선"),
    "정상 진행": (10, "#898781", "경과 관찰"),
}


def build_alerts(n_sows: int = 120, today: int | None = None) -> pd.DataFrame:
    """오늘 시점의 개체별 경보 + 원인·처방 + 긴급도."""
    long, truth = ew.generate_daily(n_sows=n_sows)
    horizon = int(long["day"].max())
    rng = np.random.default_rng(7)
    # 실제 농장은 개체마다 이유일이 달라 '오늘 기준 경과일'이 제각각이다.
    # today 를 고정하면 전원이 같은 단계에 몰려(예: 전부 발정 확인) 비현실적이므로
    # 개체별로 관측 시점을 분산시킨다(today 인자를 주면 그 값으로 고정).
    cur = {g: (today if today is not None else int(rng.integers(3, horizon + 1)))
           for g in long["individual_id"].unique()}
    rows = []
    for gid, g in long.groupby("individual_id"):
        g = g[g["day"] <= cur[gid]].sort_values("day")
        if not len(g):
            continue
        a = ew.assess(g["day"].tolist(), g["score"].tolist())
        # 개체별 관리요인(원인 귀인 입력) — 실데이터 연결 시 사양 대장으로 교체
        mgmt = {"backfat_mm": rng.uniform(9, 18), "feed_adequacy": rng.uniform(0.4, 1.0),
                "temp_c": rng.uniform(20, 32), "humidity_pct": rng.uniform(50, 85),
                "boar_exposure_min": rng.uniform(0, 25), "facility_score": rng.uniform(0.4, 1.0),
                "water_adequacy": rng.uniform(0.5, 1.0), "nh3_ppm": rng.uniform(8, 35),
                "growth_disease_cnt": int(rng.integers(0, 4))}
        att = rca.attribute(mgmt)
        cause, sev = att["top"]
        base, color, action = STATE_META[a["state"]]
        # 시간 압박: 임박은 ETA 가 짧을수록, 지연/무발정은 경과일이 길수록 급함
        press = 0.0
        if a["state"] == "발정 임박" and a["eta_days"] is not None:
            press = max(0.0, 12 - 4 * float(a["eta_days"]))
        elif a["state"] in ("발정지연 경보", "무발정 경보"):
            press = min(15.0, 0.7 * (a["today"] - ew.NORMAL_WEI))
        rows.append({
            "id": gid, "state": a["state"], "color": color,
            "eta": a["eta_days"], "day": a["today"], "peak": a["peak"],
            "cause": cause, "cause_sev": sev,
            "action": action, "fix": rca.PRESCRIPTION.get(cause, "정밀 검토"),
            "priority": round(base + press + 10 * sev, 1),
        })
    df = pd.DataFrame(rows)
    return df.sort_values("priority", ascending=False).reset_index(drop=True)


def push_text(r) -> tuple:
    """모바일 푸시 문구(제목, 본문)."""
    if r["state"] == "발정 임박":
        eta = "오늘" if (r["eta"] is not None and r["eta"] <= 0.5) else \
              (f"{r['eta']:.0f}일 후" if r["eta"] is not None else "임박")
        return (f"🔴 {r['id']} 발정 임박 ({eta})",
                f"교배 준비하세요. 승가허용 확인 필요. 주원인 {r['cause']}")
    if r["state"] == "발정 확인":
        return (f"🟢 {r['id']} 발정 확인",
                "적기 교배 실시 — 12·24시간 간격 2회 권장")
    if r["state"] == "무발정 경보":
        return (f"🟣 {r['id']} 무발정 {r['day']:.0f}일차",
                f"수의 검진 필요. 주원인 {r['cause']} → {r['fix'][:28]}")
    return (f"🟠 {r['id']} 발정지연 {r['day']:.0f}일차",
            f"주원인 {r['cause']} → {r['fix'][:28]}")


def main() -> int:
    df = build_alerts()
    act = df[df["state"] != "정상 진행"]
    counts = df["state"].value_counts()

    kpis = [
        (int(counts.get("발정 임박", 0)), "발정 임박", "오늘·내일 교배 준비", "#d03b3b"),
        (int(counts.get("발정 확인", 0)), "발정 확인", "적기 교배 실시", "#1baf7a"),
        (int(counts.get("발정지연 경보", 0)), "발정지연", "자극·요인 개선", "#e8a33d"),
        (int(counts.get("무발정 경보", 0)), "무발정", "수의 검진 대상", "#8b3fd0"),
    ]
    kpi_html = "".join(
        f'<div class="kpi" style="border-left:3px solid {c}"><div class="v">{v}</div>'
        f'<div class="l">{l}</div><div class="d">{d}</div></div>'
        for v, l, d, c in kpis)

    # 조치 큐
    rows = ""
    for i, r in act.head(12).iterrows():
        eta = "—" if r["eta"] is None else (
            "오늘" if r["eta"] <= 0.5 else f"D-{r['eta']:.0f}")
        rows += (
            f'<tr><td class="rank">{i + 1}</td>'
            f'<td><b>{r["id"]}</b></td>'
            f'<td><span class="pill" style="background:color-mix(in srgb,{r["color"]} 18%,transparent);'
            f'color:{r["color"]}">{r["state"]}</span></td>'
            f'<td class="eta">{eta}</td>'
            f'<td>{r["cause"]} <span class="mut">({r["cause_sev"]:.0%})</span></td>'
            f'<td>{r["action"]}</td>'
            f'<td class="mut">{r["fix"]}</td></tr>')

    # 모바일 푸시 목업(상위 4건)
    pushes = ""
    for _, r in act.head(4).iterrows():
        t, b = push_text(r)
        pushes += (f'<div class="push"><div class="pt">{t}</div>'
                   f'<div class="pb">{b}</div><div class="pm">양돈 AI · 지금</div></div>')

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>실시간 경보 콘솔</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#eeeeea;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12)}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14)}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14)}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:1040px;margin:0 auto}}h1{{font-size:1.5rem;letter-spacing:-.02em}}
.sub{{color:var(--ink2);font-size:.92rem;margin:5px 0 2px}}
h2{{font-size:1.02rem;margin:22px 0 3px}}.h2d{{font-size:.79rem;color:var(--muted);margin-bottom:11px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:11px;margin:16px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:11px;padding:12px 14px}}
.kpi .v{{font-size:1.9rem;font-weight:700;letter-spacing:-.02em}}.kpi .l{{font-size:.82rem;font-weight:600}}.kpi .d{{font-size:.7rem;color:var(--muted);margin-top:2px}}
.grid{{display:grid;grid-template-columns:1fr 300px;gap:16px;align-items:start}}@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:13px;padding:15px 16px}}
table{{width:100%;border-collapse:collapse;font-size:.82rem}}td,th{{text-align:left;padding:7px 8px;border-bottom:1px solid var(--surface2);vertical-align:top}}
th{{color:var(--muted);font-size:.7rem;text-transform:uppercase;letter-spacing:.03em}}
.rank{{color:var(--muted);font-variant-numeric:tabular-nums}}.eta{{font-weight:700;font-variant-numeric:tabular-nums}}
.pill{{font-size:.71rem;font-weight:700;padding:2px 8px;border-radius:999px;white-space:nowrap}}
.mut{{color:var(--muted)}}
.phone{{background:#1a1a19;border-radius:22px;padding:13px 11px 16px;border:1px solid var(--border)}}
.phone .top{{color:#8b8b85;font-size:.66rem;text-align:center;margin-bottom:9px}}
.push{{background:rgba(255,255,255,.10);border-radius:13px;padding:10px 12px;margin-bottom:8px;backdrop-filter:blur(4px)}}
.pt{{color:#fff;font-weight:700;font-size:.79rem}}.pb{{color:#d2d1c9;font-size:.73rem;margin-top:2px;line-height:1.45}}
.pm{{color:#8b8b85;font-size:.63rem;margin-top:5px}}
.note{{font-size:.73rem;color:var(--muted);margin-top:10px;line-height:1.6}}
</style></head><body><div class="wrap">
<h1>🔔 실시간 경보 콘솔</h1>
<div class="sub">진단·조기경보를 <b>오늘 할 일</b>로 변환. 긴급도순 조치 큐 + 모바일 푸시.</div>
<div class="kpis">{kpi_html}</div>

<div class="grid">
<div>
  <h2>오늘의 조치 큐</h2>
  <div class="h2d">긴급도 = 상태 가중치 + 시간 압박(D-day·경과일) + 원인 심각도. 발정 임박이 최상위(놓치면 교배 기회 소멸).</div>
  <div class="card"><table>
  <tr><th>#</th><th>개체</th><th>상태</th><th>시점</th><th>주원인</th><th>조치</th><th>개선 처방</th></tr>
  {rows}</table>
  <div class="note">전체 {len(df)}두 중 조치 필요 {len(act)}두. 실데이터 연결 시 관리요인은 사양 대장·환경센서로 교체된다.</div>
  </div>
</div>
<div>
  <h2>모바일 푸시</h2>
  <div class="h2d">실제 발송 문구 목업</div>
  <div class="phone"><div class="top">▬▬  09:00  ▬▬</div>{pushes}</div>
  <div class="note">SMTP·FCM 연동 시 그대로 발송된다. 발정 임박은 즉시, 나머지는 아침 일괄.</div>
</div>
</div>

<div class="note">※ 합성 시연 데이터(도메인 관계 반영). 외부 연결·라이브러리 없이 생성.</div>
</div></body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"경보 콘솔 생성: {OUT} ({os.path.getsize(OUT)/1024:.0f}KB)")
    print(f"  전체 {len(df)}두 · 조치 필요 {len(act)}두 · "
          f"임박 {int(counts.get('발정 임박',0))} · 지연 {int(counts.get('발정지연 경보',0))} · "
          f"무발정 {int(counts.get('무발정 경보',0))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
