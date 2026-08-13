"""월별 번식통계 **패널** — 계절 손실을 농장별로 따라간다.

`farm_monthly.py` 는 전체 곡선 하나를 낸다(여름 교배 −2.7%p). 그 값은
"우리 농장이 취약한 쪽인가"에 답하지 못한다. 이 모듈은 같은 원자료를
**농장 단위**로 쪼개서 계절 손실의 분포를 내고, 원/년으로 환산한다.

## 원자료에서 먼저 걸린 것 — 중복

    전체 6,533행 → (년도·농장·데이터구분) 유일 1,464행.  **77.6% 가 중복.**

값이 다른 중복은 0건이라 어느 쪽을 남길지 고민할 필요는 없지만, 농장마다
반복 횟수가 1~14회로 달라서 **중복을 그대로 두면 많이 실린 농장이 중앙값을
끌고 간다.** 농장별로 쪼개려면 애초에 성립하지 않는다 — 한 농장이 14행이면
그 농장의 '관측 개월'이 168개월로 잡힌다. 이 모듈은 항상 중복을 먼저 지운다.

## 실제 규모 — 179농장은 파일 전체의 농장 수다

지표마다 보고 농장이 다르다. 주 타깃인 **분만율은 68농장 · 75농장-연**,
연도는 **2020·2021 뿐**이다(2022 는 파일에 아예 없고 2023 은 분만율이 없다).

    python competition/src/farm_monthly_panel.py --audit
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, "competition", "data")
MONTHLY_XLSX = os.path.join(DATA, "farm_monthly.xlsx")
ANNUAL_XLSX = os.path.join(DATA, "farm_stats.xlsx")
OUT = os.path.join(DATA, "farm_monthly_panel.json")

MONTHS = [f"{i}월" for i in range(1, 13)]
KEY = ["년도", "농장", "데이터구분"]
TARGET = "분만율"
GESTATION_MONTHS = 4        # 임신 114일 ≈ 3.75개월 → 반올림 4 (farm_monthly 와 동일)
SUMMER = (7, 8, 9)          # 교배월 기준
WINTER = (1, 2, 3)
RATE_BOUNDS = (20.0, 100.0)  # 분만율(%) 로 물리적으로 가능한 범위

# 주 산출물 성립: 여름·겨울 교배분을 각각 낼 수 있는 농장
MIN_FARMS_SEASON = 50
# 부수 산출물(DL 대조) 성립: 연속 12개월 이상 결측 없는 농장
MIN_FARMS_SEQ = 80


def _read(path: str, what: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise SystemExit(
            f"{path} 가 없다. 원자료는 농장 식별자가 있어 커밋하지 않는다 — "
            f"{what} 스프레드시트를 이 경로에 둘 것.")
    d = pd.read_excel(path, sheet_name=0)
    d.columns = [str(c).strip() for c in d.columns]
    return d


def load_wide(path: str | None = None) -> tuple[pd.DataFrame, dict]:
    """중복을 지운 wide 테이블 + 중복 감사 결과.

    값이 서로 다른 중복이 있으면 어느 쪽이 맞는지 알 수 없으므로 세어서
    돌려준다. 조용히 첫 행을 고르면 그 선택이 결과에 숨는다.
    """
    d = _read(path or MONTHLY_XLSX, "월별 번식통계")
    miss = [c for c in KEY + MONTHS if c not in d.columns]
    if miss:
        raise SystemExit(f"컬럼이 없다: {miss}\n실제: {list(d.columns)}")
    exact = d.drop_duplicates(KEY + MONTHS)
    conflict = int((exact.groupby(KEY).size() > 1).sum())
    info = {"rows_raw": int(len(d)), "rows_dedup": int(len(exact)),
            "dup_share": round(1 - len(exact) / len(d), 3),
            "conflicting_keys": conflict}
    return exact.reset_index(drop=True), info


def to_long(wide: pd.DataFrame) -> pd.DataFrame:
    keep = [c for c in ("년도", "지역", "규모", "농장", "데이터구분")
            if c in wide.columns]
    long = wide.melt(id_vars=keep, value_vars=MONTHS,
                     var_name="월", value_name="v")
    long["v"] = pd.to_numeric(long["v"], errors="coerce")
    long["m"] = long["월"].str.rstrip("월").astype(int)
    return long.dropna(subset=["v"]).drop(columns=["월"])


def service_month(farrow_month: int) -> int:
    """분만월 → 교배월. 분만율은 분만 시점에 기록된다."""
    return ((farrow_month - GESTATION_MONTHS - 1) % 12) + 1


def annual_sows(path: str | None = None) -> pd.DataFrame:
    """농장-연 상시모돈수. 규모 보정과 원/년 환산에 쓴다."""
    a = _read(path or ANNUAL_XLSX, "연도별 번식통계")
    col = "상시모돈수(두)"
    out = a[["년도", "농장", col]].copy()
    out["n_sows"] = pd.to_numeric(out[col], errors="coerce")
    # 0 두는 상시모돈이 아니라 미기입이다 — 규모 보정에 쓰면 0 으로 나눈다
    out.loc[out["n_sows"] <= 0, "n_sows"] = np.nan
    return out.drop(columns=[col])


def _months_per_farmyear(wide: pd.DataFrame, metric: str) -> pd.DataFrame:
    s = wide[wide["데이터구분"] == metric]
    v = s[MONTHS].apply(pd.to_numeric, errors="coerce")
    return pd.DataFrame({"농장": s["농장"].values, "년도": s["년도"].values,
                         "n_months": v.notna().sum(axis=1).values})


def longest_run(long: pd.DataFrame, metric: str) -> pd.DataFrame:
    """농장별 최장 연속 관측 개월. 해가 붙어 있으면 이어서 센다.

    2022 가 파일에 없으므로 2021→2023 은 이어 세지 않는다. 그렇게 세면
    24개월 연속인 척하는 두 토막이 된다.
    """
    s = long[long["데이터구분"] == metric]
    rows = []
    for farm, g in s.groupby("농장"):
        have = {(int(y), int(m)) for y, m in zip(g["년도"], g["m"])}
        years = sorted({y for y, _ in have})
        best = cur = 0
        for y in years:
            for m in range(1, 13):
                if (y, m) in have:
                    cur += 1
                else:
                    cur = 0
                best = max(best, cur)
            # 다음 해가 인접하지 않으면 끊는다
            if (y + 1) not in years:
                cur = 0
        rows.append({"농장": farm, "run": best,
                     "n_months": int(len(have)),
                     "years": ",".join(str(y) for y in years)})
    return pd.DataFrame(rows)


def audit(path: str | None = None, annual: str | None = None) -> dict:
    wide, dup = load_wide(path)
    long = to_long(wide)
    ann = annual_sows(annual)

    metrics = {}
    for m in sorted(wide["데이터구분"].unique()):
        s = wide[wide["데이터구분"] == m]
        v = s[MONTHS].apply(pd.to_numeric, errors="coerce")
        metrics[m] = {
            "farm_years": int(len(s)), "farms": int(s["농장"].nunique()),
            "years": sorted(int(y) for y in s["년도"].unique()),
            "farm_months": int(v.notna().sum().sum()),
            "month_fill": round(float(v.notna().sum().sum() / (12 * len(s))), 3),
        }

    fy = _months_per_farmyear(wide, TARGET)
    runs = longest_run(long, TARGET)
    t = long[long["데이터구분"] == TARGET]
    lo, hi = RATE_BOUNDS
    out_of_range = int(((t["v"] < lo) | (t["v"] > hi)).sum())

    # 농장별로 여름·겨울 교배분을 **둘 다** 낼 수 있는가
    tt = t.copy()
    tt["sm"] = tt["m"].map(service_month)
    per = tt.groupby("농장")["sm"].agg(
        summer=lambda s: int(s.isin(SUMMER).sum()),
        winter=lambda s: int(s.isin(WINTER).sum()))
    both = per[(per["summer"] > 0) & (per["winter"] > 0)]

    mf, af = set(wide["농장"]), set(ann["농장"])
    tf = set(t["농장"])
    joined = ann[ann["농장"].isin(tf)]

    res = {
        "duplicates": dup,
        "n_farms_file": int(wide["농장"].nunique()),
        "n_rows_long": int(len(long)),
        "years_file": sorted(int(y) for y in wide["년도"].unique()),
        "metrics": metrics,
        "target": TARGET,
        "target_farms": int(t["농장"].nunique()),
        "target_farm_years": int(len(fy)),
        "target_farm_months": int(len(t)),
        "months_per_farmyear": {
            "min": int(fy["n_months"].min()), "median": float(fy["n_months"].median()),
            "max": int(fy["n_months"].max())},
        "value_range": [float(t["v"].min()), float(t["v"].max())],
        "out_of_range": out_of_range,
        "at_100": int((t["v"] == 100.0).sum()),
        "run_ge_12": int((runs["run"] >= 12).sum()),
        "run_ge_24": int((runs["run"] >= 24).sum()),
        "run_max": int(runs["run"].max()),
        "season_farms": int(len(both)),
        "join": {
            "monthly_farms": len(mf), "annual_farms": len(af),
            "overlap": len(mf & af),
            "target_farms_in_annual": len(tf & af),
            "sows_rows": int(len(joined)),
            "sows_missing": int(joined["n_sows"].isna().sum()),
        },
        "verdict": {
            "main": len(both) >= MIN_FARMS_SEASON,
            "main_rule": f"여름·겨울 교배분 둘 다 있는 농장 ≥ {MIN_FARMS_SEASON}",
            "side": int((runs["run"] >= 12).sum()) >= MIN_FARMS_SEQ,
            "side_rule": f"연속 12개월 이상 농장 ≥ {MIN_FARMS_SEQ}",
        },
    }
    return res


def _print_audit(r: dict) -> None:
    d = r["duplicates"]
    print("=" * 78)
    print("  월별 패널 감사")
    print("=" * 78)
    print(f"\n  [중복] 원본 {d['rows_raw']:,}행 → 유일 {d['rows_dedup']:,}행 "
          f"({d['dup_share']:.1%} 가 중복) · 값이 다른 중복 {d['conflicting_keys']}건")
    if d["conflicting_keys"] == 0:
        print("        값이 다른 중복이 0건이라 어느 행을 남길지는 문제가 안 된다.")
    print(f"        다만 반복 횟수가 농장마다 달라 그대로 두면 가중이 왜곡된다.")

    print(f"\n  [규모] 파일 전체 농장 {r['n_farms_file']} · 연도 {r['years_file']}")
    print(f"         (연도별 파일은 2020~2023 인데 월별은 2022 가 없다)")
    print(f"\n  [지표별 보고] 상위 8개")
    print(f"    {'지표':<16}{'농장-연':>7}{'농장':>6}{'농장-월':>8}  연도")
    top = sorted(r["metrics"].items(), key=lambda kv: -kv[1]["farm_months"])[:8]
    for k, v in top:
        ys = ",".join(str(y) for y in v["years"])
        print(f"    {k:<16}{v['farm_years']:>7}{v['farms']:>6}"
              f"{v['farm_months']:>8}  {ys}")

    print(f"\n  [주 타깃 {r['target']}]")
    print(f"    농장 {r['target_farms']} · 농장-연 {r['target_farm_years']} · "
          f"농장-월 {r['target_farm_months']:,}")
    mm = r["months_per_farmyear"]
    print(f"    농장-연당 관측 개월  최소 {mm['min']} · 중앙 {mm['median']:.0f} · "
          f"최대 {mm['max']}")
    print(f"    값 범위 {r['value_range'][0]:.1f}~{r['value_range'][1]:.1f}% · "
          f"범위 밖 {r['out_of_range']} · 정확히 100% 인 값 {r['at_100']}")
    print(f"    최장 연속 관측  12개월 이상 {r['run_ge_12']}농장 · "
          f"24개월 이상 {r['run_ge_24']}농장 · 최대 {r['run_max']}개월")

    j = r["join"]
    print(f"\n  [조인] 월별 {j['monthly_farms']} ∩ 연간 {j['annual_farms']} = "
          f"{j['overlap']}  ·  분만율 농장 중 연간에도 있는 곳 "
          f"{j['target_farms_in_annual']}")
    print(f"         상시모돈 붙는 농장-연 {j['sows_rows']} · "
          f"그중 결측 {j['sows_missing']}")

    v = r["verdict"]
    print(f"\n  [판정]")
    print(f"    주 산출물  {'성립' if v['main'] else '미성립'}  "
          f"— {v['main_rule']} (실제 {r['season_farms']})")
    print(f"    부수 산출물 {'성립' if v['side'] else '미성립'}  "
          f"— {v['side_rule']} (실제 {r['run_ge_12']})")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="farm_monthly_panel")
    ap.add_argument("--audit", action="store_true")
    ap.add_argument("--xlsx", default=None)
    ap.add_argument("--annual", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    if not a.audit:
        ap.error("지금 구현된 단계는 --audit 하나다")
    r = audit(a.xlsx, a.annual)
    _print_audit(r)
    if a.out:
        json.dump(r, open(a.out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\n저장: {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
