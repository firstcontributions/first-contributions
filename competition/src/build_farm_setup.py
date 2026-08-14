"""농장 최초 등록 — 규모·축사동·운영 방식을 받아 **바로 진단으로 넘긴다**.

지금까지 모든 화면이 시연농장 300두를 기준으로 돌았다. 사용자가 자기 농장을
넣을 자리가 없었다. 이 화면이 그 입구다.

## 폼이 아니라 검산기다

칸을 채우는 것만으로는 값이 없다. 넣는 즉시 **여섯 가지를 되짚어 준다.**

  1) 배치 설계     모돈·간격 → 배치 수 · 배치당 두수 · 필요 분만틀
  2) 필요 vs 보유  등록한 축사동 자리와 대 봐서 부족분을 즉시
  3) 포유 상한     방 주기에서 분만대기·세척을 빼고 남는 것이 포유 최대치
  4) 발정 판정 경로 사육 방식(스톨/군사)만 정해지면 분석 방법이 따라 정해진다
  5) 분포에서의 위치 성적을 넣으면 466농장 어디쯤인지
  6) **여름 손실 원/년** 발견 ③′ 를 **우리 규모로** — 아래

## 원/년을 처음으로 '우리 규모' 로 놓는다

발견 ③′ 의 금액은 전부 300두 환산이었다. 이 화면만 사용자의 상시모돈수를
알기 때문에, 같은 산식을 그 규모로 다시 놓을 수 있다. 환산 계수는
`farm_monthly_panel` 이 쓴 값을 그대로 받아 온다 — 여기서 새로 만들면
같은 농장에 두 화면이 다른 금액을 말한다.

여름·겨울 교배분 분만율을 넣으면 **우리 농장 값**이 나오고, 비우면 국내
분포를 우리 규모로 환산한 **범위**가 나온다. 둘을 구별해 표시한다.
계절 취약도는 연간 성적과 상관이 없으므로(ρ −0.149) PSY 로 대신 맞힐 수
없다는 것도 같이 적는다.

## 빈 칸을 조용히 채우지 않는다

이 프로젝트에서 실제로 겪은 버그다 — 진단 기본값을 실측 중앙값으로 깔았더니
**격차가 늘 +0.00** 으로 찍혔다. 중앙값을 중앙값과 비교하고 있었던 것이다.
그래서 성적란은 비우면 `진단 제외` 로 표시하고, 중앙값을 대신 넣지 않는다.

## 나가는 곳

  · `localStorage` 에만 저장한다. 서버로 보내지 않는다 — 농장 식별자다.
  · `run_farm.py` 인자 문자열과 JSON 을 만들어 준다. 복사해서 그대로 돌린다.

    python competition/src/build_farm_setup.py
출력: competition/dashboard/farm_setup.html  (외부 연결 불필요)
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)          # pigflow 패키지가 competition/ 아래에 있다

OUT = os.path.join(ROOT, "dashboard", "farm_setup.html")
STATS = os.path.join(ROOT, "data", "korean_farm_stats.json")
SEASON = os.path.join(ROOT, "data", "farm_monthly_panel.json")

# 축사 용도·사육 방식은 farm_registry 가 검증하는 어휘를 그대로 쓴다.
# 여기서 새 낱말을 만들면 등록 화면과 코드가 갈라진다.
import farm_registry as fr                                    # noqa: E402
import batch_flow as bf                                       # noqa: E402

# 간격 선택지 — batch_flow.compare 와 같은 눈금
INTERVALS = [("주간", 7), ("10일", 10), ("2주", 14), ("3주", 21),
             ("4주", 28), ("5주", 35)]

# 농장 형태. 부지가 나뉘면 배치 간 병원체 차단이 쉬워지는 대신 수송이 는다.
SITE_TYPES = [
    ("1site", "일관 (1-site)", "번식~비육이 한 부지. 국내 대부분"),
    ("2site", "2-site", "번식사 / 자돈·비육사 분리"),
    ("3site", "3-site", "번식 / 자돈 / 비육 각각 분리 — 차단 방역 최상"),
    ("breed", "번식 전문", "이유자돈까지 생산 후 판매"),
    ("finish", "비육 전문", "자돈을 사 와 비육만"),
]

# 성적 입력란 — run_farm / farm_gap 이 실제로 받는 인자만 둔다
PERF = [
    ("farrowing_rate", "분만율", "%", "farrowing_rate", 40, 100),
    ("weaned", "복당 이유두수", "두", "weaned", 5, 18),
    ("npd", "연간 비생산일수(NPD)", "일", "npd", 0, 200),
    ("wean_to_estrus", "재귀발정일", "일", "wean_to_estrus", 3, 30),
]


def quantiles() -> dict:
    """466농장 분위수 — 성적을 넣었을 때 어디쯤인지 보여 주는 데만 쓴다."""
    if not os.path.exists(STATS):
        return {}
    q = json.load(open(STATS, encoding="utf-8")).get("quantiles") or {}
    keep = ("psy", "farrowing_rate", "weaned", "npd", "wean_to_estrus")
    return {k: {p: q[k][p] for p in ("p10", "p25", "p50", "p75", "p90")}
            for k in keep if k in q}


def season() -> dict:
    """계절 손실 — 발견 ③′ 를 이 화면에 붙인다.

    지금까지 원/년은 전부 **300두 환산**이었다. 이 화면은 사용자의 상시모돈수를
    아는 유일한 자리라서, 같은 산식을 그 규모로 다시 놓을 수 있다.

    환산 계수(PSY 1두의 두당 가치)와 여름 비중은 `farm_monthly_panel` 이 쓴
    값을 그대로 가져온다. 여기서 새로 만들면 두 화면이 다른 금액을 말한다.
    """
    if not os.path.exists(SEASON):
        return {}
    r = json.load(open(SEASON, encoding="utf-8"))
    import farm_monthly_panel as mp
    return {
        "loss": r["loss"], "shrunk": r["loss_shrunk"],
        "n_farms": r["n_farms"],
        "per_sow_won": r["money"]["per_sow_won"],
        "ref_sows": r["money"]["ref_sows"],
        "share": mp.SEASON_SHARE,
        "overall_summer": r["overall"]["summer"],
        "overall_winter": r["overall"]["winter"],
        "gap": r["overall"]["summer_minus_winter"],
        "true_share": r["spread"]["true_share"],
        # 여름에 사고 구성이 어디로 기우는가 — 처방이 여기서 나온다
        "acc_1st": r["pathways"]["accidents"]["delta"].get("임신사고(1차)", 0.0),
        "acc_summer": r["pathways"]["accidents"]["summer"].get("임신사고(1차)", 0.0),
        "acc_winter": r["pathways"]["accidents"]["winter"].get("임신사고(1차)", 0.0),
        "rho_psy": r["join"].get("PSY", {}).get("rho"),
        "rho_sows": r["join"].get("상시모돈", {}).get("rho"),
        # 착상기 — 여름 손실을 겨냥할 시점
        "implantation": list(_implantation()),
    }


def _implantation() -> tuple:
    import barn_environment as be
    return be.IMPLANTATION_WINDOW


def defaults() -> dict:
    """번식 상수 기본값 — pigflow 설정에서 받는다. 여기서 새로 만들지 않는다."""
    from pigflow.config import BREEDING_DEFAULTS as B
    return {"gestation": float(B["gestation_days"]),
            "lactation": float(B["lactation_days"]),
            "wean_to_service": float(B["wean_to_service_days"]),
            "pre_farrow": 7.0, "washout": 7.0,
            "farrowing_rate": float(B["farrowing_rate"]) * 100.0,
            "weaned": float(B["weaned_per_litter"])}


def _opts(pairs) -> str:
    return "".join(f'<option value="{v}">{t}</option>' for v, t in pairs)


def build() -> str:
    q = quantiles()
    d = defaults()
    stages = list(fr.BARN_STAGES)
    housing = [(k, v[0]) for k, v in fr.HOUSING.items()]
    # 사육 방식 → 발정 판정 경로. 등록만 하면 분석 방법이 정해진다는 걸
    # 화면에서 바로 보여 주기 위해 통째로 넘긴다.
    routes = {k: {"label": v[0], "module": v[1], "signal": v[2], "note": v[3]}
              for k, v in fr.HOUSING.items()}
    sn = season()
    cfg = {"q": q, "d": d, "intervals": INTERVALS, "routes": routes,
           "perf": [{"key": k, "label": lb, "unit": u, "arg": a,
                     "lo": lo, "hi": hi} for k, lb, u, a, lo, hi in PERF],
           "season": sn,
           "cycle_base": d["gestation"] + d["lactation"] + d["wean_to_service"]}

    stage_desc = "".join(
        f'<div class="bnrow"><b>{s}</b><span class="cnt">{fr.BARN_STAGES[s]}</span></div>'
        for s in stages)

    # 통합 콘솔이 이 파일을 통째로 iframe 에 넣는다 — 완전한 문서여야 한다
    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<title>농장 등록</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{{--page:#f6f7f9;--surface:#fff;--surface2:#eef0f4;--ink:#14161a;
--ink2:#3d434d;--muted:#767d8a;--border:#dfe3ea;--accent:#2a78d6;
--good:#1baf7a;--bad:#d03b3b;--warn:#e8a33d}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
--page:#0d0f12;--surface:#161a20;--surface2:#1f242c;--ink:#eef1f5;
--ink2:#c2c8d2;--muted:#8a919c;--border:#2a303a}}}}
:root[data-theme="dark"]{{--page:#0d0f12;--surface:#161a20;--surface2:#1f242c;
--ink:#eef1f5;--ink2:#c2c8d2;--muted:#8a919c;--border:#2a303a}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;
background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:1060px;margin:0 auto}}
h1{{font-size:1.55rem;letter-spacing:-.02em}}
.sub{{color:var(--ink2);font-size:.92rem;margin:5px 0 18px}}
h2{{font-size:1.02rem;margin:26px 0 4px}}
.h2d{{font-size:.8rem;color:var(--muted);margin-bottom:12px}}
.card{{background:var(--surface);border:1px solid var(--border);
border-radius:13px;padding:17px 18px;margin-bottom:14px;overflow-x:auto}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:13px}}
label{{display:block;font-size:.78rem;font-weight:600;margin-bottom:4px}}
label .u{{color:var(--muted);font-weight:400}}
input,select{{width:100%;padding:8px 10px;border:1px solid var(--border);
border-radius:9px;background:var(--page);color:var(--ink);font-size:.9rem;
font-family:inherit}}
input:focus,select:focus{{outline:2px solid var(--accent);outline-offset:-1px}}
input.bad{{border-color:var(--bad)}}
.hint{{font-size:.7rem;color:var(--muted);margin-top:3px;min-height:1em}}
.hint.skip{{color:var(--warn);font-weight:600}}
.hint.err{{color:var(--bad);font-weight:600}}
table{{width:100%;border-collapse:collapse;font-size:.83rem;margin-top:4px}}
td,th{{text-align:left;padding:7px 9px;border-bottom:1px solid var(--surface2);
vertical-align:middle}}
th{{color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.03em}}
td input,td select{{padding:5px 7px;font-size:.82rem}}
button{{font-family:inherit;font-size:.82rem;padding:7px 13px;border-radius:9px;
border:1px solid var(--border);background:var(--surface2);color:var(--ink);
cursor:pointer;font-weight:600}}
button:hover{{border-color:var(--accent);color:var(--accent)}}
button.pri{{background:var(--accent);color:#fff;border-color:var(--accent)}}
button.x{{padding:4px 9px;color:var(--bad)}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
gap:11px;margin-top:4px}}
.kpi{{background:var(--surface2);border-radius:11px;padding:11px 13px}}
.kpi .v{{font-size:1.5rem;font-weight:700;letter-spacing:-.02em}}
.kpi .l{{font-size:.76rem;font-weight:600;margin-top:1px}}
.kpi .d{{font-size:.68rem;color:var(--muted);margin-top:2px}}
.warn{{border-left:4px solid var(--bad);
background:color-mix(in srgb,var(--bad) 6%,var(--surface))}}
.good{{border-left:4px solid var(--good);
background:color-mix(in srgb,var(--good) 6%,var(--surface))}}
.bnrow{{display:flex;align-items:center;gap:10px;padding:6px 0;
border-bottom:1px solid var(--surface2);font-size:.84rem}}
.bnrow:last-child{{border-bottom:0}}
.cnt{{margin-left:auto;color:var(--muted);font-size:.75rem;text-align:right}}
.tag{{font-size:.65rem;font-weight:700;color:var(--accent);
background:color-mix(in srgb,var(--accent) 15%,transparent);
padding:1px 6px;border-radius:999px}}
.tag.err{{color:var(--bad);background:color-mix(in srgb,var(--bad) 15%,transparent)}}
.tag.ok{{color:var(--good);background:color-mix(in srgb,var(--good) 15%,transparent)}}
.tag.skip{{color:var(--warn);background:color-mix(in srgb,var(--warn) 15%,transparent)}}
textarea{{width:100%;min-height:112px;padding:10px;border:1px solid var(--border);
border-radius:9px;background:var(--page);color:var(--ink);font-size:.78rem;
font-family:ui-monospace,SFMono-Regular,Menlo,monospace;resize:vertical}}
.note{{font-size:.73rem;color:var(--muted);margin-top:10px;line-height:1.6}}
.strip{{position:relative;height:36px;margin-top:6px}}
.strip .band{{position:absolute;top:13px;height:10px;border-radius:5px;
background:var(--surface2)}}
.strip .band2{{position:absolute;top:13px;height:10px;border-radius:5px;
background:color-mix(in srgb,var(--accent) 22%,var(--surface2))}}
.strip .med{{position:absolute;top:8px;width:2px;height:20px;background:var(--ink2)}}
.strip .me{{position:absolute;top:9px;width:12px;height:18px;
border-radius:6px;border:2px solid var(--surface)}}
.strip .lb{{position:absolute;top:26px;font-size:.62rem;color:var(--muted);
transform:translateX(-50%);white-space:nowrap}}
.back{{display:inline-block;margin-bottom:14px;font-size:.8rem;
color:var(--accent);text-decoration:none}}
.row{{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin-top:11px}}
</style></head><body><div class="wrap">
<a class="back" href="index.html">← 통합 대시보드</a>
<h1>🏠 농장 등록</h1>
<div class="sub">처음 한 번만 채우면 됩니다. <b>폼이 아니라 검산기입니다</b> —
넣는 즉시 배치 설계·필요 돈방·포유 상한·발정 판정 경로를 되짚어 줍니다.
입력은 <b>이 브라우저에만</b> 저장되고 어디로도 전송되지 않습니다.</div>

<h2>1. 규모</h2>
<div class="h2d">상시모돈수와 농장 형태가 아래 계산의 출발점입니다.</div>
<div class="card"><div class="grid">
  <div><label>농장 이름 <span class="u">(로컬 표시용)</span></label>
    <input id="f_name" placeholder="예: 행복농장"><div class="hint">저장되지 않고 화면에만 씁니다</div></div>
  <div><label>상시 모돈수 <span class="u">두</span></label>
    <input id="f_sows" type="number" min="1" max="20000" value="300"><div class="hint" id="h_sows"></div></div>
  <div><label>후보돈 <span class="u">두 · 모르면 비움</span></label>
    <input id="f_gilts" type="number" min="0" max="5000" placeholder=""><div class="hint"></div></div>
  <div><label>농장 형태</label>
    <select id="f_site">{_opts([(v, t) for v, t, _ in SITE_TYPES])}</select>
    <div class="hint" id="h_site"></div></div>
</div></div>

<h2>2. 축사동</h2>
<div class="h2d">동을 추가하고 용도·방 수·방당 자리·사육 방식을 넣습니다.
<b>사육 방식만 정하면 발정 판정 경로가 따라 정해집니다.</b></div>
<div class="card">
<table><thead><tr><th>동 이름</th><th>용도</th><th>방 수</th>
<th>방당 자리</th><th>사육 방식</th><th>자리 합</th><th></th></tr></thead>
<tbody id="barns"></tbody></table>
<div class="row"><button id="add">+ 동 추가</button>
<button id="preset">일관농장 기본 구성 넣기</button></div>
<div class="note">용도별 정의 — 이 어휘는 <code>farm_registry.BARN_STAGES</code>
와 같습니다. 화면에서 새 낱말을 만들면 코드와 갈라집니다.</div>
<div style="margin-top:8px">{stage_desc}</div>
</div>

<h2>3. 운영 방식</h2>
<div class="h2d">배치 간격이 방 수와 이유일령을 동시에 정합니다.</div>
<div class="card"><div class="grid">
  <div><label>배치 간격</label>
    <select id="f_interval">{_opts([(str(v), t) for t, v in INTERVALS])}</select>
    <div class="hint" id="h_interval"></div></div>
  <div><label>포유기간 <span class="u">일</span></label>
    <input id="f_lact" type="number" min="14" max="42" value="{d['lactation']:.0f}">
    <div class="hint" id="h_lact"></div></div>
  <div><label>분만 전 이동 <span class="u">일</span></label>
    <input id="f_pre" type="number" min="0" max="14" value="{d['pre_farrow']:.0f}"><div class="hint"></div></div>
  <div><label>세척·건조 <span class="u">일</span></label>
    <input id="f_wash" type="number" min="0" max="14" value="{d['washout']:.0f}">
    <div class="hint" id="h_wash"></div></div>
</div></div>

<h2>4. 성적 — 아는 것만</h2>
<div class="h2d"><b>비운 칸은 중앙값으로 채우지 않고 진단에서 뺍니다.</b>
중앙값을 넣으면 그 항목의 격차가 늘 0 으로 찍힙니다 — 실제로 겪은 버그입니다.</div>
<div class="card"><div class="grid" id="perf"></div></div>

<h2>5. 여름 손실 — 우리 규모로</h2>
<div class="h2d">국내 67농장 실측에서 여름 교배분 분만율이 겨울보다
<b>중앙 +2.7%p</b> 떨어집니다. 그런데 <b>농장마다 갈립니다</b>(하위10% −4.4 ~
상위10% +13.0%p). 아래 두 칸을 알면 우리 농장이 어느 쪽인지 나옵니다.</div>
<div class="card"><div class="grid">
  <div><label>여름 교배분 분만율 <span class="u">7·8·9월 교배 · %</span></label>
    <input id="s_summer" type="number" step="0.1" min="20" max="100" placeholder="">
    <div class="hint">분만 11·12·1월분입니다(임신 114일 되돌림)</div></div>
  <div><label>겨울 교배분 분만율 <span class="u">1·2·3월 교배 · %</span></label>
    <input id="s_winter" type="number" step="0.1" min="20" max="100" placeholder="">
    <div class="hint">분만 5·6·7월분</div></div>
</div></div>
<div id="season"></div>

<h2>6. 즉시 검산</h2>
<div class="h2d">위 값으로 바로 나오는 것들. 새 산식이 아니라
<code>batch_flow.plan</code> 과 같은 식입니다.</div>
<div class="card"><div class="kpis" id="kpis"></div>
<div class="note" id="cyc"></div></div>
<div id="checks"></div>
<div class="card"><b style="font-size:.9rem">발정 판정 경로</b>
<div class="h2d" style="margin:4px 0 8px">등록한 사육 방식에서 따라 나옵니다.</div>
<div id="routes"></div></div>
<div id="pos"></div>

<h2>7. 내보내기</h2>
<div class="h2d">복사해서 그대로 돌리면 이 농장 기준으로 전체 화면이 다시 계산됩니다.</div>
<div class="card">
<label>명령줄</label><textarea id="out_cmd" readonly style="min-height:64px"></textarea>
<label style="margin-top:11px">설정 JSON</label><textarea id="out_json" readonly></textarea>
<div class="row"><button class="pri" id="copy_cmd">명령줄 복사</button>
<button id="copy_json">JSON 복사</button>
<button id="reset">초기화</button>
<span id="saved" class="hint" style="margin:0"></span></div>
<div class="note">🔒 농장 이름과 성적은 <b>농장 식별자</b>입니다.
이 화면은 <code>localStorage</code> 에만 쓰고 네트워크 요청을 하지 않습니다 —
원자료 스프레드시트를 커밋하지 않는 것과 같은 이유입니다.</div>
</div>
</div>
<script>
const CFG = {json.dumps(cfg, ensure_ascii=False)};
const STAGES = {json.dumps(stages, ensure_ascii=False)};
const HOUSING = {json.dumps(housing, ensure_ascii=False)};
const KEY = "yangdon.farm.setup.v1";
const $ = s => document.querySelector(s);
const el = (t, c) => {{ const e = document.createElement(t); if (c) e.className = c; return e; }};

// 일관농장 기본 구성 — farm_registry.demo_farm 과 같은 뼈대.
// 자리 수는 모돈수에서 유도한다(주기 비율). 눈대중으로 적으면 안 된다.
//
// **분만사만 비율로 짓지 않는다.** 연속 흐름 비율로 재면 800두에서 172자리인데
// 배치 설계는 192자리를 요구한다 — AIAO 는 방 하나가 배치 하나를 통째로
// 받아야 하므로 방마다 **최대 배치 크기**만큼 있어야 하고, 평균으로 지으면
// 절반의 배치가 안 들어간다. 그래서 분만사는 배치 설계에서 역산한다.
function preset(sows) {{
  const cyc = CFG.cycle_base, d = CFG.d;
  const mate = Math.round(sows * (d.wean_to_service + 28) / cyc);
  const gest = Math.round(sows * (d.gestation - 28 - d.pre_farrow) / cyc);
  const p = planOf({{sows: sows}});
  return [
    {{name: "1동", stage: "교배사", rooms: 1, per: mate, housing: "stall"}},
    {{name: "2동", stage: "임신사", rooms: 2, per: Math.ceil(gest / 2), housing: "group"}},
    {{name: "3동", stage: "분만사", rooms: p.rooms, per: Math.ceil(p.farrow), housing: "crate"}},
    {{name: "4동", stage: "후보사", rooms: 1, per: Math.max(4, Math.round(sows * 0.05)), housing: "group"}},
  ];
}}

let barns = [];

function opts(list, sel) {{
  return list.map(o => {{
    const [v, t] = Array.isArray(o) ? o : [o, o];
    return `<option value="${{v}}"${{v === sel ? " selected" : ""}}>${{t}}</option>`;
  }}).join("");
}}

function drawBarns() {{
  const tb = $("#barns"); tb.innerHTML = "";
  barns.forEach((b, i) => {{
    const tr = el("tr");
    tr.innerHTML =
      `<td><input data-i="${{i}}" data-k="name" value="${{b.name}}" style="min-width:74px"></td>` +
      `<td><select data-i="${{i}}" data-k="stage">${{opts(STAGES, b.stage)}}</select></td>` +
      `<td><input data-i="${{i}}" data-k="rooms" type="number" min="1" max="99" value="${{b.rooms}}" style="width:66px"></td>` +
      `<td><input data-i="${{i}}" data-k="per" type="number" min="1" max="9999" value="${{b.per}}" style="width:78px"></td>` +
      `<td><select data-i="${{i}}" data-k="housing">${{opts(HOUSING, b.housing)}}</select></td>` +
      `<td><b>${{(b.rooms * b.per).toLocaleString()}}</b></td>` +
      `<td><button class="x" data-del="${{i}}">삭제</button></td>`;
    tb.appendChild(tr);
  }});
  if (!barns.length) {{
    const tr = el("tr");
    tr.innerHTML = '<td colspan="7" style="color:var(--muted);font-size:.82rem">' +
      '등록된 동이 없습니다. “일관농장 기본 구성 넣기” 로 시작해 보세요.</td>';
    tb.appendChild(tr);
  }}
}}

function num(id) {{ const v = parseFloat($(id).value); return isFinite(v) ? v : null; }}

function capacity(stage) {{
  return barns.filter(b => b.stage === stage)
              .reduce((s, b) => s + b.rooms * b.per, 0);
}}
function roomsOf(stage) {{
  return barns.filter(b => b.stage === stage).reduce((s, b) => s + b.rooms, 0);
}}

// batch_flow.plan 과 같은 식. 여기서 다르게 계산하면 화면끼리 싸운다.
function planOf(over) {{
  over = over || {{}};
  const sows = over.sows ?? (num("#f_sows") || 0);
  const iv = parseFloat($("#f_interval").value);
  const lact = num("#f_lact") ?? CFG.d.lactation;
  const pre = num("#f_pre") ?? CFG.d.pre_farrow;
  const wash = num("#f_wash") ?? CFG.d.washout;
  // 설계에는 분만율이 **반드시** 있어야 한다. 성적란을 비웠으면 진단에서는
  // 빼지만 설계에서는 뺄 수가 없으므로, 기본값을 쓰되 '가정' 이라고 밝힌다.
  const rIn = num("#p_farrowing_rate");
  const rateSrc = (rIn !== null) ? "입력값" : "설계 가정";
  const rate = (rIn ?? CFG.d.farrowing_rate) / 100;
  const cycle = CFG.d.wean_to_service + CFG.d.gestation + lact;
  const nb = cycle / iv;
  const perBatch = sows / nb;
  const farrow = perBatch * rate;
  const occupy = pre + lact + wash;
  const minRooms = Math.ceil(occupy / iv);
  const slack = minRooms * iv - occupy;
  const rooms = slack < 3 ? minRooms + 1 : minRooms;
  return {{sows, iv, lact, pre, wash, rate, rateSrc, cycle, nb, perBatch, farrow,
           occupy, minRooms, slack, rooms, crates: Math.ceil(farrow) * rooms}};
}}

function kpi(v, l, d) {{
  return `<div class="kpi"><div class="v">${{v}}</div><div class="l">${{l}}</div>` +
         `<div class="d">${{d}}</div></div>`;
}}

function strip(q, v, unit, higherBetter) {{
  const lo = q.p10, hi = q.p90, span = Math.max(1e-9, hi - lo), pad = span * .18;
  const x0 = lo - pad, x1 = hi + pad;
  const px = x => ((x - x0) / (x1 - x0)) * 100;
  const good = (v >= q.p50) === higherBetter;
  const col = good ? "var(--good)" : "var(--bad)";
  const cl = x => Math.max(0, Math.min(100, x));
  return `<div class="strip">` +
    `<div class="band" style="left:${{px(lo)}}%;width:${{px(hi) - px(lo)}}%"></div>` +
    `<div class="band2" style="left:${{px(q.p25)}}%;width:${{px(q.p75) - px(q.p25)}}%"></div>` +
    `<div class="med" style="left:${{px(q.p50)}}%"></div>` +
    `<div class="me" style="left:calc(${{cl(px(v))}}% - 6px);background:${{col}}"></div>` +
    `<div class="lb" style="left:${{px(lo)}}%">하위10% ${{lo}}</div>` +
    `<div class="lb" style="left:${{px(q.p50)}}%">중앙 ${{q.p50}}</div>` +
    `<div class="lb" style="left:${{px(hi)}}%">상위10% ${{hi}}</div></div>`;
}}

// 발견 ③′ 를 **우리 규모로** 다시 놓는다.
// 지금까지 원/년은 전부 300두 환산이었고, 이 화면만 실제 상시모돈수를 안다.
// 산식은 farm_monthly_panel.to_money 와 같다 —
//   ΔPSY = PSY × (여름 3개월/12) × (손실%p ÷ 겨울 분만율)
//   원/년 = ΔPSY × PSY 1두의 두당 가치 × 상시모돈
function renderSeason(p) {{
  const S = CFG.season;
  const box = $("#season");
  if (!S || !S.per_sow_won) {{ box.innerHTML = ""; return; }}

  // PSY 는 항등식으로 낸다(farm_gap.psy_from). 재료가 없으면 실측 중앙값을
  // 쓰되 **가정이라고 밝힌다** — 조용히 넣으면 그게 내 농장 값인 줄 안다.
  const w = num("#p_weaned"), npd = num("#p_npd");
  let psy, psySrc;
  if (w !== null && npd !== null && npd < 365) {{
    psy = w * (365 - npd) / (CFG.d.gestation + p.lact);
    psySrc = "입력값에서 유도";
  }} else {{
    psy = CFG.q.psy ? CFG.q.psy.p50 : 24.1;
    psySrc = "466농장 중앙값 · 가정";
  }}

  const su = num("#s_summer"), wi = num("#s_winter");
  const won = (lossPP) =>
    psy * S.share * (lossPP / Math.max(1e-9, wi ?? S.overall_winter))
    * S.per_sow_won * p.sows;

  let head, body;
  if (su !== null && wi !== null) {{
    const loss = wi - su;
    const dPsy = psy * S.share * (loss / wi);
    const money = dPsy * S.per_sow_won * p.sows;
    const q = S.loss;
    const worse = loss > q.median;
    head =
      `<div class="kpis">` +
      kpi(`${{loss >= 0 ? "+" : ""}}${{loss.toFixed(1)}}%p`, "우리 농장 여름 손실",
          `겨울 ${{wi}} − 여름 ${{su}}`) +
      kpi(`${{dPsy >= 0 ? "+" : ""}}${{dPsy.toFixed(2)}}두`, "연간 PSY 손실",
          `PSY ${{psy.toFixed(1)}} · ${{psySrc}}`) +
      kpi(`${{(money / 1e4).toLocaleString(undefined, {{maximumFractionDigits: 0}})}}만원`,
          "연 손실 상한", `${{Math.round(p.sows)}}두 기준`) +
      `</div>` +
      strip({{p10: q.p10, p25: q.p25, p50: q.median, p75: q.p75, p90: q.p90}},
            +loss.toFixed(1), "%p", false) +
      `<div class="note">국내 <b>${{S.n_farms}}농장</b> 분포에서 ` +
      `${{worse ? "<b>중앙보다 취약한 쪽</b>" : "중앙보다 무던한 쪽"}}입니다. ` +
      `겨울 수준을 되찾았을 때의 몫이라 <b>손실 상한</b>이고, 냉방 장비값을 뺀 ` +
      `순이익이 아닙니다.</div>`;
  }} else {{
    // **패널의 733만원(300두 중앙)과 같은 값이 아니다.** 저건 농장마다
    // 자기 PSY·자기 겨울로 낸 금액들의 **중앙값**이고, 여기 726만원은
    // **중앙 손실 하나를 대표 PSY 에 적용한** 시나리오다. 곱의 중앙값과
    // 중앙값의 곱은 다르다 — 육성률을 분위수끼리 나눠 92.1% 로 틀렸던 것과
    // 같은 갈래라, 두 수를 억지로 맞추지 않고 라벨을 '가정' 으로 둔다.
    const mid = won(S.loss.median), p90 = won(S.loss.p90);
    head =
      `<div class="kpis">` +
      kpi(`${{(mid / 1e4).toLocaleString(undefined, {{maximumFractionDigits: 0}})}}만원`,
          "중앙 농장이라면", `여름 손실 +${{S.loss.median}}%p · 가정`) +
      kpi(`${{(p90 / 1e4).toLocaleString(undefined, {{maximumFractionDigits: 0}})}}만원`,
          "취약 상위10% 라면", `여름 손실 +${{S.loss.p90}}%p · 가정`) +
      kpi(`${{Math.round(p.sows)}}두`, "우리 규모로 환산", `PSY ${{psy.toFixed(1)}} · ${{psySrc}}`) +
      `</div>` +
      `<div class="note"><b>두 칸을 비웠으므로 위는 우리 농장 값이 아닙니다</b> — ` +
      `국내 분포를 우리 규모로 환산한 범위입니다. 어느 쪽인지 알려면 ` +
      `월별 분만율 12개월이 필요합니다.</div>`;
  }}

  // **연간 성적으로는 예측이 안 된다.** 이걸 안 적으면 위 두 칸을 비운 채
  // PSY 만 보고 "우리는 괜찮겠지" 로 넘어간다.
  body =
    `<div class="note" style="margin-top:12px">` +
    `<b>연간 성적으로 계절 취약도를 맞힐 수 없습니다.</b> 67농장에서 ` +
    `PSY 와의 상관 ρ ${{S.rho_psy}} · 상시모돈 ρ ${{S.rho_sows}} 로 사실상 무관합니다 — ` +
    `<b>잘하는 농장도 여름은 피하지 못합니다.</b><br>` +
    `무너지는 경로는 사양이 아니라 <b>착상</b>입니다. 여름에 이유두수·재귀율은 ` +
    `거의 그대로인데 임신사고 구성이 <b>1차 재발 쪽으로 ` +
    `+${{(S.acc_1st * 100).toFixed(1)}}%p</b> 기웁니다` +
    `(겨울 ${{(S.acc_winter * 100).toFixed(1)}}% → 여름 ${{(S.acc_summer * 100).toFixed(1)}}%). ` +
    `그래서 겨냥할 시점은 <b>교배 후 ${{S.implantation[0]}}~${{S.implantation[1]}}일 착상기</b>이고, ` +
    `이 구간 축사의 THI 를 낮추는 것이 처방입니다.</div>`;

  box.innerHTML = `<div class="card">` + head + body + `</div>`;
}}

function render() {{
  const p = planOf();
  $("#kpis").innerHTML =
    kpi(p.nb.toFixed(1), "배치 수", `번식주기 ${{p.cycle.toFixed(0)}}일 ÷ ${{p.iv}}일`) +
    kpi(p.perBatch.toFixed(0), "배치당 모돈", "이 수가 한 방의 크기") +
    kpi(p.farrow.toFixed(0), "배치당 분만", `분만율 ${{(p.rate * 100).toFixed(0)}}% · ${{p.rateSrc}}`) +
    kpi(p.rooms, "분만사 권장 방", `최소 ${{p.minRooms}} · 여유 ${{p.slack.toFixed(0)}}일`) +
    kpi(p.crates.toLocaleString(), "필요 분만틀", "권장 방 기준");
  $("#cyc").innerHTML =
    `점유 ${{p.occupy.toFixed(0)}}일 = 분만 전 이동 ${{p.pre.toFixed(0)}} + 포유 ` +
    `${{p.lact.toFixed(0)}} + 세척 ${{p.wash.toFixed(0)}}. ` +
    `<b>세척을 빼고 세면 방이 모자라 올인/올아웃이 무너집니다</b> — ` +
    `배칭을 하는 의미 자체가 사라집니다.`;

  // -- 검산 ------------------------------------------------------------
  const rows = [];
  const need = {{
    "분만사": Math.ceil(p.farrow) * p.rooms,
    "교배사": Math.round(p.sows * (CFG.d.wean_to_service + 28) / p.cycle),
    "임신사": Math.round(p.sows * (CFG.d.gestation - 28 - p.pre) / p.cycle),
  }};
  for (const [st, n] of Object.entries(need)) {{
    const have = capacity(st);
    const gap = have - n;
    rows.push({{st, n, have, gap}});
  }}
  const short = rows.filter(r => r.have > 0 && r.gap < 0);
  const missing = rows.filter(r => r.have === 0);
  let html = "";
  if (barns.length) {{
    const cls = short.length ? "card warn" : (missing.length ? "card" : "card good");
    html += `<div class="${{cls}}"><b style="font-size:.9rem">필요 vs 보유 자리</b><table>` +
      `<thead><tr><th>용도</th><th>필요</th><th>보유</th><th>차이</th><th>방 수</th></tr></thead><tbody>`;
    for (const r of rows) {{
      const tag = r.have === 0 ? '<span class="tag skip">미등록</span>'
        : (r.gap < 0 ? `<span class="tag err">${{r.gap}}</span>`
                     : `<span class="tag ok">+${{r.gap}}</span>`);
      html += `<tr><td>${{r.st}}</td><td>${{r.n.toLocaleString()}}</td>` +
        `<td>${{r.have.toLocaleString()}}</td><td>${{tag}}</td>` +
        `<td>${{roomsOf(r.st) || "—"}}</td></tr>`;
    }}
    html += `</tbody></table>`;
    if (short.length) {{
      html += `<div class="note"><b>부족분이 곧 병목입니다.</b> ` +
        `돈방은 돈사를 건너뛰어 쓸 수 없으므로 총량이 맞아도 배분이 틀리면 밀립니다.</div>`;
    }} else if (missing.length) {{
      html += `<div class="note">${{missing.map(r => r.st).join("·")}} 이 등록되지 않아 ` +
        `대조하지 못했습니다.</div>`;
    }}
    const fRooms = roomsOf("분만사");
    if (fRooms > 0 && fRooms < p.minRooms) {{
      html += `<div class="note" style="color:var(--bad)"><b>분만사 방이 ${{fRooms}}개인데 ` +
        `최소 ${{p.minRooms}}개가 필요합니다.</b> 이 간격으로는 AIAO 가 성립하지 않습니다.</div>`;
    }}
    html += `</div>`;
  }}
  $("#checks").innerHTML = html;

  // 포유 상한 — 방 주기에서 이동·세척을 빼고 남는 것
  const fRooms = roomsOf("분만사") || p.rooms;
  const maxLact = fRooms * p.iv - p.pre - p.wash;
  $("#h_lact").textContent = maxLact >= p.lact
    ? `분만사 ${{fRooms}}방·${{p.iv}}일 간격이면 최대 ${{maxLact.toFixed(0)}}일까지 가능`
    : `⚠ 이 방 수로는 최대 ${{maxLact.toFixed(0)}}일 — 포유를 줄이거나 방을 늘려야 합니다`;
  $("#h_lact").className = maxLact >= p.lact ? "hint" : "hint err";
  $("#h_interval").textContent =
    `배치 ${{p.nb.toFixed(1)}}개 · 1회 교배 ${{p.perBatch.toFixed(0)}}두 ` +
    `(주 평균의 ${{(p.iv / 7).toFixed(1)}}배로 몰림)`;
  $("#h_wash").textContent = p.wash < 3
    ? "⚠ 세척·건조 3일 미만은 병원체가 배치를 넘어 이어집니다"
    : "방을 비우고 씻고 말리는 기간";
  $("#h_wash").className = p.wash < 3 ? "hint err" : "hint";
  $("#h_sows").textContent = p.sows > 0
    ? `배치당 ${{p.perBatch.toFixed(0)}}두씩 ${{p.nb.toFixed(1)}}개 배치`
    : "1 이상이어야 합니다";
  const site = $("#f_site").value;
  $("#h_site").textContent =
    ({json.dumps({v: n for v, _, n in SITE_TYPES}, ensure_ascii=False)})[site] || "";

  // 발정 판정 경로
  const used = [...new Set(barns.map(b => b.housing))];
  $("#routes").innerHTML = used.length
    ? used.map(h => {{
        const r = CFG.routes[h];
        return `<div class="bnrow"><b>${{r.label}}</b>` +
          `<span class="tag">${{r.module}}</span>` +
          `<span class="cnt">${{r.signal}} · ${{r.note}}</span></div>`;
      }}).join("")
    : '<div class="hint">동을 등록하면 여기에 표시됩니다.</div>';

  // 성적 → 466농장 분포에서의 위치
  let pos = "", any = false;
  const HB = {{farrowing_rate: true, weaned: true, npd: false, wean_to_estrus: false}};
  for (const f of CFG.perf) {{
    const v = num("#p_" + f.key);
    const hint = $("#h_" + f.key);
    if (v === null) {{
      hint.textContent = "비움 → 진단에서 제외 (중앙값을 넣지 않습니다)";
      hint.className = "hint skip";
      continue;
    }}
    if (v < f.lo || v > f.hi) {{
      hint.textContent = `${{f.lo}}~${{f.hi}} 범위를 벗어났습니다`;
      hint.className = "hint err";
      continue;
    }}
    hint.textContent = ""; hint.className = "hint";
    const q = CFG.q[f.key];
    if (!q) continue;
    any = true;
    const d = v - q.p50;
    pos += `<div style="margin-bottom:14px"><b style="font-size:.85rem">${{f.label}}</b> ` +
      `<span style="color:var(--muted);font-size:.78rem">중앙값 대비 ` +
      `${{d >= 0 ? "+" : ""}}${{d.toFixed(1)}}${{f.unit}}</span>` +
      strip(q, v, f.unit, HB[f.key]) + `</div>`;
  }}
  $("#pos").innerHTML = any
    ? `<div class="card"><b style="font-size:.9rem">466농장 분포에서의 위치</b>` +
      `<div class="h2d" style="margin:4px 0 10px">순위가 아니라 <b>거리</b>입니다 — ` +
      `중앙값에서 얼마나 떨어졌는지를 봅니다.</div>${{pos}}` +
      `<div class="note">기준은 국내 202농장 × 4년 = 466행 실측입니다.</div></div>`
    : "";

  renderSeason(p);

  // 내보내기
  const args = [`--sows ${{Math.round(p.sows)}}`];
  for (const f of CFG.perf) {{
    const v = num("#p_" + f.key);
    if (v !== null && v >= f.lo && v <= f.hi) {{
      args.push(`--${{f.arg.replace(/_/g, "-")}} ${{v}}`);
    }}
  }}
  $("#out_cmd").value =
    "python competition/src/run_farm.py " + args.join(" ") + "\\n" +
    `python competition/src/batch_flow.py   # 간격 ${{p.iv}}일 · 배치 ${{p.nb.toFixed(1)}}개\\n` +
    "python competition/src/farm_gap.py --sows " + Math.round(p.sows);
  $("#out_json").value = JSON.stringify(snapshot(), null, 1);
  save();
}}

function snapshot() {{
  const perf = {{}};
  for (const f of CFG.perf) {{
    const v = num("#p_" + f.key);
    perf[f.key] = (v !== null && v >= f.lo && v <= f.hi) ? v : null;
  }}
  return {{
    name: $("#f_name").value || null,
    n_sows: num("#f_sows"), n_gilts: num("#f_gilts"),
    site_type: $("#f_site").value,
    interval_days: parseFloat($("#f_interval").value),
    lactation_days: num("#f_lact"), pre_farrow_days: num("#f_pre"),
    washout_days: num("#f_wash"),
    barns: barns.map(b => ({{...b}})),
    performance: perf,
    season: {{summer_farrowing_rate: num("#s_summer"),
              winter_farrowing_rate: num("#s_winter")}},
    note: "비어 있는 성적은 진단에서 제외한다. 중앙값을 대입하지 않는다."
  }};
}}

function save() {{
  try {{
    localStorage.setItem(KEY, JSON.stringify(snapshot()));
    $("#saved").textContent = "이 브라우저에 저장됨";
  }} catch (e) {{ $("#saved").textContent = "저장 불가(브라우저 설정)"; }}
}}

function load() {{
  let s = null;
  try {{ s = JSON.parse(localStorage.getItem(KEY) || "null"); }} catch (e) {{}}
  if (!s) return false;
  $("#f_name").value = s.name || "";
  if (s.n_sows) $("#f_sows").value = s.n_sows;
  if (s.n_gilts != null) $("#f_gilts").value = s.n_gilts;
  if (s.site_type) $("#f_site").value = s.site_type;
  if (s.interval_days) $("#f_interval").value = s.interval_days;
  if (s.lactation_days) $("#f_lact").value = s.lactation_days;
  if (s.pre_farrow_days != null) $("#f_pre").value = s.pre_farrow_days;
  if (s.washout_days != null) $("#f_wash").value = s.washout_days;
  barns = (s.barns || []).map(b => ({{...b}}));
  for (const f of CFG.perf) {{
    const v = (s.performance || {{}})[f.key];
    if (v != null) $("#p_" + f.key).value = v;
  }}
  const sz = s.season || {{}};
  if (sz.summer_farrowing_rate != null) $("#s_summer").value = sz.summer_farrowing_rate;
  if (sz.winter_farrowing_rate != null) $("#s_winter").value = sz.winter_farrowing_rate;
  return true;
}}

// -- 조립 ----------------------------------------------------------------
$("#perf").innerHTML = CFG.perf.map(f =>
  `<div><label>${{f.label}} <span class="u">${{f.unit}} · 모르면 비움</span></label>` +
  `<input id="p_${{f.key}}" type="number" step="0.1" min="${{f.lo}}" max="${{f.hi}}" placeholder="">` +
  `<div class="hint" id="h_${{f.key}}"></div></div>`).join("");
$("#f_interval").value = "21";

document.addEventListener("input", e => {{
  const t = e.target;
  if (t.dataset && t.dataset.k !== undefined) {{
    const i = +t.dataset.i, k = t.dataset.k;
    barns[i][k] = (k === "rooms" || k === "per") ? Math.max(1, +t.value || 1) : t.value;
    if (k === "rooms" || k === "per") drawBarns();
  }}
  render();
}});
document.addEventListener("change", e => {{
  const t = e.target;
  if (t.dataset && t.dataset.k !== undefined) {{
    barns[+t.dataset.i][t.dataset.k] = t.value;
    drawBarns();
  }}
  render();
}});
document.addEventListener("click", e => {{
  const del = e.target.dataset ? e.target.dataset.del : null;
  if (del !== null && del !== undefined) {{ barns.splice(+del, 1); drawBarns(); render(); }}
}});
$("#add").onclick = () => {{
  barns.push({{name: (barns.length + 1) + "동", stage: STAGES[0], rooms: 1,
               per: 20, housing: HOUSING[0][0]}});
  drawBarns(); render();
}};
$("#preset").onclick = () => {{
  barns = preset(num("#f_sows") || 300); drawBarns(); render();
}};
$("#reset").onclick = () => {{
  try {{ localStorage.removeItem(KEY); }} catch (e) {{}}
  location.reload();
}};
function copyOf(id, btn) {{
  const t = $(id); t.select();
  try {{ document.execCommand("copy"); }} catch (e) {{}}
  const old = btn.textContent; btn.textContent = "복사됨";
  setTimeout(() => {{ btn.textContent = old; }}, 1200);
}}
$("#copy_cmd").onclick = e => copyOf("#out_cmd", e.target);
$("#copy_json").onclick = e => copyOf("#out_json", e.target);

if (!load()) barns = preset(300);
drawBarns();
render();
</script></body></html>
"""


def main() -> int:
    html = build()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"농장 등록 화면 생성: {OUT} ({len(html) // 1024}KB)")
    print(f"  축사 용도 {len(fr.BARN_STAGES)}종 · 사육 방식 {len(fr.HOUSING)}종 "
          f"· 농장 형태 {len(SITE_TYPES)}종 · 성적란 {len(PERF)}개")
    p = bf.plan(300, 21.0)
    print(f"  검산 기준: batch_flow.plan(300, 21) → 배치 "
          f"{p['n_batches']:.1f}개 · 배치당 {p['sows_per_batch']:.0f}두")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
