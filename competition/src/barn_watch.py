"""배치 전이 감시 — **다음 배치로 넘어갈 때마다** 돈사 현황을 찍고 검사한다.

`run_farm` ② 는 400일을 돌린 뒤 "오류 n 건" 만 말한다. 그러면 **언제 어디서**
틀어졌는지를 모른다. 등록 화면의 `분만사 −20` 도 정적 부족분이라 "며칠째에
무슨 일로 터지는지" 는 못 낸다. 이 모듈이 그 사이를 메운다.

    이동이 일어난 날마다 → 그 직후 방 상태 전부 + 직전 대비 변화 + 그 자리에서 검사

## 검사 여섯 가지

  AIAO      한 방에 두 배치가 들어갔나 (RULE T4)
  역류      단계 인덱스가 줄었나 (RULE T6)
  세척생략  전출 후 공백기를 안 채우고 입식했나 (RULE T5)
  과밀      수용두수·두당 면적을 넘겼나
  적체      나갈 나이가 됐는데 방이 없어 못 나간 배치
  유휴      쓰지 않고 비어 있는 방

앞 셋은 시뮬레이터가 **만들지 않도록 짜여 있다.** 그래도 검사한다 — 규칙이
코드에 있다는 것과 결과에 지켜졌다는 것은 다른 말이고, 그 둘을 잇는 게
이 파일이다. 0 건이 나오는 것이 정상이고, 0 이 아니면 규칙이 깨진 것이다.

## 워밍업을 판정하지 않는다

파이프라인이 채워지기 전에는 뒷단이 텅 비어 있다. 그 구간의 유휴·적체를
그대로 세면 설비가 남아도는 것처럼 보인다. `Simulator.warmup_days()` 이전
전이는 `warmup=True` 로 표시하고 집계에서 뺀다.

    python competition/src/barn_watch.py --sows 300
    python competition/src/barn_watch.py --setup my_farm.json     # 등록 화면 JSON
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

from pigflow import calc                                        # noqa: E402
from pigflow.config import default_config                       # noqa: E402
from pigflow.models import RoomState, stage_index               # noqa: E402
from pigflow.simulator import Simulator, build_rooms            # noqa: E402

DEFAULT_DAYS = 400
DEFAULT_START = date(2026, 1, 1)

# 등록 화면 축사 용도 → pigflow house.
#
# **1:1 이 아니다.** `farm_registry` 의 비육사는 정의가 "육성·비육돈" 이라
# pigflow 의 grower 와 finisher 둘을 겸한다. 하나로만 보내면 나머지 house 에
# 방이 0 개가 되어 모든 배치가 거기서 멈추고, 그 적체는 농장 문제가 아니라
# 매핑 문제다. 그래서 겸하는 동은 **머무는 일수 비율로 방을 나눈다** —
# 정상 상태에서 단계별 자리 수는 체류 일수에 비례하므로 유도되는 값이다.
#
# 등록 화면이 **육성사를 따로 받으면** 겸용 가정을 쓰면 안 된다. 그때는
# 비육사가 finisher 만 맡는다 — 안 그러면 grower 방이 두 번 세어진다.
#
# 교배사·임신사·후보사는 **번식돈** 자리라 돈군흐름(자돈~비육) 밖이다.
# 억지로 대응시키면 자돈이 임신사로 가는 그림이 나온다.
HOUSE_OF = {"분만사": ["farrowing"], "자돈사": ["nursery"],
            "육성사": ["grower"], "비육사": ["grower", "finisher"]}
HOUSE_OF_SPLIT = {**HOUSE_OF, "비육사": ["finisher"]}
BREEDING_ONLY = ("교배사", "임신사", "후보사")


def _split(n_rooms: int, houses: list, cfg) -> list:
    """방 n 개를 house 들에 체류 일수 비율로 나눈다. 최소 1개씩은 준다."""
    if len(houses) == 1:
        return [(houses[0], n_rooms)]
    dur = {h: sum(s.duration_days for s in cfg.flow_stages if s.house == h)
           for h in houses}
    tot = sum(dur.values()) or 1
    got = {h: max(1, int(round(n_rooms * dur[h] / tot))) for h in houses}
    # 반올림으로 총합이 어긋나면 가장 오래 머무는 쪽에서 조정한다
    big = max(houses, key=lambda h: dur[h])
    got[big] += n_rooms - sum(got.values())
    return [(h, n) for h, n in got.items() if n > 0]


def crates_from_setup(setup: dict) -> int:
    """등록한 분만사의 **방당 분만틀 수**. 없으면 0.

    **총수가 아니다.** pigflow 의 `crate_count` 는 한 배치가 쓰는 분만틀,
    즉 방 하나의 크기다(AIAO 는 방 하나가 배치 하나를 통째로 받는다).
    총수를 넣으면 배치가 방 수만큼 부풀어 어느 방에도 안 들어간다.

    방 크기가 제각각이면 **가장 큰 방**을 쓴다. 작은 방은 배치가 안 들어가
    죽은 자리가 되는데, 그건 `feasibility()` 가 따로 보고한다.
    """
    return max((max(1, int(b.get("per") or 1))
                for b in (setup.get("barns") or [])
                if b.get("stage") == "분만사"), default=0)


def batch_system_from_setup(setup: dict, cfg) -> tuple:
    """등록한 배치 간격 → pigflow 배치 체계 id.

    이걸 안 맞추면 등록 화면에서 3주를 골라도 시뮬레이터는 주간으로 돌아
    배치 크기가 3배 어긋난다.
    """
    iv = setup.get("interval_days")
    if not iv:
        return None, None
    want = float(iv) / 7.0
    for b in cfg.batch_systems:
        if abs(b.interval_weeks - want) < 1e-6:
            return b.id, None
    have = " · ".join(f"{b.interval_weeks:g}주" for b in cfg.batch_systems)
    return None, (f"등록 간격 {iv:g}일에 맞는 배치 체계가 없다 "
                  f"(가능: {have}) — 기본 {cfg.batch_system_id} 로 돌린다")


def rooms_from_setup(setup: dict, cfg) -> tuple:
    """등록 화면 JSON → pigflow 돈방 목록.

    돌려주는 둘째 값은 **버리거나 나눈 동**이다. 조용히 처리하면 사용자는
    자기가 등록한 축사가 그대로 반영된 줄 안다. 무엇을 왜 그랬는지 같이 준다.

    ## 분만사는 단위가 다르다

    등록 화면의 '방당 자리' 는 분만사에서 **분만틀 수**(모돈 자리)인데
    pigflow 의 farrowing 방 수용력은 **포유자돈 두수**다. 그대로 넘기면
    방이 배치보다 12배쯤 작아 배치가 한 발짝도 못 가고, 그러면 전이가
    0 회라 집계가 **전부 0 건 = 위반 없음** 으로 보인다. `feasibility()` 를
    넣게 만든 바로 그 실패라, 여기서 복당 산자수를 곱해 맞춘다.
    """
    rooms, notes = [], []
    # 복당 총산 = 이유두수 ÷ (1 − 포유 폐사)
    per_litter = (cfg.breeding.weaned_per_litter
                  / max(1e-9, 1.0 - cfg.flow_stages[0].mortality))
    barns = setup.get("barns") or []
    # 육성사를 따로 등록했으면 비육사는 겸용이 아니다
    table = HOUSE_OF_SPLIT if any(b.get("stage") == "육성사" for b in barns) \
        else HOUSE_OF
    for b in barns:
        stage = b.get("stage")
        houses = table.get(stage)
        if not houses:
            notes.append((b.get("name", "?"), stage,
                          "번식돈 자리 — 돈군흐름(자돈~비육) 밖이라 뺀다"
                          if stage in BREEDING_ONLY else "대응하는 house 없음"))
            continue
        n_rooms = max(1, int(b.get("rooms") or 1))
        per = max(1, int(b.get("per") or 1))
        parts = _split(n_rooms, houses, cfg)
        if len(parts) > 1:
            notes.append((b.get("name", "?"), stage,
                          "육성·비육을 겸하는 동 → 체류 일수 비율로 "
                          + " · ".join(f"{h} {n}방" for h, n in parts)))
        # 면적은 등록 화면이 **받으면 그걸 쓰고**, 비었으면 두수 × 그 house 의
        # 두당 면적으로 역산한다. 역산값은 정의상 법정면적을 딱 맞추므로
        # 밀사가 절대 안 잡힌다 — 그래서 입력값이 있으면 반드시 그쪽이다.
        area_in = b.get("area_m2")
        for house, n in parts:
            need = max((s.space_m2_per_head for s in cfg.flow_stages
                        if s.house == house), default=0.4)
            head = int(round(per * per_litter)) if house == "farrowing" else per
            if house == "farrowing":
                notes.append((b.get("name", "?"), stage,
                              f"분만틀 {per}개 → 포유자돈 {head}두로 환산 "
                              f"(복당 총산 {per_litter:.1f}두)"))
            area = float(area_in) if area_in else round(head * need, 1)
            for i in range(n):
                rooms.append({"room_id": f"{b.get('name', house)}-{house[:2]}{i + 1}",
                              "house": house, "capacity_head": head,
                              "area_m2": area})
    return rooms, notes


def room_view(sim) -> list:
    """지금 이 순간의 방 상태 전부."""
    out = []
    for r in sim.rooms:
        bt = next((b for b in sim.batches
                   if b.batch_id == r.current_batch_id), None)
        out.append({"room_id": r.room_id, "house": r.house,
                    "state": r.state.value,
                    "batch": r.current_batch_id,
                    "head": int(bt.head_count) if bt else 0,
                    "capacity": int(r.capacity_head),
                    "area_m2": float(r.area_m2),
                    "free_on": r.available_from.isoformat()
                    if r.available_from else None})
    return out


def _diff(prev: list, cur: list) -> list:
    """직전 전이 대비 무엇이 바뀌었나. 안 바뀐 방은 말하지 않는다."""
    if prev is None:
        return []
    was = {r["room_id"]: r for r in prev}
    out = []
    for r in cur:
        o = was.get(r["room_id"])
        if o is None:
            out.append({"room_id": r["room_id"], "kind": "신규", "to": r["state"]})
            continue
        if o["state"] != r["state"]:
            out.append({"room_id": r["room_id"], "kind": "상태",
                        "from": o["state"], "to": r["state"],
                        "batch": r["batch"] or o["batch"]})
        elif o["head"] != r["head"]:
            out.append({"room_id": r["room_id"], "kind": "두수",
                        "from": o["head"], "to": r["head"],
                        "batch": r["batch"]})
    return out


def inspect(sim, on, moves, cur, prev) -> list:
    """그 자리에서의 검사 여섯 가지. 규칙 위반은 코드가 아니라 결과로 잡는다."""
    cfg = sim.cfg
    issues = []

    # 1) AIAO — 한 방에 두 배치. current_batch_id 로는 못 잡는다(덮어써진다).
    #    배치가 들고 있는 room_id 로 세야 실제 동거가 보인다.
    seen: dict = {}
    for b in sim.batches:
        if b.room_id and b.stage.value != "SHIPPED":
            seen.setdefault(b.room_id, []).append(b.batch_id)
    for rid, ids in seen.items():
        if len(ids) > 1:
            issues.append({"code": "AIAO", "room": rid,
                           "msg": f"한 방에 배치 {len(ids)}개: {', '.join(ids)}"})

    # 2) 역류 — 단계 인덱스가 줄면 어린 배치가 병원체에 노출된다
    for e in moves:
        if stage_index(e.to_stage) <= stage_index(e.from_stage):
            issues.append({"code": "역류", "batch": e.batch_id,
                           "msg": f"{e.from_stage.value} → {e.to_stage.value}"})

    # 3) 세척 생략 — 전출한 방에 공백기를 안 채우고 입식했나
    was = {r["room_id"]: r for r in (prev or [])}
    for e in moves:
        if not e.to_room:
            continue
        o = was.get(e.to_room)
        if o and o["free_on"] and date.fromisoformat(o["free_on"]) > on:
            issues.append({"code": "세척생략", "room": e.to_room,
                           "msg": f"{o['free_on']} 까지 세척인데 {on} 입식"})

    # 4) 과밀 — 수용두수 초과 또는 두당 면적 미달
    for b in sim.batches:
        if not b.room_id or b.stage.value == "SHIPPED":
            continue
        r = next((x for x in cur if x["room_id"] == b.room_id), None)
        if not r:
            continue
        need = cfg.stage(b.stage.value).space_m2_per_head
        if r["capacity"] and b.head_count > r["capacity"]:
            issues.append({"code": "과밀", "room": r["room_id"],
                           "msg": f"{b.head_count}두 > 수용 {r['capacity']}두"})
        elif need > 0 and r["area_m2"] / max(1, b.head_count) < need - 1e-9:
            issues.append({"code": "과밀", "room": r["room_id"],
                           "msg": f"두당 {r['area_m2'] / b.head_count:.2f}㎡ "
                                  f"< 기준 {need}㎡"})

    # 5) 적체 — 나갈 나이가 지났는데 아직 그 자리에 있는 배치.
    #    **이게 '분만사 −20' 이 실제로 터지는 모습**이다.
    for b in sim.batches:
        if b.stage.value == "SHIPPED":
            continue
        s = cfg.stage(b.stage.value)
        if s.exit_age_days is None:
            continue
        over = b.age_days(on) - s.exit_age_days
        if over > 0:
            issues.append({"code": "적체", "batch": b.batch_id,
                           "room": b.room_id, "over_days": int(over),
                           "msg": f"{s.name_ko} 에서 {over}일 초과 — "
                                  f"다음 방이 안 비었다"})

    # 6) 무처소 — **방을 못 받았는데 흐름은 계속 가는 배치.**
    #    분만사가 모자라면 이렇게 나타난다. 시뮬레이터는 자리가 없어도 배치를
    #    만들고(돼지는 방이 없어도 태어난다) 나이가 차면 다음 단계로 보낸다.
    #    그래서 분만사 부족은 '적체' 로 안 잡히고 여기서만 보인다 — 실제로
    #    분만사를 5방에서 1방으로 줄여도 적체가 0 회였다.
    for b in sim.batches:
        if b.stage.value != "SHIPPED" and b.room_id is None:
            issues.append({"code": "무처소", "batch": b.batch_id,
                           "msg": f"{cfg.stage(b.stage.value).name_ko} "
                                  f"{b.head_count}두가 방 없이 있다"})

    # 7) 유휴 — 쓰지 않고 비어 있는 방(경보가 아니라 정보)
    idle = [r["room_id"] for r in cur if r["state"] == "EMPTY"]
    if idle:
        issues.append({"code": "유휴", "msg": f"빈 방 {len(idle)}개: "
                                              f"{', '.join(idle[:6])}"
                                              + (" …" if len(idle) > 6 else "")})
    return issues


def feasibility(cfg, rooms) -> list:
    """돌리기 **전에** 물리적으로 들어갈 수 있는지 본다.

    방이 배치보다 작으면 그 방은 영원히 안 뽑히고, 배치는 한 발짝도 못 간다.
    그러면 전이가 0 회라 검사할 것도 없고, 집계는 **전부 0 건 = 위반 없음**
    으로 보인다. 실제로 그렇게 나와서 이 함수를 넣었다 — 아무것도 안 움직인
    것을 '문제 없음' 으로 보고하는 게 이 도구의 가장 나쁜 실패다.
    """
    head = calc.weaned_per_batch(cfg.crate_count, cfg.breeding.weaned_per_litter)
    born = head / max(1e-9, 1.0 - cfg.flow_stages[0].mortality)
    out, h = [], born
    for s in cfg.flow_stages:
        pool = [r for r in rooms if r.house == s.house]
        need_area = s.space_m2_per_head * h
        fit = [r for r in pool
               if (not r.capacity_head or r.capacity_head >= h)
               and (s.space_m2_per_head <= 0 or r.area_m2 >= need_area - 1e-9)]
        if not pool:
            out.append({"stage": s.id, "house": s.house, "head": int(h),
                        "msg": f"{s.house} 에 등록된 방이 0개다"})
        elif not fit:
            big = max(pool, key=lambda r: r.capacity_head or 0)
            # 분만사는 두당 면적 기준이 없다(분만틀 수가 제약이다).
            # 그런 단계에 "0㎡ 필요" 라고 쓰면 무슨 말인지 알 수 없다.
            area = (f"·{big.area_m2:.0f}㎡ (두당 {s.space_m2_per_head}㎡ 필요 "
                    f"→ {need_area:.0f}㎡)") if s.space_m2_per_head > 0 else ""
            out.append({"stage": s.id, "house": s.house, "head": int(h),
                        "msg": f"{s.name_ko} 배치 {h:.0f}두가 들어갈 방이 없다 "
                               f"— {s.house} 최대 방이 {big.capacity_head}두{area}"})
        h = h - h * s.mortality
    return out


def watch(cfg=None, start=None, days: int = DEFAULT_DAYS,
          rooms=None) -> dict:
    """전이가 있었던 날마다 스냅샷 + 검사."""
    cfg = (cfg or default_config()).merged()
    start = start or DEFAULT_START
    sim = Simulator(cfg, start, rooms=rooms or build_rooms(cfg))
    warm = sim.warmup_days

    snaps, prev = [], None
    for _ in range(days):
        sim.step()
        on = sim.day - timedelta(days=1)
        moves = [e for e in sim.events if e.date == on]
        if not moves:
            continue
        cur = room_view(sim)
        snap = {
            "date": on.isoformat(), "day": (on - start).days,
            "warmup": (on - start).days < warm,
            "moves": [{"batch": e.batch_id, "from": e.from_stage.value,
                       "to": e.to_stage.value, "head": int(e.head_moved),
                       "dead": int(e.head_dead), "from_room": e.from_room,
                       "to_room": e.to_room} for e in moves],
            "rooms": cur,
            "changed": _diff(prev, cur),
            "issues": inspect(sim, on, moves, cur, prev),
            "occupied": sum(1 for r in cur if r["state"] == "OCCUPIED"),
            "washing": sum(1 for r in cur if r["state"] == "WASHING"),
            "empty": sum(1 for r in cur if r["state"] == "EMPTY"),
            "head": sum(r["head"] for r in cur),
        }
        snaps.append(snap)
        prev = cur

    steady = [s for s in snaps if not s["warmup"]]
    counts: dict = {}
    first: dict = {}
    for s in steady:
        for i in s["issues"]:
            counts[i["code"]] = counts.get(i["code"], 0) + 1
            first.setdefault(i["code"], {"day": s["day"], "date": s["date"],
                                         "msg": i["msg"]})
    jam = max((s for s in steady if any(i["code"] == "적체"
                                        for i in s["issues"])),
              key=lambda s: max(i.get("over_days", 0) for i in s["issues"]),
              default=None)
    blocked = feasibility(cfg, sim.rooms)
    # 배치가 하나도 자리를 못 잡았으면 '위반 0 건' 이 아니라 **흐름 실패**다
    # **갓 태어난 배치를 세면 안 된다.** 마지막 날 근처 배치는 아직 나갈
    #  나이가 아니라 이력이 비어 있는 게 정상이다. 처음엔 그걸 세서 정상
    #  농장에도 '못 움직인 배치 4개' 가 떴다.
    last = sim.day - timedelta(days=1)
    exit0 = cfg.flow_stages[0].exit_age_days or 0
    never = [b.batch_id for b in sim.batches
             if not b.history and b.age_days(last) > exit0]
    # 유휴는 정보라 판정에 안 넣는다. 나머지가 하나라도 있으면 위반이다.
    bad = sum(v for k, v in counts.items() if k != "유휴")
    return {
        "days": days, "warmup_days": warm,
        "n_rooms": len(sim.rooms),
        "feasible": not blocked, "blocked": blocked,
        "n_batches": len(sim.batches), "n_never_moved": len(never),
        "n_violations": int(bad),
        "verdict": ("흐름 실패" if (not steady or blocked)
                    else ("위반 있음" if bad else "정상")),
        "n_transitions": len(snaps), "n_steady": len(steady),
        "counts": counts, "first_seen": first,
        "worst_jam": {"day": jam["day"], "date": jam["date"],
                      "over_days": max(i.get("over_days", 0)
                                       for i in jam["issues"])} if jam else None,
        "utilization": round(
            sum(s["occupied"] for s in steady)
            / max(1, len(steady) * len(sim.rooms)), 3),
        "snapshots": snaps,
    }


def sweep(cfg, days: int = DEFAULT_DAYS) -> list:
    """house 마다 방을 하나씩 빼 보며 **몇 방까지 견디는지** 찾는다.

    등록 화면의 `필요 vs 보유` 는 정적 부족분이라 "지금 모자란다" 까지다.
    이건 "몇 방까지는 버티고, 그 다음 방을 빼면 며칠째에 터진다" 를 낸다 —
    한 방을 더 지을지 말지를 정하는 데 필요한 건 후자다.
    """
    m = cfg.merged()
    base = build_rooms(m)
    houses = sorted({r.house for r in base})
    out = []
    for h in houses:
        ids = [r.room_id for r in base if r.house == h]
        row = {"house": h, "designed": len(ids), "safe": len(ids),
               "break_at": None, "first_day": None, "worst": None}
        for drop in range(1, len(ids) + 1):
            rooms = [r for r in build_rooms(m) if r.room_id not in ids[:drop]]
            r = watch(cfg, days=days, rooms=rooms)
            if r["n_violations"] > 0 or not r["feasible"]:
                row["break_at"] = len(ids) - drop
                row["safe"] = len(ids) - drop + 1
                fs = r["first_seen"].get("적체") or r["first_seen"].get("무처소")
                row["first_day"] = fs["day"] if fs else None
                row["worst"] = (r["worst_jam"] or {}).get("over_days")
                row["codes"] = {k: v for k, v in r["counts"].items() if k != "유휴"}
                break
        out.append(row)
    return out


def _print_sweep(rows: list) -> None:
    print("\n  [여유 확인] house 마다 방을 빼 보며 견디는 한계를 찾는다")
    print(f"    {'house':<10}{'설계':>5}{'안전':>5}{'터짐':>5}  처음 터지는 날 · 무엇이")
    for r in rows:
        if r["break_at"] is None:
            print(f"    {r['house']:<10}{r['designed']:>5}{r['safe']:>5}{'—':>5}  "
                  f"다 빼도 안 터진다(제약이 아니다)")
            continue
        codes = " · ".join(f"{k} {v}회" for k, v in (r.get("codes") or {}).items())
        day = f"{r['first_day']}일째" if r["first_day"] is not None else "즉시"
        print(f"    {r['house']:<10}{r['designed']:>5}{r['safe']:>5}"
              f"{r['break_at']:>5}  {day} · {codes}")


def _print(r: dict, limit: int = 8, show_ok: bool = False) -> None:
    print("=" * 78)
    print(f"  배치 전이 감시 — {r['days']}일 · 돈방 {r['n_rooms']}개 · "
          f"전이 {r['n_transitions']}회")
    print("=" * 78)
    if r["blocked"]:
        print(f"\n  ❌ **돌려 보기 전에 이미 막혔다** — 배치가 들어갈 방이 없다")
        for b in r["blocked"]:
            print(f"     {b['stage']:<10} {b['msg']}")
        print(f"     → 아래 '위반 0 건' 은 지켜져서가 아니라 "
              f"**아무것도 움직이지 않아서**다.")
    print(f"\n  워밍업 {r['warmup_days']}일 (파이프라인이 채워지기 전 "
          f"{r['n_transitions'] - r['n_steady']}회는 판정에서 뺀다)")
    if r["n_never_moved"]:
        print(f"  ⚠ 한 번도 움직이지 못한 배치 {r['n_never_moved']}"
              f"/{r['n_batches']}개")
    print(f"  정상상태 전이 {r['n_steady']}회 · 방 가동률 {r['utilization']:.1%}")

    print(f"\n  판정: **{r['verdict']}**")
    print(f"\n  [검사 집계] 정상상태 기준")
    order = ["AIAO", "역류", "세척생략", "과밀", "적체", "무처소", "유휴"]
    for code in order:
        n = r["counts"].get(code, 0)
        mark = "✅" if (n == 0 and code != "유휴") else ("ℹ️ " if code == "유휴" else "❌")
        fs = r["first_seen"].get(code)
        tail = f" · 처음 {fs['day']}일째({fs['date']}) — {fs['msg']}" if fs and code != "유휴" else ""
        print(f"    {mark} {code:<6}{n:>5}회{tail}")
    if r["worst_jam"]:
        w = r["worst_jam"]
        print(f"\n  ⚠ 가장 심한 적체 — {w['day']}일째({w['date']}) "
              f"{w['over_days']}일 초과")

    shown = [s for s in r["snapshots"]
             if not s["warmup"] and (show_ok or any(
                 i["code"] != "유휴" for i in s["issues"]))]
    if not shown and not show_ok:
        print(f"\n  정상상태 전이에서 규칙 위반 0 건. "
              f"(--all 로 정상 전이도 볼 수 있다)")
        shown = [s for s in r["snapshots"] if not s["warmup"]][:limit]
        print(f"  아래는 참고로 앞 {min(limit, len(shown))}회.")
    for s in shown[:limit]:
        print(f"\n  ── {s['day']:>3}일째 {s['date']}  "
              f"재실 {s['occupied']} · 세척 {s['washing']} · 빈방 {s['empty']} "
              f"· 재사 {s['head']:,}두")
        for m in s["moves"]:
            fr_ = m["from_room"] or "—"
            to = m["to_room"] or "출하"
            print(f"       {m['batch']}  {m['from']:<10} → {m['to']:<10} "
                  f"{m['head']:>5}두 (폐사 {m['dead']})  {fr_} → {to}")
        for c in s["changed"][:6]:
            if c["kind"] == "상태":
                print(f"       · {c['room_id']}  {c['from']} → {c['to']}")
            elif c["kind"] == "두수":
                print(f"       · {c['room_id']}  {c['from']} → {c['to']}두")
        for i in s["issues"]:
            if i["code"] == "유휴" and not show_ok:
                continue
            print(f"       ⚠ {i['code']}  {i['msg']}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="barn_watch")
    ap.add_argument("--sows", type=int, default=300)
    ap.add_argument("--days", type=int, default=DEFAULT_DAYS)
    ap.add_argument("--setup", help="등록 화면이 내보낸 JSON")
    ap.add_argument("--limit", type=int, default=8)
    ap.add_argument("--all", action="store_true", help="정상 전이도 출력")
    ap.add_argument("--sweep", action="store_true",
                    help="house 마다 방을 빼 보며 견디는 한계 찾기")
    ap.add_argument("--out")
    a = ap.parse_args(argv)

    import run_farm as rf
    cfg = default_config()
    rooms = None
    if a.setup:
        setup = json.load(open(a.setup, encoding="utf-8"))
        if setup.get("n_sows"):
            a.sows = int(setup["n_sows"])
        # 간격을 먼저 맞춘다 — crate_count 역산이 간격에 딸려 움직인다
        sid, why = batch_system_from_setup(setup, cfg)
        if sid:
            cfg.batch_system_id = sid
        want = rf.crates_for_sows(a.sows, cfg)
        # **등록한 분만틀이 이긴다.** 모돈수 역산은 설계값이고 분만틀은
        # 지어 놓은 것이다. 둘이 다르면 조용히 고르지 않고 둘 다 보여 준다.
        have = crates_from_setup(setup)
        cfg.crate_count = have or want
        spec, notes = rooms_from_setup(setup, cfg.merged())
        if spec:
            cfg.rooms = spec
            rooms = build_rooms(cfg.merged(), from_config=True)
        print(f"등록 JSON: 모돈 {a.sows}두 · 돈방 {len(spec)}개 · "
              f"배치 {cfg.batch_system_id} · 방당 분만틀 {cfg.crate_count}개")
        if why:
            print(f"  · {why}")
        if have and have != want:
            print(f"  · 방당 분만틀 등록 {have}개 vs 모돈 {a.sows}두 역산 "
                  f"{want}개 — **등록값으로 돌린다**")
        for name, stage, why in notes:
            print(f"  · {name}({stage}) — {why}")
        if not spec:
            print("  → 쓸 수 있는 동이 없어 소요량대로 짓고 돌린다")
    else:
        cfg.crate_count = rf.crates_for_sows(a.sows, cfg)

    r = watch(cfg, days=a.days, rooms=rooms)
    _print(r, limit=a.limit, show_ok=a.all)
    if a.sweep:
        _print_sweep(sweep(cfg, days=a.days))
    if a.out:
        # 스냅샷 전체는 크다. 파일로 낼 때만 담는다.
        json.dump(r, open(a.out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\n저장: {a.out}")
    print("\n※ 분만틀·방 면적은 설계값이다. 실제 도면이 들어오면 그 농장 "
          "값으로 바뀌고, 위 날짜도 그 농장 날짜가 된다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
