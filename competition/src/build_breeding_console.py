"""번식 관리 콘솔 — 캘린더·현황판·임신진단·관리표를 한 화면에.

CLI 로만 돌던 번식 모듈들(repro_calendar, herd_board, pregnancy_check,
breeding_ledger, breeding_timing)을 웹 뷰로 묶는다. 순서는 현장이 묻는 순서다:

  1) 오늘 무엇을 하는가        조치 큐(긴급도순) + 날짜별 작업량
  2) 이 개체는 어떤 상태인가    발정·임신 통합 관리표
  3) 몇 주 뒤에 무엇이 비는가   17주 분만 파이프라인
  4) 군의 구성은 건강한가       산차 구성 + 도태·전입
  5) 재발돈을 언제 잡는가       임신진단 3단계 캐스케이드
  6) 교배 시각을 언제로 잡는가   적기 곡선 + 관측 주기의 영향

외부 연결·라이브러리 없이 SVG 로 그린다.

    python competition/src/build_breeding_console.py
출력: competition/dashboard/breeding_console.html
"""
from __future__ import annotations

import html as _html
import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import breeding_ledger as bl  # noqa: E402
import breeding_timing as bt  # noqa: E402
import herd_board as hb  # noqa: E402
import pregnancy_check as pc  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "breeding_console.html")

STAGE_COLOR = {"후보": "#8b8b83", "공태": "#e8a33d", "교배": "#d03b3b",
               "임신": "#2a78d6", "포유": "#1baf7a"}
E = _html.escape


def _dday(d) -> str:
    if d is None or d != d:
        return "-"
    return "오늘" if int(d) == 0 else f"D-{int(d)}"


# ------------------------------------------------------------------ SVG 유틸
def bar_chart(items, width=860, bar_h=26, gap=8, fmt="{:.0f}",
              target=None, target_label="목표") -> str:
    """가로 막대. items = [(라벨, 값, 색)]."""
    if not items:
        return '<div class="empty">데이터 없음</div>'
    lbl_w, val_w = 96, 66
    mx = max([v for _l, v, _c in items] + ([target] if target else [0])) or 1
    plot = width - lbl_w - val_w - 12
    h = len(items) * (bar_h + gap) + 6
    p = []
    if target:
        tx = lbl_w + plot * target / mx
        p.append(f'<line x1="{tx:.1f}" y1="0" x2="{tx:.1f}" y2="{h - 6}" '
                 f'stroke="var(--muted)" stroke-dasharray="4 3" stroke-width="1.2"/>'
                 f'<text x="{tx + 4:.1f}" y="10" class="tk">{target_label} '
                 f'{fmt.format(target)}</text>')
    for i, (lab, val, col) in enumerate(items):
        y = i * (bar_h + gap) + 6
        w = max(1.5, plot * val / mx)
        p.append(
            f'<text x="{lbl_w - 8}" y="{y + bar_h / 2 + 4}" class="bl" '
            f'text-anchor="end">{E(str(lab))}</text>'
            f'<rect x="{lbl_w}" y="{y}" width="{w:.1f}" height="{bar_h}" rx="4" '
            f'fill="{col}" fill-opacity=".85"/>'
            f'<text x="{lbl_w + w + 7:.1f}" y="{y + bar_h / 2 + 4}" class="bv">'
            f'{fmt.format(val)}</text>')
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" role="img">'
            f'{"".join(p)}</svg>')


def pipeline_chart(wb: pd.DataFrame, width=860) -> str:
    """17주 분만 파이프라인 — 목표선 대비 주별 분만 두수."""
    h, pad_l, pad_b, pad_t = 190, 34, 30, 10
    n = len(wb)
    mx = max(wb["farrow"].max(), wb["target"].max()) * 1.25 or 1
    bw = (width - pad_l - 10) / n
    plot_h = h - pad_b - pad_t
    p = []
    ty = pad_t + plot_h * (1 - wb["target"].iloc[0] / mx)
    p.append(f'<line x1="{pad_l}" y1="{ty:.1f}" x2="{width - 10}" y2="{ty:.1f}" '
             f'stroke="#d03b3b" stroke-dasharray="5 3" stroke-width="1.4"/>'
             f'<text x="{width - 12}" y="{ty - 5:.1f}" class="tk" '
             f'text-anchor="end" fill="#d03b3b">목표 '
             f'{wb["target"].iloc[0]:.1f}복/주</text>')
    for i, r in enumerate(wb.to_dict("records")):
        x = pad_l + i * bw
        bh = plot_h * r["farrow"] / mx
        y = pad_t + plot_h - bh
        short = r["shortfall"] > r["target"] * 0.3
        col = ("#d03b3b" if (short and r["locked"]) else
               "#e8a33d" if short else "#2a78d6")
        p.append(f'<g><title>W{r["week"]} {r["start"]:%m/%d}~{r["end"]:%m/%d} · '
                 f'분만 {r["farrow"]}복 (목표 {r["target"]:.1f})'
                 f'{" · 확정 미달" if short and r["locked"] else ""}</title>'
                 f'<rect x="{x + 2:.1f}" y="{y:.1f}" width="{bw - 4:.1f}" '
                 f'height="{bh:.1f}" rx="3" fill="{col}" fill-opacity=".85"/></g>')
        if i % 2 == 0:
            p.append(f'<text x="{x + bw / 2:.1f}" y="{h - 14}" class="ax" '
                     f'text-anchor="middle">W{r["week"]}</text>')
    p.append(f'<line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{width - 10}" '
             f'y2="{pad_t + plot_h}" stroke="var(--border)"/>')
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" role="img" '
            f'aria-label="17주 분만 파이프라인">{"".join(p)}</svg>')


def efficacy_chart(width=860) -> str:
    """교배 적기 유효도 곡선 + 지침 구간."""
    h, pad_l, pad_b, pad_t = 200, 40, 30, 12
    ov = bt.ovulation_time("sow", bt.NORMAL_WEI)
    xs = [i for i in range(0, 49)]
    ys = [bt.ai_efficacy(x, "sow", bt.NORMAL_WEI) for x in xs]
    mx = max(ys) or 1
    plot_w, plot_h = width - pad_l - 14, h - pad_b - pad_t

    def px(x):
        return pad_l + plot_w * x / 48.0

    def py(y):
        return pad_t + plot_h * (1 - y / (mx * 1.15))

    lo, hi = bt.FIELD_OPTIMAL_WINDOW
    p = [f'<rect x="{px(lo):.1f}" y="{pad_t}" width="{px(hi) - px(lo):.1f}" '
         f'height="{plot_h}" fill="#1baf7a" fill-opacity=".10"/>'
         f'<text x="{(px(lo) + px(hi)) / 2:.1f}" y="{pad_t + 14}" class="tk" '
         f'text-anchor="middle" fill="#1baf7a">지침 적기 {lo:.0f}~{hi:.0f}h</text>',
         f'<line x1="{px(ov):.1f}" y1="{pad_t}" x2="{px(ov):.1f}" '
         f'y2="{pad_t + plot_h}" stroke="#8b3fd0" stroke-dasharray="4 3"/>'
         f'<text x="{px(ov) + 5:.1f}" y="{pad_t + plot_h - 6:.1f}" class="tk" '
         f'fill="#8b3fd0">배란 {ov:.0f}h</text>']
    pts = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in zip(xs, ys))
    p.append(f'<polyline points="{pts}" fill="none" stroke="var(--accent)" '
             f'stroke-width="2.4"/>')
    w = bt.insemination_window("sow", bt.NORMAL_WEI)
    for t, lab in ((w["ai1_h"], "1차"), (w["ai2_h"], "2차")):
        p.append(f'<circle cx="{px(t):.1f}" cy="{py(bt.ai_efficacy(t, "sow", bt.NORMAL_WEI)):.1f}" '
                 f'r="5" fill="#d03b3b"/>'
                 f'<text x="{px(t):.1f}" y="{py(bt.ai_efficacy(t, "sow", bt.NORMAL_WEI)) - 11:.1f}" '
                 f'class="tk" text-anchor="middle" fill="#d03b3b">{lab} {t:.0f}h</text>')
    for x in range(0, 49, 12):
        p.append(f'<text x="{px(x):.1f}" y="{h - 12}" class="ax" '
                 f'text-anchor="middle">{x}h</text>')
    p.append(f'<line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{width - 14}" '
             f'y2="{pad_t + plot_h}" stroke="var(--border)"/>')
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" role="img" '
            f'aria-label="교배 적기 유효도 곡선">{"".join(p)}</svg>')


def main() -> int:
    today = sys.argv[1] if len(sys.argv) > 1 else "2026-08-10"
    farm, herd, scheds, scores = bl.build_demo(today)
    led = bl.ledger(farm, herd, scheds, scores, today=today)
    wb = hb.weekly_board(herd, today=today)
    pp = hb.parity_profile(herd)
    cc = hb.cull_candidates(herd)
    gi = hb.gilt_intake_plan(herd, today=today)
    st = hb.service_target(herd, today=today)
    up = bl.upcoming(scheds, today=today, days=14, farm=farm)
    wl = bl.workload(scheds, today=today, days=14)
    sc = hb.stage_counts(herd)

    # 1) 조치 큐
    q = led.head(14)
    q_rows = "".join(
        f'<tr><td>{E(str(r["id"]))}</td><td>{E(r["loc"])}</td>'
        f'<td><span class="pill" style="background:color-mix(in srgb,'
        f'{STAGE_COLOR.get(r["stage"], "#888")} 18%,transparent);'
        f'color:{STAGE_COLOR.get(r["stage"], "#888")}">{E(str(r["stage"]))}</span></td>'
        f'<td>{E(str(r["estrus"]))}</td><td>{E(str(r["pregnancy"]))}</td>'
        f'<td>{E(str(r["next_task"]))}</td><td>{_dday(r["d_day"])}</td>'
        f'<td>{E(str(r["action"]))}</td>'
        f'<td>{(str(int(r["overdue_days"])) + "일") if r["overdue_days"] else ""}</td>'
        f'</tr>' for r in q.to_dict("records"))

    # 날짜별 작업량
    task_cols = [c for c in wl.columns if c not in ("date", "합계")]
    wl_items = [(f'{r["date"]:%m/%d}', int(r["합계"]),
                 "#d03b3b" if r["합계"] >= wl["합계"].quantile(0.8) else "#2a78d6")
                for r in wl.to_dict("records")]
    wl_svg = bar_chart(wl_items, fmt="{:.0f}")

    # 단계 구성 — 2단 레이아웃 안이라 좁은 viewBox 를 쓴다.
    # 860 폭 그대로 두면 약 490px 칸에 축소돼 라벨이 읽히지 않는다.
    stage_svg = bar_chart([(k, v, STAGE_COLOR.get(k, "#888")) for k, v in sc.items()],
                          width=420, bar_h=22, gap=7)

    # 산차 구성
    par_items = [(f'{r["parity"]}산', r["n"],
                  "#d03b3b" if r["gap"] > 3 else
                  "#e8a33d" if r["gap"] < -3 else "#2a78d6")
                 for r in pp.to_dict("records")]
    par_rows = "".join(
        f'<tr><td>{E(str(r["parity"]))}</td><td>{r["n"]}</td>'
        f'<td>{r["share"]:.1%}</td><td>{r["target_share"]:.0%}</td>'
        f'<td style="color:{"#d03b3b" if r["gap"] > 3 else ("#e8a33d" if r["gap"] < -3 else "var(--ink2)")}">'
        f'{r["gap"]:+.1f}</td></tr>' for r in pp.to_dict("records"))

    # 임신진단 캐스케이드
    casc_rows = ""
    for label, sens in (("육안 점검", pc.DEFAULT_SENSITIVITY),
                        ("CCTV 발정탐지", pc.CCTV_SENSITIVITY)):
        rows = pc.detection_cascade(sens)
        cells = "".join(f'<td>{r["caught"] * 100:.1f}두</td>' for r in rows[:3])
        casc_rows += (f'<tr><td><b>{E(label)}</b></td><td>{sens["3주"]:.0%}</td>'
                      f'{cells}<td>{rows[-1]["missed_forward"] * 100:.1f}두</td>'
                      f'<td><b>{pc.npd_from_returns(sens):.1f}일</b></td></tr>')
    val_rows = ""
    for label, b, a in (
            ("초음파 철저 (5주 95%)", {"3주": .70, "5주": .95, "8~10주": .90},
             {"3주": .92, "5주": .95, "8~10주": .90}),
            ("초음파 부실 (5주 50%)", {"3주": .70, "5주": .50, "8~10주": .90},
             {"3주": .92, "5주": .50, "8~10주": .90}),
            ("초음파 없음 (5주 0%)", {"3주": .70, "5주": .0, "8~10주": .90},
             {"3주": .92, "5주": .0, "8~10주": .90})):
        v = pc.value_of_early(st["n_sows"], base_sens=b, improved_sens=a)
        val_rows += (f'<tr><td>{E(label)}</td>'
                     f'<td>{v["npd_per_return_before"]:.1f}일</td>'
                     f'<td>{v["npd_per_return_after"]:.1f}일</td>'
                     f'<td>{v["npd_days_saved_year"]:,.0f}일</td>'
                     f'<td><b>{v["won_saved_year"]:,}원</b></td></tr>')

    # 관측 주기
    det_rows = "".join(
        f'<tr><td>{E(lab)}</td><td>발견+{d["offsets"][0]:.0f}/{d["offsets"][1]:.0f}h</td>'
        f'<td>{d["conception"]:.3f}</td>'
        f'<td style="color:{"#1baf7a" if d["loss_pp"] == 0 else "#d03b3b"}">'
        f'{-d["loss_pp"]:+.1f}pp</td></tr>'
        for lab, d in ((l, bt.detection_value(iv, "sow", bt.NORMAL_WEI))
                       for l, iv in (("연속 (CCTV)", 0), ("6시간", 6),
                                     ("하루 2회", 12), ("하루 1회", 24))))

    # 도태·전입
    cull_rows = "".join(
        f'<tr><td>{E(str(r["id"]))}</td><td>{r["parity"]}산</td>'
        f'<td>{E(str(r["stage"]))}</td><td>{r["score"]}</td>'
        f'<td>{E(r["reason"])}</td></tr>' for r in cc.head(8).to_dict("records"))
    ga = gi.attrs
    intake_rows = "".join(
        f'<tr><td>{E(r["month"])}</td><td>{r["need"]}두</td>'
        f'<td>{r["backlog_left"]}두</td><td>{E(r["usable_from"])}</td></tr>'
        for r in gi.to_dict("records"))

    # 향후 일정
    up_rows = "".join(
        f'<tr><td>D+{r["d_day"]}</td><td>{r["date"]:%m/%d}</td>'
        f'<td>{E(str(r["id"]))}</td><td>{E(r["loc"])}</td>'
        f'<td>{E(r["task"])}</td><td>{E(r["detail"][:44])}</td></tr>'
        for r in up.head(16).to_dict("records"))

    lost = wb[(wb["locked"]) & (wb["shortfall"] > 0)]["shortfall"].sum()
    kpis = [
        (f'{st["n_sows"]}두', "모돈 규모", f'회전율 {st["turnover"]}회/년'),
        (f'{st["service_target_week"]:.0f}두', "주간 교배 목표",
         f'최근 실적 {st["service_actual_week"]}두 '
         f'({st["achievement"]:.0%})'),
        (f'{lost:.0f}복', "확정 분만 미달", "임신 115일 — 지금 교배해도 못 메움"),
        (f'{len(cc)}두', "도태 후보", f'적체 해소 {ga["months_to_clear"]}개월'),
    ]
    kpi_html = "".join(
        f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div>'
        f'<div class="d">{d}</div></div>' for v, l, d in kpis)

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>번식 관리 콘솔</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#eeeeea;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--accent:#2a78d6}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:1000px;margin:0 auto}}h1{{font-size:1.55rem;letter-spacing:-.02em}}
.sub{{color:var(--ink2);font-size:.92rem;margin:5px 0 4px}}
h2{{font-size:1.02rem;margin:24px 0 4px}}.h2d{{font-size:.8rem;color:var(--muted);margin-bottom:12px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:16px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:13px 15px}}
.kpi .v{{font-size:1.7rem;font-weight:700;letter-spacing:-.02em}}.kpi .l{{font-size:.8rem;font-weight:600;margin-top:1px}}.kpi .d{{font-size:.7rem;color:var(--muted);margin-top:3px}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:13px;padding:17px 18px;margin-bottom:14px;overflow-x:auto}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
@media(max-width:760px){{.two{{grid-template-columns:1fr}}}}
table{{width:100%;border-collapse:collapse;font-size:.83rem;margin-top:4px}}
td,th{{text-align:left;padding:7px 9px;border-bottom:1px solid var(--surface2);vertical-align:top;white-space:nowrap}}
th{{color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.03em}}
.pill{{font-size:.72rem;font-weight:700;padding:2px 8px;border-radius:999px;white-space:nowrap}}
.note{{font-size:.73rem;color:var(--muted);margin-top:10px;line-height:1.6}}
.bl{{font-size:11px;fill:var(--ink2)}}.bv{{font-size:11px;font-weight:600;fill:var(--ink)}}
.ax{{font-size:10px;fill:var(--muted)}}.tk{{font-size:10px;font-weight:600;fill:var(--muted)}}
.empty{{color:var(--muted);font-size:.8rem;padding:8px}}
</style></head><body><div class="wrap">
<h1>📋 번식 관리 콘솔</h1>
<div class="sub">캘린더 · 현황판 · 임신진단 · 관리표를 한 화면에. 현장이 묻는 순서대로 배치했다 — <b>오늘 할 일 → 개체 상태 → 몇 주 뒤 → 군 구성 → 왜</b>.</div>
<div class="kpis">{kpi_html}</div>

<h2>1. 오늘의 조치 큐</h2>
<div class="h2d">긴급도순. 교배·분만·발정관찰은 놓치면 그날로 기회가 사라지므로(다음 발정까지 21일) 임박한 시한작업을 위로 올린다.</div>
<div class="card"><table><thead><tr><th>개체</th><th>위치</th><th>단계</th><th>발정</th><th>임신</th><th>다음 작업</th><th>D-day</th><th>조치</th><th>경과</th></tr></thead>
<tbody>{q_rows}</tbody></table></div>

<h2>2. 날짜별 작업량 (향후 14일)</h2>
<div class="h2d">번식 작업은 이유 그룹 단위로 움직여 특정 날짜에 몰린다. 그날 사람이 모자라면 교배를 놓치고, 놓친 교배는 21일 뒤에나 다시 온다.</div>
<div class="card">{wl_svg}</div>

<h2>3. 향후 관리 일정</h2>
<div class="h2d">개체별 예정 작업. 기준일 하나만 입력하면 이 목록이 전부 자동 생성된다.</div>
<div class="card"><table><thead><tr><th>D-day</th><th>날짜</th><th>개체</th><th>위치</th><th>작업</th><th>내용</th></tr></thead>
<tbody>{up_rows}</tbody></table>
<div class="note">총 {len(up)}건</div></div>

<h2>4. 17주 분만 파이프라인</h2>
<div class="h2d">오늘 교배한 모돈이 분만하기까지가 17주다. 앞쪽 주차의 미달은 <b>이미 확정된 손실</b>이다 — 임신 115일은 단축할 수 없으므로 지금 교배해도 메울 수 없다. 빨강 = 확정 미달, 주황 = 아직 교배로 메울 수 있는 구간.</div>
<div class="card">{pipeline_chart(wb)}</div>

<div class="two">
<div><h2>5. 번식 단계 구성</h2>
<div class="h2d">현재 군의 단계 분포.</div>
<div class="card">{stage_svg}</div></div>
<div><h2>6. 산차 구성</h2>
<div class="h2d">3~5산이 성적 정점. 6산 이상 과다는 도태 신호.</div>
<div class="card"><table><thead><tr><th>산차</th><th>두수</th><th>비율</th><th>목표</th><th>편차</th></tr></thead>
<tbody>{par_rows}</tbody></table></div></div>
</div>

<h2>7. 도태 후보 · 후보돈 전입</h2>
<div class="h2d">도태 후보 {len(cc)}두 · 연간 갱신 여력 {ga["annual_capacity"]}두(월 상한 {ga["monthly_cap"]}두). 격리사·인력 제약이 있어 한 번에 다 뺄 수 없으므로 점수 상위부터 순차 교체한다.</div>
<div class="two">
<div class="card"><table><thead><tr><th>개체</th><th>산차</th><th>단계</th><th>점수</th><th>사유</th></tr></thead>
<tbody>{cull_rows}</tbody></table></div>
<div class="card"><table><thead><tr><th>전입월</th><th>필요</th><th>잔여 적체</th><th>교배 투입 가능</th></tr></thead>
<tbody>{intake_rows}</tbody></table></div>
</div>

<h2>8. 임신진단 3단계 — 재발돈 검출 캐스케이드</h2>
<div class="h2d">1차 관문은 초음파가 아니라 <b>발정체크</b>이고 재발돈의 80%가 거기서 드러난다. 장비가 아니라 관찰의 문제이며, 이 앱이 자동화하는 대상이 정확히 그 지점이다.</div>
<div class="card"><table><thead><tr><th>방식</th><th>3주 민감도</th><th>3주 검출</th><th>5주 검출</th><th>8~10주 검출</th><th>미검출</th><th>재발돈 1두당 공태</th></tr></thead>
<tbody>{casc_rows}</tbody></table></div>

<h2>9. 3주 검출률 개선의 가치 (모돈 {st["n_sows"]}두)</h2>
<div class="h2d">값어치는 <b>그 농장이 초음파를 제대로 하는가</b>에 달렸다. 초음파를 철저히 하면 5주에서 어차피 잡히고 차이는 14일뿐이라 개선 여지가 작다. 과장하지 않고 시나리오로 나눠 본다.</div>
<div class="card"><table><thead><tr><th>시나리오</th><th>개선 전</th><th>개선 후</th><th>연간 공태 절감</th><th>금액</th></tr></thead>
<tbody>{val_rows}</tbody></table></div>

<h2>10. 교배 적기 — 유효도 곡선</h2>
<div class="h2d">정자는 주입 직후엔 수정 능력이 없다(수정능획득 4~6h). 그래서 최적은 <b>배란 정각이 아니라 몇 시간 전</b>이다. 곡선은 정자 가용 구간과 난자 유효 구간의 겹침을 적분해 계산했고, 현장 지침의 적기 구간(초록)과 일치한다.</div>
<div class="card">{efficacy_chart()}</div>

<h2>11. 발정 확인 주기가 수태율에 미치는 영향</h2>
<div class="h2d">적기를 아무리 정확히 계산해도 <b>발정이 언제 시작됐는지 모르면</b> 쓸 수 없다. 각 주기는 그 주기에 최적화된 프로토콜을 쓴다고 보고 공정 비교했다. 하루 2회 점검의 최적값이 '발견 후 14/22h' 로 나오는데, 이는 현장 관행 12/24h 와 사실상 같다 — 관행은 하루 2회 점검을 전제로 최적이었던 것이다.</div>
<div class="card"><table><thead><tr><th>점검 주기</th><th>최적 프로토콜</th><th>기대 수태율</th><th>연속 대비</th></tr></thead>
<tbody>{det_rows}</tbody></table>
<div class="note">→ 개선의 본질은 더 좋은 시각표가 아니라 <b>관측 지연의 제거</b>다.</div></div>

<div class="note">※ 합성 데이터 시연이다. 실제로는 농장 번식기록(교배·분만·이유일)과 CCTV 발정 점수를 그대로 넣으면 같은 화면이 나온다.<br>
※ 수태율·민감도 개선폭은 가정값이다. 효과 크기는 농장 실증이 필요하며, 여기서는 '무엇이 무엇과 연결되는가'의 구조를 계산한다.</div>
</div></body></html>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"번식 관리 콘솔 생성: {OUT} ({os.path.getsize(OUT) // 1024}KB)")
    print(f"  개체 {len(led)}두 · 향후 14일 작업 {len(up)}건 · "
          f"확정 미달 {lost:.0f}복 · 도태 후보 {len(cc)}두")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
