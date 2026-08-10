"""동작하는 앱 프로토타입 — 눌러서 돌아다니는 단일 HTML.

`build_app_screens.py` 는 화면을 **정지 이미지처럼** 나란히 보여준다. 이 모듈은
같은 데이터를 **실제로 조작 가능한 앱**으로 만든다: 탭으로 화면을 옮기고, 목록에서
개체를 눌러 카드로 들어가고, 도면의 칸을 눌러 그 개체를 열고, 번호로 검색한다.

심사에서 "그래서 어떻게 쓰나"에 답하는 가장 빠른 방법은 눌러보게 하는 것이다.

구조:
  · 데이터는 파이썬이 계산해 JSON 으로 **HTML 안에 심는다**(외부 요청 없음)
  · 화면 전환·검색·드릴다운은 바닐라 JS. 라이브러리·CDN 을 쓰지 않는다
  · 라우팅은 해시(#/card/2022)라 뒤로가기가 동작하고 링크를 공유할 수 있다

화면: 홈(오늘 할 일) · 목록(검색) · 개체카드 · 도면 · 현황판 · 알림

    python competition/src/build_app_prototype.py
출력: competition/dashboard/app_prototype.html  (외부 연결 불필요)
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date, datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import barn_environment as be  # noqa: E402
import breeding_ledger as bl  # noqa: E402
import breeding_timing as bt  # noqa: E402
import farm_registry as fr  # noqa: E402
import herd_board as hb  # noqa: E402
import repro_calendar as rc  # noqa: E402
from build_barn_map import STATUS, cell_status  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "app_prototype.html")
TODAY = "2026-08-10"

STAGE_C = {"후보": "#8b8b83", "공태": "#e8a33d", "교배": "#d03b3b",
           "임신": "#2a78d6", "포유": "#1baf7a"}
TASK_C = {"교배": "#d03b3b", "발정 관찰": "#e8a33d", "분만": "#8b3fd0",
          "임신감정": "#2a78d6", "재발정 확인": "#d98cc4",
          "분만사 이동": "#2a78d6", "이유": "#1baf7a"}


def _iso(d):
    if isinstance(d, datetime):
        d = d.date()
    return d.isoformat() if isinstance(d, date) else None


def _num(v, default=None):
    """NaN·None 을 JSON 이 삼킬 수 있는 값으로. NaN 은 JS 에서 조용히 truthy 다."""
    if v is None or v != v:
        return default
    return v


def build_payload() -> dict:
    farm, herd, scheds, scores = bl.build_demo(TODAY)
    led = bl.ledger(farm, herd, scheds, scores, today=TODAY)
    env = be.assess(be.demo_readings(hot_summer=True))
    wb = hb.weekly_board(herd, today=TODAY)
    st = hb.service_target(herd, today=TODAY)
    risk = be.at_risk_services(herd, env, farm)
    pp = hb.parity_profile(herd)
    cc = hb.cull_candidates(herd)

    pairs = {r["id"]: cell_status(r) for r in led.to_dict("records")}
    animals = []
    for r in led.to_dict("records"):
        stt, late = pairs[r["id"]]
        animals.append({
            "id": str(r["id"]), "loc": r["loc"], "barn": r["barn"],
            "parity": int(_num(r["parity"], 0) or 0),
            "stage": r["stage"], "estrus": r["estrus"],
            "score": round(float(_num(r["estrus_score"], 0.0) or 0.0), 2),
            "preg": r["pregnancy"], "task": r["next_task"],
            "date": _iso(r["next_date"]), "dday": _num(r["d_day"]),
            "action": r["action"], "late": bool(late),
            "lateTask": r["overdue"] if late else None,
            "lateDays": int(_num(r["overdue_days"], 0) or 0),
            "conflict": r["conflict"] if bl.present(r["conflict"]) else None,
            "status": stt, "urgency": round(float(r["urgency"]), 1),
        })
    sched = {str(pid): [{"d": _iso(t["date"]), "t": t["task"],
                         "x": t["detail"], "e": bool(t["estimated"])}
                        for t in ts] for pid, ts in scheds.items()}

    barns = []
    for b, meta in farm.barns.items():
        pens = []
        for (bb, p), pen in farm.pens.items():
            if bb != b:
                continue
            occ = {k[2]: a for k, a in farm.slots.items()
                   if k[0] == b and k[1] == p}
            pens.append({"pen": p, "housing": fr.HOUSING[pen["housing"]][0],
                         "cap": pen["capacity"],
                         "slots": [{"s": s, "id": occ[s]}
                                   for s in sorted(occ, key=fr._slot_key)]})
        e = env[env["barn"] == b]
        er = e.iloc[0].to_dict() if len(e) else {}
        barns.append({"barn": b, "stage": meta["stage"], "pens": pens,
                      "thi": _num(er.get("thi")), "temp": _num(er.get("temp_c")),
                      "rh": _num(er.get("rh_pct")), "level": er.get("level"),
                      "color": er.get("color"), "advice": er.get("advice")})

    n_act = sum(1 for s, la in pairs.values() if s not in ("정상", "공실") or la)
    return {
        "today": TODAY, "animals": animals, "sched": sched, "barns": barns,
        "statusColors": {k: v[0] for k, v in STATUS.items()},
        "statusLabels": {k: v[1] for k, v in STATUS.items()},
        "stageColors": STAGE_C, "taskColors": TASK_C,
        "board": [{"w": int(r["week"]), "s": _iso(r["start"]),
                   "e": _iso(r["end"]), "f": int(r["farrow"]),
                   "wn": int(r["wean"]), "t": round(float(r["target"]), 1),
                   "locked": bool(r["locked"]),
                   "short": bool(r["shortfall"] > r["target"] * 0.3)}
                  for r in wb.to_dict("records")],
        "kpi": {"nSows": st["n_sows"], "turnover": st["turnover"],
                "svcTarget": st["service_target_week"],
                "svcActual": st["service_actual_week"],
                "farrowTarget": st["farrow_target_week"],
                "nAct": n_act,
                "nLate": int(sum(1 for a in animals if a["late"])),
                "nConf": int(sum(1 for a in animals if a["conflict"])),
                "nCull": int(len(cc)), "nRisk": int(len(risk))},
        "risk": [{"id": str(r["id"]), "barn": r["barn"],
                  "days": int(r["days_since_service"]), "level": r["level"]}
                 for r in risk.to_dict("records")],
        "parity": [{"p": str(r["parity"]), "n": int(r["n"]),
                    "share": round(float(r["share"]), 3),
                    "target": round(float(r["target_share"]), 3),
                    "gap": round(float(r["gap"]), 1)}
                   for r in pp.to_dict("records")],
        "cull": [{"id": str(r["id"]), "parity": int(r["parity"]),
                  "score": int(r["score"]), "reason": r["reason"]}
                 for r in cc.head(10).to_dict("records")],
        "ai": _ai_case(farm, herd, scores),
        "queue": [{"barn": g["barn"], "order": g["visit_order"],
                   "n": g["n"], "crit": g["n_critical"],
                   "late": g["n_overdue"], "conf": g["n_conflict"],
                   "supplies": g["supplies"],
                   "ids": [str(r["id"]) for r in g["rows"]]}
                  for g in bl.barn_queue(led)],
        "route": [b for b in farm.barns],
    }


def _ai_case(farm, herd, scores) -> dict:
    """교배기록 화면용 — 실제 개체의 실제 일정에서 뽑는다."""
    from build_app_screens import pick_service_case
    pid, wean, score = pick_service_case(herd, scores)
    est = rc.schedule_from_weaning(wean)
    est_ai = [t for t in est if t["task"] == "교배"][0]
    heat = [t for t in est if t["task"] == "발정 관찰"][-1]["date"]
    conf = datetime.combine(heat - timedelta(days=1),
                            datetime.min.time()) + timedelta(hours=6)
    w = bt.insemination_window("sow", max(0.0, (conf.date() - wean).days))
    t1 = conf + timedelta(hours=float(w["ai1_h"]))
    t2 = conf + timedelta(hours=float(w["ai2_h"]))
    return {"id": pid, "loc": farm.label(pid), "wean": _iso(wean),
            "planned": _iso(est_ai["date"]), "score": round(float(score), 2),
            "confirmed": conf.strftime("%Y-%m-%d %H:%M"),
            "ai1": t1.strftime("%m-%d %H시"), "ai2": t2.strftime("%m-%d %H시"),
            "h1": round(float(w["ai1_h"])), "h2": round(float(w["ai2_h"])),
            "ovul": round(float(w["ovulation_h"]))}


CSS = """
:root{color-scheme:light;--page:#ececea;--scr:#fff;--scr2:#f4f4f1;--ink:#0b0b0b;
--ink2:#52514e;--muted:#8d8b85;--border:rgba(11,11,11,.12);--accent:#2a78d6}
@media(prefers-color-scheme:dark){:root:where(:not([data-theme=light])){
--page:#0b0b0b;--scr:#1a1a19;--scr2:#242422;--ink:#fff;--ink2:#c3c2b7;
--muted:#8d8b85;--border:rgba(255,255,255,.14);--accent:#3987e5}}
:root[data-theme=dark]{--page:#0b0b0b;--scr:#1a1a19;--scr2:#242422;--ink:#fff;
--ink2:#c3c2b7;--muted:#8d8b85;--border:rgba(255,255,255,.14);--accent:#3987e5}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;
background:var(--page);color:var(--ink);line-height:1.5;
display:flex;flex-direction:column;align-items:center;padding:20px 12px 40px}
.intro{max-width:392px;width:100%;margin-bottom:14px}
.intro h1{font-size:1.2rem;letter-spacing:-.02em}
.intro p{font-size:.78rem;color:var(--ink2);margin-top:4px}
.app{width:392px;max-width:100%;height:730px;background:var(--scr);
border:1px solid var(--border);border-radius:26px;overflow:hidden;
display:flex;flex-direction:column;box-shadow:0 8px 30px rgba(0,0,0,.13)}
.bar{display:flex;justify-content:space-between;font-size:.64rem;
color:var(--muted);padding:8px 16px 3px;flex-shrink:0}
.hdr{display:flex;align-items:center;gap:9px;padding:5px 14px 10px;
border-bottom:1px solid var(--border);flex-shrink:0}
.hdr h2{font-size:1rem;flex:1}
.back{color:var(--accent);font-size:1.1rem;font-weight:700;cursor:pointer;
padding:2px 4px;display:none}
.back.on{display:block}
.view{flex:1;overflow-y:auto;padding:12px 13px 16px}
.tabs{display:flex;border-top:1px solid var(--border);flex-shrink:0;
background:var(--scr)}
.tab{flex:1;text-align:center;padding:8px 2px 10px;font-size:.6rem;
color:var(--muted);cursor:pointer}
.tab b{display:block;font-size:1.05rem;line-height:1.3;font-weight:400}
.tab.on{color:var(--accent);font-weight:700}
.sum{display:flex;gap:7px;margin-bottom:11px}
.sum>div{flex:1;background:var(--scr2);border-radius:10px;padding:8px 4px;
text-align:center}
.sum b{display:block;font-size:1.2rem}
.sum span{font-size:.62rem;color:var(--muted)}
.task{border-left:3px solid;background:var(--scr2);border-radius:0 9px 9px 0;
padding:8px 10px;margin-bottom:7px;cursor:pointer}
.task:active{opacity:.6}
.tl{display:flex;justify-content:space-between;align-items:baseline;font-size:.85rem}
.dd{font-weight:700;font-size:.74rem}
.t2{font-size:.68rem;color:var(--muted)}
.t3{font-size:.73rem;font-weight:600;margin-top:2px}
.late{display:inline-block;font-size:.62rem;color:#a02020;
background:rgba(160,32,32,.13);padding:1px 6px;border-radius:999px;margin-top:3px}
.srch{width:100%;padding:8px 11px;border-radius:9px;border:1px solid var(--border);
background:var(--scr2);color:var(--ink);font-size:.82rem;margin-bottom:9px}
.chips{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:9px}
.chip{font-size:.66rem;padding:3px 9px;border-radius:999px;cursor:pointer;
background:var(--scr2);color:var(--ink2);border:1px solid transparent}
.chip.on{background:var(--accent);color:#fff;font-weight:700}
.row{display:flex;align-items:center;gap:9px;padding:8px 4px;
border-bottom:1px solid var(--scr2);cursor:pointer;font-size:.8rem}
.row:active{opacity:.6}
.pin{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.rid{font-weight:700;width:46px}
.rloc{flex:1;font-size:.7rem;color:var(--muted);overflow:hidden;
text-overflow:ellipsis;white-space:nowrap}
.rtag{font-size:.65rem;font-weight:700;padding:1px 7px;border-radius:999px}
.card2{border-radius:12px;padding:12px 13px;color:#fff;margin-bottom:11px}
.cno{font-size:1.6rem;font-weight:800;letter-spacing:-.02em}
.cgrid{display:grid;grid-template-columns:1fr 1fr;gap:6px 9px;margin-top:8px}
.cgrid span{display:block;font-size:.6rem;opacity:.85}
.cgrid b{font-size:.8rem}
.sect{font-size:.66rem;font-weight:700;color:var(--muted);margin:11px 0 6px;
text-transform:uppercase;letter-spacing:.04em}
.tli{display:flex;align-items:center;gap:8px;font-size:.74rem;padding:4px 0;
border-bottom:1px solid var(--scr2)}
.tli.est{color:var(--ink2)}
.dot{width:11px;font-weight:700;flex-shrink:0}
.dt{width:40px;font-variant-numeric:tabular-nums;color:var(--muted)}
.tk2{flex:1;font-weight:600}
.dd2{font-size:.66rem;color:var(--muted)}
.hint{font-size:.67rem;color:var(--ink2);background:var(--scr2);border-radius:9px;
padding:8px 10px;margin-top:10px;line-height:1.55}
.warnbox{border-left:3px solid #e0407f;background:color-mix(in srgb,#e0407f 8%,var(--scr2))}
.mbarn{background:var(--scr2);border-radius:10px;padding:8px 10px;margin-bottom:8px}
.mh{font-size:.72rem;font-weight:700;margin-bottom:6px;display:flex;
justify-content:space-between;align-items:baseline}
.thi{font-size:.63rem;font-weight:700}
.mpen{font-size:.6rem;color:var(--muted);margin:4px 0 3px}
.mcells{display:flex;flex-wrap:wrap;gap:3px}
.mcells i{width:19px;height:16px;border-radius:3px;display:block;cursor:pointer;
font-style:normal;font-size:.52rem;color:#fff;text-align:center;line-height:16px}
.mcells i:active{outline:2px solid var(--ink)}
.mleg{display:flex;flex-wrap:wrap;gap:7px;margin-top:9px;font-size:.61rem;
color:var(--ink2)}
.mleg span{display:inline-flex;align-items:center;gap:3px}
.mleg i{width:9px;height:9px;border-radius:2px;display:inline-block}
.chart{position:relative;display:flex;align-items:flex-end;gap:3px;height:110px;
padding:0 2px;border-bottom:1px solid var(--border);margin-top:6px}
.wk{flex:1;display:flex;flex-direction:column;align-items:center;
justify-content:flex-end;cursor:default}
.wb{width:100%;border-radius:3px 3px 0 0;min-height:2px}
.wk span{font-size:.56rem;font-weight:700}
.wk em{font-size:.5rem;color:var(--muted);font-style:normal}
.tline{position:absolute;left:0;right:0;border-top:1px dashed #d03b3b}
.tline span{position:absolute;right:0;top:-11px;font-size:.55rem;color:#d03b3b;
font-weight:700}
.push{background:var(--scr2);border-radius:11px;padding:9px 11px;margin-bottom:8px;
border-left:3px solid #1baf7a;cursor:pointer}
.push.warn{border-left-color:#e0407f}
.push.heat{border-left-color:#d03b3b}
.push.feed{border-left-color:#e8a33d}
.pt{font-size:.78rem;font-weight:700}
.pb{font-size:.69rem;color:var(--ink2);margin-top:2px}
.frow{display:flex;align-items:center;gap:9px;margin-bottom:8px}
.frow>span{width:84px;font-size:.68rem;color:var(--muted);flex-shrink:0}
.frow i{display:block;font-style:normal;font-size:.58rem;color:var(--accent);
font-weight:700}
.fval{flex:1;background:var(--scr2);border-radius:8px;padding:7px 10px;font-size:.77rem}
.fval.auto{background:color-mix(in srgb,var(--accent) 12%,transparent);
border:1px solid color-mix(in srgb,var(--accent) 35%,transparent)}
.fval.hi{background:color-mix(in srgb,#d03b3b 12%,transparent);
border:1px solid color-mix(in srgb,#d03b3b 35%,transparent)}
.fval em{font-style:normal;font-size:.63rem;color:var(--muted)}
.btn{margin-top:10px;background:var(--accent);color:#fff;text-align:center;
padding:9px;border-radius:9px;font-weight:700;font-size:.82rem;cursor:pointer}
.bars{margin-top:4px}
.brow{display:flex;align-items:center;gap:7px;font-size:.7rem;margin-bottom:5px}
.brow>span:first-child{width:34px;color:var(--muted)}
.btrack{flex:1;height:13px;background:var(--scr2);border-radius:4px;overflow:hidden}
.bfill{height:100%;border-radius:4px}
.empty{color:var(--muted);font-size:.76rem;padding:16px 4px;text-align:center}
.bhead{margin:12px 0 7px;padding-bottom:5px;border-bottom:1px solid var(--border)}
.bhead:first-child{margin-top:0}
.bh1{display:flex;align-items:center;gap:7px;font-size:.88rem}
.bord{background:var(--accent);color:#fff;width:17px;height:17px;border-radius:50%;
font-size:.62rem;display:flex;align-items:center;justify-content:center;font-weight:700}
.bcnt{color:var(--muted);font-size:.7rem}
.bcrit{font-size:.62rem;font-weight:700;color:#d03b3b;
background:rgba(208,59,59,.13);padding:1px 7px;border-radius:999px}
.bsup{font-size:.65rem;color:var(--ink2);margin-top:2px}
.acts{display:flex;gap:6px;margin-top:6px}
.acts span{flex:1;text-align:center;font-size:.68rem;font-weight:700;padding:4px;
border-radius:6px;cursor:pointer}
.acts .ok{background:color-mix(in srgb,#1baf7a 16%,transparent);color:#1baf7a}
.acts .skip{background:var(--scr2);color:var(--muted)}
.acts span:active{opacity:.55}
.logrow{display:flex;align-items:baseline;gap:7px;font-size:.72rem;padding:6px 2px;
border-bottom:1px solid var(--scr2)}
.lg1{color:var(--muted);font-size:.65rem;width:64px;flex-shrink:0}
.lg2{flex:1}.lg2 em{font-style:normal;color:var(--muted);font-size:.65rem}
.lg3{font-size:.65rem;font-weight:700;padding:1px 7px;border-radius:999px}
.lg3.okc{background:color-mix(in srgb,#1baf7a 16%,transparent);color:#1baf7a}
.lg3.skc{background:var(--scr2);color:var(--muted)}
.lg4{font-size:.62rem;color:#a02020}
.btn.ghost{background:transparent;color:var(--muted);
border:1px solid var(--border)}
.foot{max-width:392px;width:100%;font-size:.7rem;color:var(--muted);
margin-top:14px;line-height:1.6}
"""

JS = r"""
const $=s=>document.querySelector(s);
const el=(t,c,h)=>{const e=document.createElement(t);if(c)e.className=c;
 if(h!==undefined)e.innerHTML=h;return e;};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,
 c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const byId=Object.fromEntries(D.animals.map(a=>[a.id,a]));
const T0=new Date(D.today+'T00:00:00');
const dday=d=>d==null?'-':(d===0?'오늘':'D-'+d);
const dnum=iso=>Math.round((new Date(iso+'T00:00:00')-T0)/864e5);
const md=iso=>iso?iso.slice(5).replace('-','/'):'';

let filter='all';
const LKEY='pig_worklog_v1';
function loadLog(){try{return JSON.parse(localStorage.getItem(LKEY)||'[]');}
 catch(e){return[];}}
function saveLog(x){try{localStorage.setItem(LKEY,JSON.stringify(x));}catch(e){}}
function addLog(a,result){
  const g=loadLog();
  g.push({ts:new Date().toISOString().slice(0,19),id:a.id,task:a.task,
    result:result,loc:a.loc,planned:a.date,operator:'현장'});
  saveLog(g);
}
function vLog(v){
  const g=loadLog().slice().reverse();
  const done=g.filter(x=>x.result==='완료').length;
  v.appendChild(el('div','sum',
    `<div><b>${g.length}</b><span>기록</span></div>
     <div><b>${done}</b><span>완료</span></div>
     <div><b>${g.length-done}</b><span>미실시</span></div>`));
  if(!g.length){
    v.appendChild(el('div','empty',
      '아직 기록이 없습니다.<br>홈에서 <b>완료</b>를 누르면 여기 쌓입니다.'));
  }
  g.forEach(x=>{
    const late=x.planned?Math.round(
      (new Date(x.ts.slice(0,10))-new Date(x.planned))/864e5):null;
    v.appendChild(el('div','logrow',
      `<span class="lg1">${esc(x.ts.slice(5,10))} ${esc(x.ts.slice(11,16))}</span>
       <span class="lg2"><b>${esc(x.id)}</b> ${esc(x.task)}
        <em>${esc(x.loc||'')}</em></span>
       <span class="lg3 ${x.result==='완료'?'okc':'skc'}">${esc(x.result)}</span>
       ${late!=null&&late>0?`<span class="lg4">+${late}일</span>`:''}`));
  });
  if(g.length){
    const b=el('div','btn ghost','기록 전체 지우기');
    b.onclick=()=>{if(confirm('작업 로그를 모두 지웁니다.')){saveLog([]);nav();}};
    v.appendChild(b);
  }
  v.appendChild(el('div','hint',
    '작업 로그는 <b>추가만</b> 합니다 — 기록을 고치면 성적이 왜곡되므로 정정은 '
    +'취소 기록을 덧붙이는 방식입니다. 이 프로토타입은 브라우저에 저장하므로 '
    +'새로고침해도 남습니다. 실제 앱은 서버에 같은 스키마로 쌓습니다.'));
}

function go(h){location.hash=h;}
function nav(){
  const p=(location.hash||'#/home').slice(2).split('/');
  const v=$('#view'); v.innerHTML=''; v.scrollTop=0;
  const back=$('#back'); back.classList.toggle('on',p[0]==='card');
  const titles={home:'오늘 할 일',list:'모돈 목록',card:'모돈카드',
   map:'축사 도면',board:'현황판',alert:'알림',ai:'교배기록 등록',
   log:'작업 로그'};
  $('#title').textContent=titles[p[0]]||'오늘 할 일';
  ({home:vHome,list:vList,card:vCard,map:vMap,board:vBoard,alert:vAlert,
    ai:vAi,log:vLog}[p[0]]||vHome)(v,p[1]);
  document.querySelectorAll('.tab').forEach(t=>
    t.classList.toggle('on',t.dataset.r===p[0]));
}

function taskCard(a){
  const c=D.taskColors[a.task]||'#888';
  const d=el('div','task',
    `<div class="tl"><b>${esc(a.id)}</b>
     <span class="dd" style="color:${c}">${dday(a.dday)}</span></div>
     <div class="t2">${esc(a.loc)}</div>
     <div class="t3" style="color:${c}">${esc(a.task)} · ${esc(a.action)}</div>
     ${a.late?`<span class="late">${esc(a.lateTask)} ${a.lateDays}일 경과</span>`:''}`);
  d.style.borderLeftColor=c;
  d.onclick=()=>go('#/card/'+a.id);
  return d;
}

function vHome(v){
  const k=D.kpi, done=loadLog();
  const doneKey=a=>a.id+'|'+a.task;
  const isDone=a=>done.some(x=>x.id===a.id&&x.task===a.task);
  const remain=D.queue.map(g=>({...g,
    items:g.ids.map(i=>byId[i]).filter(a=>a&&!isDone(a))}))
    .filter(g=>g.items.length);
  const nAct=remain.reduce((s,g)=>s+g.items.length,0);
  v.appendChild(el('div','sum',
    `<div><b>${nAct}</b><span>남은 조치</span></div>
     <div><b>${done.length}</b><span>오늘 완료</span></div>
     <div><b>${k.nConf}</b><span>경보</span></div>`));
  if(!remain.length){
    v.appendChild(el('div','empty','오늘 조치할 개체가 없습니다 👍'));
  }
  remain.forEach(g=>{
    const sup=Object.entries(g.supplies).map(([s,n])=>`${esc(s)}×${n}`).join(' · ');
    const head=el('div','bhead',
      `<div class="bh1"><span class="bord">${g.order}</span>
        <b>${esc(g.barn)}</b>
        <span class="bcnt">${g.items.length}건</span>
        ${g.crit?`<span class="bcrit">시한 ${g.crit}</span>`:''}</div>
       <div class="bsup">준비물 · ${sup||'-'}</div>`);
    v.appendChild(head);
    g.items.forEach(a=>{
      const c=D.taskColors[a.task]||'#888';
      const d=el('div','task',
        `<div class="tl"><b>${esc(a.id)}</b>
          <span class="dd" style="color:${c}">${dday(a.dday)}</span></div>
         <div class="t2">${esc(a.loc)}</div>
         <div class="t3" style="color:${c}">${esc(a.task)} · ${esc(a.action)}</div>
         ${a.late?`<span class="late">${esc(a.lateTask)} ${a.lateDays}일 경과</span>`:''}
         <div class="acts"><span class="ok">완료</span><span class="skip">미실시</span></div>`);
      d.style.borderLeftColor=c;
      d.querySelector('.ok').onclick=e=>{e.stopPropagation();
        addLog(a,'완료');nav();};
      d.querySelector('.skip').onclick=e=>{e.stopPropagation();
        addLog(a,'미실시');nav();};
      d.onclick=()=>go('#/card/'+a.id);
      v.appendChild(d);
    });
  });
  v.appendChild(el('div','hint',
    '<b>작업동별</b>로 묶었습니다. 사람은 축사를 하나씩 도니까요 — 긴급도 한 줄로 '
    +'세우면 1동→3동→1동 처럼 오가게 됩니다. 동 순서는 <b>가장 급한 개체가 있는 '
    +'동</b>부터이고, 동에 들어가기 전 챙길 <b>준비물</b>을 함께 냅니다. '
    +'완료를 누르면 로그에 쌓이고 큐에서 빠집니다.'));
}

function vList(v,q){
  const inp=el('input','srch');
  inp.placeholder='모돈번호 검색'; inp.value=q||'';
  const chips=el('div','chips');
  [['all','전체'],['공태','공태'],['교배','교배'],['임신','임신'],
   ['포유','포유'],['후보','후보']].forEach(([k,n])=>{
    const c=el('div','chip'+(filter===k?' on':''),n);
    c.onclick=()=>{filter=k;render();};
    chips.appendChild(c);
  });
  const box=el('div');
  v.append(inp,chips,box);
  function render(){
    chips.querySelectorAll('.chip').forEach((c,i)=>{
      const keys=['all','공태','교배','임신','포유','후보'];
      c.classList.toggle('on',keys[i]===filter);});
    box.innerHTML='';
    const s=inp.value.trim();
    const rows=D.animals.filter(a=>(filter==='all'||a.stage===filter)
      &&(!s||a.id.includes(s))).sort((x,y)=>x.id.localeCompare(y.id));
    if(!rows.length){box.appendChild(el('div','empty','해당 개체가 없습니다'));return;}
    rows.forEach(a=>{
      const sc=D.stageColors[a.stage]||'#888';
      const r=el('div','row',
        `<span class="pin" style="background:${D.statusColors[a.status]}"></span>
         <span class="rid">${esc(a.id)}</span>
         <span class="rloc">${esc(a.loc)}</span>
         <span class="rtag" style="background:color-mix(in srgb,${sc} 18%,transparent);
          color:${sc}">${esc(a.stage)}</span>`);
      r.onclick=()=>go('#/card/'+a.id);
      box.appendChild(r);
    });
  }
  inp.oninput=render; render();
}

function vCard(v,id){
  const a=byId[id];
  if(!a){v.appendChild(el('div','empty','개체를 찾을 수 없습니다'));return;}
  const sc=D.stageColors[a.stage]||'#888';
  const head=el('div','card2',
    `<div class="cno">${esc(a.id)}</div>
     <div class="cgrid">
      <div><span>현재상태</span><b>${esc(a.stage)}</b></div>
      <div><span>산차</span><b>${a.parity}산</b></div>
      <div><span>발정</span><b>${esc(a.estrus)} (${a.score.toFixed(2)})</b></div>
      <div><span>임신</span><b>${esc(a.preg)}</b></div>
      <div><span>위치</span><b>${esc(a.loc)}</b></div>
      <div><span>다음 작업</span><b>${esc(a.task)} ${dday(a.dday)}</b></div>
     </div>`);
  head.style.background=sc;
  v.appendChild(head);
  if(a.conflict)v.appendChild(el('div','hint warnbox',
    '⚠️ <b>모순 경보</b> — '+esc(a.conflict)));
  v.appendChild(el('div','sect','번식 일정'));
  (D.sched[a.id]||[]).forEach(t=>{
    const dd=dnum(t.d);
    if(dd<-40||dd>135)return;
    const c=D.taskColors[t.t]||'#888';
    v.appendChild(el('div','tli '+(t.e?'est':'conf'),
      `<span class="dot" style="color:${c}">${t.e?'~':'●'}</span>
       <span class="dt">${md(t.d)}</span>
       <span class="tk2">${esc(t.t)}</span>
       <span class="dd2">${dd>=0?dday(dd):(-dd)+'일 전'}</span>`));
  });
  v.appendChild(el('div','hint',
    '<b>●</b> 확정 · <b>~</b> 예상. 예정일은 표준 간격 기반 추정이며 '
    +'CCTV 나 육안으로 발정이 확인되면 그 시각으로 일정이 갱신됩니다.'));
}

function vMap(v){
  D.barns.forEach(b=>{
    const box=el('div','mbarn');
    box.appendChild(el('div','mh',
      `<span>${esc(b.barn)} ${esc(b.stage)}</span>`
      +(b.thi!=null?`<span class="thi" style="color:${b.color}">THI ${b.thi} ${esc(b.level)}</span>`:'')));
    b.pens.forEach(p=>{
      box.appendChild(el('div','mpen',esc(p.pen)+' · '+esc(p.housing)
        +' ('+p.slots.length+'/'+p.cap+')'));
      const row=el('div','mcells');
      p.slots.forEach(s=>{
        const a=byId[s.id]; if(!a)return;
        const i=el('i',null,esc(s.s));
        i.style.background=D.statusColors[a.status];
        if(a.late)i.style.border='2px solid #a02020';
        i.title=a.id+' · '+a.stage+' · '+a.task+' '+dday(a.dday);
        i.onclick=()=>go('#/card/'+a.id);
        row.appendChild(i);
      });
      box.appendChild(row);
    });
    v.appendChild(box);
  });
  const leg=el('div','mleg');
  Object.entries(D.statusColors).forEach(([k,c])=>{
    if(k==='공실')return;
    leg.appendChild(el('span',null,
      `<i style="background:${c}"></i>${esc(k)}`));
  });
  leg.appendChild(el('span',null,
    '<i style="border:2px solid #a02020"></i>기한 경과'));
  v.appendChild(leg);
  v.appendChild(el('div','hint',
    '색은 <b>들고 갈 것</b>을 뜻합니다(정액·초음파·분만준비). 칸을 눌러 개체카드로.'));
}

function vBoard(v){
  const k=D.kpi;
  v.appendChild(el('div','sum',
    `<div><b>${k.nSows}</b><span>모돈</span></div>
     <div><b>${k.turnover}</b><span>회전/년</span></div>
     <div><b>${k.svcTarget}</b><span>주 교배목표</span></div>`));
  v.appendChild(el('div','sect','주차별 분만 예정 (17주)'));
  const mx=Math.max(...D.board.map(b=>b.f),k.farrowTarget)||1;
  const ch=el('div','chart');
  D.board.forEach(b=>{
    const c=b.short&&b.locked?'#d03b3b':(b.short?'#e8a33d':'#2a78d6');
    const w=el('div','wk',
      `<div class="wb" style="height:${(72*b.f/mx).toFixed(0)}px;background:${c}"></div>
       <span>${b.f}</span><em>W${b.w}</em>`);
    w.title=`W${b.w} ${md(b.s)}~${md(b.e)} · 분만 ${b.f}복 (목표 ${b.t})`;
    ch.appendChild(w);
  });
  const tl=el('div','tline',`<span>목표 ${k.farrowTarget}</span>`);
  tl.style.bottom=(72*k.farrowTarget/mx+20).toFixed(0)+'px';
  ch.appendChild(tl); v.appendChild(ch);
  v.appendChild(el('div','sect','산차 구성'));
  const bars=el('div','bars');
  const pmax=Math.max(...D.parity.map(p=>p.n))||1;
  D.parity.forEach(p=>{
    const c=p.gap>3?'#d03b3b':(p.gap<-3?'#e8a33d':'#2a78d6');
    bars.appendChild(el('div','brow',
      `<span>${esc(p.p)}산</span>
       <span class="btrack"><span class="bfill" style="width:${(100*p.n/pmax).toFixed(0)}%;
        background:${c}"></span></span>
       <span>${p.n}두 (${(p.share*100).toFixed(0)}%/${(p.target*100).toFixed(0)}%)</span>`));
  });
  v.appendChild(bars);
  v.appendChild(el('div','hint',
    '앞쪽 주차의 <b>빨강은 이미 확정된 손실</b>입니다 — 임신 115일은 단축할 수 없어 '
    +'지금 교배해도 메울 수 없습니다. 주황은 아직 교배로 메울 수 있는 구간입니다.'));
}

function vAlert(v){
  const ai=D.ai;
  const p1=el('div','push',
    `<div class="pt">🐖 발정 확인 · ${esc(ai.id)}</div>
     <div class="pb">${esc(ai.loc)} · 승가허용 점수 <b>${ai.score.toFixed(2)}</b><br>
      적기 교배 <b>${esc(ai.ai1)} / ${esc(ai.ai2)}</b></div>`);
  p1.onclick=()=>go('#/ai'); v.appendChild(p1);
  const cf=D.animals.filter(a=>a.conflict);
  if(cf.length){const a=cf[0];
    const p=el('div','push warn',
      `<div class="pt">⚠️ 모순 경보 · ${esc(a.id)}</div>
       <div class="pb">${esc(a.stage)} 중인데 발정 신호(${a.score.toFixed(2)})<br>
        유산·오진·개체 오인 확인 필요</div>`);
    p.onclick=()=>go('#/card/'+a.id); v.appendChild(p);
  }else v.appendChild(el('div','push warn',
    '<div class="pt">⚠️ 모순 경보</div><div class="pb">해당 없음</div>'));
  const hot=D.barns.filter(b=>b.thi!=null&&b.level!=='적정')
    .sort((a,b)=>b.thi-a.thi);
  if(hot.length){const b=hot[0];
    const n=D.risk.filter(r=>r.barn===b.barn).length;
    const p=el('div','push heat',
      `<div class="pt">🌡️ ${esc(b.barn)} 열스트레스 (THI ${b.thi})</div>
       <div class="pb">착상기 모돈 <b>${n}두</b> — 3주 재발 확인 필수<br>
        ${esc(b.advice)}</div>`);
    p.onclick=()=>go('#/map'); v.appendChild(p);
  }
  v.appendChild(el('div','push feed',
    '<div class="pt">🍽️ 급이 소외 · 군사 돈방</div>'
    +'<div class="pb">섭취량 하위 개체 분리 급이 검토<br>'
    +'<em>feeding_monitor — 별도 영상 입력 필요</em></div>'));
  v.appendChild(el('div','hint',
    '알림은 <b>무엇을 들고 가야 하는지</b>까지 말합니다. 모순 경보·착상기 '
    +'열스트레스는 환경·번식기록을 겹쳐야 나오는 알림입니다. 눌러서 상세로.'));
}

function vAi(v){
  const a=D.ai;
  v.innerHTML=
   `<div class="frow"><span>모돈번호</span><div class="fval"><b>${esc(a.id)}</b></div></div>
    <div class="frow"><span>이유일 <i>입력</i></span><div class="fval">${esc(a.wean)}</div></div>
    <div class="frow"><span>예정일 <i>자동</i></span>
     <div class="fval auto">${esc(a.planned)}</div></div>
    <div class="frow"><span>발정 확인 <i>CCTV</i></span>
     <div class="fval auto">${esc(a.confirmed)} <em>점수 ${a.score.toFixed(2)}</em></div></div>
    <div class="frow"><span>1차 교배 <i>적기 자동</i></span>
     <div class="fval hi"><b>${esc(a.ai1)}</b> <em>발정 후 ${a.h1}h</em></div></div>
    <div class="frow"><span>2차 교배 <i>적기 자동</i></span>
     <div class="fval hi"><b>${esc(a.ai2)}</b> <em>발정 후 ${a.h2}h</em></div></div>
    <div class="frow"><span>교배자</span><div class="fval">선택 ▾</div></div>
    <div class="frow"><span>웅돈</span><div class="fval">선택 ▾</div></div>
    <div class="hint">농가가 채우는 칸은 <b>교배자·웅돈 둘뿐</b>입니다. 날짜·시각은
     이유일 하나에서 계산됐고, CCTV 가 발정을 확인하면 그 시각 기준으로 다시
     잡힙니다(배란 추정 ${a.ovul}h).</div>
    <div class="btn">저장</div>`;
}

window.addEventListener('hashchange',nav);
$('#back').onclick=()=>history.back();
document.querySelectorAll('.tab').forEach(t=>
  t.onclick=()=>go('#/'+t.dataset.r));
nav();
"""


def main() -> int:
    D = build_payload()
    # allow_nan=False 로 NaN 이 새면 즉시 터지게 한다. 기본값은 `NaN` 을 그대로
    # 찍는데, 그것이 JS 에서는 문법상 유효한 리터럴이라 조용히 통과한 뒤
    # 화면에서 truthy 로 잘못 동작한다(모순 경보가 전 개체에 붙던 것과 같은 부류).
    data = json.dumps(D, ensure_ascii=False, separators=(",", ":"),
                      allow_nan=False)
    tabs = [("home", "☰", "오늘"), ("list", "☷", "목록"),
            ("map", "▦", "도면"), ("board", "▤", "현황"),
            ("log", "✓", "로그"), ("alert", "◉", "알림")]
    tab_html = "".join(
        f'<div class="tab" data-r="{r}"><b>{i}</b>{n}</div>' for r, i, n in tabs)

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>양돈 번식관리 앱 프로토타입</title><style>{CSS}</style></head><body>
<div class="intro"><h1>📱 앱 프로토타입 (동작)</h1>
<p>실제로 눌러서 돌아다닐 수 있습니다. 아래 탭으로 화면을 옮기고, 목록·도면에서
개체를 누르면 카드로 들어갑니다. 화면의 모든 값은 파이썬 모듈이 계산한 실데이터입니다
(기준일 {D["today"]}).</p></div>
<div class="app">
  <div class="bar"><span>9:41</span><span>▮▮▮ ᯤ</span></div>
  <div class="hdr"><span class="back" id="back">‹</span><h2 id="title">오늘 할 일</h2></div>
  <div class="view" id="view"></div>
  <div class="tabs">{tab_html}</div>
</div>
<div class="foot">※ 합성 데이터 시연입니다. 실제로는 농장 번식기록·축사 등록 정보·
CCTV 발정 점수·환경 센서값을 그대로 넣으면 같은 화면이 나옵니다.<br>
※ 외부 연결·라이브러리 없이 동작합니다(데이터는 페이지 안에 포함).</div>
<script>const D={data};{JS}</script>
</body></html>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"앱 프로토타입 생성: {OUT} ({os.path.getsize(OUT) // 1024}KB)")
    print(f"  개체 {len(D['animals'])}두 · 축사 {len(D['barns'])}동 · "
          f"일정 {sum(len(v) for v in D['sched'].values())}건 · 화면 7종")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
