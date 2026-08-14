"""월별 번식통계 **패널** — 계절 손실을 농장별로 따라간다.

`farm_monthly.py` 는 전체 곡선 하나를 낸다(여름 교배 −2.97%p). 그 값은
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

MIN_OBS = 2                  # 계절당 최소 관측 개월. 1개월은 그 달의 사고다
SEASON_SHARE = 3.0 / 12.0    # 여름 교배 3개월이 연간 교배의 몇 할인가
REF_SOWS = 300               # 발견 ④·PSY 지렛대와 같은 축에 놓기 위한 기준 규모

# 되돌리기 규칙 — 지표마다 '기록 시점'이 다르다
#   분만율·평균이유  : 분만 시점 기록 → 임신 4개월을 빼야 교배월
#   7일내재귀율      : 이유 직후 사건. 그 달에 교배가 이뤄지므로 기록월 ≈ 교배월
#   임신사고 재발계열: 교배 후 21~42일 → 기록월이 교배월과 같거나 한 달 뒤
SHIFTED = ("분만율", "평균이유", "평균총산", "평균실산")


def _t_crit(df: float) -> float:
    """95% 양측 t 임계값. scipy 없이 쓰려고 표로 둔다(df≥30 은 정규 근사)."""
    table = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447,
             7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228, 12: 2.179, 15: 2.131,
             20: 2.086, 25: 2.060}
    if df >= 30:
        return 1.96
    for k in sorted(table):
        if df <= k:
            return table[k]
    return 2.042


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


ANNUAL_COLS = {"상시모돈수(두)": "n_sows", "PSY(두)": "psy",
               "평균비생산일수(일)": "npd", "분만율(%)": "rate"}


def annual_sows(path: str | None = None) -> pd.DataFrame:
    """농장-연 연간 성적. 규모 보정·원/년 환산·계절 취약도 조인에 쓴다."""
    a = _read(path or ANNUAL_XLSX, "연도별 번식통계")
    out = a[["년도", "농장"]].copy()
    for src, dst in ANNUAL_COLS.items():
        out[dst] = pd.to_numeric(a[src], errors="coerce") if src in a else np.nan
    # 0 두는 상시모돈이 아니라 미기입이다 — 규모 보정에 쓰면 0 으로 나눈다
    out.loc[out["n_sows"] <= 0, "n_sows"] = np.nan
    return out


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


def align(long: pd.DataFrame, metric: str,
          shift: bool | None = None) -> pd.DataFrame:
    """지표 하나를 뽑아 교배월(`sm`) 을 붙인다. 되돌릴 지표만 되돌린다.

    `shift=False` 로 강제하면 되돌리기 **전** 곡선을 낸다. 그 곡선을 나란히
    놓지 않으면 왜 되돌려야 하는지가 안 보인다.
    """
    s = long[long["데이터구분"] == metric].copy()
    do = (metric in SHIFTED) if shift is None else shift
    s["sm"] = s["m"].map(service_month) if do else s["m"]
    s.attrs["basis"] = "교배월" if do else "기록월"
    return s


def overall_season(long: pd.DataFrame, metric: str,
                   shift: bool | None = None) -> dict:
    """전체 여름 vs 겨울. 농장별로 쪼개기 전에 배선이 맞는지 확인하는 값."""
    s = align(long, metric, shift)
    by = s.groupby("sm")["v"].median()
    su = float(by.reindex(SUMMER).mean())
    wi = float(by.reindex(WINTER).mean())
    return {"metric": metric, "basis": s.attrs["basis"], "n": int(len(s)),
            "farms": int(s["농장"].nunique()),
            "by_service_month": {int(k): round(float(v), 2)
                                 for k, v in by.items()},
            "summer": round(su, 2), "winter": round(wi, 2),
            "summer_minus_winter": round(su - wi, 2)}


def farm_seasonal(long: pd.DataFrame, metric: str = TARGET,
                  min_obs: int = MIN_OBS) -> pd.DataFrame:
    """농장별 계절 손실 = 겨울 교배 − 여름 교배 (%p, 양수면 여름에 손해).

    농장-연이 여럿이면 그 농장의 모든 달을 함께 쓴다. 한 해만 있는 농장이
    61개라 해마다 따로 내면 대부분 표본이 3개월씩밖에 안 된다.

    점추정만 내면 관측 3개월짜리 농장과 6개월짜리 농장이 같아 보인다 —
    Welch 표준오차와 95% 구간을 함께 낸다.
    """
    s = align(long, metric)
    rows = []
    for farm, g in s.groupby("농장"):
        su = g.loc[g["sm"].isin(SUMMER), "v"]
        wi = g.loc[g["sm"].isin(WINTER), "v"]
        if len(su) < min_obs or len(wi) < min_obs:
            continue
        vs, vw = su.var(ddof=1) / len(su), wi.var(ddof=1) / len(wi)
        se = float(np.sqrt(vs + vw))
        # Welch–Satterthwaite. 분모가 0 이면(두 계절 다 분산 0) df 를 1 로 둔다
        den = (vs ** 2 / max(1, len(su) - 1)) + (vw ** 2 / max(1, len(wi) - 1))
        df = float((vs + vw) ** 2 / den) if den > 0 else 1.0
        loss = float(wi.mean() - su.mean())
        half = _t_crit(df) * se
        rows.append({"농장": farm, "n_summer": int(len(su)),
                     "n_winter": int(len(wi)),
                     "summer": round(float(su.mean()), 2),
                     "winter": round(float(wi.mean()), 2),
                     "loss": round(loss, 2), "se": round(se, 3),
                     "lo": round(loss - half, 2), "hi": round(loss + half, 2)})
    return pd.DataFrame(rows).sort_values("loss", ascending=False)


def shrink(d: pd.DataFrame) -> dict:
    """관측된 농장별 격차 중 **얼마가 진짜 농장 차이인가**.

    농장마다 계절당 3개월씩이라 손실 점추정은 시끄럽다. 관측 분산은
    (진짜 농장 간 분산) + (표본 오차 분산) 이므로, 뒤를 빼야 앞이 남는다.
    남는 게 0 이면 "여름 대책은 전 농장 공통 처방" 이고, 남으면 "선별 처방" 이다.
    이걸 안 하면 노이즈를 취약 농장으로 지목하게 된다.
    """
    obs = float(d["loss"].var(ddof=1))
    err = float((d["se"] ** 2).mean())
    true = max(0.0, obs - err)
    w = true / (true + d["se"] ** 2)          # 농장별 신뢰 가중
    grand = float(d["loss"].mean())
    sh = grand + w * (d["loss"] - grand)
    return {"var_observed": round(obs, 3), "var_error": round(err, 3),
            "var_true": round(true, 3),
            "true_share": round(true / obs, 3) if obs > 0 else 0.0,
            "sd_observed": round(float(np.sqrt(obs)), 2),
            "sd_true": round(float(np.sqrt(true)), 2),
            "shrunk": sh}


def by_size(d: pd.DataFrame, shrunk: pd.Series, ann: pd.DataFrame,
            years: list[int]) -> dict:
    """규모 보정 — 작은 농장은 분만율이 원래 더 튄다.

    상시모돈 중앙값으로 갈라 원값과 수축값을 나란히 낸다. 수축하면 두 층의
    차이가 줄어드는 만큼이 '작아서 커 보였던' 몫이다. 표준오차와 상시모돈의
    상관을 같이 내서, 이 보정이 필요하다는 근거를 값으로 남긴다.
    """
    a = ann[ann["년도"].isin(years)]
    m = d.assign(shrunk=shrunk.values)
    m["n_sows"] = m["농장"].map(a.groupby("농장")["n_sows"].mean())
    m = m.dropna(subset=["n_sows"])
    if len(m) < 20:
        return {}
    cut = float(m["n_sows"].median())
    out = {"cut_sows": round(cut, 1),
           "rho_se_sows": round(float(
               m["se"].corr(m["n_sows"], method="spearman")), 3)}
    for name, g in (("small", m[m["n_sows"] < cut]),
                    ("large", m[m["n_sows"] >= cut])):
        out[name] = {"n": int(len(g)),
                     "loss": round(float(g["loss"].median()), 2),
                     "shrunk": round(float(g["shrunk"].median()), 2)}
    out["gap_raw"] = round(out["small"]["loss"] - out["large"]["loss"], 2)
    out["gap_shrunk"] = round(out["small"]["shrunk"] - out["large"]["shrunk"], 2)
    return out


def _q(s: pd.Series) -> dict:
    return {k: round(float(s.quantile(v)), 2) for k, v in
            (("p10", .10), ("p25", .25), ("median", .50),
             ("p75", .75), ("p90", .90))}


def to_money(d: pd.DataFrame, ann: pd.DataFrame, years: list[int]) -> dict:
    """%p → 연간 PSY 손실 → 원/년.

        여름 교배 3개월 = 연간 교배의 1/4.
        분만복수 손실률 = 0.25 × (손실%p / 겨울 분만율)
        ΔPSY = PSY × 그 손실률
        원/년 = ΔPSY × (PSY 1두의 두당 가치) × 상시모돈

    두당 가치는 새로 만들지 않고 `farm_economics.levers()` 의 PSY +1두 를 쓴다.
    겨울을 기준으로 잡았으므로 이 값은 **손실 상한**이다 — 냉방으로 여름을
    겨울만큼 만들었을 때 되찾는 몫이지, 장비값을 뺀 순이익이 아니다.
    """
    import farm_economics as fe
    lev = fe.levers(n_sows=REF_SOWS)
    per_sow = float(lev.loc[lev["lever"] == "PSY +1두", "두당효과"].iloc[0])

    a = ann[ann["년도"].isin(years)]
    psy = pd.to_numeric(a["psy"], errors="coerce").groupby(a["농장"]).mean()
    sows = a.groupby("농장")["n_sows"].mean()
    m = d.copy()
    m["psy"] = m["농장"].map(psy)
    m["n_sows"] = m["농장"].map(sows)
    m = m.dropna(subset=["psy", "n_sows"])
    m["d_psy"] = m["psy"] * SEASON_SHARE * (m["loss"] / m["winter"])
    m["won_ref"] = m["d_psy"] * per_sow * REF_SOWS      # 300두 환산 — 비교용
    m["won_farm"] = m["d_psy"] * per_sow * m["n_sows"]  # 실제 규모
    return {"per_sow_won": int(per_sow), "ref_sows": REF_SOWS,
            "n": int(len(m)),
            "d_psy": _q(m["d_psy"]), "won_ref": _q(m["won_ref"]),
            "won_farm": _q(m["won_farm"]),
            "total_won": int(m["won_farm"].sum()),
            "table": m}


def pathways(long: pd.DataFrame) -> dict:
    """여름에 **어느 경로로** 무너지는가.

    분만율만 보면 "떨어진다"까지다. 같은 파일의 다른 지표를 같은 축에 놓으면
    발정이 안 잡히는 건지(재귀율), 붙었다 떨어지는 건지(임신사고), 낳고 잃는
    건지(이유두수)가 갈린다.

    임신사고는 **건수**라 규모에 끌린다. 전 유형을 보고한 농장-월만 추려
    유형별 **구성비**로 바꾼 뒤 계절을 비교한다 — `farm_monthly.accident_mix`
    가 커버리지 함정을 다룬 방식과 같다.
    """
    out = {"metrics": {}, "accidents": {}}
    for metric in ("분만율", "평균이유", "7일내재귀율"):
        s = long[long["데이터구분"] == metric]
        if s["농장"].nunique() < 20:
            continue
        out["metrics"][metric] = overall_season(long, metric)

    acc = long[long["데이터구분"].str.startswith("임신사고")].copy()
    if len(acc):
        acc["key"] = (acc["농장"].astype(str) + "|" + acc["년도"].astype(str)
                      + "|" + acc["m"].astype(str))
        piv = acc.pivot_table(index="key", columns="데이터구분", values="v",
                              aggfunc="sum").dropna()
        tot = piv.sum(axis=1)
        piv = piv[tot > 0]
        share = piv.div(piv.sum(axis=1), axis=0)
        mm = pd.Series([int(k.split("|")[2]) for k in share.index],
                       index=share.index)
        su = share[mm.isin(SUMMER)].mean()
        wi = share[mm.isin(WINTER)].mean()
        out["accidents"] = {
            "n_complete": int(len(share)),
            "n_summer": int(mm.isin(SUMMER).sum()),
            "n_winter": int(mm.isin(WINTER).sum()),
            "basis": "기록월",
            "delta": {k: round(float(su[k] - wi[k]), 4)
                      for k in share.columns},
            "summer": {k: round(float(su[k]), 4) for k in share.columns},
            "winter": {k: round(float(wi[k]), 4) for k in share.columns},
        }
    return out


def _spearman(a: pd.Series, b: pd.Series) -> tuple[float, int]:
    m = pd.concat([a, b], axis=1).dropna()
    if len(m) < 10:
        return float("nan"), int(len(m))
    return float(m.iloc[:, 0].corr(m.iloc[:, 1], method="spearman")), int(len(m))


def join_annual(d: pd.DataFrame, ann_raw: pd.DataFrame,
                years: list[int]) -> dict:
    """계절 취약도가 연간 성적·규모와 붙는가.

    붙으면 계절 취약도가 진단 지표로 선다. 안 붙으면 그것도 결론이다 —
    잘하는 농장도 여름은 못 피한다는 뜻이라 오히려 공통 처방의 근거가 된다.
    """
    a = ann_raw[ann_raw["년도"].isin(years)]
    g = a.groupby("농장")
    cols = {"psy": "PSY", "npd": "비생산일수", "n_sows": "상시모돈",
            "rate": "연간 분만율"}
    base = d.set_index("농장")["loss"]
    out = {}
    for key, label in cols.items():
        if key not in a.columns:
            continue
        rho, n = _spearman(base, g[key].mean())
        out[label] = {"rho": None if rho != rho else round(rho, 3), "n": n}
    return out


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


def season(path: str | None = None, annual: str | None = None) -> dict:
    wide, dup = load_wide(path)
    long = to_long(wide)
    ann = annual_sows(annual)
    years = sorted(int(y) for y in
                   long.loc[long["데이터구분"] == TARGET, "년도"].unique())

    per = farm_seasonal(long, TARGET)
    sh = shrink(per)
    money = to_money(per, ann, years)
    tbl = money.pop("table")

    # 취약한 쪽 / 무던한 쪽을 구간까지 확인해 지목한다
    vulnerable = per[per["lo"] > 0]        # 구간 전체가 0 보다 위 = 여름 손해 확실
    resilient = per[per["hi"] < 0]         # 여름이 오히려 나은 농장

    return {
        "duplicates": dup,
        "years": years,
        "overall": overall_season(long, TARGET),
        "overall_raw_month": overall_season(long, TARGET, shift=False),
        "n_farms": int(len(per)),
        "loss": _q(per["loss"]),
        "loss_mean": round(float(per["loss"].mean()), 2),
        "spread": {k: v for k, v in sh.items() if k != "shrunk"},
        "loss_shrunk": _q(sh["shrunk"]),
        "n_vulnerable": int(len(vulnerable)),
        "n_resilient": int(len(resilient)),
        "worst": [{"loss": float(r.loss), "lo": float(r.lo), "hi": float(r.hi),
                   "n": int(r.n_summer + r.n_winter)}
                  for r in per.head(5).itertuples()],
        "by_size": by_size(per, sh["shrunk"], ann, years),
        "money": money,
        "pathways": pathways(long),
        "join": join_annual(per, ann, years),
        "_per_farm": per, "_money_table": tbl,
    }


def _print_season(r: dict) -> None:
    o = r["overall"]
    print("=" * 78)
    print("  농장별 계절 손실 → 원/년")
    print("=" * 78)
    print(f"\n  [배선 확인] 전체 {o['basis']} 기준 · {o['farms']}농장 · "
          f"{o['n']}농장-월")
    print("   " + " ".join(f"{m:>2}월{o['by_service_month'].get(m, 0):>6.1f}"
                           for m in range(1, 13)))
    print(f"    여름 교배 {o['summer']} vs 겨울 교배 {o['winter']}  →  "
          f"{o['summer_minus_winter']:+.2f}%p")
    print(f"    (중복 제거 전 −2.70%p / n 4,470. 결론은 같고 폭만 커진다)")
    rw = r["overall_raw_month"]
    print(f"    되돌리기 전({rw['basis']}) 은 {rw['summer_minus_winter']:+.2f}%p "
          f"— 최저가 11월로 잡혀 여름이 가려진다")

    q, s = r["loss"], r["spread"]
    print(f"\n  [농장별 손실] 겨울 − 여름, 양수면 여름에 손해 · {r['n_farms']}농장")
    print(f"    p10 {q['p10']:+.1f} · p25 {q['p25']:+.1f} · 중앙 "
          f"{q['median']:+.1f} · p75 {q['p75']:+.1f} · p90 {q['p90']:+.1f} %p")
    print(f"    구간이 통째로 0 보다 위인 농장 {r['n_vulnerable']} · "
          f"통째로 아래(여름이 오히려 나음) {r['n_resilient']}")

    print(f"\n  [이 격차가 진짜인가] 관측 분산 {s['var_observed']} = "
          f"농장 차이 {s['var_true']} + 표본 오차 {s['var_error']}")
    print(f"    진짜 농장 차이의 몫 {s['true_share']:.0%} · "
          f"관측 SD {s['sd_observed']} → 수축 후 SD {s['sd_true']} %p")
    z = r["loss_shrunk"]
    print(f"    수축 후 분포  p10 {z['p10']:+.1f} · 중앙 {z['median']:+.1f} · "
          f"p90 {z['p90']:+.1f} %p")

    b = r.get("by_size") or {}
    if b:
        print(f"\n  [규모 보정] 상시모돈 중앙 {b['cut_sows']:.0f}두로 가름 · "
              f"표준오차와 상시모돈 ρ {b['rho_se_sows']:+.3f}")
        print(f"    작은 농장({b['small']['n']})  원값 {b['small']['loss']:+.2f}"
              f" → 수축 {b['small']['shrunk']:+.2f}")
        print(f"    큰 농장({b['large']['n']})    원값 {b['large']['loss']:+.2f}"
              f" → 수축 {b['large']['shrunk']:+.2f}")
        print(f"    층간 차이 {b['gap_raw']:+.2f} → {b['gap_shrunk']:+.2f} %p "
              f"— 줄어든 만큼이 '작아서 커 보였던' 몫이다")

    m = r["money"]
    print(f"\n  [원/년 환산] 손실 상한 · {m['n']}농장 · PSY 1두 = "
          f"{m['per_sow_won']:,}원/모돈")
    dp, wr, wf = m["d_psy"], m["won_ref"], m["won_farm"]
    print(f"    ΔPSY   p25 {dp['p25']:+.2f} · 중앙 {dp['median']:+.2f} · "
          f"p90 {dp['p90']:+.2f} 두")
    print(f"    {m['ref_sows']}두 환산  p25 {wr['p25']/1e4:,.0f} · 중앙 "
          f"{wr['median']/1e4:,.0f} · p90 {wr['p90']/1e4:,.0f} 만원/년")
    print(f"    실제 규모   중앙 {wf['median']/1e4:,.0f} 만원/년 · "
          f"{m['n']}농장 합 {m['total_won']/1e8:,.1f} 억원/년")

    p = r["pathways"]
    print(f"\n  [무너지는 경로] 같은 계절 축에 올린 다른 지표")
    for k, v in p["metrics"].items():
        print(f"    {k:<12}({v['basis']}, {v['farms']}농장)  여름 {v['summer']} "
              f"vs 겨울 {v['winter']}  →  {v['summer_minus_winter']:+.2f}")
    a = p.get("accidents") or {}
    if a.get("delta"):
        print(f"\n    임신사고 구성비 변화 — 전 유형 보고 {a['n_complete']}농장-월"
              f" (여름 {a['n_summer']} · 겨울 {a['n_winter']}, {a['basis']})")
        for k, v in sorted(a["delta"].items(), key=lambda kv: -abs(kv[1]))[:5]:
            print(f"      {k:<16}{a['winter'][k]:>7.1%} → {a['summer'][k]:>6.1%}"
                  f"   {v:+.1%}p")

    print(f"\n  [계절 취약도 × 연간 성적] Spearman ρ")
    for k, v in r["join"].items():
        rho = "n/a" if v["rho"] is None else f"{v['rho']:+.3f}"
        print(f"    {k:<10}{rho}  (n {v['n']})")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="farm_monthly_panel")
    ap.add_argument("--audit", action="store_true")
    ap.add_argument("--season", action="store_true")
    ap.add_argument("--xlsx", default=None)
    ap.add_argument("--annual", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    if not (a.audit or a.season):
        ap.error("--audit 또는 --season 을 고를 것")
    if a.audit:
        r = audit(a.xlsx, a.annual)
        _print_audit(r)
    else:
        r = season(a.xlsx, a.annual)
        _print_season(r)
        r = {k: v for k, v in r.items() if not k.startswith("_")}
    if a.out:
        json.dump(r, open(a.out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\n저장: {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
