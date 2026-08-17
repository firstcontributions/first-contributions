"""PSY 회수 우선순위 — 이미 검증된 진단을 **처방 순서로 배열**한다.

새 데이터도 새 산식도 없다. `farm_gap`(지표별 격차 → PSY 회수량 → 원/년),
`farm_panel`(하락 방어 기댓값), `farm_monthly_panel`(계절 손실 분포)의 출력을
읽어 **정렬·병치·표시**만 한다. 수치가 바뀌면 잘못 만든 것이다.

## 근거 등급을 표에 박는다

회수량 큰 순으로만 세우면 **횡단면 비교가 농장 내 변화처럼 읽힌다.** 이
프로젝트가 지켜온 실측/계산/가정 구분의 처방 버전이다.

    A · 농장 내 변화     같은 농장 전년 대비에서 움직인 것. 농장 고유 조건 통제됨
    B · 농장 간 횡단면   잘하는 농장과 못하는 농장의 차이. 교란 가능
    C · 부분모집단 측정  특정 조건에서만 잰 것

## 두 개의 축이 섞여 있다 — 그게 요지다

`farm_gap` 항목은 **"올리기"**(현재 → 중앙값, 결정론적 차분)이고,
하락 방어는 **"안 떨어지기"**(하락폭 × 발생빈도, 기댓값)다. 성격이 다른데도
금액이 같은 급(2,976 vs 3,751만원)이라는 게 이 표가 말하려는 것이다.
그래서 **같은 자에 올리되 축이 다르다고 표시**한다.

## 합치지 않는다

지표가 서로 맞물려 있어 개별 회수량의 단순 합은 이중계산이다(항이 곱해지므로
과소가 될 수도 있다). **"합쳐서 +N두" 라는 문장을 만들지 않는다.** 합과 총
격차를 나란히 보이고 차이가 왜 나는지만 적는다.

    python competition/src/psy_priority.py --sows 300
    python competition/src/psy_priority.py --setup my_farm.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import farm_gap as fg                                           # noqa: E402

OUT = os.path.join(ROOT, "data", "psy_priority.json")
PANEL = os.path.join(ROOT, "data", "farm_panel.json")
SEASON = os.path.join(ROOT, "data", "farm_monthly_panel.json")

# 20번째 뷰와 같은 예시 농장. **실제 농장이 아니다.**
DEMO_FARM = {"npd": 62.0, "weaned": 10.0, "farrowing_rate": 74.0}
DEMO_SOWS = 300

GRADE = {
    "A": ("농장 내 변화", "같은 농장 전년 대비. 농장 고유 조건이 통제됨"),
    "B": ("농장 간 횡단면", "잘하는 농장과 못하는 농장의 차이. 교란 가능"),
    "C": ("부분모집단 측정", "특정 조건에서만 잰 것"),
}

# 축 — 같은 원/년이라도 세는 방식이 다르다
AXIS = {
    "회수": "올리기 — 현재에서 중앙값으로 되돌렸을 때 (결정론적 차분)",
    "방어": "안 떨어지기 — 하락폭 × 발생빈도 (기댓값)",
    "계절": "여름을 겨울 수준으로 — 손실 상한 (농장별로 갈림)",
}

FOOTER = ("이 표는 격차의 분해이지 개입 효과의 추정이 아니다.\n"
          "실농장 개입 실험은 수행하지 않았다.")


def _load(path: str) -> dict:
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}


def farm_from_setup(path: str) -> tuple:
    """등록 화면 JSON → farm_gap 입력. **비운 성적은 넣지 않는다.**

    빈 칸을 중앙값으로 채우면 그 지표의 격차가 늘 0 으로 찍힌다 — 등록
    화면이 지키는 규칙과 같다.
    """
    s = json.load(open(path, encoding="utf-8"))
    perf = {k: v for k, v in (s.get("performance") or {}).items() if v is not None}
    return perf, int(s.get("n_sows") or DEMO_SOWS), s.get("name")


def build(farm: dict | None = None, n_sows: int = DEMO_SOWS,
          farm_name: str | None = None) -> dict:
    """항목을 모아 회수량 순으로 세운다. 계산은 각 모듈이 이미 한 것을 쓴다."""
    given = bool(farm)
    f = dict(farm or DEMO_FARM)
    diag = fg.diagnose(f, n_sows=n_sows)
    won = {w["metric"]: w["won_year"] for w in diag.get("won_per_year") or []}

    rows = []
    for r in diag["rows"]:
        rec = r.get("psy_recover")
        if not r.get("actionable") or not rec or rec <= 0:
            continue
        rows.append({
            "axis": "회수", "grade": "B",
            "name": r["name_ko"], "psy": rec,
            "won_year": won.get(r["metric"]),
            "target": f"중앙 {r['median']} (내 값 {r['value']})",
            "metric": r["metric"],
        })
    rows.sort(key=lambda x: -x["psy"])

    # 하락 방어 — 축이 다르다. 회수량 칸을 비우고 금액만 놓는다.
    dn = (_load(PANEL) or {}).get("downside") or {}
    if dn:
        # **모돈 두수가 다르면 다시 환산한다.** farm_panel 은 300두로 냈다.
        scale = n_sows / max(1, int(dn.get("n_sows") or n_sows))
        rows.append({
            "axis": "방어", "grade": "A",
            "name": "하락 방어", "psy": None,
            "won_year": round(dn["expected_won_year"] * scale),
            "target": (f"농장-연의 {dn['freq']:.0%} 가 {abs(dn['size_psy'])}두 이상 "
                       f"떨어진다 (중앙 {dn['size_psy']}두)"),
            "metric": "downside",
        })

    # 계절 — 분포로 낸다. 전체 평균 하나만 쓰면 발견 ③′ 를 버리는 것이다.
    sn = _load(SEASON)
    if sn:
        m, q = sn["money"], sn["loss"]
        ref = int(m["ref_sows"])
        sc = n_sows / max(1, ref)
        rows.append({
            "axis": "계절", "grade": "C",
            "name": "여름 손실 (선별)", "psy": None,
            "won_year": round(m["won_ref"]["median"] * sc),
            "won_p90": round(m["won_ref"]["p90"] * sc),
            "target": (f"농장별 {q['p10']:+.1f} ~ {q['p90']:+.1f}%p "
                       f"(중앙 {q['median']:+.1f}) · {sn['n_farms']}농장"),
            "metric": "season",
            "note": (f"관측 분산의 {sn['spread']['true_share']:.0%} 만 진짜 농장 "
                     f"차이 · 연간 성적과 무관(PSY ρ {sn['join']['PSY']['rho']})"),
        })

    return {
        "farm_name": farm_name, "n_sows": n_sows, "example": not given,
        "psy": diag["psy"], "psy_median_farm": diag["psy_median_farm"],
        "psy_median_observed": diag.get("psy_median_observed"),
        "psy_gap": diag["psy_gap"],
        # **합을 쓰지 않는다.** 나란히 보이고 왜 다른지만 적는다.
        "sum_of_parts": diag["sum_of_parts"],
        "sum_note": ("지표가 항등식에서 곱해지므로 개별 회수량의 합은 총 격차와 "
                     "같지 않다. 합산해 '총 +N두' 라고 쓰지 않는다."),
        "rows": rows, "grades": GRADE, "axes": AXIS, "footer": FOOTER,
    }


def _print(r: dict) -> None:
    print("=" * 80)
    who = r["farm_name"] or ("예시 농장" if r["example"] else "내 농장")
    print(f"  PSY 회수 우선순위 — {who} · 모돈 {r['n_sows']}두")
    print("=" * 80)
    if r["example"]:
        print("  ※ 등록된 농장이 없어 **예시 농장**으로 냈다. 실제 농장이 아니다.")
    print(f"\n  내 PSY {r['psy']} · 중앙 농장 {r['psy_median_farm']} → "
          f"격차 {r['psy_gap']:+.2f}두")
    print(f"  (중앙 농장은 지표별 중앙값을 항등식에 넣은 합성값이다. "
          f"PSY 열 자체의 중앙은 {r['psy_median_observed']})")

    print(f"\n  {'순':<3}{'항목':<16}{'회수량':>8}{'원/년':>12}{'등급':>5}  표적")
    print("  " + "-" * 78)
    n = 0
    for x in r["rows"]:
        if x["axis"] == "회수":
            n += 1
            no = str(n)
        else:
            no = "—"
        psy = f"{x['psy']:+.2f}두" if x["psy"] is not None else "—"
        won = f"{x['won_year']/1e4:,.0f}만원" if x["won_year"] is not None else "—"
        print(f"  {no:<3}{x['name']:<16}{psy:>8}{won:>12}{x['grade']:>5}  "
              f"{x['target']}")
        if x.get("won_p90"):
            print(f"  {'':<3}{'':<16}{'':>8}{'상위10% ' + format(x['won_p90']/1e4, ',.0f') + '만원':>12}")
        if x.get("note"):
            print(f"  {'':<3}   {x['note']}")

    print(f"\n  [축이 둘이다]")
    for k, v in r["axes"].items():
        print(f"    {k:<4}{v}")
    print(f"\n  [근거 등급]")
    for k, (nm, why) in r["grades"].items():
        print(f"    {k} · {nm:<12}{why}")

    print(f"\n  [합치지 않는다] 개별 회수량 합 {r['sum_of_parts']}두 vs "
          f"총 격차 {abs(r['psy_gap']):.2f}두")
    print(f"    {r['sum_note']}")
    print(f"\n  {r['footer'].replace(chr(10), chr(10) + '  ')}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="psy_priority")
    ap.add_argument("--sows", type=int, default=DEMO_SOWS)
    ap.add_argument("--setup", help="등록 화면이 내보낸 JSON")
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    farm, name = None, None
    n_sows = a.sows
    if a.setup:
        farm, n_sows, name = farm_from_setup(a.setup)
        if not farm:
            print("등록 JSON 에 성적이 비어 있다 — 예시 농장으로 낸다")
            farm = None
    r = build(farm, n_sows, name)
    _print(r)
    if a.out:
        json.dump(r, open(a.out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\n저장: {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
