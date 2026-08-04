"""Edinburgh Pig Behaviour Annotated 데이터셋 파서.

Kaggle: jackbyte/edinburgh-pig-behaviour-annotated (CC BY-NC 4.0)
각 녹화 폴더의 output.json 구조:
  { videoFileName, stepSize, config,
    objects: [ { id, frames: [ {frameNumber, bbox:{x,y,width,height},
                                 visible, behaviour}, ... ] }, ... ] }

프레임 단위 정형 테이블로 변환한다(개체 시계열). 컬럼은 71471 파서와 호환되게
맞춰, build_estrus_features / estrus_onset 등 기존 도구를 그대로 쓸 수 있다.
"""
from __future__ import annotations

import json
import os

import pandas as pd


def parse_edinburgh(root: str) -> pd.DataFrame:
    rows: list[dict] = []
    for dp, _, fs in os.walk(root):
        if "output.json" not in fs:
            continue
        try:
            d = json.load(open(os.path.join(dp, "output.json"), encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        rec = os.path.relpath(dp, root).replace(os.sep, "_")
        for obj in d.get("objects", []):
            oid = str(obj.get("id"))
            uid = f"{rec}#{oid}"          # 녹화+개체로 유일 식별
            for fr in obj.get("frames", []):
                bb = fr.get("bbox") or {}
                w = bb.get("width"); h = bb.get("height")
                x = bb.get("x"); y = bb.get("y")
                rows.append({
                    "recording": rec,
                    "individual_id": uid,
                    "frame_idx": fr.get("frameNumber"),
                    "behavior": fr.get("behaviour"),
                    "visible": bool(fr.get("visible", True)),
                    "bbox_w": w, "bbox_h": h,
                    "aspect_ratio": (w / h) if (w and h) else None,
                    "centroid_x": (x + w / 2) if (x is not None and w) else None,
                    "centroid_y": (y + h / 2) if (y is not None and h) else None,
                    # 71471 호환용 placeholder
                    "species": "pig", "kp_spread": None, "estrus": None,
                })
    return pd.DataFrame(rows)


def main() -> int:
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "yangdon/data/edinburgh"
    df = parse_edinburgh(root)
    print(f"파싱: {len(df)}행 (녹화 {df['recording'].nunique()}개, "
          f"개체 {df['individual_id'].nunique()}두)")
    print("\n행동 분포:")
    print(df["behavior"].value_counts().to_string())
    out = "yangdon/data/edinburgh_frames.csv"
    df.to_csv(out, index=False, encoding="utf-8-sig")
    print(f"\n저장: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
