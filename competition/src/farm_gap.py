"""내 농장이 국내 분포에서 **얼마나 멀어져 있나** — 순위가 아니라 거리.

"상위 40%입니다"는 얼마나 고쳐야 하는지 알려주지 않는다. 필요한 건
"NPD 가 중앙값보다 18일 많다 → PSY 로 치면 2.2두 손해 → 연 X원"이다.
순위는 위치만 말하고, **거리는 크기를 말한다.**

## 왜 회귀를 안 쓰는가

PSY 는 통계 모형이 아니라 **정의로 분해된다**. 466농장으로 확인:

    회전율 = (365 − NPD_연간) / (임신 + 포유)      86.2% 가 오차 0.05 이내
    PSY   = 이유두수 × 회전율

처음에 `365/(임신+포유+NPD)` 로 쟀다가 오차 −0.32 가 나왔다 — 이 데이터의
NPD 는 **주기당이 아니라 연간**이다. 정의를 맞추자 오차가 −0.01 로 떨어졌다.

정의로 분해되면 인과 추론이 필요 없다. 각 지표를 중앙값으로 되돌렸을 때
PSY 가 얼마 오르는지 **정확히** 계산된다. 다만 지표끼리 맞물려 있으므로
(포유기간을 줄이면 이유두수가 준다) 개별 효과의 합이 전체와 같지는 않다 —
그래서 합산 대신 **하나씩 되돌린 값**을 크기순으로 낸다.

    python competition/src/farm_gap.py --npd 62 --weaned 10 --farrowing 74
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

STATS = os.path.join(ROOT, "competition", "data", "korean_farm_stats.json")

# 이 지표들만 PSY 항등식에 직접 들어간다. 나머지(분만율·재귀발정)는 NPD 를
# 통해 간접적으로 작용하므로 따로 다룬다(아래 INDIRECT).
DIRECT = ["weaned", "npd", "lactation"]
# 항등식에 들어가지만 **농장이 못 바꾸는** 값. PSY 계산에는 반영하되
# "되돌리면 얼마" 를 개선 지렛대로 세지는 않는다 — 임신기간을 줄이라는
# 권고는 성립하지 않는다.
CONSTANT = ["gestation"]
INDIRECT = ["farrowing_rate", "wean_to_estrus"]
KO = {"weaned": "이유두수(복당)", "npd": "비생산일수(연간)",
      "lactation": "포유기간", "farrowing_rate": "분만율(%)",
      "wean_to_estrus": "재귀발정일", "gestation": "임신기간",
      "psy": "PSY", "turnover": "모돈회전율"}
# 값이 클수록 좋은 지표 / 작을수록 좋은 지표
HIGHER_BETTER = {"weaned", "farrowing_rate", "psy", "turnover"}
GESTATION = 115.0     # 실측 중앙. 농장이 못 바꾸는 상수다.


def load_stats(path: str | None = None) -> dict:
    p = path or STATS
    if not os.path.exists(p):
        raise SystemExit(f"{p} 가 없다. korean_farm_stats.py 를 먼저 돌릴 것.")
    return json.load(open(p, encoding="utf-8"))


def psy_from(weaned: float, npd: float, lactation: float,
             gestation: float = GESTATION) -> float:
    """PSY = 이유두수 × (365 − NPD_연간) / (임신 + 포유).

    분모가 0 이하가 되는 입력(NPD 365 이상)은 물리적으로 불가능하므로 막는다.
    """
    cyc = gestation + lactation
    if cyc <= 0:
        raise ValueError("임신+포유 가 0 이하다")
    if npd >= 365:
        raise ValueError("연간 비생산일수가 365 이상일 수 없다")
    return weaned * (365.0 - npd) / cyc


def npd_floor_annual(b: dict) -> float:
    """번식 상수 → **이론 최소** 연간 비생산일수.

    재발정·유산·도태 대기가 전혀 없고 이유 후 곧바로 재교배된다고 볼 때,
    한 주기에서 비생산인 구간은 이유~재교배 뿐이다. 연간으로 쓰려면
    회전율을 곱한다(주기당 7일 × 2.52회 = 17.6일/년).

    pigflow.calc.kpis 의 npd_floor_annual_days 와 같은 식이다. 여기 다시
    두는 이유는 시뮬레이션을 돌리지 않고 상수만으로 견주기 위해서다 —
    두 곳이 어긋나지 않는지 smoke_test 가 확인한다.
    """
    cycle = (b["wean_to_service_days"] + b["gestation_days"]
             + b["lactation_days"])
    return round(b["wean_to_service_days"] * (365.0 / cycle), 1)


def robust_z(value: float, q: dict) -> float:
    """중앙값에서 몇 IQR 만큼 떨어져 있나.

    표준편차 대신 IQR 을 쓰는 이유: NPD 는 오른쪽으로 길게 늘어진 분포라
    (평균 48.5 vs 중앙 43.0) 표준편차가 소수 농장에 끌려간다.
    """
    iqr = q["p75"] - q["p25"]
    return (value - q["p50"]) / iqr if iqr > 1e-9 else 0.0


def band(z: float, higher_better: bool) -> str:
    """거리를 말로. 부호는 **좋은 쪽이 +** 가 되도록 뒤집는다."""
    g = z if higher_better else -z
    if g >= 1.0:
        return "매우 좋음"
    if g >= 0.3:
        return "좋음"
    if g > -0.3:
        return "중앙 부근"
    if g > -1.0:
        return "나쁨"
    return "매우 나쁨"


def diagnose(farm: dict, stats: dict | None = None,
             n_sows: int | None = None) -> dict:
    """농장 값 → 지표별 거리 + 각각을 중앙값으로 되돌렸을 때의 PSY 회수량."""
    st = stats or load_stats()
    q = st["quantiles"]
    med = {k: q[k]["p50"] for k in q}

    ident = DIRECT + CONSTANT
    cur = {k: float(farm.get(k, med[k])) for k in ident}
    _psy = lambda d: psy_from(d["weaned"], d["npd"], d["lactation"],  # noqa: E731
                              d["gestation"])
    base_psy = _psy(cur)
    med_psy = _psy({k: med[k] for k in ident})

    rows = []
    for k in ident + INDIRECT:
        if k not in q:
            continue
        v = float(farm.get(k, med[k]))
        z = robust_z(v, q[k])
        hb = k in HIGHER_BETTER
        row = {"metric": k, "name_ko": KO.get(k, k), "value": round(v, 2),
               "median": round(med[k], 2), "gap": round(v - med[k], 2),
               "iqr_z": round(z, 2), "band": band(z, hb),
               "higher_better": hb, "direct": k in ident,
               "actionable": k in DIRECT}
        if k in ident:
            # 이 지표 **하나만** 중앙값으로 되돌렸을 때
            trial = dict(cur)
            trial[k] = med[k]
            row["psy_if_median"] = round(_psy(trial), 2)
            row["psy_recover"] = round(row["psy_if_median"] - base_psy, 2)
        else:
            # 간접 지표는 NPD 를 통해 작용한다. 정의로 환산되지 않으므로
            # PSY 로 못 바꾸고 거리만 보고한다 — 없는 인과를 지어내지 않는다.
            row["psy_recover"] = None
        rows.append(row)

    direct = [r for r in rows if r["actionable"]]
    rows.sort(key=lambda r: -(r["psy_recover"] or -1e9))
    # **'중앙 농장' 은 실재하지 않는다.** 지표마다 중앙값을 뽑아 항등식에 넣은
    # 합성 농장이라 25.34 가 나오는데, PSY 열 자체의 중앙값은 24.1 이다.
    # 중앙값은 함수를 통과해도 중앙값이 아니다(각 지표의 중앙이 한 농장에서
    # 동시에 나타나지 않는다). 격차를 "중앙 농장보다 낫다/못하다"로 읽는 건
    # 되지만, 25.34 를 "평균 농장의 PSY"로 인용하면 1.2두 부풀린다.
    out = {
        "psy": round(base_psy, 2),
        "psy_median_farm": round(med_psy, 2),
        "psy_median_observed": round(q["psy"]["p50"], 2) if "psy" in q else None,
        "psy_gap": round(base_psy - med_psy, 2),
        "rows": rows,
        # 전부 중앙값으로 되돌리면 — 개별 회수량의 합과 다르다(항이 곱해지므로)
        "psy_all_median": round(med_psy, 2),
        "sum_of_parts": round(sum(r["psy_recover"] for r in direct
                                  if r["psy_recover"] and r["psy_recover"] > 0),
                              2),
    }
    if n_sows:
        out["won_per_year"] = _money(out, n_sows)
    return out


def _money(diag: dict, n_sows: int) -> list:
    """PSY 회수량 → 원/년. farm_economics 의 두당 마진을 쓴다."""
    import farm_economics as fe
    surv = 0.86
    base = fe.per_sow_year(diag["psy"], surv)["net_per_sow"] * n_sows
    out = []
    for r in diag["rows"]:
        if not r.get("actionable"):
            continue
        if not r.get("psy_recover") or r["psy_recover"] <= 0:
            continue
        got = fe.per_sow_year(diag["psy"] + r["psy_recover"],
                              surv)["net_per_sow"] * n_sows
        out.append({"metric": r["metric"], "name_ko": r["name_ko"],
                    "psy_recover": r["psy_recover"], "won_year": got - base})
    return out


def _print(d: dict, n_sows: int | None) -> None:
    print("=" * 74)
    print(f"  내 농장 PSY {d['psy']} · 국내 중앙 농장 {d['psy_median_farm']} "
          f"→ 격차 {d['psy_gap']:+.2f}두")
    if d.get("psy_median_observed"):
        print(f"  ('중앙 농장' 은 지표별 중앙값을 항등식에 넣은 합성값이다. "
              f"실제 PSY 열의\n   중앙은 {d['psy_median_observed']} — "
              f"모든 지표가 동시에 중앙인 농장은 없다.)")
    print("=" * 74)
    print(f"\n  {'지표':<16}{'내 값':>9}{'중앙':>9}{'차이':>9}{'IQR거리':>9}"
          f"{'평가':>12}{'되돌리면':>10}")
    print("  " + "-" * 72)
    for r in d["rows"]:
        if r["psy_recover"] is None:
            rec = "—"
        elif not r["actionable"]:
            rec = f"({r['psy_recover']:+.2f})"      # 상수 — 지렛대 아님
        else:
            rec = f"PSY {r['psy_recover']:+.2f}"
        print(f"  {r['name_ko']:<16}{r['value']:>9}{r['median']:>9}"
              f"{r['gap']:>+9}{r['iqr_z']:>+9}{r['band']:>12}{rec:>12}")
    print("\n  * IQR거리 = (내 값 − 중앙) ÷ 사분위범위. 표준편차 대신 IQR 을 쓰는")
    print("    이유는 NPD 처럼 한쪽으로 늘어진 분포에서 표준편차가 소수 농장에")
    print("    끌려가기 때문이다.")
    print("  * '되돌리면' = 그 지표 **하나만** 중앙값으로 바꿨을 때의 PSY 변화.")
    print("    분만율·재귀발정일은 NPD 를 통해 간접 작용해 정의로 환산되지")
    print("    않으므로 거리만 보고한다 — 없는 인과를 지어내지 않는다.")
    print("    괄호친 값(임신기간)은 항등식에는 들어가지만 농장이 못 바꾸므로")
    print("    개선 지렛대에서 뺀다.")
    parts, whole = d["sum_of_parts"], d["psy_all_median"] - d["psy"]
    if parts > 0:
        print(f"\n  개별 회수량 합 {parts:+.2f} vs 전부 되돌렸을 때 {whole:+.2f}"
              f" — 항이 곱해지므로 단순 합산은 맞지 않는다.")
    if n_sows and d.get("won_per_year"):
        print(f"\n  금액 환산 (모돈 {n_sows}두 · 이유후 육성률 86% 가정)")
        for m in d["won_per_year"]:
            print(f"    {m['name_ko']:<16}PSY {m['psy_recover']:+.2f} → "
                  f"{m['won_year']:>15,}원/년")


def main(argv=None) -> int:
    st = load_stats()
    med = {k: v["p50"] for k, v in st["quantiles"].items()}
    ap = argparse.ArgumentParser(
        prog="farm_gap", description="국내 분포에서 얼마나 멀어져 있나")
    keys = DIRECT + CONSTANT + INDIRECT
    for k in keys:
        ap.add_argument(f"--{k.replace('_', '-')}", type=float,
                        default=med.get(k),
                        help=f"{KO.get(k, k)} (기본 = 국내 중앙 {med.get(k)})")
    ap.add_argument("--sows", type=int, default=None, help="모돈 두수(금액 환산)")
    ap.add_argument("--program", action="store_true",
                    help="내 프로그램의 기본 가정값을 넣고 실측과 견준다")
    a = ap.parse_args(argv)
    farm = {k: getattr(a, k) for k in keys}
    if a.program:
        sys.path.insert(0, os.path.join(ROOT, "competition"))
        from pigflow.config import BREEDING_DEFAULTS as B
        farm.update(weaned=B["weaned_per_litter"],
                    lactation=B["lactation_days"],
                    gestation=B["gestation_days"],
                    farrowing_rate=B["farrowing_rate"] * 100,
                    wean_to_estrus=B["wean_to_service_days"],
                    npd=npd_floor_annual(B))
        print("  ※ '내 값' = pigflow 기본 가정값(실제 농장 기록이 아니다)\n")
    d = diagnose(farm, st, a.sows)
    _print(d, a.sows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
