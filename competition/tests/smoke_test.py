"""파이프라인 스모크 테스트.

의존성이 제대로 깔렸는지, 핵심 모듈이 import 되고 최소 파이프라인이 도는지
빠르게 확인한다. 순수 파이썬으로 실행 가능하고(`python competition/tests/smoke_test.py`),
pytest 로도 수집된다(함수명이 test_* ).
"""
from __future__ import annotations

import importlib
import os
import sys

# competition/src 를 import 경로에 추가
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))


def test_dependencies_import() -> None:
    for mod in ("pandas", "numpy", "sklearn", "matplotlib"):
        importlib.import_module(mod)


def test_aihub_client_no_key() -> None:
    """AI Hub 클라이언트가 import 되고, 키 없이 검색 함수가 존재하는지."""
    import aihub
    assert hasattr(aihub, "search")
    assert hasattr(aihub, "download")


def test_pipeline_runs() -> None:
    """소량 합성 데이터로 회귀 파이프라인이 끝까지 도는지."""
    import numpy as np
    import generate_data
    import train

    df = generate_data.generate(n=300)
    for col in ("adg_kg_day", "mortality", "sex", "feed_intake_kg"):
        assert col in df.columns

    num, cat = train.build_features(df)
    assert "sex" in cat and "feed_intake_kg" in num  # 범주/수치 분류 정상

    from sklearn.ensemble import GradientBoostingRegressor
    pipe = train.make_pipeline(num, cat, GradientBoostingRegressor(random_state=0))
    pipe.fit(df[num + cat], df["adg_kg_day"])
    pred = pipe.predict(df[num + cat])
    assert pred.shape[0] == len(df)
    assert np.isfinite(pred).all()


def test_aihub_parsers() -> None:
    """세 데이터셋 파서가 스키마 합성 데이터를 정상 파싱하는지."""
    import tempfile
    import parse_aihub
    for key in ("71763", "71471", "622"):
        with tempfile.TemporaryDirectory() as d:
            parse_aihub.GENERATORS[key](d)
            df = parse_aihub.PARSERS[key](d)
            assert len(df) > 0, f"{key} 파싱 결과가 빔"


def test_pipeline_gilt_integration() -> None:
    """CCTV→무발정 통합 파이프라인: 조인트 생성→신호추출→결합이 되는지."""
    import pipeline_gilt
    frames, mgmt = pipeline_gilt.generate_joint(n_gilts=40, frames=8)
    signals = pipeline_gilt.build_cctv_signals(frames)
    merged = mgmt.merge(signals, on="individual_id", how="inner")
    assert len(merged) == len(mgmt)
    assert "activity_mean" in merged.columns and "feed_adequacy" in merged.columns


def test_estrus_onset_and_dashboard() -> None:
    """발정 시작점 탐지 + 대시보드 데이터 생성이 되는지."""
    import estrus_onset
    import build_dashboard
    import pipeline_gilt
    frames, mgmt = pipeline_gilt.generate_joint(n_gilts=40, frames=10)
    onsets = estrus_onset.detect_all(frames)
    assert len(onsets) == 40
    any_res = next(iter(onsets.values()))
    assert "score" in any_res and "status" in any_res
    data = build_dashboard.build_data(frames, mgmt)
    assert data["meta"]["n_gilts"] == 40
    assert len(data["gilts"]) == 40 and data["importance"]


def test_edinburgh_parser() -> None:
    """Edinburgh output.json 파서(작은 합성 샘플로 검증, 다운로드 불필요)."""
    import json
    import tempfile
    import parse_edinburgh
    sample = {"videoFileName": "color.mp4", "stepSize": 0.1, "config": {},
              "objects": [{"id": "0", "frames": [
                  {"frameNumber": 0, "bbox": {"x": 10, "y": 20, "width": 30,
                   "height": 15}, "visible": True, "behaviour": "walk"},
                  {"frameNumber": 1, "bbox": {"x": 12, "y": 22, "width": 30,
                   "height": 15}, "visible": True, "behaviour": "standing"}]}]}
    with tempfile.TemporaryDirectory() as d:
        import os as _os
        rec = _os.path.join(d, "2019_11_05", "000001")
        _os.makedirs(rec)
        json.dump(sample, open(_os.path.join(rec, "output.json"), "w"))
        df = parse_edinburgh.parse_edinburgh(d)
        assert len(df) == 2
        assert {"individual_id", "frame_idx", "behavior", "centroid_x"} <= set(df.columns)


def test_posture_eval_mapping() -> None:
    """교차검증 도구: 라벨 매핑·피처·소스 로더(작은 CSV)가 동작하는지."""
    import tempfile
    import pandas as pd
    import posture_eval
    assert posture_eval.COMP_TO_COMMON["Sternal_lying"] == "lying"
    assert posture_eval.BEHAVIOR_TO_COMMON["sleep"] == "lying"
    X = posture_eval._feats([100.0, 50.0], [50.0, 100.0], [5000.0, 5000.0])
    assert X.shape == (2, 2)
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
        pd.DataFrame({"behavior": ["standing", "lying", "walk"],
                      "bbox_w": [30, 60, 40], "bbox_h": [40, 30, 35]}).to_csv(f.name, index=False)
        src = posture_eval.load_source(f.name)
    assert set(src["posture"]) <= {"standing", "sitting", "lying"}
    assert len(src) == 2  # walk 제외


def test_view_align_feats() -> None:
    """뷰 정합 피처 함수(작은 df)와 held-out 뷰 정의."""
    import pandas as pd
    import view_align
    assert "pen1_tur_cam1" in view_align.HELD_OUT_VIEWS
    df = pd.DataFrame({"aspect": [1.0, 2.0, 0.5, 1.5],
                       "area": [100, 200, 50, 150],
                       "view": ["a", "a", "b", "b"]})
    b = view_align.baseline_feats(df); v = view_align.view_aligned_feats(df)
    assert b.shape == (4, 2) and v.shape == (4, 2)


def test_estrus_link() -> None:
    """행동→발정 연계: 활발 개체 > 휴식 개체 발정지수 확인."""
    import pandas as pd
    import estrus_link
    rows = []
    # 활발 개체 A(walk/run/investigating), 휴식 개체 B(lying/sleep)
    for f in range(12):
        rows.append({"individual_id": "A", "frame_idx": f,
                     "behavior": ["walk", "run", "investigating"][f % 3],
                     "centroid_x": f * 20.0, "centroid_y": f * 15.0,
                     "aspect_ratio": 1.2, "bbox_w": 60, "bbox_h": 50,
                     "kp_spread": 20.0, "species": "pig", "estrus": None})
        rows.append({"individual_id": "B", "frame_idx": f,
                     "behavior": ["lying", "sleep"][f % 2],
                     "centroid_x": 100.0, "centroid_y": 100.0,
                     "aspect_ratio": 1.3, "bbox_w": 60, "bbox_h": 50,
                     "kp_spread": 20.0, "species": "pig", "estrus": None})
    res = estrus_link.behavior_estrus_index(pd.DataFrame(rows)).set_index("individual_id")
    assert res.loc["A", "estrus_index"] > res.loc["B", "estrus_index"]


def test_aihub_reference() -> None:
    """71471 발정 표준: 어휘 매핑·점수·매핑 합산."""
    import aihub_estrus_reference as ref
    assert ref.to_reference("walk") == "restless"
    assert ref.to_reference("jumpontopof") == "mounting"
    assert ref.to_reference("sleep") == "lying"
    R = ref.EstrusReference()
    # 승가/서성임 개체 > 눕기 개체
    hi = R.score({"mounting": 0.3, "restless": 0.5, "standing": 0.2}, 0.9)
    lo = R.score({"lying": 0.8, "sitting": 0.2}, 0.05)
    assert hi > lo
    m = ref.map_fractions({"walk": 0.4, "run": 0.2, "lying": 0.4})
    assert round(m["restless"], 3) == 0.6 and m["lying"] == 0.4


def test_appearance_crop_feats() -> None:
    """외형 크롭 피처가 40차원으로 산출되는지(더미 이미지)."""
    import numpy as np
    import model_behavior_appearance as mba
    dummy = (np.random.rand(60, 40, 3) * 255).astype("uint8")
    f = mba.crop_feats(dummy)
    assert f.shape == (40,)
    assert mba.crop_feats(None).shape == (40,)


def test_iou_tracker() -> None:
    """IoU 추적기: 이동하는 두 개체에 안정적 ID 부여."""
    import iou_tracker as trk
    frames = [(f, [(f * 2, 10, 20, 20), (100 - f, 100, 20, 20)],
               [{"gt": "A"}, {"gt": "B"}]) for f in range(10)]
    tracks = trk.track_sequence(frames)
    ev = trk.evaluate_vs_gt(tracks)
    assert ev["n_tracks"] == 2 and ev["id_consistency"] == 1.0
    assert trk.iou((0, 0, 10, 10), (0, 0, 10, 10)) == 1.0


def test_eval_report_figs() -> None:
    """평가 리포트 그림 생성(혼동행렬·ROC/PR/보정)이 data URI 를 내는지."""
    import numpy as np
    import build_eval_report as ev
    rng = np.random.default_rng(0)
    y = rng.integers(0, 2, 200)
    proba = np.clip(0.5 + 0.3 * (y - 0.5) + rng.normal(0, 0.2, 200), 0, 1)
    uri, mets = ev.curves_fig(y, proba, "test")
    assert uri.startswith("data:image/png;base64,")
    assert 0.0 <= mets["auc"] <= 1.0 and "brier" in mets
    labels = ["a", "b", "c"]
    yc = rng.choice(labels, 90); pc = rng.choice(labels, 90)
    cm = ev.confusion_fig(yc, pc, labels, "test")
    assert cm.startswith("data:image/png;base64,")
    rows = ev.perclass_bars(yc, pc, labels)
    assert "<tr>" in rows


def test_estrus_reference_validation() -> None:
    """발정 실측 검증 다리: 합성 71471 로 보정 AUC 가 산출되는지."""
    import validate_estrus_reference as ver
    r = ver.evaluate()  # 실파일 없으면 합성 시연
    assert r["is_real"] is False and r["n"] >= 20
    assert 0.0 <= r["auc_calibrated"] <= 1.0
    assert 0.0 <= r["auc_rule"] <= 1.0
    assert len(r["proba"]) == r["n"] and len(r["y"]) == r["n"]


def test_repro_cause_attribution() -> None:
    """번식 문제 유형 분류 + 원인 귀인: THI·심각도·진단 동작."""
    import repro_cause_attribution as rca
    assert rca.thi(30, 80) > rca.thi(20, 50)   # 고온다습이 THI↑
    # 영양·수퇘지 자극 부족 개체 → 원인 귀인
    row = {"backfat_mm": 9.0, "feed_adequacy": 0.5, "temp_c": 22,
           "humidity_pct": 60, "boar_exposure_min": 2, "facility_score": 0.8,
           "water_adequacy": 0.9, "nh3_ppm": 12, "growth_disease_cnt": 0,
           "age_over_target": 20, "activity_mean": 6.0,
           "frac_standing": 0.05, "frac_tailing": 0.02}
    a = rca.attribute(row)
    assert abs(sum(a["share"].values()) - 1.0) < 1e-6
    assert a["top"][0] in rca.CAUSE_GROUPS
    d = rca.diagnose(row, risk=0.9)
    assert d["problem"] in rca.PROBLEMS and d["action"]
    # 활동↓·징후~0 → 무발정, 활동 정상·징후 뚜렷·저위험 → 정상
    assert rca.classify_problem(
        {"activity_norm": 0.05, "frac_standing": 0.02, "frac_tailing": 0.0,
         "age_over_target": 0}, risk=0.9) == "무발정"
    assert rca.classify_problem(
        {"activity_norm": 0.8, "frac_standing": 0.20, "frac_tailing": 0.10,
         "age_over_target": 0}, risk=0.1) == "정상"


def test_estrus_early_warning() -> None:
    """발정 조기경보: D-day 외삽·경보 상태·리드타임 동작."""
    import estrus_early_warning as ew
    # 상승 추세 → 임계 도달일 외삽
    d = ew.predict_onset_day([0, 1, 2, 3], [0.2, 0.3, 0.4, 0.5])
    assert d is not None and d > 3
    # 정체 추세 → 예측 없음
    assert ew.predict_onset_day([0, 1, 2], [0.2, 0.2, 0.2]) is None
    # 발정 도래(임계 지속) → 상태 '발정 확인'
    days = list(range(10)); sc = [0.2, 0.25, 0.3, 0.4, 0.6, 0.7, 0.75, 0.8, 0.82, 0.85]
    a = ew.assess(days, sc)
    assert a["state"] == "발정 확인" and a["onset_actual"] is not None
    # 끝까지 낮음 → 무발정 경보
    flat = ew.assess(list(range(22)), [0.2] * 22)
    assert flat["state"] == "무발정 경보"
    # 타임라인: 지연 개체는 지연/무발정 경보가 발화
    tl = ew.timeline(list(range(22)), [0.2] * 8 + [0.3, 0.5, 0.7, 0.8] + [0.85] * 10)
    assert tl["alert_day"] is not None


def test_repro_dashboard_svg() -> None:
    """번식 대시보드 SVG 헬퍼: 막대·라인차트가 유효 SVG 를 내는지."""
    import build_repro_dashboard as brd
    svg = brd.hbar([("A", 3, "#111", "3두"), ("B", 1, "#222", "1두")])
    assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
    ex = {"normal": {"days": [0, 1, 2], "scores": [0.2, 0.5, 0.8],
                     "onset": 2, "imminent": 1, "alert": None}}
    chart, legend = brd.line_chart(ex)
    assert "<polyline" in chart and "발정 임계" in chart and "정상 발정" in legend


def test_parse_71471_real_schema() -> None:
    """71471 실제 배포 스키마(ANNOTATION_INFO/ESTRUS) 파서 + 실측 검증 경로."""
    import json
    import tempfile
    import parse_71471_real as p71
    import validate_estrus_reference as ver
    acts = ["lying", "standing", "eating", "tailing", "sitting"]
    with tempfile.TemporaryDirectory() as d:
        for k in range(10):
            ts = 160700 + k * 100
            anns = [{"ID": 1000 + k * 10 + i,
                     "BOUNDING_BOX_X_COORDINATE": 142 + i * 180,
                     "BOUNDING_BOX_Y_COORDINATE": 455,
                     "BOUNDING_BOX_WIDTH": 360 - i * 20,
                     "BOUNDING_BOX_HEIGHT": 260 - i * 10,
                     "CATEGORY_NAME": "pig",
                     "ACTION_NAME": "tailing" if i == 0 else acts[i % len(acts)],
                     "ESTRUS": "Y" if i == 0 else "N"} for i in range(5)]
            fn = f"pigfarmA_ch9_2022092109_20-85_{ts}.json"
            json.dump({"INFO": {"VERSION": "1.0"},
                       "IMAGE": {"IMAGE_FILE_NAME": fn.replace(".json", ".jpg"),
                                 "WIDTH": 1920, "HEIGHT": 1080, "TIMESTAMP": ts,
                                 "FARMID": "pigfarmA", "HEADCOUNT": 500},
                       "ANNOTATION_INFO": anns},
                      open(os.path.join(d, fn), "w"), ensure_ascii=False)
        df = p71.parse_dir(d)
        assert len(df) == 50 and df["estrus"].sum() == 10
        assert {"session", "behavior", "estrus", "bbox_w"} <= set(df.columns)
        nm = p71.parse_name("pigfarmA_ch9_2022092109_20-85_160700.json")
        assert nm["farm"] == "pigfarmA" and nm["channel"] == "ch9" and nm["ts"] == 160700
        r = ver.evaluate_real_schema(d)
        assert r["is_real"] and r["schema"] == "71471-real"
        assert 0.0 <= r["auc_calibrated"] <= 1.0


def test_estrus_calendar_link() -> None:
    """외음부 발정 달력 × bbox 인덱스 연결(개체 내 시간 대조)."""
    import json
    import tempfile
    import estrus_calendar as ec
    with tempfile.TemporaryDirectory() as d:
        vd = os.path.join(d, "vulva"); bd = os.path.join(d, "bbox")
        os.makedirs(vd); os.makedirs(bd)
        # 개체 A: 11/02 발정 / 개체 B: 11/09 발정
        for i, (a, dt) in enumerate([("1-16", "20221102_090000"),
                                     ("1-23", "20221109_090000")]):
            json.dump({"VULVA": {"ANIMAL_ID": a, "DATE": dt,
                                 "FARM_NAME": "pigfarmA", "ESTRUS": "Y"}},
                      open(os.path.join(vd, f"v{i}.json"), "w"))
        # bbox: 발정일 프레임 + 멀리 떨어진 비발정일 프레임 + 애매구간
        for a, dt in [("1-16", "2022110209"), ("1-16", "2022101009"),
                      ("1-16", "2022110409"), ("1-23", "2022110909"),
                      ("1-23", "2022100109")]:
            fn = f"pigfarmA_ch1_{dt}_{a}_100.json"
            open(os.path.join(bd, fn), "w").write("{}")
        cal = ec.load_calendar(vd)
        assert len(cal) == 2 and cal["estrus"].sum() == 2
        idx = ec.bbox_index(bd)
        assert len(idx) == 5 and set(idx["animal"]) == {"1-16", "1-23"}
        linked = ec.link(cal, idx, window=3)
        # 발정일 2건(양성), 멀리 떨어진 2건(음성), 11/04(발정+2일)은 제외
        assert int((linked["estrus"] == 1).sum()) == 2
        assert int((linked["estrus"] == 0).sum()) == 2
        assert len(linked) == 4
        # 개체 내 대조가 성립(각 개체가 양성·음성 모두 보유)
        assert (linked.groupby("animal")["estrus"].nunique() > 1).all()


def main() -> int:
    tests = [test_dependencies_import, test_aihub_client_no_key,
             test_pipeline_runs, test_aihub_parsers,
             test_pipeline_gilt_integration, test_estrus_onset_and_dashboard,
             test_edinburgh_parser, test_posture_eval_mapping,
             test_view_align_feats, test_estrus_link, test_aihub_reference,
             test_appearance_crop_feats, test_iou_tracker,
             test_eval_report_figs, test_estrus_reference_validation,
             test_repro_cause_attribution, test_estrus_early_warning,
             test_repro_dashboard_svg, test_parse_71471_real_schema,
             test_estrus_calendar_link]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"  FAIL  {t.__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
