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


class IoUReIDTracker:
    """IoU + 외형 Re-ID 추적기.

    가림으로 끊긴 트랙을 외형(feat) 유사도로 되살려 단편화를 줄인다.
    - 활성 트랙: IoU 로 매칭
    - 미매칭 탐지: 최근 소실 트랙(gallery)과 외형 코사인 유사도로 Re-ID → ID 복원
    - 그래도 없으면 새 ID
    feats: 박스별 외형 벡터(list). None 이면 순수 IoU 로 동작.
    """

    def __init__(self, iou_thr=0.3, max_age=5, reid_thr=0.6, reid_memory=60,
                 reid_max_dist=90):
        import numpy as np
        self._np = np
        self.iou_thr = iou_thr; self.max_age = max_age
        self.reid_thr = reid_thr; self.reid_memory = reid_memory
        self.reid_max_dist = reid_max_dist    # 소실 트랙 복원 최대 중심거리(px)
        self.tracks = {}; self.lost = {}; self._next = 0; self._t = 0

    @staticmethod
    def _cdist(a, b):
        return (((a[0]+a[2]/2)-(b[0]+b[2]/2))**2 + ((a[1]+a[3]/2)-(b[1]+b[3]/2))**2) ** 0.5

    def _norm(self, v):
        v = self._np.asarray(v, dtype=float)
        n = (v * v).sum() ** 0.5
        return v / n if n else v

    def update(self, boxes, feats=None):
        np = self._np
        self._t += 1
        feats = [self._norm(f) for f in feats] if feats is not None else [None] * len(boxes)
        assign = {}
        # 1) 활성 트랙 IoU 매칭
        pairs = []
        for tid, tr in self.tracks.items():
            for bi, b in enumerate(boxes):
                v = iou(tr["box"], b)
                if v >= self.iou_thr:
                    pairs.append((v, tid, bi))
        pairs.sort(reverse=True)
        ut, ub = set(), set()
        for v, tid, bi in pairs:
            if tid in ut or bi in ub:
                continue
            ut.add(tid); ub.add(bi)
            self.tracks[tid].update(box=boxes[bi], age=0)
            if feats[bi] is not None:
                self.tracks[tid]["feat"] = feats[bi]
            assign[bi] = tid
        # 2) 미매칭 탐지 → 소실 트랙과 Re-ID
        for bi, b in enumerate(boxes):
            if bi in ub:
                continue
            best, bs = None, self.reid_thr
            if feats[bi] is not None:
                for tid, lo in self.lost.items():
                    if lo.get("feat") is None:
                        continue
                    # 위치 게이트: 마지막 위치 근처만 복원(잘못된 병합 방지)
                    if self._cdist(b, lo["box"]) > self.reid_max_dist:
                        continue
                    sim = float(np.dot(feats[bi], lo["feat"]))
                    if sim >= bs:
                        bs, best = sim, tid
            if best is not None:                      # ID 복원
                self.tracks[best] = {"box": b, "age": 0, "feat": feats[bi]}
                del self.lost[best]; assign[bi] = best; ut.add(best)
            else:                                     # 새 ID
                tid = self._next; self._next += 1
                self.tracks[tid] = {"box": b, "age": 0, "feat": feats[bi]}
                assign[bi] = tid
        # 3) 미매칭 활성 → age++/소실 이동
        matched = set(assign.values())
        for tid in list(self.tracks):
            if tid not in matched:
                self.tracks[tid]["age"] += 1
                if self.tracks[tid]["age"] > self.max_age:
                    self.lost[tid] = {"feat": self.tracks[tid].get("feat"),
                                      "box": self.tracks[tid]["box"], "t": self._t}
                    del self.tracks[tid]
        # 4) 오래된 소실 트랙 제거
        for tid in [k for k, v in self.lost.items() if self._t - v["t"] > self.reid_memory]:
            del self.lost[tid]
        return [(assign[bi], bi) for bi in range(len(boxes)) if bi in assign]


def track_sequence_reid(frames_feats: list, **kw) -> dict:
    """frames_feats: [(frame_no,[box],[meta],[feat]),...] → track_id -> members."""
    tr = IoUReIDTracker(**kw)
    tracks = {}
    for fno, boxes, metas, feats in frames_feats:
        for tid, bi in tr.update(boxes, feats):
            tracks.setdefault(tid, []).append(
                {"frame": fno, "box": boxes[bi], "meta": metas[bi]})
    return tracks


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
