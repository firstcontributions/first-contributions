"""농장 구조 등록 + 돼지관리표 — 축사동 → 돈방/군사 → 개체의 3계층.

앱이 현장에서 쓰이려면 먼저 **농장이 어떻게 생겼는지** 알아야 한다. 개체 목록만
있으면 "3동 임신사 두 번째 돈방" 같은 현장 언어로 찾을 수 없고, 카메라가 잡은
위치를 개체에 연결할 수도 없다. 그래서 계층은 세 단계다:

    축사동(barn)  3동 임신사, 4동 분만사 …   용도(stage)와 수용능력을 가진다
      └ 돈방(pen)  군사 돈방 / 스톨 열        사육 방식이 여기서 갈린다
          └ 자리(slot)  스톨 번호 / 군사 내 개체

사육 방식이 계층에 박혀 있는 게 중요하다. **스톨은 자리가 곧 개체 ID** 라 추적이
필요 없지만 활동량 신호가 없고(stall_estrus 로 판정), **군사는 활동량을 쓸 수
있지만 개체 추적이 필요하다**(motion_tracker). 같은 카메라 영상이라도 어느
돈방이냐에 따라 다른 알고리즘을 써야 하므로, 등록 정보가 곧 분석 경로를 정한다.

  Farm.add_barn / add_pen / place      등록
  Farm.table()                          돼지관리표(축사동-돈방-개체)
  Farm.occupancy()                      동·돈방별 수용률
  Farm.locate(id) / Farm.at(barn, pen)  위치 ↔ 개체 조회
  Farm.analysis_route()                 돈방별 적용 알고리즘(사육 방식에 따라)

    python competition/src/farm_registry.py
"""
from __future__ import annotations

import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# 축사 용도 — 번식 단계와 대응한다
BARN_STAGES = {
    "교배사": "이유~교배·임신 초기(스톨). 발정 확인과 교배가 일어나는 곳",
    "임신사": "임신 중기~후기. 군사 또는 스톨",
    "분만사": "분만 전 7일~이유(분만틀)",
    "후보사": "후보돈 순치·초교배 대기",
    "자돈사": "이유자돈",
    "비육사": "육성·비육돈",
}

# 사육 방식 → 발정 판정 경로. 등록만 하면 분석 방법이 자동으로 정해진다.
HOUSING = {
    "stall": ("스톨(개별)", "stall_estrus", "자세·전환·부동자세",
              "자리가 곧 개체 ID — 추적 불필요, 활동량 신호 없음"),
    "group": ("군사(합사)", "motion_tracker + temporal_features", "활동량·시간 윈도우",
              "활동량을 쓸 수 있으나 개체 추적 필요"),
    "crate": ("분만틀", "-", "-", "번식 판정 대상 아님(분만·포유 관리)"),
    "pen": ("일반 돈방", "-", "-", "비번식(자돈·비육)"),
}


def _slot_key(s):
    """자리 번호 자연 정렬 키 — 숫자면 숫자로, 아니면 문자열로."""
    t = str(s)
    return (0, int(t), "") if t.isdigit() else (1, 0, t)


class Farm:
    """농장 구조 + 개체 배치."""

    def __init__(self, name: str = "농장"):
        self.name = name
        self.barns: dict = {}        # {barn_id: {stage, note}}
        self.pens: dict = {}         # {(barn_id, pen_id): {housing, capacity, ...}}
        self.slots: dict = {}        # {(barn_id, pen_id, slot): animal_id}
        self._where: dict = {}       # {animal_id: (barn_id, pen_id, slot)}

    # -- 등록 ---------------------------------------------------------------
    def add_barn(self, barn_id: str, stage: str, note: str = "") -> "Farm":
        if stage not in BARN_STAGES:
            raise ValueError(f"알 수 없는 축사 용도: {stage} (가능: {list(BARN_STAGES)})")
        self.barns[barn_id] = {"stage": stage, "note": note}
        return self

    def add_pen(self, barn_id: str, pen_id: str, housing: str,
                capacity: int, note: str = "") -> "Farm":
        if barn_id not in self.barns:
            raise KeyError(f"축사동 {barn_id} 이 등록되지 않았다")
        if housing not in HOUSING:
            raise ValueError(f"알 수 없는 사육 방식: {housing} (가능: {list(HOUSING)})")
        if capacity <= 0:
            raise ValueError("수용능력은 1 이상이어야 한다")
        self.pens[(barn_id, pen_id)] = {"housing": housing, "capacity": int(capacity),
                                        "note": note}
        return self

    def place(self, animal_id: str, barn_id: str, pen_id: str,
              slot: str | int | None = None) -> "Farm":
        """개체를 자리에 배치. 이미 다른 곳에 있으면 옮긴다(이중 배치 방지).

        스톨은 slot 이 필수다 — 자리가 곧 개체 ID 이므로 자리 없이 넣으면
        나중에 카메라 화면의 어느 칸인지 되짚을 수 없다.
        """
        key = (barn_id, pen_id)
        if key not in self.pens:
            raise KeyError(f"돈방 {barn_id}-{pen_id} 이 등록되지 않았다")
        pen = self.pens[key]
        if pen["housing"] == "stall" and slot is None:
            raise ValueError(f"{barn_id}-{pen_id} 은 스톨이다 — slot(자리 번호) 필수")
        if animal_id in self._where:                 # 기존 자리 비우기
            self.slots.pop(self._where[animal_id], None)
        if slot is None:                             # 군사: 자리 자동 부여
            slot = 1 + sum(1 for k in self.slots if k[0] == barn_id and k[1] == pen_id)
        sk = (barn_id, pen_id, str(slot))
        if sk in self.slots and self.slots[sk] != animal_id:
            raise ValueError(f"{barn_id}-{pen_id}-{slot} 에 이미 "
                             f"{self.slots[sk]} 이 있다")
        cur = sum(1 for k in self.slots if k[0] == barn_id and k[1] == pen_id)
        if cur >= pen["capacity"] and sk not in self.slots:
            raise ValueError(f"{barn_id}-{pen_id} 수용능력 {pen['capacity']} 초과")
        self.slots[sk] = animal_id
        self._where[animal_id] = sk
        return self

    def remove(self, animal_id: str) -> "Farm":
        """출하·도태·폐사 — 자리를 비운다."""
        sk = self._where.pop(animal_id, None)
        if sk:
            self.slots.pop(sk, None)
        return self

    # -- 조회 ---------------------------------------------------------------
    def locate(self, animal_id: str):
        """개체 → (축사동, 돈방, 자리). 없으면 None."""
        return self._where.get(animal_id)

    def at(self, barn_id: str, pen_id: str | None = None) -> list:
        """위치 → 개체 목록. pen_id 를 생략하면 그 동 전체."""
        hits = [(k, a) for k, a in self.slots.items()
                if k[0] == barn_id and (pen_id is None or k[1] == pen_id)]
        return [a for _, a in sorted(hits, key=lambda x: (x[0][1], _slot_key(x[0][2])))]

    def label(self, animal_id: str) -> str:
        """현장에서 부르는 위치 문자열 — '3동 임신사 A열 12번'."""
        sk = self._where.get(animal_id)
        if not sk:
            return "미배치"
        b, p, s = sk
        return f"{b} {self.barns[b]['stage']} {p} {s}번"

    # -- 표 -----------------------------------------------------------------
    def table(self, herd: pd.DataFrame | None = None) -> pd.DataFrame:
        """돼지관리표 — 축사동·돈방·자리·개체(+ 번식 상태).

        herd 를 주면(herd_board.build_herd 결과) 단계·산차·예정일이 붙는다.
        """
        rows = []
        for (b, p, s), aid in self.slots.items():
            pen = self.pens[(b, p)]
            h = HOUSING[pen["housing"]]
            rows.append({"barn": b, "stage": self.barns[b]["stage"],
                         "pen": p, "slot": s, "id": aid,
                         "housing": pen["housing"], "housing_kr": h[0]})
        df = pd.DataFrame(rows)
        if not len(df):
            return df
        if herd is not None and len(herd):
            df = df.merge(herd, on="id", how="left", suffixes=("", "_h"))
        # 자리 번호는 문자열이라 그냥 정렬하면 1,10,11,12,2 순이 된다.
        # 스톨 번호는 카메라 화면의 물리적 순서와 같아야 읽을 수 있다.
        df["_k"] = df["slot"].map(_slot_key)
        return (df.sort_values(["barn", "pen", "_k"]).drop(columns="_k")
                  .reset_index(drop=True))

    def occupancy(self) -> pd.DataFrame:
        """돈방별 수용률 — 과밀·공실을 한눈에."""
        rows = []
        for (b, p), pen in self.pens.items():
            n = sum(1 for k in self.slots if k[0] == b and k[1] == p)
            rows.append({"barn": b, "stage": self.barns[b]["stage"], "pen": p,
                         "housing": pen["housing"], "n": n,
                         "capacity": pen["capacity"],
                         "rate": round(n / pen["capacity"], 3),
                         "free": pen["capacity"] - n})
        return pd.DataFrame(rows).sort_values(["barn", "pen"]).reset_index(drop=True)

    def barn_summary(self, herd: pd.DataFrame | None = None) -> pd.DataFrame:
        """축사동별 두수 + (herd 가 있으면) 번식 단계 구성."""
        t = self.table(herd)
        if not len(t):
            return t
        g = t.groupby(["barn", "stage"], sort=False).agg(n=("id", "count"))
        if herd is not None and "stage_h" in t.columns:
            piv = t.pivot_table(index=["barn", "stage"], columns="stage_h",
                                values="id", aggfunc="count", fill_value=0)
            g = g.join(piv)
        return g.reset_index()

    def misplaced(self, herd: pd.DataFrame) -> pd.DataFrame:
        """축사 용도와 번식 단계가 어긋난 개체 — 이동 누락을 잡아낸다.

        분만 임박한 모돈이 교배사에 남아 있거나 이유한 모돈이 분만사를 차지하고
        있으면 그 자체가 사고다. 규칙은 단계별 허용 구간으로 두되, 경계는
        느슨하게 잡는다 — 교배사의 임신 초기와 분만사의 분만 직전은 정상이다.
        """
        allow = {
            "교배사": {"공태", "교배", "임신"},   # 임신은 초기 한정(아래에서 검사)
            "임신사": {"임신", "교배"},
            "분만사": {"포유", "임신"},           # 임신은 분만 임박 한정
            "후보사": {"후보", "공태"},
            "자돈사": set(), "비육사": set(),
        }
        t = self.table(herd)
        if not len(t) or "stage_h" not in t.columns:
            return pd.DataFrame()
        rows = []
        for r in t.itertuples(index=False):
            st, bs = r.stage_h, r.stage
            if not isinstance(st, str):
                continue
            why = None
            if st not in allow.get(bs, set()):
                why = f"{bs}에 {st} 개체 — 축사 용도와 불일치"
            elif bs == "교배사" and st == "임신" and (r.week or 0) > 5:
                why = f"임신 {int(r.week)}주인데 교배사에 있음 — 임신사 이동 누락"
            elif bs == "분만사" and st == "임신" and (r.d_day is not None
                                                 and r.d_day > 14):
                why = f"분만 {int(r.d_day)}일 남았는데 분만사 점유 — 자리 낭비"
            if why:
                rows.append({"id": r.id, "loc": f"{r.barn} {r.pen} {r.slot}번",
                             "barn_stage": bs, "repro_stage": st, "reason": why})
        return pd.DataFrame(rows)

    def analysis_route(self) -> pd.DataFrame:
        """돈방마다 어떤 발정 판정 경로를 쓸지 — 등록이 곧 분석 설계.

        번식 축사(교배사·임신사·후보사)만 발정 판정 대상이다. 분만사·자돈사에
        발정 알고리즘을 돌리는 것은 의미가 없으므로 여기서 걸러낸다.
        """
        repro = {"교배사", "임신사", "후보사"}
        rows = []
        for (b, p), pen in self.pens.items():
            st = self.barns[b]["stage"]
            kr, mod, sig, note = HOUSING[pen["housing"]]
            target = st in repro and pen["housing"] in ("stall", "group")
            rows.append({"barn": b, "stage": st, "pen": p, "housing_kr": kr,
                         "estrus_target": target,
                         "module": mod if target else "-",
                         "signal": sig if target else "-",
                         "note": note})
        return pd.DataFrame(rows).sort_values(["barn", "pen"]).reset_index(drop=True)


# --------------------------------------------------------------------------
def demo_farm(n_sows: int = 68) -> Farm:
    """전형적인 일관농장 구조 — 교배사(스톨)·임신사(군사)·분만사·후보사."""
    f = Farm("시연농장")
    (f.add_barn("1동", "교배사", "이유 후 발정 확인 + 교배")
      .add_barn("2동", "임신사", "임신 확인 후 군사 전환")
      .add_barn("3동", "분만사", "분만 7일 전 이동")
      .add_barn("4동", "후보사", "순치 중인 후보돈"))
    for col in ("A열", "B열"):
        f.add_pen("1동", col, "stall", 12)
    for i in (1, 2, 3):
        f.add_pen("2동", f"{i}방", "group", 10)
    f.add_pen("3동", "분만실", "crate", 12)
    f.add_pen("4동", "순치방", "group", 12)

    idx = 0
    for col in ("A열", "B열"):
        for s in range(1, 13):
            if idx >= n_sows:
                break
            f.place(f"{2000 + idx}", "1동", col, s)
            idx += 1
    for i in (1, 2, 3):
        for _ in range(9):
            if idx >= n_sows:
                break
            f.place(f"{2000 + idx}", "2동", f"{i}방")
            idx += 1
    for s in range(1, 11):
        if idx >= n_sows:
            break
        f.place(f"{2000 + idx}", "3동", "분만실", s)
        idx += 1
    for _ in range(8):
        if idx >= n_sows:
            break
        f.place(f"{2000 + idx}", "4동", "순치방")
        idx += 1
    return f


def main() -> int:
    f = demo_farm()
    print(f"=== {f.name} 구조 등록 ===")
    for b, meta in f.barns.items():
        pens = [(p, v) for (bb, p), v in f.pens.items() if bb == b]
        cap = sum(v["capacity"] for _, v in pens)
        print(f"  {b} {meta['stage']:<5} 돈방 {len(pens)}개 · 수용 {cap}두 — {meta['note']}")
        for p, v in pens:
            print(f"     └ {p:<6} {HOUSING[v['housing']][0]:<8} 수용 {v['capacity']:>3}두")

    print("\n=== 돼지관리표 (축사동-돈방-개체) ===")
    t = f.table()
    print(f"  총 {len(t)}두")
    print(f"  {'축사동':<5} {'용도':<5} {'돈방':<6} {'자리':>4} {'개체':>6} {'사육방식':<8}")
    for r in t.head(8).itertuples(index=False):
        print(f"  {r.barn:<5} {r.stage:<5} {r.pen:<6} {r.slot:>4} {r.id:>6} "
              f"{r.housing_kr:<8}")
    print(f"  … 이하 {max(0, len(t) - 8)}행")

    print("\n=== 수용률 ===")
    for r in f.occupancy().itertuples(index=False):
        bar = "█" * int(r.rate * 20)
        print(f"  {r.barn:<5} {r.pen:<6} {r.n:>3}/{r.capacity:<3} "
              f"{r.rate:>6.0%} {bar:<20} 여유 {r.free}두")

    print("\n=== 위치 조회 ===")
    print(f"  2003 → {f.label('2003')}")
    print(f"  2030 → {f.label('2030')}")
    print(f"  1동 A열 개체: {', '.join(f.at('1동', 'A열')[:6])} …")

    print("\n=== 번식 상태 결합 (herd_board) ===")
    import herd_board as hb
    ids = sorted(f._where)
    recs = hb.generate_demo(n=len(ids) + 40, today="2026-08-10")[:len(ids)]
    for r, i in zip(recs, ids):
        r["id"] = i
    herd = hb.build_herd(recs, today="2026-08-10")
    print(f.barn_summary(herd).to_string(index=False))

    mp = f.misplaced(herd)
    print(f"\n=== 배치 오류 {len(mp)}두 (축사 용도 ↔ 번식 단계 불일치) ===")
    for r in mp.head(6).itertuples(index=False):
        print(f"  {r.id} {r.loc:<16} {r.reason}")
    print("  ※ 합성 데이터라 배치가 무작위다. 실제 농장에서는 이 목록이 곧"
          "\n    '이동 누락' 알림이 된다 — 분만 임박한 모돈이 교배사에 남아 있는 식.")

    print("\n=== 돈방별 발정 판정 경로 (등록이 곧 분석 설계) ===")
    for r in f.analysis_route().itertuples(index=False):
        mark = "○" if r.estrus_target else "·"
        print(f"  {mark} {r.barn:<4} {r.pen:<6} {r.housing_kr:<8} "
              f"{r.module:<32} {r.note}")

    print("\n※ 사육 방식이 계층에 박혀 있어야 한다. 스톨은 자리가 곧 개체 ID 라 추적이"
          "\n  필요 없는 대신 활동량 신호가 없고, 군사는 그 반대다. 같은 카메라라도"
          "\n  돈방에 따라 다른 알고리즘을 써야 하므로 등록 정보가 분석 경로를 정한다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
