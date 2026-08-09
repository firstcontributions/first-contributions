"""분할 박스 병합 — 창살·기둥에 가려 한 마리가 여러 박스로 쪼개지는 문제 보정.

국내 축사 영상 검증에서 확인된 실패 양상: 스톨 창살·파이프가 몸통을 가로지르면
탐지기가 **한 마리를 2~3개 박스**로 낸다. 마릿수가 부풀고, 추적은 더 끊긴다.

NMS 는 이걸 못 고친다 — 쪼개진 조각들은 서로 **겹치지 않기 때문**이다(IoU≈0).
그래서 겹침이 아니라 **인접성·정렬성**으로 병합한다:

  ① 두 박스가 가까이 있고(간격 ≤ gap_ratio × 평균 변 길이)
  ② 한 축으로 잘 정렬돼 있고(수직/수평 겹침 비율 ≥ align_min)
  ③ 병합해도 종횡비가 돼지답게 유지되면(≤ max_aspect)
  → 하나로 합친다.

돼지는 대체로 길쭉한 덩어리라 이 규칙이 성립한다. 과병합을 막으려고 합친 박스의
면적이 원본 합의 max_area_ratio 배를 넘으면 취소한다(멀리 떨어진 두 마리 방지).

    python competition/src/box_merge.py <영상.mp4>    # 병합 전후 마릿수 비교
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _union(a, b):
    x = min(a[0], b[0]); y = min(a[1], b[1])
    return (x, y, max(a[0] + a[2], b[0] + b[2]) - x,
            max(a[1] + a[3], b[1] + b[3]) - y)


def _gap_and_align(a, b):
    """(간격, 정렬도) — 간격은 축별 최소 빈틈, 정렬도는 직교축 겹침 비율."""
    ax1, ay1, aw, ah = a; ax2, ay2 = ax1 + aw, ay1 + ah
    bx1, by1, bw, bh = b; bx2, by2 = bx1 + bw, by1 + bh
    gx = max(0.0, max(ax1, bx1) - min(ax2, bx2))     # 수평 빈틈
    gy = max(0.0, max(ay1, by1) - min(ay2, by2))     # 수직 빈틈
    ov_y = max(0.0, min(ay2, by2) - max(ay1, by1)) / max(1e-6, min(ah, bh))
    ov_x = max(0.0, min(ax2, bx2) - max(ax1, bx1)) / max(1e-6, min(aw, bw))
    # 가로로 이웃(수평 간격이 작고 수직으로 겹침) 또는 세로로 이웃
    if gy <= gx:
        return gx, ov_y
    return gy, ov_x


def merge_split_boxes(boxes, gap_ratio: float = 0.25, align_min: float = 0.55,
                      max_aspect: float = 6.0, max_area_ratio: float = 2.2):
    """분할된 박스들을 병합. 반환: 병합된 박스 리스트."""
    cur = [tuple(map(float, b)) for b in boxes]
    changed = True
    while changed and len(cur) > 1:
        changed = False
        best = None
        for i in range(len(cur)):
            for j in range(i + 1, len(cur)):
                a, b = cur[i], cur[j]
                gap, align = _gap_and_align(a, b)
                scale = (a[2] + a[3] + b[2] + b[3]) / 4.0
                if scale <= 0 or gap > gap_ratio * scale or align < align_min:
                    continue
                u = _union(a, b)
                if u[3] <= 0 or u[2] <= 0:
                    continue
                asp = max(u[2] / u[3], u[3] / u[2])
                if asp > max_aspect:
                    continue
                if u[2] * u[3] > max_area_ratio * (a[2] * a[3] + b[2] * b[3]):
                    continue
                score = align - gap / max(1e-6, scale)      # 정렬 좋고 가까울수록
                if best is None or score > best[0]:
                    best = (score, i, j, u)
        if best:
            _, i, j, u = best
            cur = [b for k, b in enumerate(cur) if k not in (i, j)] + [u]
            changed = True
    return cur


def compare_on_video(video: str, model_path: str | None = None, step: int = 15,
                     conf: float = 0.35, max_frames: int = 60) -> dict:
    """병합 전후 마릿수·박스 크기 비교."""
    import cv2
    import numpy as np
    from ultralytics import YOLO
    import analyze_video as av
    mp = av.find_model(model_path)
    model = YOLO(mp)
    cap = cv2.VideoCapture(video)
    raw, mrg, fi, used = [], [], 0, 0
    while used < max_frames:
        ok, img = cap.read()
        if not ok:
            break
        if fi % step:
            fi += 1; continue
        fi += 1; used += 1
        r = model.predict(img, imgsz=512, conf=conf, verbose=False)[0]
        boxes = [(float(a), float(b), float(c - a), float(d - b))
                 for a, b, c, d in r.boxes.xyxy.cpu().numpy()]
        raw.append(len(boxes))
        mrg.append(len(merge_split_boxes(boxes)))
    cap.release()
    return {"video": os.path.basename(video), "frames": used,
            "raw_med": float(np.median(raw)) if raw else 0,
            "merged_med": float(np.median(mrg)) if mrg else 0,
            "raw_mean": round(float(np.mean(raw)), 1) if raw else 0,
            "merged_mean": round(float(np.mean(mrg)), 1) if mrg else 0}


def main() -> int:
    if len(sys.argv) < 2:
        # 자체 테스트: 세로 창살로 쪼개진 한 마리
        parts = [(100, 100, 60, 80), (168, 102, 55, 78)]
        out = merge_split_boxes(parts)
        print(f"자체 테스트: 조각 {len(parts)}개 → 병합 {len(out)}개  {out}")
        far = [(100, 100, 60, 80), (500, 100, 60, 80)]
        print(f"먼 두 마리:  {len(far)}개 → {len(merge_split_boxes(far))}개 (병합 안 됨이 정상)")
        return 0
    r = compare_on_video(sys.argv[1])
    print(f"{r['video']} — {r['frames']}프레임")
    print(f"  병합 전 마릿수 중앙값 {r['raw_med']:.0f} (평균 {r['raw_mean']})")
    print(f"  병합 후 마릿수 중앙값 {r['merged_med']:.0f} (평균 {r['merged_mean']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
