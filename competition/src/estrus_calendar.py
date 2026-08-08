"""71471 외음부 라벨 → **개체별 발정 달력**, 그리고 bbox 프레임과의 연결.

71471 라벨 서브셋의 성격을 실데이터로 확인한 결과:

  · `[Bbox]` 서브셋  : ESTRUS Y/N 이 있으나 **돈방/카메라 단위**(ch1~8 전부 Y,
                       ch9~16 전부 N) → 카메라 교락으로 개체 검증 불가
  · `외음부이미지`    : `{"VULVA":{"ANIMAL_ID","DATE","ESTRUS"}}` — **개체 단위**
                       이지만 전량 ESTRUS=Y (발정일에만 촬영) → 음성 없음
  · `울음소리`        : CRY_COUNT/TIMESTAMP 만, 발정 라벨 없음

따라서 어느 하나로도 지도 검증이 안 된다. 그러나 둘을 **연결하면** 길이 열린다:

  외음부 = "개체 A 가 D 일에 발정이었다"는 **발정 달력(양성 시점)**
  bbox   = 파일명 `{farm}_{ch}_{yyyymmddHH}_{animal}_{ts}.json` 에 개체·날짜 포함

  → 같은 개체의 **발정일 프레임(양성) vs 비발정일 프레임(음성)** 을 만들 수 있다.
    개체 내 시간 대조이므로 카메라·돈방 교락이 원천적으로 제거된다.

주의(정직성): 달력에 없는 날짜를 음성으로 두는 것은 **약한 라벨(weak label)** 이다.
촬영이 없었을 뿐 발정이었을 수 있다. 발정 주기(약 21일)를 고려해 발정일 ±`window`
일은 애매구간으로 제외하는 옵션을 둔다.

    python competition/src/estrus_calendar.py <외음부라벨디렉터리> [bbox라벨디렉터리]
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

import pandas as pd

# bbox 파일명: farm_chN_yyyymmddHH_animal_timestamp.json
BBOX_RE = re.compile(r"^(?P<farm>[^_]+)_(?P<ch>ch\d+)_(?P<dt>\d{8,10})_"
                     r"(?P<animal>[\w\-]+?)_(?P<ts>\d+)$")


def load_calendar(vulva_dir: str) -> pd.DataFrame:
    """외음부 라벨 디렉터리 → 발정 달력 DataFrame[animal, date, farm, estrus]."""
    rows = []
    for path in glob.glob(os.path.join(vulva_dir, "**", "*.json"), recursive=True):
        try:
            obj = json.load(open(path, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        v = obj.get("VULVA")
        if not isinstance(v, dict):
            continue
        rows.append({"animal": v.get("ANIMAL_ID"),
                     "date": str(v.get("DATE") or "")[:8],
                     "farm": v.get("FARM_NAME"),
                     "estrus": 1 if str(v.get("ESTRUS")).upper().startswith("Y") else 0})
    df = pd.DataFrame(rows)
    if not len(df):
        return df
    # (개체, 날짜) 중복 제거 — 같은 날 여러 장 촬영
    return (df.groupby(["animal", "date", "farm"], as_index=False)["estrus"]
              .max())


def bbox_index(bbox_dir: str) -> pd.DataFrame:
    """bbox 라벨 디렉터리 → 파일명 인덱스[file, farm, channel, date, animal, ts]."""
    rows = []
    for path in glob.glob(os.path.join(bbox_dir, "**", "*.json"), recursive=True):
        m = BBOX_RE.match(os.path.basename(path)[:-5])
        if not m:
            continue
        rows.append({"path": path, "file": os.path.basename(path),
                     "farm": m["farm"], "channel": m["ch"],
                     "date": m["dt"][:8], "animal": m["animal"],
                     "ts": int(m["ts"])})
    return pd.DataFrame(rows)


def link(cal: pd.DataFrame, idx: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """발정 달력 × bbox 인덱스 → 개체 내 대조 라벨.

    label 1 : 그 개체의 그 날짜가 달력에 있음(발정 확인)
    label 0 : 그 개체가 달력에 존재하지만, 이 날짜는 발정일에서 window 일 초과로 떨어짐
    제외    : 발정일 ±window 이내의 비발정일(애매구간)
    달력에 아예 없는 개체는 제외(음성 신뢰 불가).
    """
    if not len(cal) or not len(idx):
        return pd.DataFrame()
    pos = cal[cal["estrus"] == 1]
    by_animal = pos.groupby("animal")["date"].apply(
        lambda s: sorted(pd.to_datetime(s, format="%Y%m%d"))).to_dict()
    out = []
    for r in idx.itertuples(index=False):
        days = by_animal.get(r.animal)
        if not days:                       # 달력에 없는 개체 → 음성 신뢰 불가
            continue
        d = pd.to_datetime(r.date, format="%Y%m%d", errors="coerce")
        if pd.isna(d):
            continue
        gap = min(abs((d - x).days) for x in days)
        if gap == 0:
            lab = 1
        elif gap > window:
            lab = 0
        else:
            continue                       # 애매구간 제외
        out.append({**r._asdict(), "estrus": lab, "days_from_estrus": gap})
    return pd.DataFrame(out)


def summarize(cal: pd.DataFrame, idx: pd.DataFrame | None = None,
              linked: pd.DataFrame | None = None) -> str:
    lines = [f"발정 달력: 개체 {cal['animal'].nunique()} · 날짜 "
             f"{cal['date'].nunique()} · (개체,날짜) {len(cal)} · "
             f"발정 {int(cal['estrus'].sum())}"]
    if idx is not None and len(idx):
        lines.append(f"bbox 인덱스: 파일 {len(idx):,} · 개체 {idx['animal'].nunique()} · "
                     f"날짜 {idx['date'].nunique()} · 채널 {idx['channel'].nunique()}")
        ov = set(cal["animal"]) & set(idx["animal"])
        lines.append(f"개체 교집합: {len(ov)}두")
    if linked is not None and len(linked):
        n1 = int((linked["estrus"] == 1).sum()); n0 = int((linked["estrus"] == 0).sum())
        per = linked.groupby("animal")["estrus"].nunique()
        lines.append(f"연결 결과: 프레임 {len(linked):,} (발정 {n1:,} / 비발정 {n0:,}) · "
                     f"개체 {linked['animal'].nunique()}")
        lines.append(f"★ 개체 내 대조 가능(양쪽 다 보유): {int((per > 1).sum())}두 "
                     f"— 이 개체들이 카메라 교락 없는 유효 검증 대상")
    elif linked is not None:
        lines.append("연결 결과 없음 — 개체ID/날짜가 겹치는 bbox 표본이 필요")
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cal = load_calendar(sys.argv[1])
    if not len(cal):
        print("외음부 라벨을 찾지 못했습니다(VULVA 키 확인).")
        return 1
    idx = bbox_index(sys.argv[2]) if len(sys.argv) > 2 else pd.DataFrame()
    linked = link(cal, idx) if len(idx) else None
    print(summarize(cal, idx if len(idx) else None, linked))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
