"""추적 파라미터 탐색 — 과분할의 진짜 원인을 찾아 최적 설정을 고른다.

진단 결과(국내 축사 영상): 과분할 20.3배의 주원인은 **카메라 흔들림이 아니라
탐지 불안정**이었다.
  · 카메라 이동 평균 6.97px (박스 크기 대비 작음) → 모션 보상은 14% 개선에 그침
  · **탐지 흔들림 3.02마리/프레임**(마릿수 16 중 19%가 매 프레임 명멸)
매 프레임 3마리가 사라졌다 나타나면 트랙이 죽고 새로 생기기를 반복한다.

그래서 조정할 손잡이는 셋이다:
  · conf     — 낮추면 명멸이 줄지만 오탐이 는다
  · max_age  — 크게 하면 잠깐 놓쳐도 트랙이 버틴다(명멸에 직접 대응)
  · merge    — 창살에 쪼개진 박스를 합쳐 마릿수·매칭을 안정화

효율 설계: YOLO 를 **한 번만** 돌려 프레임별 박스를 캐시하고(낮은 임계로 넉넉히),
그 위에서 파라미터만 쓸어본다. 매 조합마다 추론하면 수십 배 느리다.

    python competition/src/tracking_sweep.py <영상.mp4>
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import box_merge as bm  # noqa: E402
import motion_tracker as mt  # noqa: E402

CACHE_CONF = 0.15      # 캐시는 넉넉히 잡고, 스윕에서 걸러낸다


def cache_detections(video: str, model_path: str | None = None, step: int = 3,
                     max_frames: int = 200) -> dict:
    """YOLO 1회 실행 → 프레임별 (박스, 신뢰도) + 카메라 변환 캐시."""
    import cv2
    from ultralytics import YOLO
    import analyze_video as av
    mp = av.find_model(model_path)
    if mp is None:
        raise FileNotFoundError("탐지 모델 없음")
    model = YOLO(mp)
    cap = cv2.VideoCapture(video)
    frames, mats, prev_gray, fi, used = [], [], None, 0, 0
    while used < max_frames:
        ok, img = cap.read()
        if not ok:
            break
        if fi % step:
            fi += 1; continue
        fi += 1; used += 1
        r = model.predict(img, imgsz=512, conf=CACHE_CONF, verbose=False)[0]
        boxes = [(float(a), float(b), float(c - a), float(d - b))
                 for a, b, c, d in r.boxes.xyxy.cpu().numpy()]
        confs = [float(c) for c in r.boxes.conf.cpu().numpy()]
        frames.append((boxes, confs))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mats.append(mt.estimate_camera_motion(prev_gray, gray, boxes)
                    if prev_gray is not None else None)
        prev_gray = gray
    cap.release()
    return {"video": os.path.basename(video), "frames": frames, "mats": mats}


def run_setting(cache: dict, conf: float, max_age: int, iou_thr: float = 0.25,
                merge: bool = False, motion: bool = False) -> dict:
    """캐시 위에서 한 설정을 평가. 반환: 과분할·트랙수·마릿수·활동량."""
    tr = mt.MCIoUTracker(iou_thr=iou_thr, max_age=max_age)
    seen, counts, acts, prev = set(), [], [], {}
    for (boxes, confs), M in zip(cache["frames"], cache["mats"]):
        b = [bx for bx, c in zip(boxes, confs) if c >= conf]
        if merge:
            b = bm.merge_split_boxes(b)
        counts.append(len(b))
        Mu = M if motion else None
        for tid, bi in tr.update(b, Mu):
            seen.add(tid)
            x, y, w, h = b[bi]; cx, cy = x + w / 2, y + h / 2
            if tid in prev:
                px, py = prev[tid]
                if motion and M is not None:
                    wp = mt.warp_box((px, py, 0.0, 0.0), M); px, py = wp[0], wp[1]
                acts.append(((cx - px) ** 2 + (cy - py) ** 2) ** 0.5)
            prev[tid] = (cx, cy)
    med = float(np.median(counts)) if counts else 1.0
    flick = float(np.mean(np.abs(np.diff(counts)))) if len(counts) > 1 else 0.0
    return {"conf": conf, "max_age": max_age, "iou": iou_thr, "merge": merge,
            "motion": motion, "med_pigs": med, "tracks": len(seen),
            "frag": round(len(seen) / med, 1) if med else None,
            "flicker": round(flick, 2),
            "act": round(float(np.mean(acts)), 2) if acts else 0.0}


def sweep(video: str, model_path: str | None = None, max_frames: int = 168) -> list:
    """대표 조합을 쓸어보고 과분할 오름차순으로 반환."""
    cache = cache_detections(video, model_path, max_frames=max_frames)
    out = []
    out.append(run_setting(cache, 0.35, 8))                      # 현재 기본값
    for conf in (0.25, 0.35, 0.45):
        for age in (8, 20, 40):
            out.append(run_setting(cache, conf, age))
    out.append(run_setting(cache, 0.25, 40, merge=True))
    out.append(run_setting(cache, 0.25, 40, motion=True))
    out.append(run_setting(cache, 0.25, 40, merge=True, motion=True))
    # 중복 제거 후 정렬
    seen, uniq = set(), []
    for r in out:
        k = (r["conf"], r["max_age"], r["merge"], r["motion"])
        if k in seen:
            continue
        seen.add(k); uniq.append(r)
    return sorted(uniq, key=lambda r: r["frag"] if r["frag"] is not None else 1e9)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    rows = sweep(sys.argv[1])
    print(f"{'conf':>5} {'age':>4} {'merge':>6} {'motion':>7} "
          f"{'마릿수':>6} {'트랙':>5} {'과분할':>6} {'명멸':>5} {'활동':>6}")
    for r in rows:
        print(f"{r['conf']:>5.2f} {r['max_age']:>4d} {str(r['merge']):>6} "
              f"{str(r['motion']):>7} {r['med_pigs']:>6.0f} {r['tracks']:>5d} "
              f"{r['frag']:>6.1f} {r['flicker']:>5.2f} {r['act']:>6.2f}")
    b, base = rows[0], next((r for r in rows if r["conf"] == 0.35
                             and r["max_age"] == 8 and not r["merge"]
                             and not r["motion"]), None)
    print(f"\n최적: conf {b['conf']} · max_age {b['max_age']} · merge {b['merge']} "
          f"· motion {b['motion']} → 과분할 {b['frag']}배")
    if base and base["frag"]:
        print(f"기본(conf 0.35/age 8) 대비 {(1 - b['frag']/base['frag'])*100:+.0f}% 개선")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
