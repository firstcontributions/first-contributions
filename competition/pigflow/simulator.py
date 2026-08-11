"""명세 §7 전이 규칙으로 하루씩 진행하는 시뮬레이터.

RULE T1 단방향   T2 (일령 도달) AND (빈 돈방)   T3 배치 통째 이동
RULE T4 방당 1배치(AIAO)   T5 전출 후 WASHING   T6 역류 금지

warm-up: 파이프라인이 채워지기 전 구간은 정상 상태가 아니다. 그 기간의
가동률·병목을 그대로 보고하면 설비가 남아도는 것처럼 보이므로, 총 사육일령
이상 돌린 뒤부터를 steady state 로 본다.
"""
from __future__ import annotations

from datetime import date, timedelta

from . import calc, validate
from .config import Config
from .models import Batch, MoveEvent, Room, RoomState, Stage


def build_rooms(cfg: Config, from_config: bool = True) -> list:
    """보유 돈방 목록. config.rooms 가 있으면 그것을, 없으면 소요량대로 만든다."""
    if from_config and cfg.rooms:
        return [Room(room_id=r["room_id"], house=r["house"],
                     capacity_head=int(r["capacity_head"]),
                     area_m2=float(r["area_m2"])) for r in cfg.rooms]
    iv = cfg.batch_system.interval_weeks
    rooms = []
    for s in cfg.flow_stages:
        n = calc.rooms_required(s, iv)
        head = calc.head_per_room(cfg, s.id)
        area = calc.area_per_room_m2(cfg, s.id)
        for i in range(n):
            rooms.append(Room(room_id=f"{s.id}-{i + 1}", house=s.house,
                              capacity_head=head, area_m2=area))
    return rooms


class Simulator:
    def __init__(self, cfg: Config, start: date, rooms: list | None = None):
        self.cfg = cfg.merged()
        self.start = start
        self.rooms = rooms if rooms is not None else build_rooms(self.cfg)
        self.batches: list = []
        self.events: list = []
        self.findings: list = []
        self.shipped: list = []
        self.day = start
        self._seq = 0
        self._no_room_streak: dict = {}
        self.occupancy_log: list = []

    # -- 내부 --------------------------------------------------------------
    def _stage_ids(self) -> list:
        return [s.id for s in self.cfg.flow_stages]

    def _free_room(self, house: str, on: date, stage_id: str | None = None,
                   head: int = 0):
        """빈 돈방 찾기 — **house 만 보면 안 된다**.

        NURSERY_1(0.25㎡)과 NURSERY_2(0.35㎡)는 같은 house 를 쓰지만 요구
        면적이 다르다. house 로만 고르면 좁은 방에 큰 돼지를 넣게 되고, 그
        결과가 과밀 경고로 되돌아온다(실제로 999건이 그렇게 났다).
        스테이지의 두당 면적과 수용두수를 만족하는 방만 고른다.
        """
        need = 0.0
        if stage_id:
            need = self.cfg.stage(stage_id).space_m2_per_head
        best = None
        for r in self.rooms:
            if r.house != house or not r.is_available(on):
                continue
            if head > 0:
                if need > 0 and r.area_m2 / head < need - 1e-9:
                    continue
                if r.capacity_head and r.capacity_head < head:
                    continue
            # 요건을 만족하는 방 중 **가장 작은 것**을 쓴다. 큰 방을 먼저
            # 소진하면 뒤에 오는 큰 배치가 들어갈 곳이 없어진다.
            if best is None or r.area_m2 < best.area_m2:
                best = r
        return best

    def _release(self, room: Room, on: date, stage_id: str):
        """RULE T5 — 전출 직후 WASHING, available_from = 전출일 + 공백기."""
        dt = self.cfg.stage(stage_id).downtime_days
        room.state = RoomState.WASHING
        room.current_batch_id = None
        room.available_from = on + timedelta(days=dt)

    def _place(self, room: Room, batch: Batch, on: date):
        room.state = RoomState.OCCUPIED
        room.current_batch_id = batch.batch_id
        room.available_from = None
        batch.room_id = room.room_id
        batch.entered_stage_on = on

    def _move(self, batch: Batch, to_stage: Stage, on: date,
              to_room: Room | None):
        from_stage, from_room = batch.stage, batch.room_id
        # RULE T6 — 역류는 만들지 않는다. 만들어졌다면 검증에서 잡힌다.
        s_cur = self.cfg.stage(from_stage.value)
        died = int(round(batch.head_count * s_cur.mortality))
        moved = batch.head_count - died
        ev = MoveEvent(date=on, batch_id=batch.batch_id,
                       from_stage=from_stage, to_stage=to_stage,
                       head_moved=moved, head_dead=died,
                       from_room=from_room,
                       to_room=to_room.room_id if to_room else None)
        self.events.append(ev)
        batch.history.append((on, from_stage, to_stage, moved, from_room))
        batch.head_count = moved
        batch.stage = to_stage
        if to_room is not None:
            self._place(to_room, batch, on)
        else:
            batch.room_id = None
            batch.entered_stage_on = on

    # -- 하루 --------------------------------------------------------------
    def step(self):
        on = self.day
        cfg = self.cfg
        b = cfg.breeding
        iv_days = int(round(cfg.batch_system.interval_days))

        # 1) 배치 생성 — 간격마다 한 배치가 분만한다
        if (on - self.start).days % iv_days == 0:
            self._seq += 1
            weaned = calc.weaned_per_batch(cfg.crate_count, b.weaned_per_litter)
            born = weaned / max(1e-9, 1.0 - cfg.flow_stages[0].mortality)
            bt = Batch(batch_id=f"B{self._seq:03d}",
                       service_date=on - timedelta(days=b.gestation_days),
                       farrow_date=on,
                       wean_date=on + timedelta(days=b.lactation_days),
                       stage=Stage(cfg.flow_stages[0].id),
                       head_count=int(round(born)),
                       entered_stage_on=on)
            room = self._free_room(cfg.flow_stages[0].house, on,
                                   cfg.flow_stages[0].id, bt.head_count)
            if room:
                self._place(room, bt, on)
            else:
                self._bottleneck(cfg.flow_stages[0].id, on)
            self.batches.append(bt)

        # 2) 이동 — 오래된 배치부터(먼저 들어온 것이 먼저 나간다)
        ids = self._stage_ids()
        for bt in sorted([x for x in self.batches
                          if x.stage != Stage.SHIPPED],
                         key=lambda x: x.farrow_date):
            s = cfg.stage(bt.stage.value)
            if bt.entered_stage_on is None:
                continue
            # RULE T2-a 일령 도달
            if bt.age_days(on) < (s.exit_age_days or 10**9):
                continue
            nxt_id = ids[ids.index(s.id) + 1] if ids.index(s.id) + 1 < len(ids) \
                else "SHIPPED"
            if nxt_id == "SHIPPED":
                if bt.room_id:
                    self._release(self._room(bt.room_id), on, s.id)
                self._move(bt, Stage.SHIPPED, on, None)
                self.shipped.append(bt)
                continue
            nxt = cfg.stage(nxt_id)
            # 이동 후 두수(현 단계 폐사 반영)로 방을 고른다
            head_after = bt.head_count - int(round(bt.head_count * s.mortality))
            room = self._free_room(nxt.house, on, nxt_id, head_after)
            if room is None:
                # RULE T2-b 빈 방 없음 → 이동 보류, 병목 기록
                self._bottleneck(nxt_id, on)
                continue
            self._no_room_streak[nxt_id] = 0
            if bt.room_id:
                self._release(self._room(bt.room_id), on, s.id)
            self._move(bt, Stage(nxt_id), on, room)

        # 3) 세척 종료 처리
        for r in self.rooms:
            if r.state == RoomState.WASHING and r.available_from \
                    and on >= r.available_from:
                r.state = RoomState.EMPTY

        # 4) 검증 — 과밀·출하지연
        for bt in self.batches:
            if bt.room_id and bt.stage != Stage.SHIPPED:
                self.findings += validate.check_density(
                    cfg, self._room(bt.room_id), bt, on)
            if bt.stage != Stage.SHIPPED:
                self.findings += validate.check_market_delay(cfg, bt, on)

        self.occupancy_log.append({
            "date": on,
            "occupied": sum(1 for r in self.rooms
                            if r.state == RoomState.OCCUPIED),
            "washing": sum(1 for r in self.rooms
                           if r.state == RoomState.WASHING),
            "empty": sum(1 for r in self.rooms if r.state == RoomState.EMPTY),
        })
        self.day = on + timedelta(days=1)

    def _room(self, rid: str) -> Room:
        return next(r for r in self.rooms if r.room_id == rid)

    def _bottleneck(self, stage_id: str, on: date):
        n = self._no_room_streak.get(stage_id, 0) + 1
        self._no_room_streak[stage_id] = n
        self.findings += validate.check_bottleneck(
            self.cfg, stage_id, 0, n, on, rooms=self.rooms)

    # -- 실행 --------------------------------------------------------------
    def run(self, days: int) -> "Simulator":
        for _ in range(days):
            self.step()
        # 실행이 끝난 뒤 전체 이벤트에 대해 역류·AIAO 를 한 번에 본다
        self.findings += validate.check_backflow(self.events)
        self.findings += validate.check_aiao(self.cfg, self.rooms, self.batches)
        return self

    @property
    def warmup_days(self) -> int:
        """정상 상태 도달까지 — 총 사육일령만큼은 파이프라인이 차지 않는다."""
        return calc.market_age_days(self.cfg)

    def steady_events(self) -> list:
        cut = self.start + timedelta(days=self.warmup_days)
        return [e for e in self.events if e.date >= cut]

    def steady_occupancy(self) -> list:
        cut = self.start + timedelta(days=self.warmup_days)
        return [o for o in self.occupancy_log if o["date"] >= cut]
