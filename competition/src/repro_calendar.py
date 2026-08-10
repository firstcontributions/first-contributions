"""번식 작업 캘린더 — 날짜 하나로 전체 일정을 자동 생성(입력 간소화).

현장 입력 부담이 번식관리 앱이 외면받는 흔한 이유다. 번식 주기는 간격이 정해져
있으므로 **기준일 하나만 넣으면** 이후 작업일이 전부 계산된다. 농가는 값을 채우는
대신 **날짜를 확인·조정**만 하면 된다.

자동 생성되는 일정(경산돈, 이유 기준):
    이유 D0
    → 발정 관찰 시작   D+3      (WEI 하한 전부터 관찰)
    → 발정 예상        D+WEI    (산차·계절로 보정)
    → **교배 1·2차**    발정 시각 + 적기(breeding_timing, WEI·산차 보정)
    → 재발정 확인      교배+21일  (안 돌아오면 임신 가능성)
    → 임신감정(초음파)  교배+30일
    → 분만사 이동      분만 7일 전
    → **분만 예정**     교배+115일  (3-3-3 규칙 114~115일)
    → 이유 예정        분만+28일   (포유기간)
    → 1주기 ≈ 150일

후보돈(gilt)은 **이유가 없다** — 초발정 확인일(또는 초교배 예정일)이 기준이다.
경산돈 경로에 후보돈을 억지로 넣으면 '발정 관찰'이 '교배' 뒤에 오는 모순이 생긴다.
그래서 진입점을 셋으로 나눈다:

    schedule_from_weaning(이유일)   경산돈
    schedule_from_estrus(발정일)    후보돈 초교배 / CCTV 발정 확인
    schedule_from_service(교배일)   과거 기록만 있는 경우

CCTV 가 실제 발정을 확인하면 그 시각으로 교배 일정이 **자동 갱신**된다
(예상일은 어디까지나 예정, 관측이 우선). 예상은 `~`, 확정은 공백으로 구분한다.

그룹 등록(입력시간 감소): 같은 날 이유한 모돈은 일정이 같으므로 개체별로 다시
입력할 필요가 없다. `group_from_weaning()` 이 한 번의 입력으로 N두 일정을 만든다.

    python competition/src/repro_calendar.py            # 시연
    python competition/src/repro_calendar.py 2026-08-10 # 이유일 지정
"""
from __future__ import annotations

import os
import sys
from datetime import date, datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import breeding_timing as bt  # noqa: E402

# 주기 상수(일) — breeding_timing 과 공유
GESTATION = bt.GESTATION            # 115 (3-3-3 규칙 114~115)
LACTATION = bt.LACTATION            # 28
RETURN_CHECK = bt.RETURN_CYCLE      # 21 (재발정 확인)
OBSERVE_LEAD = 3                    # 이유 후 관찰 시작
PREG_CHECK_US = 30                  # 초음파 임신감정(교배 후)
MOVE_BEFORE_FARROW = 7              # 분만사 이동(분만 전)

# 산차별 기대 WEI(일). 초산돈은 포유 중 체력 소모가 커 재귀발정이 늦다.
WEI_BY_PARITY = {"primiparous": 6.0, "sow": 5.0}

# 작업 종류별 중요도(경보 우선순위와 연결)
PRIORITY = {"교배": 100, "분만": 90, "발정 관찰": 80, "재발정 확인": 70,
            "임신감정": 60, "분만사 이동": 50, "이유": 40}


def _d(x) -> date:
    if isinstance(x, datetime):
        return x.date()
    if isinstance(x, date):
        return x
    return datetime.strptime(str(x)[:10], "%Y-%m-%d").date()


def _dt(x, default_hour: int = 8) -> datetime:
    if isinstance(x, datetime):
        return x
    return datetime.combine(_d(x), datetime.min.time()) + timedelta(hours=default_hour)


def expected_wei(parity: str = "sow", season_hot: bool = False) -> float:
    """기대 이유-발정 간격(일). 더위(하계 불임)면 늘어난다."""
    w = WEI_BY_PARITY.get(parity, WEI_BY_PARITY["sow"])
    return w + (1.5 if season_hot else 0.0)


def _preg_checks(service_date) -> list:
    """교배일 → 임신진단 작업들.

    임신감정을 '교배 후 30일 초음파' 한 번으로 두면 현장 지침과 어긋난다.
    실제 1차 관문은 3주 발정체크이고 재발돈의 80% 가 거기서 드러난다. 그래서
    재발정 확인과 임신진단을 따로 두지 않고 **3단계 체크포인트**로 합친다.
    """
    import pregnancy_check as pc
    return pc.checkpoint_tasks(service_date)


def _finish(tasks: list) -> list:
    # 이미 우선순위가 실린 작업(임신진단 체크포인트 등)은 덮어쓰지 않는다 —
    # 관문마다 잡아내는 몫이 달라 같은 '임신감정'이라도 급함이 다르다.
    for t in tasks:
        t.setdefault("priority", PRIORITY.get(t["task"], 10))
    return sorted(tasks, key=lambda t: (t["date"], -t["priority"]))


def schedule_from_estrus(estrus, parity: str = "sow", wei_days: float | None = None,
                         confirmed: bool = True) -> list:
    """발정(확인 또는 예상) 시각 → 교배 이후 전체 일정.

    후보돈 초교배와 CCTV 발정 확인이 같은 경로를 쓴다. 교배 적기는 발정 시작
    기준 시간이므로 **시각(hour)까지** 의미가 있다 — 날짜만 주면 08시로 본다.
    wei_days: 교배 적기 보정용. 후보돈은 이유 개념이 없어 기본값(7)을 쓴다.
    """
    e_dt = _dt(estrus)
    p = "gilt" if parity == "gilt" else "sow"
    wei = bt.NORMAL_WEI if wei_days is None else float(wei_days)
    est = not confirmed

    win = bt.insemination_window(p, wei)
    tasks = [{"date": e_dt.date(), "task": "발정 관찰",
              "detail": ("발정 확인됨" if confirmed else "발정 예상일"),
              "estimated": est}]
    ai_dts = []
    for i, h in enumerate((win["ai1_h"], win["ai2_h"]), start=1):
        t = e_dt + timedelta(hours=float(h))
        ai_dts.append(t)
        tasks.append({"date": t.date(), "task": "교배",
                      "detail": (f"{i}차 — 발정 후 {h:.0f}h ({t:%H시}) · "
                                 f"배란 추정 {win['ovulation_h']:.0f}h"),
                      "estimated": est})
    svc = ai_dts[0].date()
    tasks += _preg_checks(svc) + [
        {"date": svc + timedelta(days=GESTATION - MOVE_BEFORE_FARROW),
         "task": "분만사 이동", "detail": f"분만 {MOVE_BEFORE_FARROW}일 전",
         "estimated": True},
        {"date": svc + timedelta(days=GESTATION), "task": "분만",
         "detail": f"교배 후 {GESTATION}일 (3-3-3 규칙)", "estimated": True},
        {"date": svc + timedelta(days=GESTATION + LACTATION), "task": "이유",
         "detail": f"포유 {LACTATION}일 — 다음 주기 시작", "estimated": True},
    ]
    return _finish(tasks)


def schedule_from_weaning(weaning, parity: str = "sow", season_hot: bool = False,
                          estrus_confirmed=None) -> list:
    """이유일 → 전체 작업 일정(경산돈).

    estrus_confirmed: CCTV/육안으로 **실제 확인된 발정 시작 일시**(선택).
      주어지면 교배 일정을 그 시각 기준으로 다시 잡는다(예상보다 관측 우선).
    반환: [{date, task, detail, priority, estimated}] 날짜순
    """
    if parity == "gilt":
        raise ValueError("후보돈은 이유가 없다 — schedule_from_estrus() 를 쓸 것")
    w0 = _d(weaning)
    wei = expected_wei(parity, season_hot)

    if estrus_confirmed is not None:
        e_dt = _dt(estrus_confirmed, default_hour=6)
        wei_actual = max(0.0, (e_dt.date() - w0).days)
        confirmed = True
    else:
        e_dt = _dt(w0 + timedelta(days=round(wei)))
        wei_actual = wei
        confirmed = False

    head = [
        {"date": w0, "task": "이유", "detail": f"산차구분 {parity}",
         "estimated": False},
        {"date": w0 + timedelta(days=OBSERVE_LEAD), "task": "발정 관찰",
         "detail": f"CCTV 관찰 시작 (예상 발정 D+{wei:.0f})", "estimated": True},
    ]
    return _finish(head + schedule_from_estrus(
        e_dt, parity=parity, wei_days=wei_actual, confirmed=confirmed))


def schedule_from_service(service, parity: str = "sow") -> list:
    """교배일만 아는 경우(이유일 모름) → 이후 일정."""
    s = _d(service)
    tasks = [
        {"date": s, "task": "교배", "detail": "입력된 교배일", "estimated": False},
        *_preg_checks(s),
        {"date": s + timedelta(days=GESTATION - MOVE_BEFORE_FARROW),
         "task": "분만사 이동", "detail": f"분만 {MOVE_BEFORE_FARROW}일 전",
         "estimated": True},
        {"date": s + timedelta(days=GESTATION), "task": "분만",
         "detail": f"교배 후 {GESTATION}일", "estimated": True},
        {"date": s + timedelta(days=GESTATION + LACTATION), "task": "이유",
         "detail": f"포유 {LACTATION}일", "estimated": True},
    ]
    return _finish(tasks)


# --------------------------------------------------------------------------
# 그룹(일괄) 등록 — 같은 날 이유한 모돈은 일정이 같다
def group_from_weaning(ids, weaning, parity: str = "sow",
                       season_hot: bool = False) -> dict:
    """이유 배치 하나 → N두 일정. 입력 1회로 개체별 캘린더가 생긴다.

    ids: 개체번호 목록, 또는 {개체번호: 산차구분} 매핑(산차가 섞인 배치용).
    """
    if isinstance(ids, dict):
        pairs = list(ids.items())
    else:
        pairs = [(i, parity) for i in ids]
    return {pid: schedule_from_weaning(weaning, parity=pr, season_hot=season_hot)
            for pid, pr in pairs}


def confirm_estrus(schedules: dict, pid: str, when, weaning=None) -> dict:
    """그룹 일정 중 한 개체의 발정이 확인되면 그 개체만 다시 계산한다.

    weaning 을 주지 않으면 기존 일정의 '이유' 작업에서 되찾는다.
    """
    cur = schedules.get(pid)
    if cur is None:
        raise KeyError(pid)
    if weaning is None:
        weaning = next((t["date"] for t in cur if t["task"] == "이유"), None)
        if weaning is None:
            raise ValueError(f"{pid}: 이유일을 찾을 수 없다")
    out = dict(schedules)
    out[pid] = schedule_from_weaning(weaning, estrus_confirmed=when)
    return out


def due_today(schedules: dict, today=None, horizon: int = 0) -> list:
    """개체별 일정 dict → 오늘(또는 horizon 일 이내) 할 일 목록(긴급도순).

    schedules: {개체ID: [task, ...]}
    """
    t0 = _d(today) if today else date.today()
    out = []
    for pid, tasks in schedules.items():
        for t in tasks:
            dd = (t["date"] - t0).days
            if 0 <= dd <= horizon:
                out.append({**t, "id": pid, "d_day": dd})
    return sorted(out, key=lambda t: (t["d_day"], -t["priority"]))


def overdue(schedules: dict, today=None, grace: int = 1) -> list:
    """기한이 지난 작업 — 놓친 교배·임신감정을 잡아낸다(공태일의 주범)."""
    t0 = _d(today) if today else date.today()
    out = []
    for pid, tasks in schedules.items():
        for t in tasks:
            late = (t0 - t["date"]).days
            if late > grace:
                out.append({**t, "id": pid, "late_days": late})
    return sorted(out, key=lambda t: (-t["priority"], -t["late_days"]))


def cycle_summary(tasks: list) -> dict:
    """일정에서 회전 지표를 뽑는다(이유→다음 이유 = 1주기)."""
    weans = [t["date"] for t in tasks if t["task"] == "이유"]
    svc = next((t["date"] for t in tasks if t["task"] == "교배"), None)
    farrow = next((t["date"] for t in tasks if t["task"] == "분만"), None)
    if len(weans) < 2 or svc is None:
        return {}
    cycle = (weans[-1] - weans[0]).days
    return {"cycle_days": cycle,
            "turnover_per_year": round(365 / cycle, 2) if cycle else None,
            "wei_days": (svc - weans[0]).days,
            "service_date": svc, "farrow_date": farrow,
            "npd_days": cycle - GESTATION - LACTATION}


# --------------------------------------------------------------------------
def _show(tasks, only=None):
    for t in tasks:
        if only and t["task"] not in only:
            continue
        mark = "~" if t["estimated"] else " "
        print(f" {mark}{t['date']:%Y-%m-%d}  {t['task']:<9} {t['detail']}")


def main() -> int:
    wean = sys.argv[1] if len(sys.argv) > 1 else "2026-08-10"

    print(f"=== 경산돈: 이유일 {wean} 하나만 입력 ===")
    tasks = schedule_from_weaning(wean, parity="sow")
    _show(tasks)
    s = cycle_summary(tasks)
    print(f"   → 1주기 {s['cycle_days']}일 · 회전율 {s['turnover_per_year']}회/년 "
          f"· 공태일 {s['npd_days']}일")

    print("\n=== 후보돈: 이유가 없다 — 초발정 확인일이 기준 ===")
    _show(schedule_from_estrus("2026-08-10", parity="gilt"))

    print("\n=== CCTV 발정 확인 시 자동 갱신 (예상 8/15 → 확인 8/14) ===")
    conf = datetime(2026, 8, 14, 6, 0)
    _show(schedule_from_weaning(wean, "sow", estrus_confirmed=conf),
          only={"발정 관찰", "교배"})
    print("   (~ = 예상, 공백 = 확정. 관측이 예상을 대체한다)")

    print("\n=== 그룹 등록: 이유 배치 1회 입력 → 12두 일정 ===")
    ids = [f"{2200+i}" for i in range(12)]
    grp = group_from_weaning(ids, wean)
    n_tasks = sum(len(v) for v in grp.values())
    print(f"  입력 1건(이유일 {wean}, {len(ids)}두) → 작업 {n_tasks}건 자동 생성")
    grp = confirm_estrus(grp, "2203", datetime(2026, 8, 14, 6, 0))
    print("  2203 발정 확인 → 해당 개체만 교배일 재계산:")
    _show(grp["2203"], only={"교배"})

    print("\n=== 오늘 할 일 (D-day 순) ===")
    today = "2026-08-16"
    todo = due_today(grp, today=today, horizon=1)
    print(f"  기준일 {today} · {len(todo)}건")
    for t in todo[:8]:
        mark = "~" if t["estimated"] else " "
        print(f"  D+{t['d_day']} {mark}{t['id']:>5} {t['task']:<9} {t['detail']}")

    print("\n=== 기한 경과 (놓친 작업 = 공태일) ===")
    late = overdue(grp, today="2026-08-20")
    for t in late[:4]:
        print(f"  {t['late_days']}일 경과 {t['id']:>5} {t['task']:<9} {t['detail']}")

    print("\n※ 예정일은 표준 간격 기반 추정이다. 실제 발정·분만은 개체차가 있으므로"
          "\n  관측(CCTV·육안)이 확인되면 그 값으로 일정이 갱신된다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
