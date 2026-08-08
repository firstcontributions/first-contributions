"""AI Hub 71471 [Keypoints] 서브셋 파서 + 자세(pose) 피처.

실제 스키마(2023 rework 배포본):

    {"INFO": {"DATASET_NAME": "[Keypoints]돼지(백돼지) 발정행동 데이터 - rework"},
     "IMAGE": {"IMAGE_FILE_NAME": "pigfarmA_ch9_2022080509_334_663233.jpg",
               "WIDTH":1920, "HEIGHT":1080, "TIMESTAMP":663233, "FARMID":"pigfarmA"},
     "ANNOTATION_INFO": [
        {"ID":2648664,
         "KEYPOINTS":[x1,y1,v1, x2,y2,v2, ...],   # COCO 방식 평면 리스트
         "NUM_KEYPIONTS":8,                        # (원문 오타 그대로)
         "CATEGORY_NAME":"pig", "ACTION_NAME":"lying", "ESTRUS":"N"}]}

**왜 keypoints 인가**: [Bbox] 서브셋은 행동 어휘가 4종(lying/standing/sitting/
eating)뿐이고 발정 지시 행동(꼬리세움·승가·기립반사)이 없어 발정 판정이 불가했다
(docs/AIHUB.md 참조). keypoints 는 **관절 좌표**라 라벨 어휘에 의존하지 않고
자세를 직접 기하로 계산할 수 있다 — 라벨의 한계를 우회하는 경로.

부위명(코·귀·꼬리 등)은 명세에 없으므로, **부위명이 필요 없는 회전·평행이동·
크기 불변 기술자**를 쓴다:
  · 정규화 쌍거리 28개(8점 → C(8,2)) : 자세 형태 그 자체
  · PCA 주축비(elongation)            : 몸이 늘어졌는지 웅크렸는지
  · 산포(spread)·볼록껍질 면적비       : 사지를 편 정도
  · 가시성 패턴 8개                    : 가림 = 자세/겹침 정보
이 기술자는 개체가 어느 방향을 보든 동일하게 계산된다.

    python competition/src/parse_71471_keypoints.py <라벨디렉터리>
"""
from __future__ import annotations

import glob
import itertools
import json
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import parse_71471_real as p71  # noqa: E402  (파일명 규칙 재사용)

NK = 8                                   # 개체당 키포인트 수
PAIRS = list(itertools.combinations(range(NK), 2))   # 28쌍
PAIR_COLS = [f"d{i}_{j}" for i, j in PAIRS]
VIS_COLS = [f"v{k}" for k in range(NK)]
POSE_COLS = ["kp_n_vis", "kp_spread", "kp_elong", "kp_hull_ratio",
             "kp_w", "kp_h", "kp_aspect", "kp_area"]


def _kp_array(flat) -> np.ndarray | None:
    """평면 리스트 → (NK,3) 배열. 길이가 안 맞으면 None."""
    if not flat or len(flat) < NK * 3:
        return None
    a = np.asarray(flat[: NK * 3], dtype=float).reshape(NK, 3)
    return a


def pose_features(kp: np.ndarray) -> dict:
    """(NK,3) 키포인트 → 회전·크기 불변 자세 기술자.

    가시성 0(미표기) 인 점은 형태 계산에서 제외하되, 쌍거리는 결측(NaN)로 둔다.
    """
    xy = kp[:, :2]
    vis = kp[:, 2]
    ok = vis > 0
    out = {f"v{k}": float(vis[k]) for k in range(NK)}
    out["kp_n_vis"] = float(ok.sum())
    P = xy[ok]
    if len(P) < 3:
        for c in POSE_COLS:
            out.setdefault(c, np.nan)
        for c in PAIR_COLS:
            out[c] = np.nan
        return out
    c = P.mean(axis=0)
    d = np.linalg.norm(P - c, axis=1)
    scale = d.mean() or 1.0                       # 크기 정규화 기준
    out["kp_spread"] = float(d.std() / scale)
    # PCA 주축비 — 몸의 늘어짐(1에 가까울수록 웅크림, 클수록 길쭉)
    cov = np.cov((P - c).T)
    ev = np.linalg.eigvalsh(cov) if cov.shape == (2, 2) else np.array([1.0, 1.0])
    ev = np.clip(ev, 1e-9, None)
    out["kp_elong"] = float(np.sqrt(ev[-1] / ev[0]))
    w = float(P[:, 0].max() - P[:, 0].min())
    h = float(P[:, 1].max() - P[:, 1].min())
    out["kp_w"], out["kp_h"] = w, h
    out["kp_aspect"] = float(w / h) if h else np.nan
    out["kp_area"] = w * h
    # 볼록껍질 면적 / 외접사각 면적 — 사지를 편 정도
    try:
        from scipy.spatial import ConvexHull
        out["kp_hull_ratio"] = float(ConvexHull(P).volume / (w * h)) if w * h else np.nan
    except Exception:  # noqa: BLE001  (scipy 없거나 퇴화 시)
        out["kp_hull_ratio"] = np.nan
    # 정규화 쌍거리 — 자세 형태 그 자체(회전·평행이동·크기 불변)
    for (i, j), col in zip(PAIRS, PAIR_COLS):
        if vis[i] > 0 and vis[j] > 0:
            out[col] = float(np.linalg.norm(xy[i] - xy[j]) / scale)
        else:
            out[col] = np.nan
    return out


def parse_dir(label_dir: str) -> pd.DataFrame:
    """keypoints 라벨 디렉터리 → 인스턴스 단위 테이블(자세 피처 포함)."""
    rows = []
    for path in glob.glob(os.path.join(label_dir, "**", "*.json"), recursive=True):
        try:
            obj = json.load(open(path, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        anns = obj.get("ANNOTATION_INFO")
        if not anns:
            continue
        img = obj.get("IMAGE", {}) or {}
        fn = os.path.basename(path)
        nm = p71.parse_name(img.get("IMAGE_FILE_NAME") or fn)
        farm = img.get("FARMID") or nm["farm"]
        ts = img.get("TIMESTAMP")
        session = "_".join(str(x) for x in
                           (farm, nm["channel"], nm["datetime"]) if x)
        for a in anns:
            kp = _kp_array(a.get("KEYPOINTS"))
            if kp is None:
                continue
            est = str(a.get("ESTRUS") or "").upper()
            r = {"file": fn, "farm": farm, "channel": nm["channel"],
                 "session": session, "animal": nm["pen"],
                 "date": (nm["datetime"] or "")[:8],
                 "frame_idx": int(ts) if ts is not None else nm["ts"],
                 "ann_id": a.get("ID"), "behavior": a.get("ACTION_NAME"),
                 "estrus": 1 if est.startswith("Y") else 0 if est.startswith("N") else None,
                 "cx": float(kp[kp[:, 2] > 0][:, 0].mean()) if (kp[:, 2] > 0).any() else np.nan,
                 "cy": float(kp[kp[:, 2] > 0][:, 1].mean()) if (kp[:, 2] > 0).any() else np.nan}
            r.update(pose_features(kp))
            rows.append(r)
    return pd.DataFrame(rows)


FEATURES = POSE_COLS + VIS_COLS + PAIR_COLS


def summarize(df: pd.DataFrame) -> str:
    if not len(df):
        return "파싱 결과 없음 — 경로/스키마 확인 필요"
    lines = [f"인스턴스 {len(df):,} | 파일 {df['file'].nunique():,} | "
             f"개체 {df['animal'].nunique()} | 채널 {df['channel'].nunique()} | "
             f"날짜 {df['date'].nunique()}"]
    if df["estrus"].notna().any():
        lines.append(f"ESTRUS(돈방 라벨) Y {int(df['estrus'].sum()):,} "
                     f"({df['estrus'].mean():.1%})")
    lines.append("행동: " + ", ".join(
        f"{k} {v:,}" for k, v in df["behavior"].value_counts().head(6).items()))
    lines.append(f"자세 피처 {len(FEATURES)}개 "
                 f"(가시 관절 평균 {df['kp_n_vis'].mean():.1f}/{NK}, "
                 f"주축비 평균 {df['kp_elong'].mean():.2f})")
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    df = parse_dir(sys.argv[1])
    print(summarize(df))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
