"""모돈군 현황판 — 주차별 임신돈·포유모돈, 산차 구성, 도태·후보돈 전입 계획.

캘린더(repro_calendar)가 **개체 한 두의 일정**을 다룬다면, 이 모듈은 **군 전체의
구성과 흐름**을 본다. 번식 성적이 무너지는 방식은 대개 개체 사고가 아니라 구조다:

  · 산차 구성이 늙으면(6산 이상 과다) 산자수·수태율이 같이 떨어진다.
  · 도태를 미루면 후보돈 전입이 밀리고, 밀리면 다시 늙은 모돈을 못 뺀다.
  · 주간 교배 두수가 목표에 못 미치면 **17주 뒤 분만이 비고**, 그 빈 자리는
    되돌릴 수 없다(임신 115일은 단축 불가).

그래서 현황판의 핵심은 "지금 몇 두인가"가 아니라 **"몇 주 뒤에 무엇이 빈다"** 다.

  1) weekly_board()      주차별 교배·분만·이유 예정 + 임신돈 재고 (17주 파이프라인)
  2) parity_profile()    산차별 두수 vs 목표 분포 — 편차가 도태·전입의 근거
  3) cull_candidates()   도태 후보(노령·연속재발정·저산자·장기공태) + 사유
  4) gilt_intake_plan()  월별 후보돈 전입 필요 두수(순치·초교배 일령 역산)
  5) service_target()    주간 교배 목표 두수와 달성률

    python competition/src/herd_board.py            # 시연(합성 300두)
"""
from __future__ import annotations

import os
import sys
from datetime import date, datetime, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import breeding_timing as bt  # noqa: E402
import repro_calendar as rc  # noqa: E402

GESTATION = bt.GESTATION      # 115
LACTATION = bt.LACTATION      # 28

# 목표 산차 구성(%) — 3~5산이 성적 정점이므로 그 구간을 두껍게 유지한다.
# 1산이 과다하면 산자수가 낮고, 6산 이상이 과다하면 수태율·활력이 떨어진다.
TARGET_PARITY_MIX = {1: 0.20, 2: 0.18, 3: 0.17, 4: 0.15, 5: 0.12, 6: 0.09, 7: 0.09}

REPLACEMENT_RATE = 0.40       # 연간 갱신율 목표(국내 권장 35~45%)
GILT_ACCLIMATION_D = 60       # 전입 후 순치·검역 기간
INTAKE_CAPACITY_FACTOR = 1.8  # 월 전입 상한 = 기본치 × 이 값(격리사·인력 제약)
CULL_PARITY = 7               # 이 산차 이상은 도태 검토
MAX_RETURNS = 2               # 연속 재발정 허용 횟수
LOW_LITTER = 9.0              # 총산자수 저조 기준(두)
MAX_NPD = 30                  # 비생산일수 상한(일)

STAGES = ["후보", "공태", "교배", "임신", "포유"]


def _d(x) -> date:
    return rc._d(x)


# --------------------------------------------------------------------------
def build_herd(records, today=None) -> pd.DataFrame:
    """개체 기록 → 현재 단계·주차·예정일이 붙은 현황 테이블.

    records: [{id, parity, service_date?, farrow_date?, weaning_date?,
               returns?, last_litter?, entry_date?}]

    단계는 **가장 최근에 지난 사건**으로 정한다. 사건 종류로 분기하면(교배 기록이
    있으니 임신) 이미 이유까지 마친 모돈이 계속 '임신'으로 남는다 — 실제로 그
    버그가 있었고, 공태돈이 한 두도 잡히지 않았다. 공태는 NPD 의 원천이라 놓치면
    현황판의 존재 이유가 없어진다.
    """
    t0 = _d(today) if today else date.today()
    rows = []
    for r in records:
        parity = int(r.get("parity", 0))
        svc = _d(r["service_date"]) if r.get("service_date") else None
        far = _d(r["farrow_date"]) if r.get("farrow_date") else None
        wea = _d(r["weaning_date"]) if r.get("weaning_date") else None

        past = [(d, k) for d, k in ((svc, "svc"), (far, "far"), (wea, "wea"))
                if d is not None and d <= t0]
        last = max(past)[1] if past else None

        stage, week, due, dday = "후보", None, None, None
        if last == "wea":
            stage = "공태"
            due = wea + timedelta(days=round(rc.expected_wei("sow")))
            dday = (due - t0).days
        elif last == "far":
            stage = "포유"
            week = (t0 - far).days // 7 + 1
            due = far + timedelta(days=LACTATION)
            dday = (due - t0).days
        elif last == "svc":
            exp_far = far or (svc + timedelta(days=GESTATION))
            gd = (t0 - svc).days
            stage = "교배" if gd < 21 else "임신"
            week = gd // 7 + 1
            due, dday = exp_far, (exp_far - t0).days
        elif parity > 0:
            stage = "공태"

        npd = 0
        if stage == "공태" and wea:
            npd = (t0 - wea).days
        rows.append({
            "id": r["id"], "parity": parity, "stage": stage,
            "week": week, "due_date": due, "d_day": dday,
            "service_date": svc, "farrow_date": far, "weaning_date": wea,
            "returns": int(r.get("returns", 0)),
            "last_litter": float(r.get("last_litter", np.nan)),
            "npd": npd,
        })
    df = pd.DataFrame(rows)
    df.attrs["today"] = t0
    return df


def weekly_board(herd: pd.DataFrame, today=None, weeks: int = 17,
                 conception_rate: float = 0.85) -> pd.DataFrame:
    """주차별 파이프라인 — 이번 주부터 N주간 분만·이유 예정과 임신돈 재고.

    17주(≈119일)를 보는 이유: 오늘 교배한 모돈이 분만하기까지가 그 길이다.
    즉 **17주 표의 마지막 칸이 비어 있으면 지금 교배가 부족하다는 뜻**이고,
    그 빈칸은 임신 기간을 줄일 수 없으므로 나중에 메울 수 없다.

    주의: 재고(preg_stock)가 뒤로 갈수록 줄어드는 것은 정상이다 — **아직 하지
    않은 교배**는 반영될 수 없기 때문이다. 판단 기준은 재고가 아니라 목표 대비
    분만 두수(shortfall)다.
    """
    t0 = _d(today) if today else herd.attrs.get("today", date.today())
    mon = t0 - timedelta(days=t0.weekday())          # 이번 주 월요일
    target = service_target(herd, conception_rate, today=t0)["farrow_target_week"]
    preg = herd[(herd["stage"].isin(("교배", "임신"))) & (herd["due_date"].notna())]
    lact = herd[herd["stage"] == "포유"]
    rows = []
    for w in range(weeks):
        s = mon + timedelta(days=7 * w)
        e = s + timedelta(days=6)
        farrow_n = int(((preg["due_date"] >= s) & (preg["due_date"] <= e)).sum())
        wean_n = int(((lact["due_date"] >= s) & (lact["due_date"] <= e)).sum())
        # 그 주 시점에 임신 상태로 남아 있는 두수(분만 예정이 그 주보다 뒤)
        # 교배 후 115일이 지나야 분만이므로, 오늘 이후 교배분이 채우는 구간은
        # W16 이후다. 그 앞 구간의 미달은 **이미 확정된 손실**이다.
        rows.append({"week": w, "start": s, "end": e,
                     "farrow": farrow_n, "wean": wean_n,
                     "target": target,
                     "shortfall": round(target - farrow_n, 1),
                     # 그 주의 분만은 [s-115, e-115] 사이 교배에서 나온다.
                     # **주의 끝**까지 역산해도 오늘 이전이어야 완전히 확정이다
                     # (주 시작으로 판정하면 아직 메울 수 있는 주까지 손실로 샌다).
                     "locked": e <= t0 + timedelta(days=GESTATION),
                     "preg_stock": int((preg["due_date"] > e).sum()),
                     "lact_stock": int((lact["due_date"] > e).sum())})
    return pd.DataFrame(rows)


def parity_profile(herd: pd.DataFrame) -> pd.DataFrame:
    """산차별 실제 두수 vs 목표 구성. gap>0 이면 과다(도태 우선순위)."""
    prod = herd[herd["parity"] > 0]
    n = len(prod)
    rows = []
    for p, share in TARGET_PARITY_MIX.items():
        actual = int((prod["parity"] >= p).sum() if p == max(TARGET_PARITY_MIX)
                     else (prod["parity"] == p).sum())
        target = share * n
        rows.append({"parity": p if p < max(TARGET_PARITY_MIX) else f"{p}+",
                     "n": actual, "share": round(actual / n, 3) if n else 0.0,
                     "target_share": share, "target_n": round(target, 1),
                     "gap": round(actual - target, 1)})
    return pd.DataFrame(rows)


def cull_candidates(herd: pd.DataFrame) -> pd.DataFrame:
    """도태 후보 + 사유. 사유가 여러 개면 점수가 쌓인다(높을수록 우선)."""
    rows = []
    for r in herd.itertuples(index=False):
        reasons, score = [], 0
        if r.parity >= CULL_PARITY:
            reasons.append(f"{r.parity}산 노령")
            score += 30 + 5 * (r.parity - CULL_PARITY)
        if r.returns >= MAX_RETURNS:
            reasons.append(f"재발정 {r.returns}회")
            score += 35 * r.returns
        if not np.isnan(r.last_litter) and r.last_litter < LOW_LITTER and r.parity >= 2:
            reasons.append(f"총산자 {r.last_litter:.0f}두")
            score += 25
        if r.npd > MAX_NPD:
            reasons.append(f"공태 {r.npd}일")
            score += 20 + (r.npd - MAX_NPD)
        if reasons:
            rows.append({"id": r.id, "parity": r.parity, "stage": r.stage,
                         "score": score, "reason": " · ".join(reasons)})
    df = pd.DataFrame(rows)
    return (df.sort_values("score", ascending=False).reset_index(drop=True)
            if len(df) else df)


def gilt_intake_plan(herd: pd.DataFrame, months: int = 6, today=None,
                     replacement_rate: float = REPLACEMENT_RATE,
                     capacity_factor: float = INTAKE_CAPACITY_FACTOR) -> pd.DataFrame:
    """월별 후보돈 전입 계획.

    필요 두수 = 모돈 규모 × 갱신율 ÷ 12. 여기에 **도태 대기 물량**을 얹되,
    한 달에 소화할 수 있는 양에는 상한이 있다(capacity_factor × 기본치). 상한을
    무시하면 "도태 후보 79두 → 두 달에 78두 전입" 처럼 군의 28%를 두 달 만에
    갈아치우는 계획이 나온다 — 격리사 용량·순치 인력·자금 어디로도 불가능하다.

    전입은 순치 60일이 걸리므로 '교배에 쓸 시점'에서 역산해야 한다 — 이번 달
    전입분이 실제 교배 가능한 건 두 달 뒤다.
    """
    t0 = _d(today) if today else herd.attrs.get("today", date.today())
    n_sows = int((herd["parity"] > 0).sum())
    base = n_sows * replacement_rate / 12.0
    cand = cull_candidates(herd)
    pending = len(cand)
    on_hand = int((herd["parity"] == 0).sum())
    cap = base * capacity_factor
    backlog = max(0.0, pending - on_hand)
    rows = []
    for m in range(months):
        month_start = (t0.replace(day=1) + timedelta(days=32 * m)).replace(day=1)
        extra = min(backlog, max(0.0, cap - base))
        backlog -= extra
        rows.append({"month": month_start.strftime("%Y-%m"),
                     "need": int(round(base + extra)),
                     "backlog_left": int(round(backlog)),
                     "usable_from": (month_start
                                     + timedelta(days=GILT_ACCLIMATION_D)
                                     ).strftime("%Y-%m-%d")})
    df = pd.DataFrame(rows)
    per_month_extra = max(0.0, cap - base)
    clear = (int(np.ceil(max(0.0, pending - on_hand) / per_month_extra))
             if per_month_extra > 0 else None)
    df.attrs.update({"n_sows": n_sows, "cull_pending": pending,
                     "gilts_on_hand": on_hand, "monthly_base": round(base, 1),
                     "monthly_cap": round(cap, 1),
                     "annual_capacity": int(round(n_sows * replacement_rate)),
                     "months_to_clear": clear, "backlog_left": int(round(backlog))})
    return df


def service_target(herd: pd.DataFrame, conception_rate: float = 0.85,
                   today=None, lookback_days: int = 7) -> dict:
    """주간 교배 목표 두수와 최근 실적.

    목표 분만복수/주 = 모돈수 × 회전율 ÷ 52. 수태율로 나누면 필요 교배두수다
    (실패분을 다시 교배해야 하므로 항상 분만 목표보다 많다).
    """
    t0 = _d(today) if today else herd.attrs.get("today", date.today())
    n_sows = int((herd["parity"] > 0).sum())
    turn = bt.turnover(conception_rate)
    farrow_wk = n_sows * turn / 52.0
    target = farrow_wk / max(0.05, conception_rate)
    svc = herd["service_date"].dropna()
    recent = int(((svc > t0 - timedelta(days=lookback_days)) & (svc <= t0)).sum())
    return {"n_sows": n_sows, "turnover": turn,
            "farrow_target_week": round(farrow_wk, 1),
            "service_target_week": round(target, 1),
            "service_actual_week": recent,
            "achievement": round(recent / target, 2) if target else None}


def stage_counts(herd: pd.DataFrame) -> dict:
    c = herd["stage"].value_counts().to_dict()
    return {s: int(c.get(s, 0)) for s in STAGES}


# --------------------------------------------------------------------------
def generate_demo(n: int = 300, today="2026-08-10", seed: int = 7) -> list:
    """합성 모돈군 — 주기의 각 단계에 고르게 흩어진 300두."""
    rng = np.random.default_rng(seed)
    t0 = _d(today)
    recs = []
    cycle = GESTATION + LACTATION + 7
    for i in range(n):
        pid = f"{2000 + i}"
        if rng.random() < 0.09:                       # 후보돈 재고
            recs.append({"id": pid, "parity": 0,
                         "entry_date": t0 - timedelta(days=int(rng.integers(5, 90)))})
            continue
        parity = int(np.clip(rng.geometric(0.22), 1, 10))
        # 주기 안의 임의 위치
        pos = int(rng.integers(0, cycle))
        svc = t0 - timedelta(days=pos)
        far = svc + timedelta(days=GESTATION)
        rec = {"id": pid, "parity": parity,
               "returns": int(rng.random() < 0.10) + int(rng.random() < 0.03),
               "last_litter": float(np.clip(rng.normal(11.5, 2.2), 4, 18))}
        if pos < GESTATION:
            rec["service_date"] = svc
        elif pos < GESTATION + LACTATION:
            rec.update({"service_date": svc, "farrow_date": far})
        else:
            rec.update({"service_date": svc, "farrow_date": far,
                        "weaning_date": far + timedelta(days=LACTATION)})
        recs.append(rec)
    return recs


def main() -> int:
    today = sys.argv[1] if len(sys.argv) > 1 else "2026-08-10"
    herd = build_herd(generate_demo(today=today), today=today)
    sc = stage_counts(herd)
    print(f"=== 모돈군 현황 ({today}) · 총 {len(herd)}두 ===")
    print("  " + " · ".join(f"{k} {v}두" for k, v in sc.items()))

    st = service_target(herd, today=today)
    print(f"\n=== 주간 교배 목표 ===")
    print(f"  모돈 {st['n_sows']}두 · 회전율 {st['turnover']}회/년")
    print(f"  주간 분만 목표 {st['farrow_target_week']}복 → "
          f"교배 목표 {st['service_target_week']}두 "
          f"(최근 7일 실적 {st['service_actual_week']}두, "
          f"달성률 {st['achievement']:.0%})")

    print("\n=== 주차별 파이프라인 (17주 = 오늘 교배분의 분만까지) ===")
    wb = weekly_board(herd, today=today)
    print(f"  {'주':>3} {'기간':<12} {'분만':>4} {'목표':>5} {'이유':>4} "
          f"{'임신재고':>7}")
    for r in wb.itertuples(index=False):
        flag = ""
        if r.shortfall > r.target * 0.3:
            flag = "  ← 분만 미달(확정 손실)" if r.locked else "  ← 교배로 메울 구간"
        print(f"  W{r.week:<2} {r.start:%m/%d}~{r.end:%m/%d} "
              f"{r.farrow:>4} {r.target:>5.1f} {r.wean:>4} {r.preg_stock:>7}{flag}")
    lost = wb[(wb["locked"]) & (wb["shortfall"] > 0)]["shortfall"].sum()
    print(f"  → 확정 구간 누적 미달 {lost:.0f}복 "
          f"(임신 115일은 단축 불가 — 지금 교배해도 메울 수 없다)")

    print("\n=== 산차 구성 (목표 대비) ===")
    pp = parity_profile(herd)
    print(f"  {'산차':>4} {'두수':>5} {'비율':>7} {'목표':>7} {'편차':>7}")
    for r in pp.itertuples(index=False):
        bar = "＋" if r.gap > 3 else ("－" if r.gap < -3 else " ")
        print(f"  {str(r.parity):>4} {r.n:>5} {r.share:>7.1%} "
              f"{r.target_share:>7.1%} {r.gap:>+7.1f} {bar}")

    cc = cull_candidates(herd)
    print(f"\n=== 도태 후보 {len(cc)}두 (상위 8) ===")
    for r in cc.head(8).itertuples(index=False):
        print(f"  {r.id} {r.parity}산 {r.stage:<3} 점수{r.score:>4}  {r.reason}")

    gi = gilt_intake_plan(herd, today=today)
    a = gi.attrs
    print(f"\n=== 후보돈 전입 계획 (갱신율 {REPLACEMENT_RATE:.0%}) ===")
    print(f"  모돈 {a['n_sows']}두 → 연간 갱신 여력 {a['annual_capacity']}두 "
          f"(월 기본 {a['monthly_base']}두, 상한 {a['monthly_cap']}두)")
    print(f"  도태 후보 {a['cull_pending']}두 · 현재 후보돈 {a['gilts_on_hand']}두 "
          f"→ 적체 해소 {a['months_to_clear']}개월 소요")
    for r in gi.itertuples(index=False):
        print(f"  {r.month} 전입 {r.need:>3}두 (잔여 적체 {r.backlog_left:>3}두) "
              f"→ 교배 투입 가능 {r.usable_from}")
    print("  ※ 도태 후보 전부를 한 번에 뺄 수는 없다 — 점수 상위부터 순차 교체한다.")

    print("\n※ 합성 데이터 시연이다. 실제로는 농장 번식기록(교배·분만·이유일)을 그대로"
          "\n  넣으면 같은 표가 나온다 — 추가 입력이 필요 없다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
