"""작업 로그 — 무엇을 언제 누가 했는지 쌓고, 그것으로 일정을 정정한다.

지금까지 일정은 '예정'만 있고 '완료'가 없었다. 그래서 완료 여부를 사건 진행으로
**역추론**했다(분만했으면 교배는 했겠지). 그 추론은 큰 사건에는 통하지만
"오늘 아침 2022 교배 1차를 했다" 같은 것은 잡지 못한다. 결과적으로 이미 끝낸
작업이 조치 큐에 계속 남는다.

로그를 쌓으면 세 가지가 한꺼번에 풀린다:

  1) **큐 정정** — 완료 기록이 있으면 그 작업은 오늘 큐에서 빠진다.
  2) **성적 측정** — 예정일 대비 며칠에 실제로 했는가. 적기 준수율이 곧
     수태율의 선행 지표다(breeding_timing: 관측 지연 12h 당 -4.3pp).
  3) **책임 소재** — 누가 했는지 남으므로 교육·배치의 근거가 된다.

로그는 **추가만 한다**(append-only). 기록을 고치면 성적이 왜곡되므로, 정정이
필요하면 취소 기록을 덧붙이는 방식이다.

    python competition/src/work_log.py          # 시연(합성 로그 생성 후 집계)
파일: competition/data/work_log.csv
"""
from __future__ import annotations

import os
import sys
from datetime import date, datetime, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import repro_calendar as rc  # noqa: E402

LOG = os.path.join(ROOT, "competition", "data", "work_log.csv")
COLS = ["ts", "work_date", "animal_id", "task", "result", "operator",
        "planned_date", "note"]

RESULTS = ("완료", "미실시", "취소")
# 예정일 대비 며칠까지를 '정시'로 볼 것인가. 작업마다 유효 구간이 다르다 —
# 교배는 반나절만 밀려도 적기를 놓치지만 임신감정은 며칠 여유가 있다.
ON_TIME = {"교배": 0, "발정 관찰": 1, "분만": 1, "재발정 확인": 6,
           "임신감정": 10, "분만사 이동": 3, "이유": 2}
DEFAULT_ON_TIME = 2


def _d(x) -> date:
    return rc._d(x)


def record(animal_id: str, task: str, work_date, operator: str = "",
           result: str = "완료", planned_date=None, note: str = "",
           path: str = LOG) -> dict:
    """작업 한 건 기록(추가만). 반환은 기록된 행."""
    if result not in RESULTS:
        raise ValueError(f"result 는 {RESULTS} 중 하나여야 한다: {result}")
    row = {"ts": datetime.now().isoformat(timespec="seconds"),
           "work_date": _d(work_date).isoformat(),
           "animal_id": str(animal_id), "task": task, "result": result,
           "operator": operator,
           "planned_date": _d(planned_date).isoformat() if planned_date else "",
           "note": note}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    pd.DataFrame([row], columns=COLS).to_csv(
        path, mode="a", header=new, index=False, encoding="utf-8")
    return row


def load(path: str = LOG) -> pd.DataFrame:
    if not os.path.exists(path):
        return pd.DataFrame(columns=COLS)
    d = pd.read_csv(path, dtype=str).fillna("")
    for c in COLS:
        if c not in d.columns:
            d[c] = ""
    d["work_date"] = pd.to_datetime(d["work_date"], errors="coerce").dt.date
    d["planned_date"] = pd.to_datetime(d["planned_date"],
                                       errors="coerce").dt.date
    return d[COLS]


def done_keys(log: pd.DataFrame) -> set:
    """완료로 처리된 (개체, 작업) 집합.

    취소 기록이 뒤에 오면 완료를 무효로 본다 — 추가만 하는 로그에서 정정을
    표현하는 방법이다.
    """
    if not len(log):
        return set()
    d = log.sort_values("ts")
    state = {}
    for r in d.itertuples(index=False):
        k = (str(r.animal_id), r.task)
        if r.result == "완료":
            state[k] = True
        elif r.result in ("취소", "미실시"):
            state[k] = False
    return {k for k, v in state.items() if v}


def apply_to_ledger(led: pd.DataFrame, log: pd.DataFrame) -> pd.DataFrame:
    """완료 기록이 있는 작업을 큐에서 뺀다.

    같은 개체의 '다음 작업'이 이미 끝난 것이면 그 행은 오늘 할 일이 아니다.
    긴급도를 0 으로 내려 조치 큐에서 자연스럽게 빠지게 하고, done 열로 표시한다.
    """
    keys = done_keys(log)
    if not keys or not len(led):
        d = led.copy()
        d["done"] = False
        return d
    d = led.copy()
    d["done"] = [(str(r["id"]), r["next_task"]) in keys
                 for r in d.to_dict("records")]
    d.loc[d["done"], "urgency"] = 0.0
    return d.sort_values("urgency", ascending=False).reset_index(drop=True)


def compliance(log: pd.DataFrame) -> pd.DataFrame:
    """예정일 대비 실제 수행일 — 작업별 정시/지연/조기.

    적기 준수는 수태율의 선행 지표다. 교배가 하루 밀리는 것과 임신감정이
    하루 밀리는 것은 무게가 다르므로 작업별 허용 폭(ON_TIME)을 따로 둔다.
    """
    d = log[(log["result"] == "완료") & log["planned_date"].notna()].copy()
    if not len(d):
        return pd.DataFrame()
    d["delay"] = [(w - p).days for w, p in zip(d["work_date"], d["planned_date"])]
    rows = []
    for task, g in d.groupby("task", sort=False):
        tol = ON_TIME.get(task, DEFAULT_ON_TIME)
        on = int(((g["delay"] >= -1) & (g["delay"] <= tol)).sum())
        rows.append({"task": task, "n": int(len(g)), "tol_days": tol,
                     "on_time": on, "late": int((g["delay"] > tol).sum()),
                     "early": int((g["delay"] < -1).sum()),
                     "on_time_rate": round(on / len(g), 3),
                     "mean_delay": round(float(g["delay"].mean()), 1),
                     "max_delay": int(g["delay"].max())})
    return pd.DataFrame(rows).sort_values("on_time_rate")


def summary(log: pd.DataFrame, days: int = 14, today=None) -> dict:
    """최근 N일 집계 — 일자별·작업별·작업자별."""
    if not len(log):
        return {"n": 0}
    t0 = _d(today) if today else date.today()
    lo = t0 - timedelta(days=days - 1)
    d = log[(log["work_date"] >= lo) & (log["work_date"] <= t0)]
    done = d[d["result"] == "완료"]
    daily = (done.groupby("work_date").size()
             .reindex([lo + timedelta(days=i) for i in range(days)],
                      fill_value=0))
    return {
        "n": int(len(done)), "n_all": int(len(d)),
        "n_missed": int((d["result"] == "미실시").sum()),
        "daily": [{"date": k.isoformat(), "n": int(v)}
                  for k, v in daily.items()],
        "by_task": done.groupby("task").size().sort_values(
            ascending=False).to_dict(),
        "by_operator": done.groupby("operator").size().sort_values(
            ascending=False).to_dict(),
        "period": [lo.isoformat(), t0.isoformat()],
    }


# --------------------------------------------------------------------------
def generate_demo(scheds: dict, today="2026-08-10", back: int = 21,
                  seed: int = 5, path: str | None = None) -> pd.DataFrame:
    """과거 작업을 합성해 로그를 채운다(파일에 쓰지 않고 DataFrame 으로).

    실제 농장에서는 앱이 '완료' 버튼으로 쌓는다. 여기서는 지난 3주치 예정 작업
    중 일부를 실제로 수행한 것처럼 만든다 — 일부는 늦게, 일부는 미실시.
    """
    rng = np.random.default_rng(seed)
    t0 = _d(today)
    ops = ["김철수", "이영희", "박민수"]
    rows = []
    for pid, tasks in scheds.items():
        for t in tasks:
            dd = (t["date"] - t0).days
            if not (-back <= dd < 0):
                continue
            u = rng.random()
            if u < 0.08:                       # 미실시
                res, delay = "미실시", 0
            elif u < 0.30:                     # 지연 수행
                res, delay = "완료", int(rng.integers(1, 5))
            else:
                res, delay = "완료", int(rng.integers(0, 2))
            w = t["date"] + timedelta(days=delay)
            if w > t0:
                continue
            rows.append({
                "ts": datetime.combine(w, datetime.min.time()).isoformat(
                    timespec="seconds"),
                "work_date": w, "animal_id": str(pid), "task": t["task"],
                "result": res, "operator": ops[int(rng.integers(len(ops)))],
                "planned_date": t["date"], "note": ""})
    d = pd.DataFrame(rows, columns=COLS).sort_values("ts").reset_index(drop=True)
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        d.to_csv(path, index=False, encoding="utf-8")
    return d


def main() -> int:
    import breeding_ledger as bl
    today = sys.argv[1] if len(sys.argv) > 1 else "2026-08-10"
    farm, herd, scheds, scores = bl.build_demo(today)
    led = bl.ledger(farm, herd, scheds, scores, today=today)
    log = generate_demo(scheds, today=today)

    print(f"=== 작업 로그 (최근 3주 합성) · {len(log):,}건 ===")
    s = summary(log, days=14, today=today)
    print(f"  기간 {s['period'][0]} ~ {s['period'][1]} · 완료 {s['n']}건 · "
          f"미실시 {s['n_missed']}건")
    print("  작업별: " + " · ".join(f"{k} {v}" for k, v in
                                 list(s["by_task"].items())[:6]))
    print("  작업자별: " + " · ".join(f"{k} {v}" for k, v in
                                  s["by_operator"].items()))
    mx = max(x["n"] for x in s["daily"]) or 1
    print("  일자별:")
    for x in s["daily"]:
        print(f"    {x['date']} {'█' * int(24 * x['n'] / mx)} {x['n']}")

    print("\n=== 적기 준수 (예정일 대비) ===")
    c = compliance(log)
    print(f"  {'작업':<10} {'건수':>4} {'허용':>4} {'정시':>4} {'지연':>4} "
          f"{'준수율':>7} {'평균지연':>7}")
    for r in c.itertuples(index=False):
        print(f"  {r.task:<10} {r.n:>4} {r.tol_days:>3}일 {r.on_time:>4} "
              f"{r.late:>4} {r.on_time_rate:>7.0%} {r.mean_delay:>6.1f}일")
    print("  → 교배는 허용 폭이 0일이다. 반나절만 밀려도 적기를 놓치기 때문이며,"
          "\n    이 준수율이 곧 수태율의 선행 지표다.")

    print("\n=== 로그가 조치 큐를 정정한다 ===")
    # 조치 대상 정의는 breeding_ledger 한 곳을 쓴다(도면·큐와 같은 숫자)
    before = sum(1 for r in led.to_dict("records") if bl.is_actionable(r))
    led2 = apply_to_ledger(led, log)
    after = sum(1 for r in led2.to_dict("records") if bl.is_actionable(r))
    print(f"  조치 대상 {before}두 → {after}두 "
          f"(완료 기록으로 {before - after}두 제외 · "
          f"로그상 완료 {int(led2['done'].sum())}두)")
    for g in bl.barn_queue(led2)[:4]:
        print(f"    {g['barn']} {g['n']}건")
    print("  ※ 로그가 없으면 이미 끝낸 작업이 큐에 계속 남는다. 사건 진행으로"
          "\n    역추론하는 방식은 '오늘 아침에 했다'를 잡지 못한다.")

    print("\n※ 합성 로그 시연이다. 실제로는 앱의 '완료' 버튼이 같은 스키마로 쌓는다."
          "\n※ 로그는 추가만 한다 — 정정은 취소 기록을 덧붙이는 방식이다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
