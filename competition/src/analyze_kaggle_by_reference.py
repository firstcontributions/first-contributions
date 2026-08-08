"""AI Hub 71471 발정 표준으로 케글 데이터를 분석하는 프로그램.

흐름:
  1) 71471 표준(aihub_estrus_reference) 로드 — 발정 행동 기준.
  2) 케글 Edinburgh 행동 데이터를 개체 단위로 집계 → 표준 카테고리로 매핑 →
     표준 발정 기준으로 점수화(발정 의심 랭킹).
  3) (선택) 71471 실데이터(발정 정답 프레임 CSV)가 있으면 표준을 지도 보정하고
     AUC 를 보고(기준의 타당성 검증).
  4) 케글 탐지 데이터(multiview)의 활동량을 표준 활동 기준으로 요약(보조).

    python competition/src/analyze_kaggle_by_reference.py [71471_frames.csv]
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import aihub_estrus_reference as ref  # noqa: E402
import model_71471_estrus as est  # noqa: E402
import parse_edinburgh  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
EDIN = os.path.join(ROOT, "competition", "data", "edinburgh_frames.csv")


def individual_profiles(frames: pd.DataFrame) -> pd.DataFrame:
    """개체별: 표준 카테고리 비율 + 활동량(0~1)."""
    act = est.build_estrus_features(frames)[["individual_id", "activity_mean"]]
    a = act["activity_mean"].to_numpy(float)
    act["activity_norm"] = ((a - a.min()) / ((a.max() - a.min()) or 1)).round(3)
    bf = (frames.groupby("individual_id")["behavior"]
          .value_counts(normalize=True).unstack(fill_value=0.0))
    rows = []
    for iid, arow in act.set_index("individual_id").iterrows():
        frac = bf.loc[iid].to_dict() if iid in bf.index else {}
        rows.append({"individual_id": iid,
                     "activity_norm": float(arow["activity_norm"]),
                     "ref_fractions": ref.map_fractions(frac)})
    return pd.DataFrame(rows)


def analyze_edinburgh(reference: ref.EstrusReference) -> pd.DataFrame:
    frames = pd.read_csv(EDIN) if os.path.exists(EDIN) else \
        parse_edinburgh.parse_edinburgh(os.path.join(ROOT, "competition/data/edinburgh"))
    frames = frames[frames["behavior"].notna() & frames["centroid_x"].notna()]
    prof = individual_profiles(frames)
    scorer = reference.score_calibrated if reference.calibrated else reference.score
    prof["raw"] = [scorer(r, a) for r, a in
                   zip(prof["ref_fractions"], prof["activity_norm"])]
    r = prof["raw"].to_numpy()
    prof["estrus_index"] = ((r - r.min()) / ((r.max() - r.min()) or 1)).round(3)
    # 표준 기준 주요 유발 카테고리
    def drivers(fr):
        contrib = {c: reference.weights.get(c, 0) * fr.get(c, 0)
                   for c in ref.REFERENCE_BEHAVIORS}
        pos = sorted(((v, k) for k, v in contrib.items() if v > 0.02), reverse=True)
        return ", ".join(k for _, k in pos[:3]) or "-"
    prof["ref_drivers"] = prof["ref_fractions"].apply(drivers)
    return prof.sort_values("estrus_index", ascending=False)


def calibrate_from_71471(reference: ref.EstrusReference, csv: str) -> None:
    """71471 프레임 CSV(behavior, individual_id, estrus, centroid_*)로 표준 보정."""
    frames = pd.read_csv(csv)
    prof = individual_profiles(frames)
    # 개체별 발정 정답
    y = (frames.dropna(subset=["estrus"]).groupby("individual_id")["estrus"]
         .first())
    prof = prof[prof["individual_id"].isin(y.index)]
    yy = y.loc[prof["individual_id"]].astype(int).to_numpy()
    auc = reference.calibrate(list(prof["ref_fractions"]),
                              prof["activity_norm"].to_numpy(), yy)
    print(f"[표준 보정] 71471 발정 정답으로 지도 보정 완료 — 교차검증 AUC {auc:.3f} "
          f"(개체 {len(yy)}, 발정 {yy.mean():.0%})")


def analyze_detection_activity() -> None:
    """케글 탐지(multiview) 활동량을 표준 활동 기준으로 보조 요약."""
    try:
        import build_activity_analysis as act
    except Exception:  # noqa: BLE001
        return
    root = act.DEFAULT
    if not os.path.isdir(root):
        print("\n[탐지 활동] multiview 데이터 없음 — 생략")
        return
    sess = act.sessions(root)
    top = sorted(sess.items(), key=lambda kv: -len(kv[1]))[:5]
    print("\n=== 케글 탐지(multiview) 활동 요약 — 표준 활동 기준 ===")
    print("  (활동량 급증 시점 = 표준상 발정/이상행동 의심 후보)")
    for (pen, cam, date), fr in top:
        counts, activity, _ = act.analyze(fr)
        peak = int(np.argmax(activity)) if activity else 0
        print(f"  {pen}·{cam}·{date}({len(fr)}f): 평균 {np.mean(counts):.1f}두 · "
              f"최대활동 {max(activity):.3f} @F{peak}")


def main() -> int:
    reference = ref.EstrusReference()
    cal_csv = sys.argv[1] if len(sys.argv) > 1 else None
    if cal_csv and os.path.isfile(cal_csv):
        calibrate_from_71471(reference, cal_csv)
    else:
        print("[표준] 71471 실데이터 없음 → 규칙 기준(수의학 가중치) 사용. "
              "71471 프레임 CSV 를 인자로 주면 지도 보정+AUC 검증.")

    res = analyze_edinburgh(reference)
    mode = "보정됨" if reference.calibrated else "규칙기준"
    print(f"\n=== 케글 Edinburgh — 71471 발정 표준({mode}) 분석 ===")
    print(f"개체 {len(res)}두 | 발정 의심(지수≥0.6) {(res['estrus_index']>=0.6).sum()}두\n")
    cols = ["individual_id", "estrus_index", "activity_norm", "ref_drivers"]
    print("발정 의심 상위 8두:")
    print(res[cols].head(8).to_string(index=False))
    print("\n하위 4두(휴식 위주):")
    print(res[cols].tail(4).to_string(index=False))

    analyze_detection_activity()
    print("\n※ 표준 = AI Hub 71471 발정행동. 규칙 가중치는 71471 정답으로 보정 시 확정.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
