"""축사 환경(온습도) → 번식 영향 계산 — ICT 데이터를 숫자 표시로 끝내지 않는다.

환경 센서를 붙여 온도·습도를 화면에 띄우는 것 자체는 어렵지 않다. 문제는 그게
**무슨 뜻인지**다. 26℃ 는 높은가? 습도 80% 면 어떤가? 사람이 판단하라고 숫자만
던지면 결국 안 본다.

돼지에게 더위는 온도만의 문제가 아니라 온도×습도다. 표준 지표는 THI
(온습도지수)이며, 모돈 번식에는 특히 직접적이다:

  · THI 74 초과 — 경증 열스트레스. 사료 섭취 감소 시작
  · THI 79 초과 — 중등도. **하계불임** 구간: 이유 후 발정 지연, 미약발정,
    배아 착상 실패로 이어진다(교배 후 2~3주가 가장 취약)
  · THI 84 초과 — 중증. 수태율이 눈에 띄게 떨어진다

그래서 이 모듈은 THI 를 계산해 **번식 일정에 되먹인다** — 더운 구간의 축사는
기대 WEI 를 늘려 잡고(repro_calendar), 그 기간 교배한 개체는 재발 위험군으로
표시한다. 환경 데이터가 경보와 일정에 실제로 영향을 주게 하는 것이 목적이다.

    python competition/src/barn_environment.py
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# THI 구간 (모돈 기준) — (하한, 라벨, 색, 설명)
THI_BANDS = [
    (84.0, "중증", "#d03b3b", "수태율 저하 · 즉시 냉방 조치"),
    (79.0, "중등도", "#e8a33d", "하계불임 구간 — 발정 지연·착상 실패 위험"),
    (74.0, "경증", "#e0c33d", "사료 섭취 감소 시작"),
    (-1e9, "적정", "#1baf7a", "정상 범위"),
]

# 열스트레스가 WEI(이유-발정 간격)를 늘리는 정도(일). 구간별 경험적 보정.
WEI_PENALTY = {"적정": 0.0, "경증": 0.5, "중등도": 1.5, "중증": 3.0}

# 교배 후 이 기간이 착상기라 열스트레스에 가장 취약하다(일)
IMPLANTATION_WINDOW = (7, 21)


def thi(temp_c: float, rh_pct: float) -> float:
    """온습도지수. NRC 계열 표준식.

        THI = 0.8·T + (RH/100)·(T − 14.4) + 46.4
    """
    t, rh = float(temp_c), float(rh_pct)
    return round(0.8 * t + (rh / 100.0) * (t - 14.4) + 46.4, 1)


def band(thi_value: float) -> tuple:
    """THI → (라벨, 색, 설명)."""
    for lo, label, color, desc in THI_BANDS:
        if thi_value > lo:
            return label, color, desc
    return THI_BANDS[-1][1], THI_BANDS[-1][2], THI_BANDS[-1][3]


def assess(readings: dict) -> pd.DataFrame:
    """{축사동: (온도, 습도)} → 축사별 THI·등급·WEI 보정.

    readings 값은 (temp_c, rh_pct) 튜플이거나 {"temp","rh"} 딕셔너리.
    """
    rows = []
    for barn, v in readings.items():
        t, rh = (v["temp"], v["rh"]) if isinstance(v, dict) else (v[0], v[1])
        x = thi(t, rh)
        label, color, desc = band(x)
        rows.append({"barn": barn, "temp_c": round(float(t), 1),
                     "rh_pct": round(float(rh), 1), "thi": x,
                     "level": label, "color": color, "advice": desc,
                     "wei_penalty_d": WEI_PENALTY[label],
                     "heat_stress": label != "적정"})
    return pd.DataFrame(rows)


def at_risk_services(herd: pd.DataFrame, env: pd.DataFrame,
                     farm=None) -> pd.DataFrame:
    """열스트레스 축사에 있으면서 **착상기**에 든 개체 — 재발 위험군.

    교배 후 7~21일이 착상기다. 이 시기에 더위를 먹으면 수정은 됐어도 착상이
    실패해 3주 재발로 돌아온다. 환경과 번식 기록을 겹쳐야만 보이는 위험이라
    둘 중 하나만 있는 시스템에서는 잡히지 않는다.
    """
    from datetime import date as _date
    hot = set(env[env["heat_stress"]]["barn"])
    if not hot or farm is None:
        return pd.DataFrame()
    lo, hi = IMPLANTATION_WINDOW
    lv = env.set_index("barn")["level"].to_dict()
    t0 = herd.attrs.get("today", _date.today())
    rows = []
    for r in herd.itertuples(index=False):
        loc = farm.locate(r.id)
        if not loc or loc[0] not in hot:
            continue
        # 주차(week)로 재면 7일 단위로 뭉개져 착상기 경계가 흐려진다.
        # 교배일이 있으므로 일 단위로 정확히 센다.
        if r.stage not in ("교배", "임신") or not isinstance(r.service_date, _date):
            continue
        days = (t0 - r.service_date).days
        if lo <= days <= hi:
            rows.append({"id": r.id, "barn": loc[0],
                         "days_since_service": int(days), "level": lv[loc[0]],
                         "risk": "착상기 열스트레스 — 3주 재발 확인 필수"})
    return pd.DataFrame(rows)


def demo_readings(seed: int = 5, hot_summer: bool = True) -> dict:
    """축사별 온습도 합성 — 여름철 오후, 동마다 편차."""
    rng = np.random.default_rng(seed)
    base_t = 29.0 if hot_summer else 19.0
    out = {}
    for i, b in enumerate(("1동", "2동", "3동", "4동")):
        # 분만사(3동)는 자돈 보온 때문에 더 덥게 유지된다
        bump = 2.5 if b == "3동" else 0.0
        out[b] = (round(base_t + bump + rng.normal(0, 1.6), 1),
                  round(float(np.clip(rng.normal(72, 8), 40, 95)), 1))
    return out


def main() -> int:
    import farm_registry as fr
    import herd_board as hb

    print("=== THI 구간 기준 (모돈) ===")
    for lo, label, _c, desc in THI_BANDS:
        rng_s = f">{lo:.0f}" if lo > -1e8 else "이하"
        print(f"  {label:<5} THI {rng_s:<5} — {desc} (WEI +{WEI_PENALTY[label]}일)")

    for season, hot in (("여름 오후", True), ("봄철", False)):
        env = assess(demo_readings(hot_summer=hot))
        print(f"\n=== 축사 환경 ({season}) ===")
        print(f"  {'축사동':<5} {'온도':>6} {'습도':>6} {'THI':>6} {'등급':<6} 조치")
        for r in env.itertuples(index=False):
            print(f"  {r.barn:<5} {r.temp_c:>5.1f}℃ {r.rh_pct:>5.1f}% "
                  f"{r.thi:>6.1f} {r.level:<6} {r.advice}")

    # 환경 × 번식 기록 — 착상기 위험군
    farm = fr.demo_farm()
    ids = sorted(farm._where)
    recs = hb.generate_demo(n=len(ids) + 40, today="2026-08-10")[:len(ids)]
    for r, i in zip(recs, ids):
        r["id"] = i
    herd = hb.build_herd(recs, today="2026-08-10")
    env = assess(demo_readings(hot_summer=True))
    risk = at_risk_services(herd, env, farm)
    print(f"\n=== 착상기 열스트레스 위험군 {len(risk)}두 ===")
    for r in risk.head(8).itertuples(index=False):
        print(f"  {r.id} {r.barn} 교배 후 {r.days_since_service}일 "
              f"({r.level}) — {r.risk}")
    print("  ※ 환경 데이터와 번식 기록을 겹쳐야만 보이는 위험이다. 온습도만 띄우는"
          "\n    시스템도, 번식 기록만 쓰는 시스템도 이 목록을 만들지 못한다.")

    print("\n※ THI 임계값은 문헌 기준이나 품종·순응도에 따라 다르다. WEI 보정폭은"
          "\n  가정값이며 농장 데이터로 재추정해야 한다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
