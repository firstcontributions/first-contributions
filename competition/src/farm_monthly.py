"""월별 번식통계 — 계절성과 임신사고 구성. 기준연도 2020~2023.

연도별 통계(korean_farm_stats)가 "얼마나 잘하나"라면, 월별은 **"언제 무너지나"**
와 **"무엇 때문에 무너지나"** 를 말한다. 179개 농장 × 19지표 × 12개월.

## 두 가지를 이 데이터로 확인했다

**1) 여름 불임이 실재한다 — 단 교배월로 되돌려야 보인다.**
분만율은 **분만 시점**에 기록되므로 그대로 보면 12월이 최저(80.2%)다. 임신
114일(≈3.8개월)을 빼서 교배월로 옮기면 7·8월 교배분이 최저다:

    교배 7월 → 분만 11월  80.3%
    교배 8월 → 분만 12월  80.2%
    여름 교배(7·8·9월) 81.0%  vs  겨울 교배(1·2·3월) 83.7%   → −2.7%p

**2) 임신사고의 3분의 2가 '재발'이다 — 발정 관리가 잡는 항목.**
1차 재발 35.9% + 불규칙 19.6% + 2차 재발 11.5% = **67.1%**.

## 커버리지 함정

지표마다 보고하는 농장 수가 다르다(공태 52.6% vs 2차재발 22.1%). 전체 합으로
구성비를 내면 많이 보고된 항목이 커 보인다 — 실제로 그렇게 계산했을 때
불규칙이 1위(29.0%)로 나왔지만, **전 유형을 다 보고한 농장-월만** 추리면
1차 재발이 1위(35.9%)다. 이 모듈은 후자로 계산하고 커버리지를 함께 낸다.

    python competition/src/farm_monthly.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DEFAULT_XLSX = os.path.join(ROOT, "competition", "data", "farm_monthly.xlsx")
OUT = os.path.join(ROOT, "competition", "data", "farm_monthly.json")

MONTHS = [f"{i}월" for i in range(1, 13)]
GESTATION_MONTHS = 4        # 임신 114일 ≈ 3.75개월 → 반올림 4
SUMMER = (7, 8, 9)          # 교배월 기준
WINTER = (1, 2, 3)
# 발정 관리가 직접 겨냥하는 사고 유형 — 재발은 발정을 다시 잡는 일이다
RETURN_TYPES = ("임신사고(1차)", "임신사고(2차)", "임신사고(불규칙)")


def load(path: str | None = None) -> pd.DataFrame:
    p = path or DEFAULT_XLSX
    if not os.path.exists(p):
        raise SystemExit(
            f"{p} 가 없다. 원자료는 농장 식별자가 있어 커밋하지 않는다 — "
            f"월별 번식통계 스프레드시트를 이 경로에 둘 것.")
    d = pd.read_excel(p, sheet_name=0)
    d.columns = [str(c).strip() for c in d.columns]
    need = ["년도", "농장", "데이터구분"] + MONTHS
    miss = [c for c in need if c not in d.columns]
    if miss:
        raise SystemExit(f"컬럼이 없다: {miss}\n실제: {list(d.columns)}")
    long = d.melt(id_vars=["년도", "지역", "규모", "농장", "데이터구분"],
                  value_vars=MONTHS, var_name="월", value_name="v")
    long["v"] = pd.to_numeric(long["v"], errors="coerce")
    long["m"] = long["월"].str.rstrip("월").astype(int)
    return long.dropna(subset=["v"])


def service_month(farrow_month: int) -> int:
    """분만월 → 교배월. 분만율·산자수는 분만 시점에 기록된다."""
    return ((farrow_month - GESTATION_MONTHS - 1) % 12) + 1


def seasonality(long: pd.DataFrame, metric: str,
                shift_to_service: bool = False) -> dict:
    """월별 중앙값. shift_to_service 면 교배월 기준으로 되돌린다."""
    g = long[long["데이터구분"] == metric].groupby("m")["v"].agg(
        ["median", "count"])
    if not len(g):
        return {}
    by = {}
    for fm in g.index:
        key = service_month(int(fm)) if shift_to_service else int(fm)
        by[key] = round(float(g.loc[fm, "median"]), 2)
    out = {"metric": metric, "by_month": by,
           "n": int(g["count"].sum()),
           "basis": "교배월" if shift_to_service else "기록월",
           "min_month": int(min(by, key=by.get)),
           "max_month": int(max(by, key=by.get)),
           "amplitude": round(max(by.values()) - min(by.values()), 2)}
    s = [by[m] for m in SUMMER if m in by]
    w = [by[m] for m in WINTER if m in by]
    if s and w:
        out["summer"] = round(float(np.mean(s)), 2)
        out["winter"] = round(float(np.mean(w)), 2)
        out["summer_minus_winter"] = round(out["summer"] - out["winter"], 2)
    return out


def accident_mix(long: pd.DataFrame) -> dict:
    """임신사고 구성 — **전 유형을 보고한 농장-월만** 쓴다.

    지표별 보고율이 22~53% 로 크게 다르다. 전체 합으로 구성비를 내면 많이
    보고된 항목이 커 보인다(그렇게 하면 불규칙 29.0% 1위, 제대로 하면 1차
    재발 35.9% 1위). 커버리지를 함께 돌려줘 이 한계를 드러낸다.
    """
    acc = long[long["데이터구분"].str.startswith("임신사고")].copy()
    if not len(acc):
        return {}
    acc["key"] = (acc["농장"].astype(str) + "|" + acc["년도"].astype(str)
                  + "|" + acc["m"].astype(str))
    piv = acc.pivot_table(index="key", columns="데이터구분", values="v",
                          aggfunc="sum")
    coverage = {k: round(float(v), 3) for k, v in piv.notna().mean().items()}
    full = piv.dropna()
    if len(full) < 30:
        return {"coverage": coverage, "n_complete": int(len(full)),
                "note": "완전 보고 레코드가 너무 적어 구성비를 내지 않는다"}
    s = full.sum()
    tot = float(s.sum())
    mix = {k: round(float(v) / tot, 4) for k, v in
           s.sort_values(ascending=False).items()}
    ret = sum(mix.get(t, 0.0) for t in RETURN_TYPES)
    # 같은 계산을 전체 합으로도 해서 얼마나 다른지 보인다
    naive = piv.sum()
    naive_mix = {k: round(float(v) / float(naive.sum()), 4)
                 for k, v in naive.sort_values(ascending=False).items()}
    return {"coverage": coverage, "n_complete": int(len(full)),
            "n_all": int(len(piv)), "mix": mix,
            "return_share": round(ret, 4),
            "naive_mix_top": list(naive_mix)[:3],
            "mix_top": list(mix)[:3]}


def run(path: str | None = None, verbose: bool = True) -> dict:
    long = load(path)
    years = sorted(int(x) for x in long["년도"].dropna().unique())
    res = {
        "n_obs": int(len(long)),
        "n_farms": int(long["농장"].nunique()),
        "years": years,
        "metrics": sorted(long["데이터구분"].unique().tolist()),
        # 분만율·산자수는 분만 시점 기록 → 교배월로 되돌린다
        "farrowing_rate": seasonality(long, "분만율", shift_to_service=True),
        # **되돌리기 전** 곡선도 같이 낸다. 산식은 위와 같고 플래그만 다르다.
        # 기록월 그대로 보면 12월이 최저라 여름 불임이 안 보이는데, 그 '안
        # 보이는 그림' 을 나란히 놓지 않으면 왜 되돌려야 하는지가 안 보인다.
        "farrowing_rate_raw": seasonality(long, "분만율"),
        "weaned": seasonality(long, "평균이유", shift_to_service=True),
        # 재귀율은 이유 직후 사건이라 기록월이 곧 발생월이다
        "return_7d": seasonality(long, "7일내재귀율"),
        "accidents": accident_mix(long),
    }
    if verbose:
        _print(res)
    return res


def _print(r: dict) -> None:
    print("=" * 76)
    print(f"  월별 번식통계 — 농장 {r['n_farms']}개 · 관측 {r['n_obs']:,}건 · "
          f"{r['years'][0]}~{r['years'][-1]}")
    print("=" * 76)
    for key, title in (("farrowing_rate", "분만율"), ("weaned", "평균이유"),
                       ("return_7d", "7일내재귀율")):
        s = r.get(key)
        if not s:
            continue
        print(f"\n  {title} — {s['basis']} 기준 (관측 {s['n']:,})")
        print("   " + " ".join(
            f"{m:>2}월{s['by_month'].get(m, float('nan')):>6.1f}"
            for m in range(1, 13)))
        print(f"    최저 {s['min_month']}월 · 최고 {s['max_month']}월 · "
              f"진폭 {s['amplitude']}")
        if "summer_minus_winter" in s:
            print(f"    여름(7·8·9월) {s['summer']} vs 겨울(1·2·3월) "
                  f"{s['winter']}  →  {s['summer_minus_winter']:+.1f}")

    a = r.get("accidents") or {}
    if a.get("mix"):
        print(f"\n  임신사고 구성 — 전 유형 보고 {a['n_complete']:,} / "
              f"{a['n_all']:,} 농장-월")
        for k, v in list(a["mix"].items())[:6]:
            bar = "█" * int(v * 60)
            print(f"    {k:<18}{v:>6.1%} {bar}")
        print(f"\n    **재발 계열 {a['return_share']:.1%}** "
              f"(1차·2차·불규칙) — 발정 관리가 직접 겨냥하는 항목")
        if a["mix_top"][0] != a["naive_mix_top"][0]:
            print(f"    ※ 전체 합으로 계산하면 1위가 {a['naive_mix_top'][0]} 로"
                  f" 바뀐다. 지표별 보고율이 22~53% 로 달라 많이 보고된 항목이")
            print(f"      커 보이기 때문이다 — 완전 보고 레코드만 쓴 위 값이 맞다.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="farm_monthly")
    ap.add_argument("xlsx", nargs="?", default=None)
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args(argv)
    r = run(a.xlsx)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(r, open(a.out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"\n저장: {a.out}  (원자료는 농장 식별자가 있어 커밋하지 않는다)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
