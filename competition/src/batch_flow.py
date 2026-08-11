"""돈군흐름(배칭) — 개체 단위 연속 흐름이 아니라 **배치 단위**로 관리한다.

지금까지 이 프로젝트는 모돈을 하나씩 따로 굴렸다. 이유일이 제각각이면 교배도
분만도 흩어지고, 그러면 **올인/올아웃(AIAO)이 성립하지 않는다** — 방을 비울
틈이 없어 세척·건조를 못 하고 병원체가 배치를 넘어 이어진다.

배치(batch)란 한 무리의 모돈이 같이 교배되고 같이 분만하고 같이 이유되어
다음 사이클로 함께 넘어가는 것이다. 배치는 **이유 직후 시작**하며, 이유 후
7일 이내에 교배해야 분만일이 모이고 이유일령이 고르게 된다.

핵심 계산 세 가지:

  1) **배치 수** = 번식주기(150일) ÷ 배치 간격.
     3주 간격이면 150/21 ≈ 7배치, 5주 간격이면 ≈ 4배치.
  2) **배치당 두수** = 모돈 규모 ÷ 배치 수. 이 숫자가 곧 한 번에 분만하는
     두수이고, 분만사 한 방의 크기를 정한다.
  3) **AIAO 방 수** = 분만사 점유기간 ÷ 배치 간격.
     점유 = 분만 전 이동 7일 + 포유 28일 + **세척·건조 7일**. 세척 기간을
     빼먹으면 방이 모자라 결국 올인/올아웃이 무너진다 — 배칭의 목적 자체가
     사라지므로 여기서는 반드시 포함한다.

간격을 좁히면(주간) 방이 많이 필요한 대신 배치가 작아 인력이 고르게 퍼지고,
넓히면(5주) 방은 적지만 한 번에 몰려 분만 감독이 빡세다. 정답은 없고 농장의
방 수·인력에 달렸다 — 그래서 비교표를 낸다.

    python competition/src/batch_flow.py            # 간격별 비교 + 배치 배정
    python competition/src/batch_flow.py 21         # 3주 간격으로
"""
from __future__ import annotations

import os
import sys
from datetime import date, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import breeding_timing as bt  # noqa: E402
import repro_calendar as rc  # noqa: E402

GESTATION = bt.GESTATION          # 115
LACTATION = bt.LACTATION          # 28
CYCLE = bt.CYCLE_DAYS             # 150 = 115 + 28 + 7

MOVE_IN = rc.MOVE_BEFORE_FARROW   # 분만 전 분만사 이동(7일)
WASHDOWN = 7                      # 세척·건조·소독 — AIAO 의 존재 이유
FARROW_OCCUPY = MOVE_IN + LACTATION + WASHDOWN      # 분만사 점유 42일

# 이유 후 이 안에 교배해야 배치가 유지된다(그림의 '7일 이내')
BATCH_WINDOW = 7

# 분만 지연·세척 지연에 대비한 최소 여유(일). 딱 맞게 지으면 첫 사고에서 끝난다.
BUFFER = 3

# 현대 양돈장이 쓰는 배치 간격(일). 주간 2간격은 3~4일씩 두 번이다.
BATCH_INTERVALS = {
    "주간 2간격": 3.5, "주간": 7, "10일": 10, "2주": 14,
    "3주": 21, "4주": 28, "5주": 35,
}


def plan(n_sows: int, interval_days: float, farrow_rate: float = 0.88) -> dict:
    """배치 간격 → 배치 수·배치당 두수·필요 방 수.

    farrow_rate: 교배 대비 실제 분만 비율(수태 실패·유산 반영). 분만사 방
    크기는 **교배 두수가 아니라 분만 두수**로 잡아야 빈 분만틀이 줄어든다.
    """
    iv = float(interval_days)
    n_batch = CYCLE / iv
    per_batch = n_sows / n_batch
    farrow_per_batch = per_batch * farrow_rate
    rooms = int(np.ceil(FARROW_OCCUPY / iv))
    crates = int(np.ceil(farrow_per_batch)) * rooms
    # 방 여유 = 방 수 × 간격 − 점유기간. 0 이면 다음 배치가 들어오는 날
    # 세척이 끝나는 것이라 하루만 밀려도 AIAO 가 깨진다. 방 수만 보면
    # '충분하다'로 읽히므로 여유를 따로 낸다.
    slack = rooms * iv - FARROW_OCCUPY
    # 실무 권장: 여유를 최소 BUFFER 일 확보한 방 수. 분만이 며칠 늦어지거나
    # 세척이 밀리는 일은 늘 있으므로, 딱 맞게 지으면 첫 사고에서 AIAO 가
    # 무너지고 다시는 회복되지 않는다(배치가 한 번 흐트러지면 되돌리기 어렵다).
    rooms_safe = int(np.ceil((FARROW_OCCUPY + BUFFER) / iv))
    # 주간 교배 두수(평준화 관점) — 간격이 넓으면 같은 두수가 한 날에 몰린다
    per_week = n_sows / (CYCLE / 7.0)
    return {
        "interval_days": iv,
        "n_batches": round(n_batch, 1),
        "sows_per_batch": round(per_batch, 1),
        "farrow_per_batch": round(farrow_per_batch, 1),
        "farrow_rooms": rooms,
        "crates_needed": crates,
        "crates_per_room": int(np.ceil(farrow_per_batch)),
        "slack_days": round(slack, 1),
        "rooms_recommended": rooms_safe,
        "crates_recommended": int(np.ceil(farrow_per_batch)) * rooms_safe,
        "services_per_event": round(per_batch, 1),
        "services_per_week_avg": round(per_week, 1),
        "peak_ratio": round(per_batch / per_week, 1) if per_week else None,
    }


def compare(n_sows: int, farrow_rate: float = 0.88) -> pd.DataFrame:
    """간격별 비교표 — 방 수와 작업 집중도의 맞바꿈을 한눈에."""
    rows = []
    for name, iv in BATCH_INTERVALS.items():
        p = plan(n_sows, iv, farrow_rate)
        rows.append({"name": name, "interval": iv,
                     "n_batches": p["n_batches"],
                     "sows_per_batch": p["sows_per_batch"],
                     "farrow_per_batch": p["farrow_per_batch"],
                     "farrow_rooms": p["farrow_rooms"],
                     "crates": p["crates_needed"],
                     "peak_ratio": p["peak_ratio"],
                     "slack_days": p["slack_days"],
                     "rooms_recommended": p["rooms_recommended"]})
    return pd.DataFrame(rows)


def batch_of(weaning, anchor, interval_days: float) -> int:
    """이유일 → 배치 번호. anchor 는 0번 배치의 기준 이유일."""
    d = (rc._d(weaning) - rc._d(anchor)).days
    return int(np.floor(d / float(interval_days)))


def batch_dates(anchor, batch_no: int, interval_days: float) -> dict:
    """배치의 표준 일정 — 이유 기준으로 다음 주기까지."""
    w = rc._d(anchor) + timedelta(days=round(batch_no * float(interval_days)))
    svc = w + timedelta(days=rc.WEI_BY_PARITY["sow"])
    far = svc + timedelta(days=GESTATION)
    return {"batch": batch_no, "wean": w,
            "service_from": w, "service_to": w + timedelta(days=BATCH_WINDOW),
            "service": svc, "move_in": far - timedelta(days=MOVE_IN),
            "farrow": far, "next_wean": far + timedelta(days=LACTATION),
            "room_free": far + timedelta(days=LACTATION + WASHDOWN)}


def assign(herd: pd.DataFrame, interval_days: float, anchor=None) -> pd.DataFrame:
    """모돈군을 배치에 배정하고 **배치 이탈**을 표시한다.

    이탈: 이유 후 BATCH_WINDOW 안에 교배하지 못한 개체. 이들이 많으면 분만이
    흩어져 올인/올아웃이 깨진다. 배치 관리의 성패는 이 비율에 달렸다.
    """
    d = herd[herd["weaning_date"].notna()].copy()
    if not len(d):
        return pd.DataFrame()
    a = rc._d(anchor) if anchor else min(d["weaning_date"])
    d["batch"] = [batch_of(w, a, interval_days) for w in d["weaning_date"]]
    d["batch_wean"] = [rc._d(a) + timedelta(days=round(b * interval_days))
                       for b in d["batch"]]
    # 실제 교배가 배치 창 안에 들어왔는가
    lag, inb = [], []
    for r in d.itertuples(index=False):
        # service_date 는 **직전 주기의 교배**일 수 있다. 공태돈은 이유 후 아직
        # 교배하지 않았으므로 그대로 빼면 -143일 같은 값이 나온다. 이유일보다
        # 뒤인 교배만 이번 배치의 교배로 인정하고, 나머지는 '미교배'다.
        if (isinstance(r.service_date, date) and isinstance(r.weaning_date, date)
                and r.service_date > r.weaning_date):
            k = (r.service_date - r.weaning_date).days
            lag.append(k)
            inb.append(k <= BATCH_WINDOW)
        else:
            lag.append(np.nan)
            inb.append(False)
    d["wei_actual"] = lag
    d["in_batch"] = inb
    return d


def integrity(assigned: pd.DataFrame) -> dict:
    """배치 유지율 — 창 안에 교배된 비율과 이탈 사유."""
    if not len(assigned):
        return {"n": 0}
    served = assigned[assigned["wei_actual"].notna()]
    n = int(len(served))
    ok = int(served["in_batch"].sum())
    late = int((served["wei_actual"] > BATCH_WINDOW).sum())
    return {"n": n, "in_batch": ok,
            "rate": round(ok / n, 3) if n else None,
            "late": late, "unserved": int(len(assigned) - n),
            "mean_wei": round(float(served["wei_actual"].mean()), 1) if n else None,
            "n_batches": int(assigned["batch"].nunique())}


def room_schedule(anchor, interval_days: float, n_batches: int = 6) -> pd.DataFrame:
    """분만사 방 점유표 — 배치가 언제 들어오고 언제 비는가.

    AIAO 가 성립하려면 다음 배치가 들어오기 전에 **세척·건조가 끝나야** 한다.
    방이 모자라면 여기서 겹침으로 드러난다.
    """
    rows = []
    rooms = int(np.ceil(FARROW_OCCUPY / float(interval_days)))
    for b in range(n_batches):
        x = batch_dates(anchor, b, interval_days)
        rows.append({"batch": b, "room": b % rooms,
                     "move_in": x["move_in"], "farrow": x["farrow"],
                     "wean": x["next_wean"], "free": x["room_free"]})
    d = pd.DataFrame(rows)
    # 같은 방을 쓰는 연속 배치가 겹치는지
    conf = []
    for room, g in d.groupby("room"):
        g = g.sort_values("move_in")
        prev_free = None
        for r in g.itertuples(index=False):
            conf.append(bool(prev_free is not None and r.move_in < prev_free))
            prev_free = r.free
    d = d.sort_values(["room", "move_in"]).reset_index(drop=True)
    d["overlap"] = conf
    return d.sort_values("batch").reset_index(drop=True)


def generate_demo(n_sows: int = 300, interval_days: float = 21.0,
                  today="2026-08-10", adherence: float = 0.82,
                  seed: int = 9) -> pd.DataFrame:
    """배치 배정 시연용 모돈군 — 이유 후 **재교배까지** 있는 기록.

    herd_board 의 생성기는 이유 이후 재교배를 만들지 않아 유지율이 항상 0%
    으로 나온다. 배치 유지율은 '이유 후 며칠에 교배했나'의 분포가 있어야
    의미가 있으므로 여기서 따로 만든다.

    adherence: 이유 후 창(7일) 안에 교배한 비율. 나머지는 늦거나 미교배.
    """
    rng = np.random.default_rng(seed)
    t0 = rc._d(today)
    n_batch = max(1, int(round(CYCLE / interval_days)))
    rows = []
    for i in range(n_sows):
        b = i % n_batch
        # 배치 기준 이유일 — 과거로 흩뿌린다
        wean = t0 - timedelta(days=int(b * interval_days) + 7)
        # 같은 배치라도 이유일이 며칠 흔들린다(분만일 편차)
        wean += timedelta(days=int(rng.integers(-1, 2)))
        u = rng.random()
        if u < adherence:
            wei = int(rng.integers(3, BATCH_WINDOW + 1))
            svc = wean + timedelta(days=wei)
        elif u < adherence + 0.12:
            svc = wean + timedelta(days=int(rng.integers(8, 26)))  # 이탈(지연)
        else:
            svc = None                                            # 미교배
        rows.append({"id": f"{3000 + i}", "parity": int(rng.integers(1, 8)),
                     "weaning_date": wean,
                     "service_date": svc if svc and svc <= t0 else None,
                     "farrow_date": None, "stage": "공태"})
    return pd.DataFrame(rows)


def main() -> int:
    import herd_board as hb  # noqa: F401
    iv = float(sys.argv[1]) if len(sys.argv) > 1 else 21.0
    today = "2026-08-10"

    print("=== 배치 간격 비교 (모돈 300두, 분만율 88%) ===")
    print("  간격을 좁히면 방이 많이 필요한 대신 일이 고르게 퍼지고,")
    print("  넓히면 방은 적지만 한 번에 몰린다. 정답은 농장의 방·인력에 달렸다.")
    c = compare(300)
    print(f"  {'간격':<9} {'배치수':>5} {'배치당':>6} {'분만':>6} "
          f"{'최소방':>5} {'여유':>5} {'권장방':>5} {'분만틀':>6} {'집중도':>6}")
    for _i, r in c.iterrows():
        warn = " ⚠" if r["slack_days"] < BUFFER else ""
        print(f"  {r['name']:<9} {r['n_batches']:>5.1f} "
              f"{r['sows_per_batch']:>6.1f} {r['farrow_per_batch']:>6.1f} "
              f"{r['farrow_rooms']:>5} {r['slack_days']:>4.0f}일 "
              f"{r['rooms_recommended']:>5} {r['crates']:>6} "
              f"{r['peak_ratio']:>5.1f}×{warn}")
    print(f"  ⚠ = 여유가 {BUFFER}일 미만. 최소 방 수는 세척이 정확히 제 날에"
          "\n    끝나야만 성립하므로, 권장 방 수로 지어야 한 번의 지연을 견딘다.")

    print(f"\n=== {iv:.0f}일 간격 상세 ===")
    p = plan(300, iv)
    print(f"  배치 {p['n_batches']}개 · 배치당 모돈 {p['sows_per_batch']}두 → "
          f"분만 {p['farrow_per_batch']}두")
    print(f"  분만사 {p['farrow_rooms']}방 × {p['crates_per_room']}틀 "
          f"= 분만틀 {p['crates_needed']}개")
    print(f"  점유 {FARROW_OCCUPY}일 = 이동 {MOVE_IN} + 포유 {LACTATION} + "
          f"세척 {WASHDOWN} · 방 여유 {p['slack_days']:.0f}일")
    if p["slack_days"] < BUFFER:
        print(f"  ⚠ 여유 부족 — 권장 {p['rooms_recommended']}방 "
              f"(분만틀 {p['crates_recommended']}개). 딱 맞게 지으면 분만이"
              "\n    며칠 늦거나 세척이 밀리는 순간 AIAO 가 무너지고, 배치가 한 번"
              "\n    흐트러지면 되돌리기 어렵다.")
    print(f"  1회 교배 {p['services_per_event']}두 (주 평균 "
          f"{p['services_per_week_avg']}두의 {p['peak_ratio']}배)")

    print(f"\n=== 분만사 방 점유표 (배치 6개) ===")
    rs = room_schedule("2026-08-03", iv)
    print(f"  {'배치':>3} {'방':>3} {'이동':<11} {'분만':<11} {'이유':<11} "
          f"{'비움':<11} 겹침")
    for r in rs.itertuples(index=False):
        print(f"  {r.batch:>3} {r.room:>3} {r.move_in:%m-%d} → {r.farrow:%m-%d} "
              f"  {r.wean:%m-%d}   {r.free:%m-%d}   "
              f"{'⚠ 겹침' if r.overlap else 'OK'}")
    if not rs["overlap"].any():
        print("  → 겹침 없음. 다음 배치가 들어오기 전에 세척이 끝난다(AIAO 성립).")

    print("\n=== 모돈군을 배치에 배정 (300두) ===")
    herd = generate_demo(300, iv, today=today)
    a = assign(herd, iv)
    if len(a):
        g = integrity(a)
        print(f"  이유 기록 있는 모돈 {len(a)}두 → 배치 {g['n_batches']}개")
        print(f"  교배 완료 {g['n']}두 중 창(이유+{BATCH_WINDOW}일) 안 "
              f"{g['in_batch']}두 = 유지율 {g['rate']:.0%}")
        print(f"  이탈 {g['late']}두 · 미교배 {g['unserved']}두 · "
              f"평균 WEI {g['mean_wei']}일")
        print(f"  {'배치':>4} {'두수':>4} {'기준 이유일':<12} {'창 안':>6} {'유지율':>6}")
        for b, sub in a.sort_values("batch").groupby("batch"):
            ok = int(sub["in_batch"].sum())
            print(f"  {b:>4} {len(sub):>4} {sub['batch_wean'].iloc[0]}   "
                  f"{ok:>3}/{len(sub):<3} {ok / len(sub):>6.0%}")
        print("  ※ 이탈이 많으면 분만이 흩어져 올인/올아웃이 깨진다. 배치 관리의"
              "\n    성패는 '이유 후 7일 안에 교배' 를 지키는 비율에 달렸다.")
    print("\n※ 합성 데이터다. 실제 배치 설계는 농장의 분만사 방 수가 먼저 정해져"
          "\n  있는 경우가 많아, 그 제약에서 역산해 간격을 고르게 된다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
