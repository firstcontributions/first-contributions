"""명세 §5 핵심 계산식 — **순수 함수**(외부 상태 의존 없음).

설계 근거: 분만틀 수가 흐름의 유일한 고정 물리량이다. 모돈 두수와 PSY 는
계절 변동을 타므로 설계 기준으로 삼지 않는다(CEVA / John Carr 모델).

검산(명세 §5, 분만틀 10 · 주간배치 · 이유 24일):
    services_per_batch = ceil(10 / 0.82)          = 13
    gilts_per_batch    = ceil(13 * 0.22)          = 3
    sow_inventory      = (10*52)/2.3 + 3*7        = 247
    weaned_per_batch   = 10 * 12                  = 120
    shipped_per_batch  = 120 * 0.95               = 114
    rooms(SUCKLING)    = ceil((24+4+3)/7)         = 5
    rooms(FINISHER)    = ceil((55+7)/7)           = 9
이 값들은 테스트로 고정한다.
"""
from __future__ import annotations

import math

from .config import BreedingCfg, Config, StageCfg
from .models import Stage


# 5-1 --------------------------------------------------------------------
def services_per_batch(crate_count: int, farrowing_rate: float) -> int:
    """배치당 교배 두수 = 분만틀 ÷ 분만율.

    분만율은 **평균이 아니라 하위 분위수**를 넣어야 한다. 평균으로 잡으면
    절반의 배치에서 분만틀이 빈다(기본값 0.82 = 전 세계 10분위).
    """
    if crate_count <= 0:
        return 0
    return math.ceil(crate_count / max(1e-9, farrowing_rate))


# 5-2 --------------------------------------------------------------------
def gilts_per_batch(services: int, gilt_ratio: float) -> int:
    return math.ceil(services * gilt_ratio) if services > 0 else 0


# 5-3 --------------------------------------------------------------------
def sow_inventory(crate_count: int, interval_weeks: float,
                  sow_turnover: float, gilts: int, gilt_lead_weeks: int
                  ) -> float:
    """번식돈군 규모 = 분만틀×(52/간격주)/회전율 + 후보돈×후보돈주기."""
    if interval_weeks <= 0:
        raise ValueError("interval_weeks 는 0 보다 커야 한다")
    breeding = crate_count * (52.0 / interval_weeks) / max(1e-9, sow_turnover)
    return breeding + gilts * gilt_lead_weeks


# 5-4 --------------------------------------------------------------------
def weaned_per_batch(crate_count: int, weaned_per_litter: float) -> float:
    return crate_count * weaned_per_litter


# 5-5 --------------------------------------------------------------------
def shipped_per_batch(weaned: float, post_wean_survival: float) -> float:
    return weaned * post_wean_survival


def liveweight_per_batch_kg(shipped: float, target_weight_kg: float) -> float:
    return shipped * target_weight_kg


# 5-6 ★ -------------------------------------------------------------------
def rooms_required(stage: StageCfg, interval_weeks: float) -> int:
    """스테이지별 필요 돈방 수 — 가장 중요한 계산.

    (사육일 + 사전점유일 + **공백기**) ÷ 배치 간격. 공백기를 빼면 방이 모자라
    올인/올아웃이 무너지고, 그러면 배칭의 목적 자체가 사라진다.
    """
    if stage.terminal:
        return 0
    days = interval_weeks * 7.0
    if days <= 0:
        raise ValueError("interval_weeks 는 0 보다 커야 한다")
    return math.ceil(stage.occupancy_days / days)


def room_slack_days(stage: StageCfg, interval_weeks: float) -> float:
    """방 여유 = 방 수 × 간격 − 점유일.

    0 이면 세척이 정확히 제 날에 끝나야만 성립한다는 뜻이다. 방 수만 보면
    '충분하다'로 읽히므로 여유를 따로 낸다.
    """
    if stage.terminal:
        return 0.0
    n = rooms_required(stage, interval_weeks)
    return n * interval_weeks * 7.0 - stage.occupancy_days


# 5-8 --------------------------------------------------------------------
def batch_head_at(cfg: Config, stage_id: str, weaned: float | None = None
                  ) -> float:
    """스테이지 진입 두수 — 앞 단계들의 누적 폐사를 반영.

    SUCKLING 은 이유 전이므로 분만 두수에서 시작한다. 그 외 스테이지는
    이유두수에서 시작해 이전 단계 폐사를 곱해 나간다.
    """
    b = cfg.breeding
    if weaned is None:
        weaned = weaned_per_batch(cfg.crate_count, b.weaned_per_litter)
    flow = cfg.flow_stages
    ids = [s.id for s in flow]
    if stage_id not in ids:
        raise KeyError(stage_id)
    i = ids.index(stage_id)
    if i == 0:
        # 포유 구간의 진입은 '생시' 두수. 이유두수를 포유 폐사로 역산한다.
        m = flow[0].mortality
        return weaned / max(1e-9, 1.0 - m)
    head = weaned
    for s in flow[1:i]:
        head *= (1.0 - s.mortality)
    return head


# 5-7 --------------------------------------------------------------------
def head_per_room(cfg: Config, stage_id: str, safety_margin: float | None = None
                  ) -> int:
    sm = cfg.safety_margin if safety_margin is None else safety_margin
    return math.ceil(batch_head_at(cfg, stage_id) * (1.0 + sm))


def area_per_room_m2(cfg: Config, stage_id: str) -> float:
    s = cfg.stage(stage_id)
    return head_per_room(cfg, stage_id) * s.space_m2_per_head


# 5-9 --------------------------------------------------------------------
def market_age_days(cfg: Config) -> int:
    return sum(s.duration_days for s in cfg.flow_stages)


# 배치 수 (명세 §4) ---------------------------------------------------------
def groups_required(breeding: BreedingCfg, interval_weeks: float) -> int:
    """배치 수 = ceil(주기(주) / 간격(주)).

    주간 20.4/1≈21 · 3주 20.4/3≈7 · 4주 20.4/4≈6 이 나온다. 명세 표의
    B4W groups=5 와는 1 차이가 나는데, 표는 실무 관행값(5/4/1 시스템)이고
    이 식은 순수 산술이다. 둘을 섞지 않기 위해 계산값을 그대로 돌려주고,
    표의 값이 필요하면 BatchSystemCfg.groups 를 쓴다.
    """
    return math.ceil(breeding.cycle_weeks / interval_weeks)


# 종합 --------------------------------------------------------------------
def plan(cfg: Config) -> dict:
    """분만틀 기준 전체 설계 — 명세 §5 전부를 한 번에."""
    b = cfg.breeding
    bs = cfg.batch_system
    iv = bs.interval_weeks
    svc = services_per_batch(cfg.crate_count, b.farrowing_rate)
    gilts = gilts_per_batch(svc, b.gilt_ratio_of_service)
    weaned = weaned_per_batch(cfg.crate_count, b.weaned_per_litter)
    shipped = shipped_per_batch(weaned, b.post_wean_survival)
    target = cfg.stage("SHIPPED").target_weight_kg or 115.0
    rooms = {}
    for s in cfg.flow_stages:
        rooms[s.id] = {
            "rooms_required": rooms_required(s, iv),
            "occupancy_days": s.occupancy_days,
            "slack_days": round(room_slack_days(s, iv), 1),
            "head_per_room": head_per_room(cfg, s.id),
            "area_per_room_m2": round(area_per_room_m2(cfg, s.id), 1),
            "head_at_entry": round(batch_head_at(cfg, s.id), 1),
        }
    return {
        "batch_system": bs.id, "interval_weeks": iv,
        "crate_count": cfg.crate_count,
        "services_per_batch": svc,
        "gilts_per_batch": gilts,
        "sow_inventory": round(sow_inventory(
            cfg.crate_count, iv, b.sow_turnover, gilts, b.gilt_lead_weeks), 1),
        "weaned_per_batch": round(weaned, 1),
        "shipped_per_batch": round(shipped, 1),
        "liveweight_per_batch_kg": round(
            liveweight_per_batch_kg(shipped, target), 1),
        "groups_required": groups_required(b, iv),
        "groups_table": bs.groups,
        "market_age_days": market_age_days(cfg),
        "cycle_days": b.cycle_days,
        "rooms": rooms,
    }


def compare_systems(cfg: Config, system_ids=None) -> list:
    """what-if — 배치 시스템별 소요 비교(명세 요구사항 5)."""
    ids = system_ids or [b.id for b in cfg.batch_systems]
    out = []
    for sid in ids:
        p = plan(cfg.with_batch_system(sid))
        out.append({
            "system": sid, "interval_weeks": p["interval_weeks"],
            "groups": p["groups_required"],
            "services_per_batch": p["services_per_batch"],
            "sow_inventory": p["sow_inventory"],
            "weaned_per_batch": p["weaned_per_batch"],
            "total_rooms": sum(r["rooms_required"] for r in p["rooms"].values()),
            "rooms": {k: v["rooms_required"] for k, v in p["rooms"].items()},
            "min_slack": min(r["slack_days"] for r in p["rooms"].values()),
        })
    return out


# KPI (명세 §9) -----------------------------------------------------------
def kpis(breeding: BreedingCfg, weaned_total: float, shipped_total: float,
         avg_sows: float) -> dict:
    """연간 두수 → PSY/MSY.

    npd_floor_days 는 **이론 최소 비생산일**이다 = 이유~재교배 간격. 재발정·
    유산·도태 대기가 전혀 없다는 가정이라 현장 NPD(40~60일)와 직접 비교하면
    안 된다. 설정 회전율(sow_turnover)과 이론 회전율의 차이가 그 손실이다.
    """
    turnover = 365.0 / breeding.cycle_days
    npd_floor = 365.0 / turnover - (breeding.gestation_days
                                    + breeding.lactation_days)
    return {
        "psy": round(weaned_total / max(1e-9, avg_sows), 2),
        "msy": round(shipped_total / max(1e-9, avg_sows), 2),
        "sow_turnover": round(turnover, 2),
        "npd_floor_days": round(npd_floor, 1),
        "post_wean_survival": round(
            shipped_total / max(1e-9, weaned_total), 3),
    }


BENCHMARK = {
    "target": {"name": "부경양돈농협 상위", "psy": 27.3, "msy": 23.1,
               "farrowing_rate": 0.827, "npd": 40.0, "turnover": 2.34},
    "floor": {"name": "한돈팜스 전국 평균", "psy": 22.8, "msy": 18.4},
}
