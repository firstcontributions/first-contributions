"""71471 발정 라벨 감사 — **피처로 쓰기 전에 누수부터 본다**.

STATUS.md 3-1 A-2. 발정 AUC 0.465 를 올릴 후보로 `vulva_dir`(외음부 주석)을
피처로 쓰자는 안이 있다. 그런데 그게 **주석자가 발정을 이미 알고 붙인 라벨**
이면, 피처로 쓰는 건 정답을 피처 쪽으로 옮기는 것이다. AUC 가 크게 뛰어도
누수다. 이 프로젝트는 누수된 0.642 를 버리고 0.467 을 썼다(원칙 2) — 같은
실수를 반대편에서 반복하면 그 결정의 값어치가 사라진다.

**AUC 가 잘 나올수록 의심한다.** 그래서 모델을 돌리기 전에 이 감사를 통과해야
한다. 감사 중에는 발정 라벨과 후보 피처를 함께 쓰는 어떤 모델도 학습하지 않고,
교차표와 분포만 본다.

## 검사 다섯

    L1 존재 자체가 라벨인가   발정 구간에만 값이 채워져 있나(결측이 곧 라벨)
    L2 완전 분리              특정 값이 한쪽에서만 100%/0% 로 나오나
    L3 주석 순서              발정이 먼저 붙고 후보가 나중에 붙었나
    L4 프레임 일관성          프레임마다 붙었나, 판정 구간에만 붙었나
    L5 주석자 맹검            주석자가 발정 여부를 알 수 있었나

L5 는 코드로 확인할 수 없는 경우가 많다. **가이드에 명시가 없으면 '확인 불가'
로 기록하고 추정하지 않는다.** 그리고 확인 불가는 통과가 아니다 — 회색이면
진행하지 않는다.

## 판정

    청색  L1~L5 전부 통과, L1 정확도가 우연 수준   → 본 실험 진행
    회색  하나라도 확인 불가                        → **중단.** 한계로 기록
    적색  L1·L2·L4 중 하나라도 걸림                 → 부정 결과 심화

    python competition/src/estrus_label_audit.py --bbox <bbox_dir> [--vulva <vulva_dir>]
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

OUT = os.path.join(ROOT, "data", "estrus_label_audit.json")

# pigfarmA_ch10_2022071510_025_01645
NAME_RE = re.compile(r"(?P<farm>pigfarm\w+?)_ch(?P<ch>\d+)_(?P<stamp>\d{10})"
                     r"_(?P<pen>[\w\-]+)_(?P<ts>\d+)$")

# 이 값들이 한쪽 라벨에서만 나오면 완전 분리다
SEP_HI = 0.98          # 이 이상이면 완전 분리로 본다
CHANCE = 0.02          # 다수 클래스 대비 이만큼 넘으면 우연 수준이 아니다


def _flag(ok: bool | None) -> str:
    return "통과" if ok is True else ("확인 불가" if ok is None else "걸림")


def load_bbox(bbox_dir: str) -> pd.DataFrame:
    """bbox 주석 → 박스 한 줄. **ESTRUS 가 이 파일 안에 들어 있다.**"""
    rows = []
    for p in sorted(glob.glob(os.path.join(bbox_dir, "**", "*.json"),
                              recursive=True)):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:                                    # noqa: BLE001
            continue
        img, info = d.get("IMAGE") or {}, d.get("INFO") or {}
        m = NAME_RE.match(os.path.basename(p)[:-5])
        for a in d.get("ANNOTATION_INFO") or []:
            rows.append({
                "file": os.path.basename(p)[:-5],
                "farm": img.get("FARMID"),
                "ch": int(m.group("ch")) if m else None,
                "stamp": m.group("stamp") if m else None,
                "pen": m.group("pen") if m else None,
                "created": info.get("CREATE_DATE_TIME"),
                "estrus": a.get("ESTRUS"),
                "action": a.get("ACTION_NAME"),
                "injection": a.get("INJECTION"),
                "has_injection": "INJECTION" in a,
                "feed": a.get("FEED"),
            })
    return pd.DataFrame(rows)


def load_vulva(vulva_dir: str) -> pd.DataFrame:
    """외음부 주석 → 레코드 한 줄. `estrus_calendar.load_calendar` 와 같은
    스키마를 읽되, **버리지 않고 전부 들고 온다** — 어떤 필드가 있는지 자체가
    감사 대상이다."""
    rows = []
    for p in sorted(glob.glob(os.path.join(vulva_dir, "**", "*.json"),
                              recursive=True)):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:                                    # noqa: BLE001
            continue
        v = d.get("VULVA")
        if not isinstance(v, dict):
            continue
        row = {f"v_{k}": v.get(k) for k in v}
        row["file"] = os.path.basename(p)[:-5]
        row["created"] = (d.get("INFO") or {}).get("CREATE_DATE_TIME")
        rows.append(row)
    return pd.DataFrame(rows)


def _sep(d: pd.DataFrame, col: str, label: str) -> dict:
    """L2 — 어떤 값이 한쪽 라벨에서만 나오는가."""
    t = pd.crosstab(d[col].fillna("(결측)"), d[label])
    if t.shape[1] < 2:
        return {"note": "라벨이 한 종류뿐이라 분리를 볼 수 없다", "n": int(len(d))}
    share = t.div(t.sum(axis=1), axis=0)
    worst = share.max(axis=1)
    bad = worst[worst >= SEP_HI]
    return {"table": t.to_dict(),
            "separating_values": {str(k): round(float(v), 4)
                                  for k, v in bad.items()},
            "max_share": round(float(worst.max()), 4)}


def _predict_from(d: pd.DataFrame, col: str, label: str) -> dict:
    """그 열 하나만으로 라벨을 얼마나 맞히나 — 다수 클래스와 비교한다.

    이게 우연 수준을 크게 넘으면 그 열은 **라벨의 사본**이지 피처가 아니다.
    """
    g = d.groupby(d[col].fillna("(결측)"))[label]
    pred = g.transform(lambda s: s.mode().iloc[0] if len(s) else None)
    acc = float((pred == d[label]).mean())
    maj = float(d[label].value_counts(normalize=True).max())
    return {"acc": round(acc, 4), "majority": round(maj, 4),
            "gain": round(acc - maj, 4), "leaky": (acc - maj) > CHANCE}


def audit_bbox(bbox_dir: str) -> dict:
    """bbox 쪽 감사. **VULVA 가 없어도 여기까지는 잰다.**"""
    d = load_bbox(bbox_dir)
    if not len(d):
        return {"error": f"{bbox_dir} 에서 읽은 박스가 0개다"}
    d = d[d["estrus"].notna()]
    out = {
        "n_files": int(d["file"].nunique()), "n_boxes": int(len(d)),
        "fields": sorted({c for c in d.columns}),
        "estrus": {str(k): int(v) for k, v in
                   d["estrus"].value_counts(dropna=False).items()},
        "channels": int(d["ch"].nunique()),
    }
    # L2 — 카메라 채널이 라벨을 결정하는가
    out["L2_channel"] = _sep(d, "ch", "estrus")
    out["L2_channel_predict"] = _predict_from(d, "ch", "estrus")
    # L1 — 결측 자체가 라벨인가(INJECTION 블록의 유무)
    out["L1_missing"] = _predict_from(d, "has_injection", "estrus")
    # L4 — 한 파일(프레임) 안에서 라벨이 섞이는가. 안 섞이면 프레임 라벨이
    #      아니라 돈방·세션 라벨이라는 뜻이다.
    mixed = int((d.groupby("file")["estrus"].nunique() > 1).sum())
    out["L4_frame"] = {"mixed_files": mixed, "n_files": out["n_files"],
                       "share_mixed": round(mixed / max(1, out["n_files"]), 4)}
    # L3 — 주석 생성 시각이 라벨별로 다른가
    if d["created"].notna().any():
        ct = d.groupby("estrus")["created"].agg(["min", "max", "nunique"])
        out["L3_created"] = ct.astype(str).to_dict()
    return out


def audit_vulva(vulva_dir: str, bbox: pd.DataFrame | None = None) -> dict:
    """외음부 주석 감사. **ESTRUS 가 같은 레코드에 있는지부터 본다.**"""
    d = load_vulva(vulva_dir)
    if not len(d):
        return {"error": f"{vulva_dir} 에서 읽은 VULVA 레코드가 0개다",
                "verdict": "확인 불가"}
    cols = [c for c in d.columns if c.startswith("v_")]
    lab = "v_ESTRUS"
    out = {"n": int(len(d)), "fields": cols,
           "has_estrus_field": lab in d.columns}
    if lab not in d.columns:
        out["verdict"] = "확인 불가 — ESTRUS 필드가 없어 대조할 라벨이 없다"
        return out
    d[lab] = d[lab].astype(str).str.upper().str[:1]
    out["estrus"] = {str(k): int(v) for k, v in d[lab].value_counts().items()}
    # 후보 피처 = ESTRUS 를 뺀 나머지 VULVA 필드
    cand = [c for c in cols if c != lab and d[c].nunique(dropna=False) > 1]
    out["candidates"] = cand
    out["L1_missing"] = {c: _predict_from(d.assign(_m=d[c].notna()), "_m", lab)
                         for c in cand}
    out["L2_separation"] = {c: _sep(d, c, lab) for c in cand
                            if d[c].nunique() <= 20}
    return out


def verdict(bb: dict, vv: dict | None) -> dict:
    """청/회/적. **확인 불가는 통과가 아니다.**"""
    checks = {}
    # L2 는 bbox 에서 실측된다
    p = bb.get("L2_channel_predict") or {}
    checks["L2 완전 분리"] = not p.get("leaky", False)
    checks["L1 결측이 곧 라벨"] = not (bb.get("L1_missing") or {}).get("leaky", False)
    f = bb.get("L4_frame") or {}
    # 프레임마다 라벨이 갈리지 않으면 프레임 라벨이 아니다 → 걸림
    checks["L4 프레임 일관성"] = f.get("share_mixed", 0) > 0.05
    checks["L3 주석 순서"] = None       # 생성 시각만으로는 순서를 못 정한다
    checks["L5 주석자 맹검"] = None     # 가이드에 명시 없음 — 추정하지 않는다
    if vv is None or vv.get("error"):
        checks["VULVA 감사"] = None
    else:
        leaky = any(v.get("leaky") for v in (vv.get("L1_missing") or {}).values())
        checks["VULVA 감사"] = not leaky
    if any(v is False for v in checks.values()):
        col = "적색"
    elif any(v is None for v in checks.values()):
        col = "회색"
    else:
        col = "청색"
    return {"checks": checks, "color": col}


def run(bbox_dir: str, vulva_dir: str | None = None) -> dict:
    bb = audit_bbox(bbox_dir)
    vv = audit_vulva(vulva_dir) if vulva_dir else None
    return {"bbox": bb, "vulva": vv, "verdict": verdict(bb, vv)}


def _print(r: dict) -> None:
    bb, vv, vd = r["bbox"], r.get("vulva"), r["verdict"]
    print("=" * 78)
    print("  71471 발정 라벨 감사 — 피처로 쓰기 전에")
    print("=" * 78)
    if bb.get("error"):
        print(f"  ❌ {bb['error']}")
        return
    print(f"\n  [bbox] 파일 {bb['n_files']:,} · 박스 {bb['n_boxes']:,} · "
          f"채널 {bb['channels']} · ESTRUS {bb['estrus']}")

    p = bb["L2_channel_predict"]
    t = bb["L2_channel"]
    print(f"\n  L2 완전 분리 — 카메라 채널만으로 발정을 맞히면?")
    print(f"     정확도 {p['acc']:.4f} vs 다수 클래스 {p['majority']:.4f} "
          f"(+{p['gain']:.4f})  →  {_flag(not p['leaky'])}")
    if t.get("separating_values"):
        ks = list(t["separating_values"])[:16]
        print(f"     한쪽으로 완전히 쏠린 채널 {len(t['separating_values'])}개: "
              f"{', '.join('ch' + k for k in ks)}")

    m = bb["L1_missing"]
    print(f"\n  L1 결측이 곧 라벨인가 — 필드 유무만으로 맞히면?")
    print(f"     정확도 {m['acc']:.4f} vs {m['majority']:.4f} "
          f"(+{m['gain']:.4f})  →  {_flag(not m['leaky'])}")

    f = bb["L4_frame"]
    print(f"\n  L4 프레임 일관성 — 한 파일 안에서 라벨이 갈리나?")
    print(f"     섞인 파일 {f['mixed_files']}/{f['n_files']} "
          f"({f['share_mixed']:.2%})  →  {_flag(f['share_mixed'] > 0.05)}")
    if f["share_mixed"] <= 0.05:
        print(f"     거의 안 갈린다 = **프레임 라벨이 아니라 돈방·세션 라벨**이다")

    print(f"\n  [VULVA]")
    if vv is None:
        print(f"     디렉터리가 주어지지 않았다 — 감사 못 함")
    elif vv.get("error"):
        print(f"     {vv['error']}")
    else:
        print(f"     레코드 {vv['n']:,} · 필드 {vv['fields']}")
        print(f"     ESTRUS 필드가 같은 레코드에 있나: "
              f"{'예' if vv['has_estrus_field'] else '아니오'}")
        for c, s in (vv.get("L1_missing") or {}).items():
            print(f"       {c:<24}결측만으로 {s['acc']:.4f} "
                  f"(다수 {s['majority']:.4f})  {_flag(not s['leaky'])}")

    print(f"\n  [판정] **{vd['color']}**")
    for k, v in vd["checks"].items():
        mark = {"통과": "✅", "걸림": "❌", "확인 불가": "⬜"}[_flag(v)]
        print(f"     {mark} {k:<18}{_flag(v)}")
    if vd["color"] != "청색":
        print(f"\n  → 청색이 아니면 본 실험을 진행하지 않는다. "
              f"확인 불가는 통과가 아니다.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="estrus_label_audit")
    ap.add_argument("--bbox", required=True, help="bbox 라벨 디렉터리")
    ap.add_argument("--vulva", default=None, help="외음부 라벨 디렉터리")
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    r = run(a.bbox, a.vulva)
    _print(r)
    if a.out:
        json.dump(r, open(a.out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1, default=str)
        print(f"\n저장: {a.out}")
    print("\n※ 원자료는 커밋하지 않는다. 집계 표만 남긴다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
