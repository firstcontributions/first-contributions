"""명세 §6 데이터 모델 — Room · Batch · MoveEvent."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class Stage(str, Enum):
    SUCKLING = "SUCKLING"
    NURSERY_1 = "NURSERY_1"
    NURSERY_2 = "NURSERY_2"
    GROWER = "GROWER"
    FINISHER = "FINISHER"
    SHIPPED = "SHIPPED"


# 단방향 순서(명세 RULE T1). 인덱스 비교로 역류를 판정한다.
STAGE_ORDER = [Stage.SUCKLING, Stage.NURSERY_1, Stage.NURSERY_2,
               Stage.GROWER, Stage.FINISHER, Stage.SHIPPED]


def stage_index(s: Stage | str) -> int:
    return STAGE_ORDER.index(Stage(s))


def next_stage(s: Stage | str) -> Stage | None:
    i = stage_index(s)
    return STAGE_ORDER[i + 1] if i + 1 < len(STAGE_ORDER) else None


class RoomState(str, Enum):
    EMPTY = "EMPTY"          # 입식 가능
    OCCUPIED = "OCCUPIED"    # 배치 재실 중
    WASHING = "WASHING"      # 세척·소독·건조(downtime)


@dataclass
class Room:
    room_id: str
    house: str                       # farrowing / nursery / grower / finisher
    capacity_head: int
    area_m2: float
    state: RoomState = RoomState.EMPTY
    current_batch_id: str | None = None
    available_from: date | None = None   # downtime 종료일

    def is_available(self, on: date) -> bool:
        """입식 가능 여부. WASHING 이어도 available_from 이 지나면 쓸 수 있다."""
        if self.state == RoomState.OCCUPIED:
            return False
        return self.available_from is None or on >= self.available_from


@dataclass
class Batch:
    batch_id: str                    # 예: "2026-W15"
    service_date: date
    farrow_date: date
    wean_date: date
    stage: Stage
    head_count: int
    room_id: str | None = None
    entered_stage_on: date | None = None
    history: list = field(default_factory=list)

    def age_days(self, on: date) -> int:
        """일령 — 분만일이 0일령이다."""
        return (on - self.farrow_date).days


@dataclass
class MoveEvent:
    date: date
    batch_id: str
    from_stage: Stage
    to_stage: Stage
    head_moved: int
    head_dead: int
    from_room: str | None
    to_room: str | None
