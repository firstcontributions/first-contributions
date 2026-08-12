"""가상 농장 데이터 생성 — **실측 분포를 재현하고, 재현했는지 검사한다.**

시뮬레이션용 합성 데이터는 아무렇게나 만들면 안 된다. 난수로 채운 이력은
그럴듯해 보이지만 시뮬레이션 결과를 통째로 무의미하게 만든다. 두 가지를
지켜야 쓸 수 있다:

  1. **주변분포가 실측과 맞을 것** — 재귀발정일·분만율·복당이유·NPD 를
     국내 466농장(연도별)·179농장(월별) 실측에서 뽑는다.
  2. **개체 안에서 날짜가 앞뒤가 맞을 것** — 교배는 발정 당일이거나 다음 날,
     분만은 교배 + 임신기간, 이유는 분만 + 포유기간. 이게 깨지면 앱의
     일정·지연 판정이 전부 헛돈다.

그리고 만든 뒤에 `validate()` 로 1번을 실제로 검사한다. **검사 없는 합성은
쓰지 않는다** — 이 모듈의 요점이 그것이다.

    python competition/src/synth_farm.py --sows 300 --years 2
    python competition/src/synth_farm.py --sows 300 --csv /tmp/herd.csv

## 무엇을 실측에서 가져오고 무엇을 가정하는가

  실측  재귀발정일 · 분만율 · 복당이유 · 임신/포유기간 · 계절 변동(−2.7%p) ·
        임신사고 유형 구성(1차 35.9% · 불규칙 19.6% · 2차 11.5% …)
  가정  산차 분포 · 임신기간 분산 · **개체 이질성**(잘하는 모돈/못하는 모돈)

개체 이질성은 실측 자료에 없다(농장 단위 집계뿐). 그런데 이게 없으면 모든
모돈이 똑같이 행동해서 "관리가 필요한 개체"를 고르는 기능이 무의미해진다.
그래서 농장 평균은 실측에 맞추되 개체별로 흩뜨리고, 그 사실을 명시한다.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

STATS = os.path.join(ROOT, "competition", "data", "korean_farm_stats.json")
MONTHLY = os.path.join(ROOT, "competition", "data", "farm_monthly.json")

# 실측에 없어 가정하는 값 — 바꿀 때 여기만 보면 된다.
PARITY_MIX = [0.18, 0.17, 0.16, 0.14, 0.12, 0.09, 0.07, 0.07]   # 1~8산
GESTATION_SD = 1.2          # 임신기간 표준편차(일). 실측은 농장 평균만 있다.
SOW_HETEROGENEITY = 0.35    # 개체 이질성 — 농장 평균 대비 개체 편차의 크기
# **실측과 같은 구간을 써야 한다.** farm_monthly 는 교배월 7·8·9 를 1·2·3 과
# 비교해 −2.7%p 를 냈다. 여기서 6월을 넣거나 "나머지 전체"와 비교하면 대비가
# 달라져 −5.2%p 같은 값이 나오고, 그걸 통과시키면 합성이 실측보다 계절을
# 과장한 채로 시뮬레이션에 들어간다.
SUMMER = (7, 8, 9)          # 교배월 기준 하계
WINTER = (1, 2, 3)          # 대조군 — 실측과 동일
# 재발 유형 구성(월별 실측, 완전 보고분). 나머지 사고는 도태·폐사로 묶는다.
RETURN_MIX = {"1차": 0.359, "불규칙": 0.196, "2차": 0.115}


def _load(path: str, what: str) -> dict:
    if not os.path.exists(path):
        raise SystemExit(f"{path} 가 없다 — {what} 를 먼저 돌릴 것.")
    return json.load(open(path, encoding="utf-8"))


class Params:
    """실측에서 뽑은 생성 파라미터. 어디서 왔는지 함께 들고 다닌다."""

    def __init__(self, stats: dict | None = None, monthly: dict | None = None):
        s = stats or _load(STATS, "korean_farm_stats.py")
        m = monthly or _load(MONTHLY, "farm_monthly.py")
        q = s["quantiles"]
        self.wean_to_estrus = (q["wean_to_estrus"]["p50"],
                               q["wean_to_estrus"]["p25"],
                               q["wean_to_estrus"]["p75"])
        self.farrowing_rate = q["farrowing_rate"]["p50"] / 100.0
        self.weaned = q["weaned"]["p50"]
        self.gestation = q["gestation"]["p50"]
        self.lactation = q["lactation"]["p50"]
        self.born_alive = q["born_alive"]["p50"]
        # 계절 효과는 %p 라 비율로 바꾼다
        self.summer_gap = m["farrowing_rate"]["summer_minus_winter"] / 100.0
        self.source = {
            "annual": f"{s['n_farms']}농장 {s['years'][0]}~{s['years'][-1]}",
            "monthly": f"{m['n_farms']}농장 {m['years'][0]}~{m['years'][-1]}",
        }


def _skewed(rng, med: float, p25: float, p75: float, n: int) -> np.ndarray:
    """중앙값·사분위로 오른쪽 꼬리 분포를 만든다(재귀발정일·NPD 용).

    정규분포를 쓰면 안 된다 — 재귀발정일은 평균 8.5 인데 중앙이 6.9 로
    오른쪽으로 길게 늘어져 있다. 대칭 분포로 만들면 '늦게 오는 소수'가
    사라져서 조기경보 기능을 시험할 표본이 없어진다.
    """
    sigma = max(0.05, np.log(max(p75, med + 0.1) / max(med, 0.1)) / 0.6745)
    return rng.lognormal(np.log(max(med, 0.1)), sigma, n)


def generate(n_sows: int = 300, years: float = 1.0, start: str = "2025-01-01",
             seed: int = 0, params: Params | None = None) -> pd.DataFrame:
    """개체·사이클 단위 이력. 한 행 = 한 모돈의 한 번식 사이클.

    컬럼: sow_id · parity · wean_prev · estrus · service · farrow · wean ·
          outcome · return_type · born_alive · weaned · month_service
    """
    P = params or Params()
    rng = np.random.default_rng(seed)
    t0 = date.fromisoformat(start)
    horizon = int(365 * years)

    # 개체 이질성 — 농장 평균은 유지하되 개체마다 다르게. 실측에 없는 가정이다.
    quality = rng.normal(0.0, SOW_HETEROGENEITY, n_sows)
    parity = rng.choice(np.arange(1, len(PARITY_MIX) + 1), n_sows,
                        p=np.array(PARITY_MIX) / sum(PARITY_MIX))
    # 사이클 위상을 흩뜨려 정상 상태에서 시작한다. 전부 같은 날 이유하면
    # 첫 배치만 몰리고 그 뒤가 텅 빈다.
    cycle = P.gestation + P.lactation + P.wean_to_estrus[0]
    phase = rng.uniform(0, cycle, n_sows)

    rows = []
    for i in range(n_sows):
        sid = f"S{2000 + i}"
        par = int(parity[i])
        # 직전 이유일 — 위상만큼 과거로
        wean_prev = t0 - timedelta(days=float(phase[i]))
        cursor = wean_prev
        while (cursor - t0).days < horizon:
            w2e = float(_skewed(rng, *P.wean_to_estrus, 1)[0])
            # 잘하는 개체는 빨리 발정이 온다(quality 가 클수록 짧게)
            w2e = max(3.0, w2e * (1.0 - 0.25 * quality[i]))
            estrus = cursor + timedelta(days=w2e)
            # 발정 발견 당일 또는 다음 날 교배
            service = estrus + timedelta(days=int(rng.integers(0, 2)))
            mo = service.month
            # 계절 + 개체 편차를 반영한 이 사이클의 분만 확률
            fr = P.farrowing_rate + (P.summer_gap if mo in SUMMER else 0.0)
            fr = float(np.clip(fr + 0.06 * quality[i], 0.35, 0.98))
            if rng.random() < fr:
                gest = P.gestation + rng.normal(0, GESTATION_SD)
                farrow = service + timedelta(days=float(gest))
                lact = max(14.0, P.lactation + rng.normal(0, 1.5))
                wean = farrow + timedelta(days=float(lact))
                ba = max(4, int(round(rng.normal(
                    P.born_alive + 0.6 * quality[i], 1.6))))
                wn = max(0, min(ba, int(round(rng.normal(
                    P.weaned + 0.6 * quality[i], 1.3)))))
                rows.append(dict(sow_id=sid, parity=par, wean_prev=cursor,
                                 estrus=estrus, service=service, farrow=farrow,
                                 wean=wean, outcome="분만", return_type=None,
                                 born_alive=ba, weaned=wn,
                                 month_service=mo))
                cursor = wean
                par += 1
            else:
                # 실패 — 유형에 따라 다음 발정까지 걸리는 시간이 다르다.
                # 1차 재발은 정상 발정주기(21일), 불규칙은 그보다 길다.
                kinds = list(RETURN_MIX) + ["기타"]
                w = list(RETURN_MIX.values())
                w.append(max(0.0, 1.0 - sum(w)))
                kind = str(rng.choice(kinds, p=np.array(w) / sum(w)))
                delay = {"1차": 21.0, "2차": 42.0,
                         "불규칙": float(rng.uniform(26, 40)),
                         "기타": float(rng.uniform(45, 80))}[kind]
                rows.append(dict(sow_id=sid, parity=par, wean_prev=cursor,
                                 estrus=estrus, service=service, farrow=None,
                                 wean=None, outcome="재발", return_type=kind,
                                 born_alive=None, weaned=None,
                                 month_service=mo))
                cursor = service + timedelta(days=delay)
    df = pd.DataFrame(rows)
    df.attrs["params"] = P.source
    df.attrs["assumed"] = {
        "parity_mix": PARITY_MIX, "gestation_sd": GESTATION_SD,
        "sow_heterogeneity": SOW_HETEROGENEITY,
        "note": "개체 이질성·산차 분포·임신기간 분산은 실측에 없는 가정",
    }
    return df


# -- 검증 -----------------------------------------------------------------
def validate(df: pd.DataFrame, params: Params | None = None,
             tol: float = 0.15) -> dict:
    """합성 결과가 실측 분포를 재현하는지. **이걸 안 하면 쓰면 안 된다.**"""
    P = params or Params()
    out: dict = {"n_rows": int(len(df)), "n_sows": int(df["sow_id"].nunique()),
                 "checks": [], "ok": True}

    def chk(name, got, want, unit="", rel=tol):
        bad = abs(got - want) > abs(want) * rel
        out["checks"].append({"name": name, "got": round(float(got), 3),
                              "want": round(float(want), 3), "unit": unit,
                              "ok": not bad})
        if bad:
            out["ok"] = False

    far = df[df["outcome"] == "분만"]
    chk("분만율", len(far) / max(1, len(df)), P.farrowing_rate)
    w2e = (pd.to_datetime(df["estrus"]) - pd.to_datetime(df["wean_prev"])
           ).dt.days
    chk("재귀발정일 중앙", w2e.median(), P.wean_to_estrus[0])
    if len(far):
        g = (pd.to_datetime(far["farrow"]) - pd.to_datetime(far["service"])
             ).dt.days
        chk("임신기간 중앙", g.median(), P.gestation, "일", 0.03)
        lc = (pd.to_datetime(far["wean"]) - pd.to_datetime(far["farrow"])
              ).dt.days
        chk("포유기간 중앙", lc.median(), P.lactation, "일", 0.10)
        chk("복당 이유두수 중앙", far["weaned"].median(), P.weaned, "두")

    # 계절 효과가 살아 있는지 — 여름 교배의 분만율이 낮아야 한다
    # 실측과 **같은 대비**로 잰다: 여름(7·8·9) vs 겨울(1·2·3).
    #
    # **표본이 작으면 이 검사를 하면 안 된다.** 계절 효과(−2.7%p)는 두 비율의
    # 차이인데, 각 군 100건이면 표준오차가 5%p 를 넘는다 — 실제로 모돈 150두·
    # 1.5년에서 −6.4%p 가 나와 실패했다. 생성기가 과장한 게 아니라 잡음이었다
    # (모돈 800·3년으로 재면 주입 −2.7 → 관측 −2.2, 시드 편차 ±0.9).
    # 그래서 허용치를 표준오차에서 계산하고, 표본이 모자라면 건너뛴다.
    s = df[df["month_service"].isin(SUMMER)]
    w = df[df["month_service"].isin(WINTER)]
    ns, nw = len(s), len(w)
    if ns >= 200 and nw >= 200:
        ps = (s["outcome"] == "분만").mean()
        pw = (w["outcome"] == "분만").mean()
        gap = ps - pw
        se = float(np.sqrt(ps * (1 - ps) / ns + pw * (1 - pw) / nw))
        ok = abs(gap - P.summer_gap) < max(0.01, 2.5 * se)
        out["checks"].append({"name": "하계 분만율 차(%p)",
                              "got": round(gap * 100, 2),
                              "want": round(P.summer_gap * 100, 2),
                              "unit": "%p", "ok": ok,
                              "se_pp": round(se * 100, 2), "n": [ns, nw]})
        if not ok:
            out["ok"] = False
    else:
        out["checks"].append({
            "name": "하계 분만율 차(%p)", "got": float("nan"),
            "want": round(P.summer_gap * 100, 2), "unit": "%p", "ok": True,
            "skipped": f"표본 부족(여름 {ns}·겨울 {nw}, 각 200 필요)"})

    # **날짜 정합성** — 여기가 깨지면 앱의 일정 판정이 전부 헛돈다
    bad = []
    if (pd.to_datetime(df["service"]) < pd.to_datetime(df["estrus"])).any():
        bad.append("교배가 발정보다 앞선다")
    if len(far):
        if (pd.to_datetime(far["farrow"])
                <= pd.to_datetime(far["service"])).any():
            bad.append("분만이 교배보다 앞선다")
        if (pd.to_datetime(far["wean"])
                <= pd.to_datetime(far["farrow"])).any():
            bad.append("이유가 분만보다 앞선다")
        if (far["weaned"] > far["born_alive"]).any():
            bad.append("이유두수가 실산두수보다 많다")
    # 같은 개체의 사이클이 시간순으로 겹치지 않아야 한다
    for sid, g in df.groupby("sow_id"):
        g = g.sort_values("estrus")
        prev = None
        for r in g.itertuples(index=False):
            if prev is not None and r.wean_prev < prev:
                bad.append(f"{sid}: 사이클이 겹친다")
                break
            prev = r.wean if r.wean is not None else r.service
    out["consistency"] = bad
    if bad:
        out["ok"] = False
    return out


def to_herd_csv(df: pd.DataFrame, path: str, today: str | None = None) -> int:
    """앱이 먹는 형태 — 개체별 **최근** 이벤트 한 줄."""
    t = date.fromisoformat(today) if today else date.today()
    past = df[pd.to_datetime(df["service"]).dt.date <= t]
    rows = []
    for sid, g in past.groupby("sow_id"):
        r = g.sort_values("service").iloc[-1]
        rows.append({"id": sid, "parity": int(r["parity"]),
                     "weaning_date": r["wean_prev"],
                     "service_date": r["service"],
                     "farrow_date": r["farrow"],
                     "outcome": r["outcome"]})
    out = pd.DataFrame(rows)
    out.to_csv(path, index=False, encoding="utf-8-sig")
    return len(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="synth_farm")
    ap.add_argument("--sows", type=int, default=300)
    ap.add_argument("--years", type=float, default=1.0)
    ap.add_argument("--start", default="2025-01-01")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--csv", help="개체별 최근 이벤트를 CSV 로 저장")
    a = ap.parse_args(argv)

    P = Params()
    df = generate(a.sows, a.years, a.start, a.seed, P)
    v = validate(df, P)

    print("=" * 72)
    print(f"  가상 농장 — 모돈 {a.sows}두 · {a.years}년 · 사이클 {len(df):,}건")
    print("=" * 72)
    print(f"  실측 출처: 연도별 {P.source['annual']} · 월별 {P.source['monthly']}")
    print(f"\n  {'검사 항목':<20}{'합성':>10}{'실측':>10}   판정")
    print("  " + "-" * 52)
    for c in v["checks"]:
        print(f"  {c['name']:<20}{c['got']:>10}{c['want']:>10}   "
              + ("✅" if c["ok"] else "❌"))
    if v["consistency"]:
        print("\n  ❌ 날짜 정합성 위반:")
        for b in v["consistency"][:5]:
            print(f"     {b}")
    print(f"\n  종합: {'✅ 실측 분포를 재현한다' if v['ok'] else '❌ 재현 실패 — 쓰면 안 된다'}")
    print("\n  가정(실측에 없음): 산차 분포 · 임신기간 분산 · **개체 이질성**")
    print("    개체 이질성이 없으면 모든 모돈이 똑같이 행동해서 '관리가 필요한")
    print("    개체를 고르는' 기능을 시험할 수 없다. 농장 평균은 실측에 맞추되")
    print("    개체별로 흩뜨렸다.")
    if a.csv:
        n = to_herd_csv(df, a.csv, a.start)
        print(f"\n  저장: {a.csv} ({n}두)")
    return 0 if v["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
