"""돈군흐름 관제 — 분만틀에서 역산한 설계, 그리고 어디서 막히는가.

번식 관리는 "이 모돈을 언제 교배하나"이고, 돈군흐름은 "그 배치가 나갈 자리가
있나"다. 둘은 같은 문제의 앞뒤다. 발정을 놓쳐 배치가 흩어지면 올인올아웃이
깨지고, 비육사가 모자라면 앞 단계가 밀려 이유 자돈이 갈 곳을 잃는다.

이 뷰가 다른 뷰와 다른 점: **설비 결정을 다룬다.** 다른 화면은 오늘 무엇을
할지를 말하고, 이 화면은 몇 년을 쓸 돈사를 어떻게 지을지를 말한다.

  1) 분만틀에서 역산한 설계     분만틀이 유일한 고정 물리량이다
  2) 필요 vs 보유 돈방          부족분이 곧 병목
  3) 돈방 점유 간트             AIAO 가 지켜지는지는 그림이 빠르다
  4) 시뮬레이션 병목            365일을 하루씩 돌린 결과
  5) 배치 시스템 what-if        같은 분만틀로 무엇이 달라지나
  6) KPI vs 벤치마크            PSY/MSY 를 어디에 대는가
  7) 발정 탐지와의 연결          이유 후 7일이 배치를 만든다

    python competition/src/build_pigflow_console.py
출력: competition/dashboard/pigflow_console.html  (외부 연결 불필요)
"""
from __future__ import annotations

import html as _html
import os
import sys
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "competition"))

import farm_economics as fe            # noqa: E402
from pigflow import calc, report, validate                      # noqa: E402
from pigflow.config import load_config                          # noqa: E402
from pigflow.simulator import Simulator, build_rooms            # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "pigflow_console.html")
YAML = os.path.join(ROOT, "competition", "pigflow", "example_farm.yaml")
E = _html.escape
START = date(2026, 1, 1)
SIM_DAYS = 420

HOUSE_KO = {"farrowing": "분만사", "nursery": "자돈사", "grower": "육성사",
            "finisher": "비육사"}
STAGE_COLOR = {"SUCKLING": "#d4728a", "NURSERY_1": "#6aa9dd",
               "NURSERY_2": "#4b86c4", "GROWER": "#5ba36b",
               "FINISHER": "#c79338"}


# -- SVG ------------------------------------------------------------------
def need_have_bars(rows, width=880) -> str:
    """스테이지별 필요 vs 보유 — 부족한 돈사는 붉게.

    같은 돈사를 두 스테이지가 나눠 쓰면 보유 막대는 돈사 단위라 두 행이 같은
    값을 갖는다. 그게 맞다 — 방을 스테이지에 미리 못 박아 두지 않는다.
    """
    lbl_w, val_w, bar_h, gap, grp = 150, 132, 15, 4, 13
    plot = width - lbl_w - val_w
    mx = max(max(r["rooms_required"], r["house_have"]) for r in rows) * 1.1 or 1
    h = len(rows) * (bar_h * 2 + gap + grp) + 20
    p, y = [], 8
    for r in rows:
        need, have = r["rooms_required"], r["house_have"]
        short = r["shortage"] > 0
        col = STAGE_COLOR.get(r["stage"], "#888")
        p.append(f'<text x="{lbl_w - 8}" y="{y + bar_h}" class="bl hi" '
                 f'text-anchor="end">{E(r["name_ko"])}</text>')
        p.append(f'<text x="{lbl_w - 8}" y="{y + bar_h * 2 + gap - 2}" '
                 f'class="tk" text-anchor="end">{E(HOUSE_KO.get(r["house"], r["house"]))}'
                 f' · 점유 {r["occupancy_days"]}일</text>')
        w1 = max(2, plot * need / mx)
        p.append(f'<rect x="{lbl_w}" y="{y}" width="{w1:.1f}" height="{bar_h}" '
                 f'rx="3" fill="{col}"/>'
                 f'<text x="{lbl_w + w1 + 6:.1f}" y="{y + bar_h - 3}" '
                 f'class="bv">필요 {need}</text>')
        w2 = max(2, plot * have / mx)
        yy = y + bar_h + gap
        p.append(f'<rect x="{lbl_w}" y="{yy}" width="{w2:.1f}" height="{bar_h}" '
                 f'rx="3" fill="{col}" fill-opacity=".32"/>')
        tail = (f'<tspan fill="#d03b3b" font-weight="700"> 부족 {r["shortage"]}</tspan>'
                if short else "")
        p.append(f'<text x="{lbl_w + w2 + 6:.1f}" y="{yy + bar_h - 3}" '
                 f'class="bv">보유 {have}{tail}</text>')
        if short:
            # 부족분을 붉은 점선으로 이어 보여준다
            x0 = lbl_w + w2
            x1 = lbl_w + plot * need / mx
            p.append(f'<line x1="{x0:.1f}" y1="{yy + bar_h / 2}" x2="{x1:.1f}" '
                     f'y2="{yy + bar_h / 2}" stroke="#d03b3b" stroke-width="2" '
                     f'stroke-dasharray="3 3"/>')
        y += bar_h * 2 + gap + grp
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" role="img" '
            f'aria-label="스테이지별 필요 돈방과 보유 돈방 비교">'
            f'{"".join(p)}</svg>')


def gantt_svg(sim, houses, days=126, width=900) -> str:
    """돈방 점유 간트 — 재실은 스테이지 색, 세척은 빗금.

    AIAO 가 지켜지면 블록 사이에 반드시 빗금(세척)이 낀다. 블록이 맞붙어
    있으면 세척 없이 다음 배치가 들어간 것이고, 그건 배칭을 하는 의미가 없다.
    """
    cut = sim.start + timedelta(days=sim.warmup_days)
    end = cut + timedelta(days=days)
    dt_by_house = report.downtime_by_house(sim.cfg)
    rooms = [r for r in sim.rooms if r.house in houses]
    lbl_w, row_h, gap = 84, 17, 4
    plot = width - lbl_w - 8
    px = plot / days
    top = 24
    h = top + len(rooms) * (row_h + gap) + 26
    occ = report.occupancy_spans(sim)
    p = [f'<defs><pattern id="wash" width="5" height="5" '
         f'patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<rect width="5" height="5" fill="var(--surface2)"/>'
         f'<line x1="0" y1="0" x2="0" y2="5" stroke="var(--muted)" '
         f'stroke-width="1.4" opacity=".55"/></pattern></defs>']
    # 월 눈금
    d = cut
    while d < end:
        nxt = (d.replace(day=1) + timedelta(days=32)).replace(day=1)
        x = lbl_w + (d - cut).days * px
        p.append(f'<line x1="{x:.1f}" y1="{top - 6}" x2="{x:.1f}" '
                 f'y2="{h - 22}" stroke="var(--border)" stroke-width="1"/>'
                 f'<text x="{x + 3:.1f}" y="{top - 10}" class="tk">'
                 f'{d:%-m월}</text>')
        d = nxt
    y = top
    for r in rooms:
        p.append(f'<text x="{lbl_w - 7}" y="{y + row_h - 4}" class="bl" '
                 f'text-anchor="end">{E(r.room_id)}</text>')
        p.append(f'<rect x="{lbl_w}" y="{y}" width="{plot:.1f}" '
                 f'height="{row_h}" rx="3" fill="var(--surface2)" '
                 f'fill-opacity=".5"/>')
        wash = dt_by_house.get(r.house, 0)
        for (s, e, bid, sid, n) in occ.get(r.room_id, []):
            if e <= cut or s >= end:
                continue
            x0 = lbl_w + max(0, (s - cut).days) * px
            x1 = lbl_w + min(days, (e - cut).days) * px
            w = max(1.0, x1 - x0)
            col = STAGE_COLOR.get(sid, "#888")
            p.append(f'<rect x="{x0:.1f}" y="{y}" width="{w:.1f}" '
                     f'height="{row_h}" rx="3" fill="{col}">'
                     f'<title>{E(bid)} · {E(sid)} · {n}두\n'
                     f'{s:%Y-%m-%d} → {e:%Y-%m-%d} ({(e - s).days}일)</title>'
                     f'</rect>')
            if w > 26:
                p.append(f'<text x="{x0 + 4:.1f}" y="{y + row_h - 5}" '
                         f'class="gb">{E(bid)}</text>')
            # 세척 구간
            ws = lbl_w + (e - cut).days * px
            we = lbl_w + min(days, (e - cut).days + wash) * px
            if we > ws and (e - cut).days < days:
                p.append(f'<rect x="{ws:.1f}" y="{y}" width="{we - ws:.1f}" '
                         f'height="{row_h}" rx="2" fill="url(#wash)">'
                         f'<title>세척·소독·건조 {wash}일</title></rect>')
        y += row_h + gap
    leg = []
    lx = lbl_w
    for sid in ("SUCKLING", "NURSERY_1", "NURSERY_2", "GROWER", "FINISHER"):
        if not any(r.house == sim.cfg.stage(sid).house for r in rooms):
            continue
        nm = sim.cfg.stage(sid).name_ko
        leg.append(f'<rect x="{lx}" y="{h - 16}" width="9" height="9" rx="2" '
                   f'fill="{STAGE_COLOR[sid]}"/>'
                   f'<text x="{lx + 13}" y="{h - 8}" class="tk">{E(nm)}</text>')
        lx += 22 + len(nm) * 11
    leg.append(f'<rect x="{lx}" y="{h - 16}" width="9" height="9" rx="2" '
               f'fill="url(#wash)"/><text x="{lx + 13}" y="{h - 8}" '
               f'class="tk">세척(공백기)</text>')
    p += leg
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" role="img" '
            f'aria-label="돈방 점유 간트">{"".join(p)}</svg>')


def bench_bars(psy, msy, width=880) -> str:
    """PSY/MSY 를 국내 평균·상위·덴마크에 나란히 댄다."""
    rows = [("이 설계 (시뮬레이션)", psy, msy, True)]
    for name, v in fe.gf.BENCHMARKS.items():
        rows.append((name, v["psy"], v["msy"], False))
    lbl_w, val_w, bar_h, gap, grp = 176, 118, 14, 4, 12
    plot = width - lbl_w - val_w
    mx = max(max(r[1], r[2]) for r in rows) * 1.08
    h = len(rows) * (bar_h * 2 + gap + grp) + 22
    p, y = [], 8
    for name, a, b, hi in rows:
        p.append(f'<text x="{lbl_w - 8}" y="{y + bar_h + 2}" '
                 f'class="{"bl hi" if hi else "bl"}" text-anchor="end">'
                 f'{E(name)}</text>')
        for j, (v, col, tag) in enumerate(((a, "#2a78d6", "PSY"),
                                           (b, "#e8a33d", "MSY"))):
            w = max(2, plot * v / mx)
            yy = y + j * (bar_h + gap)
            p.append(f'<rect x="{lbl_w}" y="{yy}" width="{w:.1f}" '
                     f'height="{bar_h}" rx="3" fill="{col}" '
                     f'fill-opacity="{"1" if hi else ".6"}"/>'
                     f'<text x="{lbl_w + w + 6:.1f}" y="{yy + bar_h - 3}" '
                     f'class="bv">{tag} {v:.1f}</text>')
        y += bar_h * 2 + gap + grp
    p.append(f'<text x="{lbl_w}" y="{h - 6}" class="tk">'
             f'<tspan fill="#2a78d6">■</tspan> PSY(이유두수/모돈/년) &#160;'
             f'<tspan fill="#e8a33d">■</tspan> MSY(출하두수/모돈/년)</text>')
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" role="img" '
            f'aria-label="PSY MSY 벤치마크 비교">{"".join(p)}</svg>')


# -- 본문 -----------------------------------------------------------------
def main() -> int:
    cfg = load_config(YAML).merged()
    p = calc.plan(cfg)
    rooms = build_rooms(cfg)
    rt = report.rooms_table(cfg, rooms)
    sim = Simulator(cfg, START, rooms=rooms).run(SIM_DAYS)
    s = validate.summarize(sim.findings)
    k = report.kpi_report(sim)
    bn = report.bottlenecks(sim)
    wf = report.whatif_table(cfg)

    # 설계대로 지었을 때(부족 0)와 대비 — 도구가 거짓 경보를 내지 않는다는 증거
    clean = Simulator(cfg, START, rooms=build_rooms(cfg, from_config=False)
                      ).run(SIM_DAYS)
    clean_n = validate.summarize(clean.findings)["n"]

    # 부족·잉여는 **돈사 단위**로 한 번씩만 센다. 스테이지 행을 그대로 합하면
    # 자돈사처럼 두 스테이지가 나눠 쓰는 돈사가 두 번 계산된다.
    by_house = {}
    for r in rt:
        by_house[r["house"]] = (r["house_required"], r["house_have"])
    deficit = sum(max(0, n - h) for n, h in by_house.values())
    surplus = sum(max(0, h - n) for n, h in by_house.values())
    short = [r for r in rt if r["shortage"] > 0]
    houses = sorted({r["house"] for r in rt},
                    key=lambda x: [r["house"] for r in rt].index(x))
    short_names = ", ".join(
        f'{HOUSE_KO.get(h, h)} {n - hv}방'
        for h, (n, hv) in by_house.items() if n > hv)
    surp_names = ", ".join(
        f'{HOUSE_KO.get(h, h)} {hv - n}방'
        for h, (n, hv) in by_house.items() if hv > n)

    kpis = [
        (f'{cfg.crate_count}', "분만틀 (설계 기준)",
         f'배치당 교배 {p["services_per_batch"]}두 · '
         f'후보돈 {p["gilts_per_batch"]}두'),
        (f'{p["sow_inventory"]:.0f}', "번식돈군 규모(두)",
         f'{p["batch_system"]} {p["interval_weeks"]}주 간격 · '
         f'{p["groups_required"]}개 배치'),
        (f'{sum(r["rooms_required"] for r in rt)}', "필요 돈방 (보유 "
         + f'{len(rooms)})',
         (f'<b style="color:#d03b3b">{short_names} 부족</b>'
          + (f' · {surp_names} 잉여' if surp_names else ""))
         if deficit else "돈사별로 모두 충족"),
        (f'{len(bn)}', "병목 스테이지",
         f'{SIM_DAYS}일 시뮬레이션 · 오류 {s["errors"]}건'),
    ]
    kpi_html = "".join(
        f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div>'
        f'<div class="d">{d}</div></div>' for v, l, d in kpis)

    # 병목 상세
    msgs = {}
    for f in sim.findings:
        msgs[(f.check, f.message)] = msgs.get((f.check, f.message), 0) + 1
    bn_html = ""
    if bn:
        for (chk, msg), n in sorted(msgs.items(), key=lambda x: -x[1]):
            bn_html += (f'<div class="bnrow"><span class="tag err">{E(chk)}</span>'
                        f'<span>{E(msg)}</span>'
                        f'<span class="cnt">{n}일</span></div>')
    else:
        bn_html = ('<div class="ok">병목 없음 — 모든 배치가 제 일령에 다음 '
                   '돈방으로 이동했다.</div>')

    # what-if 표
    stage_ids = [x.id for x in cfg.flow_stages]
    wf_head = "".join(f"<th>{E(cfg.stage(i).name_ko)}</th>" for i in stage_ids)
    wf_rows = ""
    cur = cfg.batch_system_id
    for r in wf:
        hi = ' class="cur"' if r["system"] == cur else ""
        cells = "".join(f'<td>{r["rooms"][i]}</td>' for i in stage_ids)
        wf_rows += (
            f'<tr{hi}><td><b>{E(r["system"])}</b>'
            + (' <span class="tag">현재</span>' if r["system"] == cur else "")
            + f'</td><td>{r["interval_weeks"]}주</td><td>{r["groups"]}</td>'
            f'<td>{r["services_per_batch"]}</td>'
            f'<td>{r["sow_inventory"]:.0f}</td>'
            f'<td>{r["weaned_per_batch"]:.0f}</td>{cells}'
            f'<td><b>{r["total_rooms"]}</b></td>'
            f'<td>{r["min_slack"]:.0f}일</td></tr>')

    # 스테이지 표
    st_rows = ""
    for r in rt:
        warn = ' class="warn-row"' if r["shortage"] > 0 else ""
        st_rows += (
            f'<tr{warn}><td><b>{E(r["name_ko"])}</b></td>'
            f'<td>{E(HOUSE_KO.get(r["house"], r["house"]))}</td>'
            f'<td>{r["duration"]}일</td><td>{r["downtime"]}일</td>'
            f'<td>{r["occupancy_days"]}일</td>'
            f'<td><b>{r["rooms_required"]}</b></td>'
            f'<td>{r["house_have"]}</td>'
            f'<td>{"<b>" + str(r["shortage"]) + "</b>" if r["shortage"] else "–"}</td>'
            f'<td>{r["slack_days"]:.0f}일</td>'
            f'<td>{r["head_per_room"]}두</td>'
            f'<td>{r["area_per_room_m2"]:.0f}㎡</td></tr>')

    # 생산비 지렛대 — 왜 발정만 봐서는 안 되는가
    lv = fe.levers(n_sows=int(round(p["sow_inventory"])))
    lv_rows = ""
    for r in lv.itertuples(index=False):
        own = "시세" not in r.경로
        lv_rows += (
            f'<tr><td><b>{E(r.lever)}</b></td>'
            f'<td>{r.연간효과:,}원</td><td>{r.두당효과:,}원</td>'
            f'<td>{E(r.경로)}</td>'
            f'<td>{"✅ 앱이 다룸" if own else "⬜ 통제 불가"}</td></tr>')

    ov = k["room_utilization"]
    occ_now = sim.steady_occupancy()[-1] if sim.steady_occupancy() else {}

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>돈군흐름 관제</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#eeeeea;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--accent:#2a78d6}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:1000px;margin:0 auto}}h1{{font-size:1.55rem;letter-spacing:-.02em}}
.sub{{color:var(--ink2);font-size:.92rem;margin:5px 0 4px}}
h2{{font-size:1.02rem;margin:24px 0 4px}}.h2d{{font-size:.8rem;color:var(--muted);margin-bottom:12px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:16px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:13px 15px}}
.kpi .v{{font-size:1.65rem;font-weight:700;letter-spacing:-.02em}}.kpi .l{{font-size:.8rem;font-weight:600;margin-top:1px}}.kpi .d{{font-size:.7rem;color:var(--muted);margin-top:3px}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:13px;padding:17px 18px;margin-bottom:14px;overflow-x:auto}}
.warn{{border-left:4px solid #d03b3b;background:color-mix(in srgb,#d03b3b 6%,var(--surface))}}
.good{{border-left:4px solid #3d9960;background:color-mix(in srgb,#3d9960 6%,var(--surface))}}
.flow{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:.84rem}}
.fx{{background:var(--surface2);border-radius:9px;padding:9px 13px;text-align:center;min-width:96px}}
.fx b{{display:block;font-size:1.2rem;letter-spacing:-.02em}}
.fx span{{font-size:.68rem;color:var(--muted)}}
.fa{{color:var(--muted);font-size:.78rem;white-space:nowrap}}
table{{width:100%;border-collapse:collapse;font-size:.83rem;margin-top:4px}}
td,th{{text-align:left;padding:7px 9px;border-bottom:1px solid var(--surface2);vertical-align:top;white-space:nowrap}}
th{{color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.03em}}
tr.cur{{background:color-mix(in srgb,var(--accent) 9%,transparent)}}
tr.warn-row td{{background:color-mix(in srgb,#d03b3b 8%,transparent)}}
.tag{{font-size:.65rem;font-weight:700;color:var(--accent);background:color-mix(in srgb,var(--accent) 15%,transparent);padding:1px 6px;border-radius:999px}}
.tag.err{{color:#d03b3b;background:color-mix(in srgb,#d03b3b 15%,transparent)}}
.bnrow{{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--surface2);font-size:.85rem}}
.bnrow:last-child{{border-bottom:0}}.cnt{{margin-left:auto;color:var(--muted);font-size:.76rem;white-space:nowrap}}
.ok{{color:#3d9960;font-weight:600;font-size:.88rem}}
.note{{font-size:.73rem;color:var(--muted);margin-top:10px;line-height:1.6}}
.bl{{font-size:11.5px;fill:var(--ink2)}}.bl.hi{{fill:var(--ink);font-weight:700}}
.bv{{font-size:11px;font-weight:600;fill:var(--ink)}}
.tk{{font-size:10px;font-weight:600;fill:var(--muted)}}
.gb{{font-size:9.5px;font-weight:700;fill:#fff;opacity:.9}}
.back{{display:inline-block;margin-bottom:14px;font-size:.8rem;color:var(--accent);text-decoration:none}}
</style></head><body><div class="wrap">
<a class="back" href="index.html">← 통합 대시보드</a>
<h1>🔄 돈군흐름 관제</h1>
<div class="sub">번식 관리는 “이 모돈을 언제 교배하나”이고, 돈군흐름은 <b>“그 배치가 나갈 자리가 있나”</b>다.
둘은 같은 문제의 앞뒤다 — 발정을 놓쳐 배치가 흩어지면 올인올아웃이 깨지고, 비육사가 모자라면 앞 단계가 밀린다.</div>
<div class="kpis">{kpi_html}</div>

<h2>1. 설계는 분만틀에서 역산한다</h2>
<div class="h2d">모돈 두수나 PSY 를 설계 기준으로 삼으면 안 된다 — 계절을 탄다.
<b>분만틀 수만이 고정된 물리량</b>이고 나머지는 거기서 나온다(CEVA / John Carr 모델).</div>
<div class="card"><div class="flow">
  <div class="fx"><b>{cfg.crate_count}</b><span>분만틀</span></div>
  <div class="fa">÷ 분만율 {cfg.breeding.farrowing_rate:.0%} →</div>
  <div class="fx"><b>{p["services_per_batch"]}</b><span>배치당 교배</span></div>
  <div class="fa">그중 후보돈 {p["gilts_per_batch"]}두 →</div>
  <div class="fx"><b>{p["sow_inventory"]:.0f}</b><span>번식돈군(두)</span></div>
  <div class="fa">× 복당 {cfg.breeding.weaned_per_litter:.0f}두 →</div>
  <div class="fx"><b>{p["weaned_per_batch"]:.0f}</b><span>배치당 이유</span></div>
  <div class="fa">× 육성률 {cfg.breeding.post_wean_survival:.0%} →</div>
  <div class="fx"><b>{p["shipped_per_batch"]:.0f}</b><span>배치당 출하</span></div>
</div>
<div class="note"><b>분만율은 평균이 아니라 하위 분위수를 넣는다.</b> 평균으로 잡으면
절반의 배치에서 분만틀이 빈다. 여기서는 {cfg.breeding.farrowing_rate:.0%} 를 썼고,
이 값이 1%p 떨어질 때마다 배치당 교배가 늘어 모돈 규모가 커진다 —
<b>발정 탐지가 분만율을 지키는 일</b>인 이유가 여기 있다.<br>
번식주기 {p["cycle_days"]}일(이유~재교배 {cfg.breeding.wean_to_service_days} +
임신 {cfg.breeding.gestation_days} + 포유 {cfg.breeding.lactation_days}) ·
출하일령 {p["market_age_days"]}일.</div></div>

<h2>2. 필요 vs 보유 돈방 — 부족분이 곧 병목</h2>
<div class="h2d">필요 돈방 = (사육일 + 사전점유일 + <b>공백기</b>) ÷ 배치 간격.
공백기를 빼고 세면 방이 모자라 올인올아웃이 무너지고, 그러면 배칭을 하는 의미 자체가 사라진다.</div>
{f'''<div class="card warn"><b>총량은 맞는데 배분이 틀렸다.</b>
필요 {sum(r["rooms_required"] for r in rt)}방 · 보유 {len(rooms)}방으로 수는 같지만,
{E(short_names)}이 모자라고 {E(surp_names)}이 남는다. 돈방은 돈사를 건너뛰어 쓸 수 없으므로
<b>총 방 수를 세는 것으로는 이 문제가 보이지 않는다</b> — 스테이지별로 갈라야 나온다.
</div>''' if deficit and surplus else ""}
<div class="card">{need_have_bars(rt)}</div>
<div class="card"><table><thead><tr><th>스테이지</th><th>돈사</th><th>사육일</th>
<th>공백기</th><th>점유일</th><th>필요방</th><th>보유방</th><th>부족</th>
<th>설계여유</th><th>방당두수</th><th>방면적</th></tr></thead>
<tbody>{st_rows}</tbody></table>
<div class="note"><b>보유방은 돈사 단위</b>다. 자돈사처럼 두 스테이지가 한 돈사를 나눠 쓰면
방을 스테이지에 미리 못 박지 않으므로 두 행의 보유·부족이 같게 나온다.<br>
<b>설계여유</b> = 필요방 × 간격 − 점유일. 0 이면 세척이 정확히 제 날에 끝나야만 성립한다는 뜻이라,
방 수만 보고 “충분하다”고 읽으면 안 된다.</div></div>

<h2>3. 돈방 점유 간트 — AIAO 가 지켜지는가</h2>
<div class="h2d">표보다 그림이 빠르다. <b>블록 사이에 빗금(세척)이 반드시 끼어야 한다.</b>
블록이 맞붙어 있으면 세척 없이 다음 배치가 들어간 것이다. 블록에 마우스를 올리면 배치·두수·기간이 나온다.</div>
<div class="card">{gantt_svg(sim, houses)}
<div class="note">warm-up {sim.warmup_days}일(파이프라인이 차기 전 구간) 이후 126일.
정상 상태 가동률 <b>{ov:.1%}</b> — 현재 재실 {occ_now.get("occupied", 0)} ·
세척 {occ_now.get("washing", 0)} · 빈방 {occ_now.get("empty", 0)} (총 {len(sim.rooms)}방).</div></div>

<h2>4. 시뮬레이션 — {SIM_DAYS}일을 하루씩</h2>
<div class="h2d">전이 규칙(일령 도달 AND 빈 돈방 → 배치 통째 이동, 전출 후 세척, 역류 금지)으로 돌린다.
빈 방이 2일 연속 없으면 병목으로 기록한다.</div>
<div class="card {"warn" if bn else "good"}">{bn_html}
<div class="note">{"비육사가 한 방 모자라면 앞 단계가 밀린다. 육성돈이 못 나가면 이유자돈이 갈 곳이 없고, 결국 분만사까지 거슬러 올라간다 — 병목은 그 지점 하나의 문제가 아니다." if bn else ""}
같은 설계를 <b>소요량대로 지어</b> 돌리면 경고 <b>{clean_n}건</b>이다 —
이 도구가 아무 데서나 경보를 내는 게 아니라는 확인이다.</div></div>

<h2>5. what-if — 같은 분만틀로 무엇이 달라지나</h2>
<div class="h2d">배치 간격을 바꾸면 필요 돈방과 모돈 규모가 함께 움직인다.
간격이 길수록 시설은 덜 들지만 <b>한 배치가 어긋났을 때의 손실이 커진다</b>.</div>
<div class="card"><table><thead><tr><th>시스템</th><th>간격</th><th>배치수</th>
<th>배치당 교배</th><th>모돈규모</th><th>배치당 이유</th>{wf_head}
<th>총 돈방</th><th>최소여유</th></tr></thead>
<tbody>{wf_rows}</tbody></table>
<div class="note">배치당 교배·이유 두수가 어느 시스템에서나 같은 것은 <b>분만틀 수만의 함수</b>이기 때문이다.
바뀌는 것은 <b>얼마나 자주</b> 그 일이 돌아오는가이고, 그래서 모돈 규모와 돈방 수가 달라진다.<br>
소규모 농장이 5주 배치를 택하는 이유가 이 표에 있다 — 총 돈방
{min(r["total_rooms"] for r in wf)}개면 되고 작업이 한 주에 몰린다.
대신 배치 하나가 깨지면 5주치가 날아간다.</div></div>

<h2>6. KPI — 어디에 대고 재는가</h2>
<div class="h2d">PSY 만 보면 안 된다. 국내는 이유까지는 준수한데 <b>이유 후에 흘린다</b> —
PSY 대비 MSY 격차가 그 손실이다.</div>
<div class="card">{bench_bars(k["psy"], k["msy"])}
<div class="note">이 설계의 PSY {k["psy"]} → MSY {k["msy"]} (이유후 생존
{k["post_wean_survival"]:.1%}, 이유 {k["weaned_total"]:,}두 → 출하 {k["shipped_total"]:,}두,
출하 배치 {k["batches_shipped"]}개 · <b>동일 코호트</b>).<br>
<b>이 값들은 설계 상한이다.</b> 시뮬레이터는 모든 배치가 분만틀을 채운다고 보므로,
재발정·유산 손실은 분만율 {cfg.breeding.farrowing_rate:.0%} 로만 들어간다.
이론 회전율 {k["sow_turnover"]} vs 설정 {k["sow_turnover_config"]} 의 차이가
현장에서 실제로 새는 몫이고, 그 대부분이 <b>비생산일수</b>다.</div></div>

<h2>7. 왜 발정 탐지와 한 앱인가</h2>
<div class="h2d">두 기능을 억지로 붙인 게 아니다. <b>배치는 이유 직후 7일 안에 교배해야 만들어진다</b> —
그 창을 놓친 모돈은 다음 배치로 밀리고, 배치가 흩어지면 이 페이지의 계산이 전부 무너진다.</div>
<div class="card"><div class="flow">
  <div class="fx"><b>이유</b><span>D0</span></div>
  <div class="fa">→ 3~7일 내 발정</div>
  <div class="fx"><b>발정 탐지</b><span>CCTV·활동량</span></div>
  <div class="fa">→ 적기 교배</div>
  <div class="fx"><b>분만율</b><span>{cfg.breeding.farrowing_rate:.0%} 유지</span></div>
  <div class="fa">→ 분만틀 충진</div>
  <div class="fx"><b>배치 유지</b><span>AIAO 성립</span></div>
</div>
<div class="note">놓친 모돈 1두는 단순히 21일 늦는 게 아니라 <b>배치 크기를 줄인다</b>.
배치가 분만틀을 못 채우면 그 방은 비고, 뒤 단계 돈방도 덜 차서 가동률이 떨어진다.
반대로 밀린 모돈이 다음 배치에 얹히면 그 배치가 넘쳐 과밀이 된다.</div></div>

<h2>8. 그래도 번식만 봐서는 안 된다 — 지렛대 순서</h2>
<div class="h2d">모든 개선을 <b>같은 단위(원/년)</b> 로 환산해 세워야 투자 우선순위를 정할 수 있다.
모돈 {int(round(p["sow_inventory"]))}두 기준.</div>
<div class="card"><table><thead><tr><th>지렛대</th><th>연간효과</th>
<th>모돈 두당</th><th>경로</th><th>이 앱</th></tr></thead>
<tbody>{lv_rows}</tbody></table>
<div class="note">사료가 생산비의 <b>{fe.cost_per_pig()["feed_share"]:.0%}</b> 라
FCR 0.1 개선이 PSY +1두보다 크다. 발정 탐지만 붙들고 있으면 더 큰 것을 놓친다는 뜻이고,
이 앱이 발정 관리에서 <b>전체 관리</b>로 넘어간 근거가 이 표다.<br>
손익분기 지육단가 <b>{fe.breakeven_price(k["psy"], k["post_wean_survival"]):,}원/kg</b>
(가정 시세 {fe.PORK_PRICE:,}원) — 시세가 이 아래면 성적이 좋아도 적자다.</div></div>

<div class="note">※ 설정: <code>competition/pigflow/example_farm.yaml</code>
(분만틀 {cfg.crate_count} · {p["batch_system"]} · 비육사를 <b>일부러 한 방 부족하게</b> 잡아
병목 탐지를 보인다). 농장 YAML 을 바꾸면 이 페이지 전체가 그 농장 값으로 다시 계산된다.<br>
※ <b>배치 1개 = 돈방 1개</b>로 모델링한다. 실제로는 한 배치를 여러 펜에 나누는 농장이 많으므로,
여기서 “돈방”은 물리적 펜이 아니라 <b>한 배치를 통째로 받는 단위 공간</b>으로 읽어야 한다.<br>
※ 사육일수·폐사율·단가는 국내 관행 초기값이다. 농장 전산기록으로 바꾸지 않으면 그 농장의 계산이 아니다.
결론으로 삼을 것은 절대 금액이 아니라 <b>지렛대의 순서</b>다.<br>
※ 재현: <code>python -m pigflow --config competition/pigflow/example_farm.yaml</code> ·
검산 테스트 <code>python competition/pigflow/tests/test_pigflow.py</code></div>
</div></body></html>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"돈군흐름 관제 생성: {OUT} ({os.path.getsize(OUT) // 1024}KB)")
    print(f"  분만틀 {cfg.crate_count} · 돈방 {len(rooms)} · "
          f"병목 {len(bn)}곳 · 이동 {len(sim.events)}건 · "
          f"PSY {k['psy']} / MSY {k['msy']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
