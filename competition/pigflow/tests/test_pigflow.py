"""pigflow 테스트 — 명세 §5 검산 예시를 **고정값으로 못 박는다**.

    python competition/pigflow/tests/test_pigflow.py     # 단독 실행
    pytest competition/pigflow/tests/                    # pytest 로도 수집

명세 §10 요구사항 1: "섹션 5의 검산 예시(분만틀 10개 → sow_inventory 247,
분만사 5돈방)를 pytest로 고정." 계산식을 손대다 이 값이 흔들리면 실패한다.
"""
from __future__ import annotations

import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pigflow import calc, report, validate                       # noqa: E402
from pigflow.config import Config, default_config, load_config   # noqa: E402
from pigflow.models import Batch, Room, RoomState, Stage, stage_index  # noqa: E402
from pigflow.simulator import Simulator, build_rooms             # noqa: E402


def _cfg() -> Config:
    """명세 §5 검산 조건: 분만틀 10 · 주간배치 · 이유 24일."""
    c = default_config()
    c.crate_count = 10
    c.batch_system_id = "WEEKLY"
    return c


# -- §5 검산 (요구사항 1) ---------------------------------------------------
def test_spec_worked_example() -> None:
    """명세 §5 검산 8개 값 전부."""
    c = _cfg()
    b = c.breeding
    svc = calc.services_per_batch(c.crate_count, b.farrowing_rate)
    assert svc == 13, f"배치당 교배 13 이어야 하는데 {svc}"

    gilts = calc.gilts_per_batch(svc, b.gilt_ratio_of_service)
    assert gilts == 3, f"배치당 후보돈 3 이어야 하는데 {gilts}"

    inv = calc.sow_inventory(c.crate_count, 1, b.sow_turnover, gilts,
                             b.gilt_lead_weeks)
    assert round(inv) == 247, f"모돈규모 247 이어야 하는데 {inv:.1f}"

    weaned = calc.weaned_per_batch(c.crate_count, b.weaned_per_litter)
    assert weaned == 120

    shipped = calc.shipped_per_batch(weaned, b.post_wean_survival)
    assert shipped == 114

    # 분만사 = (24 사육 + 4 사전점유 + 3 공백) / 7 = 4.43 → 5
    assert calc.rooms_required(c.stage("SUCKLING"), 1) == 5
    # 비육사 = (55 + 7) / 7 = 8.86 → 9
    assert calc.rooms_required(c.stage("FINISHER"), 1) == 9

    assert calc.market_age_days(c) == 175
    assert b.cycle_days == 143      # 5 + 114 + 24


def test_downtime_is_counted_in_rooms() -> None:
    """공백기를 빼면 방이 모자란다 — 명세 §0-4 의 핵심.

    공백기 0 으로 두면 비육사가 9방에서 8방으로 줄어든다. 그 한 방이
    AIAO 를 지탱하는 방이다.
    """
    from dataclasses import replace as _replace
    c = _cfg()
    fin = c.stage("FINISHER")
    assert calc.rooms_required(fin, 1) == 9
    assert calc.rooms_required(_replace(fin, downtime_days=0), 1) == 8


def test_room_slack_flags_zero_margin() -> None:
    c = _cfg()
    # 이유자돈(전기): (21+0+7)=28, 4방 × 7일 = 28 → 여유 0
    assert calc.room_slack_days(c.stage("NURSERY_1"), 1) == 0.0
    assert calc.room_slack_days(c.stage("SUCKLING"), 1) == 4.0
    assert calc.room_slack_days(c.stage("SHIPPED"), 1) == 0.0


def test_terminal_stage_needs_no_room() -> None:
    c = _cfg()
    assert calc.rooms_required(c.stage("SHIPPED"), 1) == 0
    assert [s.id for s in c.flow_stages] == [
        "SUCKLING", "NURSERY_1", "NURSERY_2", "GROWER", "FINISHER"]


def test_mortality_cascades_forward() -> None:
    """스테이지 진입 두수는 앞 단계 폐사를 누적 반영해야 한다."""
    c = _cfg()
    # SUCKLING 진입 = 생시두수 = 이유 120 / (1 - 12%)
    assert round(calc.batch_head_at(c, "SUCKLING"), 1) == 136.4
    assert calc.batch_head_at(c, "NURSERY_1") == 120.0
    assert round(calc.batch_head_at(c, "NURSERY_2"), 1) == 117.6   # ×0.98
    n2 = calc.batch_head_at(c, "NURSERY_2")
    assert calc.batch_head_at(c, "GROWER") < n2                    # 단조 감소
    assert calc.batch_head_at(c, "FINISHER") < calc.batch_head_at(c, "GROWER")


def test_zero_interval_rejected() -> None:
    c = _cfg()
    for fn, args in ((calc.rooms_required, (c.stage("FINISHER"), 0)),
                     (calc.sow_inventory, (10, 0, 2.3, 3, 7))):
        try:
            fn(*args)
        except ValueError:
            continue
        raise AssertionError(f"{fn.__name__} 이 간격 0 을 통과시킴")


# -- 설정 -------------------------------------------------------------------
def test_yaml_partial_stage_update() -> None:
    """YAML 에 한 필드만 적어도 나머지가 살아 있어야 한다."""
    import tempfile
    src = ("crate_count: 40\nbatch_system_id: B3W\n"
           "breeding: {lactation_days: 28}\n"
           "stages:\n  - {id: FINISHER, downtime_days: 10}\n")
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False,
                                     encoding="utf-8") as f:
        f.write(src)
        p = f.name
    try:
        c = load_config(p)
    finally:
        os.unlink(p)
    fin = c.stage("FINISHER")
    assert fin.downtime_days == 10
    assert fin.duration_days == 55          # 지워지지 않았다
    assert fin.space_m2_per_head == 0.80
    assert c.crate_count == 40 and c.batch_system_id == "B3W"
    assert c.breeding.lactation_days == 28
    assert c.breeding.gestation_days == 114
    assert c.breeding.cycle_days == 147


def test_merged_wean_to_finish() -> None:
    """wean-to-finish 통합 — 이동이 사라지고 점유일이 합쳐진다."""
    c = _cfg()
    c.merge_stages = ["NURSERY_1", "NURSERY_2", "GROWER", "FINISHER"]
    m = c.merged()
    ids = [s.id for s in m.flow_stages]
    assert len(ids) == 2 and ids[0] == "SUCKLING"
    combo = m.flow_stages[1]
    assert combo.duration_days == 21 + 25 + 50 + 55
    assert combo.space_m2_per_head == 0.80          # 가장 큰 값
    assert combo.downtime_days == 7                 # 마지막 단계의 공백기만
    assert m.market_age_days == 175                 # 총 일령은 그대로
    assert m.merged() is m or m.merged().merge_stages == []


def test_with_batch_system_does_not_mutate() -> None:
    c = _cfg()
    other = c.with_batch_system("B3W")
    assert other.batch_system_id == "B3W"
    assert c.batch_system_id == "WEEKLY"


# -- what-if (요구사항 5) ---------------------------------------------------
def test_whatif_monotonic() -> None:
    """간격이 길수록 모돈규모·총돈방은 줄어야 한다."""
    rows = calc.compare_systems(_cfg())
    assert [r["system"] for r in rows] == ["WEEKLY", "B2W", "B3W", "B4W", "B5W"]
    sows = [r["sow_inventory"] for r in rows]
    rooms = [r["total_rooms"] for r in rows]
    assert sows == sorted(sows, reverse=True), sows
    assert rooms == sorted(rooms, reverse=True), rooms
    # 배치당 교배·이유 두수는 분만틀 수만의 함수라 간격에 무관하다
    assert len({r["services_per_batch"] for r in rows}) == 1
    assert len({r["weaned_per_batch"] for r in rows}) == 1


# -- 검증 규칙 §8 -----------------------------------------------------------
def test_v1_density() -> None:
    c = _cfg()
    b = Batch("B1", date(2026, 1, 1), date(2026, 1, 1), date(2026, 1, 25),
              Stage.FINISHER, 100)
    tight = Room("X", "finisher", 100, 79.0)     # 0.79㎡/두 < 0.80
    ok = Room("Y", "finisher", 100, 80.0)
    assert len(validate.check_density(c, tight, b, date(2026, 6, 1))) == 1
    assert validate.check_density(c, ok, b, date(2026, 6, 1)) == []


def test_v2_bottleneck_house_level() -> None:
    """nursery 처럼 두 스테이지가 한 돈사를 쓰면 필요 수를 합쳐 말해야 한다."""
    c = _cfg()
    rooms = [Room(f"N{i}", "nursery", 200, 60.0) for i in range(5)]
    assert validate.check_bottleneck(c, "NURSERY_2", 0, 1) == []   # 1회는 무시
    f = validate.check_bottleneck(c, "NURSERY_2", 0, 2, rooms=rooms)[0]
    # N1(4방) + N2(5방) = 9 를 말해야지 N2 의 5 만 말하면 안 된다
    assert "필요 돈방 9" in f.message, f.message
    assert "보유 5" in f.message, f.message
    assert f.level == validate.ERROR and f.check == "V2"


def test_v3_aiao_two_batches_one_room() -> None:
    c = _cfg()
    r = [Room("G1", "grower", 200, 100.0)]
    bs = [Batch("A", date(2026, 1, 1), date(2026, 1, 1), date(2026, 1, 25),
                Stage.GROWER, 100, room_id="G1"),
          Batch("B", date(2026, 1, 8), date(2026, 1, 8), date(2026, 2, 1),
                Stage.GROWER, 100, room_id="G1")]
    out = validate.check_aiao(c, r, bs)
    assert any("연속사육" in f.message and "G1" in f.message for f in out)


def test_v3_zero_downtime_is_error() -> None:
    c = _cfg()
    c.stage("GROWER").downtime_days = 0
    out = validate.check_aiao(c, [], [])
    assert any(f.check == "V3" and "공백기 0일" in f.message for f in out)


def test_v4_market_delay_grace() -> None:
    from datetime import timedelta
    c = _cfg()
    b = Batch("B1", date(2025, 9, 1), date(2025, 9, 1), date(2025, 9, 25),
              Stage.FINISHER, 100)
    # 목표 175일령 + 유예 14일 = 189일까지는 정상, 190일부터 지연
    assert validate.check_market_delay(
        c, b, b.farrow_date + timedelta(days=189)) == []
    assert len(validate.check_market_delay(
        c, b, b.farrow_date + timedelta(days=190))) == 1


def test_v5_performance_thresholds() -> None:
    assert validate.check_performance(0.10, 0.05) == []
    assert len(validate.check_performance(0.15, 0.05)) == 1
    assert len(validate.check_performance(0.15, 0.10)) == 2


def test_v6_backflow() -> None:
    from pigflow.models import MoveEvent
    good = MoveEvent(date(2026, 1, 1), "A", Stage.NURSERY_1, Stage.NURSERY_2,
                     100, 2, "N1", "N2")
    bad = MoveEvent(date(2026, 1, 1), "B", Stage.GROWER, Stage.NURSERY_2,
                    100, 2, "G1", "N2")
    assert validate.check_backflow([good]) == []
    out = validate.check_backflow([good, bad])
    assert len(out) == 1 and out[0].check == "V6"
    assert stage_index(Stage.SHIPPED) > stage_index(Stage.FINISHER)


# -- 시뮬레이터 §7 ----------------------------------------------------------
def test_room_sizing_prevents_false_density_alarms() -> None:
    """돈방 배정은 house 가 아니라 **면적 요건**으로 골라야 한다.

    house 만 보면 NURSERY_1 용 좁은 방(0.25㎡)에 NURSERY_2 배치(0.35㎡)가
    들어가 과밀 경고가 쏟아진다(실제로 999건 났다). 회귀 방지.
    """
    c = _cfg()
    sim = Simulator(c, date(2026, 1, 1)).run(400)
    dens = [f for f in sim.findings if f.check == "V1"]
    assert dens == [], f"과밀 경고 {len(dens)}건: {dens[0].message if dens else ''}"


def test_simulator_clean_run_when_built_to_spec() -> None:
    """소요량대로 지으면 병목도 역류도 없어야 한다."""
    sim = Simulator(_cfg(), date(2026, 1, 1)).run(400)
    assert len(sim.rooms) == 32              # 5+4+5+9+9
    assert sim.shipped, "출하된 배치가 없다"
    assert validate.summarize(sim.findings)["n"] == 0, \
        [f.message for f in sim.findings[:3]]
    # 모든 이동은 단방향
    for e in sim.events:
        assert stage_index(e.to_stage) > stage_index(e.from_stage)


def test_simulator_aiao_one_batch_per_room() -> None:
    """RULE T4 — 어느 시점에도 한 방에 두 배치가 있으면 안 된다."""
    sim = Simulator(_cfg(), date(2026, 1, 1)).run(400)
    live = {}
    for b in sim.batches:
        if b.room_id and b.stage != Stage.SHIPPED:
            live.setdefault(b.room_id, []).append(b.batch_id)
    assert all(len(v) == 1 for v in live.values()), live


def test_simulator_washing_gap_respected() -> None:
    """RULE T5 — 전출 후 공백기 안에는 다음 배치가 못 들어간다."""
    sim = Simulator(_cfg(), date(2026, 1, 1)).run(200)
    # 방별 (전출일, 입식일) 쌍을 이벤트에서 뽑는다
    out_at, ins = {}, []
    for e in sorted(sim.events, key=lambda x: x.date):
        if e.from_room:
            out_at[e.from_room] = (e.date, e.from_stage)
        if e.to_room and e.to_room in out_at:
            ins.append((e.to_room, out_at[e.to_room], e.date))
    assert ins, "재사용된 방이 없다 — 기간을 늘려야 한다"
    for rid, (left, from_stage), came in ins:
        dt = sim.cfg.stage(from_stage.value).downtime_days
        assert (came - left).days >= dt, \
            f"{rid}: 공백 {(came - left).days}일 < {dt}일"


def test_bottleneck_detected_when_short_one_room() -> None:
    """비육사를 한 방 줄이면 그 스테이지가 병목으로 잡혀야 한다."""
    c = _cfg()
    rooms = [r for r in build_rooms(c) if r.room_id != "FINISHER-9"]
    assert len(rooms) == 31
    sim = Simulator(c, date(2026, 1, 1), rooms=rooms).run(400)
    bn = {b["stage"] for b in report.bottlenecks(sim)}
    assert "FINISHER" in bn, bn
    msg = next(f.message for f in sim.findings if f.check == "V2")
    assert "필요 돈방 9" in msg and "보유 8" in msg, msg


def test_warmup_excluded_from_steady_state() -> None:
    sim = Simulator(_cfg(), date(2026, 1, 1)).run(300)
    assert sim.warmup_days == 175
    assert len(sim.steady_events()) < len(sim.events)
    assert all(o["date"] >= sim.start.replace(day=1) for o in
               sim.steady_occupancy())
    assert len(sim.steady_occupancy()) == 300 - 175


def test_room_available_from_semantics() -> None:
    r = Room("X", "nursery", 100, 40.0, state=RoomState.WASHING,
             available_from=date(2026, 3, 10))
    assert not r.is_available(date(2026, 3, 9))
    assert r.is_available(date(2026, 3, 10))
    r.state = RoomState.OCCUPIED
    assert not r.is_available(date(2026, 3, 20))


# -- 리포트 §9 --------------------------------------------------------------
def test_kpi_cohort_consistency() -> None:
    """이유후 생존율은 설정 폐사율의 곱과 일치해야 한다.

    이유 이벤트와 출하 이벤트를 각각 창 안에서 합산하면 서로 다른 배치를
    비교하게 되어 97.1% 같은 값이 나온다. 동일 코호트로 세는지 확인.
    """
    c = _cfg()
    sim = Simulator(c, date(2026, 1, 1)).run(500)
    k = report.kpi_report(sim)
    expect = 1.0
    for s in c.flow_stages[1:]:
        expect *= (1.0 - s.mortality)
    assert abs(k["post_wean_survival"] - expect) < 0.01, \
        f"{k['post_wean_survival']} vs 설정 {expect:.3f}"
    assert k["msy"] < k["psy"], "MSY 가 PSY 보다 클 수 없다"
    assert 0.0 < k["room_utilization"] <= 1.0
    assert k["npd_floor_days"] == c.breeding.wean_to_service_days


def test_rooms_table_house_level_shortage() -> None:
    """nursery 는 두 스테이지가 나눠 쓰므로 부족분을 돈사 단위로 봐야 한다."""
    c = _cfg()
    rooms = [r for r in build_rooms(c) if not r.room_id.startswith("NURSERY_1")]
    rt = {r["stage"]: r for r in report.rooms_table(c, rooms)}
    assert rt["NURSERY_1"]["house_required"] == 9      # 4 + 5
    assert rt["NURSERY_1"]["house_have"] == 5
    assert rt["NURSERY_1"]["shortage"] == 4
    assert rt["NURSERY_2"]["shortage"] == 4            # 같은 돈사 → 같은 부족
    assert rt["GROWER"]["shortage"] == 0


def test_gantt_renders() -> None:
    sim = Simulator(_cfg(), date(2026, 1, 1)).run(250)
    g = report.gantt(sim, house="finisher", width=40)
    lines = g.splitlines()
    assert len(lines) == 1 + 9                    # 헤더 + 비육사 9방
    assert any("▓" in ln for ln in lines[1:]), g
    assert any("░" in ln for ln in lines[1:]), "세척 구간이 안 보인다"


def test_demo_main_runs() -> None:
    """`python -m pigflow` 가 예외 없이 끝나는지."""
    import contextlib
    import io
    from pigflow.__main__ import main
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = main(["--days", "220"])
    out = buf.getvalue()
    assert rc == 0
    for token in ("필요 돈방", "KPI", "what-if", "PSY"):
        assert token in out, f"'{token}' 이 출력에 없다"


def test_example_yaml_reproduces_finisher_bottleneck() -> None:
    """동봉한 예시 농장은 비육사 1방 부족이 유일한 병목이어야 한다."""
    p = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "example_farm.yaml")
    c = load_config(p).merged()
    rt = {r["stage"]: r for r in report.rooms_table(c, build_rooms(c))}
    assert rt["FINISHER"]["shortage"] == 1
    assert all(rt[s]["shortage"] == 0 for s in
               ("SUCKLING", "NURSERY_1", "NURSERY_2", "GROWER"))
    sim = Simulator(c, date(2026, 1, 1)).run(400)
    assert {b["stage"] for b in report.bottlenecks(sim)} == {"FINISHER"}


TESTS = [v for k, v in sorted(globals().items()) if k.startswith("test_")]


def main() -> int:
    failed = 0
    for t in TESTS:
        try:
            t()
            print(f"  PASS  {t.__name__}")
        except Exception as e:                                    # noqa: BLE001
            failed += 1
            print(f"  FAIL  {t.__name__}: {e}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
