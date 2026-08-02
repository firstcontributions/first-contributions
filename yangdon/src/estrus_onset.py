"""시간 윈도우 기반 발정 시작점(onset) 탐지.

개체의 프레임 시계열에서 활동량·발정행동을 슬라이딩 윈도우로 합산해
발정 점수를 만들고, 점수가 임계값을 지속적으로 넘는 첫 시점을 '발정 시작'
으로 본다. 끝까지 넘지 않으면 '무발정(anestrus)'으로 표시한다.

프레임 활동량 = 직전 프레임 대비 중심(centroid) 이동거리.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

ESTRUS_BEHAVIORS = ("standing", "tailing")


def _per_frame(gf: pd.DataFrame) -> pd.DataFrame:
    gf = gf.sort_values("frame_idx").copy()
    dx = gf["centroid_x"].astype(float).diff()
    dy = gf["centroid_y"].astype(float).diff()
    gf["activity"] = np.sqrt(dx ** 2 + dy ** 2).fillna(0.0)
    gf["is_estrus_beh"] = gf["behavior"].isin(ESTRUS_BEHAVIORS).astype(float)
    return gf


def detect_onset(gf: pd.DataFrame, window: int = 5,
                 act_ref: float = 25.0, threshold: float = 0.5,
                 sustain: int = 2) -> dict:
    """한 개체의 프레임들 → 발정 점수 시계열 + 시작점/상태.

    act_ref : 활동량 정규화 기준(모집단 상위 활동 수준). 실데이터에서 분포로 보정.
    threshold, sustain : 점수가 threshold 이상을 sustain 윈도우 연속 유지하면 발정 시작.
    """
    gf = _per_frame(gf)
    n = len(gf)
    frames = gf["frame_idx"].astype(int).tolist()
    act = gf["activity"].to_numpy()
    beh = gf["is_estrus_beh"].to_numpy()

    # 슬라이딩 윈도우(뒤쪽 window개) 평균
    score = np.zeros(n)
    for i in range(n):
        lo = max(0, i - window + 1)
        a = np.clip(act[lo:i + 1].mean() / act_ref, 0, 1)   # 활동 성분
        b = beh[lo:i + 1].mean()                            # 행동 성분
        score[i] = round(0.6 * a + 0.4 * b, 3)

    # 지속 임계 충족 첫 시점
    onset_frame = None
    run = 0
    for i in range(n):
        run = run + 1 if score[i] >= threshold else 0
        if run >= sustain:
            onset_frame = frames[i - sustain + 1]
            break

    return {
        "frames": frames,
        "activity": [round(float(x), 2) for x in act],
        "score": [float(x) for x in score],
        "onset_frame": onset_frame,
        "status": "estrus" if onset_frame is not None else "anestrus",
        "peak_score": round(float(score.max()), 3) if n else 0.0,
    }


def detect_all(frames: pd.DataFrame, **kw) -> dict[str, dict]:
    """개체별 onset 탐지 결과 딕셔너리."""
    return {str(gid): detect_onset(g, **kw)
            for gid, g in frames.groupby("individual_id")}


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import pipeline_gilt
    fr, _ = pipeline_gilt.generate_joint(n_gilts=6, frames=20)
    for gid, res in detect_all(fr).items():
        print(f"{gid}: status={res['status']} onset={res['onset_frame']} "
              f"peak={res['peak_score']}")
