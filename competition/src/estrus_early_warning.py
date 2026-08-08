"""발정 조기경보 — 이유/초교배 기준 일(day) 단위 D-day 예측 + 지연·무발정 경보.

estrus_onset.py 가 '한 영상 안'의 발정 시작 프레임을 잡는다면, 이 모듈은
농장 운영 타임스케일(일 단위)에서:

  · 이유(또는 초교배 목표일) 이후 매일의 발정 준비도 점수 추세를 추적
  · 추세를 외삽해 **발정 예상일(D-day)** 을 예측(임박 경보)
  · 정상 발정 구간(WEI)을 지나도 점수가 안 오르면 **발정지연 → 무발정 경보**

도메인 근거:
  · 경산돈 정상 이유-발정 간격(WEI) 약 4~7일. 7일 초과 시 지연 의심.
  · 관찰 지평(예: 21일) 내 발정 미도래 → 무발정. 조기에 잡을수록 재발정 유도·
    도태 판단이 빨라져 비생산일수(NPD)·번식성적 손실을 줄인다.

핵심 가치(심사): 육안 확인 전에 며칠 앞서 경보 → '리드타임'. 특히 미약발정은
점수가 낮게라도 오르므로, 임계 교차 전에 추세로 선제 포착한다.

    python competition/src/estrus_early_warning.py     # 합성 시연
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

NORMAL_WEI = 7          # 정상 이유-발정 간격 상한(일)
DELAY_ALERT_DAY = 8     # 이 날짜까지 미도래면 '발정지연' 경보
ANESTRUS_DAY = 21       # 관찰 지평 — 이후에도 미도래면 '무발정' 경보
ONSET_THR = 0.55        # 발정 판정 점수 임계
SUSTAIN = 2             # 임계 연속 유지 일수

STATES = ["정상 진행", "발정 임박", "발정 확인", "발정지연 경보", "무발정 경보"]


def predict_onset_day(days, scores, thr: float = ONSET_THR,
                      lookback: int = 3) -> float | None:
    """최근 상승 추세를 선형 외삽해 임계 도달 예상일(D-day). 상승 없으면 None."""
    days = np.asarray(days, float); scores = np.asarray(scores, float)
    if len(days) < 2 or scores[-1] >= thr:
        return float(days[-1]) if len(days) and scores[-1] >= thr else None
    x = days[-lookback:]; y = scores[-lookback:]
    if len(x) < 2:
        return None
    slope = np.polyfit(x, y, 1)[0]
    if slope <= 1e-3:               # 추세 정체/하락 → 예측 불가
        return None
    eta = x[-1] + (thr - y[-1]) / slope
    return float(round(eta, 1))


def assess(days, scores, horizon: int = ANESTRUS_DAY) -> dict:
    """한 개체의 일별 점수 → 현재 경보 상태 + D-day + 실제 발정일(있으면).

    days: 이유 후 경과일 배열(0,1,2,...), scores: 일별 발정 준비도(0~1).
    """
    days = list(map(float, days)); scores = list(map(float, scores))
    # 실제 발정 확인일: 임계를 SUSTAIN일 연속 유지한 첫날
    onset_actual, run = None, 0
    for d, s in zip(days, scores):
        run = run + 1 if s >= ONSET_THR else 0
        if run >= SUSTAIN:
            onset_actual = d - SUSTAIN + 1
            break
    today = days[-1] if days else 0.0
    pred = predict_onset_day(days, scores)

    if onset_actual is not None:
        state = "발정 확인"
    elif today >= horizon:
        state = "무발정 경보"
    elif today >= DELAY_ALERT_DAY:
        state = "발정지연 경보"
    elif pred is not None and pred <= today + 3:
        state = "발정 임박"
    else:
        state = "정상 진행"

    # 리드타임: 임박 예측일과 실제 발정일의 차(양수=선제 경보한 일수)
    lead = None
    if onset_actual is not None and pred is not None:
        lead = round(onset_actual - pred, 1)
    return {"state": state, "today": today, "onset_actual": onset_actual,
            "predicted_day": pred, "eta_days": None if pred is None
            else round(pred - today, 1), "lead_time": lead,
            "peak": round(max(scores), 3) if scores else 0.0}


# --------------------------------------------------------------------------
def generate_daily(n_sows: int = 300, horizon: int = ANESTRUS_DAY, seed: int = 5):
    """이유 후 일별 발정 준비도 궤적(합성). 유형별로 다른 곡선.

    반환: (long_df[individual_id,day,score], truth[individual_id,type,onset_day]).
    유형: normal(4~7일 발정), delayed(9~14일), silent(낮게 상승·간신히 교차),
          anestrus(끝까지 미도래).
    """
    rng = np.random.default_rng(seed)
    types = rng.choice(["normal", "delayed", "silent", "anestrus"],
                       size=n_sows, p=[0.55, 0.2, 0.15, 0.10])
    rows, truth = [], []
    for i in range(n_sows):
        gid = f"S{i:04d}"; t = types[i]
        if t == "normal":
            onset = rng.integers(4, 8); peak = rng.uniform(0.75, 0.95)
        elif t == "delayed":
            onset = rng.integers(9, 15); peak = rng.uniform(0.7, 0.9)
        elif t == "silent":
            onset = rng.integers(5, 12); peak = rng.uniform(0.55, 0.68)  # 간신히 교차
        else:  # anestrus
            onset = None; peak = rng.uniform(0.2, 0.45)                  # 미도래
        base = rng.uniform(0.1, 0.25)
        onset_day = None
        for d in range(horizon + 1):
            if onset is None:
                s = base + 0.02 * d / horizon + rng.normal(0, 0.04)      # 완만·낮음
            else:
                # onset 부근에서 상승하는 로지스틱 곡선
                s = base + (peak - base) / (1 + np.exp(-(d - onset) * 1.1))
                s += rng.normal(0, 0.04)
            s = float(np.clip(s, 0, 1))
            rows.append({"individual_id": gid, "day": d, "score": round(s, 3)})
        truth.append({"individual_id": gid, "type": t,
                      "onset_true": None if onset is None else int(onset)})
    return pd.DataFrame(rows), pd.DataFrame(truth)


def timeline(days, scores) -> dict:
    """일자를 하루씩 진행하며(rolling) 경보가 처음 발화한 날을 기록.

    조기경보의 본질은 '오늘 시점' 판정이다. 각 날 d 까지의 관찰로 assess 해
    - imminent_day : '발정 임박'이 처음 뜬 날(선제 예측)
    - alert_day    : '발정지연/무발정 경보'가 처음 뜬 날
    - onset_actual : 실제 발정 확인일
    """
    days = list(map(float, days)); scores = list(map(float, scores))
    imminent_day = alert_day = None
    for i in range(len(days)):
        a = assess(days[: i + 1], scores[: i + 1])
        if imminent_day is None and a["state"] == "발정 임박":
            imminent_day = days[i]
        if alert_day is None and a["state"] in ("발정지연 경보", "무발정 경보"):
            alert_day = days[i]
    final = assess(days, scores)
    return {"imminent_day": imminent_day, "alert_day": alert_day,
            "onset_actual": final["onset_actual"], "final_state": final["state"],
            "peak": final["peak"]}


def run_demo() -> None:
    from sklearn.metrics import precision_score, recall_score
    long, truth = generate_daily()
    res = []
    for gid, g in long.groupby("individual_id"):
        g = g.sort_values("day")
        t = timeline(g["day"].tolist(), g["score"].tolist())
        t["individual_id"] = gid; res.append(t)
    rdf = pd.DataFrame(res).merge(truth, on="individual_id")

    print("=== 관찰 지평 종료 시점 상태 분포 ===")
    for s in STATES:
        n = int((rdf["final_state"] == s).sum())
        print(f"  {s:12s} {n:3d}두 ({n/len(rdf):.0%})")

    # 문제 = 정상 WEI(7일) 초과로 발정하거나 끝내 미도래(무발정). 도메인 정의.
    y_true = ((rdf["onset_true"].isna())
              | (rdf["onset_true"] > NORMAL_WEI)).astype(int)
    y_pred = rdf["alert_day"].notna().astype(int)
    print(f"\n발정지연·무발정 조기 포착(WEI>{NORMAL_WEI} 또는 무발정)  정밀도 "
          f"{precision_score(y_true, y_pred, zero_division=0):.2f}"
          f" | 재현율 {recall_score(y_true, y_pred, zero_division=0):.2f}"
          f"  (실제 문제 {int(y_true.sum())}두)")

    # 리드타임: 실제 발정일 - 임박 경보일(양수=며칠 앞서 경보)
    got = rdf[rdf["onset_actual"].notna() & rdf["imminent_day"].notna()].copy()
    if len(got):
        got["lead"] = got["onset_actual"] - got["imminent_day"]
        print(f"발정 임박 조기경보 리드타임 평균 {got['lead'].mean():+.1f}일 "
              f"(양수=선제), 중앙값 {got['lead'].median():+.1f}일 "
              f"| 대상 {len(got)}두")

    # 지연군을 정상 발정 상한(NORMAL_WEI={0})일 전에 경보한 비율
    dl = rdf[rdf["type"] == "delayed"]
    if len(dl):
        early = (dl["alert_day"].notna()
                 & (dl["alert_day"] <= dl["onset_actual"].fillna(999))).mean()
        print(f"발정지연군 {len(dl)}두 중 실제 발정 전에 경보 {early:.0%}")

    print("\n=== 개체 예시(유형별) ===")
    for t in ["normal", "delayed", "silent", "anestrus"]:
        sub = rdf[rdf["type"] == t]
        if not len(sub):
            continue
        r = sub.iloc[0]
        im = "-" if pd.isna(r["imminent_day"]) else f"{r['imminent_day']:.0f}일"
        al = "-" if pd.isna(r["alert_day"]) else f"{r['alert_day']:.0f}일"
        oa = "-" if pd.isna(r["onset_actual"]) else f"{r['onset_actual']:.0f}일"
        print(f"  [{t:8s}] {r['individual_id']} → 임박경보 {im} | 지연/무발정경보 {al}"
              f" | 실제발정 {oa} | 최종 {r['final_state']}")


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    run_demo()
