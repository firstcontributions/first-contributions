"""교배 적기(AI timing) 산출 + 회전율·경제 효과 — 교배사 핵심 로직.

배경(국내 번식 병목): 모돈 1회전 = 임신 115일 + 포유 28일 + 이유후 재귀발정 7일
= **150일**, 이론상 연 2.43회전이 가능하다. 그런데 국내는 2회가 고작이며, 가장 큰
원인은 **이유 후 수정을 해도 수태율이 낮아** 재발정(21일 주기)이 반복되며 공태일수
(NPD)가 쌓이는 것이다. 공태일은 그대로 사료비·기회비용 손실이다.

따라서 이 앱의 두 축은 **발정 확인**과 **교배 적기**다 — 적기를 맞추면 수태율이
오르고, 수태율이 오르면 회전율이 오르며, 그것이 곧 수익이다.

수의학 근거(교배 적기):
  · 배란은 **발정 지속시간의 약 2/3 지점**에서 일어난다.
  · 발정 지속: 경산돈 48~60h, 후보돈(미경산) 40~48h — 후보돈이 더 짧다.
  · 정자는 수정능을 ~24h 유지, 난자는 배란 후 ~8~12h 만 유효.
    → **배란 직전(0~24h 전) 수정**이 최적이다.
  · **WEI(이유-발정 간격) 보정**: WEI 가 짧으면(3~4일) 발정이 길고 배란이 늦으며,
    WEI 가 길면(5~6일) 발정이 짧고 배란이 빠르다. 같은 "발정 확인 시각"이라도
    WEI 에 따라 적기가 달라진다 — 이 보정이 현장 관행(일괄 12/24h)과의 차이다.

    python competition/src/breeding_timing.py        # 시연
"""
from __future__ import annotations

import sys

# 번식 주기 상수(일)
GESTATION = 115          # 임신
LACTATION = 28           # 포유
NORMAL_WEI = 7           # 정상 이유-발정 간격
RETURN_CYCLE = 21        # 재발정 주기(수태 실패 시)
CYCLE_DAYS = GESTATION + LACTATION + NORMAL_WEI      # 150

# 발정 지속시간(h) — 산차별
ESTRUS_DURATION = {"gilt": 44.0, "sow": 54.0}        # 후보돈 / 경산돈
OVULATION_FRAC = 2.0 / 3.0                            # 배란 시점(발정 지속의 2/3)
SPERM_VIABLE_H = 24.0                                 # 정자 수정능 유지
OVUM_VIABLE_H = 10.0                                  # 난자 유효


def estrus_duration(parity: str = "sow", wei_days: float = NORMAL_WEI) -> float:
    """발정 지속시간(h). WEI 가 짧을수록 길어진다(현장 관찰)."""
    base = ESTRUS_DURATION.get(parity, ESTRUS_DURATION["sow"])
    # WEI 4일이면 +6h, 7일 기준 0, 10일이면 -6h (선형 근사, 범위 제한)
    adj = (NORMAL_WEI - float(wei_days)) * 2.0
    return float(max(24.0, min(84.0, base + adj)))


def ovulation_time(parity: str = "sow", wei_days: float = NORMAL_WEI) -> float:
    """발정 시작 후 배란까지 시간(h)."""
    return estrus_duration(parity, wei_days) * OVULATION_FRAC


def insemination_window(parity: str = "sow", wei_days: float = NORMAL_WEI) -> dict:
    """발정 시작 기준 최적 수정 창(h)과 권장 2회 수정 시각.

    최적 창 = [배란 - 정자 수정능(24h), 배란 + 난자 유효(10h)의 절반] 로 잡되,
    실무 안전을 위해 배란 직전 구간을 우선한다.
    """
    ov = ovulation_time(parity, wei_days)
    start = max(0.0, ov - SPERM_VIABLE_H)
    end = ov + OVUM_VIABLE_H / 2.0
    ai1, ai2 = optimal_ai_times(parity, wei_days)
    return {"parity": parity, "wei_days": float(wei_days),
            "estrus_duration_h": round(estrus_duration(parity, wei_days), 1),
            "ovulation_h": round(ov, 1),
            "window_start_h": round(start, 1), "window_end_h": round(end, 1),
            "ai1_h": ai1, "ai2_h": ai2}


def optimal_ai_times(parity: str = "sow", wei_days: float = NORMAL_WEI,
                     n_ai: int = 2, min_gap_h: float = 8.0) -> list:
    """수태율을 **최대화하는** 수정 시각을 탐색해 반환(h, 발정 시작 기준).

    초기 구현은 '창의 1/3·2/3 지점'이라는 임의 규칙을 썼는데, 그 값이 관행
    (12/24h)보다 못한 경우가 생겼다(모델 기준 자기모순). 권장값은 **자기 모델의
    argmax** 여야 하므로 격자 탐색으로 정한다. 현장 운용을 고려해 두 수정 사이
    최소 간격(min_gap_h)을 둔다.
    """
    ov = ovulation_time(parity, wei_days)
    lo = max(0.0, ov - SPERM_VIABLE_H - 4.0)
    hi = ov + OVUM_VIABLE_H
    grid = [round(lo + i * 0.5, 1) for i in range(int((hi - lo) / 0.5) + 1)]
    if n_ai == 1:
        best = max(grid, key=lambda t: conception_prob([t], parity, wei_days))
        return [best]
    best, best_p = [grid[0], grid[-1]], -1.0
    for i, a in enumerate(grid):
        for b in grid[i:]:
            if b - a < min_gap_h:
                continue
            p = conception_prob([a, b], parity, wei_days)
            if p > best_p:
                best_p, best = p, [a, b]
    return best


def conception_prob(ai_hours: list, parity: str = "sow",
                    wei_days: float = NORMAL_WEI, base: float = 0.90) -> float:
    """수정 시각(발정 시작 후 h) 목록 → 기대 수태율.

    각 수정의 유효도는 **배란 대비 상대 시점**으로 정한다:
      · 배란 24h 전 ~ 배란   : 최적(1.0 부근)
      · 너무 이르면(정자 수명 초과) 또는 배란 후 늦으면 급감
    여러 번 수정하면 실패 확률이 곱으로 줄어든다(독립 근사).
    base 는 적기에 맞췄을 때의 상한(관리·정액 품질 등 다른 요인 포함).
    """
    ov = ovulation_time(parity, wei_days)
    eff = []
    for t in ai_hours:
        d = float(t) - ov                       # 음수=배란 전, 양수=배란 후
        if -SPERM_VIABLE_H <= d <= 0:
            e = 1.0 - 0.3 * (abs(d) / SPERM_VIABLE_H)      # 직전일수록 좋음
        elif 0 < d <= OVUM_VIABLE_H:
            e = 1.0 - 0.7 * (d / OVUM_VIABLE_H)            # 배란 후 급감
        else:
            over = abs(d) - (SPERM_VIABLE_H if d < 0 else OVUM_VIABLE_H)
            e = max(0.0, 0.3 - 0.02 * over)
        eff.append(max(0.0, min(1.0, e)))
    if not eff:
        return 0.0
    fail = 1.0
    for e in eff:
        fail *= (1.0 - base * e)
    return round(1.0 - fail, 3)


# --------------------------------------------------------------------------
def cycle_days(conception_rate: float, wei_days: float = NORMAL_WEI) -> float:
    """수태율 → 1회전 평균 소요일수.

    수태 실패 시 재발정(21일)을 기다려 재수정한다. 평균 수정 횟수는 1/r 이므로
    추가 지연은 (1/r - 1) × 21일이다.
    """
    r = max(0.05, min(1.0, float(conception_rate)))
    return GESTATION + LACTATION + float(wei_days) + (1.0 / r - 1.0) * RETURN_CYCLE


def turnover(conception_rate: float, wei_days: float = NORMAL_WEI) -> float:
    """연간 모돈 회전율(회/년)."""
    return round(365.0 / cycle_days(conception_rate, wei_days), 2)


def npd(conception_rate: float, wei_days: float = NORMAL_WEI) -> float:
    """1회전당 비생산일수(공태일) — 임신·포유를 뺀 나머지."""
    return round(cycle_days(conception_rate, wei_days) - GESTATION - LACTATION, 1)


def economics(n_sows: int, cr_before: float, cr_after: float,
              wei_days: float = NORMAL_WEI, npd_cost_won: int = 6000) -> dict:
    """수태율 개선의 경제 효과(연간).

    npd_cost_won: 공태일 1일당 비용(사료+기회비용). 농가·시세에 따라 조정.
    """
    d0, d1 = cycle_days(cr_before, wei_days), cycle_days(cr_after, wei_days)
    t0, t1 = 365.0 / d0, 365.0 / d1
    npd0, npd1 = npd(cr_before, wei_days), npd(cr_after, wei_days)
    # 연간 공태일 = 회전수 × 회전당 공태일
    npd_year0, npd_year1 = t0 * npd0, t1 * npd1
    saved_days = (npd_year0 - npd_year1) * n_sows
    return {"n_sows": n_sows,
            "cr_before": cr_before, "cr_after": cr_after,
            "cycle_before": round(d0, 1), "cycle_after": round(d1, 1),
            "turnover_before": round(t0, 2), "turnover_after": round(t1, 2),
            "npd_before": npd0, "npd_after": npd1,
            "npd_days_saved_year": round(saved_days, 0),
            "won_saved_year": int(saved_days * npd_cost_won),
            "extra_litters_year": round((t1 - t0) * n_sows, 1)}


def main() -> int:
    print("=== 교배 적기 (발정 시작 기준 시간) ===")
    for parity in ("sow", "gilt"):
        for wei in (4, 7, 10):
            w = insemination_window(parity, wei)
            print(f"  {parity:5s} WEI {wei:2d}일 → 발정지속 {w['estrus_duration_h']}h · "
                  f"배란 {w['ovulation_h']}h · 창 {w['window_start_h']}~{w['window_end_h']}h · "
                  f"권장 수정 {w['ai1_h']}h, {w['ai2_h']}h")

    print("\n=== 관행(12/24h 일괄) vs 적기 맞춤 — 기대 수태율 ===")
    for parity in ("sow", "gilt"):
        for wei in (4, 7, 10):
            w = insemination_window(parity, wei)
            rout = conception_prob([12, 24], parity, wei)
            opt = conception_prob([w["ai1_h"], w["ai2_h"]], parity, wei)
            print(f"  {parity:5s} WEI {wei:2d}일 → 관행 {rout:.3f} vs 적기 {opt:.3f} "
                  f"({opt - rout:+.3f})")

    print("\n=== 회전율·공태일 (수태율의 영향) ===")
    for cr in (0.70, 0.80, 0.85, 0.90):
        print(f"  수태율 {cr:.0%} → 1회전 {cycle_days(cr):.0f}일 · "
              f"회전율 {turnover(cr):.2f}회/년 · 회전당 공태일 {npd(cr):.0f}일")

    print("\n=== 경제 효과(모돈 300두, 수태율 78% → 85%) ===")
    e = economics(300, 0.78, 0.85)
    print(f"  1회전 {e['cycle_before']}일 → {e['cycle_after']}일 · "
          f"회전율 {e['turnover_before']} → {e['turnover_after']}회/년")
    print(f"  연간 공태일 절감 {e['npd_days_saved_year']:,.0f}일 · "
          f"추가 산차 {e['extra_litters_year']}회 · "
          f"절감액 약 {e['won_saved_year']:,}원/년")
    print("\n※ 수태율 개선폭은 가정값이다. 적기 수정의 효과 크기는 농장 실증이 필요하며,"
          "\n  여기서는 '적기가 왜 회전율·수익과 직결되는가'의 구조를 계산한다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
