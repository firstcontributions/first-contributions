"""사육단계 관리 — 번식에서 출하까지. 전체 관리로 넓히는 축.

지금까지 이 프로젝트는 **번식돈만** 다뤘다(발정→교배→임신→분만→이유). 그런데
농장의 돈은 거기서 끝나지 않는다. 이유 이후 자돈사·육성사·비육사를 거쳐
약 175일령에 출하되며, **모돈 성적(PSY)이 좋아도 이유 후에 죽으면 수익(MSY)이
안 나온다.** 국내가 덴마크에 뒤지는 큰 몫이 바로 이 구간이다.

    PSY(이유두수) ──[이유 후 육성률]──> MSY(출하두수)
    한국  22.8 ──────── 80.7% ────────> 18.4
    덴마크 31.3 ──────── 93.3% ────────> 29.2

즉 **국내 이유후 폐사율이 덴마크의 약 3배**다. 번식만 붙들고 있으면 이 손실이
보이지 않는다.

이 모듈이 다루는 것:
  1) 단계별 일정·체중  이유 배치가 언제 어느 돈사에 있고 몇 kg 인지
  2) **사육밀도**      축산법 시행령 기준 대비 과밀 여부. 밀사는 증체·사료효율을
                      떨어뜨리고, 배치가 밀리면 바로 여기서 터진다
  3) **지연 개체**     정상 흐름에서 뒤처진 돼지(tail-ender). 어린 배치로
                      되돌리면 AIAO 가 깨지므로 **역류를 금지**한다
  4) PSY·MSY          벤치마크 대조 — 어느 구간에서 새는지

    python competition/src/growth_flow.py
"""
from __future__ import annotations

import os
import sys
from datetime import timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import repro_calendar as rc  # noqa: E402

# (단계, 시작일령, 종료일령, 시작체중kg, 종료체중kg, 돈사, 법정 두당면적㎡)
# 면적은 「축산법 시행령」 별표1 기준. 새끼돼지 0.2~0.3 · 육성돈 0.45 · 비육돈 0.8
STAGES = [
    ("포유자돈", 0, 28, 1.4, 8.0, "분만사", None),
    ("이유자돈", 28, 70, 8.0, 30.0, "자돈사", 0.30),
    ("육성돈", 70, 105, 30.0, 60.0, "육성사", 0.45),
    ("비육돈", 105, 175, 60.0, 115.0, "비육사", 0.80),
]
MARKET_AGE = 175
MARKET_WEIGHT = 115.0

# 단계별 폐사율(구간 누적). 이유 직후 자돈사가 가장 취약하다 — 모체이행항체가
# 3~4주에 최저점이고 그 시점이 이유와 겹친다.
MORTALITY = {"포유자돈": 0.07, "이유자돈": 0.03, "육성돈": 0.01, "비육돈": 0.01}

# 성적 벤치마크 (조사 주체·연도가 달라 단일 수치로 일반화하면 안 된다)
BENCHMARKS = {
    "한돈팜스 전체 평균": {"psy": 22.8, "msy": 18.4},
    "부경양돈농협 상위": {"psy": 27.3, "msy": 23.1},
    "덴마크": {"psy": 31.3, "msy": 29.2},
}

# 지연 개체 판정 — 같은 배치 평균 대비 이만큼 뒤처지면 tail-ender
TAIL_ENDER_WEIGHT_GAP = 0.85     # 배치 평균 체중의 85% 미만
TAIL_ENDER_AGE_OVER = 14         # 예상 출하일령보다 이만큼 초과


def stage_at(age_days: int):
    """일령 → (단계, 돈사, 법정 두당면적)."""
    for name, a0, a1, _w0, _w1, barn, area in STAGES:
        if a0 <= age_days < a1:
            return name, barn, area
    return ("출하", "-", None) if age_days >= MARKET_AGE else (None, None, None)


def weight_at(age_days: float) -> float:
    """일령 → 기대 체중(단계별 선형 보간).

    실제 성장은 S 자(곰페르츠)에 가깝지만, 단계 경계의 체중이 현장 기준으로
    정해져 있으므로 그 점들을 이어 쓰는 편이 현장 수치와 어긋나지 않는다.
    """
    a = float(age_days)
    if a <= 0:
        return STAGES[0][3]
    for _n, a0, a1, w0, w1, _b, _ar in STAGES:
        if a0 <= a < a1:
            return w0 + (w1 - w0) * (a - a0) / (a1 - a0)
    last = STAGES[-1]
    # 비육 이후는 마지막 구간의 일당증체로 연장한다
    adg = (last[4] - last[3]) / (last[2] - last[1])
    return last[4] + adg * (a - last[2])


def age_for_weight(target_kg: float) -> float:
    """목표 체중에 도달하는 일령(출하 시기 추정)."""
    for _n, a0, a1, w0, w1, _b, _ar in STAGES:
        if w0 <= target_kg <= w1:
            return a0 + (a1 - a0) * (target_kg - w0) / (w1 - w0)
    last = STAGES[-1]
    adg = (last[4] - last[3]) / (last[2] - last[1])
    return last[2] + (target_kg - last[4]) / adg


def batch_timeline(wean_date, n_weaned: int, mortality: dict | None = None
                   ) -> pd.DataFrame:
    """이유 배치 → 단계별 일정·두수·체중.

    이유일을 28일령으로 잡는다(포유 28일). 단계마다 폐사가 누적되므로 뒤로 갈수록
    두수가 준다 — 출하 두수는 이유 두수가 아니라 **육성률을 곱한 값**이다.
    """
    m = dict(MORTALITY if mortality is None else mortality)
    w0 = rc._d(wean_date)
    n = float(n_weaned)
    rows = []
    for name, a0, a1, wt0, wt1, barn, area in STAGES:
        if name == "포유자돈":
            continue                      # 이유 배치는 포유를 이미 지났다
        start = w0 + timedelta(days=a0 - STAGES[0][2])
        end = w0 + timedelta(days=a1 - STAGES[0][2])
        n_in = n
        n = n * (1.0 - m.get(name, 0.0))
        rows.append({"stage": name, "barn": barn,
                     "age_from": a0, "age_to": a1,
                     "start": start, "end": end,
                     "days": a1 - a0,
                     "n_in": int(round(n_in)), "n_out": int(round(n)),
                     "died": int(round(n_in - n)),
                     "kg_from": wt0, "kg_to": wt1,
                     "adg_kg": round((wt1 - wt0) / (a1 - a0), 3),
                     "area_per_head": area,
                     "area_needed_m2": (round(n_in * area, 1) if area else None)})
    d = pd.DataFrame(rows)
    d.attrs["market_date"] = w0 + timedelta(days=MARKET_AGE - STAGES[0][2])
    d.attrs["n_marketed"] = int(round(n))
    d.attrs["survival"] = round(n / max(1.0, float(n_weaned)), 4)
    return d


def density_check(n_pigs: int, area_m2: float, stage: str) -> dict:
    """사육밀도 — 법정 기준 대비.

    밀사는 증체·사료섭취를 떨어뜨리고 유해가스·서열싸움을 키운다. 배치가
    밀려 다음 방이 안 비면 바로 여기서 터지므로, batch_flow 의 병목과
    같은 사건의 두 얼굴이다.
    """
    req = next((a for n, _a0, _a1, _w0, _w1, _b, a in STAGES
                if n == stage for a in [a]), None)
    if not req:
        return {"stage": stage, "regulated": False}
    per = area_m2 / max(1, n_pigs)
    return {"stage": stage, "regulated": True,
            "n_pigs": n_pigs, "area_m2": area_m2,
            "per_head_m2": round(per, 3), "required_m2": req,
            "ratio": round(per / req, 2),
            "overcrowded": per < req,
            "capacity": int(area_m2 // req),
            "excess": max(0, n_pigs - int(area_m2 // req))}


def tail_enders(pigs: pd.DataFrame, today=None) -> pd.DataFrame:
    """정상 흐름에서 뒤처진 개체 — 그리고 **역류 금지**.

    지연된 돼지를 어린 배치로 되돌리는 것이 현장의 흔한 대처인데, 그러면
    AIAO 가 깨지고 어린 돼지가 병원체에 노출된다. 연구 보고로도 지연 개체는
    출하 시 약 10kg 가볍고 꼬리병변 2.2배·귀병변 1.6배다. 되돌리지 말고
    **별도 회복돈방(hospital pen)** 으로 빼는 것이 원칙이다.

    pigs: [id, batch, age_days, weight_kg]
    """
    if not len(pigs):
        return pd.DataFrame()
    d = pigs.copy()
    d["expected_kg"] = d["age_days"].map(weight_at)
    d["ratio"] = d["weight_kg"] / d["expected_kg"].replace(0, np.nan)
    batch_mean = d.groupby("batch")["weight_kg"].transform("mean")
    d["vs_batch"] = d["weight_kg"] / batch_mean.replace(0, np.nan)
    # 지금 증체 속도를 유지한다고 볼 때 출하 체중에 닿는 일령
    d["age_at_market"] = [
        a + (MARKET_WEIGHT - w) / max(0.1, _adg_at(a))
        for a, w in zip(d["age_days"], d["weight_kg"])]
    d["delay_days"] = (d["age_at_market"] - MARKET_AGE).round(1)
    d["tail_ender"] = ((d["vs_batch"] < TAIL_ENDER_WEIGHT_GAP)
                       | (d["delay_days"] > TAIL_ENDER_AGE_OVER))
    d["action"] = np.where(
        d["tail_ender"],
        "회복돈방 분리 — 어린 배치로 되돌리지 말 것(AIAO 파괴)",
        "정상 흐름 유지")
    return d.sort_values("vs_batch").reset_index(drop=True)


def _adg_at(age_days: float) -> float:
    """해당 일령 구간의 일당증체(kg/일)."""
    for _n, a0, a1, w0, w1, _b, _ar in STAGES:
        if a0 <= age_days < a1:
            return (w1 - w0) / (a1 - a0)
    last = STAGES[-1]
    return (last[4] - last[3]) / (last[2] - last[1])


def psy_msy(litters_per_sow_year: float, weaned_per_litter: float,
            post_wean_survival: float) -> dict:
    """PSY·MSY 와 벤치마크 대조.

    MSY = PSY × 이유후 육성률. 번식만 잘해도(PSY 높아도) 이유 후에 죽으면
    MSY 가 안 오른다 — 국내가 뒤지는 큰 몫이 이 구간이다.
    """
    psy = litters_per_sow_year * weaned_per_litter
    msy = psy * post_wean_survival
    cmp_ = {}
    for name, b in BENCHMARKS.items():
        cmp_[name] = {"psy_gap": round(psy - b["psy"], 1),
                      "msy_gap": round(msy - b["msy"], 1),
                      "their_survival": round(b["msy"] / b["psy"], 3)}
    return {"psy": round(psy, 1), "msy": round(msy, 1),
            "post_wean_survival": round(post_wean_survival, 3),
            "post_wean_mortality": round(1 - post_wean_survival, 3),
            "vs": cmp_}


def main() -> int:
    print("=== 사육단계 (번식 다음이 통째로 비어 있었다) ===")
    print(f"  {'단계':<8} {'일령':<10} {'체중(kg)':<12} {'돈사':<6} "
          f"{'법정면적':>8} {'ADG':>7}")
    for name, a0, a1, w0, w1, barn, area in STAGES:
        adg = (w1 - w0) / (a1 - a0)
        ar = f"{area}㎡" if area else "-"
        print(f"  {name:<8} {f'{a0}~{a1}':<10} {f'{w0}~{w1}':<12} {barn:<6} "
              f"{ar:>8} {adg:>6.3f}")
    print(f"  출하 {MARKET_AGE}일령 · {MARKET_WEIGHT}kg")

    print("\n=== 이유 배치 300두의 출하까지 ===")
    tl = batch_timeline("2026-08-10", 300)
    print(f"  {'단계':<8} {'기간':<24} {'입식':>5} {'폐사':>5} {'출식':>5} "
          f"{'필요면적':>9}")
    for r in tl.itertuples(index=False):
        area = f"{r.area_needed_m2:.0f}㎡" if r.area_needed_m2 else "-"
        print(f"  {r.stage:<8} {r.start:%Y-%m-%d}~{r.end:%m-%d} ({r.days:>3}일) "
              f"{r.n_in:>5} {r.died:>5} {r.n_out:>5} {area:>9}")
    print(f"  → 출하 {tl.attrs['market_date']:%Y-%m-%d} · "
          f"{tl.attrs['n_marketed']}두 · 육성률 {tl.attrs['survival']:.1%}")
    print("  ※ 출하 두수는 이유 두수가 아니라 **육성률을 곱한 값**이다.")

    print("\n=== 사육밀도 (축산법 시행령 기준) ===")
    for stage, n, area in (("이유자돈", 300, 90.0), ("이유자돈", 300, 70.0),
                           ("육성돈", 290, 130.0), ("비육돈", 287, 200.0)):
        d = density_check(n, area, stage)
        mark = "⚠ 과밀" if d["overcrowded"] else "적정"
        ex = f" · 초과 {d['excess']}두" if d["excess"] else ""
        print(f"  {stage:<8} {n:>3}두 / {area:>5.0f}㎡ = "
              f"두당 {d['per_head_m2']:.3f}㎡ (기준 {d['required_m2']}) "
              f"{mark}{ex}")
    print("  ※ 밀사는 배치가 밀려 다음 방이 안 빌 때 터진다 — batch_flow 의")
    print("    병목과 같은 사건의 두 얼굴이다.")

    print("\n=== 지연 개체(tail-ender) ===")
    rng = np.random.default_rng(3)
    n = 40
    ages = np.full(n, 120)
    base = np.array([weight_at(a) for a in ages])
    wts = base * rng.normal(1.0, 0.10, n)
    wts[:3] *= 0.72                        # 확실히 뒤처진 개체 몇 마리
    pigs = pd.DataFrame({"id": [f"P{i:03d}" for i in range(n)],
                         "batch": "B1", "age_days": ages,
                         "weight_kg": wts.round(1)})
    te = tail_enders(pigs)
    n_te = int(te["tail_ender"].sum())
    print(f"  {n}두 중 지연 {n_te}두 (배치 평균 대비 "
          f"{TAIL_ENDER_WEIGHT_GAP:.0%} 미만 또는 출하 {TAIL_ENDER_AGE_OVER}일 초과)")
    for r in te.head(4).itertuples(index=False):
        print(f"  {r.id} {r.weight_kg:>5.1f}kg (배치 대비 {r.vs_batch:>4.0%}) "
              f"출하 지연 {r.delay_days:>+5.1f}일 → {r.action[:22]}")
    print("  ※ 되돌리지 말 것. 지연 개체를 어린 배치로 보내면 AIAO 가 깨지고")
    print("    어린 돼지가 병원체에 노출된다(보고: 출하 시 10kg 경량, 꼬리병변 2.2배).")

    print("\n=== PSY · MSY — 어디서 새는가 ===")
    for label, (lit, wpl, surv) in {
            "우리 농장(가정)": (2.34, 11.5, 0.86),
            "국내 평균 수준": (2.20, 10.4, 0.807),
            "덴마크 수준": (2.30, 13.6, 0.933)}.items():
        r = psy_msy(lit, wpl, surv)
        print(f"  {label:<14} PSY {r['psy']:>5.1f} → MSY {r['msy']:>5.1f} "
              f"(이유후 폐사 {r['post_wean_mortality']:.1%})")
    print(f"  {'벤치마크':<14} " + " · ".join(
        f"{k} {v['psy']}/{v['msy']}" for k, v in BENCHMARKS.items()))
    print("  → 국내 이유후 폐사율이 덴마크의 약 3배다. **번식만 붙들고 있으면**")
    print("    이 손실이 보이지 않는다 — 전체 관리로 넓혀야 하는 이유다.")

    print("\n※ 단계 경계·법정면적은 기준값이고, 폐사율·증체는 농장마다 다르다."
          "\n  실제 수치를 넣으면 같은 표가 그 농장 기준으로 다시 계산된다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
