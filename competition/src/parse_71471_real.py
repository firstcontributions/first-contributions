"""AI Hub 71471 **실제 라벨 스키마** 파서 (labelon 배포본).

실데이터 확인 결과 스키마가 다음과 같다(대문자 키, 프레임=이미지 1개 JSON):

    {"INFO": {"DATASET_NAME": "[Bbox]돼지(백돼지) 발정행동 데이터", ...},
     "IMAGE": {"IMAGE_FILE_NAME": "pigfarmA_ch9_2022092109_20-85_160700.jpg",
               "WIDTH":1920, "HEIGHT":1080, "TIMESTAMP":160700,
               "FARMID":"pigfarmA", "HEADCOUNT":500, "RECORD_TIME":23},
     "ANNOTATION_INFO": [
        {"ID":122946126,
         "BOUNDING_BOX_X_COORDINATE":142, "BOUNDING_BOX_Y_COORDINATE":455,
         "BOUNDING_BOX_WIDTH":363, "BOUNDING_BOX_HEIGHT":260,
         "CATEGORY_NAME":"pig", "ACTION_NAME":"lying",
         "ESTRUS":"N"}, ...]}

핵심: **ESTRUS 가 bbox(개체 인스턴스)별 정답 라벨**이다("Y"/"N"). 이것이
발정 판정의 지도학습 정답이 된다(그동안 없던 실측 근거).

주의: 개체 추적 ID 는 없다(ANNOTATION_INFO.ID 는 주석 고유번호). 개체 단위
집계가 필요하면 iou_tracker 로 프레임 간 ID 를 부여한다. 발정 검증 자체는
**인스턴스 단위**로 바로 가능하다.

파일명 규칙: {farm}_{channel}_{yyyymmddHH}_{pen}_{timestamp}.json
    python competition/src/parse_71471_real.py <라벨디렉터리>
"""
from __future__ import annotations

import json
import os
import re
import sys

import pandas as pd

NAME_RE = re.compile(r"^(?P<farm>[^_]+)_(?P<ch>ch\d+)_(?P<dt>\d{8,10})_"
                     r"(?P<pen>[\w\-]+?)_(?P<ts>\d+)$")


def is_real_schema(obj: dict) -> bool:
    """이 JSON 이 71471 실제 배포 스키마인지."""
    return isinstance(obj, dict) and "ANNOTATION_INFO" in obj


def parse_name(basename: str) -> dict:
    """파일명 → {farm, channel, datetime, pen, timestamp}. 실패 시 부분값."""
    stem = basename.rsplit(".", 1)[0]
    m = NAME_RE.match(stem)
    if not m:
        return {"farm": None, "channel": None, "datetime": None,
                "pen": None, "ts": None}
    g = m.groupdict()
    return {"farm": g["farm"], "channel": g["ch"], "datetime": g["dt"],
            "pen": g["pen"], "ts": int(g["ts"])}


def parse_dir(label_dir: str) -> pd.DataFrame:
    """라벨 디렉터리 → 인스턴스(bbox) 단위 테이블.

    반환 컬럼: file, farm, channel, session, pen, frame_idx(timestamp),
      ann_id, behavior(ACTION_NAME), estrus(0/1), species,
      bbox_x/y/w/h, aspect_ratio, area, centroid_x/y, img_w/h, headcount
    """
    rows = []
    for root, _dirs, files in os.walk(label_dir):
        for fn in files:
            if not fn.lower().endswith(".json"):
                continue
            path = os.path.join(root, fn)
            try:
                obj = json.load(open(path, encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            if not is_real_schema(obj):
                continue
            img = obj.get("IMAGE", {}) or {}
            nm = parse_name(img.get("IMAGE_FILE_NAME") or fn)
            farm = img.get("FARMID") or nm["farm"]
            ts = img.get("TIMESTAMP")
            ts = int(ts) if ts is not None else nm["ts"]
            # 세션 = 농장+채널+날짜시각(같은 녹화 구간) → 누수 방지 그룹 키
            session = "_".join(str(x) for x in
                               (farm, nm["channel"], nm["datetime"]) if x)
            for a in obj.get("ANNOTATION_INFO") or []:
                w = a.get("BOUNDING_BOX_WIDTH")
                h = a.get("BOUNDING_BOX_HEIGHT")
                x = a.get("BOUNDING_BOX_X_COORDINATE")
                y = a.get("BOUNDING_BOX_Y_COORDINATE")
                est = a.get("ESTRUS")
                rows.append({
                    "file": fn, "farm": farm, "channel": nm["channel"],
                    "session": session, "pen": nm["pen"], "frame_idx": ts,
                    "ann_id": a.get("ID"),
                    "species": a.get("CATEGORY_NAME"),
                    "behavior": a.get("ACTION_NAME"),
                    "estrus": (1 if str(est).upper().startswith("Y")
                               else 0 if str(est).upper().startswith("N")
                               else None),
                    "bbox_x": x, "bbox_y": y, "bbox_w": w, "bbox_h": h,
                    "aspect_ratio": (w / h) if (w and h) else None,
                    "area": (w * h) if (w and h) else None,
                    "centroid_x": (x + w / 2) if (x is not None and w) else None,
                    "centroid_y": (y + h / 2) if (y is not None and h) else None,
                    "img_w": img.get("WIDTH"), "img_h": img.get("HEIGHT"),
                    "headcount": img.get("HEADCOUNT"),
                })
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame) -> str:
    """파싱 결과 요약(발정 라벨 분포 포함)."""
    if not len(df):
        return "파싱 결과 없음 — 경로/스키마 확인 필요"
    n_est = int(df["estrus"].sum()) if df["estrus"].notna().any() else 0
    rate = df["estrus"].mean() if df["estrus"].notna().any() else float("nan")
    beh = df["behavior"].value_counts().head(8)
    lines = [
        f"인스턴스 {len(df):,}개 | 파일 {df['file'].nunique():,} | "
        f"세션 {df['session'].nunique()} | 농장 {df['farm'].nunique()}",
        f"발정(ESTRUS=Y) {n_est:,}개 ({rate:.1%})",
        "행동 분포: " + ", ".join(f"{k} {v:,}" for k, v in beh.items()),
    ]
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    df = parse_dir(sys.argv[1])
    print(summarize(df))
    out = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "data", "aihub_71471_frames.csv")
    if len(df):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        df.to_csv(out, index=False)
        print(f"저장: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
