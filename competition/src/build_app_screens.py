"""앱 사용 화면 — 실제로 농가가 보게 될 화면을 실데이터로 채워 보인다.

지표만 늘어놓으면 "그래서 현장에서 어떻게 쓰나"에 답이 안 된다. 이 뷰는 앞의
모듈들이 만든 값을 **그대로 화면에 얹어** 하루 동선을 보여준다. 화면의 숫자는
목업이 아니라 `breeding_ledger` · `repro_calendar` · `barn_environment` 가
계산한 값이다 — 화면을 위해 따로 지어낸 값이 하나도 없다.

여섯 화면:
  1) 오늘 할 일     긴급도 큐. 앱을 켜면 첫 화면
  2) 모돈카드       개체 상세 + 일정 타임라인(예상 `~` / 확정 구분)
  3) 교배기록 등록   **예정일이 이미 채워져 있다** — 농가는 확인만
  4) 발정 알림      CCTV 가 발정을 잡으면 적기 시각까지 계산해 밀어준다
  5) 축사 도면      동선. 어느 동을 먼저 도는가
  6) 임신돈 현황판   주차별 분만 예정과 목표 대비

경쟁 제품과의 차이가 드러나는 지점을 화면 안에 표시했다(파란 배지). 특히
③ 은 경쟁 제품도 내세우는 기능이지만, 우리는 **관측(CCTV)이 예상을 덮어쓴다**는
점이 다르다 — 예정일은 추정이고 실제 발정이 확인되면 교배 시각이 다시 잡힌다.

    python competition/src/build_app_screens.py
출력: competition/dashboard/app_screens.html  (외부 연결 불필요)
"""
from __future__ import annotations

import html as _html
import os
import sys
from datetime import datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import barn_environment as be  # noqa: E402
import breeding_ledger as bl  # noqa: E402
import breeding_timing as bt  # noqa: E402
import herd_board as hb  # noqa: E402
import repro_calendar as rc  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "app_screens.html")
E = _html.escape
TODAY = "2026-08-10"

STAGE_C = {"후보": "#8b8b83", "공태": "#e8a33d", "교배": "#d03b3b",
           "임신": "#2a78d6", "포유": "#1baf7a"}
TASK_C = {"교배": "#d03b3b", "발정 관찰": "#e8a33d", "분만": "#8b3fd0",
          "임신감정": "#2a78d6", "재발정 확인": "#d98cc4",
          "분만사 이동": "#2a78d6", "이유": "#1baf7a"}


def _dd(d) -> str:
    if d is None or d != d:
        return "-"
    return "오늘" if int(d) == 0 else f"D-{int(d)}"


def phone(title: str, body: str, note: str = "", badge: str = "") -> str:
    """휴대폰 프레임 하나."""
    b = f'<div class="badge">{E(badge)}</div>' if badge else ""
    n = f'<div class="pnote">{note}</div>' if note else ""
    return (f'<div class="pwrap"><div class="phone">'
            f'<div class="bar"><span>9:41</span><span>▮▮▮ ᯤ</span></div>'
            f'<div class="hdr"><span class="back">‹</span>{E(title)}</div>'
            f'<div class="body">{body}</div></div>{b}{n}</div>')


def screen_today(led) -> str:
    rows = ""
    for r in led.head(6).to_dict("records"):
        col = TASK_C.get(r["next_task"], "#888")
        late = (f'<span class="late">{int(r["overdue_days"])}일 경과</span>'
                if r["overdue_days"] else "")
        rows += (
            f'<div class="task" style="border-left-color:{col}">'
            f'<div class="tl"><b>{E(str(r["id"]))}</b>'
            f'<span class="dd" style="color:{col}">{_dd(r["d_day"])}</span></div>'
            f'<div class="t2">{E(r["loc"])}</div>'
            f'<div class="t3" style="color:{col}">{E(str(r["next_task"]))}'
            f' · {E(str(r["action"]))}</div>{late}</div>')
    # 조치 대상 수는 도면 뷰와 **같은 정의**를 써야 한다. urgency>0 으로 세면
    # 전 개체가 잡혀(68) 도면의 23 과 어긋난다 — 화면마다 숫자가 다르면
    # "지어낸 값이 없다"는 이 뷰의 전제가 무너진다.
    from build_barn_map import cell_status
    pairs = [cell_status(r) for r in led.to_dict("records")]
    n_act = sum(1 for s, late in pairs if s not in ("정상", "공실") or late)
    return (f'<div class="sum"><div><b>{n_act}</b><span>조치 대상</span></div>'
            f'<div><b>{int((led["overdue_days"] > 0).sum())}</b><span>지연</span></div>'
            f'<div><b>{int(led["conflict"].notna().sum())}</b><span>경보</span></div>'
            f'</div>{rows}')


def screen_card(led, sched, pid: str) -> str:
    r = led[led["id"] == pid].iloc[0]
    sc = STAGE_C.get(r["stage"], "#888")
    head = (
        f'<div class="card2" style="background:{sc}">'
        f'<div class="cno">{E(pid)}</div>'
        f'<div class="cgrid">'
        f'<div><span>현재상태</span><b>{E(str(r["stage"]))}</b></div>'
        f'<div><span>산차</span><b>{int(r["parity"])}산</b></div>'
        f'<div><span>발정</span><b>{E(str(r["estrus"]))}</b></div>'
        f'<div><span>위치</span><b>{E(r["loc"])}</b></div>'
        f'</div></div>')
    t0 = rc._d(TODAY)
    items = ""
    for t in sched[pid]:
        dd = (t["date"] - t0).days
        if dd < -30 or dd > 130:
            continue
        col = TASK_C.get(t["task"], "#888")
        mark = "~" if t["estimated"] else "●"
        cls = "est" if t["estimated"] else "conf"
        items += (f'<div class="tli {cls}">'
                  f'<span class="dot" style="color:{col}">{mark}</span>'
                  f'<span class="dt">{t["date"]:%m/%d}</span>'
                  f'<span class="tk2">{E(t["task"])}</span>'
                  f'<span class="dd2">{_dd(dd) if dd >= 0 else f"{-dd}일 전"}</span>'
                  f'</div>')
    return (head + '<div class="sect">번식 일정</div>' + items
            + '<div class="legend2">● 확정 &nbsp; ~ 예상(관측되면 갱신)</div>')


def pick_service_case(herd, scores):
    """교배기록 화면에 쓸 개체 — 이유일이 있고 교배가 아직 남은 공태돈."""
    t0 = rc._d(TODAY)
    cand = herd[(herd["stage"] == "공태") & herd["weaning_date"].notna()]
    for r in cand.sort_values("weaning_date", ascending=False).itertuples(index=False):
        wean = r.weaning_date
        est = rc.schedule_from_weaning(wean)
        ai = [t for t in est if t["task"] == "교배"]
        if ai and ai[0]["date"] >= t0:
            return str(r.id), wean, scores.get(r.id, 0.0)
    r = cand.iloc[0]
    return str(r["id"]), r["weaning_date"], scores.get(r["id"], 0.0)


def screen_service(pid: str, wean, score: float) -> str:
    """교배기록 등록 — 예정일이 이미 채워져 있다.

    날짜·시각을 화면에 박아 넣으면 다른 화면의 같은 개체와 어긋난다(실제로
    모돈카드는 08/10, 이 화면은 08-16 이라 모순이었다). 전부 실제 일정에서 뽑는다.
    """
    t0 = rc._d(TODAY)
    est = rc.schedule_from_weaning(wean)
    est_ai = [t for t in est if t["task"] == "교배"][0]
    # CCTV 가 예상보다 하루 이르게 발정을 확인한 경우
    est_heat = [t for t in est if t["task"] == "발정 관찰"][-1]["date"]
    conf_dt = datetime.combine(est_heat - timedelta(days=1),
                               datetime.min.time()) + timedelta(hours=6)
    conf = rc.schedule_from_weaning(wean, estrus_confirmed=conf_dt)
    ai = [t for t in conf if t["task"] == "교배"]
    win = bt.insemination_window("sow", max(0.0, (conf_dt.date() - wean).days))
    ai_dts = [datetime.combine(t["date"], datetime.min.time()) for t in ai]
    hours = (win["ai1_h"], win["ai2_h"])
    base = conf_dt
    times = [base + timedelta(hours=float(h)) for h in hours]
    return (
        f'<div class="frow"><span>모돈번호</span>'
        f'<div class="fval fixed">{E(pid)}</div></div>'
        f'<div class="frow"><span>이유일 <i>입력</i></span>'
        f'<div class="fval fixed">{wean:%Y-%m-%d}</div></div>'
        f'<div class="frow"><span>예정일 <i>자동</i></span>'
        f'<div class="fval auto">{est_ai["date"]:%Y-%m-%d} '
        f'<em>(이유 +{(est_ai["date"] - wean).days}일)</em></div></div>'
        f'<div class="frow"><span>발정 확인 <i>CCTV</i></span>'
        f'<div class="fval auto">{conf_dt:%m-%d %H:%M} '
        f'<em>승가허용 점수 {score:.2f}</em></div></div>'
        f'<div class="frow"><span>1차 교배 <i>적기 자동</i></span>'
        f'<div class="fval hi">{times[0]:%m-%d} <b>{times[0]:%H}시</b> '
        f'<em>발정 후 {hours[0]:.0f}h</em></div></div>'
        f'<div class="frow"><span>2차 교배 <i>적기 자동</i></span>'
        f'<div class="fval hi">{times[1]:%m-%d} <b>{times[1]:%H}시</b> '
        f'<em>발정 후 {hours[1]:.0f}h</em></div></div>'
        f'<div class="frow"><span>교배자</span><div class="fval sel">선택 ▾</div></div>'
        f'<div class="frow"><span>웅돈</span><div class="fval sel">선택 ▾</div></div>'
        f'<div class="hintbox">농가가 채우는 칸은 <b>교배자·웅돈 둘뿐</b>이다.'
        f' 날짜·시각은 이유일 하나에서 전부 계산됐고, CCTV 가 발정을 확인하면'
        f' 그 시각 기준으로 다시 잡힌다.</div>'
        f'<div class="btn">저장</div>')


def screen_alert(pid: str, loc: str, score: float, t1, t2,
                 conflict_html: str = "", heat_html: str = "") -> str:
    return (
        f'<div class="push">'
        f'<div class="pt">🐖 발정 확인 · {E(pid)}</div>'
        f'<div class="pb">{E(loc)} · 승가허용 점수 <b>{score:.2f}</b><br>'
        f'적기 교배 <b>{t1:%m-%d %H시} / {t2:%H시}</b></div>'
        f'<div class="pw">지금 확인</div></div>'
        f'{conflict_html}{heat_html}'
        f'<div class="push feed">'
        f'<div class="pt">🍽️ 급이 소외 · 군사 돈방</div>'
        f'<div class="pb">섭취량 하위 개체 분리 급이 검토<br>'
        f'<em>feeding_monitor — 별도 영상 입력 필요</em></div></div>'
        f'<div class="hintbox">알림은 <b>무엇을 들고 가야 하는지</b>까지 말한다.'
        f' 발정만 알리고 끝내면 결국 사람이 다시 판단해야 한다.</div>')


def screen_map(farm, led, env) -> str:
    from build_barn_map import cell_status, STATUS
    by = {r["id"]: r for r in led.to_dict("records")}
    envm = {r["barn"]: r for r in env.to_dict("records")}
    out = ""
    for b, meta in farm.barns.items():
        e = envm.get(b, {})
        cells = ""
        for (bb, p), _pen in farm.pens.items():
            if bb != b:
                continue
            occ = {k[2]: a for k, a in farm.slots.items()
                   if k[0] == b and k[1] == p}
            for s in sorted(occ, key=lambda x: (len(x), x)):
                st, late = cell_status(by.get(occ[s], {}))
                col = STATUS[st][0]
                bd = ";border:2px solid #a02020" if late else ""
                cells += f'<i style="background:{col}{bd}"></i>'
        thi = (f'<span class="thi" style="color:{e.get("color", "#888")}">'
               f'THI {e.get("thi", "-")}</span>') if e else ""
        out += (f'<div class="mbarn"><div class="mh">{E(b)} '
                f'{E(meta["stage"])}{thi}</div>'
                f'<div class="mcells">{cells}</div></div>')
    leg = "".join(f'<span><i style="background:{c}"></i>{E(t.split(" (")[0])}</span>'
                  for _k, (c, t) in STATUS.items() if _k not in ("공실",))
    return out + f'<div class="mleg">{leg}</div>'


def screen_board(wb, st) -> str:
    mx = max(max(wb["farrow"]), wb["target"].iloc[0]) or 1
    bars = ""
    for r in wb.head(10).to_dict("records"):
        h = 62 * r["farrow"] / mx
        short = r["shortfall"] > r["target"] * 0.3
        col = ("#d03b3b" if (short and r["locked"]) else
               "#e8a33d" if short else "#2a78d6")
        bars += (f'<div class="wk"><div class="wb" style="height:{h:.0f}px;'
                 f'background:{col}"></div><span>{r["farrow"]}</span>'
                 f'<em>W{r["week"]}</em></div>')
    tl = 62 * st["farrow_target_week"] / mx
    return (f'<div class="sum"><div><b>{st["n_sows"]}</b><span>모돈</span></div>'
            f'<div><b>{st["turnover"]}</b><span>회전/년</span></div>'
            f'<div><b>{st["service_target_week"]:.0f}</b><span>주 교배목표</span></div>'
            f'</div>'
            f'<div class="sect">주차별 분만 예정</div>'
            f'<div class="chart"><div class="tline" style="bottom:{tl + 20:.0f}px">'
            f'<span>목표 {st["farrow_target_week"]:.1f}</span></div>{bars}</div>'
            f'<div class="hintbox">앞쪽 주차의 빨강은 <b>이미 확정된 손실</b>이다.'
            f' 임신 115일은 단축할 수 없어 지금 교배해도 메울 수 없다.</div>')


def main() -> int:
    farm, herd, scheds, scores = bl.build_demo(TODAY)
    led = bl.ledger(farm, herd, scheds, scores, today=TODAY)
    env = be.assess(be.demo_readings(hot_summer=True))
    wb = hb.weekly_board(herd, today=TODAY)
    st = hb.service_target(herd, today=TODAY)
    pid = str(led.iloc[0]["id"])

    # 알림 화면도 실제 결과에서 뽑는다 — 없으면 "해당 없음"으로 정직하게 둔다.
    svc_id, svc_wean, svc_score = pick_service_case(herd, scores)
    svc_loc = farm.label(svc_id)
    _est = rc.schedule_from_weaning(svc_wean)
    _heat = [t for t in _est if t["task"] == "발정 관찰"][-1]["date"]
    _conf = datetime.combine(_heat - timedelta(days=1),
                             datetime.min.time()) + timedelta(hours=6)
    _w = bt.insemination_window("sow", max(0.0, (_conf.date() - svc_wean).days))
    ai_t1 = _conf + timedelta(hours=float(_w["ai1_h"]))
    ai_t2 = _conf + timedelta(hours=float(_w["ai2_h"]))

    cf = bl.conflicts(led)
    if len(cf):
        c0 = cf.iloc[0]
        conflict_html = (
            f'<div class="push warn"><div class="pt">⚠️ 모순 경보 · '
            f'{E(str(c0["id"]))}</div><div class="pb">{E(str(c0["stage"]))} 중인데 '
            f'발정 신호({c0["estrus_score"]:.2f})<br>유산·오진·개체 오인 확인 필요'
            f'</div></div>')
    else:
        conflict_html = ('<div class="push warn"><div class="pt">⚠️ 모순 경보</div>'
                         '<div class="pb">해당 없음</div></div>')
    risk = be.at_risk_services(herd, env, farm)
    hot = env[env["heat_stress"]].sort_values("thi", ascending=False)
    if len(hot):
        h0 = hot.iloc[0]
        n_r = int((risk["barn"] == h0["barn"]).sum()) if len(risk) else 0
        heat_html = (
            f'<div class="push heat"><div class="pt">🌡️ {E(h0["barn"])} '
            f'열스트레스 (THI {h0["thi"]})</div><div class="pb">착상기 모돈 '
            f'<b>{n_r}두</b> — 3주 재발 확인 필수<br>{E(h0["advice"])}</div></div>')
    else:
        heat_html = ""

    screens = [
        phone("오늘 할 일", screen_today(led),
              "앱을 켜면 첫 화면. 긴급도순이며 <b>시한작업</b>(교배·분만·발정관찰)이"
              " 단순 지연보다 위에 온다 — 놓치면 다음 발정까지 21일이다.",
              "① 조치 큐"),
        phone("모돈카드", screen_card(led, scheds, pid),
              "개체 하나의 전체 번식 일정. <b>예상(~)과 확정(●)을 구분</b>해 표시하므로"
              " 무엇이 추정인지 농가가 안다.", "② 개체 상세"),
        phone("교배기록 등록", screen_service(svc_id, svc_wean, svc_score),
              "경쟁 제품도 '작업예정일자 제공'을 내세운다. 차이는"
              " <b>CCTV 관측이 예상을 덮어쓴다</b>는 점 — 예정일은 추정이고,"
              " 실제 발정이 확인되면 교배 <b>시각</b>까지 다시 계산된다.",
              "③ 입력 간소화"),
        phone("알림", screen_alert(svc_id, svc_loc, svc_score, ai_t1, ai_t2,
                                   conflict_html, heat_html),
              "발정만 알리지 않는다. <b>모순 경보</b>(임신 중 발정 신호),"
              " <b>착상기 열스트레스</b>, <b>급이 소외</b>는 환경·번식기록·영상을"
              " 겹쳐야 나오는 알림이다.", "④ 능동 알림"),
        phone("축사 도면", screen_map(farm, led, env),
              "목록은 '누가 급한가'에 답하지만 '어디로 가야 하는가'에는 답하지 못한다."
              " 색은 <b>들고 갈 것</b>(정액·초음파·분만준비), 테두리는 기한 경과.",
              "⑤ 동선"),
        phone("임신돈 현황판", screen_board(wb, st),
              "개체가 아니라 <b>군의 흐름</b>. 17주 뒤 분만이 비면 지금 교배가"
              " 부족하다는 뜻이고, 그 빈칸은 나중에 메울 수 없다.", "⑥ 군 단위"),
    ]

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>앱 사용 화면</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#eeeeea;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--accent:#2a78d6;--scr:#fff;--scr2:#f4f4f1}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5;--scr:#1c1c1b;--scr2:#262624}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5;--scr:#1c1c1b;--scr2:#262624}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:1180px;margin:0 auto}}h1{{font-size:1.55rem;letter-spacing:-.02em}}
.sub{{color:var(--ink2);font-size:.92rem;margin:5px 0 18px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:26px 20px}}
.pwrap{{display:flex;flex-direction:column;align-items:center}}
.phone{{width:296px;background:var(--scr);border:1px solid var(--border);
 border-radius:26px;overflow:hidden;box-shadow:0 6px 22px rgba(0,0,0,.10)}}
.bar{{display:flex;justify-content:space-between;font-size:.62rem;color:var(--muted);
 padding:7px 15px 3px}}
.hdr{{display:flex;align-items:center;gap:8px;font-weight:700;font-size:.9rem;
 padding:6px 14px 10px;border-bottom:1px solid var(--border)}}
.back{{color:var(--muted);font-size:1.1rem}}
.body{{padding:11px 12px 15px;min-height:414px;background:var(--scr)}}
.badge{{margin-top:9px;font-size:.72rem;font-weight:700;color:var(--accent);
 background:color-mix(in srgb,var(--accent) 13%,transparent);padding:2px 10px;border-radius:999px}}
.pnote{{font-size:.74rem;color:var(--ink2);margin-top:7px;line-height:1.55;max-width:300px}}
.sum{{display:flex;gap:7px;margin-bottom:10px}}
.sum div{{flex:1;background:var(--scr2);border-radius:9px;padding:7px 4px;text-align:center}}
.sum b{{display:block;font-size:1.15rem}}.sum span{{font-size:.62rem;color:var(--muted)}}
.task{{border-left:3px solid;background:var(--scr2);border-radius:0 8px 8px 0;
 padding:7px 9px;margin-bottom:6px}}
.tl{{display:flex;justify-content:space-between;font-size:.82rem}}
.dd{{font-weight:700;font-size:.74rem}}
.t2{{font-size:.68rem;color:var(--muted)}}
.t3{{font-size:.72rem;font-weight:600;margin-top:2px}}
.late{{display:inline-block;font-size:.62rem;color:#a02020;background:rgba(160,32,32,.12);
 padding:1px 6px;border-radius:999px;margin-top:3px}}
.card2{{border-radius:11px;padding:11px 12px;color:#fff;margin-bottom:10px}}
.cno{{font-size:1.5rem;font-weight:800;letter-spacing:-.02em}}
.cgrid{{display:grid;grid-template-columns:1fr 1fr;gap:5px 8px;margin-top:7px}}
.cgrid span{{display:block;font-size:.6rem;opacity:.82}}
.cgrid b{{font-size:.78rem}}
.sect{{font-size:.68rem;font-weight:700;color:var(--muted);margin:9px 0 5px;
 text-transform:uppercase;letter-spacing:.04em}}
.tli{{display:flex;align-items:center;gap:7px;font-size:.73rem;padding:3.5px 0;
 border-bottom:1px solid var(--surface2)}}
.tli.est{{color:var(--ink2)}}.tli .dot{{width:10px;font-weight:700}}
.dt{{width:38px;font-variant-numeric:tabular-nums;color:var(--muted)}}
.tk2{{flex:1;font-weight:600}}.dd2{{font-size:.66rem;color:var(--muted)}}
.legend2{{font-size:.63rem;color:var(--muted);margin-top:7px}}
.frow{{display:flex;align-items:center;gap:8px;margin-bottom:7px}}
.frow>span{{width:82px;font-size:.68rem;color:var(--muted);flex-shrink:0}}
.frow i{{display:block;font-style:normal;font-size:.58rem;color:var(--accent);font-weight:700}}
.fval{{flex:1;background:var(--scr2);border-radius:7px;padding:6px 9px;font-size:.76rem}}
.fval.auto{{background:color-mix(in srgb,var(--accent) 11%,transparent);
 border:1px solid color-mix(in srgb,var(--accent) 34%,transparent)}}
.fval.hi{{background:color-mix(in srgb,#d03b3b 11%,transparent);
 border:1px solid color-mix(in srgb,#d03b3b 34%,transparent)}}
.fval.fixed{{font-weight:700}}.fval.sel{{color:var(--muted)}}
.fval em{{font-style:normal;font-size:.63rem;color:var(--muted)}}
.hintbox{{font-size:.66rem;color:var(--ink2);background:var(--scr2);border-radius:8px;
 padding:7px 9px;margin-top:9px;line-height:1.5}}
.btn{{margin-top:9px;background:var(--accent);color:#fff;text-align:center;
 padding:8px;border-radius:8px;font-weight:700;font-size:.8rem}}
.push{{background:var(--scr2);border-radius:11px;padding:9px 11px;margin-bottom:8px;
 border-left:3px solid #1baf7a}}
.push.warn{{border-left-color:#e0407f}}.push.heat{{border-left-color:#d03b3b}}
.push.feed{{border-left-color:#e8a33d}}
.pt{{font-size:.76rem;font-weight:700}}
.pb{{font-size:.68rem;color:var(--ink2);margin-top:2px}}
.pw{{display:inline-block;margin-top:6px;font-size:.66rem;font-weight:700;
 color:var(--accent)}}
.mbarn{{background:var(--scr2);border-radius:9px;padding:7px 9px;margin-bottom:7px}}
.mh{{font-size:.7rem;font-weight:700;margin-bottom:5px;display:flex;
 justify-content:space-between;align-items:baseline}}
.thi{{font-size:.62rem;font-weight:700}}
.mcells{{display:flex;flex-wrap:wrap;gap:3px}}
.mcells i{{width:15px;height:13px;border-radius:3px;display:block}}
.mleg{{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px;font-size:.6rem;color:var(--ink2)}}
.mleg span{{display:inline-flex;align-items:center;gap:3px}}
.mleg i{{width:9px;height:9px;border-radius:2px;display:inline-block}}
.chart{{position:relative;display:flex;align-items:flex-end;gap:4px;height:96px;
 padding:0 2px;border-bottom:1px solid var(--border)}}
.wk{{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end}}
.wb{{width:100%;border-radius:3px 3px 0 0;min-height:2px}}
.wk span{{font-size:.58rem;font-weight:700}}.wk em{{font-size:.53rem;color:var(--muted);
 font-style:normal}}
.tline{{position:absolute;left:0;right:0;border-top:1px dashed #d03b3b}}
.tline span{{position:absolute;right:0;top:-11px;font-size:.55rem;color:#d03b3b;
 font-weight:700}}
.note{{font-size:.73rem;color:var(--muted);margin-top:22px;line-height:1.6}}
</style></head><body><div class="wrap">
<h1>📱 앱 사용 화면</h1>
<div class="sub">화면의 숫자는 목업이 아니라 <b>앞의 모듈들이 계산한 값</b>이다 — 화면을 위해 지어낸 값이 하나도 없다. 하루 동선 순서로 배치했다.</div>
<div class="grid">{"".join(screens)}</div>
<div class="note">※ 합성 데이터 시연이다. 실제로는 농장 번식기록·축사 등록 정보·CCTV 발정 점수·환경 센서값을 그대로 넣으면 같은 화면이 나온다.<br>
※ 화면 구성은 기능 배치를 보이기 위한 것으로, 실제 앱의 시각 디자인은 별도다.</div>
</div></body></html>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"앱 사용 화면 생성: {OUT} ({os.path.getsize(OUT) // 1024}KB)")
    print(f"  화면 {len(screens)}종 · 개체 {len(led)}두 · 기준일 {TODAY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
