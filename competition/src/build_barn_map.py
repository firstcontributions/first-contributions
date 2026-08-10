"""농장 도면 기반 실시간 관제 — 축사 배치도 위에 관리대상돈을 띄운다.

목록은 "누가 급한가"에 답하지만 "어디로 가야 하는가"에는 답하지 못한다. 현장은
사람이 축사를 걸어 다니며 일한다. 그래서 같은 정보라도 **도면 위에 놓여야**
동선이 된다 — 1동 A열 3·7·11번을 한 번에 돌고 2동으로 넘어가는 식.

이 뷰가 겹치는 세 층:
  1) 사육현황  개체가 어느 자리에 있고 번식 단계가 무엇인지(farm_registry + herd_board)
  2) 환경      축사별 THI 열스트레스 등급(barn_environment)
  3) 업무      오늘 해야 할 일과 지연·경보(breeding_ledger)

자리 하나가 곧 개체 하나이므로 스톨은 격자로, 군사는 묶음으로 그린다. 색은
**조치 종류**를 뜻한다 — 예쁘게 칠하는 게 아니라 무엇을 들고 가야 하는지를
구분하려는 것이다(정액인지, 초음파인지, 분만 준비인지).

    python competition/src/build_barn_map.py
출력: competition/dashboard/barn_map.html  (외부 연결·라이브러리 불필요)
"""
from __future__ import annotations

import html as _html
import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import barn_environment as be  # noqa: E402
import breeding_ledger as bl  # noqa: E402
import farm_registry as fr  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "barn_map.html")

# 조치 종류별 색 — 들고 가야 할 것이 다르면 색도 다르다.
# '지연'은 여기 없다. 지연은 작업 종류가 아니라 **수식어**이므로 색을 따로 주면
# 두 가지가 망가진다: (1) 교배 빨강과 지연 빨강이 구분되지 않고, (2) 오늘 교배할
# 개체가 지난 관찰 때문에 '지연' 색으로 덮여 정작 해야 할 일이 가려진다.
# 그래서 지연은 **테두리**로 표시하고 색은 작업 종류를 유지한다.
STATUS = {
    "교배":      ("#d03b3b", "교배 (정액 준비)"),
    "발정확인":   ("#e8a33d", "발정 확인 (등누르기)"),
    "분만":      ("#8b3fd0", "분만 임박 (야간 순찰)"),
    "임신감정":   ("#2a78d6", "임신감정 (초음파)"),
    "재발확인":   ("#d98cc4", "재발정 확인 (웅돈 노출)"),
    "경보":      ("#e0407f", "모순 경보 (유산·오진 의심)"),
    "정상":      ("#7d9c86", "조치 없음"),
    "공실":      ("#c9c9c2", "빈 자리"),
}
OVERDUE_STROKE = "#a02020"
TASK_TO_STATUS = {"교배": "교배", "발정 관찰": "발정확인", "분만": "분만",
                  "임신감정": "임신감정", "재발정 확인": "재발확인",
                  "분만사 이동": "임신감정", "이유": "정상"}
# D-day 가 며칠 이내면 '조치 대상'으로 칠할지. 작업마다 준비 시간이 다르다 —
# 교배는 당일 판단이지만 분만은 자리·인력·야간 순찰을 미리 잡아야 한다.
ACT_WINDOW = 2
ACT_WINDOW_BY_TASK = {"분만": 7, "분만사 이동": 5}


def _dday(d) -> str:
    """D-day 표기. NaN·None 은 '-'."""
    if d is None or d != d:
        return "-"
    return "오늘" if int(d) == 0 else f"D-{int(d)}"


def _present(v) -> bool:
    """None·NaN 을 결측으로 본다.

    `if row["conflict"]:` 로 끝내면 안 된다 — pandas 를 거친 결측은 float NaN 이
    되어 올 수 있고 bool(nan) 은 True 다. 그대로 두면 전 개체가 경보로 칠해진다.
    """
    return v is not None and v == v


def cell_status(row) -> tuple:
    """관리표 한 행 → (색 구분, 기한경과 여부).

    임박한 시한작업이 지연보다 **앞선다**. 오늘 교배해야 할 개체를 어제 놓친
    관찰 때문에 '지연'으로 칠하면, 정작 오늘 들고 가야 할 정액이 화면에서
    사라진다. 지연은 테두리로 따로 표시하므로 정보가 없어지지도 않는다.
    """
    late = (row.get("overdue_days") or 0) > 0
    c = row.get("conflict")
    if _present(c) and str(c).strip():
        return "경보", late
    d, task = row.get("d_day"), row.get("next_task")
    if _present(d) and d <= ACT_WINDOW_BY_TASK.get(task, ACT_WINDOW):
        return TASK_TO_STATUS.get(task, "정상"), late
    return "정상", late


def build_layout(farm: fr.Farm, led: pd.DataFrame) -> dict:
    """축사동 → 돈방 → 자리 배치 + 각 자리의 상태."""
    by_id = {r["id"]: r for r in led.to_dict("records")}
    out = {}
    for b, meta in farm.barns.items():
        pens = []
        for (bb, p), pen in farm.pens.items():
            if bb != b:
                continue
            occupied = {k[2]: a for k, a in farm.slots.items()
                        if k[0] == b and k[1] == p}
            cells = []
            for s in sorted(occupied, key=fr._slot_key):
                aid = occupied[s]
                r = by_id.get(aid, {})
                st, late = cell_status(r)
                cells.append({"slot": s, "id": aid, "status": st, "late": late,
                              "overdue": r.get("overdue"),
                              "overdue_days": r.get("overdue_days", 0),
                              "stage": r.get("stage", "-"),
                              "task": r.get("next_task", "-"),
                              "d_day": r.get("d_day"),
                              "action": r.get("action", "-"),
                              "estrus": r.get("estrus", "-")})
            free = pen["capacity"] - len(cells)
            pens.append({"pen": p, "housing": pen["housing"],
                         "capacity": pen["capacity"], "cells": cells,
                         "free": free})
        out[b] = {"stage": meta["stage"], "pens": pens}
    return out


# ------------------------------------------------------------------ SVG 그리기
CW, CH, GAP = 40, 34, 5        # 자리 칸 크기·간격
PER_ROW = 12
PAD_X, PEN_LBL = 14, 96


def draw_barn(barn: str, info: dict, env_row, x0: int = 0) -> tuple:
    """축사 하나를 SVG 로. (svg문자열, 높이) 반환."""
    parts, y = [], 44
    for pen in info["pens"]:
        cells = pen["cells"]
        n_rows = max(1, -(-max(1, len(cells) + pen["free"]) // PER_ROW))
        parts.append(
            f'<text x="{PAD_X}" y="{y + 20}" class="pl">{_html.escape(pen["pen"])}</text>'
            f'<text x="{PAD_X}" y="{y + 34}" class="ps">'
            f'{fr.HOUSING[pen["housing"]][0]}</text>')
        cx0 = PAD_X + PEN_LBL
        idx = 0
        for c in cells:
            r, col = divmod(idx, PER_ROW)
            cx, cy = cx0 + col * (CW + GAP), y + r * (CH + GAP)
            color = STATUS[c["status"]][0]
            dd = _dday(c["d_day"])
            tip = (f'{c["id"]} · {pen["pen"]} {c["slot"]}번 · {c["stage"]} · '
                   f'{c["task"]} {dd} · 발정 {c["estrus"]}')
            if c["late"]:
                tip += f' · {c["overdue"]} {c["overdue_days"]}일 경과'
            edge = (f' stroke="{OVERDUE_STROKE}" stroke-width="2.5"'
                    if c["late"] else "")
            parts.append(
                f'<g class="cell"><title>{_html.escape(tip)}</title>'
                f'<rect x="{cx}" y="{cy}" width="{CW}" height="{CH}" rx="5" '
                f'fill="{color}" fill-opacity=".9"{edge}/>'
                f'<text x="{cx + CW / 2}" y="{cy + CH / 2 + 4}" class="cn">'
                f'{_html.escape(str(c["slot"]))}</text></g>')
            idx += 1
        for _ in range(pen["free"]):                 # 빈 자리
            r, col = divmod(idx, PER_ROW)
            cx, cy = cx0 + col * (CW + GAP), y + r * (CH + GAP)
            parts.append(
                f'<rect x="{cx}" y="{cy}" width="{CW}" height="{CH}" rx="5" '
                f'fill="none" stroke="{STATUS["공실"][0]}" '
                f'stroke-dasharray="3 3" stroke-width="1.2"/>')
            idx += 1
        y += n_rows * (CH + GAP) + 12

    h = y + 8
    env_txt = ""
    if env_row is not None:
        env_txt = (f'<text x="{PAD_X}" y="30" class="env" fill="{env_row["color"]}" '
                   f'text-anchor="end" transform="translate(880,0)">'
                   f'{env_row["temp_c"]}℃ · {env_row["rh_pct"]}% · '
                   f'THI {env_row["thi"]} ({env_row["level"]})</text>')
    head = (f'<rect x="1" y="1" width="898" height="{h - 2}" rx="12" '
            f'fill="var(--surface)" stroke="var(--border)"/>'
            f'<text x="{PAD_X}" y="28" class="bt">{_html.escape(barn)} '
            f'{_html.escape(info["stage"])}</text>{env_txt}')
    return f'<g transform="translate({x0},0)">{head}{"".join(parts)}</g>', h


def build_svg(layout: dict, env: pd.DataFrame) -> str:
    envm = {r["barn"]: r for r in env.to_dict("records")}
    parts, y = [], 0
    for barn, info in layout.items():
        g, h = draw_barn(barn, info, envm.get(barn))
        parts.append(f'<g transform="translate(0,{y})">{g}</g>')
        y += h + 14
    return (f'<svg viewBox="0 0 900 {y}" width="100%" '
            f'style="max-width:900px" role="img" '
            f'aria-label="농장 축사 배치도와 관리대상돈">{"".join(parts)}</svg>')


def legend_html() -> str:
    out = "".join(
        f'<span class="lg"><i style="background:{c}"></i>{_html.escape(t)}</span>'
        for _k, (c, t) in STATUS.items())
    out += (f'<span class="lg"><i style="background:transparent;'
            f'border:2.5px solid {OVERDUE_STROKE}"></i>테두리 = 기한 경과</span>')
    return out


def barn_tasks(led: pd.DataFrame) -> pd.DataFrame:
    """축사동별 업무 요약 — 어느 동을 먼저 돌아야 하는가."""
    d = led.copy()
    pairs = [cell_status(r) for r in d.to_dict("records")]
    d["status"] = [p[0] for p in pairs]
    d["late"] = [p[1] for p in pairs]
    act = d[(~d["status"].isin(("정상", "공실"))) | d["late"]]
    if not len(act):
        return pd.DataFrame()
    g = (act[~act["status"].isin(("정상", "공실"))]
         .groupby(["barn", "status"]).size().unstack(fill_value=0))
    g = g.reindex(sorted(set(d["barn"])), fill_value=0)
    for k in STATUS:
        if k not in ("정상", "공실") and k not in g.columns:
            g[k] = 0
    g["지연"] = act.groupby("barn")["late"].sum().reindex(g.index, fill_value=0)
    g["합계"] = act.groupby("barn").size().reindex(g.index, fill_value=0)
    return (g.reset_index().rename(columns={"index": "barn"})
             .sort_values("합계", ascending=False))


def main() -> int:
    today = sys.argv[1] if len(sys.argv) > 1 else "2026-08-10"
    farm, herd, scheds, scores = bl.build_demo(today)
    led = bl.ledger(farm, herd, scheds, scores, today=today)
    env = be.assess(be.demo_readings(hot_summer=True))
    layout = build_layout(farm, led)
    svg = build_svg(layout, env)

    # 축사별 업무 리스트
    bt = barn_tasks(led)
    cols = [k for k in STATUS if k not in ("정상", "공실")] + ["지연"]
    bt_rows = ""
    for r in bt.to_dict("records"):
        cells = "".join(f'<td>{int(r.get(k, 0)) or ""}</td>' for k in cols)
        bt_rows += (f'<tr><td><b>{_html.escape(str(r["barn"]))}</b></td>{cells}'
                    f'<td><b>{int(r["합계"])}</b></td></tr>')
    bt_head = "".join(f"<th>{k}</th>" for k in cols)

    # 환경 카드
    env_rows = "".join(
        f'<tr><td><b>{_html.escape(r["barn"])}</b></td><td>{r["temp_c"]}℃</td>'
        f'<td>{r["rh_pct"]}%</td><td><b>{r["thi"]}</b></td>'
        f'<td><span class="pill" style="background:color-mix(in srgb,{r["color"]} 20%,'
        f'transparent);color:{r["color"]}">{r["level"]}</span></td>'
        f'<td>{_html.escape(r["advice"])}</td>'
        f'<td>+{r["wei_penalty_d"]}일</td></tr>'
        for r in env.to_dict("records"))

    risk = be.at_risk_services(herd, env, farm)
    risk_rows = "".join(
        f'<tr><td>{_html.escape(str(r["id"]))}</td><td>{_html.escape(r["barn"])}</td>'
        f'<td>교배 후 {r["days_since_service"]}일</td>'
        f'<td>{_html.escape(r["level"])}</td>'
        f'<td>{_html.escape(r["risk"])}</td></tr>'
        for r in risk.head(12).to_dict("records")) or \
        '<tr><td colspan="5">해당 없음</td></tr>'

    # 조치 대기 개체 상위
    act = led[led["urgency"] > 0].head(14)
    act_rows = "".join(
        f'<tr><td>{_html.escape(str(r["id"]))}</td><td>{_html.escape(r["loc"])}</td>'
        f'<td>{_html.escape(str(r["stage"]))}</td>'
        f'<td>{_html.escape(str(r["next_task"]))}</td>'
        f'<td>{_dday(r["d_day"])}</td>'
        f'<td>{_html.escape(str(r["action"]))}</td></tr>'
        for r in act.to_dict("records"))

    pairs = [cell_status(r) for r in led.to_dict("records")]
    n_act = sum(1 for s, late in pairs if s not in ("정상", "공실") or late)
    hot_n = int(env["heat_stress"].sum())
    kpis = [(f"{len(led)}두", "등록 개체", f"{len(farm.barns)}개 동 · "
             f"{len(farm.pens)}개 돈방"),
            (f"{n_act}두", "오늘 조치 대상", "도면에서 색으로 표시"),
            (f"{hot_n}동", "열스트레스 축사", "THI 74 초과"),
            (f"{len(risk)}두", "착상기 위험군", "환경×번식기록 교차")]
    kpi_html = "".join(
        f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div>'
        f'<div class="d">{d}</div></div>' for v, l, d in kpis)

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>농장 도면 관제</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#eeeeea;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--accent:#2a78d6}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:1000px;margin:0 auto}}h1{{font-size:1.55rem;letter-spacing:-.02em}}
.sub{{color:var(--ink2);font-size:.92rem;margin:5px 0 4px}}
h2{{font-size:1.02rem;margin:22px 0 4px}}.h2d{{font-size:.8rem;color:var(--muted);margin-bottom:12px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:16px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:13px 15px}}
.kpi .v{{font-size:1.7rem;font-weight:700;letter-spacing:-.02em}}.kpi .l{{font-size:.8rem;font-weight:600;margin-top:1px}}.kpi .d{{font-size:.7rem;color:var(--muted);margin-top:3px}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:13px;padding:17px 18px;margin-bottom:14px;overflow-x:auto}}
.lg{{display:inline-flex;align-items:center;gap:5px;font-size:.76rem;color:var(--ink2);margin:0 12px 6px 0}}.lg i{{width:12px;height:12px;border-radius:3px;display:inline-block}}
table{{width:100%;border-collapse:collapse;font-size:.83rem;margin-top:4px}}
td,th{{text-align:left;padding:7px 9px;border-bottom:1px solid var(--surface2);vertical-align:top;white-space:nowrap}}
th{{color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.03em}}
.pill{{font-size:.72rem;font-weight:700;padding:2px 8px;border-radius:999px;white-space:nowrap}}
.note{{font-size:.73rem;color:var(--muted);margin-top:10px;line-height:1.6}}
.bt{{font-size:14px;font-weight:700;fill:var(--ink)}}
.pl{{font-size:12px;font-weight:600;fill:var(--ink2)}}
.ps{{font-size:10px;fill:var(--muted)}}
.cn{{font-size:11px;font-weight:600;fill:#fff;text-anchor:middle}}
.env{{font-size:11px;font-weight:600}}
.cell{{cursor:default}}.cell:hover rect{{fill-opacity:1;stroke:var(--ink);stroke-width:1.5}}
</style></head><body><div class="wrap">
<h1>🗺️ 농장 도면 관제</h1>
<div class="sub">축사 배치도 위에 <b>사육현황 · 환경 · 오늘의 업무</b>를 겹쳐 표시. 목록이 아니라 <b>동선</b>으로 본다.</div>
<div class="kpis">{kpi_html}</div>

<h2>1. 축사 배치도 — 관리대상돈</h2>
<div class="h2d">칸 하나가 자리 하나. 색은 <b>조치 종류</b>다(들고 갈 것이 다르면 색도 다르다). 칸에 마우스를 올리면 개체 상세가 나온다. 점선은 빈 자리.</div>
<div class="card">
<div style="margin-bottom:10px">{legend_html()}</div>
{svg}
</div>

<h2>2. 축사동별 업무 리스트</h2>
<div class="h2d">어느 동부터 돌아야 하는지. 합계가 큰 동을 먼저 간다.</div>
<div class="card"><table><thead><tr><th>축사동</th>{bt_head}<th>합계</th></tr></thead>
<tbody>{bt_rows}</tbody></table></div>

<h2>3. 환경 (ICT) — THI 열스트레스</h2>
<div class="h2d">온·습도를 숫자로만 띄우면 아무도 안 본다. THI 로 환산해 <b>번식에 미치는 영향</b>과 WEI 보정으로 연결한다.</div>
<div class="card"><table><thead><tr><th>축사동</th><th>온도</th><th>습도</th><th>THI</th><th>등급</th><th>조치</th><th>WEI 보정</th></tr></thead>
<tbody>{env_rows}</tbody></table></div>

<h2>4. 착상기 열스트레스 위험군</h2>
<div class="h2d">교배 후 7~21일이 착상기다. 이때 더위를 먹으면 수정은 됐어도 착상이 실패해 3주 재발로 돌아온다. <b>환경과 번식기록을 겹쳐야만</b> 보이는 위험이다.</div>
<div class="card"><table><thead><tr><th>개체</th><th>축사동</th><th>경과</th><th>등급</th><th>조치</th></tr></thead>
<tbody>{risk_rows}</tbody></table></div>

<h2>5. 조치 대기 개체</h2>
<div class="h2d">긴급도순. 도면의 색칠된 칸과 같은 목록이다.</div>
<div class="card"><table><thead><tr><th>개체</th><th>위치</th><th>단계</th><th>작업</th><th>D-day</th><th>조치</th></tr></thead>
<tbody>{act_rows}</tbody></table></div>

<div class="note">※ 합성 데이터 시연이다. 실제로는 농장의 축사 등록 정보와 번식기록, 환경 센서값을 그대로 넣으면 같은 화면이 나온다.<br>
※ THI 임계값은 문헌 기준이며 품종·순응도에 따라 다르다. WEI 보정폭은 가정값으로, 농장 데이터로 재추정해야 한다.</div>
</div></body></html>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    kb = os.path.getsize(OUT) // 1024
    print(f"농장 도면 관제 생성: {OUT} ({kb}KB)")
    print(f"  개체 {len(led)}두 · 조치 대상 {n_act}두 · 열스트레스 {hot_n}동 · "
          f"착상기 위험 {len(risk)}두")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
