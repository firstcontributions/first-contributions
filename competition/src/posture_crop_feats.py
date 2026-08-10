"""자세 크롭 외형 피처 — bbox 기하가 카메라를 넘지 못하는 지점을 메운다.

bbox 기하만 쓰면 못 본 카메라에서 정확도가 0.401 로 주저앉는다(실측). 이유는
분명하다. 같은 자세라도 카메라 각도가 바뀌면 종횡비·면적이 통째로 달라지고,
무엇보다 **좌횡와/우횡와는 bbox 로는 원리상 구분이 불가능하다** — 둘 다 옆으로
누운 같은 모양의 상자다. 상자 안을 봐야 한다.

여기서 뽑는 것(크롭을 48×48 로 정규화 후):
  · 그래디언트 방향 히스토그램(2×2 셀 × 9빈 = 36) — 몸통 축의 방향과 다리 윤곽
  · 밝기 격자 4×4(16) — 몸통/바닥 대비의 공간 배치
  · 실루엣 2차 모멘트 — 장축/단축 비, 방향(sin2θ·cos2θ), 채움 비율
  · 엣지 밀도·대비 — 다리·귀 같은 돌출부가 만드는 고주파

크롭을 **고정 크기로 리사이즈**하는 것이 핵심이다. 절대 크기는 카메라 거리에
따라 변하지만 정규화된 모양은 덜 변한다. 크기 정보는 이미 bbox 기하 피처가
들고 있으므로 역할이 겹치지 않는다.

방향은 sin2θ·cos2θ 로 넣는다. θ 와 θ+180° 는 같은 축이라 각도를 그대로 쓰면
같은 자세가 0 과 1 로 갈린다.

    python competition/src/posture_crop_feats.py        # 추출 + 캐시
캐시: competition/data/posture_crops.npz
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import posture_features as pf  # noqa: E402

CACHE = os.path.join(ROOT, "competition", "data", "posture_crops.npz")
VERSION = 2            # 피처 정의 버전 — 바뀌면 캐시를 무효화한다
SZ = 48                 # 크롭 정규화 크기
NBINS = 9               # 그래디언트 방향 빈
CELLS = 2               # 2×2 셀

CROP_COLS = (
    [f"hog{c}_{b}" for c in range(CELLS * CELLS) for b in range(NBINS)]
    + [f"grid{i}" for i in range(16)]
    + ["sil_fill", "sil_elong", "sil_sin2t", "sil_cos2t",
       "edge_den", "contrast", "mean_i", "std_i"]
)


def _silhouette(u8: np.ndarray) -> np.ndarray:
    """크롭에서 몸통 실루엣을 뽑는다(Otsu).

    처음엔 중앙값으로 잘랐는데, 배경이 넓고 몸통이 좁으면 중앙값이 배경값과
    같아져 **크롭 전체가 실루엣**이 돼버렸다. 그러면 장단축비도 방향도 무의미해진다.
    Otsu 는 두 봉우리 사이를 잡으므로 이 경우에 안전하다.

    극성은 **네 모서리**로 정한다. 중앙부가 몸통이라고 가정했더니 몸통이 가늘 때
    중앙 과반을 못 채워 배경을 실루엣으로 잡았다. bbox 는 몸통에 붙어 있으므로
    모서리는 거의 항상 바닥이고, 이 가정이 훨씬 잘 버틴다.
    """
    import cv2
    _t, mask = cv2.threshold(u8, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    m = mask > 0
    k = max(3, SZ // 8)
    corners = np.concatenate([m[:k, :k].ravel(), m[:k, -k:].ravel(),
                              m[-k:, :k].ravel(), m[-k:, -k:].ravel()])
    bg_is_true = corners.mean() > 0.5
    return ~m if bg_is_true else m


def _crop_feats(g8: np.ndarray) -> np.ndarray:
    """정규화된 회색조 크롭(uint8) → 외형 피처 벡터."""
    sil_mask = _silhouette(g8)
    g = g8.astype(np.float32) / 255.0
    gx = np.zeros_like(g); gy = np.zeros_like(g)
    gx[:, 1:-1] = g[:, 2:] - g[:, :-2]
    gy[1:-1, :] = g[2:, :] - g[:-2, :]
    mag = np.sqrt(gx * gx + gy * gy)
    # 0~180°: 방향은 축이지 화살표가 아니다
    ang = (np.degrees(np.arctan2(gy, gx)) % 180.0)
    bins = np.minimum((ang / (180.0 / NBINS)).astype(int), NBINS - 1)

    feats = []
    cs = SZ // CELLS
    for cy in range(CELLS):
        for cx in range(CELLS):
            m = mag[cy * cs:(cy + 1) * cs, cx * cs:(cx + 1) * cs]
            bb = bins[cy * cs:(cy + 1) * cs, cx * cs:(cx + 1) * cs]
            h = np.bincount(bb.ravel(), weights=m.ravel(), minlength=NBINS)
            s = h.sum()
            feats.extend((h / s if s > 1e-8 else h).tolist())

    # 4×4 밝기 격자
    q = SZ // 4
    feats.extend([float(g[i * q:(i + 1) * q, j * q:(j + 1) * q].mean())
                  for i in range(4) for j in range(4)])

    ys, xs = np.nonzero(sil_mask)
    if len(xs) > 8:
        fill = len(xs) / float(SZ * SZ)
        x0, y0 = xs.mean(), ys.mean()
        dx, dy = xs - x0, ys - y0
        cxx, cyy, cxy = (dx * dx).mean(), (dy * dy).mean(), (dx * dy).mean()
        tr_, det = cxx + cyy, cxx * cyy - cxy * cxy
        disc = max(0.0, tr_ * tr_ / 4 - det) ** 0.5
        l1, l2 = tr_ / 2 + disc, max(1e-6, tr_ / 2 - disc)
        elong = float(np.sqrt(l1 / l2))
        th = 0.5 * np.arctan2(2 * cxy, cxx - cyy)
        sin2t, cos2t = float(np.sin(2 * th)), float(np.cos(2 * th))
    else:
        fill, elong, sin2t, cos2t = 0.0, 1.0, 0.0, 1.0
    feats.extend([fill, elong, sin2t, cos2t])

    feats.extend([float((mag > 0.12).mean()), float(g.max() - g.min()),
                  float(g.mean()), float(g.std())])
    return np.asarray(feats, dtype=np.float32)


def extract(df: pd.DataFrame, img_dirs: dict, verbose: bool = True) -> np.ndarray:
    """행 순서대로 크롭 피처 행렬 반환. 이미지는 한 번씩만 읽는다."""
    import cv2
    out = np.zeros((len(df), len(CROP_COLS)), dtype=np.float32)
    df = df.reset_index(drop=True)
    groups = df.groupby("image_id", sort=False).indices
    n_miss, done = 0, 0
    for img_id, idxs in groups.items():
        # image_id 에 이미 확장자가 들어 있다. 무심코 .jpg 를 덧붙이면 전부
        # 못 찾고 0 벡터가 캐시된다(실제로 23,450개 전부 누락됐다).
        name = str(img_id)
        cands = [name] if os.path.splitext(name)[1] else [name + ".jpg",
                                                          name + ".png"]
        path = None
        for d in img_dirs.values():
            for c in cands:
                p = os.path.join(d, c)
                if os.path.exists(p):
                    path = p
                    break
            if path:
                break
        im = cv2.imread(path, cv2.IMREAD_GRAYSCALE) if path else None
        if im is None:
            n_miss += len(idxs)
            continue
        H, W = im.shape
        for i in idxs:
            r = df.iloc[i]
            x, y = int(max(0, r["x"])), int(max(0, r["y"]))
            w, h = int(max(1, r["w"])), int(max(1, r["h"]))
            x2, y2 = min(W, x + w), min(H, y + h)
            if x2 - x < 4 or y2 - y < 4:
                n_miss += 1
                continue
            crop = cv2.resize(im[y:y2, x:x2], (SZ, SZ),
                              interpolation=cv2.INTER_AREA)
            out[i] = _crop_feats(crop)
        done += 1
        if verbose and done % 500 == 0:
            print(f"  {done}/{len(groups)} 이미지", flush=True)
    ok = len(df) - n_miss
    if verbose:
        print(f"  완료: {ok:,}/{len(df):,} 박스 (누락 {n_miss:,})")
    # 조용히 0 행렬을 캐시하면 "외형 피처가 도움이 안 된다"는 잘못된 결론이 난다.
    if ok < 0.5 * len(df):
        raise RuntimeError(
            f"크롭 추출 실패: {ok:,}/{len(df):,} 만 성공했다. "
            f"이미지 경로/파일명을 확인할 것 (탐색 경로: {list(img_dirs.values())})")
    return out


def load_all(rebuild: bool = False) -> tuple:
    """(full_df, crop_matrix) — 캐시가 있으면 재사용."""
    a = pf.add_rich(pf.load_split("train1.csv"))
    b = pf.add_rich(pf.load_split("train2.csv"))
    full = (pd.concat([a, b], ignore_index=True)
              .drop_duplicates(subset=["image_id", "bbox"])
              .reset_index(drop=True))
    key = full["image_id"].astype(str) + "|" + full["bbox"].astype(str)
    if not rebuild and os.path.exists(CACHE):
        z = np.load(CACHE, allow_pickle=True)
        # 피처 정의가 바뀌면 예전 캐시를 그대로 쓰면 안 된다 — 조용히 옛 값으로
        # 비교하면 개선/악화를 잘못 읽는다. 버전을 키에 포함시킨다.
        same_ver = str(z["version"]) == str(VERSION) if "version" in z else False
        if same_ver and list(z["key"]) == list(key):
            return full, z["X"]
        print("  (캐시 버전/키 불일치 — 재추출)")
    X = extract(full, {"t1": os.path.join(pf.COMP, "train1_images"),
                       "t2": os.path.join(pf.COMP, "train2_images")})
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    np.savez_compressed(CACHE, X=X, key=key.to_numpy(), version=VERSION)
    return full, X


def main() -> int:
    rebuild = "--rebuild" in sys.argv
    print("크롭 외형 피처 추출 (6,240 이미지 · 23,450 박스)")
    full, X = load_all(rebuild)
    print(f"  피처 행렬 {X.shape} · 컬럼 {len(CROP_COLS)}")
    nz = (X.any(axis=1)).mean()
    print(f"  유효 행 비율 {nz:.1%} · 캐시 {CACHE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
