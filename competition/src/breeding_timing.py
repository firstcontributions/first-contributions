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
SPERM_VIABLE_H = 30.0                                 # 정자 생존(자궁·난관 내)
OVUM_VIABLE_H = 10.0                                  # 난자 유효
# 수정능획득(capacitation): 주입 직후의 정자는 수정 능력이 없다. 자궁·난관을
# 거치며 4~6h 이 지나야 난자를 수정시킬 수 있고, 그 사이 난관팽대부에 정자
# 저장소가 만들어진다. **배란 시점에 이미 수정능을 갖춘 정자가 대기하고 있어야**
# 한다 — 이것이 "배란 직전이 아니라 배란 몇 시간 전"이 적기인 이유다.
CAPACITATION_H = 4.0

# 현장 지침(발정확인·정액주입 가이드)의 적기 구간(승가허용 시작 기준 h).
# 모델 권장값이 이 구간을 벗어나면 둘 중 하나가 틀린 것이다 — 검증용 기준.
FIELD_OPTIMAL_WINDOW = (12.0, 36.0)
FIELD_NO_AI_BEFORE_H = 12.0      # 이 전에는 '주입 금지'(수태율 낮음)


def estrus_duration(parity: str = "sow", wei_days: float = NORMAL_WEI) -> float:
    """발정 지속시간(h). WEI 가 짧을수록 길어진다(현장 관찰)."""
    base = ESTRUS_DURATION.get(parity, ESTRUS_DURATION["sow"])
    # WEI 4일이면 +6h, 7일 기준 0, 10일이면 -6h (선형 근사, 범위 제한)
    adj = (NORMAL_WEI - float(wei_days)) * 2.0
    return float(max(24.0, min(84.0, base + adj)))


def ovulation_time(parity: str = "sow", wei_days: float = NORMAL_WEI) -> float:
    """발정 시작 후 배란까지 시간(h)."""
    return estrus_duration(parity, wei_days) * OVULATION_FRAC


def insemination_window(parity: str = "sow", wei_days: float = NORMAL_WEI,
                        frac: float = 0.5) -> dict:
    """발정 시작 기준 최적 수정 창(h)과 권장 2회 수정 시각.

    창을 상수식(배란-24h ~ 배란+5h)으로 박아두면 유효도 모델과 어긋난다.
    **유효도가 정점의 frac 이상인 구간**을 창으로 삼아 모델과 항상 일치시킨다.
    """
    ov = ovulation_time(parity, wei_days)
    grid = [i * 0.5 for i in range(0, int((ov + OVUM_VIABLE_H) / 0.5) + 1)]
    effs = [(t, ai_efficacy(t, parity, wei_days)) for t in grid]
    peak_t, peak_e = max(effs, key=lambda x: x[1])
    ok = [t for t, e in effs if e >= frac * peak_e and e > 0]
    start, end = (min(ok), max(ok)) if ok else (peak_t, peak_t)
    ai1, ai2 = optimal_ai_times(parity, wei_days)
    return {"parity": parity, "wei_days": float(wei_days),
            "estrus_duration_h": round(estrus_duration(parity, wei_days), 1),
            "ovulation_h": round(ov, 1),
            "peak_h": round(peak_t, 1), "peak_efficacy": round(peak_e, 3),
            "window_start_h": round(start, 1), "window_end_h": round(end, 1),
            "ai1_h": ai1, "ai2_h": ai2}


def estrus_timeline(parity: str = "sow", wei_days: float = NORMAL_WEI) -> dict:
    """발정 전후 관찰 신호의 시간 구조(승가허용 시작 = 0h 기준).

    현장 지침의 타임라인을 그대로 모델에 넣은 것. 관찰 신호마다 **나타나는
    시점이 다르다**는 점이 중요하다 — 외음부 변화는 승가허용보다 이틀 먼저
    시작하므로, 카메라가 외음부를 읽으면 **승가허용 전에 미리 알 수 있다**.
    등누르기(배부압박) 반응은 창이 하루뿐이라 육안 점검은 놓치기 쉽다.
    """
    dur = estrus_duration(parity, wei_days)
    return {
        "vulva_change": (-48.0, 48.0),      # 외음부 발적·부종 — 약 4일간
        "prodromal": (-24.0, 0.0),          # 발정징후(불안·발성) — 승가허용 전
        "standing_heat": (0.0, dur),        # 승가허용(발정기간)
        "back_pressure": (12.0, 36.0),      # 등누르기 검사 허용 — 약 1일
        "ovulation": ovulation_time(parity, wei_days),
        "ai_window": (FIELD_OPTIMAL_WINDOW[0], FIELD_OPTIMAL_WINDOW[1]),
    }


def check_against_field_guide(parity: str = "sow",
                              wei_days: float = NORMAL_WEI) -> dict:
    """모델 권장값이 현장 지침의 적기 구간 안에 있는지 검증.

    지침은 '주입 금지(~12h) / 적기(12~36h) / 다음차(36h~)' 로 구간을 나눈다.
    모델이 이 밖을 권하면 둘 중 하나가 틀렸다는 뜻이므로 드러내 놓고 본다.
    """
    w = insemination_window(parity, wei_days)
    lo, hi = FIELD_OPTIMAL_WINDOW
    times = [w["ai1_h"], w["ai2_h"]]
    return {"parity": parity, "wei_days": wei_days,
            "ai_times": times, "peak_h": w["peak_h"],
            "field_window": FIELD_OPTIMAL_WINDOW,
            "in_window": all(lo <= t <= hi for t in times),
            "peak_in_window": lo <= w["peak_h"] <= hi,
            "no_early_ai": all(t >= FIELD_NO_AI_BEFORE_H for t in times)}


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


def ai_efficacy(ai_h: float, parity: str = "sow",
                wei_days: float = NORMAL_WEI, steps: int = 200) -> float:
    """수정 1회의 유효도 0~1 — 정자 가용 구간과 난자 유효 구간의 겹침으로 계산.

    이전 구현은 "배란 직전일수록 좋다"고 보아 **배란 시각 정각을 최적(1.0)** 으로
    줬다. 그런데 현장 지침의 수태율 곡선은 배란보다 이른 시점에서 정점을 찍고
    배란 무렵엔 이미 내려온다. 원인은 수정능획득이다 — 배란 직전에 주입한 정자는
    아직 수정 능력이 없어, 난자가 나왔을 때 쓸 수 있는 정자가 없다.

    그래서 시간 겹침을 직접 적분한다:
      정자 수정 가능 구간 S = [주입 + 수정능획득, 주입 + 생존시간]
      난자 유효 구간      O = [배란, 배란 + 난자수명]
      유효도 = (1/난자수명) ∫_{S∩O} w_정자(경과) · w_난자(경과) dτ

    가중치는 둘 다 시간이 갈수록 떨어진다(정자는 완만히, 난자는 급격히).
    이 형태는 '배란 4~12h 전 주입이 최적'이라는 보고와 일치하며, 배란 직전·직후
    주입이 나쁜 이유도 같은 식에서 자동으로 나온다.
    """
    ov = ovulation_time(parity, wei_days)
    s0, s1 = float(ai_h) + CAPACITATION_H, float(ai_h) + SPERM_VIABLE_H
    o0, o1 = ov, ov + OVUM_VIABLE_H
    lo, hi = max(s0, o0), min(s1, o1)
    if hi <= lo:
        return 0.0
    acc, dt = 0.0, (hi - lo) / steps
    for i in range(steps):
        tau = lo + (i + 0.5) * dt
        age_s = tau - float(ai_h)                 # 주입 후 경과
        age_o = tau - ov                          # 배란 후 경과
        w_s = 1.0 - 0.4 * (age_s - CAPACITATION_H) / max(
            1e-9, SPERM_VIABLE_H - CAPACITATION_H)
        w_o = 1.0 - age_o / OVUM_VIABLE_H
        acc += max(0.0, w_s) * max(0.0, w_o) * dt
    return max(0.0, min(1.0, acc / OVUM_VIABLE_H))


def conception_prob(ai_hours: list, parity: str = "sow",
                    wei_days: float = NORMAL_WEI, base: float = 1.55) -> float:
    """수정 시각(발정 시작 후 h) 목록 → 기대 수태율.

    여러 번 수정하면 실패 확률이 곱으로 줄어든다(독립 근사).
    base 는 유효도를 수태율로 환산하는 계수 — 적기 2회 수정 시 85~90% 대가
    나오도록 잡았다(관리·정액 품질 등 다른 요인이 이미 반영된 상한).
    """
    eff = [ai_efficacy(t, parity, wei_days) for t in ai_hours]
    if not eff:
        return 0.0
    fail = 1.0
    for e in eff:
        fail *= max(0.0, 1.0 - base * e)
    return round(1.0 - fail, 3)


def timing_under_detection(check_interval_h: float, offsets=(12.0, 24.0),
                           parity: str = "sow", wei_days: float = NORMAL_WEI,
                           steps: int = 24) -> float:
    """**발정 확인 주기**가 수태율에 미치는 영향 — 이 앱의 실제 가치.

    적기 계산이 아무리 정확해도 **발정이 언제 시작됐는지 모르면** 쓸 수 없다.
    하루 2회 육안 점검이면 발정 시작을 최대 12h 늦게 알게 되고, 수정 시각은
    그만큼 통째로 밀린다. 즉 관행 대비 개선의 본질은 '더 좋은 시각표'가 아니라
    **관측 지연의 제거**다.

    점검 주기 T 일 때 실제 발정 시작은 발견 시점보다 U(0,T) 만큼 앞이다.
    수정은 '발견 + offset' 에 하므로 발정 시작 기준으로는 offset + U(0,T) 가
    된다. 그 분포에 대한 기대 수태율을 반환한다.
    """
    T = max(0.0, float(check_interval_h))
    if T <= 1e-9:
        return conception_prob(list(offsets), parity, wei_days)
    tot = 0.0
    for i in range(steps):
        lag = (i + 0.5) * T / steps          # 발견이 늦은 정도
        tot += conception_prob([o + lag for o in offsets], parity, wei_days)
    return round(tot / steps, 3)


def best_offsets_for_interval(check_interval_h: float, parity: str = "sow",
                              wei_days: float = NORMAL_WEI,
                              min_gap_h: float = 8.0) -> tuple:
    """점검 주기 T 를 아는 농장이 고를 **최적 고정 프로토콜**(발견 후 h).

    이게 없으면 비교가 불공정해진다. 적기 오프셋(24/32h)을 그대로 둔 채 지연만
    키우면 하루 1회 점검의 수태율이 0.37 로 나왔다 — 현실에 없는 숫자다. 실제로
    하루 1회 점검하는 농장은 발견이 늦다는 걸 알고 **더 이르게** 주입한다.
    그러니 각 주기마다 그 주기에 맞는 최선의 프로토콜을 찾아 비교해야 하고,
    남는 차이가 곧 **불확실성 자체의 비용**이다.
    """
    grid = [i * 2.0 for i in range(0, 19)]          # 발견 후 0~36h
    best, best_p = (0.0, min_gap_h), -1.0
    for i, a in enumerate(grid):
        for b in grid[i:]:
            if b - a < min_gap_h:
                continue
            p = timing_under_detection(check_interval_h, (a, b), parity, wei_days)
            if p > best_p:
                best_p, best = p, (a, b)
    return best


def detection_value(check_interval_h: float, parity: str = "sow",
                    wei_days: float = NORMAL_WEI) -> dict:
    """점검 주기별 기대 수태율 + 연속 관측(CCTV) 대비 손실.

    각 주기는 **그 주기에 최적화된 프로토콜**을 쓴다고 가정한다(공정 비교).
    """
    w = insemination_window(parity, wei_days)
    best = conception_prob([w["ai1_h"], w["ai2_h"]], parity, wei_days)
    off = best_offsets_for_interval(check_interval_h, parity, wei_days)
    got = timing_under_detection(check_interval_h, off, parity, wei_days)
    return {"check_interval_h": check_interval_h, "conception": got,
            "offsets": off, "best_possible": best,
            "loss_pp": round((best - got) * 100, 1)}


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
    print("=== 발정 전후 타임라인 (승가허용 시작 = 0h) ===")
    tl = estrus_timeline("sow", NORMAL_WEI)
    for k, label in (("vulva_change", "외음부 변화"), ("prodromal", "발정징후"),
                     ("standing_heat", "승가허용"), ("back_pressure", "등누르기 허용"),
                     ("ai_window", "주입 적기(지침)")):
        a, b = tl[k]
        print(f"  {label:<14} {a:>+6.0f}h ~ {b:>+6.0f}h")
    print(f"  {'배란':<14} {tl['ovulation']:>+6.0f}h")
    print("  → 외음부 변화는 승가허용보다 이틀 먼저 시작한다. 카메라가 외음부를"
          "\n    읽으면 승가허용 전에 미리 대비할 수 있다(조기 신호).")

    print("\n=== 수정 유효도 곡선 (sow, WEI 7 · 배란 36h) ===")
    for t in range(0, 45, 4):
        e = ai_efficacy(t, "sow", NORMAL_WEI)
        zone = ("주입금지" if t < FIELD_NO_AI_BEFORE_H else
                "적기" if t <= FIELD_OPTIMAL_WINDOW[1] else "늦음")
        print(f"  {t:>3}h {e:.3f} {'█' * int(e * 50):<26} {zone}")

    print("\n=== 교배 적기 (발정 시작 기준 시간) ===")
    for parity in ("sow", "gilt"):
        for wei in (4, 7, 10):
            w = insemination_window(parity, wei)
            chk = check_against_field_guide(parity, wei)
            ok = "지침 적기 내" if chk["in_window"] else "⚠ 지침 이탈"
            print(f"  {parity:5s} WEI {wei:2d}일 → 발정지속 {w['estrus_duration_h']}h · "
                  f"배란 {w['ovulation_h']}h · 창 {w['window_start_h']}~{w['window_end_h']}h · "
                  f"권장 {w['ai1_h']}h, {w['ai2_h']}h  [{ok}]")

    print("\n=== 발정 확인 주기가 수태율에 미치는 영향 (앱의 실제 가치) ===")
    print("  각 주기는 '그 주기에 최적화된 프로토콜'을 쓴다고 본다 — 공정 비교.")
    for iv, label in ((0, "연속(CCTV)"), (2, "2시간"), (6, "6시간"),
                      (12, "하루 2회"), (24, "하루 1회")):
        d = detection_value(iv, "sow", NORMAL_WEI)
        print(f"  {label:<10} 프로토콜 발견+{d['offsets'][0]:.0f}/{d['offsets'][1]:.0f}h → "
              f"수태율 {d['conception']:.3f}  (연속 대비 {-d['loss_pp']:+.1f}pp)")
    print("  → 하루 2회 점검의 최적 프로토콜이 '발견 후 14/22h' 로 나오는데, 이는"
          "\n    현장 지침의 12/24h 관행과 사실상 같다. 모델이 관행을 독립적으로"
          "\n    재현한 셈이며, 거꾸로 관행은 '하루 2회 점검'을 전제로 최적이다.")
    print("  → 즉 개선의 본질은 시각표가 아니라 **관측 지연의 제거**다.")

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
