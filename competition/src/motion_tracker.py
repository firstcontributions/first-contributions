"""카메라 모션 보상 추적 — 흔들리는 영상에서도 개체 ID를 유지한다.

문제: IoU 추적은 **카메라가 고정**이라고 가정한다. 핸드헬드·PTZ 영상에서는
카메라가 움직이면 모든 박스가 통째로 이동해 IoU 가 끊기고, 같은 개체에 새 ID 가
계속 붙는다. 실측: 국내 축사 핸드헬드 영상에서 **트랙/마릿수 20.3배 과분할**.

해법: 프레임 간 **전역(카메라) 모션을 추정**해, 기존 트랙 박스를 그만큼 이동시킨
뒤 IoU 를 계산한다. 카메라 이동분이 상쇄되어 개체 고유의 움직임만 남는다.

  ① 배경 특징점 추출 — **탐지 박스 영역은 제외**(돼지 자체 움직임이 섞이면
     카메라 모션 추정이 오염된다. 이 마스킹이 핵심)
  ② Lucas-Kanade optical flow 로 특징점 대응 추적
  ③ RANSAC 부분 아핀(회전+평행이동+스케일) 추정 → 이상치 제거
  ④ 기존 트랙 박스를 그 변환으로 워프 후 IoU 매칭

활동량도 보정된다 — 카메라 이동으로 생긴 '가짜 활동량'이 제거되어, 발정 판정의
핵심 지표인 개체 활동량이 실제 값에 가까워진다.

    python competition/src/motion_tracker.py <영상.mp4>   # 보정 전후 비교
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from iou_tracker import iou  # noqa: E402

MIN_PTS = 8            # 아핀 추정에 필요한 최소 대응점
MAX_CORNERS = 300


def estimate_camera_motion(prev_gray, gray, exclude_boxes=None):
    """이전→현재 프레임의 전역 카메라 변환(2x3 아핀). 실패 시 None.

    exclude_boxes: 돼지 탐지 박스들 — 이 영역의 특징점은 **제외**한다.
    (돼지의 자체 움직임을 카메라 모션으로 오인하면 보정이 역효과)
    """
    import cv2
    mask = np.full(prev_gray.shape[:2], 255, np.uint8)
    for (x, y, w, h) in (exclude_boxes or []):
        cv2.rectangle(mask, (int(x), int(y)), (int(x + w), int(y + h)), 0, -1)
    if mask.mean() < 30:            # 화면 대부분이 돼지 → 배경 추정 불가
        return None
    p0 = cv2.goodFeaturesToTrack(prev_gray, maxCorners=MAX_CORNERS,
                                 qualityLevel=0.01, minDistance=8, mask=mask)
    if p0 is None or len(p0) < MIN_PTS:
        return None
    p1, st, _ = cv2.calcOpticalFlowPyrLK(prev_gray, gray, p0, None)
    if p1 is None:
        return None
    st = st.reshape(-1).astype(bool)
    a, b = p0.reshape(-1, 2)[st], p1.reshape(-1, 2)[st]
    if len(a) < MIN_PTS:
        return None
    M, _inl = cv2.estimateAffinePartial2D(a, b, method=cv2.RANSAC,
                                          ransacReprojThreshold=3.0)
    return M


def warp_box(box, M):
    """박스를 아핀 변환으로 이동(축 정렬 사각형 유지)."""
    import cv2
    if M is None:
        return box
    x, y, w, h = box
    pts = np.array([[x, y], [x + w, y], [x + w, y + h], [x, y + h]],
                   dtype=np.float32).reshape(-1, 1, 2)
    q = cv2.transform(pts, M).reshape(-1, 2)
    nx, ny = float(q[:, 0].min()), float(q[:, 1].min())
    return (nx, ny, float(q[:, 0].max() - nx), float(q[:, 1].max() - ny))


def motion_magnitude(M) -> float:
    """변환의 평행이동 크기(px) — 카메라 흔들림 지표."""
    if M is None:
        return 0.0
    return float((M[0, 2] ** 2 + M[1, 2] ** 2) ** 0.5)


class MCIoUTracker:
    """카메라 모션 보상 IoU 추적기.

    update(boxes, M) — M 은 이전→현재 프레임의 아핀 변환(None 이면 순수 IoU).
    기존 트랙 박스를 M 으로 워프한 뒤 매칭하므로, 카메라가 움직여도 ID 가 유지된다.
    """

    def __init__(self, iou_thr: float = 0.25, max_age: int = 8):
        self.iou_thr = iou_thr
        self.max_age = max_age
        self.tracks: dict = {}
        self._next = 0

    def update(self, boxes: list, M=None) -> list:
        # 1) 카메라 모션만큼 기존 트랙을 미리 이동
        if M is not None:
            for tr in self.tracks.values():
                tr["box"] = warp_box(tr["box"], M)
        # 2) 탐욕적 IoU 매칭
        pairs = []
        for tid, tr in self.tracks.items():
            for bi, b in enumerate(boxes):
                v = iou(tr["box"], b)
                if v >= self.iou_thr:
                    pairs.append((v, tid, bi))
        pairs.sort(reverse=True)
        assign, ut, ub = {}, set(), set()
        for v, tid, bi in pairs:
            if tid in ut or bi in ub:
                continue
            ut.add(tid); ub.add(bi)
            self.tracks[tid]["box"] = boxes[bi]
            self.tracks[tid]["age"] = 0
            assign[bi] = tid
        # 3) 미매칭 탐지 → 새 트랙
        for bi, b in enumerate(boxes):
            if bi in ub:
                continue
            tid = self._next; self._next += 1
            self.tracks[tid] = {"box": b, "age": 0}
            assign[bi] = tid
        # 4) 미매칭 트랙 소멸
        for tid in list(self.tracks):
            if tid not in ut and tid not in set(assign.values()):
                self.tracks[tid]["age"] += 1
                if self.tracks[tid]["age"] > self.max_age:
                    del self.tracks[tid]
        return [(assign[bi], bi) for bi in range(len(boxes)) if bi in assign]


# --------------------------------------------------------------------------
def compare_on_video(video: str, model_path: str | None = None,
                     step: int = 3, conf: float = 0.35, max_frames: int = 400) -> dict:
    """같은 영상에 순수 IoU vs 모션 보상을 돌려 과분할을 비교."""
    import cv2
    from ultralytics import YOLO
    import analyze_video as av
    mp = av.find_model(model_path)
    if mp is None:
        raise FileNotFoundError("탐지 모델 없음")
    model = YOLO(mp)
    cap = cv2.VideoCapture(video)
    plain, mc = MCIoUTracker(), MCIoUTracker()
    seen_p, seen_m, counts, mags = set(), set(), [], []
    act_p, act_m, prev_p, prev_m = [], [], {}, {}
    prev_gray, fi, used = None, 0, 0
    while used < max_frames:
        ok, img = cap.read()
        if not ok:
            break
        if fi % step:
            fi += 1
            continue
        fi += 1; used += 1
        res = model.predict(img, imgsz=512, conf=conf, verbose=False)[0]
        boxes = [(float(a), float(b), float(c - a), float(d - b))
                 for a, b, c, d in res.boxes.xyxy.cpu().numpy()]
        counts.append(len(boxes))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        M = estimate_camera_motion(prev_gray, gray, boxes) if prev_gray is not None else None
        mags.append(motion_magnitude(M))
        prev_gray = gray
        for tid, bi in plain.update(boxes, None):
            seen_p.add(tid)
            x, y, w, h = boxes[bi]; c = (x + w / 2, y + h / 2)
            if tid in prev_p:
                act_p.append(((c[0]-prev_p[tid][0])**2 + (c[1]-prev_p[tid][1])**2) ** 0.5)
            prev_p[tid] = c
        for tid, bi in mc.update(boxes, M):
            seen_m.add(tid)
            x, y, w, h = boxes[bi]; c = (x + w / 2, y + h / 2)
            if tid in prev_m:
                # 활동량도 **카메라 이동을 보상해야** 한다. 직전 중심을 M 으로 워프한
                # 뒤 비교해야 개체 고유의 움직임만 남는다(원본끼리 빼면 카메라 이동이
                # 그대로 활동량으로 잡힌다 — 발정 판정의 핵심 지표가 오염됨).
                px, py = prev_m[tid]
                if M is not None:
                    wb = warp_box((px, py, 0.0, 0.0), M)
                    px, py = wb[0], wb[1]
                act_m.append(((c[0] - px) ** 2 + (c[1] - py) ** 2) ** 0.5)
            prev_m[tid] = c
    cap.release()
    med = float(np.median(counts)) if counts else 1.0
    lp = [v for v in plain.tracks.values()]      # 참고용(살아있는 트랙)
    return {
        "video": os.path.basename(video), "frames": used, "med_pigs": med,
        "cam_motion_px": round(float(np.mean(mags)), 2),
        "tracks_plain": len(seen_p), "tracks_mc": len(seen_m),
        "frag_plain": round(len(seen_p) / med, 1) if med else None,
        "frag_mc": round(len(seen_m) / med, 1) if med else None,
        "act_plain": round(float(np.mean(act_p)), 2) if act_p else 0.0,
        "act_mc": round(float(np.mean(act_m)), 2) if act_m else 0.0,
        "det_flicker": round(float(np.mean(np.abs(np.diff(counts)))), 2) if len(counts) > 1 else 0.0,
        "det_cv": round(float(np.std(counts) / max(1e-6, np.mean(counts))), 3) if counts else 0.0,
        "_alive_plain": len(lp),
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    r = compare_on_video(sys.argv[1])
    print(f"{r['video']} — {r['frames']}프레임, 마릿수 중앙값 {r['med_pigs']:.0f}, "
          f"카메라 이동 평균 {r['cam_motion_px']}px")
    print(f"  순수 IoU     트랙 {r['tracks_plain']:4d}  과분할 {r['frag_plain']}배  "
          f"활동량 {r['act_plain']}px")
    print(f"  모션 보상    트랙 {r['tracks_mc']:4d}  과분할 {r['frag_mc']}배  "
          f"활동량 {r['act_mc']}px")
    print(f"  탐지 흔들림: 프레임간 마릿수 변화 평균 {r['det_flicker']}마리 "
          f"(변동계수 {r['det_cv']})")
    if r["frag_plain"] and r["frag_mc"]:
        imp = (1 - r["frag_mc"] / r["frag_plain"]) * 100
        print(f"  → 과분할 {imp:+.0f}% 개선, 활동량 "
              f"{r['act_mc'] - r['act_plain']:+.2f}px (카메라 이동분 제거)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
