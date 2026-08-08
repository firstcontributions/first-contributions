"""AI Hub 라벨 → 분석용 정형 테이블(train.csv) 파서.

실제 데이터 확보 전, AI Hub 공개 문서(데이터 view 페이지의 '어노테이션 포맷 및
데이터 구조')에서 확인한 스키마에 맞춰 미리 작성했다. 각 파서는 실제 라벨
디렉터리를 받아 pandas DataFrame 을 돌려준다.

세 데이터셋:
  71763  양돈 생체 에너지 데이터(2023)  — JSON, 정형 회귀에 최적
  71471  소·돼지 발정행동 데이터        — JSON, 행동분류/발정탐지
  622    지능형 스마트축사(양돈)         — XML(CVAT), 탐지/자세

각 파서에는 '문서 스키마대로' 합성 샘플을 만드는 generate_synthetic_* 가 딸려
있어, 실데이터 없이도 파싱 로직을 검증할 수 있다(--selftest).

주의: 실제 필드명이 문서와 미세하게 다를 수 있다. 파서는 방어적으로 접근하며
(get/기본값), 실데이터가 오면 이 스키마와 대조해 필요한 곳만 수정한다.
"""
from __future__ import annotations

import json
import os
import random
import xml.etree.ElementTree as ET
from typing import Any

import pandas as pd

# ---------------------------------------------------------------------------
# 71763 양돈 생체 에너지 데이터 (JSON)
#   annotations = {
#     "keypoint-top": [{"pointcount": n, "distance": d}, ...],
#     "TextInfo": {chamber-number, pig-number, weight, pig-classification,
#                  measure-date, measure-time},
#     "SensorData": {T, RH, CO2, NH3, breath-rate},
#     "TemperatureData": {rectal-, back-, neck-, head-temperature},
#     "FeedingAndManagementData": {ventilation-rate, feedstuff-volume,
#         watersupply, pig-manure, sensibleHeat, IatentHeat, ...},
#   }
# ---------------------------------------------------------------------------
PIG_CLASSES_71763 = ["weaningpig", "piglet", "growing-pig", "porker"]


def _num(d: dict, key: str, default: Any = None) -> Any:
    v = d.get(key, default)
    return v if v is not None else default


def parse_71763(label_dir: str) -> pd.DataFrame:
    """71763 라벨 JSON 디렉터리 → 관측 단위 정형 테이블.

    타깃 후보: breath_rate(호흡수), sensible_heat(현열량), latent_heat(잠열량).
    """
    rows: list[dict] = []
    for path in _iter_json(label_dir):
        try:
            obj = json.load(open(path, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        ann = obj.get("annotations", obj)  # 최상위가 곧 annotations 인 경우도 허용
        ti = ann.get("TextInfo", {})
        sd = ann.get("SensorData", {})
        td = ann.get("TemperatureData", {})
        fm = ann.get("FeedingAndManagementData", {})
        kps = ann.get("keypoint-top", []) or []
        kp_dist = kps[0].get("distance") if kps and isinstance(kps[0], dict) else None

        rows.append({
            "chamber": _num(ti, "chamber-number"),
            "pig_id": _num(ti, "pig-number"),
            "weight_kg": _num(ti, "weight"),
            "pig_class": ti.get("pig-classification"),
            "measure_date": ti.get("measure-date"),
            "measure_time": ti.get("measure-time"),
            # 환경 센서
            "temp_c": _num(sd, "T"),
            "humidity_pct": _num(sd, "RH"),
            "co2_ppm": _num(sd, "CO2"),
            "nh3_ppm": _num(sd, "NH3"),
            "breath_rate": _num(sd, "breath-rate"),
            # 개체 온도
            "rectal_temp": _num(td, "rectal-temperature"),
            "back_temp": _num(td, "back-temperature"),
            "neck_temp": _num(td, "neck-temperature"),
            "head_temp": _num(td, "head-temperature"),
            # 사양관리 + 열량(생체에너지)
            "ventilation": _num(fm, "ventilation-rate"),
            "feed_volume": _num(fm, "feedstuff-volume"),
            "water_supply": _num(fm, "watersupply"),
            "manure_heat": _num(fm, "pig-manure"),
            "sensible_heat": _num(fm, "sensibleHeat"),
            "latent_heat": _num(fm, "IatentHeat"),
            "keypoint_distance": kp_dist,
        })
    return pd.DataFrame(rows)


def generate_synthetic_71763(out_dir: str, n: int = 200) -> None:
    """문서 스키마대로 71763 라벨 JSON 을 생성(파서 검증용)."""
    os.makedirs(out_dir, exist_ok=True)
    rng = random.Random(71763)
    for i in range(n):
        T = round(rng.uniform(15, 32), 1)
        RH = round(rng.uniform(40, 85), 1)
        weight = round(rng.uniform(8, 120), 1)
        # 호흡수: 고온·고습일수록 증가(열스트레스)
        breath = round(20 + (T - 20) * 2.2 + (RH - 60) * 0.1 + rng.gauss(0, 3), 1)
        sensible = round(weight * 1.1 + (T - 20) * 0.5 + rng.gauss(0, 5), 1)
        latent = round(weight * 0.7 + (RH - 60) * 0.3 + rng.gauss(0, 4), 1)
        ann = {
            "annotations": {
                "keypoint-top": [{"pointcount": 2,
                                  "distance": round(rng.uniform(20, 90), 1)}],
                "TextInfo": {
                    "chamber-number": rng.randint(1, 8),
                    "pig-number": rng.randint(1, 300),
                    "weight": weight,
                    "pig-classification": rng.choice(PIG_CLASSES_71763),
                    "measure-date": "2023-08-01",
                    "measure-time": f"{rng.randint(0,23):02d}:00:00",
                },
                "SensorData": {"T": T, "RH": RH,
                               "CO2": round(rng.uniform(500, 3000)),
                               "NH3": round(rng.uniform(2, 40), 1),
                               "breath-rate": breath},
                "TemperatureData": {
                    "rectal-temperature": round(rng.uniform(38.5, 40.5), 1),
                    "back-temperature": round(rng.uniform(30, 38), 1),
                    "neck-temperature": round(rng.uniform(30, 38), 1),
                    "head-temperature": round(rng.uniform(30, 38), 1)},
                "FeedingAndManagementData": {
                    "ventilation-rate": round(rng.uniform(10, 60), 1),
                    "feedstuff-volume": round(rng.uniform(0.5, 3.5), 2),
                    "watersupply": round(rng.uniform(1, 10), 1),
                    "pig-manure": round(rng.uniform(50, 300), 1),
                    "sensibleHeat": sensible,
                    "IatentHeat": latent},
            }
        }
        json.dump(ann, open(os.path.join(out_dir, f"S_{i:04d}.json"), "w",
                            encoding="utf-8"), ensure_ascii=False)


# ---------------------------------------------------------------------------
# 71471 소·돼지 발정행동 데이터 (JSON)
#   행동분류: standing/lying/eating/head shaking/tailing/sitting ...
#   발정여부(estrus): 발정체크장비 + 전문가 검수
#   Bounding Box / Keypoints / Polygon 어노테이션
# ---------------------------------------------------------------------------
BEHAVIORS_71471 = ["standing", "lying", "eating", "head shaking",
                   "tailing", "sitting"]
SPECIES_71471 = ["pig", "blackpig"]


def parse_71471(label_dir: str) -> pd.DataFrame:
    """71471 라벨 JSON → 개체·프레임(키프레임) 단위 테이블.

    발정 판단은 시간에 걸친 행동/활동 변화가 핵심이므로, 프레임 단위 행을
    개체(individual_id)·프레임(frame_idx) 식별자와 함께 반환한다. keypoint 는
    프레임 간 이동(활동량) 계산을 위해 중심좌표(centroid)와 산포로 축약한다.
    상위 피처 집계는 build_estrus_features() (model_71471_estrus.py) 가 담당.
    """
    rows: list[dict] = []
    for path in _iter_json(label_dir):
        try:
            obj = json.load(open(path, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        meta = obj.get("metadata", obj.get("info", {}))
        species = obj.get("species") or meta.get("species")
        indiv = (obj.get("individual_id") or meta.get("individual_id")
                 or _id_from_name(os.path.basename(path)))
        frame = (obj.get("frame_idx") if obj.get("frame_idx") is not None
                 else meta.get("frame_idx"))
        estrus = _to_int(obj.get("estrus", meta.get("estrus")))
        for a in _annotations_list(obj):
            bbox = a.get("bbox") or a.get("bounding_box") or []
            kps = a.get("keypoints") or a.get("keypoint") or []
            w = h = None
            if len(bbox) == 4:
                x1, y1, x3, y4 = bbox
                w = abs(x3) if (x3 < x1 or x3 < 5) else abs(x3 - x1)
                h = abs(y4) if (y4 < y1 or y4 < 5) else abs(y4 - y1)
            cx, cy, spread = _keypoint_summary(kps)
            rows.append({
                "file": os.path.basename(path),
                "individual_id": indiv,
                "frame_idx": frame,
                "species": species,
                "behavior": a.get("behavior") or a.get("action")
                            or a.get("category"),
                "estrus": estrus,
                "bbox_w": w, "bbox_h": h,
                "aspect_ratio": (w / h) if (w and h) else None,
                "centroid_x": cx, "centroid_y": cy, "kp_spread": spread,
            })
    return pd.DataFrame(rows)


def _keypoint_summary(kps: list) -> tuple:
    """[x1,y1,x2,y2,...] 평면 리스트 → (중심x, 중심y, 산포)."""
    if not kps:
        return (None, None, None)
    flat = kps
    if isinstance(kps[0], (list, tuple)):  # [[x,y],...] 형태
        flat = [v for xy in kps for v in xy[:2]]
    xs = flat[0::2]
    ys = flat[1::2]
    if not xs or not ys:
        return (None, None, None)
    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)
    spread = (sum((x - cx) ** 2 for x in xs) / len(xs)) ** 0.5
    return (round(cx, 2), round(cy, 2), round(spread, 2))


def _id_from_name(name: str):
    """파일명에서 개체 식별자 추출(발정시간·채널·프레임 인코딩 규칙 대응).

    실데이터 파일명 규칙 확인 후 이 함수만 조정하면 된다. 기본은 마지막
    '_f### / frame' 앞부분을 개체 키로 본다.
    """
    base = name.rsplit(".", 1)[0]
    for tok in ("_f", "_frame", "_F"):
        if tok in base:
            return base.split(tok)[0]
    return base


def generate_synthetic_71471(out_dir: str, n_individuals: int = 80,
                             frames: int = 20) -> None:
    """개체×프레임 구조의 합성 라벨 생성.

    발정 개체는 (a) 활동량↑(프레임 간 중심 이동 큼), (b) standing/tailing 잦음,
    (c) lying 적음 — 이라는 도메인 신호를 심어, 시계열 집계 피처가 학습되도록 한다.
    """
    os.makedirs(out_dir, exist_ok=True)
    rng = random.Random(71471)
    farms = ["pigfarmA", "blackpigB"]
    for ind in range(n_individuals):
        estrus = 1 if rng.random() < 0.4 else 0
        species = rng.choice(SPECIES_71471)
        farm = rng.choice(farms)
        base_x, base_y = rng.uniform(200, 800), rng.uniform(200, 600)
        # 활동량: 발정이 평균적으로 높지만 개체차로 범위가 겹치게(현실적)
        move = (rng.uniform(10, 28) if estrus else rng.uniform(5, 20)) \
            + rng.gauss(0, 3)
        move = max(2.0, move)
        # 행동 분포도 경향만 다르게(완전 분리 아님)
        if estrus:
            probs = {"standing": .24, "tailing": .15, "eating": .15,
                     "head shaking": .10, "sitting": .11, "lying": .25}
        else:
            probs = {"lying": .34, "eating": .20, "standing": .15,
                     "sitting": .13, "head shaking": .08, "tailing": .10}
        behs = list(probs); wts = list(probs.values())
        for f in range(frames):
            behavior = rng.choices(behs, weights=wts)[0]
            cx = base_x + rng.gauss(0, move)
            cy = base_y + rng.gauss(0, move)
            kps = []
            for _ in range(17):  # 17 keypoint
                kps += [round(cx + rng.gauss(0, 25), 1),
                        round(cy + rng.gauss(0, 25), 1)]
            w = rng.uniform(120, 300); h = rng.uniform(70, 180)
            obj = {
                "metadata": {"species": species, "farm": farm,
                             "individual_id": f"{farm}_{ind:03d}",
                             "frame_idx": f},
                "estrus": estrus,
                "annotations": [{
                    "behavior": behavior,
                    "bbox": [round(cx - w / 2, 1), round(cy - h / 2, 1),
                             round(w, 1), round(h, 1)],
                    "keypoints": kps}],
            }
            fn = f"{farm}_{ind:03d}_ch1_f{f:03d}.json"
            json.dump(obj, open(os.path.join(out_dir, fn), "w",
                                encoding="utf-8"), ensure_ascii=False)


# ---------------------------------------------------------------------------
# 622 지능형 스마트축사(양돈) — CVAT XML (annotations.xml)
#   <image name width height>
#     <box label xtl ytl xbr ybr/>
#     <polygon label points="x,y;x,y;..."/>
#     <points label points="x,y;..."/>
#   라벨 = 월령/상태 (이유자돈 전기/후기, 육성돈, 비육돈, 분만돈, 임신돈, 환돈)
# ---------------------------------------------------------------------------
STAGES_622 = ["이유자돈전기", "이유자돈후기", "육성돈전기", "육성돈후기",
              "비육돈전기", "비육돈후기", "분만돈", "임신돈", "환돈"]


def parse_622(label_dir: str) -> pd.DataFrame:
    """622 CVAT XML → 객체 단위 테이블(이미지·라벨·형상)."""
    rows: list[dict] = []
    for path in _iter_files(label_dir, ".xml"):
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError:
            continue
        for img in root.iter("image"):
            iw = _to_float(img.get("width"))
            ih = _to_float(img.get("height"))
            name = img.get("name")
            for box in img.findall("box"):
                xtl, ytl = _to_float(box.get("xtl")), _to_float(box.get("ytl"))
                xbr, ybr = _to_float(box.get("xbr")), _to_float(box.get("ybr"))
                rows.append({
                    "file": os.path.basename(path), "image": name,
                    "img_w": iw, "img_h": ih, "shape": "box",
                    "label": box.get("label"),
                    "obj_w": (xbr - xtl) if (xbr and xtl) else None,
                    "obj_h": (ybr - ytl) if (ybr and ytl) else None,
                })
            for poly in list(img.findall("polygon")) + list(img.findall("points")):
                pts = _parse_points(poly.get("points", ""))
                rows.append({
                    "file": os.path.basename(path), "image": name,
                    "img_w": iw, "img_h": ih,
                    "shape": poly.tag, "label": poly.get("label"),
                    "num_points": len(pts),
                })
    return pd.DataFrame(rows)


def generate_synthetic_622(out_dir: str, n_images: int = 60) -> None:
    os.makedirs(out_dir, exist_ok=True)
    rng = random.Random(622)
    root = ET.Element("annotations")
    for i in range(n_images):
        img = ET.SubElement(root, "image", id=str(i), name=f"img_{i:04d}.jpg",
                            width="1920", height="1080")
        for _ in range(rng.randint(1, 6)):
            label = rng.choice(STAGES_622)
            xtl, ytl = rng.uniform(0, 1500), rng.uniform(0, 800)
            ET.SubElement(img, "box", label=label,
                          xtl=f"{xtl:.1f}", ytl=f"{ytl:.1f}",
                          xbr=f"{xtl + rng.uniform(50, 300):.1f}",
                          ybr=f"{ytl + rng.uniform(50, 250):.1f}")
            if rng.random() < 0.5:
                pts = ";".join(f"{rng.uniform(0,1920):.1f},{rng.uniform(0,1080):.1f}"
                               for _ in range(rng.randint(4, 10)))
                ET.SubElement(img, "polygon", label=label, points=pts)
    ET.ElementTree(root).write(os.path.join(out_dir, "annotations.xml"),
                               encoding="utf-8", xml_declaration=True)


# --------------------------- 공용 유틸 ---------------------------
def _iter_files(root: str, ext: str):
    for dp, _, fs in os.walk(root):
        for f in fs:
            if f.lower().endswith(ext):
                yield os.path.join(dp, f)


def _iter_json(root: str):
    return _iter_files(root, ".json")


def _annotations_list(obj: dict) -> list[dict]:
    a = obj.get("annotations", [])
    if isinstance(a, dict):
        return [a]
    return a if isinstance(a, list) else []


def _parse_points(s: str) -> list[tuple[float, float]]:
    out = []
    for pair in s.split(";"):
        if "," in pair:
            x, y = pair.split(",")[:2]
            out.append((_to_float(x), _to_float(y)))
    return out


def _to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _to_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


# --------------------------- CLI / self-test ---------------------------
PARSERS = {"71763": parse_71763, "71471": parse_71471, "622": parse_622}
GENERATORS = {"71763": generate_synthetic_71763,
              "71471": generate_synthetic_71471,
              "622": generate_synthetic_622}


def selftest() -> int:
    import tempfile
    ok = True
    for key in ("71763", "71471", "622"):
        with tempfile.TemporaryDirectory() as d:
            GENERATORS[key](d)
            df = PARSERS[key](d)
            n = len(df)
            print(f"[{key}] 합성→파싱 행 {n}, 열 {df.shape[1]}: "
                  f"{list(df.columns)[:6]}...")
            if n == 0:
                ok = False
                print(f"  ‼ {key} 파싱 결과가 비었습니다.")
            else:
                nonnull = df.notna().mean().mean()
                print(f"  평균 비결측 비율 {nonnull:.0%}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv or argv[0] == "--selftest":
        return selftest()
    if len(argv) < 2:
        print("사용: python parse_aihub.py <71763|71471|622> <label_dir> "
              "[out.csv]  |  --selftest")
        return 1
    key, label_dir = argv[0], argv[1]
    if key not in PARSERS:
        print(f"알 수 없는 데이터셋: {key}")
        return 1
    df = PARSERS[key](label_dir)
    out = argv[2] if len(argv) >= 3 else f"competition/data/{key}_parsed.csv"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    df.to_csv(out, index=False, encoding="utf-8-sig")
    print(f"[{key}] 파싱 완료: {len(df)}행 → {out}")
    print(df.head())
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv[1:]))
