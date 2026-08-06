"""간단한 IoU 기반 다개체 추적기.

탐지(bbox)만 있는 영상에 개체 ID를 부여한다(추적기 출력=탐지→추적 파이프라인).
탐욕적 IoU 매칭 + 트랙 생성/소멸(max_age). 무거운 의존성 없음.

Edinburgh 처럼 GT ID 가 있으면 evaluate_vs_gt() 로 ID 일관성을 검증한다.
"""
from __future__ import annotations


def iou(a, b) -> float:
    ax, ay, aw, ah = a; bx, by, bw, bh = b
    x1, y1 = max(ax, bx), max(ay, by)
    x2, y2 = min(ax + aw, bx + bw), min(ay + ah, by + bh)
    iw, ih = max(0, x2 - x1), max(0, y2 - y1)
    inter = iw * ih
    union = aw * ah + bw * bh - inter
    return inter / union if union > 0 else 0.0


class IoUTracker:
    def __init__(self, iou_thr: float = 0.3, max_age: int = 5):
        self.iou_thr = iou_thr
        self.max_age = max_age
        self.tracks: dict[int, dict] = {}   # id -> {box, age}
        self._next = 0

    def update(self, boxes: list) -> list:
        """현재 프레임 boxes[(x,y,w,h),...] → [(track_id, box_index), ...]."""
        assign = {}
        pairs = []
        for tid, tr in self.tracks.items():
            for bi, b in enumerate(boxes):
                v = iou(tr["box"], b)
                if v >= self.iou_thr:
                    pairs.append((v, tid, bi))
        pairs.sort(reverse=True)
        used_t, used_b = set(), set()
        for v, tid, bi in pairs:
            if tid in used_t or bi in used_b:
                continue
            used_t.add(tid); used_b.add(bi)
            self.tracks[tid]["box"] = boxes[bi]; self.tracks[tid]["age"] = 0
            assign[bi] = tid
        # 미매칭 박스 → 새 트랙
        for bi, b in enumerate(boxes):
            if bi in used_b:
                continue
            tid = self._next; self._next += 1
            self.tracks[tid] = {"box": b, "age": 0}
            assign[bi] = tid
        # 미매칭 트랙 age++ / 소멸
        for tid in list(self.tracks):
            if tid not in used_t:
                self.tracks[tid]["age"] += 1
                if self.tracks[tid]["age"] > self.max_age:
                    del self.tracks[tid]
        return [(assign[bi], bi) for bi in range(len(boxes)) if bi in assign]


def track_sequence(frames: list, iou_thr=0.3, max_age=5) -> dict:
    """frames: [(frame_no, [box,...], [meta,...]), ...] 시간순.
    반환: track_id -> list of {frame, box, meta}."""
    tr = IoUTracker(iou_thr, max_age)
    tracks: dict[int, list] = {}
    for fno, boxes, metas in frames:
        for tid, bi in tr.update(boxes):
            tracks.setdefault(tid, []).append(
                {"frame": fno, "box": boxes[bi], "meta": metas[bi]})
    return tracks


def evaluate_vs_gt(tracks: dict) -> dict:
    """meta 에 gt id('gt') 가 있으면 ID 일관성 검증.
    ID consistency = 각 트랙에서 최빈 GT id 비율의 (길이가중) 평균."""
    from collections import Counter
    total, correct, gts = 0, 0, set()
    frag = 0
    gt_to_tracks: dict = {}
    for tid, members in tracks.items():
        g = [m["meta"].get("gt") for m in members if m["meta"].get("gt") is not None]
        if not g:
            continue
        c = Counter(g); maj, cnt = c.most_common(1)[0]
        total += len(g); correct += cnt
        for x in set(g):
            gts.add(x)
        gt_to_tracks.setdefault(maj, set()).add(tid)
    frag = sum(len(v) for v in gt_to_tracks.values()) - len(gt_to_tracks) if gt_to_tracks else 0
    return {"n_tracks": len(tracks), "n_gt": len(gts),
            "id_consistency": round(correct / total, 3) if total else 0.0,
            "fragments": frag}


if __name__ == "__main__":
    # 자체 테스트: 두 개체가 서서히 이동
    frames = []
    for f in range(10):
        frames.append((f, [(f * 2, 10, 20, 20), (100 - f, 100, 20, 20)],
                       [{"gt": "A"}, {"gt": "B"}]))
    tr = track_sequence(frames)
    print("tracks:", {k: len(v) for k, v in tr.items()})
    print("eval:", evaluate_vs_gt(tr))
