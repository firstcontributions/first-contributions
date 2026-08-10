"""교배사(스톨) 전용 발정 지표 — 활동량이 없는 환경에서 발정을 읽는다.

문제: 교배사·임신사는 **스톨(개별 사육틀)** 이라 모돈이 이동하지 못한다. 군사 사육의
주력 신호인 **활동량이 구조적으로 성립하지 않는다**(실측: 스톨 8.7px vs 군사 14.0px).
그러나 교배 의사결정은 바로 이 교배사에서 일어난다 — 여기서 못 하면 앱이 무의미하다.

전환: 스톨에서 관찰 가능한 것은 **자세와 그 시간적 변화**다. 발정 모돈은
  · 눕기가 줄고 **기립 비율이 오른다**(불안·서성임의 스톨 버전)
  · **자세 전환이 잦아진다**(누웠다 일어서기 반복)
  · 웅돈 접촉·압박 시 **부동자세(기립반사)** — 미동 없이 버틴다
  · 통로 쪽(웅돈 방향)으로 **머리를 향한다**

이 모듈은 개체별 자세 시계열에서 위 지표를 뽑고, 71471 표준 카테고리로 매핑해
`EstrusReference` 로 점수화한다. 개체가 스톨에 고정돼 **위치가 곧 개체 ID** 이므로
군사 사육에서 문제였던 추적 단편화가 없다 — 오히려 스톨이 유리한 점이다.

  입력: 개체별 프레임 시계열 [stall_id, frame_idx, posture, (bbox)]
        posture ∈ {lying, sitting, standing}
  출력: 개체별 지표 + 발정 점수 + 순위

    python competition/src/stall_estrus.py     # 합성 시연
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import aihub_estrus_reference as ref  # noqa: E402

STAND = {"standing", "stand", "기립"}
SIT = {"sitting", "sit", "기좌"}
LIE = {"lying", "lie", "lateral_lying", "sternal_lying", "sleep", "횡와"}

# 부동자세 판정: 기립 상태가 이 프레임 수 이상 '연속 유지'되면 후보
IMMOBILE_MIN_RUN = 8


def _canon(p) -> str:
    s = str(p).strip().lower()
    if s in STAND:
        return "standing"
    if s in SIT:
        return "sitting"
    if s in LIE:
        return "lying"
    return "other"


def stall_features(df: pd.DataFrame, id_col: str = "stall_id") -> pd.DataFrame:
    """개체별 자세 시계열 → 스톨 발정 지표.

    반환 컬럼:
      stand_frac     기립 비율(발정 시 ↑)
      lie_frac       눕기 비율(발정 시 ↓)
      transitions    자세 전환 횟수/프레임(불안정 = 발정 시 ↑)
      longest_stand  최장 연속 기립(프레임) — 부동자세 후보
      immobile_frac  기립을 IMMOBILE_MIN_RUN 이상 유지한 프레임 비율
      posture_entropy 자세 분포 엔트로피(전환 다양성)
    """
    d = df.copy()
    d["p"] = d["posture"].map(_canon)
    rows = []
    for sid, g in d.sort_values([id_col, "frame_idx"]).groupby(id_col, sort=False):
        p = g["p"].to_numpy()
        n = len(p)
        if n == 0:
            continue
        stand = float((p == "standing").mean())
        lie = float((p == "lying").mean())
        sit = float((p == "sitting").mean())
        trans = float((p[1:] != p[:-1]).sum()) / max(1, n - 1)
        # 연속 기립 구간
        runs, cur = [], 0
        for v in p:
            if v == "standing":
                cur += 1
            else:
                if cur:
                    runs.append(cur)
                cur = 0
        if cur:
            runs.append(cur)
        longest = max(runs) if runs else 0
        immobile = float(sum(r for r in runs if r >= IMMOBILE_MIN_RUN)) / n
        # 자세 분포 엔트로피
        fr = np.array([stand, lie, sit], dtype=float)
        fr = fr[fr > 0]
        ent = float(-(fr * np.log(fr)).sum()) if len(fr) else 0.0
        rows.append({id_col: sid, "n_frames": n,
                     "stand_frac": round(stand, 3), "lie_frac": round(lie, 3),
                     "sit_frac": round(sit, 3), "transitions": round(trans, 3),
                     "longest_stand": int(longest),
                     "immobile_frac": round(immobile, 3),
                     "posture_entropy": round(ent, 3)})
    return pd.DataFrame(rows)


def estrus_score(feat: pd.DataFrame, id_col: str = "stall_id") -> pd.DataFrame:
    """스톨 지표 → 71471 표준 카테고리로 매핑해 발정 점수·순위 산출.

    매핑 근거:
      · 기립 비율            → standing(약한 신호 0.15)
      · **부동자세 유지**     → immobility(1.0) — 스톨에서 가장 강한 관측 신호
      · 자세 전환 잦음        → restless(0.5) — 군사의 '서성임'에 대응
      · 눕기                 → lying(-0.6)
    활동량 대체값으로는 **자세 전환률**을 개체군 상대(0~1)로 정규화해 넣는다.
    """
    R = ref.EstrusReference()
    d = feat.copy()
    if not len(d):
        return d
    tr = d["transitions"].to_numpy(dtype=float)
    scale = np.percentile(tr, 95) or 1.0
    d["activity_proxy"] = np.clip(tr / scale, 0, 1)
    scores = []
    for r in d.itertuples(index=False):
        frac = {"standing": float(r.stand_frac),
                "immobility": float(r.immobile_frac),
                "restless": float(min(1.0, r.transitions * 3.0)),
                "lying": float(r.lie_frac),
                "sitting": float(r.sit_frac)}
        scores.append(R.score(frac, float(getattr(r, "activity_proxy", 0.0))))
    d["estrus_score"] = np.round(scores, 3)
    d["rank"] = d["estrus_score"].rank(ascending=False, method="min").astype(int)
    return d.sort_values("estrus_score", ascending=False).reset_index(drop=True)


# --------------------------------------------------------------------------
def generate_demo(n_stalls: int = 24, frames: int = 120, seed: int = 3):
    """스톨 자세 시계열 합성. 일부 개체를 발정(기립↑·전환↑·부동자세)으로 만든다."""
    rng = np.random.default_rng(seed)
    rows, truth = [], []
    for i in range(n_stalls):
        est = 1 if rng.random() < 0.25 else 0
        truth.append({"stall_id": f"S{i:02d}", "estrus": est})
        # 개체차를 크게 줘 분포가 **겹치게** 한다. 발정/비발정을 완전 분리하면
        # AUC 1.0 같은 비현실적 수치가 나와 시연이 오히려 오해를 부른다
        # (원래 잘 눕지 않는 모돈, 발정인데도 조용한 모돈이 실제로 존재한다).
        ind = float(rng.normal(0, 0.13))            # 개체 성향
        base_stand = (0.42 if est else 0.26) + ind
        base_stand = float(np.clip(base_stand, 0.05, 0.85))
        if est:
            probs = {"standing": base_stand, "sitting": 0.10,
                     "lying": max(0.05, 1 - base_stand - 0.10)}
            switch = float(np.clip(rng.normal(0.16, 0.05), 0.03, 0.35))
        else:
            probs = {"standing": base_stand, "sitting": 0.08,
                     "lying": max(0.05, 1 - base_stand - 0.08)}
            switch = float(np.clip(rng.normal(0.09, 0.04), 0.02, 0.30))
        keys = list(probs); w = np.array([probs[k] for k in keys]); w = w / w.sum()
        cur = rng.choice(keys, p=w)
        for f in range(frames):
            if rng.random() < switch:
                cur = rng.choice(keys, p=w)
            rows.append({"stall_id": f"S{i:02d}", "frame_idx": f, "posture": cur})
    return pd.DataFrame(rows), pd.DataFrame(truth)


def degrade(ts: pd.DataFrame, acc: float, seed: int = 0,
            id_col: str = "stall_id") -> pd.DataFrame:
    """자세 인식 오류를 주입한다 — 상류 정확도가 발정 판정에 얼마나 전파되는가.

    자세 시계열은 공짜로 주어지지 않는다. 못 본 카메라에서 3클래스 정확도는
    실측 0.513(기존) ~ 0.636(개선)이다. 그 오차를 넣고 다시 재야 "자세 병목을
    푼 것이 발정 판정에 실제로 값을 하는가"를 답할 수 있다.

    오류 모형은 단순화다 — 확률 (1-acc) 로 다른 자세를 균등 추출한다. 실제
    혼동은 비대칭(횡와↔기립이 많다)이므로 이 추정은 낙관·비관 어느 쪽으로도
    치우칠 수 있다. 정확한 전파를 보려면 실측 혼동행렬을 써야 한다.
    """
    rng = np.random.default_rng(seed)
    d = ts.copy()
    p = d["posture"].map(_canon).to_numpy(dtype=object)
    kinds = np.array(["standing", "sitting", "lying"], dtype=object)
    flip = rng.random(len(p)) > float(acc)
    for i in np.nonzero(flip)[0]:
        alt = kinds[kinds != p[i]]
        if len(alt):
            p[i] = alt[rng.integers(len(alt))]
    d["posture"] = p
    return d


def main() -> int:
    from sklearn.metrics import roc_auc_score
    ts, truth = generate_demo()
    feat = stall_features(ts)
    sc = estrus_score(feat).merge(truth, on="stall_id")
    auc = roc_auc_score(sc["estrus"], sc["estrus_score"])
    print(f"스톨 {len(sc)}개 · 프레임 {ts['frame_idx'].nunique()} · "
          f"발정 {int(sc['estrus'].sum())}두")
    print(f"발정 점수 AUC {auc:.3f}  (합성 시연 — 실측 아님)\n")
    print(f"{'스톨':>5} {'기립':>6} {'눕기':>6} {'전환':>6} {'부동':>6} "
          f"{'점수':>7} {'정답':>4}")
    for r in sc.head(10).itertuples(index=False):
        print(f"{r.stall_id:>5} {r.stand_frac:>6.2f} {r.lie_frac:>6.2f} "
              f"{r.transitions:>6.2f} {r.immobile_frac:>6.2f} "
              f"{r.estrus_score:>7.3f} {'발정' if r.estrus else '-':>4}")
    print("\n=== 자세 인식 오류의 전파 (상류 정확도 → 발정 판정 AUC) ===")
    print("  자세 시계열은 공짜가 아니다. 못 본 카메라의 3클래스 실측치를 넣고 다시 잰다.")
    print("  스톨 200개 · 시드 20회 평균 — 24개/5회로 재니 순서가 뒤집힐 만큼"
          "\n  시드 분산이 커서 표본을 늘렸다.")
    big_ts, big_truth = generate_demo(n_stalls=200, frames=120, seed=3)
    prop = {}
    for acc, lab in ((1.00, "완벽(참고)"), (0.636, "개선 후(크롭+뷰정규화)"),
                     (0.547, "다수 클래스 기준선"), (0.513, "기존(기하만)")):
        aucs = []
        for s in range(1 if acc >= 1.0 else 20):
            n = big_ts if acc >= 1.0 else degrade(big_ts, acc, seed=s)
            sc2 = estrus_score(stall_features(n)).merge(big_truth, on="stall_id")
            aucs.append(roc_auc_score(sc2["estrus"], sc2["estrus_score"]))
        prop[acc] = float(np.mean(aucs))
        print(f"  자세 정확도 {acc:.3f} ({lab:<20}) → 발정 AUC "
              f"{np.mean(aucs):.3f} ± {np.std(aucs):.3f}")
    gain, gap = prop[0.636] - prop[0.513], prop[1.00] - prop[0.513]
    print(f"  → 자세 0.513→0.636 개선이 발정 AUC 를 {gain:+.3f} 올린다"
          f"(완벽 자세까지의 격차 {gap:.3f} 중 {gain / gap:.0%} 회수).")
    print("  → 전파는 있으나 1:1 이 아니다. 자세 오차가 시계열 통계(전환율·부동)로"
          "\n    집계되며 일부 상쇄되기 때문이다. 오류 모형은 균등 추출 단순화이고"
          "\n    실제 혼동은 비대칭(횡와↔기립)이라 이 값은 어림치다.")

    print("\n※ 스톨은 개체가 고정돼 **위치가 곧 개체 ID** — 군사 사육의 추적 단편화 문제가"
          "\n  없다. 대신 활동량이 없으므로 자세·전환·부동자세로 판정한다.")
    print("※ 합성 데이터 시연이다. 실측에는 스톨 자세 시계열 + 발정 정답이 필요하다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
