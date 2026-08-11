"""농장 경영 — 생산비·사료·손익, 그리고 **어느 지렛대가 돈이 되는가**.

앞의 모듈들은 각자 성적을 다뤘다. 발정 탐지는 수태율을, 배치는 AIAO 를,
사육단계는 육성률을 본다. 그런데 농가가 실제로 관리하는 것은 **돈**이고,
성적은 그 수단이다. 이 모듈은 흩어진 성적을 하나의 손익으로 합쳐
"어디를 고치면 얼마가 되는가"에 답한다.

두 가지를 조심했다.

**1) 사료비가 절반을 넘는다.** 두당 생산비에서 사료가 가장 큰 덩어리이므로,
FCR 0.1 개선이 PSY 1두 개선보다 클 수 있다. 번식 지표만 보고 투자 우선순위를
정하면 큰 것을 놓친다. 그래서 지렛대를 **같은 단위(원/모돈/년)로 환산해**
나란히 세운다.

**2) 개선 효과를 겹쳐 세지 않는다.** 발정 탐지는 수태율을 올려 회전율을
높이고, 배치·위생은 육성률을 올린다. 둘은 서로 다른 경로라 더할 수 있지만,
같은 경로를 두 모듈이 각각 주장하면 이중 계산이 된다. 여기서는 경로별로
한 번씩만 센다.

단가는 시세와 농장에 따라 크게 변하므로 전부 인자로 뺐다. 기본값은 국내
통상 수준의 어림값이며, **결론은 절대 금액이 아니라 지렛대의 순서**다.

    python competition/src/farm_economics.py
"""
from __future__ import annotations

import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import growth_flow as gf  # noqa: E402

# 단계별 사료요구율(FCR)과 사료 단가(원/kg). 자돈사료가 가장 비싸다.
FEED = {
    "이유자돈": {"fcr": 1.6, "price": 900},
    "육성돈": {"fcr": 2.4, "price": 650},
    "비육돈": {"fcr": 3.2, "price": 600},
}

# 두당 비사료 비용(원) — 농장·연도에 따라 크게 변한다
NON_FEED = {
    "약품·백신": 12000, "노무비": 45000, "수도광열": 15000,
    "감가상각·수선": 35000, "기타(수송·판매)": 18000,
}
SOW_COST_PER_YEAR = 900_000     # 모돈 1두 유지비(사료·상각·후보돈 상각 포함)
DRESSING_RATE = 0.76            # 지육률
PORK_PRICE = 5200               # 지육 단가(원/kg) — 시세 변동 큼


def feed_plan(stages=None) -> pd.DataFrame:
    """단계별 증체·사료 요구량·사료비."""
    rows = []
    for name, a0, a1, w0, w1, _barn, _area in (stages or gf.STAGES):
        if name not in FEED:
            continue
        f = FEED[name]
        gain = w1 - w0
        kg = gain * f["fcr"]
        rows.append({"stage": name, "days": a1 - a0, "gain_kg": round(gain, 1),
                     "fcr": f["fcr"], "feed_kg": round(kg, 1),
                     "price": f["price"], "cost": int(round(kg * f["price"]))})
    d = pd.DataFrame(rows)
    if len(d):
        d.attrs["total_feed_kg"] = round(float(d["feed_kg"].sum()), 1)
        d.attrs["total_gain_kg"] = round(float(d["gain_kg"].sum()), 1)
        d.attrs["overall_fcr"] = round(
            float(d["feed_kg"].sum() / max(1e-9, d["gain_kg"].sum())), 2)
        d.attrs["feed_cost"] = int(d["cost"].sum())
    return d


def cost_per_pig(feed_cost: int | None = None,
                 non_feed: dict | None = None) -> dict:
    """출하 1두당 생산비 구조 — 사료가 얼마를 차지하는가."""
    fc = feed_plan().attrs["feed_cost"] if feed_cost is None else feed_cost
    nf = dict(NON_FEED if non_feed is None else non_feed)
    total = fc + sum(nf.values())
    parts = {"사료비": fc, **nf}
    return {"total": int(total),
            "parts": parts,
            "share": {k: round(v / total, 3) for k, v in parts.items()},
            "feed_share": round(fc / total, 3)}


def revenue_per_pig(market_kg: float = gf.MARKET_WEIGHT,
                    dressing: float = DRESSING_RATE,
                    price: int = PORK_PRICE) -> dict:
    """출하 1두당 수취액."""
    carcass = market_kg * dressing
    return {"live_kg": market_kg, "carcass_kg": round(carcass, 1),
            "price_per_kg": price, "revenue": int(round(carcass * price))}


def per_sow_year(psy: float, post_wean_survival: float,
                 market_kg: float = gf.MARKET_WEIGHT,
                 price: int = PORK_PRICE,
                 sow_cost: int = SOW_COST_PER_YEAR) -> dict:
    """모돈 1두당 연간 손익 — 모든 성적이 여기로 모인다.

    MSY = PSY × 이유후 육성률. 출하두수에 두당 마진을 곱하고 모돈 유지비를 뺀다.
    """
    msy = psy * post_wean_survival
    rev = revenue_per_pig(market_kg, price=price)["revenue"]
    cost = cost_per_pig()["total"]
    margin = rev - cost
    return {"psy": round(psy, 2), "survival": round(post_wean_survival, 3),
            "msy": round(msy, 2),
            "revenue_per_pig": rev, "cost_per_pig": cost,
            "margin_per_pig": margin,
            "gross_per_sow": int(round(msy * margin)),
            "sow_cost": sow_cost,
            "net_per_sow": int(round(msy * margin - sow_cost))}


def breakeven_price(psy: float, post_wean_survival: float,
                    market_kg: float = gf.MARKET_WEIGHT,
                    dressing: float = DRESSING_RATE,
                    sow_cost: int = SOW_COST_PER_YEAR) -> int:
    """손익분기 지육 단가(원/kg).

    모돈 유지비까지 덮으려면 얼마를 받아야 하는가. 시세가 이 아래로 내려가면
    성적이 좋아도 적자다 — 그래서 시세만 보지 말고 이 값을 알고 있어야 한다.
    """
    msy = max(1e-6, psy * post_wean_survival)
    cost = cost_per_pig()["total"]
    need_per_pig = cost + sow_cost / msy
    return int(round(need_per_pig / (market_kg * dressing)))


def levers(n_sows: int = 300, psy: float = 24.0, survival: float = 0.86,
           price: int = PORK_PRICE) -> pd.DataFrame:
    """개선 지렛대를 **같은 단위(원/년)** 로 환산해 나란히 세운다.

    번식 지표만 보면 사료를 놓치고, 사료만 보면 번식을 놓친다. 각 지렛대를
    현실적인 1단위씩 움직여 농장 전체 연간 손익 변화를 재고 크기순으로 낸다.
    """
    base = per_sow_year(psy, survival, price=price)["net_per_sow"] * n_sows

    def farm_net(p=psy, s=survival, fcr_delta=0.0, pr=price):
        fp = feed_plan()
        fc = int(round(sum(
            (r.gain_kg * max(0.1, r.fcr + fcr_delta)) * r.price
            for r in fp.itertuples(index=False))))
        cost = cost_per_pig(feed_cost=fc)["total"]
        rev = revenue_per_pig(price=pr)["revenue"]
        msy = p * s
        return int(round((msy * (rev - cost) - SOW_COST_PER_YEAR) * n_sows))

    rows = [
        ("PSY +1두", "발정 탐지·적기 교배 → 수태율·회전율",
         farm_net(p=psy + 1) - base),
        ("이유후 육성률 +2%p", "배치·AIAO·환경 → 폐사 감소",
         farm_net(s=min(1.0, survival + 0.02)) - base),
        ("FCR -0.1", "사료 관리·밀도 개선",
         farm_net(fcr_delta=-0.1) - base),
        ("지육 단가 +100원", "시세(농장이 못 바꾼다)",
         farm_net(pr=price + 100) - base),
    ]
    d = pd.DataFrame(rows, columns=["lever", "경로", "연간효과"])
    d["두당효과"] = (d["연간효과"] / n_sows).round(0).astype(int)
    d.attrs["base_net"] = base
    d.attrs["n_sows"] = n_sows
    return d.sort_values("연간효과", ascending=False).reset_index(drop=True)


def app_value(n_sows: int = 300, psy: float = 24.0, survival: float = 0.86,
              d_psy: float = 0.8, d_survival: float = 0.01) -> dict:
    """이 앱이 만드는 값 — **경로별로 한 번씩만** 센다.

    발정 탐지·적기 교배는 수태율을 통해 회전율(PSY)을 올리고, 배치·AIAO 관리는
    폐사를 줄여 육성률을 올린다. 두 경로는 서로 다르므로 더할 수 있다. 같은
    경로를 두 번 세지 않도록 각 개선폭은 한 곳에서만 쓴다.
    """
    base = per_sow_year(psy, survival)["net_per_sow"] * n_sows
    repro = per_sow_year(psy + d_psy, survival)["net_per_sow"] * n_sows - base
    grow = per_sow_year(psy, min(1.0, survival + d_survival))[
        "net_per_sow"] * n_sows - base
    both = per_sow_year(psy + d_psy, min(1.0, survival + d_survival))[
        "net_per_sow"] * n_sows - base
    return {"base_net": base, "repro_path": repro, "growth_path": grow,
            "combined": both, "sum_of_parts": repro + grow,
            "interaction": both - (repro + grow),
            "d_psy": d_psy, "d_survival": d_survival, "n_sows": n_sows}


def main() -> int:
    print("=== 단계별 사료 — 생산비의 가장 큰 덩어리 ===")
    fp = feed_plan()
    print(f"  {'단계':<8} {'증체':>6} {'FCR':>5} {'사료':>7} {'단가':>6} {'사료비':>9}")
    for r in fp.itertuples(index=False):
        print(f"  {r.stage:<8} {r.gain_kg:>5.0f}kg {r.fcr:>5.1f} "
              f"{r.feed_kg:>6.0f}kg {r.price:>5}원 {r.cost:>8,}원")
    print(f"  합계 증체 {fp.attrs['total_gain_kg']:.0f}kg · "
          f"사료 {fp.attrs['total_feed_kg']:.0f}kg · "
          f"전체 FCR {fp.attrs['overall_fcr']} · "
          f"사료비 {fp.attrs['feed_cost']:,}원")

    print("\n=== 출하 1두당 생산비 구조 ===")
    c = cost_per_pig()
    for k, v in sorted(c["parts"].items(), key=lambda x: -x[1]):
        bar = "█" * int(28 * c["share"][k])
        print(f"  {k:<12} {v:>8,}원 {c['share'][k]:>6.1%} {bar}")
    print(f"  {'합계':<12} {c['total']:>8,}원")
    print(f"  → 사료가 {c['feed_share']:.0%}. **FCR 0.1 개선이 PSY 1두보다"
          f" 클 수 있다**는 뜻이고,")
    print("    번식 지표만 보고 투자 우선순위를 정하면 큰 것을 놓친다.")

    r = revenue_per_pig()
    print(f"\n=== 두당 수취·마진 ===")
    print(f"  생체 {r['live_kg']:.0f}kg × 지육률 {DRESSING_RATE:.0%} = "
          f"지육 {r['carcass_kg']:.0f}kg × {r['price_per_kg']:,}원 "
          f"= {r['revenue']:,}원")
    print(f"  마진 {r['revenue'] - c['total']:,}원/두")

    print("\n=== 모돈 1두당 연간 손익 ===")
    print(f"  {'구성':<16} {'PSY':>5} {'육성률':>6} {'MSY':>5} "
          f"{'총이익':>11} {'순이익':>11}")
    for label, (p, s) in {"국내 평균 수준": (22.8, 0.807),
                          "우리 목표": (24.0, 0.86),
                          "부경 상위": (27.3, 0.846),
                          "덴마크 수준": (31.3, 0.933)}.items():
        e = per_sow_year(p, s)
        print(f"  {label:<16} {e['psy']:>5.1f} {e['survival']:>6.1%} "
              f"{e['msy']:>5.1f} {e['gross_per_sow']:>10,}원 "
              f"{e['net_per_sow']:>10,}원")
    be = breakeven_price(24.0, 0.86)
    print(f"  손익분기 지육단가 {be:,}원/kg (현재 가정 {PORK_PRICE:,}원)")
    print("  ※ 시세가 이 아래면 성적이 좋아도 적자다. 시세만 보지 말고 이 값을")
    print("    알고 있어야 감산·증산을 판단할 수 있다.")

    print(f"\n=== 개선 지렛대 — 같은 단위로 세워 비교 (모돈 300두) ===")
    lv = levers(300)
    print(f"  {'지렛대':<20} {'연간효과':>13} {'모돈두당':>10}  경로")
    for r2 in lv.itertuples(index=False):
        print(f"  {r2.lever:<20} {r2.연간효과:>12,}원 "
              f"{r2.두당효과:>9,}원  {r2.경로}")
    print(f"  (기준 순이익 {lv.attrs['base_net']:,}원/년)")

    print(f"\n=== 이 앱이 만드는 값 — 경로별로 한 번씩만 ===")
    v = app_value(300)
    print(f"  번식 경로 (발정 탐지 → PSY +{v['d_psy']}): "
          f"{v['repro_path']:,}원/년")
    print(f"  사육 경로 (배치·AIAO → 육성률 +{v['d_survival']:.0%}): "
          f"{v['growth_path']:,}원/년")
    print(f"  동시 적용 {v['combined']:,}원 · 단순 합 {v['sum_of_parts']:,}원 "
          f"· 상호작용 {v['interaction']:+,}원")
    print("  ※ 두 경로는 서로 다르므로 더할 수 있다. 다만 같은 경로를 두 모듈이")
    print("    각각 주장하면 이중 계산이 되므로 여기서는 한 번씩만 셌다.")

    print("\n※ 단가·비용은 시세와 농장에 따라 크게 변한다. 결론으로 삼을 것은"
          "\n  절대 금액이 아니라 **지렛대의 순서**다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
