"""모돈 두수 하나로 전체를 돌린다 — 설계 · 개체 · 흐름 · 손익.

지금까지 모듈이 흩어져 있어서 "모돈 300두 농장" 하나를 끝까지 돌려 보려면
진입점을 여섯 개 따로 불러야 했다. 이 스크립트가 그 배선이다.

    python competition/src/run_farm.py --sows 300
    python competition/src/run_farm.py --sows 300 --npd 62 --weaned 10
    python competition/src/run_farm.py --data     # 필요한 자료가 뭔지만 출력

## 무엇이 실측이고 무엇이 가정인가

이걸 구분하지 않으면 "다 되는 것처럼" 보인다. 출력 끝에 항상 찍는다.

  실측   국내 466농장 번식성적(벤치마크·기본 상수) · 케글 자세/탐지 성능
  계산   돈방 소요·배치 흐름·생산비 — 위 값에서 산식으로 나온다
  유도   ③ 개체 배치 — 난수가 아니라 **번식주기 비율로 유도**한 값이다
         (단계별 두수 = 총두수 × 단계 일수 ÷ 주기). 실제 도면·이력은 아니다

이 스크립트에 난수는 **없다.** 같은 입력이면 여섯 단계가 전부 같은 값을 낸다
(두 번 돌려 diff 로 확인). 예전에 여기 "합성 난수" 라고 적어 놨었는데 틀렸다.

## 모돈 두수 → 분만틀 수

pigflow 는 분만틀을 기준으로 설계한다(모돈 두수는 계절을 타므로). 두수로
시작하려면 역산해야 하는데, sow_inventory 가 분만틀에 대해 단조증가라
이분 탐색으로 찾는다.
"""
from __future__ import annotations

import argparse
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "competition"))

# 이 프로그램을 돌리는 데 필요한 자료 — 없으면 무엇이 대체되는지 함께 적는다.
REQUIRED = [
    ("모돈 두수", "필수", "상시 사육 모돈 수. 이것만 있으면 전체가 돈다",
     "—"),
    ("분만틀 수", "권장", "실제 분만사 분만틀 개수. 설계의 유일한 고정 물리량",
     "모돈 두수에서 역산"),
    ("배치 간격", "권장", "주간/2주/3주/4주/5주 중 무엇으로 운영하는가",
     "주간(WEEKLY)"),
    ("보유 돈방 목록", "권장", "돈사별 방 개수·면적·수용두수 → 부족분 진단",
     "소요량대로 지은 것으로 가정(부족 0)"),
    ("번식 성적", "권장", "PSY·NPD·분만율·복당이유두수·재귀발정일",
     "국내 466농장 실측 중앙값"),
    ("사료·단가", "선택", "단계별 FCR·사료단가·지육단가 → 손익 정확도",
     "관행 초기값"),
    ("개체 이력", "선택", "개체별 이유·교배·분만일 → 오늘의 작업 큐",
     "주기 비율로 유도한 배치(개체 이력 없음)"),
    ("CCTV 영상", "선택", "군사 돈방 고정 카메라 → 발정 탐지",
     "미사용(일정 기반 관리만)"),
]


def crates_for_sows(n_sows: int, cfg) -> int:
    """모돈 두수 → 분만틀 수. sow_inventory 의 역함수(단조증가라 이분 탐색)."""
    from pigflow import calc
    b = cfg.breeding
    iv = cfg.batch_system.interval_weeks

    def sows(cr: int) -> float:
        svc = calc.services_per_batch(cr, b.farrowing_rate)
        g = calc.gilts_per_batch(svc, b.gilt_ratio_of_service)
        return calc.sow_inventory(cr, iv, b.sow_turnover, g, b.gilt_lead_weeks)

    lo, hi = 1, 4
    while sows(hi) < n_sows and hi < 100_000:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if sows(mid) < n_sows:
            lo = mid + 1
        else:
            hi = mid
    # 목표를 넘긴 값과 그 직전 중 더 가까운 쪽
    return min([max(1, lo - 1), lo], key=lambda c: abs(sows(c) - n_sows))


def program_metrics(cfg) -> dict:
    """이 프로그램이 **스스로 깔고 있는** 번식 성적 — farm_gap 입력 형태로.

    실측 기록이 없을 때 진단의 기준선으로 쓴다. 중앙값을 기본값으로 넣으면
    격차가 늘 0 이 되어 아무것도 진단하지 못한다.

    NPD 만 상수가 아니라 파생값이다. pigflow 는 비생산일수를 따로 두지 않고
    번식주기에서 나오므로, 이론 최소치(재발정·유산 0)를 쓴다 — 그래서 실측
    중앙 43일보다 한참 낮게 나오는 것이 정상이고, 그 차이가 이 설계가
    낙관적인 폭이다.
    """
    b = cfg.breeding
    return {
        "weaned": float(b.weaned_per_litter),
        "lactation": float(b.lactation_days),
        "gestation": float(b.gestation_days),
        "farrowing_rate": float(b.farrowing_rate) * 100.0,
        "wean_to_estrus": float(b.wean_to_service_days),
        "npd": _npd_floor(b),
    }


def _npd_floor(b) -> float:
    import farm_gap as fg
    return fg.npd_floor_annual({
        "wean_to_service_days": b.wean_to_service_days,
        "gestation_days": b.gestation_days,
        "lactation_days": b.lactation_days})


def run(n_sows: int, system: str = "WEEKLY", days: int = 400,
        farm_metrics: dict | None = None, verbose: bool = True) -> dict:
    from datetime import date

    import breeding_ledger as bl
    import farm_economics as fe
    import farm_gap as fg
    import farm_registry as fr
    import growth_flow as gf
    from pigflow import calc, report, validate
    from pigflow.config import default_config
    from pigflow.simulator import Simulator, build_rooms

    out: dict = {"n_sows": n_sows, "system": system}
    p = lambda *a: print(*a) if verbose else None                # noqa: E731

    # 1) 설계 — 두수에서 분만틀을 역산해 pigflow 로 넘긴다
    cfg = default_config()
    cfg.batch_system_id = system
    cfg.crate_count = crates_for_sows(n_sows, cfg)
    plan = calc.plan(cfg)
    out["plan"] = plan
    p("=" * 76)
    p(f"  모돈 {n_sows}두 농장 · {system} 배치 — 전체 시뮬레이션")
    p("=" * 76)
    p(f"\n① 설계 (모돈 두수 → 분만틀 역산)")
    p(f"   분만틀 {cfg.crate_count}개 → 설계 모돈 {plan['sow_inventory']:.0f}두 "
      f"(입력 {n_sows}두, 오차 {plan['sow_inventory'] - n_sows:+.0f})")
    p(f"   배치당 교배 {plan['services_per_batch']}두 · "
      f"이유 {plan['weaned_per_batch']:.0f}두 · 출하 {plan['shipped_per_batch']:.0f}두")
    p(f"   번식주기 {plan['cycle_days']}일 · 출하일령 {plan['market_age_days']}일")

    # 2) 돈방 소요 + 흐름 시뮬레이션
    rooms = build_rooms(cfg)
    sim = Simulator(cfg, date(2026, 1, 1), rooms=rooms).run(days)
    s = validate.summarize(sim.findings)
    k = report.kpi_report(sim)
    out["rooms"] = len(rooms)
    out["findings"] = s
    out["kpi"] = k
    p(f"\n② 돈군흐름 {days}일 시뮬레이션")
    p(f"   돈방 {len(rooms)}개 · 이동 {len(sim.events)}건 · "
      f"출하 배치 {len(sim.shipped)}개")
    p(f"   검증: 오류 {s['errors']}건 · 경고 {s['warnings']}건"
      + (f"  {s['by_check']}" if s["n"] else "  (설계대로 지으면 0)"))
    # **PSY 분모 주의.** pigflow 는 후보돈 자리를 포함한 총 모돈 규모로 나누고,
    # 실측 통계(⑤)는 보통 번식돈 기준이다. 같은 이름의 다른 지표라서 두 값이
    # 다르게 나오는데, 설명 없이 나란히 두면 어느 쪽이 틀린 줄 안다.
    b = cfg.breeding
    gilt_slots = plan["gilts_per_batch"] * b.gilt_lead_weeks
    breeding_only = plan["sow_inventory"] - gilt_slots
    psy_breeding = (plan["weaned_per_batch"] * (52.0 / cfg.batch_system.interval_weeks)
                    / max(1e-9, breeding_only))
    out["psy_breeding_only"] = round(psy_breeding, 2)
    p(f"   PSY {k['psy']} · MSY {k['msy']} · 가동률 {k['room_utilization']:.1%}")
    p(f"   ※ 이 PSY 의 분모는 후보돈 자리 {gilt_slots:.0f}두를 **포함한** "
      f"{plan['sow_inventory']:.0f}두다.")
    p(f"     번식돈 {breeding_only:.0f}두만으로 세면 PSY {psy_breeding:.2f} — "
      f"⑤의 실측 비교는 이쪽 기준이다.")

    # 3) 개체 배치 — 실제 도면이 없으면 비율로 만든다
    farm = fr.demo_farm(n_sows)
    occ = farm.occupancy()
    out["placed"] = len(farm._where)
    p(f"\n③ 개체 배치 (도면 미입력 → 번식주기 비율로 생성)")
    p("   " + " · ".join(
        f"{st} {int(v)}두" for st, v in occ.groupby("stage")["n"].sum().items()))
    p(f"   돈방 {len(farm.pens)}개 · 배치 {len(farm._where)}두")

    # 4) 사육 단계 흐름
    tl = gf.batch_timeline("2026-08-10", int(plan["weaned_per_batch"]))
    out["growth"] = {"survival": float(tl.attrs["survival"]),
                     "marketed": int(tl.attrs["n_marketed"])}
    p(f"\n④ 이유 후 사육 — 배치 {plan['weaned_per_batch']:.0f}두 기준")
    p(f"   출하 {tl.attrs['n_marketed']}두 · 육성률 {tl.attrs['survival']:.1%}")

    # 5) 성적 진단 — 실측 분포에서 얼마나 멀어져 있나
    #
    # **기본값을 중앙값으로 채우면 안 된다.** 원래 farm_metrics 가 없으면
    # 실측 중앙값을 그대로 넣었는데, 그러면 "내 값 = 중앙값" 이라 격차가
    # 항상 0.00 으로 찍혔다. 진단이 아니라 항등식을 확인한 셈이다.
    # 입력이 없을 때의 정직한 기본값은 **이 프로그램 자신의 가정값**이다.
    st = fg.load_stats()
    fm = program_metrics(cfg)
    given = bool(farm_metrics)
    fm.update(farm_metrics or {})
    diag = fg.diagnose(fm, st, n_sows=n_sows)
    out["gap"] = diag
    out["gap_basis"] = "입력값" if given else "프로그램 가정값"
    src = "내 농장" if given else "내 프로그램 가정"
    p(f"\n⑤ 성적 진단 (국내 466농장 분포 대비)")
    p(f"   {src} PSY {diag['psy']} · 중앙 농장 {diag['psy_median_farm']} "
      f"→ 격차 {diag['psy_gap']:+.2f}두")
    p(f"   (중앙 농장은 지표별 중앙값을 항등식에 넣은 합성값. 실제 PSY 열의 "
      f"중앙은 {diag['psy_median_observed']})")
    for r in diag["rows"][:3]:
        rec = (f"되돌리면 PSY {r['psy_recover']:+.2f}"
               if r["psy_recover"] is not None else "간접 지표")
        p(f"     {r['name_ko']:<14}{r['value']:>7} (중앙 {r['median']}) "
          f"IQR {r['iqr_z']:+.2f} {r['band']:<8}{rec}")
    if not given:
        p(f"   ※ 실측 기록을 안 넣었으므로 위는 **가정값 대 실측 분포**다."
          f"\n     NPD {fm['npd']}일은 재발정·유산이 0 인 이론 최소치고 실측 중앙은"
          f" {diag['rows'][0]['median'] if diag['rows'][0]['metric']=='npd' else 43.0}일이다."
          f"\n     이 프로그램이 낙관적인 폭이 곧 발정 관리로 메울 몫이다.")
        p(f"   같은 가정을 시뮬레이션으로 돌리면 PSY {psy_breeding:.2f} — "
          f"항등식 {diag['psy']} 과의 차 {psy_breeding - diag['psy']:+.2f}두가"
          f"\n     후보돈 자리·모돈 교체에서 빠지는 몫이다.")

    # 6) 손익 — 무엇부터 고칠 것인가
    lv = fe.levers(n_sows=n_sows, psy=diag["psy"])
    out["levers"] = lv.to_dict("records")
    p(f"\n⑥ 개선 지렛대 (모돈 {n_sows}두 · 원/년)")
    for r in lv.itertuples(index=False):
        p(f"     {r.lever:<18}{r.연간효과:>15,}원   {r.경로}")
    be = fe.breakeven_price(diag["psy"], 0.86)
    out["breakeven"] = be
    p(f"   손익분기 지육단가 {be:,}원/kg (가정 시세 {fe.PORK_PRICE:,}원)")

    if verbose:
        _provenance()
    return out


def _provenance() -> None:
    print("\n" + "-" * 76)
    print("  이 결과의 출처 — 무엇이 실측이고 무엇이 가정인가")
    print("-" * 76)
    print("  실측  국내 466농장 번식성적(벤치마크·기본 상수) · "
          "케글 자세 0.636 / 탐지 mAP50 0.659")
    print("  계산  돈방 소요 · 배치 흐름 · 생산비 — 위 값에서 산식으로 나온다")
    print("  가정  사료 FCR·단가 = 관행 초기값 · 이유후 육성률 86%")
    print("  유도  ③ 개체 배치는 **번식주기 비율로 만든 것**이고 실제 이력이 아니다"
          "\n        (난수가 아니다 — 같은 입력이면 여섯 단계가 늘 같은 값을 낸다)")
    print("\n  → 실제 농장 값을 넣으면 ①②④⑤⑥ 이 그 농장 계산으로 바뀐다.")
    print("     `--data` 로 필요한 자료 목록을 볼 수 있다.")


def print_requirements() -> None:
    print("=" * 76)
    print("  시뮬레이션에 필요한 자료")
    print("=" * 76)
    w = max(len(x[0]) for x in REQUIRED)
    print(f"  {'항목':<{w}}  {'구분':<4}  설명 / 없을 때 대체값")
    print("  " + "-" * 72)
    for name, need, desc, fallback in REQUIRED:
        print(f"  {name:<{w}}  {need:<4}  {desc}")
        print(f"  {'':<{w}}  {'':<4}  ↳ 없으면: {fallback}")
    print("\n  필수는 **모돈 두수 하나**다. 나머지는 없으면 국내 실측 중앙값이나")
    print("  관행값으로 채우고, 무엇이 대체됐는지 결과 끝에 항상 표시한다.")
    print("\n  농장 값을 넣는 곳:")
    print("    돈방·배치     competition/pigflow/example_farm.yaml 를 복사해 수정")
    print("    번식 성적     run_farm.py --npd 62 --weaned 10 --farrowing-rate 74")
    print("    사료·단가     src/farm_economics.py 의 FEED / NON_FEED / PORK_PRICE")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="run_farm")
    ap.add_argument("--sows", type=int, default=300, help="상시 모돈 두수")
    ap.add_argument("--system", default="WEEKLY",
                    choices=["WEEKLY", "B2W", "B3W", "B4W", "B5W"])
    ap.add_argument("--days", type=int, default=400)
    ap.add_argument("--npd", type=float, help="연간 비생산일수")
    ap.add_argument("--weaned", type=float, help="복당 이유두수")
    ap.add_argument("--farrowing-rate", type=float, help="분만율(%%)")
    ap.add_argument("--wean-to-estrus", type=float, help="재귀발정일")
    ap.add_argument("--data", action="store_true", help="필요한 자료만 출력")
    a = ap.parse_args(argv)
    if a.data:
        print_requirements()
        return 0
    fm = {k: v for k, v in (("npd", a.npd), ("weaned", a.weaned),
                            ("farrowing_rate", a.farrowing_rate),
                            ("wean_to_estrus", a.wean_to_estrus))
          if v is not None}
    run(a.sows, a.system, a.days, fm or None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
