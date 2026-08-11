"""명세 §9 KPI 집계 + 돈방 점유 간트.

요구사항 4: "현재 돈사 구성에서 병목이 어디인지"와 "각 스테이지 필요 돈방 수
vs 보유 돈방 수" 표를 낸다.
요구사항 5: 배치 시스템별 what-if 비교표.
"""
from __future__ import annotations

from collections import Counter
from datetime import timedelta

from . import calc
from .config import Config
from .models import Stage


def rooms_table(cfg: Config, rooms: list | None = None) -> list:
    """스테이지별 **필요 vs 보유** — 병목의 원인을 숫자로."""
    iv = cfg.batch_system.interval_weeks
    have = Counter(r.house for r in (rooms or []))
    # house 를 두 스테이지가 공유하면(nursery) 필요 수를 합쳐 비교해야 한다
    need_by_house = Counter()
    for s in cfg.flow_stages:
        need_by_house[s.house] += calc.rooms_required(s, iv)
    out = []
    for s in cfg.flow_stages:
        need = calc.rooms_required(s, iv)
        out.append({
            "stage": s.id, "name_ko": s.name_ko, "house": s.house,
            "occupancy_days": s.occupancy_days,
            "duration": s.duration_days, "downtime": s.downtime_days,
            "rooms_required": need,
            "slack_days": round(calc.room_slack_days(s, iv), 1),
            "head_per_room": calc.head_per_room(cfg, s.id),
            "area_per_room_m2": round(calc.area_per_room_m2(cfg, s.id), 1),
            "house_required": need_by_house[s.house],
            "house_have": have.get(s.house, 0),
            "shortage": max(0, need_by_house[s.house] - have.get(s.house, 0)),
        })
    return out


def bottlenecks(sim) -> list:
    """병목 집계 — 어느 스테이지에서 몇 번 막혔나(warm-up 이후)."""
    cut = sim.start + timedelta(days=sim.warmup_days)
    c = Counter(f.ref for f in sim.findings
                if f.check == "V2" and f.at and f.at >= cut)
    return [{"stage": k, "events": v} for k, v in c.most_common()]


def kpi_report(sim, avg_sows: float | None = None) -> dict:
    """명세 §9 KPI — warm-up 이후 구간만 센다.

    **같은 코호트로 센다.** 이유 이벤트와 출하 이벤트를 각각 창(window) 안에서
    합산하면 서로 다른 배치를 비교하게 되어 이유후 생존율이 설정값(94.1%)보다
    높게 나온다. 실제로 그렇게 짜서 97.1% 가 나왔었다. 출하된 배치를 기준으로
    **그 배치 자신의 이유 두수**를 되짚어 쓴다.
    """
    cfg = sim.cfg
    b = cfg.breeding
    first = Stage(cfg.flow_stages[0].id)
    cut = sim.start + timedelta(days=sim.warmup_days)
    cohort = [x for x in sim.shipped if x.history and x.history[-1][0] >= cut]
    days = max(1, (sim.day - cut).days)
    years = days / 365.0
    if avg_sows is None:
        avg_sows = calc.sow_inventory(
            cfg.crate_count, cfg.batch_system.interval_weeks, b.sow_turnover,
            calc.gilts_per_batch(
                calc.services_per_batch(cfg.crate_count, b.farrowing_rate),
                b.gilt_ratio_of_service),
            b.gilt_lead_weeks)
    weaned_total = 0
    for x in cohort:
        for (_d, fs, _ts, moved, _fr) in x.history:
            if fs == first:
                weaned_total += moved
                break
    shipped_total = sum(x.head_count for x in cohort)
    k = calc.kpis(b, weaned_total / max(1e-9, years),
                  shipped_total / max(1e-9, years), avg_sows)
    occ = sim.steady_occupancy()
    total_rooms = max(1, len(sim.rooms))
    k["room_utilization"] = round(
        sum(o["occupied"] for o in occ) / (len(occ) * total_rooms), 3
    ) if occ else None
    k["batches_shipped"] = len(cohort)
    k["weaned_total"] = weaned_total
    k["shipped_total"] = shipped_total
    k["avg_sows"] = round(avg_sows, 1)
    k["days_steady"] = days
    # 설정 회전율(2.3)은 재발정·도태를 포함한 실적치, 계산 회전율은 무손실
    # 이론치다. 둘이 벌어지는 폭이 그 농장의 번식 손실이다.
    k["sow_turnover_config"] = b.sow_turnover
    k["benchmark"] = calc.BENCHMARK
    return k


def gantt(sim, house: str | None = None, width: int = 72) -> str:
    """돈방 점유 간트(텍스트) — ▓ 재실 · ░ 세척 · · 빈방.

    AIAO 가 지켜지는지는 표보다 그림이 빠르다. 같은 방에 ▓ 가 끊기지 않고
    이어지면 세척 없이 다음 배치가 들어간 것이다.
    """
    cut = sim.start + timedelta(days=sim.warmup_days)
    days = [cut + timedelta(days=i) for i in range(width)]
    lines = []
    rooms = [r for r in sim.rooms if house is None or r.house == house]
    # house 별 공백기 — 같은 house 를 쓰는 스테이지 중 가장 긴 값
    dt_by_house = {}
    for s in sim.cfg.flow_stages:
        dt_by_house[s.house] = max(dt_by_house.get(s.house, 0), s.downtime_days)
    # 이력에서 방별 점유 구간 (start, end) 을 복원한다
    occ = {r.room_id: [] for r in rooms}
    for b in sim.batches:
        prev_day = None
        for (d, _fs, _ts, _h, from_room) in b.history:
            if from_room and from_room in occ:
                occ[from_room].append((prev_day or b.farrow_date, d))
            prev_day = d
        if b.room_id and b.room_id in occ:
            occ[b.room_id].append((prev_day or b.farrow_date, sim.day))
    for r in rooms:
        dt = timedelta(days=dt_by_house.get(r.house, 0))
        row = []
        for d in days:
            ch = "·"
            for (s, e) in occ.get(r.room_id, []):
                if s <= d < e:
                    ch = "▓"
                    break
                if e <= d < e + dt:
                    ch = "░"
            row.append(ch)
        lines.append(f"  {r.room_id:<14}{''.join(row)}")
    head = f"  {'돈방':<14}{cut:%m/%d} → {days[-1]:%m/%d}"
    return head + "\n" + "\n".join(lines)


def whatif_table(cfg: Config) -> list:
    """배치 시스템별 비교(명세 요구사항 5)."""
    return calc.compare_systems(cfg)
