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


def merge_split_boxes(boxes, gap_ratio: float = 0.18, align_min: float = 0.70,
                      max_aspect: float = 4.0, max_area_ratio: float = 1.35,
                      max_size_vs_median: float = 1.25, max_rounds: int = 1):
    """분할된 박스들을 병합. 반환: 병합된 박스 리스트.

    ⚠️ 과병합 주의(실측 교훈): 군사 사육 영상에서는 돼지들이 서로 붙어 있어
    "창살에 쪼개진 한 마리"와 "나란히 선 두 마리"를 구분하기 어렵다. 초기 버전은
    연쇄 병합까지 허용해 프레임 전체를 한 덩어리로 만들었다(마릿수 5 → 1).
    안전장치 셋:
      · max_rounds=1        연쇄 병합 금지(한 번만)
      · max_size_vs_median  합친 박스가 온전한 개체 크기(75퍼센타일)의 N배 초과 시 취소
      · 임계 강화           더 가깝고(0.18) 더 잘 정렬된(0.70) 경우만
    붙어 있는 개체가 많은 영상에서는 **끄는 편이 안전**하다.
    """
    import numpy as _np
    cur = [tuple(map(float, b)) for b in boxes]
    if len(cur) < 2:
        return cur
    # 기준 크기는 **75퍼센타일**을 쓴다. 중앙값을 쓰면 조각이 많은 프레임에서
    # 기준 자체가 조각 크기로 내려가 정상 병합까지 막힌다(온전한 개체는 상위에 분포).
    areas = [b[2] * b[3] for b in cur]
    med_area = float(_np.percentile(areas, 75)) or 1.0
    rounds, changed = 0, True
    while changed and len(cur) > 1 and rounds < max_rounds:
        rounds += 1
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
                if u[2] * u[3] > max_size_vs_median * med_area:
                    continue      # 온전한 개체(75퍼센타일)보다 과도하게 큼 → 두 마리
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
        # 자체 테스트
        mix = [(0, 0, 45, 60), (50, 2, 45, 58), (300, 0, 100, 60), (420, 0, 100, 60)]
        print(f"조각2+정상2: {len(mix)}개 → {len(merge_split_boxes(mix))}개 (3이 정상)")
        adj = [(0, 0, 100, 60), (102, 0, 100, 60), (204, 0, 100, 60)]
        print(f"나란한 3마리: {len(adj)}개 → {len(merge_split_boxes(adj))}개 (3이 정상, 과병합 금지)")
        far = [(100, 100, 60, 80), (500, 100, 60, 80)]
        print(f"먼 두 마리:   {len(far)}개 → {len(merge_split_boxes(far))}개 (2가 정상)")
        return 0
    r = compare_on_video(sys.argv[1])
    print(f"{r['video']} — {r['frames']}프레임")
    print(f"  병합 전 마릿수 중앙값 {r['raw_med']:.0f} (평균 {r['raw_mean']})")
    print(f"  병합 후 마릿수 중앙값 {r['merged_med']:.0f} (평균 {r['merged_mean']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
