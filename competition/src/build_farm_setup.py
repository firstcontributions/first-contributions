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
import growth_flow as gf                                      # noqa: E402
import repro_calendar as rc                                   # noqa: E402
import farm_economics as fe                                   # noqa: E402

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


def downstream_stages() -> list:
    """뒷단 3단계 — 사육일수·법정 두당면적·구간 폐사율.

    `growth_flow.STAGES` 가 원본이다. 여기서 일수를 다시 적으면 등록 화면이
    말하는 농장과 `batch_flow`·`growth_flow` 가 말하는 농장이 갈린다.
    """
    out = []
    for name, a0, a1, _w0, _w1, barn, area in gf.STAGES:
        if area is None:                      # 포유자돈은 분만사 안이라 뺀다
            continue
        out.append({"stage": barn, "label": name, "days": a1 - a0,
                    "age": [a0, a1], "area": area,
                    "mort": gf.MORTALITY.get(name, 0.0)})
    return out


def sim_stages() -> list:
    """시뮬레이터가 실제로 쓰는 흐름 단계 — 방 소요가 여기서 갈린다.

    `growth_flow` 는 자돈사를 **한 구간**(24~70일령)으로 보지만 pigflow 는
    전기·후기로 나눠 **방을 따로 쓴다**(21일 + 25일). 그러면 배치가 중간에
    한 번 옮겨 타므로 같은 46일이라도 방이 하나 더 든다. 화면이 이걸 모른 채
    3방으로 잡으면 등록은 통과하는데 돌리면 적체가 난다 — 실제로 그랬다.

    육성·비육 경계도 다르다(35/70 vs 50/55). 합은 105일로 같으므로 **어느
    쪽이 틀린 게 아니라 경계 정의가 다른 것**이고, 그래서 둘 다 보여 준다.
    """
    from pigflow.config import default_config
    ko = {"farrowing": "분만사", "nursery": "자돈사",
          "grower": "육성사", "finisher": "비육사"}
    return [{"stage": ko[s.house], "id": s.id, "label": s.name_ko,
             "days": int(s.duration_days)}
            for s in default_config().merged().flow_stages if s.house in ko]


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
           "season": sn, "down": downstream_stages(), "sim": sim_stages(),
           "washdown": bf.WASHDOWN, "market_age": gf.MARKET_AGE,
           # 역산(방 → 두수) 상수. **여기서 새로 만들지 않는다** —
           # batch_flow.capacity_from_rooms 와 같은 값이어야 하고,
           # 테스트가 브라우저에서 두 결과를 직접 대조한다.
           "cap": {"farrow_rate": bf.FARROW_RATE_P10,
                   "gilt_share": bf.GILT_SHARE,
                   "gilt_weeks": bf.GILT_PIPELINE_WEEKS,
                   "weaned_per_crate": bf.WEANED_PER_CRATE,
                   "turnover": bf.SOW_TURNOVER,
                   "gestation": bf.GESTATION,
                   "wei": rc.WEI_BY_PARITY["sow"],
                   "service_hold": bf.SERVICE_HOLD_DAYS,
                   "washdown": bf.WASHDOWN, "move_in": bf.MOVE_IN,
                   "down_days": bf.DOWNSTREAM_DAYS,
                   "grow_survival": bf.GROW_SURVIVAL,
                   "ceiling": bf.CEILING,
                   # 한 두를 더 냈을 때 남는 돈. **총원가가 아니라 한계 이익**
                   # 이다 — 돈사·모돈·인력이 이미 있는 상태에서 빈 틀을
                   # 채우는 것이라 노무비·감가상각은 안 늘어난다.
                   "margin": fe.margin_per_pig()["margin"],
                   "mort": {b: gf.MORTALITY[n]
                            for n, _a0, _a1, _w0, _w1, b, a in gf.STAGES if a}},
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

<h2>1. 규모 — 어느 쪽에서 시작합니까</h2>
<div class="h2d"><b>이미 지어진 농장이면 아래를 ‘돈사 → 두수’ 로 바꾸세요.</b>
그러면 상시모돈수를 묻지 않고, 등록한 방이 <b>몇 두를 받을 수 있는지</b>와
<b>무엇이 그걸 정하는지</b>를 대신 냅니다.</div>
<div class="card"><div class="grid">
  <div><label>계산 방향</label>
    <select id="f_dir">
      <option value="design">두수 → 돈사 (새로 설계)</option>
      <option value="reverse">돈사 → 두수 (이미 지어진 농장)</option>
    </select><div class="hint" id="h_dir"></div></div>
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

<h2>2. 운영 방식</h2>
<div class="h2d">배치 간격이 방 수와 이유일령을 동시에 정합니다 —
<b>돈사를 등록하기 전에 먼저 정해야 필요 방 수가 나옵니다.</b></div>
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

<h2>3. 돈사 등록</h2>
<div class="h2d">여기가 이 화면의 본론입니다. 동을 추가하고 <b>용도·방 수·방당
자리·방당 면적·사육 방식</b>을 넣으면, 바로 아래에서 <b>번식사부터 출하까지</b>
필요 자리·AIAO 방 수·법정 사육밀도를 한꺼번에 대조합니다.
사육 방식은 발정 판정 경로까지 정합니다.</div>
<div class="card">
<table><thead><tr><th>동 이름</th><th>용도</th><th>방 수</th>
<th>방당 자리</th><th>방당 면적<span class="u"> ㎡</span></th>
<th>사육 방식</th><th>자리 합</th><th>두당 면적</th><th></th></tr></thead>
<tbody id="barns"></tbody></table>
<div class="row"><button id="add">+ 동 추가</button>
<button class="pri" id="preset">일관농장 기본 구성 넣기</button>
<span class="hint" id="h_barns" style="margin:0"></span></div>
<div class="note"><b>면적은 비워도 됩니다</b> — 비우면 밀사 판정만 못 합니다.
자리 수에서 되돌려 채우지 않습니다. 역산한 면적은 정의상 법정 기준에 딱
맞아서 <b>어떤 농장도 과밀로 안 잡히기</b> 때문입니다.</div>
<div class="note" style="margin-top:6px">용도별 정의 — 이 어휘는
<code>farm_registry.BARN_STAGES</code> 와 같습니다. 화면에서 새 낱말을 만들면
코드와 갈라집니다. 뒷단 3단계는 <code>growth_flow.STAGES</code> 의 일령
구간과 1:1 입니다.</div>
<div style="margin-top:8px">{stage_desc}</div>
</div>
<div id="cap"></div>
<div id="top"></div>
<div id="checks"></div>
<div class="card"><b style="font-size:.9rem">발정 판정 경로</b>
<div class="h2d" style="margin:4px 0 8px">등록한 사육 방식에서 따라 나옵니다.</div>
<div id="routes"></div></div>

<h2>4. 성적 — 아는 것만</h2>
<div class="h2d"><b>비운 칸은 중앙값으로 채우지 않고 진단에서 뺍니다.</b>
중앙값을 넣으면 그 항목의 격차가 늘 0 으로 찍힙니다 — 실제로 겪은 버그입니다.</div>
<div class="card"><div class="grid" id="perf"></div>
<div class="grid" style="margin-top:13px">
  <div><label>이유후 육성률 <span class="u">% · 모르면 비움</span></label>
    <input id="p_survival" type="number" step="0.1" min="50" max="100" placeholder="">
    <div class="hint" id="h_survival"></div></div>
</div>
<div class="note"><b>육성률은 <code>run_farm</code> 인자가 아닙니다</b> —
생산량 상한 계산과 JSON 내보내기에만 씁니다. 명령줄에는 넣지 않습니다.</div>
</div>

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
//
// **뒷단(자돈·육성·비육)도 같은 이유로 배치 설계에서 나온다.** 예전 기본
// 구성은 번식사 넷에서 끝났는데, 그러면 등록만으로는 병목이 안 보인다 —
// batch_flow 가 잡아낸 육성사 여유 0일이 화면에 한 번도 안 뜨는 것이다.
//
// 면적은 **일부러 비워 둔다.** 자리 수 × 법정면적으로 채우면 정의상 늘
// '적정' 이라 밀사 판정이 무의미해진다.
function preset(sows) {{
  const cyc = CFG.cycle_base, d = CFG.d;
  const mate = Math.round(sows * (d.wean_to_service + 28) / cyc);
  const gest = Math.round(sows * (d.gestation - 28 - d.pre_farrow) / cyc);
  const p = planOf({{sows: sows}});
  const out = [
    {{name: "1동", stage: "교배사", rooms: 1, per: mate, area: null, housing: "stall"}},
    {{name: "2동", stage: "임신사", rooms: 2, per: Math.ceil(gest / 2), area: null, housing: "group"}},
    {{name: "3동", stage: "분만사", rooms: p.rooms, per: Math.ceil(p.farrow), area: null, housing: "crate"}},
    {{name: "4동", stage: "후보사", rooms: 1, per: Math.max(4, Math.round(sows * 0.05)), area: null, housing: "group"}},
  ];
  // **둘 중 큰 쪽으로 짓는다.** 정적 계산만 따르면 등록은 통과하는데
  // 돌리면 적체가 난다(자돈사 3방 → 적체 55회). 통과하는 기본 구성을
  // 주는 게 이 버튼의 존재 이유다.
  const sim = simRooms(p.iv, p.wash);
  downPlan(p).forEach((r, i) => out.push({{
    name: (5 + i) + "동", stage: r.stage,
    rooms: Math.max(r.minRooms, sim[r.stage] || 0),
    per: r.perRoom, area: null, housing: "pen"}}));
  return out;
}}

// 뒷단 단계별 입식두수·필요 방·여유 — batch_flow.downstream 과 같은 식.
//   점유 = 사육일수 + 세척 · 최소 방 = ceil(점유 / 간격)
//   여유 = 방 × 간격 − 점유   (0 이면 세척 당일 바로 넣어야 한다는 뜻)
// 단계 폐사는 **그 단계 안에서** 나므로 다음 단계 입식은 곱해서 준다.
//
// **첫 단계 기간은 포유기간에 딸려 움직인다.** growth_flow 는 28일 이유를
// 전제로 자돈사를 28~70일령으로 두는데, 21일 이유로 당기면 자돈사가 7일
// 길어진다 — 출하일령은 그대로이므로 앞에서 던 날이 뒤로 넘어갈 뿐이다.
function downPlan(p) {{
  const wPer = num("#p_weaned");
  // **분만복수를 올림한 뒤에 곱한다.** 안 올리면 35.3복 × 11두 = 388두가
  // 나오는데 시뮬레이터는 분만틀 36개로 396두를 만들어, 8두 차이로 방이
  // 안 들어가고 배치가 한 발짝도 못 간다. 분만사 자리를 올림해 잡는 것과
  // 같은 이유다 — 방은 최대 배치를 받아야 한다.
  let head = Math.ceil(p.farrow) * (wPer ?? CFG.d.weaned);   // 배치당 이유두수
  const src = (wPer !== null) ? "입력값" : "설계 가정";
  return CFG.down.map((s, i) => {{
    const a0 = (i === 0) ? p.lact : s.age[0];
    const days = Math.max(1, s.age[1] - a0);
    const occupy = days + p.wash;
    const minRooms = Math.max(1, Math.ceil(occupy / p.iv));
    const perRoom = Math.ceil(head);
    const row = {{stage: s.stage, label: s.label, age: [a0, s.age[1]], days,
                 area: s.area, head, perRoom, occupy, minRooms, src,
                 shift: days - s.days, need: perRoom * minRooms}};
    head = head * (1 - s.mort);
    return row;
  }});
}}

let barns = [];

function opts(list, sel) {{
  return list.map(o => {{
    const [v, t] = Array.isArray(o) ? o : [o, o];
    return `<option value="${{v}}"${{v === sel ? " selected" : ""}}>${{t}}</option>`;
  }}).join("");
}}

// 법정 두당면적 — growth_flow.STAGES 에서 온다. 번식사는 시행령에 두당
// 면적 기준이 없어 판정하지 않는다(빈칸으로 둔다).
const LEGAL = Object.fromEntries(CFG.down.map(s => [s.stage, s.area]));

// 시뮬레이터 방 소요 — 하위 단계마다 방을 따로 쓴다.
// 자돈사는 전기·후기로 나뉘어 46일 한 구간으로 잡을 때보다 방이 더 든다.
function simRooms(iv, wash) {{
  const out = {{}};
  for (const s of CFG.sim) {{
    out[s.stage] = (out[s.stage] || 0) + Math.max(1, Math.ceil((s.days + wash) / iv));
  }}
  return out;
}}

function density(b) {{
  const need = LEGAL[b.stage];
  if (!need) return {{tag: "", txt: "—"}};
  if (!b.area) return {{tag: "skip", txt: "면적 미입력"}};
  const per = b.area / Math.max(1, b.per);
  const ok = per >= need - 1e-9;
  return {{tag: ok ? "ok" : "err",
          txt: `${{per.toFixed(2)}}㎡ / 기준 ${{need}}`,
          over: ok ? 0 : Math.ceil(b.per - b.area / need)}};
}}

function drawBarns() {{
  const tb = $("#barns"); tb.innerHTML = "";
  barns.forEach((b, i) => {{
    const dn = density(b);
    const tr = el("tr");
    tr.innerHTML =
      `<td><input data-i="${{i}}" data-k="name" value="${{b.name}}" style="min-width:74px"></td>` +
      `<td><select data-i="${{i}}" data-k="stage">${{opts(STAGES, b.stage)}}</select></td>` +
      `<td><input data-i="${{i}}" data-k="rooms" type="number" min="1" max="99" value="${{b.rooms}}" style="width:64px"></td>` +
      `<td><input data-i="${{i}}" data-k="per" type="number" min="1" max="9999" value="${{b.per}}" style="width:74px"></td>` +
      `<td><input data-i="${{i}}" data-k="area" type="number" min="0" step="0.1" value="${{b.area ?? ""}}" placeholder="비움" style="width:74px"></td>` +
      `<td><select data-i="${{i}}" data-k="housing">${{opts(HOUSING, b.housing)}}</select></td>` +
      `<td><b>${{(b.rooms * b.per).toLocaleString()}}</b></td>` +
      `<td>${{dn.tag ? `<span class="tag ${{dn.tag}}">${{dn.txt}}</span>` : dn.txt}}` +
      `${{dn.over ? `<div class="hint err">초과 ${{dn.over}}두</div>` : ""}}</td>` +
      `<td><button class="x" data-del="${{i}}">삭제</button></td>`;
    tb.appendChild(tr);
  }});
  if (!barns.length) {{
    const tr = el("tr");
    tr.innerHTML = '<td colspan="9" style="color:var(--muted);font-size:.82rem">' +
      '등록된 동이 없습니다. “일관농장 기본 구성 넣기” 로 시작해 보세요.</td>';
    tb.appendChild(tr);
  }}
}}

function num(id) {{ const v = parseFloat($(id).value); return isFinite(v) ? v : null; }}

// ── 역산: 지어 놓은 방 → 넣을 수 있는 개체 수 ─────────────────────────
//
// batch_flow.capacity_from_rooms 를 그대로 옮긴 것이다. 상수는 CFG.cap 으로
// 파이썬에서 받아오고, 테스트가 브라우저에서 두 결과를 직접 대조한다 —
// 화면과 모듈이 다른 두수를 말하면 그 자리에서 깨진다.

// 파이썬 round() 는 .5 에서 짝수로 간다(JS Math.round 는 위로). 두 결과를
// 대조하는 함수라 이 차이를 그냥 두면 안 된다.
function rnd(x) {{
  const f = Math.floor(x);
  if (Math.abs(x - f - 0.5) > 1e-9) return Math.round(x);
  return (f % 2 === 0) ? f : f + 1;
}}

function planFromCrates(n, iv, wPer) {{
  const C = CFG.cap, w = iv / 7;
  wPer = wPer || C.weaned_per_crate;
  const services = Math.ceil(n / Math.max(0.05, C.farrow_rate));
  const gilts = Math.ceil(services * C.gilt_share);
  const breeding = n * (52 / w) / Math.max(0.1, C.turnover);
  return {{services, gilts, breeding: rnd(breeding),
          herd: rnd(breeding + gilts * C.gilt_weeks),
          weaned: n * wPer}};
}}

// wPer 는 **방을 지을 때 쓴 값과 같아야 한다.** batch_flow 기본값 12.0 은
// 설계 *목표*고 모델값은 11.0 이다. 목표로 되읽으면 396자리 자돈사가
// 33분만틀로 보이는데 지을 때는 36으로 잡았다 — 같은 돈사가 방향에 따라
// 다른 크기로 나온다.
function capacityFromRooms(iv, lact, pre, wash, extra, wPer) {{
  const C = CFG.cap;
  extra = extra || {{}};
  wPer = wPer || C.weaned_per_crate;
  const cycle = C.gestation + Math.round(lact) + C.wei;

  const have = {{}};
  for (const b of barns) {{
    const d = have[b.stage] || (have[b.stage] = {{rooms: 0, per: 0, places: 0}});
    d.rooms += b.rooms;
    d.per = Math.max(d.per, b.per);        // 배치는 **한 방**에 들어간다
    d.places += b.rooms * b.per;
  }}

  const rows = [];
  const f = have["분만사"];
  if (f) {{
    const need = Math.max(Math.ceil((pre + Math.round(lact) + wash) / iv),
                          extra["분만사"] || 0);
    rows.push({{stage: "분만사", kind: "AIAO", rooms: f.rooms, need_rooms: need,
               per: f.per, crates: f.rooms >= need ? f.per : 0,
               why: f.rooms >= need ? null : `방 ${{f.rooms}}개 < 필요 ${{need}}개`}});
  }}

  // 뒷단 — 단계 폐사를 빼며 내려가므로 분만틀당 두수가 단계마다 다르다
  let head = wPer;
  for (const [st, days] of Object.entries(C.down_days)) {{
    const h = have[st], perCrate = head;
    head *= 1 - (C.mort[st] || 0);
    if (!h) continue;
    const need = Math.max(Math.ceil((days + wash) / iv), extra[st] || 0);
    const ok = h.rooms >= need;
    rows.push({{stage: st, kind: "AIAO", rooms: h.rooms, need_rooms: need,
               per: h.per, crates: ok ? Math.floor(h.per / perCrate) : 0,
               sigma: perCrate / Math.max(1e-9, wPer),
               why: ok ? null : `방 ${{h.rooms}}개 < 필요 ${{need}}개`}});
  }}

  // 번식 축사 — 연속 흐름이라 방 수가 아니라 자리 총합이 제약이다
  for (const [st, hold] of [["교배사", C.wei + C.service_hold],
                            ["임신사", C.gestation - C.service_hold - pre]]) {{
    const h = have[st];
    if (!h || hold <= 0) continue;
    rows.push({{stage: st, kind: "연속", rooms: h.rooms, need_rooms: null,
               per: h.places, sows: Math.floor(h.places * cycle / hold),
               why: null}});
  }}

  for (const r of rows) {{
    if (r.sows === undefined) {{
      r.sows = r.crates > 0 ? planFromCrates(r.crates, iv, wPer).herd : 0;
    }}
  }}
  const live = rows.filter(r => r.sows > 0);
  const blocked = rows.filter(r => r.why);
  // **막힌 돈사가 병목이다.** 막힌 곳은 지지 두수 0 이라 live 에서 빠지는데,
  // 그러면 그다음으로 작은 돈사가 병목으로 뽑혀 틀린 처방이 나간다.
  let binding = null, n_sows = 0, crates = 0;
  if (blocked.length) {{
    binding = blocked[0].stage;
  }} else if (live.length) {{
    const b = live.reduce((a, x) => x.sows < a.sows ? x : a);
    binding = b.stage; n_sows = b.sows;
    crates = Math.min(...rows.filter(r => r.crates).map(r => r.crates));
  }}
  // **방이 복당 이유두수의 상한도 정한다.** 방 하나가 배치 하나를 받으므로
  // 분만틀 × 복당이유 × σ ≤ 방당 자리. 설계 목표 12두를 그냥 상한으로 쓰면
  // 방이 넘치는 생산량을 "낼 수 있다" 고 말하게 된다.
  const caps = rows.filter(r => r.sigma && crates)
                   .map(r => r.per / (crates * r.sigma));
  return {{rows, blocked, binding, n_sows, crates, interval_days: iv,
          weaned_per_crate: wPer,
          weaned_ceiling: caps.length ? +Math.min(...caps).toFixed(2) : null,
          flows: blocked.length === 0}};
}}

// batch_flow.throughput 을 그대로 옮긴 것이다. 한 줄 항등식이고, 곱하는
// 넷 말고는 아무것도 안 들어간다:
//   연간 출하 = 분만틀 × 채움률 × 복당 이유두수 × 육성률 × 연간 배치수
// 앞의 둘은 **지어 놓은 것**이라 성적으로 못 바꾼다. 나머지 셋이 길이다.
function throughput(cap, fr, wl, gs) {{
  const C = CFG.cap, T = C.ceiling;
  const crates = cap.crates || 0;
  const perYear = 365 / (cap.interval_days || 1);
  fr = (fr === null || fr === undefined) ? C.farrow_rate : fr;
  wl = (wl === null || wl === undefined)
    ? (cap.weaned_per_crate || C.weaned_per_crate) : wl;
  gs = (gs === null || gs === undefined) ? C.grow_survival : gs;
  const fill = Math.min(1, fr / C.farrow_rate);
  // 복당 이유두수 상한은 **설계 목표와 방 중 작은 쪽**이다
  const roomCap = cap.weaned_ceiling;
  const topW = roomCap ? Math.min(T.weaned, roomCap) : T.weaned;
  const roomBound = !!roomCap && roomCap < T.weaned;
  const out = (f, w, s) => crates * f * w * s * perYear;
  const now = out(fill, wl, gs), top = out(T.fill, topW, T.survival);

  const ways = [
    {{key: "fill", name: "빈 분만틀 채우기", unit: "%",
     now: +(fill * 100).toFixed(1), target: 100,
     how: `분만율 ${{(fr * 100).toFixed(1)}}% → ${{(C.farrow_rate * 100).toFixed(0)}}% ` +
          `(설계 기준). 발정 탐지·적기 교배`,
     gain: out(T.fill, wl, gs) - now}},
    {{key: "weaned", name: "복당 이유두수", unit: "두",
     now: +wl.toFixed(1), target: +topW.toFixed(1),
     how: "포유 폐사 감소 · 포유능력 · 양자보내기" + (roomBound
       ? ` — 방이 ${{topW.toFixed(1)}}두에서 막습니다(목표 ${{T.weaned}}두)` : ""),
     gain: out(fill, topW, gs) - now}},
    {{key: "survival", name: "이유후 육성률", unit: "%",
     now: +(gs * 100).toFixed(1), target: T.survival * 100,
     how: "AIAO · 밀도 · 환경 — 자돈사 이행항체 최저점 구간",
     gain: out(fill, wl, T.survival) - now}},
  ];
  for (const w of ways) {{
    w.gain = rnd(Math.max(0, w.gain));
    w.at_target = w.now >= w.target - 1e-9;
  }}
  return {{crates, batches_per_year: +perYear.toFixed(1),
          binding: cap.binding, flows: cap.flows,
          factors: {{fill: +fill.toFixed(4), weaned: wl, survival: gs}},
          top_weaned: +topW.toFixed(2), weaned_room_bound: roomBound,
          now_year: rnd(now), ceiling_year: rnd(top),
          gap_year: rnd(top - now),
          achieved: top ? +(now / top).toFixed(3) : null, ways,
          sum_of_ways: ways.reduce((a, w) => a + w.gain, 0)}};
}}

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

// 역산 결과 카드. **두수 하나만 크게 쓰지 않는다** — 이 계산의 답은
// 두수가 아니라 병목의 이름이다. 두수만 보면 "그럼 300두 키우면 되겠네"
// 로 끝나고, 정작 무엇을 고쳐야 하는지는 안 남는다.
function renderCap(cap) {{
  const box = $("#cap");
  if (!cap) {{ box.innerHTML = ""; return; }}
  if (!barns.length) {{
    box.innerHTML = `<div class="card"><div class="hint">돈사를 등록하면 ` +
      `받을 수 있는 두수가 여기 나옵니다.</div></div>`;
    return;
  }}
  const cls = cap.flows ? (cap.n_sows > 0 ? "card good" : "card") : "card warn";
  let h = `<div class="${{cls}}"><b style="font-size:.9rem">이 돈사가 받는 규모` +
    `</b><div class="h2d" style="margin:4px 0 8px">돈사마다 지지할 수 있는 ` +
    `규모를 따로 내고 <b>가장 작은 것</b>을 취합니다. 돈방은 돈사를 건너뛰어 ` +
    `쓸 수 없어서, 총량이 커도 한 곳이 막히면 거기서 끝납니다.</div>`;

  if (!cap.flows) {{
    h += `<div class="note" style="color:var(--bad)"><b>두수를 말하기 전에 ` +
      `막힌 곳이 있습니다 — ${{cap.blocked.map(r => `${{r.stage}}(${{r.why}})`)
        .join(" · ")}}.</b> 자리가 남아도 회전이 안 되면 배치가 밀립니다. ` +
      `<b>두수를 줄여도 안 풀립니다</b> — 방을 늘리거나 간격을 넓혀야 합니다.</div>`;
  }} else {{
    h += `<div class="kpis">` +
      kpi(`${{cap.n_sows.toLocaleString()}}두`, "받을 수 있는 상시모돈",
          `병목: ${{cap.binding}}`) +
      kpi(`${{cap.crates}}`, "배치당 분만틀", "방 하나가 배치 하나") +
      kpi(`${{Math.round(planFromCrates(cap.crates,
            parseFloat($("#f_interval").value),
            num("#p_weaned") ?? CFG.d.weaned).weaned).toLocaleString()}}두`,
          "배치당 이유",
          `복당 ${{(num("#p_weaned") ?? CFG.d.weaned).toFixed(1)}}두 · ` +
          `${{num("#p_weaned") !== null ? "입력값" : "설계 가정"}}`) +
      `</div>`;
  }}

  h += `<table><thead><tr><th>용도</th><th>세는 법</th><th>방</th>` +
    `<th>필요 방</th><th>방당/자리</th><th>지지 모돈</th></tr></thead><tbody>`;
  for (const r of cap.rows) {{
    const isBind = r.stage === cap.binding;
    h += `<tr><td>${{isBind ? `<b>${{r.stage}}</b> ` +
        `<span class="tag err">병목</span>` : r.stage}}</td>` +
      `<td>${{r.kind}}</td><td>${{r.rooms}}</td>` +
      `<td>${{r.need_rooms === null ? "—" : (r.why
        ? `<span class="tag err">${{r.need_rooms}}</span>` : r.need_rooms)}}</td>` +
      `<td>${{r.per.toLocaleString()}}</td>` +
      `<td>${{r.sows ? r.sows.toLocaleString() + "두" : "—"}}</td></tr>`;
  }}
  h += `</tbody></table>`;
  h += `<div class="note"><b>답은 두수가 아니라 병목의 이름입니다.</b> ` +
    `${{cap.binding ? `${{cap.binding}} 를 넓히기 전까지는 다른 돈사를 키워도 ` +
      `두수가 안 늘어납니다.` : ""}} 지지 모돈은 ` +
    `<code>batch_flow.capacity_from_rooms</code> 와 같은 식이고, 분만틀 → ` +
    `모돈 환산은 존 카 모델(분만율 하위10분위 ${{(CFG.cap.farrow_rate * 100)
      .toFixed(0)}}% · 회전율 ${{CFG.cap.turnover}})입니다.</div></div>`;
  box.innerHTML = h;
}}

// 생산량 상한과 거기까지 가는 길. **두수를 크게 쓰고 끝내지 않는다** —
// 상한은 지어 놓은 것이 정하고, 농장이 움직일 수 있는 건 셋뿐이다.
function renderTop(cap) {{
  const box = $("#top");
  if (!cap || !barns.length || !cap.flows || !cap.crates) {{
    box.innerHTML = ""; return;
  }}
  const t = throughput(cap, num("#p_farrowing_rate") === null ? null
                              : num("#p_farrowing_rate") / 100,
                       num("#p_weaned"),
                       num("#p_survival") === null ? null
                              : num("#p_survival") / 100);
  const given = (num("#p_farrowing_rate") !== null || num("#p_weaned") !== null
                 || num("#p_survival") !== null);
  const won = g => (g * CFG.cap.margin / 1e4);
  const pct = Math.round(t.achieved * 100);

  let h = `<div class="card"><b style="font-size:.9rem">이 돈사의 연간 최대 ` +
    `출하두수</b><div class="h2d" style="margin:4px 0 8px">` +
    `연간 출하 = <b>분만틀 × 채움률 × 복당 이유두수 × 육성률 × 연간 배치수</b>. ` +
    `앞의 둘은 지어 놓은 것이라 성적으로 못 바꿉니다 — 나머지 셋이 길입니다.</div>`;

  h += `<div class="kpis">` +
    kpi(`${{t.ceiling_year.toLocaleString()}}두`, "연간 상한",
        `분만틀 ${{t.crates}} × 배치 ${{t.batches_per_year}}회/년`) +
    kpi(`${{t.now_year.toLocaleString()}}두`, given ? "지금 성적으로" : "설계 기준으로",
        given ? `상한의 ${{pct}}%` : "성적을 넣으면 우리 값으로 바뀝니다") +
    kpi(`${{t.gap_year.toLocaleString()}}두`, "상한까지 남은 몫",
        `연 ${{won(t.gap_year).toLocaleString(undefined, {{maximumFractionDigits: 0}})}}만원`) +
    `</div>`;

  // 달성률 막대 — 상한은 물리량이라 100% 가 진짜 끝이다
  h += `<div class="strip" style="height:30px"><div class="band" ` +
    `style="left:0;width:100%"></div><div class="band2" ` +
    `style="left:0;width:${{Math.max(0, Math.min(100, pct))}}%;` +
    `background:color-mix(in srgb,var(--good) 55%,var(--surface2))"></div>` +
    `<div class="lb" style="left:${{Math.max(6, Math.min(96, pct))}}%">` +
    `달성 ${{pct}}%</div><div class="lb" style="left:98%">상한</div></div>`;

  h += `<table style="margin-top:16px"><thead><tr><th>상한까지 가는 길</th>` +
    `<th>지금</th><th>설계 기준</th><th>이것만 올리면</th><th>원/년</th>` +
    `</tr></thead><tbody>`;
  for (const w of [...t.ways].sort((a, b) => b.gain - a.gain)) {{
    h += `<tr><td><b>${{w.name}}</b><div class="hint">${{w.how}}</div></td>` +
      `<td>${{w.now}}${{w.unit}}</td><td>${{w.target}}${{w.unit}}</td>` +
      `<td>${{w.at_target ? '<span class="tag ok">도달</span>'
        : `<b>+${{w.gain.toLocaleString()}}두</b>`}}</td>` +
      `<td>${{w.at_target ? "—" : won(w.gain).toLocaleString(undefined,
        {{maximumFractionDigits: 0}}) + "만원"}}</td></tr>`;
  }}
  h += `</tbody></table>`;

  if (!given) {{
    h += `<div class="note" style="color:var(--warn)"><b>성적을 하나도 안 ` +
      `넣어서 ‘지금’ 은 우리 농장 값이 아닙니다</b> — 설계 기준으로 돌린 것이라 ` +
      `상한과 같게 나옵니다. 4번에 분만율·이유두수·육성률을 넣으면 ` +
      `우리 격차로 바뀝니다.</div>`;
  }}
  // **합치지 않는다.** 네 항이 곱해지므로 개별 몫의 합 ≠ 총 격차다.
  h += `<div class="note"><b>세 몫을 더하지 마세요.</b> 항이 곱해지므로 ` +
    `개별 합 ${{t.sum_of_ways.toLocaleString()}}두 ≠ 총 격차 ` +
    `${{t.gap_year.toLocaleString()}}두 입니다. 각 몫은 <b>그것 하나만</b> ` +
    `설계 기준까지 올렸을 때의 값입니다.</div>`;
  h += `<div class="note">상한을 더 올리려면 성적이 아니라 <b>돈사</b>를 ` +
    `늘려야 합니다 — 지금 상한을 붙잡고 있는 건 <b>${{t.binding}}</b> 입니다. ` +
    `원/년은 <b>한계 이익 ${{CFG.cap.margin.toLocaleString()}}원/두</b> 기준이라 ` +
    `사료·약품·수송만 뺐습니다. 돈사를 새로 짓는 판단에는 쓸 수 없습니다 ` +
    `(감가상각·노무비가 같이 늡니다).</div></div>`;
  box.innerHTML = h;
}}

function render() {{
  // 역산 모드는 모돈수를 **묻지 않고 낸다.** 그래서 planOf 보다 먼저 돈다.
  const dir = $("#f_dir").value;
  // 생산량 상한은 **두 모드 모두** 낸다 — 등록한 돈사가 무엇을 낼 수 있는지는
  // 어느 방향으로 들어왔든 알아야 하는 값이다.
  let cap = null;
  if (barns.length) {{
    const iv = parseFloat($("#f_interval").value);
    const wash = num("#f_wash") ?? CFG.d.washout;
    cap = capacityFromRooms(iv, num("#f_lact") ?? CFG.d.lactation,
                   num("#f_pre") ?? CFG.d.pre_farrow, wash, simRooms(iv, wash),
                   num("#p_weaned") ?? CFG.d.weaned);
  }}
  if (dir === "reverse" && cap && cap.n_sows > 0) $("#f_sows").value = cap.n_sows;
  $("#f_sows").disabled = (dir === "reverse");
  $("#h_dir").textContent = dir === "reverse"
    ? "상시모돈수는 등록한 방에서 나옵니다 — 직접 못 고칩니다"
    : "상시모돈수에서 필요한 돈사를 역산합니다";
  renderCap(dir === "reverse" ? cap : null);
  renderTop(cap);

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

  // -- 돈사 검사 --------------------------------------------------------
  // 예전에는 번식사 셋(분만·교배·임신)만 봤다. 그러면 등록만으로는 뒷단
  // 병목이 안 보인다 — batch_flow 가 잡은 육성사 여유 0일이 화면에 한 번도
  // 안 뜬다. 그래서 **출하까지** 같은 표에 놓는다.
  //
  // 앞단과 뒷단은 세는 방식이 다르다:
  //   교배사·임신사  연속 흐름 — 자리 = 모돈 × (머무는 일수 / 번식주기)
  //   분만사·뒷단    AIAO — 방 하나가 배치 하나를 통째로 받는다
  const dn = downPlan(p);
  const sim = simRooms(p.iv, p.wash);
  const rows = [
    {{st: "교배사", need: Math.round(p.sows * (CFG.d.wean_to_service + 28) / p.cycle),
      kind: "연속", note: `이유~교배 후 4주`}},
    {{st: "임신사", need: Math.round(p.sows * (CFG.d.gestation - 28 - p.pre) / p.cycle),
      kind: "연속", note: `교배 4주~분만 ${{p.pre.toFixed(0)}}일 전`}},
    {{st: "분만사", need: Math.ceil(p.farrow) * p.rooms, kind: "AIAO",
      minRooms: p.minRooms, occupy: p.occupy,
      note: `분만 ${{Math.ceil(p.farrow)}}복 × ${{p.rooms}}방`}},
  ];
  for (const r of dn) {{
    rows.push({{st: r.stage, need: r.need, kind: "AIAO", minRooms: r.minRooms,
                occupy: r.occupy, perRoom: r.perRoom, days: r.days,
                note: `${{r.label}} ${{r.age[0]}}~${{r.age[1]}}일령 · ${{r.days}}일 · ` +
                      `입식 ${{Math.ceil(r.head)}}두` +
                      (r.shift ? ` <b>(이유 ${{p.lact.toFixed(0)}}일령이라 ` +
                                 `${{r.shift > 0 ? "+" : ""}}${{r.shift}}일)</b>` : "")}});
  }}

  let html = "", worst = null;
  if (barns.length) {{
    for (const r of rows) {{
      r.have = capacity(r.st);
      r.rooms = roomsOf(r.st);
      r.gap = r.have - r.need;
      // 여유 일수 — AIAO 단계만. 방 × 간격 − 점유. 0 이면 세척이 끝나는
      // 그날 바로 넣어야 한다는 뜻이라 하루만 밀려도 앞이 막힌다.
      r.slack = (r.kind === "AIAO" && r.rooms > 0)
        ? r.rooms * p.iv - r.occupy : null;
      // 시뮬레이터는 하위 단계마다 방을 따로 쓴다 — 더 빡빡한 쪽이 기준이다
      r.sim = sim[r.st] || 0;
      r.needRooms = Math.max(r.minRooms || 0, r.sim);
      // 방이 더 들면 자리도 더 든다 — 필요량을 큰 쪽 방 수로 다시 낸다
      if (r.perRoom && r.needRooms > r.minRooms) r.need = r.perRoom * r.needRooms;
      r.gap = r.have - r.need;
      r.bad = r.have > 0 && (r.gap < 0 || (r.needRooms && r.rooms < r.needRooms));
      if (r.bad && (!worst || r.gap < worst.gap)) worst = r;
    }}
    const short = rows.filter(r => r.bad);
    const tight = rows.filter(r => !r.bad && r.slack !== null && r.slack < 3);
    const missing = rows.filter(r => r.have === 0);
    const cls = short.length ? "card warn"
      : (missing.length ? "card" : (tight.length ? "card" : "card good"));
    html += `<div class="${{cls}}"><b style="font-size:.9rem">돈사 검사 — ` +
      `번식사부터 출하까지</b>` +
      `<div class="h2d" style="margin:4px 0 8px">배치 ${{p.perBatch.toFixed(0)}}두 · ` +
      `간격 ${{p.iv}}일 · 세척 ${{p.wash.toFixed(0)}}일 기준. 뒷단 필요 자리는 ` +
      `이유두수 ${{dn.length ? Math.ceil(dn[0].head) : 0}}두(${{dn.length ? dn[0].src : "—"}})에서 ` +
      `단계 폐사를 빼며 내려갑니다.</div><table>` +
      `<thead><tr><th>용도</th><th>세는 법</th><th>필요</th><th>보유</th>` +
      `<th>차이</th><th>방(보유/최소)</th><th>시뮬</th><th>여유</th></tr></thead><tbody>`;
    for (const r of rows) {{
      const tag = r.have === 0 ? '<span class="tag skip">미등록</span>'
        : (r.gap < 0 ? `<span class="tag err">${{r.gap.toLocaleString()}}</span>`
                     : `<span class="tag ok">+${{r.gap.toLocaleString()}}</span>`);
      const rm = r.needRooms
        ? `${{r.rooms || "—"}} / ${{r.needRooms}}` + (r.rooms && r.rooms < r.needRooms
            ? ' <span class="tag err">부족</span>' : "")
        : (r.rooms || "—");
      // 시뮬 소요가 정적 계산보다 크면 그 차이가 곧 '돌리면 나는 적체' 다
      const sm = !r.sim ? "—"
        : (r.sim > (r.minRooms || 0) ? `<span class="tag">${{r.sim}} ↑</span>` : r.sim);
      const sl = r.slack === null ? "—"
        : (r.slack < 0 ? `<span class="tag err">${{r.slack.toFixed(0)}}일</span>`
          : (r.slack < 3 ? `<span class="tag skip">${{r.slack.toFixed(0)}}일</span>`
                         : `${{r.slack.toFixed(0)}}일`));
      html += `<tr><td><b>${{r.st}}</b><div class="hint">${{r.note}}</div></td>` +
        `<td>${{r.kind}}</td><td>${{r.need.toLocaleString()}}</td>` +
        `<td>${{r.have.toLocaleString()}}</td><td>${{tag}}</td>` +
        `<td>${{rm}}</td><td>${{sm}}</td><td>${{sl}}</td></tr>`;
    }}
    html += `</tbody></table>`;
    // 시뮬 소요가 더 큰 이유는 둘 중 하나다. 뭉뚱그리면 둘 다 틀리게 읽힌다.
    const up = rows.filter(r => r.sim > (r.minRooms || 0));
    if (up.length) {{
      const why = up.map(r => {{
        const sub = CFG.sim.filter(s => s.stage === r.st);
        if (sub.length > 1) {{
          return `<b>${{r.st}}</b> — 전·후기로 나뉘어 방을 따로 씁니다` +
            `(${{sub.map(s => `${{s.label}} ${{s.days}}일`).join(" + ")}}). ` +
            `배치가 중간에 한 번 옮겨 타므로 같은 ${{r.days}}일이라도 방이 더 듭니다`;
        }}
        return `<b>${{r.st}}</b> — 구간 경계 정의가 다릅니다` +
          `(시뮬 ${{sub[0].days}}일 vs 일령구간 ${{r.days}}일). ` +
          `육성·비육 합은 105일로 같고 나누는 지점만 다릅니다`;
      }}).join("<br>");
      html += `<div class="note">‘시뮬’ 칸이 더 큰 곳:<br>${{why}}<br>` +
        `일령 구간으로만 세면 등록은 통과하는데 돌리면 적체가 납니다 — ` +
        `그래서 <b>필요 방·필요 자리는 둘 중 큰 쪽</b>으로 냅니다.</div>`;
    }}

    if (short.length) {{
      html += `<div class="note" style="color:var(--bad)"><b>여기서 흐름이 막힙니다 — ` +
        `${{short.map(r => r.st).join("·")}}.</b> 돈방은 돈사를 건너뛰어 쓸 수 없으므로 ` +
        `총 자리가 맞아도 배분이 틀리면 밀립니다. 뒷단이 막히면 앞으로 거슬러 올라가 ` +
        `분만사까지 멈춥니다.</div>`;
    }} else if (tight.length) {{
      html += `<div class="note"><b>${{tight.map(r => r.st).join("·")}} 여유가 ` +
        `3일 미만입니다.</b> 세척이 끝나는 날 바로 넣어야 한다는 뜻이라 ` +
        `하루만 밀려도 앞 단계가 막힙니다 — 방 하나를 더 두거나 간격을 넓혀야 합니다.</div>`;
    }} else if (!missing.length) {{
      html += `<div class="note" style="color:var(--good)"><b>출하까지 자리가 이어집니다.</b> ` +
        `이 구성이면 배치가 한 방씩 밟아 나갑니다.</div>`;
    }}
    if (missing.length) {{
      html += `<div class="note">${{missing.map(r => r.st).join("·")}} 이(가) 등록되지 않아 ` +
        `대조하지 못했습니다 — <b>미등록은 통과가 아닙니다.</b></div>`;
    }}
    // 후보사는 표에 없다. 없어서가 아니라 **필요량을 낼 식이 없어서**다.
    html += `<div class="note">후보사는 이 표에 없습니다 — 필요 자리가 ` +
      `갱신율·순치기간에 달렸는데 둘 다 안 받고 있어, 넣으면 지어낸 수가 됩니다. ` +
      `등록만 해 두면 발정 판정 경로에는 반영됩니다.</div>`;
    // 밀사 — 자리 수가 맞아도 면적이 모자라면 법정 기준 위반이다
    const dense = barns.map(b => [b, density(b)]).filter(x => x[1].tag === "err");
    if (dense.length) {{
      html += `<div class="note" style="color:var(--bad)"><b>사육밀도 초과 ` +
        `${{dense.length}}동</b> — ${{dense.map(x => `${{x[0].name}}(${{x[1].txt}})`).join(" · ")}}. ` +
        `자리 수가 맞아도 면적이 모자라면 「축산법 시행령」 기준 위반이고, ` +
        `밀사는 증체·사료효율을 떨어뜨립니다.</div>`;
    }}
    html += `</div>`;
  }}
  $("#checks").innerHTML = html;
  $("#h_barns").textContent = barns.length
    ? `${{barns.length}}동 · 방 ${{barns.reduce((s, b) => s + b.rooms, 0)}}개 · ` +
      `자리 ${{barns.reduce((s, b) => s + b.rooms * b.per, 0).toLocaleString()}}`
    : "";

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
  // 등록한 돈사를 **실제로 돌려 보는** 줄을 맨 앞에 둔다. 이 화면의 검사는
  // 정적 대조라 "자리가 맞는가" 까지고, 배치가 실제로 밟아 나가는지는
  // 400일 돌려 봐야 안다(무처소·적체·역류는 거기서만 잡힌다).
  $("#out_cmd").value =
    "# 아래 JSON 을 my_farm.json 으로 저장한 뒤\\n" +
    "python competition/src/barn_watch.py --setup my_farm.json          # 돈군흐름 검사\\n" +
    "python competition/src/barn_watch.py --setup my_farm.json --sweep  # 방을 빼며 한계\\n" +
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
    direction: $("#f_dir").value,
    name: $("#f_name").value || null,
    n_sows: num("#f_sows"), n_gilts: num("#f_gilts"),
    site_type: $("#f_site").value,
    interval_days: parseFloat($("#f_interval").value),
    lactation_days: num("#f_lact"), pre_farrow_days: num("#f_pre"),
    washout_days: num("#f_wash"),
    // area_m2 는 barn_watch.rooms_from_setup 이 읽는 이름이다. 비었으면
    // 넣지 않는다 — null 을 넣으면 그쪽이 0 으로 읽어 방이 다 탈락한다.
    barns: barns.map(b => {{
      const o = {{name: b.name, stage: b.stage, rooms: b.rooms, per: b.per,
                 housing: b.housing, area: b.area ?? null}};
      if (b.area) o.area_m2 = b.area;
      return o;
    }}),
    performance: perf,
    growth: {{survival: num("#p_survival")}},
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
  if (s.direction) $("#f_dir").value = s.direction;
  $("#f_name").value = s.name || "";
  if (s.n_sows) $("#f_sows").value = s.n_sows;
  if (s.n_gilts != null) $("#f_gilts").value = s.n_gilts;
  if (s.site_type) $("#f_site").value = s.site_type;
  if (s.interval_days) $("#f_interval").value = s.interval_days;
  if (s.lactation_days) $("#f_lact").value = s.lactation_days;
  if (s.pre_farrow_days != null) $("#f_pre").value = s.pre_farrow_days;
  if (s.washout_days != null) $("#f_wash").value = s.washout_days;
  barns = (s.barns || []).map(b => ({{
    ...b, area: (b.area ?? b.area_m2) || null}}));
  for (const f of CFG.perf) {{
    const v = (s.performance || {{}})[f.key];
    if (v != null) $("#p_" + f.key).value = v;
  }}
  const gw = (s.growth || {{}}).survival;
  if (gw != null) $("#p_survival").value = gw;
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
    if (k === "rooms" || k === "per") barns[i][k] = Math.max(1, +t.value || 1);
    // 면적은 **비움을 살려 둔다.** 0 으로 바꾸면 '면적 미입력' 과 '0㎡' 를
    // 구별할 수 없어져, 안 적은 농장이 전부 밀사로 찍힌다.
    else if (k === "area") barns[i][k] = t.value === "" ? null : Math.max(0, +t.value || 0);
    else barns[i][k] = t.value;
    if (k !== "name") {{
      // 표를 다시 그리면 커서가 날아간다 — 같은 칸으로 되돌려 준다.
      const pos = t.selectionStart;
      drawBarns();
      const back = document.querySelector(`[data-i="${{i}}"][data-k="${{k}}"]`);
      if (back) {{
        back.focus();
        try {{ back.setSelectionRange(pos, pos); }} catch (e) {{}}
      }}
    }}
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
               per: 20, area: null, housing: HOUSING[0][0]}});
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
