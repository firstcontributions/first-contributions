"""명세 §8 검증·경고 규칙 V1~V6.

경고와 오류를 구분한다. WARN 은 성적이 나빠지는 상태이고, ERROR 는 **AIAO 가
깨진 상태**다 — 후자는 배칭의 전제가 무너진 것이라 성적 문제와 급이 다르다.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from . import calc
from .config import Config
from .models import Batch, Room, stage_index

WARN, ERROR = "WARN", "ERROR"


@dataclass
class Finding:
    level: str
    check: str
    message: str
    at: date | None = None
    ref: str | None = None          # room_id 또는 batch_id


# V1 ----------------------------------------------------------------------
def check_density(cfg: Config, room: Room, batch: Batch,
                  on: date | None = None) -> list:
    """과밀사육 — 두당 면적이 법정 최소치 미만."""
    try:
        s = cfg.stage(batch.stage.value)
    except KeyError:
        return []
    if s.space_m2_per_head <= 0 or batch.head_count <= 0:
        return []
    per = room.area_m2 / batch.head_count
    if per < s.space_m2_per_head - 1e-9:
        return [Finding(WARN, "V1",
                        f"밀사: {s.name_ko} {room.room_id}, "
                        f"두당 {per:.3f}㎡ (기준 {s.space_m2_per_head}㎡)",
                        on, room.room_id)]
    return []


# V2 ----------------------------------------------------------------------
def check_bottleneck(cfg: Config, stage_id: str, available: int,
                     consecutive: int, on: date | None = None,
                     rooms: list | None = None) -> list:
    """병목 — 다음 스테이지에 빈 방이 2회 이상 연속으로 없음.

    필요/보유는 **돈사(house) 단위**로 센다. nursery 처럼 두 스테이지가 한
    돈사를 나눠 쓰면 스테이지 하나의 소요량만 보고 "필요 3, 보유 5" 라고 쓰게
    되는데, 정작 막힌 이유는 N1(3) + N2(3) = 6 이 5 를 넘긴 것이다. 실제로
    그렇게 모순된 메시지가 나왔다.

    보유 방 수는 실제 돈방 목록에서 센다. cfg.rooms(YAML) 만 보면 소요량대로
    지은 시뮬레이션에서 "보유 0" 이라는 거짓말이 나온다.
    """
    if available > 0 or consecutive < 2:
        return []
    s = cfg.stage(stage_id)
    iv = cfg.batch_system.interval_weeks
    share = [x for x in cfg.flow_stages if x.house == s.house]
    need = sum(calc.rooms_required(x, iv) for x in share)
    if rooms is not None:
        have = sum(1 for r in rooms if getattr(r, "house", None) == s.house)
    else:
        have = sum(1 for r in cfg.rooms if r.get("house") == s.house)
    who = "+".join(x.name_ko for x in share) if len(share) > 1 else s.name_ko
    return [Finding(ERROR, "V2",
                    f"{s.name_ko} 입식 불가 — {s.house}사({who}) 수용능력 부족. "
                    f"필요 돈방 {need}, 보유 {have}",
                    on, stage_id)]


# V3 ----------------------------------------------------------------------
def check_aiao(cfg: Config, rooms: list, batches: list,
               on: date | None = None) -> list:
    """AIAO 위반 — 한 방에 두 배치가 있거나 공백기가 0."""
    out = []
    by_room = {}
    for b in batches:
        if b.room_id:
            by_room.setdefault(b.room_id, []).append(b.batch_id)
    for rid, ids in by_room.items():
        if len(set(ids)) > 1:
            out.append(Finding(ERROR, "V3",
                               f"연속사육 상태: {rid} 에 배치 {sorted(set(ids))}",
                               on, rid))
    for s in cfg.flow_stages:
        if s.downtime_days == 0:
            out.append(Finding(ERROR, "V3",
                               f"연속사육 상태: {s.name_ko} 공백기 0일 — "
                               f"세척·건조 없이 다음 배치가 들어간다",
                               on, s.id))
    return out


# V4 ----------------------------------------------------------------------
def check_market_delay(cfg: Config, batch: Batch, on: date,
                       grace_days: int = 14) -> list:
    """출하 지연 — 목표 일령 + 14일 초과.

    지연 배치는 정상 흐름 대비 출하체중이 약 10kg 낮고 질병 위험이 높다는
    보고가 있어 별도 지표로 누적한다.
    """
    target = calc.market_age_days(cfg)
    age = batch.age_days(on)
    if age > target + grace_days:
        return [Finding(WARN, "V4",
                        f"출하지연 {batch.batch_id}: {age}일령 (목표 {target}일령)",
                        on, batch.batch_id)]
    return []


# V5 ----------------------------------------------------------------------
def check_performance(pre_wean_mortality: float, stillborn: float,
                      on: date | None = None) -> list:
    """성적 임계치 — 넘으면 분만사 AIAO 전환 이득이 크다."""
    out = []
    if pre_wean_mortality > 0.12:
        out.append(Finding(WARN, "V5",
                           f"분만사 AIAO 전환 검토: 이유 전 폐사 "
                           f"{pre_wean_mortality:.1%} > 12%", on))
    if stillborn > 0.08:
        out.append(Finding(WARN, "V5",
                           f"분만사 AIAO 전환 검토: 사산 {stillborn:.1%} > 8%",
                           on))
    return out


# V6 ----------------------------------------------------------------------
def check_backflow(events: list) -> list:
    """역류 이동 — to_stage 순서가 from_stage 보다 앞.

    뒤처진 돼지를 어린 배치로 되돌리는 것은 현장의 흔한 대처인데, 그러면
    AIAO 가 깨지고 어린 돼지가 병원체에 노출된다. 규칙 위반으로 잡는다.
    """
    out = []
    for e in events:
        if stage_index(e.to_stage) < stage_index(e.from_stage):
            out.append(Finding(ERROR, "V6",
                               f"역류 이동 감지: {e.batch_id} "
                               f"{e.from_stage.value}→{e.to_stage.value}",
                               e.date, e.batch_id))
    return out


def summarize(findings: list) -> dict:
    out = {"n": len(findings), "errors": 0, "warnings": 0, "by_check": {}}
    for f in findings:
        out["errors" if f.level == ERROR else "warnings"] += 1
        out["by_check"][f.check] = out["by_check"].get(f.check, 0) + 1
    return out
