"""돈군흐름 데모 — 명세 요구사항 4·5.

    cd competition                        # 또는 PYTHONPATH=competition
    python -m pigflow                     # 기본값(분만틀 10, 주간배치)
    python -m pigflow --config farm.yaml  # 농장 설정
    python -m pigflow --gantt farrowing   # 특정 돈사 점유 간트

출력:
  1) 설계 요약        분만틀 → 교배두수 · 모돈규모 · 배치당 두수
  2) 필요 vs 보유 돈방  (요구사항 4)
  3) 시뮬레이션 병목    (요구사항 4)
  4) KPI              (명세 §9)
  5) what-if 비교      (요구사항 5)
"""
from __future__ import annotations

import argparse
from datetime import date

from . import calc, report, validate
from .config import load_config
from .simulator import Simulator, build_rooms


def _tbl(rows: list, cols: list) -> str:
    """헤더·구분선 있는 고정폭 표. 한글은 2칸을 먹으므로 폭을 따로 센다."""
    def w(s):
        return sum(2 if ord(c) > 0x1100 else 1 for c in str(s))

    def pad(s, n, right=False):
        gap = " " * max(0, n - w(s))
        return gap + str(s) if right else str(s) + gap

    keys = [c[0] for c in cols]
    heads = [c[1] for c in cols]
    right = [len(c) > 2 and c[2] == ">" for c in cols]
    body = [[("" if r.get(k) is None else str(r.get(k))) for k in keys]
            for r in rows]
    widths = [max(w(h), *(w(b[i]) for b in body)) if body else w(h)
              for i, h in enumerate(heads)]
    out = ["  " + "  ".join(pad(h, widths[i], right[i])
                            for i, h in enumerate(heads)),
           "  " + "  ".join("-" * widths[i] for i in range(len(heads)))]
    for b in body:
        out.append("  " + "  ".join(pad(v, widths[i], right[i])
                                    for i, v in enumerate(b)))
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="pigflow", description="돈군흐름 설계·검증")
    ap.add_argument("--config", help="농장 YAML (없으면 기본값)")
    ap.add_argument("--crates", type=int, help="분만틀 수 (YAML 보다 우선)")
    ap.add_argument("--system", help="배치 시스템 WEEKLY/B2W/B3W/B4W/B5W")
    ap.add_argument("--days", type=int, default=400, help="시뮬레이션 일수")
    ap.add_argument("--gantt", nargs="?", const="", help="돈방 점유 간트(돈사명)")
    a = ap.parse_args(argv)

    cfg = load_config(a.config)
    if a.crates:
        cfg.crate_count = a.crates
    if a.system:
        cfg.batch_system_id = a.system
    cfg = cfg.merged()

    p = calc.plan(cfg)
    print("=" * 78)
    print(f"  돈군흐름 설계 — 분만틀 {cfg.crate_count}개 · "
          f"{p['batch_system']}({p['interval_weeks']}주 간격)")
    print("=" * 78)
    print(f"  배치당 교배      {p['services_per_batch']:>6} 두 "
          f"(분만율 {cfg.breeding.farrowing_rate:.0%} 역산)")
    print(f"  배치당 후보돈    {p['gilts_per_batch']:>6} 두")
    print(f"  번식돈군 규모    {p['sow_inventory']:>6} 두")
    print(f"  배치당 이유      {p['weaned_per_batch']:>6} 두")
    print(f"  배치당 출하      {p['shipped_per_batch']:>6} 두 "
          f"({p['liveweight_per_batch_kg']:,.0f} kg)")
    print(f"  배치 수          {p['groups_required']:>6} 군 "
          f"(관행표 {p['groups_table']}군)")
    print(f"  번식주기         {p['cycle_days']:>6} 일 · "
          f"출하일령 {p['market_age_days']}일")

    # -- 2) 필요 vs 보유 -----------------------------------------------------
    rooms = build_rooms(cfg)
    has_inventory = bool(cfg.rooms)
    rt = report.rooms_table(cfg, rooms)
    print("\n" + "-" * 78)
    print("  ① 스테이지별 필요 돈방 vs 보유 돈방")
    print("-" * 78)
    cols = [("name_ko", "스테이지"), ("house", "돈사"),
            ("occupancy_days", "점유일", ">"), ("rooms_required", "필요방", ">"),
            ("house_have", "보유방", ">"), ("shortage", "부족", ">"),
            ("slack_days", "설계여유", ">"), ("head_per_room", "방당두수", ">"),
            ("area_per_room_m2", "방면적㎡", ">")]
    print(_tbl(rt, cols))
    print("  * 설계여유 = 필요방 × 간격 − 점유일. 필요방만 지었을 때의 여유이며, "
          "보유방이 더 많으면 실제 여유는 그만큼 늘어난다.")
    if not has_inventory:
        print("  * 보유 돈방 미입력 → 소요량대로 지은 것으로 가정(부족 0). "
              "YAML 의 rooms: 에 실제 돈방을 넣으면 부족분이 나온다.")
    # 보유방이 남는 돈사는 실제 여유가 있으므로 경고하지 않는다
    tight = [r for r in rt
             if r["slack_days"] < 1.0 and r["house_have"] <= r["house_required"]]
    if tight:
        print("  ! 여유 1일 미만: " + ", ".join(
            f"{r['name_ko']}({r['slack_days']}일)" for r in tight)
            + " — 세척이 하루만 밀려도 AIAO 가 깨진다.")

    # -- 3) 시뮬레이션 -------------------------------------------------------
    sim = Simulator(cfg, date(2026, 1, 1), rooms=rooms).run(a.days)
    s = validate.summarize(sim.findings)
    print("\n" + "-" * 78)
    print(f"  ② 시뮬레이션 {a.days}일 (warm-up {sim.warmup_days}일 제외)")
    print("-" * 78)
    print(f"  이동 이벤트 {len(sim.events)}건 · 출하 배치 {len(sim.shipped)}개 · "
          f"돈방 {len(sim.rooms)}개")
    print(f"  검증 결과   오류 {s['errors']}건 · 경고 {s['warnings']}건"
          + (f" {s['by_check']}" if s["n"] else ""))
    bn = report.bottlenecks(sim)
    if bn:
        print("  병목 위치:")
        print(_tbl([{"stage": b["stage"], "events": b["events"]} for b in bn],
                   [("stage", "스테이지"), ("events", "발생", ">")]))
    else:
        print("  병목 없음 — 모든 배치가 제 일령에 다음 돈방으로 이동했다.")
    # 같은 문장이 수십 번 반복되므로 중복을 접고 건수만 붙인다
    seen = {}
    for f in sim.findings:
        seen[(f.level, f.check, f.message)] = seen.get(
            (f.level, f.check, f.message), 0) + 1
    for (lvl, chk, msg), n in sorted(seen.items(), key=lambda x: -x[1])[:6]:
        print(f"    [{lvl}/{chk}] {msg}" + (f"  ×{n}" if n > 1 else ""))
    if len(seen) > 6:
        print(f"    ... 외 {len(seen) - 6}종")

    # -- 4) KPI --------------------------------------------------------------
    k = report.kpi_report(sim)
    print("\n" + "-" * 78)
    print("  ③ KPI (명세 §9)")
    print("-" * 78)
    bm = k["benchmark"]
    print(f"  PSY {k['psy']:>6}   (평균 {bm['floor']['psy']} · "
          f"상위 {bm['target']['psy']})")
    print(f"  MSY {k['msy']:>6}   (평균 {bm['floor']['msy']} · "
          f"상위 {bm['target']['msy']})")
    print(f"  이유후 생존 {k['post_wean_survival']:>6.1%}  "
          f"(이유 {k['weaned_total']}두 → 출하 {k['shipped_total']}두, "
          f"출하배치 {k['batches_shipped']}개 · 동일 코호트)")
    print(f"  모돈회전율 {k['sow_turnover']:>5} (이론) vs "
          f"{k['sow_turnover_config']} (설정) · "
          f"이론 최소 NPD {k['npd_floor_days']}일")
    print(f"  돈방 가동률 {k['room_utilization']:.1%}  "
          f"(평균 모돈 {k['avg_sows']}두 · 정상구간 {k['days_steady']}일)")
    print("  * PSY/MSY 는 모든 배치가 분만틀을 채운다는 설계 가정의 상한이다. "
          "재발정·유산 손실은 분만율(설정 "
          f"{cfg.breeding.farrowing_rate:.0%})로만 반영된다.")

    # -- 5) what-if ----------------------------------------------------------
    print("\n" + "-" * 78)
    print("  ④ 배치 시스템 what-if — 같은 분만틀로 무엇이 달라지나")
    print("-" * 78)
    wf = []
    for r in report.whatif_table(cfg):
        row = {"system": r["system"], "iv": f"{r['interval_weeks']}주",
               "groups": r["groups"], "svc": r["services_per_batch"],
               "sows": r["sow_inventory"], "weaned": r["weaned_per_batch"],
               "total": r["total_rooms"], "slack": r["min_slack"]}
        row.update({k2: v for k2, v in r["rooms"].items()})
        wf.append(row)
    stage_cols = [(s.id, s.name_ko, ">") for s in cfg.flow_stages]
    print(_tbl(wf, [("system", "시스템"), ("iv", "간격"), ("groups", "배치수", ">"),
                    ("svc", "배치당교배", ">"), ("sows", "모돈규모", ">"),
                    ("weaned", "배치당이유", ">")] + stage_cols
               + [("total", "총돈방", ">"), ("slack", "최소여유", ">")]))
    print("  * 간격이 길수록 배치당 두수는 커지고 필요 돈방 수는 줄지만, "
          "한 배치가 어긋났을 때의 손실도 그만큼 커진다.")

    if a.gantt is not None:
        print("\n" + "-" * 78)
        print(f"  ⑤ 돈방 점유 간트  ▓재실 ░세척 ·빈방"
              + (f" — {a.gantt}" if a.gantt else ""))
        print("-" * 78)
        print(report.gantt(sim, house=a.gantt or None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
