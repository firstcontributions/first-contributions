"""국내 466개 농장 번식성적 실측 — 문헌값을 실측 분포로 바꾼다.

지금까지 벤치마크는 문헌 인용(한돈팜스 평균 PSY 22.8 등)이었다. 국내 실농장
연도별 번식통계(2020~2023, 466행 × 17지표)를 받아 **실측 분위수**로 바꾼다.
"평균보다 낫다"보다 "상위 몇 %"가 농가에 훨씬 잘 읽힌다.

## 이 데이터가 확인해 준 것

우리 앱은 발정 탐지 → 적기 교배 → 분만율·NPD 개선을 주장한다. 그 논거가
실제 데이터로 지지되는지 466농장으로 확인했다(PSY 상위 25% vs 하위 25%):

    비생산일수   32.3일  vs  67.9일   −35.6일   ← 가장 큰 격차
    분만율       87.0%  vs  72.5%   +14.5%p
    재귀발정일     6.0일  vs   8.0일   −2.0일

PSY 와의 순위상관도 같은 순서다(NPD −0.737 · 회전율 +0.727 · 분만율 +0.563).
**세 지표 모두 발정 관리가 만드는 값**이고, 이것이 이 프로젝트가 발정에서
출발한 이유의 실측 근거다.

## 원자료는 커밋하지 않는다

농장 식별자(`0021749`, `PIGGO_182`)가 들어 있어 개별 농장이 특정될 수 있다.
집계 결과(JSON)만 저장하고 원본 xlsx 는 gitignore 한다. 재현하려면 같은
스프레드시트를 `competition/data/farm_stats.xlsx` 에 두고 다시 실행하면 된다.

    python competition/src/korean_farm_stats.py [xlsx경로]
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
DEFAULT_XLSX = os.path.join(ROOT, "competition", "data", "farm_stats.xlsx")
OUT = os.path.join(ROOT, "competition", "data", "korean_farm_stats.json")

# 시트 컬럼 → 우리 코드의 이름. 이름이 바뀌면 여기만 고친다.
COLS = {
    "년도": "year", "지역": "region", "규모": "scale", "농장": "farm",
    "상시모돈수(두)": "sows", "MSY(두)": "msy", "PSY(두)": "psy",
    "모돈회전율(회전)": "turnover", "평균비생산일수(일)": "npd",
    "평균총산(두)": "born_total", "평균실산(두)": "born_alive",
    "평균이유(두)": "weaned", "분만율(%)": "farrowing_rate",
    "초교배일령(일)": "first_service_age", "임신기간(일)": "gestation",
    "포유기간(일)": "lactation", "재귀발정일(일)": "wean_to_estrus",
}
NUM = ["sows", "msy", "psy", "turnover", "npd", "born_total", "born_alive",
       "weaned", "farrowing_rate", "first_service_age", "gestation",
       "lactation", "wean_to_estrus"]
# PSY 를 좌우하는 후보 — 정의상 자명한 것(weaned)도 대조군으로 함께 본다
DRIVERS = ["farrowing_rate", "npd", "wean_to_estrus", "turnover",
           "born_total", "born_alive", "weaned", "lactation",
           "first_service_age", "sows"]
KO = {"psy": "PSY(이유/모돈/년)", "msy": "MSY(출하/모돈/년)",
      "npd": "비생산일수", "farrowing_rate": "분만율(%)",
      "wean_to_estrus": "재귀발정일", "turnover": "모돈회전율",
      "born_total": "평균총산", "born_alive": "평균실산", "weaned": "평균이유",
      "lactation": "포유기간", "first_service_age": "초교배일령",
      "gestation": "임신기간", "sows": "상시모돈수"}


def load(path: str | None = None) -> pd.DataFrame:
    path = path or DEFAULT_XLSX
    if not os.path.exists(path):
        raise SystemExit(
            f"{path} 가 없다. 원자료는 농장 식별자가 있어 커밋하지 않는다 — "
            f"스프레드시트를 이 경로에 두고 다시 실행할 것.")
    d = pd.read_excel(path, sheet_name=0)
    d.columns = [str(c).strip() for c in d.columns]
    missing = [k for k in COLS if k not in d.columns]
    if missing:
        raise SystemExit(f"컬럼이 없다: {missing}\n실제: {list(d.columns)}")
    d = d.rename(columns=COLS)[list(COLS.values())]
    for c in NUM:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    return d


def quantiles(d: pd.DataFrame, cols=None, qs=(.1, .25, .5, .75, .9)) -> dict:
    """지표별 실측 분위수. 농가는 '평균 대비'보다 '상위 몇 %'를 본다."""
    out = {}
    for c in (cols or NUM):
        s = d[c].dropna()
        if len(s) < 20:
            continue
        out[c] = {"n": int(len(s)), "mean": round(float(s.mean()), 2),
                  **{f"p{int(q * 100)}": round(float(s.quantile(q)), 2)
                     for q in qs}}
    return out


def drivers(d: pd.DataFrame, target: str = "psy") -> list:
    """무엇이 성적을 가르는가 — 순위상관 + 상하위 4분위 격차.

    순위상관(Spearman)을 쓰는 이유: 지표마다 단위가 다르고 이상치가 있어
    피어슨은 한두 농장에 끌려간다.
    """
    t = d.dropna(subset=[target])
    hi = t[t[target] >= t[target].quantile(.75)]
    lo = t[t[target] <= t[target].quantile(.25)]
    out = []
    for c in DRIVERS:
        if c == target or t[c].notna().sum() < 30:
            continue
        rho = float(t[[c, target]].corr(method="spearman").iloc[0, 1])
        a, b = float(hi[c].median()), float(lo[c].median())
        out.append({"metric": c, "name_ko": KO.get(c, c),
                    "spearman": round(rho, 3),
                    "top25": round(a, 2), "bottom25": round(b, 2),
                    "gap": round(a - b, 2)})
    return sorted(out, key=lambda r: -abs(r["spearman"]))


def by_scale(d: pd.DataFrame) -> list:
    """규모별 성적 — 큰 농장이 정말 나은가."""
    out = []
    for k, g in d.groupby("scale"):
        s = g["psy"].dropna()
        if len(s) < 10:
            continue
        out.append({"scale": str(k), "n": int(len(s)),
                    "psy_median": round(float(s.median()), 2),
                    "npd_median": round(float(g["npd"].median()), 1),
                    "farrowing_median": round(float(g["farrowing_rate"]
                                                    .median()), 1)})
    return sorted(out, key=lambda r: r["psy_median"])


def compare_defaults(d: pd.DataFrame) -> list:
    """우리가 박아둔 상수 vs 실측. 어긋나면 그 농장 계산이 아니다."""
    sys.path.insert(0, os.path.join(ROOT, "competition"))
    from pigflow.config import BREEDING_DEFAULTS as B
    pairs = [
        ("gestation", "gestation_days", B["gestation_days"], 1.0),
        ("lactation", "lactation_days", B["lactation_days"], 1.0),
        ("wean_to_estrus", "wean_to_service_days",
         B["wean_to_service_days"], 1.0),
        ("farrowing_rate", "farrowing_rate", B["farrowing_rate"] * 100, 1.0),
        ("turnover", "sow_turnover", B["sow_turnover"], 1.0),
        ("weaned", "weaned_per_litter", B["weaned_per_litter"], 1.0),
    ]
    out = []
    for col, name, ours, _ in pairs:
        s = d[col].dropna()
        med = float(s.median())
        # 실측 중앙값 대비 10% 넘게 벌어지면 손봐야 한다
        off = abs(ours - med) / max(med, 1e-9) > 0.10
        out.append({"metric": col, "name_ko": KO.get(col, col),
                    "config": name, "ours": round(float(ours), 2),
                    "median": round(med, 2), "mean": round(float(s.mean()), 2),
                    "p25": round(float(s.quantile(.25)), 2),
                    "p75": round(float(s.quantile(.75)), 2),
                    "off": bool(off)})
    return out


def percentile_of(d: pd.DataFrame, metric: str, value: float) -> float:
    """어떤 값이 실측 분포에서 몇 분위인가 — 농가 피드백에 쓴다."""
    s = d[metric].dropna()
    if not len(s):
        return float("nan")
    return float((s < value).mean())


def run(path: str | None = None, verbose: bool = True) -> dict:
    d = load(path)
    res = {
        "n_rows": int(len(d)),
        "years": sorted(int(x) for x in d["year"].dropna().unique()),
        "n_farms": int(d["farm"].nunique()),
        "quantiles": quantiles(d),
        "drivers_psy": drivers(d, "psy"),
        "by_scale": by_scale(d),
        "defaults_check": compare_defaults(d),
    }
    both = d.dropna(subset=["psy", "msy"])
    if len(both) >= 20:
        res["post_wean_survival"] = {
            "n": int(len(both)),
            "median": round(float((both["msy"] / both["psy"]).median()), 3),
            "p25": round(float((both["msy"] / both["psy"]).quantile(.25)), 3),
            "p75": round(float((both["msy"] / both["psy"]).quantile(.75)), 3),
        }
    if verbose:
        _print(res)
    return res


def _print(r: dict) -> None:
    print("=" * 74)
    print(f"  국내 농장 번식성적 실측 — {r['n_rows']}행 · "
          f"농장 {r['n_farms']}개 · {r['years'][0]}~{r['years'][-1]}")
    print("=" * 74)
    q = r["quantiles"]
    print(f"\n  {'지표':<14}{'n':>5}{'하위10%':>9}{'25%':>8}{'중앙':>8}"
          f"{'75%':>8}{'상위10%':>9}")
    for k in ("psy", "msy", "npd", "farrowing_rate", "turnover", "weaned",
              "wean_to_estrus"):
        if k not in q:
            continue
        v = q[k]
        print(f"  {KO.get(k, k):<14}{v['n']:>5}{v['p10']:>9}{v['p25']:>8}"
              f"{v['p50']:>8}{v['p75']:>8}{v['p90']:>9}")

    print("\n  무엇이 PSY 를 가르는가 (순위상관 · 상하위 4분위 중앙값)")
    print(f"  {'지표':<14}{'ρ':>8}{'상위25%':>10}{'하위25%':>10}{'격차':>10}")
    for x in r["drivers_psy"][:7]:
        print(f"  {x['name_ko']:<14}{x['spearman']:>+8.3f}{x['top25']:>10}"
              f"{x['bottom25']:>10}{x['gap']:>+10}")

    print("\n  우리 기본값 vs 실측 중앙값")
    for x in r["defaults_check"]:
        mark = "  ⚠️ 손볼 것" if x["off"] else ""
        print(f"  {x['name_ko']:<14}{x['config']:<22}"
              f"{x['ours']:>8} vs {x['median']:>7}{mark}")

    if "post_wean_survival" in r:
        p = r["post_wean_survival"]
        print(f"\n  이유후 육성률(MSY/PSY, {p['n']}농장): 중앙 {p['median']:.1%} "
              f"· 25% {p['p25']:.1%} · 75% {p['p75']:.1%}")
    print("\n  규모별 PSY 중앙값")
    for s in r["by_scale"]:
        print(f"    {s['scale']:<12} n={s['n']:>3}  PSY {s['psy_median']:>5} · "
              f"NPD {s['npd_median']:>5} · 분만율 {s['farrowing_median']:>5}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="korean_farm_stats")
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
