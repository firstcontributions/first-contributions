"""개체 발정·임신 통합 관리표 + 향후 관리 일정.

앞의 모듈들이 각자 한 조각씩 답한다 — 어디 있는가(farm_registry), 번식 단계는
무엇인가(herd_board), 언제 무엇을 해야 하는가(repro_calendar), 임신은 확인됐는가
(pregnancy_check), 발정 징후가 보이는가(stall_estrus / 활동량). 현장이 필요한 건
그 다섯을 한 줄에 놓은 **개체별 한 행**이다.

    개체 | 위치 | 산차 | 단계 | 발정신호 | 임신확인 | 다음 작업 | D-day | 조치

설계에서 조심한 것 하나. 발정 점수와 임신 상태는 **서로 모순될 수 있다**.
임신 중인 개체에 발정 점수가 높게 나오면 그건 발정이 아니라 *경보*다 —
유산이거나 임신감정 오류이거나 개체 오인이다. 그래서 두 축을 곱해서 하나의
점수로 뭉개지 않고, 교차 결과를 그대로 드러낸다(`conflict` 열).

  ledger()        개체별 통합 한 행
  upcoming()      향후 N일 관리 일정(기간·축사동·작업별)
  workload()      날짜별 작업량 — 인력 배치용
  conflicts()     발정 신호 ↔ 임신 상태 모순 개체

    python competition/src/breeding_ledger.py
"""
from __future__ import annotations

import os
import sys
from datetime import date, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import farm_registry as fr  # noqa: E402
import herd_board as hb  # noqa: E402
import repro_calendar as rc  # noqa: E402

# 발정 점수 판정 경계 — stall_estrus / 활동량 점수 모두 0~1 로 정규화해 넣는다
ESTRUS_HI = 0.62         # 이 이상이면 '발정 의심'
ESTRUS_MID = 0.45        # 이 이상이면 '관찰'

# 단계별로 '발정 신호가 나와야 정상'인지 — 모순 판정의 기준
EXPECT_ESTRUS = {"공태": True, "후보": True, "교배": True,
                 "임신": False, "포유": False}

ACTIONS = {
    "교배": "정액 준비 · 적기 수정",
    "발정 관찰": "승가허용 확인(등누르기)",
    "재발정 확인": "웅돈 노출 + 발정체크",
    "임신감정": "초음파 확인",
    "분만사 이동": "분만사 자리 확보 후 이동",
    "분만": "분만 준비 · 야간 순찰",
    "이유": "자돈 분리 · 모돈 교배사 이동",
}


OVERDUE_HORIZON = 14      # 이보다 오래 지난 작업은 조치 불가 — 큐에서 뺀다


def present(v) -> bool:
    """None·NaN 을 결측으로 본다 — 소비 측이 반드시 이걸 써야 한다.

    `if row["conflict"]:` 로 끝내면 안 된다. pandas 를 거친 결측은 float NaN 이
    되어 오는데 bool(nan) 은 True 다. 그대로 두면 전 개체가 경보로 잡힌다(실제로
    68/68 이 그랬다). 결측이 생기는 곳이 여기이므로 판정도 여기서 제공한다.
    """
    return v is not None and v == v


def _still_actionable(task: dict, today: date) -> bool:
    """지난 작업이 아직 손쓸 여지가 있는지.

    체크포인트처럼 유효 구간(window_end)이 있으면 그 끝을 기준으로, 없으면
    예정일을 기준으로 본다. 어느 쪽이든 지난 지 OVERDUE_HORIZON 을 넘으면
    조치 대상이 아니다.
    """
    ref = task.get("window_end") or task["date"]
    return (today - ref).days <= OVERDUE_HORIZON


def _anchor(row, today: date) -> date:
    """기록에 남은 마지막 실제 사건 — 이보다 앞선 예정 작업은 완료로 본다.

    번식 기록은 '무엇을 했는가'만 남고 '무엇을 안 했는가'는 남지 않는다. 그래서
    완료 여부를 사건의 진행으로 역추론한다: 분만했다면 교배는 당연히 했다.
    """
    dates = [getattr(row, k, None)
             for k in ("service_date", "farrow_date", "weaning_date")]
    past = [d for d in dates if isinstance(d, date) and d <= today]
    return max(past) if past else date.min


def _estrus_label(score: float) -> str:
    if score is None or (isinstance(score, float) and np.isnan(score)):
        return "-"
    if score >= ESTRUS_HI:
        return "발정 의심"
    if score >= ESTRUS_MID:
        return "관찰"
    return "정상"


def _preg_label(row) -> str:
    """임신 확인 상태 — 교배 후 경과일과 통과한 체크포인트로 정한다."""
    if row["stage"] not in ("교배", "임신"):
        return "-"
    d = row.get("days_since_service")
    if d is None or (isinstance(d, float) and np.isnan(d)):
        return "미확인"
    if d < 18:
        return "확인 전"
    if d < 30:
        return "3주 통과"       # 재발 없음
    if d < 56:
        return "초음파 확인"
    return "임신 확정"


def ledger(farm: fr.Farm, herd: pd.DataFrame, schedules: dict,
           estrus_scores: dict | None = None, today=None) -> pd.DataFrame:
    """개체별 통합 한 행 — 위치·단계·발정·임신·다음 작업.

    schedules: {개체ID: [task, ...]}  (repro_calendar 결과)
    estrus_scores: {개체ID: 0~1}      (stall_estrus 또는 활동량 기반)
    """
    t0 = rc._d(today) if today else herd.attrs.get("today", date.today())
    es = estrus_scores or {}
    base = farm.table(herd)
    if not len(base):
        return base
    rows = []
    for r in base.itertuples(index=False):
        pid = r.id
        stage = getattr(r, "stage_h", None)
        svc = getattr(r, "service_date", None)
        dss = (t0 - svc).days if isinstance(svc, date) else np.nan
        score = es.get(pid, np.nan)

        # 이미 지나온 작업은 '놓친 것'이 아니다. 분만한 모돈에게 "교배 142일
        # 경과" 라고 알리면 경보가 통째로 못 쓰게 된다 — 실제로 그 버그가 있었고
        # 68두 전부가 지연으로 잡혔다. 기록에 남은 **마지막 실제 사건**을 기준선
        # 으로 삼아, 그보다 앞선 작업은 완료로 본다.
        anchor = _anchor(r, t0)

        # 다음 작업: 오늘 이후 가장 가까운 것(같은 날이면 우선순위 높은 것)
        tasks = [t for t in schedules.get(pid, []) if t["date"] >= t0]
        nxt = tasks[0] if tasks else None
        # 기한 지난 작업 중 가장 급한 것 — 기준선 이후이면서 **아직 손쓸 수 있는**
        # 것만. 임신 112일째 모돈에게 "3주 재발정 확인 94일 경과" 는 조치가
        # 불가능한 과거사다. 그런 항목은 성적 리포트의 몫이지 작업 큐가 아니다.
        late = [t for t in schedules.get(pid, [])
                if anchor < t["date"] < t0 and _still_actionable(t, t0)]
        late_top = max(late, key=lambda t: (t["priority"], t["date"])) if late else None

        row = {
            "id": pid, "loc": f"{r.barn} {r.pen} {r.slot}번", "barn": r.barn,
            "housing": r.housing, "parity": getattr(r, "parity", np.nan),
            "stage": stage,
            "estrus_score": score, "estrus": _estrus_label(score),
            "days_since_service": dss,
            "next_task": nxt["task"] if nxt else "-",
            "next_date": nxt["date"] if nxt else None,
            "d_day": (nxt["date"] - t0).days if nxt else None,
            "action": ACTIONS.get(nxt["task"], "-") if nxt else "-",
            "priority": nxt["priority"] if nxt else 0,
            "overdue": late_top["task"] if late_top else None,
            # 경과일은 판정과 같은 기준(구간이 있으면 구간 종료)으로 센다.
            # 예정일 기준으로 세면 "구간이 14일 전 닫혔는데 24일 경과" 처럼
            # 필터 기준과 표시가 어긋난다.
            "overdue_days": (t0 - (late_top.get("window_end")
                                   or late_top["date"])).days if late_top else 0,
        }
        row["pregnancy"] = _preg_label(row)
        rows.append(row)
    df = pd.DataFrame(rows)

    # 발정 신호 ↔ 번식 단계 모순. 곱해서 뭉개지 않고 별도 열로 남긴다.
    exp = df["stage"].map(EXPECT_ESTRUS)
    hot = df["estrus_score"] >= ESTRUS_HI
    # dtype 에 주의. pandas 3 은 [str, None, ...] 을 str dtype 으로 추론하면서
    # None 을 **float NaN** 으로 바꾼다. 그런데 bool(nan) 은 True 라서, dict 로
    # 꺼내 `if row["conflict"]:` 로 판정하면 전 개체가 경보로 잡힌다(실제로 68두
    # 전부가 그렇게 됐다). notna() 로는 정상으로 보여 더 늦게 발견된다.
    # object dtype 을 강제해 진짜 None 을 유지한다.
    MSG = "임신·포유 중 발정 신호 — 유산/오진/개체 오인 의심"
    df["conflict"] = pd.Series(
        [MSG if (bool(h) and e is not None and e == e and not e) else None
         for h, e in zip(hot, exp)], index=df.index, dtype=object)
    # 긴급도. 지연을 선형으로 키우면 19일 지난 임신감정이 **오늘 해야 할 교배**를
    # 눌러버린다. 교배·분만·발정관찰은 놓치면 그날로 기회가 사라지고 다음 발정
    # (21일)까지 기다려야 하므로, 임박한 시한작업에 별도 가중을 준다.
    # 지연 가중은 포화시킨다 — 이미 늦은 것들 사이의 순서는 덜 중요하다.
    dd = df["d_day"].fillna(99)
    decay = np.maximum(0.2, 1.0 - dd.clip(lower=0) / 14.0)
    time_critical = df["next_task"].isin(("교배", "분만", "발정 관찰")) & (dd <= 1)
    df["urgency"] = (df["priority"] * decay
                     + df["overdue_days"].clip(0, OVERDUE_HORIZON) * 4
                     + np.where(time_critical, 120, 0)
                     + np.where(df["conflict"].notna(), 60, 0)
                     + np.where(hot & (exp == True), 30, 0)).round(1)  # noqa: E712
    return df.sort_values("urgency", ascending=False).reset_index(drop=True)


def upcoming(schedules: dict, today=None, days: int = 14,
             farm: fr.Farm | None = None) -> pd.DataFrame:
    """향후 N일 관리 일정 — 날짜·작업·개체(+위치)."""
    t0 = rc._d(today) if today else date.today()
    end = t0 + timedelta(days=days)
    rows = []
    for pid, tasks in schedules.items():
        for t in tasks:
            if t0 <= t["date"] <= end:
                rows.append({"date": t["date"], "d_day": (t["date"] - t0).days,
                             "id": pid, "task": t["task"],
                             "detail": t["detail"], "priority": t["priority"],
                             "estimated": t["estimated"],
                             "loc": farm.label(pid) if farm else ""})
    df = pd.DataFrame(rows)
    if not len(df):
        return df
    return df.sort_values(["d_day", "priority"],
                          ascending=[True, False]).reset_index(drop=True)


def workload(schedules: dict, today=None, days: int = 14) -> pd.DataFrame:
    """날짜별 작업량 — 어느 날이 몰리는지 보고 미리 인력을 뺀다.

    번식 작업은 배치(이유 그룹)로 움직여서 특정 요일에 몰린다. 그날 사람이
    모자라면 교배를 놓치고, 놓친 교배는 21일 뒤에나 다시 온다.
    """
    up = upcoming(schedules, today, days)
    if not len(up):
        return up
    piv = up.pivot_table(index="date", columns="task", values="id",
                         aggfunc="count", fill_value=0)
    piv["합계"] = piv.sum(axis=1)
    return piv.reset_index()


def conflicts(led: pd.DataFrame) -> pd.DataFrame:
    """발정 신호 ↔ 임신 상태 모순 개체만."""
    if not len(led) or "conflict" not in led.columns:
        return pd.DataFrame()
    return led[led["conflict"].notna()][
        ["id", "loc", "stage", "estrus_score", "pregnancy", "conflict"]
    ].reset_index(drop=True)


# --------------------------------------------------------------------------
def build_demo(today="2026-08-10", seed: int = 11):
    """농장 + 모돈군 + 일정 + 발정 점수를 한 번에 만든 시연 세트."""
    rng = np.random.default_rng(seed)
    farm = fr.demo_farm()
    ids = sorted(farm._where)
    recs = hb.generate_demo(n=len(ids) + 40, today=today)[:len(ids)]
    for r, i in zip(recs, ids):
        r["id"] = i
    herd = hb.build_herd(recs, today=today)

    scheds, scores = {}, {}
    t0 = rc._d(today)
    for r in herd.itertuples(index=False):
        if isinstance(r.weaning_date, date):
            scheds[r.id] = rc.schedule_from_weaning(r.weaning_date)
        elif isinstance(r.service_date, date):
            scheds[r.id] = rc.schedule_from_service(r.service_date)
        else:
            # 후보돈은 이유가 없다 — 경산돈 경로를 쓰면 '이유 2일 경과' 같은
            # 있을 수 없는 지연 알림이 뜬다. 초발정 예정 기준으로 잡는다.
            scheds[r.id] = rc.schedule_from_estrus(
                t0 + timedelta(days=int(rng.integers(1, 14))),
                parity="gilt", confirmed=False)
        # 발정 점수: 공태·후보는 높게 나올 수 있고, 임신·포유는 낮다.
        # 소수는 일부러 모순되게 둔다 — 그런 개체를 잡아내는 게 이 표의 몫이다.
        if r.stage in ("공태", "후보", "교배"):
            s = rng.beta(4, 3)
        else:
            s = rng.beta(2, 8) if rng.random() > 0.04 else rng.uniform(0.65, 0.9)
        scores[r.id] = round(float(s), 3)
    return farm, herd, scheds, scores


def main() -> int:
    today = sys.argv[1] if len(sys.argv) > 1 else "2026-08-10"
    farm, herd, scheds, scores = build_demo(today)
    led = ledger(farm, herd, scheds, scores, today=today)

    print(f"=== 개체 발정·임신 통합 관리표 ({today}) · {len(led)}두 ===")
    print(f"  {'개체':>5} {'위치':<16} {'산차':>3} {'단계':<4} {'발정':<6} "
          f"{'임신':<8} {'다음작업':<9} {'D':>4}  조치")
    for r in led.head(14).itertuples(index=False):
        dd = "지남" if r.d_day is None else f"D-{r.d_day}" if r.d_day else "오늘"
        par = "-" if not np.isfinite(r.parity) else f"{int(r.parity)}"
        print(f"  {r.id:>5} {r.loc:<16} {par:>3} {str(r.stage):<4} "
              f"{r.estrus:<6} {r.pregnancy:<8} {r.next_task:<9} {dd:>4}  {r.action}")

    ov = led[led["overdue_days"] > 0]
    print(f"\n=== 기한 경과 {len(ov)}두 (놓친 작업 = 공태일) ===")
    for r in ov.head(5).itertuples(index=False):
        print(f"  {r.id} {r.loc:<16} {r.overdue:<9} {r.overdue_days}일 경과")

    cf = conflicts(led)
    print(f"\n=== 모순 경보 {len(cf)}두 ===")
    for r in cf.itertuples(index=False):
        print(f"  {r.id} {r.loc:<16} {r.stage} · 발정점수 {r.estrus_score:.2f} "
              f"→ {r.conflict}")
    if not len(cf):
        print("  없음")
    print("  ※ 발정 점수와 임신 상태를 곱해 한 점수로 뭉개면 이런 개체가 사라진다."
          "\n    임신 중 발정 신호는 발정이 아니라 유산·오진·개체 오인의 신호다.")

    print("\n=== 향후 14일 관리 일정 (상위 12건) ===")
    up = upcoming(scheds, today=today, days=14, farm=farm)
    for r in up.head(12).itertuples(index=False):
        mark = "~" if r.estimated else " "
        print(f" {mark}D+{r.d_day:<2} {r.date:%m/%d} {r.id:>5} {r.loc:<18} "
              f"{r.task:<9} {r.detail[:34]}")
    print(f"  … 총 {len(up)}건")

    print("\n=== 날짜별 작업량 (인력 배치) ===")
    wl = workload(scheds, today=today, days=14)
    cols = [c for c in wl.columns if c not in ("date", "합계")]
    # itertuples 는 '발정 관찰' 처럼 공백이 든 컬럼명을 _3 같은 이름으로 바꾼다.
    # getattr(r, '발정 관찰', 0) 이 조용히 0 을 돌려줘 표가 전부 0 으로 찍혔다.
    thresh = wl["합계"].quantile(0.8)
    print(f"  {'날짜':<12} " + " ".join(f"{c:>7}" for c in cols) + f" {'합계':>6}")
    for _, r in wl.iterrows():
        vals = " ".join(f"{int(r[c]):>7}" for c in cols)
        peak = "  ← 몰림" if r["합계"] >= thresh else ""
        print(f"  {r['date']:%Y-%m-%d} {vals} {int(r['합계']):>6}{peak}")
    print("  ※ 번식 작업은 이유 그룹 단위로 움직여 특정 날짜에 몰린다. 그날 사람이"
          "\n    모자라면 교배를 놓치고, 놓친 교배는 21일 뒤에나 다시 온다.")

    print("\n※ 합성 데이터 시연이다. 실제로는 농장 번식기록과 CCTV 발정 점수를 그대로"
          "\n  넣으면 같은 표가 나온다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
