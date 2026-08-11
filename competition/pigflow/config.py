"""명세 §2~4 — 스테이지·번식주기·배치시스템 설정.

**하드코딩 금지**(명세 요구사항 3). 아래 기본값은 국내 일반 관행의 초기값이며,
농장 전산기록이 있으면 YAML 로 덮어쓴다:

    cfg = load_config("myfarm.yaml")

주의(명세 §11): duration_days·폐사율은 초기값이다. 실제 농장 값으로 교체하지
않으면 그 농장의 계산이 아니다.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field, replace

# 법정 최소 면적 출처: 「축산법 시행령」 별표1
# (새끼돼지 0.2~0.3㎡ · 육성돈 0.45㎡ · 비육돈 0.8㎡)
# space_m2_per_head 는 **최소치**이므로 설계 시 safety_margin 을 곱해 쓴다.
STAGE_DEFAULTS = [
    dict(id="SUCKLING", name_ko="포유자돈", house="farrowing",
         entry_age_days=0, exit_age_days=24, duration_days=24,
         entry_weight_kg=1.4, exit_weight_kg=7.0,
         extra_occupancy_days=4, downtime_days=3,
         space_m2_per_head=0.0, unit="crate", expected_mortality_pct=12.0,
         note="분만틀 단위. extra_occupancy_days 는 분만 전 모돈 입방 대기일수."),
    dict(id="NURSERY_1", name_ko="이유자돈(전기)", house="nursery",
         entry_age_days=24, exit_age_days=45, duration_days=21,
         entry_weight_kg=7.0, exit_weight_kg=15.0,
         extra_occupancy_days=0, downtime_days=7,
         space_m2_per_head=0.25, unit="pen", expected_mortality_pct=2.0,
         note="모체이행항체 최저점 구간. 온도 30℃ 예열 후 입식."),
    dict(id="NURSERY_2", name_ko="이유자돈(후기)", house="nursery",
         entry_age_days=45, exit_age_days=70, duration_days=25,
         entry_weight_kg=15.0, exit_weight_kg=30.0,
         extra_occupancy_days=0, downtime_days=7,
         space_m2_per_head=0.35, unit="pen", expected_mortality_pct=1.5,
         note=""),
    dict(id="GROWER", name_ko="육성돈", house="grower",
         entry_age_days=70, exit_age_days=120, duration_days=50,
         entry_weight_kg=30.0, exit_weight_kg=60.0,
         extra_occupancy_days=0, downtime_days=7,
         space_m2_per_head=0.45, unit="pen", expected_mortality_pct=1.5,
         note=""),
    dict(id="FINISHER", name_ko="비육돈", house="finisher",
         entry_age_days=120, exit_age_days=175, duration_days=55,
         entry_weight_kg=60.0, exit_weight_kg=115.0,
         extra_occupancy_days=0, downtime_days=7,
         space_m2_per_head=0.80, unit="pen", expected_mortality_pct=1.0,
         note=""),
    dict(id="SHIPPED", name_ko="출하", house=None,
         entry_age_days=175, exit_age_days=None, duration_days=0,
         entry_weight_kg=115.0, exit_weight_kg=115.0,
         extra_occupancy_days=0, downtime_days=0,
         space_m2_per_head=0.0, unit=None, expected_mortality_pct=0.0,
         terminal=True, target_weight_kg=115.0, weight_tolerance_kg=8.0,
         note=""),
]

BREEDING_DEFAULTS = dict(
    wean_to_service_days=5, gestation_days=114, lactation_days=24,
    farrowing_rate=0.82, gilt_ratio_of_service=0.22, gilt_lead_weeks=7,
    sow_turnover=2.3, weaned_per_litter=12.0, post_wean_survival=0.95,
)

BATCH_SYSTEM_DEFAULTS = [
    dict(id="WEEKLY", interval_weeks=1, groups=21, typical_wean_age=24,
         scale="대규모"),
    dict(id="B2W", interval_weeks=2, groups=10, typical_wean_age=19,
         scale="중대규모"),
    dict(id="B3W", interval_weeks=3, groups=7, typical_wean_age=28,
         scale="중소규모"),
    dict(id="B4W", interval_weeks=4, groups=5, typical_wean_age=21,
         scale="소중규모"),
    dict(id="B5W", interval_weeks=5, groups=4, typical_wean_age=28,
         scale="소규모"),
]


@dataclass
class StageCfg:
    id: str
    name_ko: str
    house: str | None
    entry_age_days: int
    exit_age_days: int | None
    duration_days: int
    entry_weight_kg: float
    exit_weight_kg: float
    extra_occupancy_days: int = 0
    downtime_days: int = 0
    space_m2_per_head: float = 0.0
    unit: str | None = "pen"
    expected_mortality_pct: float = 0.0
    terminal: bool = False
    target_weight_kg: float | None = None
    weight_tolerance_kg: float | None = None
    note: str = ""

    @property
    def occupancy_days(self) -> int:
        """돈방이 묶여 있는 총 일수 — 사육 + 사전점유 + 공백기.

        공백기를 빼면 방이 모자라 AIAO 가 무너진다(명세 §0-4).
        """
        return self.duration_days + self.extra_occupancy_days + self.downtime_days

    @property
    def mortality(self) -> float:
        return self.expected_mortality_pct / 100.0


@dataclass
class BreedingCfg:
    wean_to_service_days: int = 5
    gestation_days: int = 114
    lactation_days: int = 24
    farrowing_rate: float = 0.82
    gilt_ratio_of_service: float = 0.22
    gilt_lead_weeks: int = 7
    sow_turnover: float = 2.3
    weaned_per_litter: float = 12.0
    post_wean_survival: float = 0.95

    @property
    def cycle_days(self) -> int:
        return (self.wean_to_service_days + self.gestation_days
                + self.lactation_days)

    @property
    def cycle_weeks(self) -> float:
        return self.cycle_days / 7.0


@dataclass
class BatchSystemCfg:
    id: str
    interval_weeks: float
    groups: int
    typical_wean_age: int
    scale: str = ""

    @property
    def interval_days(self) -> float:
        return self.interval_weeks * 7.0


@dataclass
class Config:
    stages: list = field(default_factory=list)
    breeding: BreedingCfg = field(default_factory=BreedingCfg)
    batch_systems: list = field(default_factory=list)
    batch_system_id: str = "WEEKLY"
    crate_count: int = 10
    safety_margin: float = 0.10
    # TODO 미구현 — 한 배치를 여러 돈방에 나누는 모드. 현재는 배치 1개가
    # 돈방 1개를 통째로 쓴다고 가정하므로 이 값을 True 로 해도 동작이 같다.
    allow_split: bool = False
    merge_stages: list = field(default_factory=list)
    rooms: list = field(default_factory=list)      # 보유 돈방(없으면 소요량만 계산)

    # -- 조회 -------------------------------------------------------------
    def stage(self, sid: str) -> StageCfg:
        for s in self.stages:
            if s.id == sid:
                return s
        raise KeyError(sid)

    @property
    def flow_stages(self) -> list:
        """터미널(SHIPPED)을 뺀 실제 사육 스테이지."""
        return [s for s in self.stages if not s.terminal]

    @property
    def batch_system(self) -> BatchSystemCfg:
        for b in self.batch_systems:
            if b.id == self.batch_system_id:
                return b
        raise KeyError(self.batch_system_id)

    @property
    def market_age_days(self) -> int:
        """총 사육일령(명세 5-9) — 터미널 제외 스테이지 duration 합."""
        return sum(s.duration_days for s in self.flow_stages)

    def with_batch_system(self, sid: str) -> "Config":
        return replace(self, batch_system_id=sid)

    def merged(self) -> "Config":
        """wean-to-finish 모드 — merge_stages 를 하나로 합쳐 이동을 없앤다.

        명세 §2: NURSERY_1~FINISHER 를 한 돈사에서 처리하면 이동 횟수가 0 이 된다.
        합친 스테이지의 점유일은 각 duration 합 + 마지막 공백기다(중간에 방을
        비우지 않으므로 중간 downtime 은 발생하지 않는다).
        """
        if not self.merge_stages:
            return self
        ids = list(self.merge_stages)
        keep, merge = [], []
        for s in self.stages:
            (merge if s.id in ids else keep).append(s)
        if not merge:
            return self
        first, last = merge[0], merge[-1]
        combo = StageCfg(
            id="+".join(ids), name_ko="+".join(m.name_ko for m in merge),
            house=first.house, entry_age_days=first.entry_age_days,
            exit_age_days=last.exit_age_days,
            duration_days=sum(m.duration_days for m in merge),
            entry_weight_kg=first.entry_weight_kg,
            exit_weight_kg=last.exit_weight_kg,
            extra_occupancy_days=first.extra_occupancy_days,
            downtime_days=last.downtime_days,
            space_m2_per_head=max(m.space_m2_per_head for m in merge),
            unit=first.unit,
            expected_mortality_pct=100.0 * (
                1.0 - _prod(1.0 - m.mortality for m in merge)),
            note="wean-to-finish 통합 스테이지")
        out = []
        placed = False
        for s in self.stages:
            if s.id in ids:
                if not placed:
                    out.append(combo)
                    placed = True
            else:
                out.append(s)
        return replace(self, stages=out, merge_stages=[])


def _prod(xs) -> float:
    p = 1.0
    for x in xs:
        p *= x
    return p


def default_config() -> Config:
    return Config(
        stages=[StageCfg(**s) for s in STAGE_DEFAULTS],
        breeding=BreedingCfg(**BREEDING_DEFAULTS),
        batch_systems=[BatchSystemCfg(**b) for b in BATCH_SYSTEM_DEFAULTS],
    )


def load_config(path: str | None = None) -> Config:
    """기본값 + YAML 오버라이드.

    YAML 은 부분만 적어도 된다. 예:
        crate_count: 40
        batch_system_id: B3W
        breeding: {lactation_days: 28}
        stages:
          - {id: FINISHER, downtime_days: 10}
        rooms:
          - {room_id: F1, house: finisher, capacity_head: 130, area_m2: 110}
    """
    cfg = default_config()
    if not path:
        return cfg
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    import yaml
    raw = yaml.safe_load(open(path, encoding="utf-8")) or {}

    for k in ("batch_system_id", "crate_count", "safety_margin",
              "allow_split", "merge_stages"):
        if k in raw:
            setattr(cfg, k, raw[k])
    if "breeding" in raw:
        for k, v in (raw["breeding"] or {}).items():
            if hasattr(cfg.breeding, k):
                setattr(cfg.breeding, k, v)
    # 스테이지는 id 로 찾아 **부분 갱신**한다. 통째로 갈아끼우게 하면
    # YAML 에 한 필드만 적었을 때 나머지가 사라진다.
    for s in raw.get("stages", []) or []:
        sid = s.get("id")
        try:
            tgt = cfg.stage(sid)
        except KeyError:
            cfg.stages.append(StageCfg(**s))
            continue
        for k, v in s.items():
            if k != "id" and hasattr(tgt, k):
                setattr(tgt, k, v)
    for b in raw.get("batch_systems", []) or []:
        cfg.batch_systems = [x for x in cfg.batch_systems if x.id != b.get("id")]
        cfg.batch_systems.append(BatchSystemCfg(**b))
    if "rooms" in raw:
        cfg.rooms = list(raw["rooms"] or [])
    return cfg
