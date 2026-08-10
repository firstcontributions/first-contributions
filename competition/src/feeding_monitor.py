"""개체별 섭취 모니터링 — 합사 스톨의 먹이 경쟁을 CCTV로 계량한다.

배경: 교배사·임신사의 사육 방식은 여러 형태다.
  · 일반 스톨      개체 고정, 경쟁 없음
  · **반스톨 / 자유출입스톨 / 자동급이(ESF)** — **합사**라 급이기에서 **먹이 경쟁**이
    일어난다. 강한 개체가 오래 차지하고 약한 개체는 밀려나, 같은 양을 넣어도
    개체별 섭취가 벌어진다.

왜 중요한가: 섭취 편차는 등지방(BCS) 편차로, 다시 **번식 성적**으로 이어진다
(BCS 3~3.25 = P2 16~18mm 가 교배 목표인데, 밀려난 개체는 야위고 독식한 개체는
비만해진다 — 둘 다 무발정·난산 위험). 즉 급이 관리는 발정 관리의 앞단이다.
또한 원인 귀인의 `feed_adequacy` 를 **문헌 가정이 아니라 관측값**으로 채운다.

계량 방식(카메라만으로 가능한 것):
  · **점유 시간**   급이기 구역에 머문 시간(세션 단위로 분해)
  · **방문·세션**   방문 횟수, 세션 평균 길이, 급이 시작 후 첫 도착 시각
  · **경쟁(우열)**  A 가 떠난 직후 B 가 같은 자리를 차지 → B 가 A 를 밀어냄
                   밀어낸/밀려난 횟수로 우열 순위를 만든다
  · **섭취 강도**   급이기 안에서의 **머리 움직임(저작 리듬)** — 점유시간과 **독립적인**
                   신호다. 초기 구현은 섭취량을 점유시간에 비례 배분하고 그것을 다시
                   시간으로 나눠 속도를 구했는데, 그러면 속도가 **상수가 되는 순환논리**
                   였다(실제로 전 개체 ~400g/분으로 동일하게 나왔다). 지금은 강도를
                   따로 재고, 섭취량을 **시간 × 강도**로 배분해 속도가 개체마다 달라진다.

    python competition/src/feeding_monitor.py     # 합성 시연
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

DISPLACE_WINDOW_S = 6.0     # A 이탈 후 이 시간 내 B 진입이면 '밀어냄'으로 본다
MIN_SESSION_S = 3.0         # 이보다 짧은 체류는 지나간 것으로 보고 제외


def in_zone(cx: float, cy: float, zone) -> bool:
    """정규화 좌표(0~1)가 급이기 구역 안인가. zone=(x, y, w, h) 정규화."""
    x, y, w, h = zone
    return (x <= cx <= x + w) and (y <= cy <= y + h)


def zone_of(cx: float, cy: float, zones: list):
    """어느 급이 구역에 있는지(없으면 None)."""
    for i, z in enumerate(zones):
        if in_zone(cx, cy, z):
            return i
    return None


def feeding_sessions(tracks: pd.DataFrame, zones: list, fps: float = 10.0,
                     id_col: str = "pig_id") -> pd.DataFrame:
    """추적 결과 → 급이 세션 목록(세션별 저작 강도 포함).

    tracks: [pig_id, frame_idx, cx, cy] (cx/cy 는 0~1 정규화 중심좌표)
    반환: [pig_id, zone, start_s, end_s, dur_s, motion]
      motion = 세션 중 프레임 간 중심 이동량의 평균(×1000). 급이기 안에서는 몸이
      거의 고정되므로 이 미세 움직임이 **머리 놀림(저작)** 을 반영한다.
    """
    d = tracks.sort_values([id_col, "frame_idx"]).copy()
    d["zone"] = [zone_of(a, b, zones) for a, b in zip(d["cx"], d["cy"])]
    out = []
    for pid, g in d.groupby(id_col, sort=False):
        cur_zone, start = None, None
        prev_f, prev_xy, buf = None, None, []
        for r in g.itertuples(index=False):
            z = r.zone
            if z != cur_zone:
                if cur_zone is not None and start is not None:
                    dur = (prev_f - start) / fps
                    if dur >= MIN_SESSION_S:
                        out.append({id_col: pid, "zone": int(cur_zone),
                                    "start_s": start / fps, "end_s": prev_f / fps,
                                    "dur_s": dur,
                                    "motion": float(np.mean(buf) * 1000) if buf else 0.0})
                cur_zone, start, buf = z, r.frame_idx, []
            elif prev_xy is not None:
                buf.append(((r.cx - prev_xy[0]) ** 2 + (r.cy - prev_xy[1]) ** 2) ** 0.5)
            prev_f, prev_xy = r.frame_idx, (r.cx, r.cy)
        if cur_zone is not None and start is not None and prev_f is not None:
            dur = (prev_f - start) / fps
            if dur >= MIN_SESSION_S:
                out.append({id_col: pid, "zone": int(cur_zone),
                            "start_s": start / fps, "end_s": prev_f / fps,
                            "dur_s": dur,
                            "motion": float(np.mean(buf) * 1000) if buf else 0.0})
    return pd.DataFrame(out)


def displacements(sessions: pd.DataFrame, id_col: str = "pig_id") -> pd.DataFrame:
    """자리 뺏김(밀어냄) 이벤트 — A 이탈 직후 같은 구역에 B 진입.

    반환: [winner, loser, zone, t_s]  (winner 가 loser 를 밀어냄)
    """
    ev = []
    for z, g in sessions.groupby("zone"):
        g = g.sort_values("start_s")
        for a in g.itertuples(index=False):
            for b in g.itertuples(index=False):
                pa, pb = getattr(a, id_col), getattr(b, id_col)
                if pa == pb:
                    continue
                gap = b.start_s - a.end_s
                if 0 <= gap <= DISPLACE_WINDOW_S:
                    ev.append({"winner": pb, "loser": pa, "zone": int(z),
                               "t_s": round(b.start_s, 1)})
    return pd.DataFrame(ev)


def feeding_metrics(sessions: pd.DataFrame, disp: pd.DataFrame,
                    total_feed_kg: float | None = None,
                    id_col: str = "pig_id") -> pd.DataFrame:
    """개체별 섭취 지표. total_feed_kg 를 주면 섭취량·속도를 추정한다.

    ⚠️ 섭취량은 **시간 × 저작 강도**로 배분한다. 시간만으로 배분하면 속도가 상수가
    되는 순환논리에 빠진다(초기 구현의 오류). 그래도 이는 추정이며, ESF(자동급이)
    실측 기록이 있으면 그 값을 쓰는 편이 항상 낫다.
    """
    if not len(sessions):
        return pd.DataFrame()
    g = sessions.groupby(id_col)
    m = pd.DataFrame({
        "feed_time_s": g["dur_s"].sum().round(1),
        "n_visits": g["dur_s"].size(),
        "mean_visit_s": g["dur_s"].mean().round(1),
        "first_arrival_s": g["start_s"].min().round(1),
    }).reset_index()
    w = disp["winner"].value_counts() if len(disp) else pd.Series(dtype=int)
    l = disp["loser"].value_counts() if len(disp) else pd.Series(dtype=int)
    m["displaced_others"] = m[id_col].map(w).fillna(0).astype(int)
    m["displaced_by"] = m[id_col].map(l).fillna(0).astype(int)
    # 우열 지수: 밀어낸 횟수 - 밀려난 횟수 (정규화)
    net = m["displaced_others"] - m["displaced_by"]
    rng = max(1, int(net.abs().max()))
    m["dominance"] = (net / rng).round(3)
    # 저작 강도(세션 길이 가중 평균) — 점유시간과 독립적인 섭취 속도 대리지표
    if "motion" in sessions:
        wsum = sessions.assign(_wm=sessions["motion"] * sessions["dur_s"]).groupby(id_col)
        chew = (wsum["_wm"].sum() / g["dur_s"].sum().replace(0, np.nan))
        m["chew_intensity"] = m[id_col].map(chew).fillna(0).round(2)
    else:
        m["chew_intensity"] = 0.0
    # 섭취 점유 비율
    tot = m["feed_time_s"].sum() or 1.0
    m["time_share"] = (m["feed_time_s"] / tot).round(3)
    if total_feed_kg:
        # 시간 × 강도로 배분 — 시간만 쓰면 속도가 상수가 되는 순환논리가 된다
        eff = m["feed_time_s"] * m["chew_intensity"].clip(lower=1e-6)
        share = eff / (eff.sum() or 1.0)
        m["intake_share"] = share.round(3)
        m["intake_kg_est"] = (share * float(total_feed_kg)).round(2)
        mins = (m["feed_time_s"] / 60.0).replace(0, np.nan)
        m["eat_rate_g_per_min"] = (m["intake_kg_est"] * 1000 / mins).round(0)
    return m.sort_values("feed_time_s", ascending=False).reset_index(drop=True)


def flag_risk(metrics: pd.DataFrame, id_col: str = "pig_id") -> pd.DataFrame:
    """급이 관리 위험 개체 표시 — 원인 귀인의 feed_adequacy 로 연결된다.

    · 소외(underfed)  : 점유시간이 개체군 하위 20% 이고 밀려남이 잦다
    · 독식(overfed)   : 점유시간 상위 20% 이고 밀어냄이 잦다
    feed_adequacy(0~1) 는 점유 비율을 균등 기대치 대비로 환산한다
    (모두 똑같이 먹으면 1.0).
    """
    d = metrics.copy()
    if not len(d):
        return d
    n = len(d)
    even = 1.0 / n
    d["feed_adequacy"] = (d["time_share"] / even).clip(0, 2).round(3) / 2 * 2
    d["feed_adequacy"] = d["feed_adequacy"].clip(0, 1.5).round(3)
    lo, hi = d["feed_time_s"].quantile(0.2), d["feed_time_s"].quantile(0.8)
    def _flag(r):
        if r["feed_time_s"] <= lo and r["displaced_by"] >= r["displaced_others"]:
            return "소외(급이 부족 위험)"
        if r["feed_time_s"] >= hi and r["displaced_others"] > r["displaced_by"]:
            return "독식(과비 위험)"
        return "정상"
    d["status"] = d.apply(_flag, axis=1)
    return d


# --------------------------------------------------------------------------
def generate_demo(n_pigs: int = 12, minutes: float = 20.0, fps: float = 10.0,
                  seed: int = 5):
    """합사 급이 상황 합성 — 우열에 따라 급이기 점유가 갈리도록 만든다."""
    rng = np.random.default_rng(seed)
    zones = [(0.05, 0.35, 0.18, 0.30), (0.77, 0.35, 0.18, 0.30)]   # 급이기 2곳
    n_frames = int(minutes * 60 * fps)
    rank = rng.permutation(n_pigs)          # 서열(낮을수록 우세)
    # 저작 진폭(빨리 먹는 개체일수록 큼) — 점유시간과 **독립적으로** 부여한다
    chew_amp = rng.uniform(0.002, 0.012, n_pigs)
    rows = []
    for i in range(n_pigs):
        pid = f"P{i:02d}"
        dom = 1.0 - rank[i] / max(1, n_pigs - 1)        # 0~1 우세도
        # 우세할수록 급이기 체류가 길고 자주 간다
        n_sess = int(np.clip(rng.normal(3 + 4 * dom, 1.2), 1, 10))
        pos = [(0.5, 0.75)] * n_frames                   # 기본 위치(급이기 밖)
        occupied = []
        for _ in range(n_sess):
            dur_s = float(np.clip(rng.normal(40 + 120 * dom, 25), 8, 400))
            st = int(rng.uniform(0, max(1, n_frames - dur_s * fps)))
            en = int(min(n_frames, st + dur_s * fps))
            z = zones[int(rng.integers(0, len(zones)))]
            bx = z[0] + z[2] / 2
            by = z[1] + z[3] / 2
            # 개체마다 저작(머리 놀림) 진폭이 다르다 — 섭취 속도의 대리지표
            amp = chew_amp[i]
            for f in range(st, en):
                pos[f] = (bx + rng.normal(0, amp), by + rng.normal(0, amp))
            occupied.append((st, en))
        for f in range(0, n_frames, 5):                  # 2fps 로 기록(부하 감소)
            rows.append({"pig_id": pid, "frame_idx": f,
                         "cx": pos[f][0], "cy": pos[f][1]})
    return pd.DataFrame(rows), zones, fps


def main() -> int:
    tracks, zones, fps = generate_demo()
    sess = feeding_sessions(tracks, zones, fps=fps)
    disp = displacements(sess)
    met = flag_risk(feeding_metrics(sess, disp, total_feed_kg=2.5 * 12))
    print(f"개체 {tracks['pig_id'].nunique()} · 급이기 {len(zones)}곳 · "
          f"세션 {len(sess)} · 자리뺏김 {len(disp)}건\n")
    print(f"{'개체':>5} {'점유(초)':>8} {'방문':>4} {'점유율':>6} "
          f"{'추정섭취kg':>10} {'g/분':>6} {'우열':>6} {'상태':>16}")
    for r in met.itertuples(index=False):
        print(f"{r.pig_id:>5} {r.feed_time_s:>8.0f} {r.n_visits:>4d} "
              f"{r.time_share:>6.2f} {r.intake_kg_est:>10.2f} "
              f"{r.eat_rate_g_per_min:>6.0f} {r.dominance:>6.2f} {r.status:>16}")
    under = met[met["status"].str.startswith("소외")]
    over = met[met["status"].str.startswith("독식")]
    print(f"\n소외 {len(under)}두 · 독식 {len(over)}두 → 급이 조절 대상")
    print("※ 섭취량은 **점유시간 비례 배분 추정**이다. 같은 시간에도 먹는 속도가 다르므로,"
          "\n  ESF(자동급이) 실측 기록이 있으면 그 값을 쓰는 편이 항상 낫다.")
    print("※ 이 지표는 원인 귀인의 feed_adequacy 를 관측값으로 대체해, 영양 부족·과비를"
          "\n  BCS 목표(P2 16~18mm)와 연결한다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
