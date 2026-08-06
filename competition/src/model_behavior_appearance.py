"""행동 인식 개선 — 외형(크롭) 피처 추가 + before/after 비교.

기존 기하+모션 피처만으론 행동 인식이 약하다(정확도 ~0.43). Edinburgh 영상
프레임에서 각 돼지 bbox 크롭의 **외형 피처**(HSV 색상 히스토그램 + 그래디언트
방향 히스토그램)를 추가해 성능을 끌어올린다. 같은 개체가 train/test 에 섞이지
않도록 GroupKFold(individual_id).

    python competition/src/model_behavior_appearance.py
영상 캐시: /tmp/edin_vids/<rec>/color.mp4 (없으면 해당 녹화 제외)
"""
from __future__ import annotations

import json
import os
import sys

import cv2
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GroupKFold, cross_val_predict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import model_edinburgh_behavior as beh  # noqa: E402

EDIN = os.path.join(ROOT, "competition", "data", "edinburgh")
VID = "/tmp/edin_vids"
STEP = 3          # 영상프레임 = frameNumber × 3
CROP = 48         # 크롭 리사이즈
MIN_COUNT = 100


def crop_feats(bgr) -> np.ndarray:
    """크롭 → HSV 색 히스토그램(32) + 그래디언트 방향 히스토그램(8) = 40-D."""
    if bgr is None or bgr.size == 0:
        return np.zeros(40)
    im = cv2.resize(bgr, (CROP, CROP))
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    hh = cv2.calcHist([hsv], [0], None, [16], [0, 180]).flatten()  # 16
    sh = cv2.calcHist([hsv], [1], None, [8], [0, 256]).flatten()   # 8
    color = np.concatenate([hh, sh]); color = color / (color.sum() or 1)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32)
    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0); gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1)
    mag = np.sqrt(gx ** 2 + gy ** 2); ang = (np.arctan2(gy, gx) + np.pi)  # 0..2pi
    bins = np.minimum((ang / (2 * np.pi) * 16).astype(int), 15)
    oh = np.zeros(16)
    for b in range(16):
        oh[b] = mag[bins == b].sum()
    oh = oh / (oh.sum() or 1)
    return np.concatenate([color, oh])  # 16+8+16 = 40


def build_frames() -> pd.DataFrame:
    rows = []
    for date in sorted(os.listdir(EDIN)):
        dpath = os.path.join(EDIN, date)
        if not os.path.isdir(dpath):
            continue
        for vid in sorted(os.listdir(dpath)):
            oj = os.path.join(dpath, vid, "output.json")
            rec = f"{date}_{vid}"
            video = os.path.join(VID, rec, "color.mp4")
            if not (os.path.exists(oj) and os.path.exists(video)):
                continue
            d = json.load(open(oj, encoding="utf-8"))
            # frameNumber -> list of (uid, bbox, behavior)
            per_fn = {}
            for o in d["objects"]:
                uid = f"{rec}#{o['id']}"
                for f in o["frames"]:
                    if not f.get("visible", True):
                        continue
                    per_fn.setdefault(f["frameNumber"], []).append(
                        (uid, f["bbox"], f.get("behaviour")))
            cap = cv2.VideoCapture(video)
            needed = {fn * STEP: fn for fn in per_fn}
            idx = 0
            print(f"  {rec}: {len(per_fn)} 프레임 크롭 중...")
            while True:
                ok, frame = cap.read()
                if not ok:
                    break
                if idx in needed:
                    fn = needed[idx]
                    for uid, bb, behavior in per_fn[fn]:
                        x, y, w, h = int(bb["x"]), int(bb["y"]), int(bb["width"]), int(bb["height"])
                        crop = frame[max(0, y):y + h, max(0, x):x + w]
                        af = crop_feats(crop)
                        row = {"recording": rec, "individual_id": uid,
                               "frame_idx": fn, "behavior": behavior,
                               "bbox_w": w, "bbox_h": h,
                               "aspect_ratio": w / h if h else 0,
                               "centroid_x": x + w / 2, "centroid_y": y + h / 2}
                        for k in range(40):
                            row[f"a{k}"] = float(af[k])
                        rows.append(row)
                idx += 1
            cap.release()
    return pd.DataFrame(rows)


def evaluate(df: pd.DataFrame):
    df = beh.add_motion(df)
    vc = df["behavior"].value_counts()
    keep = set(vc[vc >= MIN_COUNT].index)
    df["behavior"] = df["behavior"].where(df["behavior"].isin(keep), "other")
    geom = ["bbox_w", "bbox_h", "aspect_ratio", "area", "speed", "accel",
            "darea", "centroid_x", "centroid_y"]
    app = [f"a{k}" for k in range(40)]
    df = df.dropna(subset=geom)
    y = df["behavior"].to_numpy(); groups = df["individual_id"].to_numpy()

    def run(cols, title):
        clf = RandomForestClassifier(n_estimators=250, min_samples_leaf=2,
                                     class_weight="balanced", n_jobs=-1, random_state=42)
        pred = cross_val_predict(clf, df[cols], y, cv=GroupKFold(5),
                                 groups=groups, n_jobs=-1)
        acc = accuracy_score(y, pred); mf1 = f1_score(y, pred, average="macro", zero_division=0)
        print(f"  {title:26s} 정확도 {acc:.3f} | Macro-F1 {mf1:.3f}")
        return acc, mf1

    print(f"\n프레임 {len(df)} | 개체 {df['individual_id'].nunique()} | "
          f"녹화 {df['recording'].nunique()} | 행동 {df['behavior'].nunique()}종")
    print("\n=== 행동 인식: 외형 피처 전/후 (GroupKFold) ===")
    b = run(geom, "기하+모션 (before)")
    a = run(geom + app, "+외형 피처 (after)")
    print(f"\n  변화: 정확도 {b[0]:.3f} → {a[0]:.3f} ({a[0]-b[0]:+.3f}) | "
          f"Macro-F1 {b[1]:.3f} → {a[1]:.3f} ({a[1]-b[1]:+.3f})")


def main() -> int:
    print("크롭 외형 피처 추출 중 (영상 필요)...")
    df = build_frames()
    if df.empty:
        print("영상 캐시 없음 (/tmp/edin_vids). 영상 다운로드 후 실행.")
        return 1
    evaluate(df)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
