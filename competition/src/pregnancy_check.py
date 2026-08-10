"""임신진단 3단계 체크포인트 — 재발돈을 언제 잡느냐가 공태일을 결정한다.

현장 지침의 진단 체계는 한 번이 아니라 **세 번**이다:

    3주   (18~24일)  웅돈노출 + 발정체크   재발돈의 80% 를 여기서 잡는다
    5주   (30~40일)  초음파 진단          15%  (3주에 놓친 규칙재발·불규칙재발·초기유산)
    8~10주(56~70일)  육안 관찰            5%   (앞서 놓친 것·유산·문제 모돈)

여기서 이 프로젝트에 결정적인 사실이 하나 나온다. **가장 많이 잡는 1차 관문이
초음파가 아니라 발정체크다.** 즉 임신진단의 80% 는 장비 문제가 아니라 *관찰*
문제이고, 그것이 바로 이 앱이 자동화하는 대상이다.

놓치면 비용은 시간으로 청구된다. 교배 21일 뒤 재발을 잡으면 다음 교배까지
공태가 21일이지만, 5주에 잡으면 35일, 8~10주면 63일이다. 같은 실패인데 **놓친
기간만큼 공태일이 곱해진다** — 그래서 조기 검출이 곧 회전율이다.

  detection_cascade()  단계별 검출·누락 흐름과 평균 공태일
  npd_from_returns()   재발돈 1두가 만드는 공태일 기대값
  value_of_early()     3주 검출률 개선의 연간 금액 효과
  checkpoint_tasks()   개체 교배일 → 3단계 진단 작업 일정

    python competition/src/pregnancy_check.py
"""
from __future__ import annotations

import os
import sys
from datetime import timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import breeding_timing as bt  # noqa: E402
import repro_calendar as rc  # noqa: E402

RETURN_CYCLE = bt.RETURN_CYCLE      # 21 — 규칙재발 주기

# (이름, 검사 시작일, 종료일, 방법, 이 관문에서 잡히는 재발돈 비율, 작업 분류)
# 비율은 현장 지침 표의 '재발돈 발생 비율' — 전체 재발돈 중 그 시기에 드러나는 몫.
# 1차 관문은 초음파가 아니라 발정체크이므로 작업 분류도 '재발정 확인'이 맞다.
CHECKPOINTS = [
    ("3주", 18, 24, "웅돈노출 + 발정체크", 0.80, "재발정 확인"),
    ("5주", 30, 40, "초음파 진단", 0.15, "임신감정"),
    ("8~10주", 56, 70, "육안 관찰", 0.05, "임신감정"),
]

# 각 관문을 '실제로 수행했을 때' 잡아내는 확률(민감도). 3주 발정체크는 사람이
# 하루 두 번 보는 방식이면 놓치는 게 많다 — 이 값이 앱이 끌어올리는 지점이다.
DEFAULT_SENSITIVITY = {"3주": 0.70, "5주": 0.95, "8~10주": 0.90}
CCTV_SENSITIVITY = {"3주": 0.92, "5주": 0.95, "8~10주": 0.90}

NPD_COST_WON = 6000        # 공태 1일당 비용(사료 + 기회비용)


def _mid(a: int, b: int) -> float:
    return (a + b) / 2.0


def detection_cascade(sensitivity: dict | None = None) -> list:
    """재발돈 100% 가 세 관문을 거치며 어떻게 걸러지는지.

    관문마다 '그 시기에 드러나는 몫 × 민감도' 만 잡히고, 놓친 몫은 다음 관문으로
    넘어간다. 마지막까지 놓치면 그대로 장기 공태돈이 된다.
    """
    sens = dict(DEFAULT_SENSITIVITY if sensitivity is None else sensitivity)
    carried = 0.0           # 앞 관문에서 놓쳐 넘어온 몫
    rows = []
    for name, d0, d1, method, share, _task in CHECKPOINTS:
        available = share + carried
        s = sens.get(name, 0.9)
        caught = available * s
        carried = available - caught
        rows.append({"name": name, "day_from": d0, "day_to": d1,
                     "method": method, "share": share,
                     "sensitivity": s, "caught": round(caught, 4),
                     "missed_forward": round(carried, 4),
                     "npd_if_caught": round(_mid(d0, d1), 1)})
    rows.append({"name": "미검출", "day_from": None, "day_to": None,
                 "method": "-", "share": 0.0, "sensitivity": 0.0,
                 "caught": 0.0, "missed_forward": round(carried, 4),
                 "npd_if_caught": 114.0})     # 분만예정일에야 드러남
    return rows


def npd_from_returns(sensitivity: dict | None = None) -> float:
    """재발돈 1두가 만드는 기대 공태일.

    관문에서 잡히면 그날부터 재교배가 가능하므로, 잡힌 시점이 곧 공태일이다.
    끝까지 놓치면 분만 예정일(114일)에야 '빈 배'가 드러난다.
    """
    rows = detection_cascade(sensitivity)
    total = sum(r["caught"] * r["npd_if_caught"] for r in rows)
    total += rows[-1]["missed_forward"] * rows[-1]["npd_if_caught"]
    return round(total, 1)


def value_of_early(n_sows: int, conception_rate: float = 0.82,
                   base_sens: dict | None = None,
                   improved_sens: dict | None = None,
                   npd_cost_won: int = NPD_COST_WON) -> dict:
    """3주 발정체크 민감도 개선의 연간 효과.

    수태율 자체는 그대로 두고 **검출 시점만** 당겼을 때의 이득이다. 수태율 개선
    효과와 섞지 않으려는 것 — 두 효과를 합산하면 이중 계산이 된다.
    """
    b = dict(DEFAULT_SENSITIVITY if base_sens is None else base_sens)
    a = dict(CCTV_SENSITIVITY if improved_sens is None else improved_sens)
    npd_b, npd_a = npd_from_returns(b), npd_from_returns(a)
    cycles = 365.0 / bt.cycle_days(conception_rate)
    returns_year = n_sows * cycles * (1.0 - conception_rate)
    saved = returns_year * (npd_b - npd_a)
    return {"n_sows": n_sows, "conception_rate": conception_rate,
            "returns_per_year": round(returns_year, 1),
            "npd_per_return_before": npd_b, "npd_per_return_after": npd_a,
            "npd_saved_per_return": round(npd_b - npd_a, 1),
            "npd_days_saved_year": round(saved, 0),
            "won_saved_year": int(saved * npd_cost_won),
            "sens_before": b.get("3주"), "sens_after": a.get("3주")}


def checkpoint_tasks(service_date, estimated: bool = True) -> list:
    """교배일 → 3단계 진단 작업(캘린더에 넣을 형태).

    구간의 시작일을 작업일로 잡고, 상세에 구간과 방법을 적는다.
    """
    s = rc._d(service_date)
    out = []
    for name, d0, d1, method, share, task in CHECKPOINTS:
        out.append({
            "date": s + timedelta(days=d0),
            "task": task,
            "detail": f"{name} ({d0}~{d1}일) {method} — 재발돈의 {share:.0%}",
            "estimated": estimated,
            # 잡아내는 몫이 큰 관문일수록 우선순위를 높인다
            "priority": rc.PRIORITY.get(task, 60) + int(share * 30),
            "window_end": s + timedelta(days=d1),
            "checkpoint": name,
        })
    return out


def main() -> int:
    print("=== 임신진단 3단계 (현장 지침) ===")
    print(f"  {'단계':<7} {'시기':<10} {'방법':<20} {'재발 비율':>8}")
    for name, d0, d1, method, share, _t in CHECKPOINTS:
        print(f"  {name:<7} {f'{d0}~{d1}일':<10} {method:<20} {share:>8.0%}")

    print("\n=== 검출 캐스케이드 (재발돈 100두 기준) ===")
    for label, sens in (("육안 점검", DEFAULT_SENSITIVITY),
                        ("CCTV 발정탐지", CCTV_SENSITIVITY)):
        rows = detection_cascade(sens)
        print(f"\n  [{label}]  3주 민감도 {sens['3주']:.0%}")
        print(f"    {'단계':<7} {'검출':>7} {'누적누락':>8} {'공태일':>7}")
        for r in rows:
            print(f"    {r['name']:<7} {r['caught'] * 100:>6.1f}두 "
                  f"{r['missed_forward'] * 100:>7.1f}두 {r['npd_if_caught']:>7.0f}")
        print(f"    → 재발돈 1두당 기대 공태일 {npd_from_returns(sens):.1f}일")

    print("\n=== 3주 검출률 개선의 가치 (모돈 300두, 수태율 82%) ===")
    print("  가치는 '그 농장이 초음파를 제대로 하는가'에 따라 크게 달라진다.")
    scenarios = [
        ("초음파 철저 (5주 95%)", {"3주": 0.70, "5주": 0.95, "8~10주": 0.90},
         {"3주": 0.92, "5주": 0.95, "8~10주": 0.90}),
        ("초음파 부실 (5주 50%)", {"3주": 0.70, "5주": 0.50, "8~10주": 0.90},
         {"3주": 0.92, "5주": 0.50, "8~10주": 0.90}),
        ("초음파 없음 (5주 0%)", {"3주": 0.70, "5주": 0.0, "8~10주": 0.90},
         {"3주": 0.92, "5주": 0.0, "8~10주": 0.90}),
    ]
    for label, b, a in scenarios:
        v = value_of_early(300, base_sens=b, improved_sens=a)
        print(f"  {label:<20} 공태 {v['npd_per_return_before']:>5.1f}→"
              f"{v['npd_per_return_after']:>5.1f}일/두 · "
              f"연 {v['npd_days_saved_year']:>5,.0f}일 · "
              f"약 {v['won_saved_year']:>10,}원/년")
    v = value_of_early(300)
    print(f"  (연간 재발돈 {v['returns_per_year']:.0f}두 기준)")
    print("  → 초음파를 철저히 하는 농장에서는 3주 개선의 여지가 작다. 5주에서"
          "\n    어차피 잡히고 차이는 14일뿐이기 때문이다. 반대로 초음파가 부실한"
          "\n    농장일수록 이 앱의 값어치가 커진다 — 과장하지 말고 그렇게 팔아야 한다.")

    print("\n=== 개체 일정 예시 (교배 2026-08-16) ===")
    for t in checkpoint_tasks("2026-08-16"):
        print(f"  {t['date']:%Y-%m-%d}~{t['window_end']:%m-%d}  {t['detail']}")

    print("\n※ 핵심: 임신진단의 1차 관문은 초음파가 아니라 **발정체크**이고 재발돈의"
          "\n  80% 가 거기서 드러난다. 장비가 아니라 관찰의 문제이며, 이 앱이 자동화하는"
          "\n  대상이 정확히 그 지점이다.")
    print("※ 민감도 70%→92% 는 가정값이다. 실측 검증에는 농장의 3주 재발 검출 기록과"
          "\n  CCTV 판정을 맞대어 봐야 한다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
