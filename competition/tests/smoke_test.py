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
    # 등지방은 U자형 — 적정(16~22mm)은 무벌점, 야윔·비만 양쪽에 벌점
    base = {"feed_adequacy": 0.9, "temp_c": 22, "humidity_pct": 60,
            "boar_exposure_min": 20, "facility_score": 0.9,
            "water_adequacy": 0.9, "nh3_ppm": 10, "growth_disease_cnt": 0}
    sev = lambda bf: rca.attribute({**base, "backfat_mm": bf})["severity"]["영양 부족"]
    assert sev(17) == 0.0, "적정 등지방에 벌점"
    assert sev(9) > 0.3, "야윔에 벌점 없음"
    assert sev(26) > 0.3, "비만에 벌점 없음(양방향 미반영)"
    assert 1.0 <= rca.bcs_from_backfat(17) <= 5.0
    assert rca.bcs_from_backfat(9) < rca.bcs_from_backfat(17) < rca.bcs_from_backfat(25)
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


def test_estrus_contrast_eval() -> None:
    """개체 내 대조 발정 검증: 프레임 구성·그룹 AUC·결론 문장."""
    import json
    import tempfile
    import estrus_contrast_eval as ece
    acts = ["lying", "standing", "sitting", "eating"]
    with tempfile.TemporaryDirectory() as d:
        vd = os.path.join(d, "v"); bd = os.path.join(d, "b")
        os.makedirs(vd); os.makedirs(bd)
        animals = ["1-10", "1-11", "1-12", "1-13"]
        for i, a in enumerate(animals):   # 모두 09/21 발정
            json.dump({"VULVA": {"ANIMAL_ID": a, "DATE": "20220921_090000",
                                 "FARM_NAME": "pigfarmA", "ESTRUS": "Y"}},
                      open(os.path.join(vd, f"v{i}.json"), "w"))
        # 같은 채널(ch3)에서 발정일(0921)·비발정일(1005) 프레임 생성
        for a in animals:
            for dt in ("2022092109", "2022100509"):
                for t in range(6):
                    anns = [{"ID": 1, "BOUNDING_BOX_X_COORDINATE": 10 + j * 50,
                             "BOUNDING_BOX_Y_COORDINATE": 20,
                             "BOUNDING_BOX_WIDTH": 100, "BOUNDING_BOX_HEIGHT": 80,
                             "CATEGORY_NAME": "pig",
                             "ACTION_NAME": acts[(j + t) % 4], "ESTRUS": "Y"}
                            for j in range(4)]
                    fn = f"pigfarmA_ch3_{dt}_{a}_{1000 + t}.json"
                    json.dump({"IMAGE": {"IMAGE_FILE_NAME": fn[:-5] + ".jpg",
                                         "WIDTH": 1920, "HEIGHT": 1080,
                                         "TIMESTAMP": 1000 + t, "FARMID": "pigfarmA"},
                               "ANNOTATION_INFO": anns},
                              open(os.path.join(bd, fn), "w"))
        F = ece.build_frames(vd, bd)
        assert len(F) == 48 and F["animal"].nunique() == 4
        assert F.groupby("animal")["y"].nunique().eq(2).all()  # 개체 내 대조 성립
        r = ece.evaluate(vd, bd)
        assert r["ok"] and r["n_within_contrast"] == 4
        assert r["auc_behavior"] is not None
        assert isinstance(ece.verdict(r), str) and ece.verdict(r)


def test_keypoints_parser_pose() -> None:
    """71471 [Keypoints] 파서 + 회전·크기 불변 자세 기술자."""
    import json
    import tempfile
    import numpy as np
    import parse_71471_keypoints as kpp
    # 자세 기술자: 회전·평행이동·크기를 바꿔도 쌍거리는 동일해야 한다
    base = np.array([[0, 0], [10, 0], [20, 0], [20, 10],
                     [10, 10], [0, 10], [5, 5], [15, 5]], float)
    kp1 = np.hstack([base, np.full((8, 1), 2.0)])
    th = np.pi / 3
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    kp2 = np.hstack([(base @ R.T) * 2.5 + 100, np.full((8, 1), 2.0)])
    f1, f2 = kpp.pose_features(kp1), kpp.pose_features(kp2)
    for c in kpp.PAIR_COLS[:6]:
        assert abs(f1[c] - f2[c]) < 1e-6, f"{c} 불변성 위반"
    assert abs(f1["kp_elong"] - f2["kp_elong"]) < 1e-6
    # 파서
    with tempfile.TemporaryDirectory() as d:
        kp = [v for j in range(8) for v in (800 + j * 10, 600 + (j % 3) * 15, 2)]
        fn = "pigfarmA_ch9_2022080509_334_663233.json"
        json.dump({"IMAGE": {"IMAGE_FILE_NAME": fn[:-5] + ".jpg", "WIDTH": 1920,
                             "HEIGHT": 1080, "TIMESTAMP": 663233, "FARMID": "pigfarmA"},
                   "ANNOTATION_INFO": [{"ID": 1, "KEYPOINTS": kp, "NUM_KEYPIONTS": 8,
                                        "CATEGORY_NAME": "pig", "ACTION_NAME": "lying",
                                        "ESTRUS": "N"}]},
                  open(os.path.join(d, fn), "w"))
        df = kpp.parse_dir(d)
        assert len(df) == 1 and df["animal"].iloc[0] == "334"
        assert df["channel"].iloc[0] == "ch9" and df["estrus"].iloc[0] == 0
        assert set(kpp.FEATURES) <= set(df.columns) and len(kpp.FEATURES) == 44


def test_pose_vs_behavior_eval() -> None:
    """자세 vs 행동라벨 비교 평가: 채널 분리 검증과 결론 문장."""
    import json
    import tempfile
    import random
    import pose_vs_behavior_eval as pve
    random.seed(4)
    acts = ["lying", "standing", "sitting", "eating"]
    with tempfile.TemporaryDirectory() as d:
        # ch1~4 발정 / ch5~8 비발정 (클래스별 채널 4개씩)
        for ch in range(1, 9):
            est = "Y" if ch <= 4 else "N"
            for t_ in range(6):
                anns = []
                for i in range(3):
                    kp = [v for j in range(8) for v in
                          (800 + i * 150 + j * 11 + random.randint(-4, 4),
                           600 + (j % 3) * 18 + random.randint(-4, 4), 2)]
                    anns.append({"ID": ch * 100 + t_ * 10 + i, "KEYPOINTS": kp,
                                 "NUM_KEYPIONTS": 8, "CATEGORY_NAME": "pig",
                                 "ACTION_NAME": random.choice(acts), "ESTRUS": est})
                fn = f"pigfarmA_ch{ch}_2022071009_100_{5000 + t_}.json"
                json.dump({"IMAGE": {"IMAGE_FILE_NAME": fn[:-5] + ".jpg",
                                     "WIDTH": 1920, "HEIGHT": 1080,
                                     "TIMESTAMP": 5000 + t_, "FARMID": "pigfarmA"},
                           "ANNOTATION_INFO": anns},
                          open(os.path.join(d, fn), "w"))
        r = pve.evaluate(d)
        assert r["ok"] and r["n_channels"] == 8
        assert r["n_pos_ch"] == 4 and r["n_neg_ch"] == 4
        assert 0.0 <= r["auc_pose"] <= 1.0 and 0.0 <= r["auc_behavior"] <= 1.0
        assert set(r["auc_pose_parts"]) == {"쌍거리(28)", "형태지표(8)", "가시성(8)"}
        assert isinstance(pve.verdict(r), str) and pve.verdict(r)


def test_motion_tracker() -> None:
    """카메라 모션 보상 추적: 화면 전체가 이동해도 ID 유지."""
    import numpy as np
    import motion_tracker as mt
    # 카메라가 오른쪽으로 20px 이동한 것과 동등한 아핀
    M = np.array([[1.0, 0.0, 20.0], [0.0, 1.0, 0.0]])
    assert abs(mt.motion_magnitude(M) - 20.0) < 1e-6
    b = mt.warp_box((10, 10, 40, 30), M)
    assert abs(b[0] - 30) < 1e-6 and abs(b[1] - 10) < 1e-6
    # 개체는 정지, 카메라만 이동 → 보상하면 트랙 2개 유지
    mc, plain = mt.MCIoUTracker(), mt.MCIoUTracker()
    ids_mc, ids_pl = set(), set()
    M = np.array([[1.0, 0.0, 50.0], [0.0, 1.0, 0.0]])   # 박스 너비(40)보다 큰 이동
    for k in range(6):
        sh = k * 50.0                      # 카메라 누적 이동
        boxes = [(10 + sh, 10, 40, 30), (400 + sh, 100, 40, 30)]
        for tid, _ in mc.update(boxes, M if k else None):
            ids_mc.add(tid)
        for tid, _ in plain.update(boxes, None):
            ids_pl.add(tid)
    assert len(ids_mc) == 2, f"보상 시 ID 유지 실패: {len(ids_mc)}"
    assert len(ids_pl) > len(ids_mc)        # 보상 없으면 과분할


def test_box_merge() -> None:
    """창살 분할 박스 병합: 인접 조각은 합치고 멀리 떨어진 개체는 유지."""
    import box_merge as bm
    # 조각(작음) 2개 + 온전한 개체 2마리 → 조각만 합쳐 3개가 되어야 한다.
    # (프레임 내 '온전한 개체 크기'가 있어야 무엇이 조각인지 판별 가능하다)
    mix = [(0, 0, 45, 60), (50, 2, 45, 58), (300, 0, 100, 60), (420, 0, 100, 60)]
    assert len(bm.merge_split_boxes(mix)) == 3
    assert len(bm.merge_split_boxes([(100, 100, 60, 80), (500, 100, 60, 80)])) == 2
    assert len(bm.merge_split_boxes([(10, 10, 50, 50)])) == 1
    # 과병합 방지(실측 회귀): 비슷한 크기 개체가 나란히 붙어 있으면 합치지 않는다.
    # 군사 사육 영상에서 이 케이스를 놓쳐 마릿수가 5→1 로 붕괴한 적이 있다.
    adj = [(0, 0, 100, 60), (102, 0, 100, 60), (204, 0, 100, 60)]
    assert len(bm.merge_split_boxes(adj)) == 3, "붙어 있는 개체를 과병합함"


def test_temporal_features() -> None:
    """시간 윈도우 피처: 서성임(제자리 맴돎) vs 직선 이동 구분."""
    import numpy as np
    import pandas as pd
    import temporal_features as tf
    rows = []
    for k in range(20):                     # A: 제자리 왕복(서성임)
        rows.append({"individual_id": "A", "frame_idx": k, "speed": 5.0,
                     "centroid_x": 100 + (5 if k % 2 else -5), "centroid_y": 100,
                     "darea": 0.0})
    for k in range(20):                     # B: 직선 이동
        rows.append({"individual_id": "B", "frame_idx": k, "speed": 5.0,
                     "centroid_x": 100 + 5 * k, "centroid_y": 100, "darea": 0.0})
    d = tf.add_temporal(pd.DataFrame(rows))
    assert set(tf.TEMPORAL_COLS) <= set(d.columns)
    a = d[(d.individual_id == "A") & (d.frame_idx >= 15)]["path_ratio15"].mean()
    b = d[(d.individual_id == "B") & (d.frame_idx >= 15)]["path_ratio15"].mean()
    assert a > b, f"서성임 경로비({a:.2f})가 직선({b:.2f})보다 커야 함"
    assert np.isfinite(d[tf.TEMPORAL_COLS].to_numpy()).all()


def test_breeding_timing() -> None:
    """교배 적기: WEI 보정·argmax 권장·회전율 경제 계산."""
    import breeding_timing as bt
    # WEI 가 짧으면 발정이 길고 배란이 늦다
    assert bt.ovulation_time("sow", 4) > bt.ovulation_time("sow", 10)
    # 후보돈은 경산돈보다 발정이 짧다
    assert bt.estrus_duration("gilt", 7) < bt.estrus_duration("sow", 7)
    # 권장 시각은 **자기 모델의 argmax** — 관행(12/24h)보다 항상 낫거나 같아야 한다
    for parity in ("sow", "gilt"):
        for wei in (4, 7, 10):
            w = bt.insemination_window(parity, wei)
            opt = bt.conception_prob([w["ai1_h"], w["ai2_h"]], parity, wei)
            routine = bt.conception_prob([12, 24], parity, wei)
            assert opt >= routine - 1e-9, f"{parity} WEI{wei}: 권장이 관행보다 나쁨"
            # 창은 유효도 정점을 포함하고, 정점은 **배란보다 앞**이어야 한다
            # (수정능획득 때문 — 배란 정각 주입은 이미 늦다)
            assert w["window_start_h"] <= w["peak_h"] <= w["window_end_h"]
            assert w["peak_h"] < w["ovulation_h"], "정점이 배란 이후 — 수정능획득 누락"

    # 수정능획득 지연: 배란 직전 주입보다 몇 시간 앞선 주입이 낫다
    ov = bt.ovulation_time("sow", 7)
    assert bt.ai_efficacy(ov - 8, "sow", 7) > bt.ai_efficacy(ov, "sow", 7)
    # 지침의 '주입 금지' 구간은 유효도가 낮아야 한다
    assert bt.ai_efficacy(0, "sow", 7) < 0.05
    assert bt.ai_efficacy(4, "sow", 7) < bt.ai_efficacy(24, "sow", 7)
    # 배란 한참 뒤 수정은 수태율이 급감한다
    assert bt.conception_prob([ov - 6], "sow", 7) > bt.conception_prob([ov + 30], "sow", 7)

    # 현장 지침(적기 12~36h)과 대조 — 권장값이 구간을 벗어나면 안 된다
    for parity in ("sow", "gilt"):
        for wei in (4, 7, 10):
            c = bt.check_against_field_guide(parity, wei)
            assert c["in_window"], f"{parity} WEI{wei}: 권장 {c['ai_times']} 이 지침 이탈"
            assert c["peak_in_window"] and c["no_early_ai"]

    # 관측 지연: 점검 주기가 길수록 수태율이 떨어진다(각 주기의 최적 프로토콜 기준).
    # 오프셋을 고정한 채 지연만 키우면 하루 1회 점검이 0.37 로 나오는 비현실적
    # 결과가 됐다 — 주기마다 최적 프로토콜을 다시 찾아 비교해야 한다.
    prev = None
    for iv in (0, 6, 12, 24):
        d = bt.detection_value(iv, "sow", 7)
        assert 0.5 < d["conception"] <= 1.0, f"{iv}h 주기 수태율 {d['conception']}"
        if prev is not None:
            assert d["conception"] <= prev + 1e-9, "점검이 뜸한데 수태율이 올랐다"
        prev = d["conception"]
    # 점검이 뜸할수록 프로토콜은 더 이르게 잡혀야 한다(지연을 미리 상쇄)
    assert (bt.best_offsets_for_interval(24, "sow", 7)[0]
            < bt.best_offsets_for_interval(0, "sow", 7)[0])

    tl = bt.estrus_timeline("sow", 7)
    assert tl["vulva_change"][0] < tl["standing_heat"][0], \
        "외음부 변화가 승가허용보다 늦다 — 조기 신호가 성립하지 않음"
    assert tl["prodromal"][1] <= tl["standing_heat"][0]
    # 회전율: 수태율이 높을수록 회전 빠르고 공태일 적다
    assert bt.turnover(0.9) > bt.turnover(0.7)
    assert bt.npd(0.9) < bt.npd(0.7)
    assert bt.cycle_days(1.0) == bt.GESTATION + bt.LACTATION + bt.NORMAL_WEI
    e = bt.economics(300, 0.78, 0.85)
    assert e["won_saved_year"] > 0 and e["turnover_after"] > e["turnover_before"]


def test_stall_estrus() -> None:
    """교배사(스톨) 발정 지표: 자세 기반 특징 추출과 점수화."""
    import pandas as pd
    import stall_estrus as se
    # A: 기립 많고 전환 잦음(발정 양상) / B: 계속 누움
    rows = []
    for f in range(40):
        rows.append({"stall_id": "A", "frame_idx": f,
                     "posture": "standing" if f % 3 else "lying"})
        rows.append({"stall_id": "B", "frame_idx": f, "posture": "lying"})
    feat = se.stall_features(pd.DataFrame(rows)).set_index("stall_id")
    assert feat.loc["A", "stand_frac"] > feat.loc["B", "stand_frac"]
    assert feat.loc["A", "transitions"] > feat.loc["B", "transitions"]
    assert feat.loc["B", "lie_frac"] == 1.0
    sc = se.estrus_score(se.stall_features(pd.DataFrame(rows))).set_index("stall_id")
    assert sc.loc["A", "estrus_score"] > sc.loc["B", "estrus_score"]
    # 부동자세: 연속 기립이 길면 immobile_frac 이 잡힌다
    long_stand = [{"stall_id": "C", "frame_idx": f, "posture": "standing"}
                  for f in range(30)]
    fc = se.stall_features(pd.DataFrame(long_stand)).iloc[0]
    assert fc["longest_stand"] == 30 and fc["immobile_frac"] == 1.0
    # 합성 시연이 **완전 분리(AUC 1.0)가 아니어야** 한다(개체차 반영)
    from sklearn.metrics import roc_auc_score
    ts, truth = se.generate_demo(n_stalls=40, seed=0)
    d = se.estrus_score(se.stall_features(ts)).merge(truth, on="stall_id")
    auc = roc_auc_score(d["estrus"], d["estrus_score"])
    assert 0.5 < auc < 0.99, f"합성이 비현실적으로 쉬움(AUC {auc:.3f})"

    # 자세 오류 전파: 상류 정확도가 낮을수록 발정 AUC 가 낮아야 한다.
    # 표본이 작으면 시드 분산에 순서가 뒤집힌다(24개/5회로 재니 실제로 뒤집혔다).
    import numpy as np
    big_ts, big_truth = se.generate_demo(n_stalls=200, frames=120, seed=3)

    def auc_at(acc, seeds=12):
        vals = []
        for s in range(1 if acc >= 1.0 else seeds):
            n = big_ts if acc >= 1.0 else se.degrade(big_ts, acc, seed=s)
            d = se.estrus_score(se.stall_features(n)).merge(big_truth,
                                                           on="stall_id")
            vals.append(roc_auc_score(d["estrus"], d["estrus_score"]))
        return float(np.mean(vals))

    perfect, better, worse = auc_at(1.0), auc_at(0.636), auc_at(0.513)
    assert perfect > better > worse, (
        f"자세 오류가 발정 AUC 에 단조롭게 전파되지 않음 "
        f"({perfect:.3f} / {better:.3f} / {worse:.3f})")
    # degrade 는 실제로 라벨을 바꿔야 한다(무작위성이 죽으면 조용히 통과한다)
    d0 = se.degrade(big_ts, 0.5, seed=1)
    changed = (d0["posture"].to_numpy() != big_ts["posture"].to_numpy()).mean()
    assert 0.2 < changed < 0.6, f"오류 주입 비율이 이상하다({changed:.2f})"
    assert set(d0["posture"]) <= {"standing", "sitting", "lying"}


def test_feeding_monitor() -> None:
    """합사 급이 모니터링: 세션·경쟁·섭취속도(순환논리 회귀 검증)."""
    import numpy as np
    import pandas as pd
    import feeding_monitor as fm
    zones = [(0.0, 0.0, 0.3, 0.3)]
    rows = []
    # A: 급이기에 오래 + 머리 많이 움직임(빨리 먹음)
    # B: 급이기에 오래 + 거의 안 움직임(천천히 먹음)  → 같은 시간, 다른 속도
    rng = np.random.default_rng(0)
    for f in range(300):
        rows.append({"pig_id": "A", "frame_idx": f,
                     "cx": 0.15 + rng.normal(0, 0.010),
                     "cy": 0.15 + rng.normal(0, 0.010)})
        rows.append({"pig_id": "B", "frame_idx": f,
                     "cx": 0.15 + rng.normal(0, 0.001),
                     "cy": 0.15 + rng.normal(0, 0.001)})
        rows.append({"pig_id": "C", "frame_idx": f, "cx": 0.8, "cy": 0.8})
    tracks = pd.DataFrame(rows)
    sess = fm.feeding_sessions(tracks, zones, fps=10.0)
    assert set(sess["pig_id"]) == {"A", "B"}, "급이기 밖 개체가 세션에 포함됨"
    assert "motion" in sess.columns
    met = fm.feeding_metrics(sess, fm.displacements(sess), total_feed_kg=6.0)
    m = met.set_index("pig_id")
    # 저작 강도가 큰 A 가 더 빨리 먹은 것으로 추정돼야 한다
    assert m.loc["A", "chew_intensity"] > m.loc["B", "chew_intensity"]
    assert m.loc["A", "eat_rate_g_per_min"] > m.loc["B", "eat_rate_g_per_min"]
    # 순환논리 회귀: 점유시간이 같은데 속도가 같아지면 안 된다
    assert abs(m.loc["A", "eat_rate_g_per_min"] - m.loc["B", "eat_rate_g_per_min"]) > 1
    d = fm.flag_risk(met)
    assert "feed_adequacy" in d.columns and "status" in d.columns
    assert fm.zone_of(0.15, 0.15, zones) == 0 and fm.zone_of(0.9, 0.9, zones) is None


def test_repro_calendar() -> None:
    """작업 캘린더: 날짜 1개 → 전체 일정, 관측이 예상을 대체, 그룹 일괄 생성."""
    from datetime import date, datetime
    import repro_calendar as rc
    tasks = rc.schedule_from_weaning("2026-08-10", parity="sow")
    kinds = [t["task"] for t in tasks]
    for need in ("이유", "발정 관찰", "교배", "재발정 확인", "임신감정",
                 "분만사 이동", "분만"):
        assert need in kinds, f"{need} 작업이 생성되지 않음"
    assert tasks == sorted(tasks, key=lambda t: t["date"]), "날짜순이 아님"

    # 순서 회귀: '발정 관찰'이 '교배'보다 뒤에 오면 안 된다
    first_obs = min(t["date"] for t in tasks if t["task"] == "발정 관찰")
    first_ai = min(t["date"] for t in tasks if t["task"] == "교배")
    assert first_obs < first_ai, "발정 관찰이 교배 뒤에 배치됨"

    s = rc.cycle_summary(tasks)
    assert 140 <= s["cycle_days"] <= 160, f"1주기 {s['cycle_days']}일 (150 근처여야)"
    assert s["npd_days"] == s["cycle_days"] - rc.GESTATION - rc.LACTATION

    # 후보돈은 이유가 없다 — 경산돈 경로로 넣으면 거부해야 한다
    try:
        rc.schedule_from_weaning("2026-08-10", parity="gilt")
        raise AssertionError("후보돈에 이유 기준 일정이 허용됨")
    except ValueError:
        pass
    g = rc.schedule_from_estrus("2026-08-10", parity="gilt")
    assert "이유" not in [t["task"] for t in g][:2]
    assert min(t["date"] for t in g if t["task"] == "교배") >= date(2026, 8, 10)

    # 관측이 예상을 대체한다: 확정 교배는 estimated=False
    conf = rc.schedule_from_weaning("2026-08-10", "sow",
                                    estrus_confirmed=datetime(2026, 8, 14, 6))
    ai = [t for t in conf if t["task"] == "교배"]
    assert ai and all(not t["estimated"] for t in ai), "확정 발정인데 교배가 추정으로 남음"
    est = [t for t in tasks if t["task"] == "교배"]
    assert all(t["estimated"] for t in est), "미확인인데 교배가 확정으로 표시됨"
    assert ai[0]["date"] != est[0]["date"], "발정 확인이 교배일에 반영되지 않음"

    # 그룹 등록: 입력 1회 → N두, 개별 확인은 해당 개체만 갱신
    grp = rc.group_from_weaning(["A", "B", "C"], "2026-08-10")
    assert len(grp) == 3 and all(len(v) == len(tasks) for v in grp.values())
    grp2 = rc.confirm_estrus(grp, "B", datetime(2026, 8, 14, 6))
    ai_b = [t["date"] for t in grp2["B"] if t["task"] == "교배"]
    ai_a = [t["date"] for t in grp2["A"] if t["task"] == "교배"]
    assert ai_b != ai_a, "개체 확인이 반영되지 않음"
    assert grp2["A"] == grp["A"], "다른 개체 일정까지 바뀜"

    todo = rc.due_today(grp, today="2026-08-16", horizon=1)
    assert todo and all(0 <= t["d_day"] <= 1 for t in todo)
    assert todo == sorted(todo, key=lambda t: (t["d_day"], -t["priority"]))
    late = rc.overdue(grp, today="2026-09-30")
    assert late and all(t["late_days"] > 0 for t in late)


def test_farm_registry() -> None:
    """축사 등록·배치 규칙·관리표·분석 경로."""
    import farm_registry as fr
    f = fr.Farm("t")
    f.add_barn("1동", "교배사").add_pen("1동", "A열", "stall", 3)
    f.add_barn("2동", "임신사").add_pen("2동", "1방", "group", 2)

    # 미등록 축사/돈방, 잘못된 용도·방식은 거부
    for bad in (lambda: f.add_barn("9동", "없는용도"),
                lambda: f.add_pen("9동", "x", "stall", 2),
                lambda: f.add_pen("1동", "y", "없는방식", 2),
                lambda: f.add_pen("1동", "z", "stall", 0),
                lambda: f.place("A", "1동", "없는방")):
        try:
            bad()
            raise AssertionError("잘못된 등록이 허용됨")
        except (KeyError, ValueError):
            pass

    # 스톨은 자리 번호 필수 — 없으면 카메라 화면과 대조할 수 없다
    try:
        f.place("A", "1동", "A열")
        raise AssertionError("스톨에 자리 없이 배치가 허용됨")
    except ValueError:
        pass

    f.place("A", "1동", "A열", 1).place("B", "1동", "A열", 2)
    assert f.locate("A") == ("1동", "A열", "1")
    assert f.at("1동", "A열") == ["A", "B"]
    assert "1동" in f.label("A") and "1번" in f.label("A")
    assert f.label("없는개체") == "미배치"

    # 같은 자리 이중 배치 금지
    try:
        f.place("C", "1동", "A열", 1)
        raise AssertionError("이미 찬 자리에 배치가 허용됨")
    except ValueError:
        pass
    # 수용능력 초과 금지
    f.place("C", "1동", "A열", 3)
    try:
        f.place("D", "1동", "A열", 4)
        raise AssertionError("수용능력 초과 배치가 허용됨")
    except ValueError:
        pass

    # 이동하면 옛 자리는 비어야 한다(같은 개체가 두 곳에 잡히면 두수가 틀어진다)
    f.place("A", "2동", "1방")
    assert f.locate("A")[0] == "2동"
    assert "A" not in f.at("1동", "A열")
    assert len(f.table()) == 3

    # 자리 번호 자연 정렬(1,10,2 가 아니라 1,2,10)
    g = fr.Farm("s")
    g.add_barn("1동", "교배사").add_pen("1동", "A열", "stall", 12)
    for s in (10, 2, 1):
        g.place(f"P{s}", "1동", "A열", s)
    assert list(g.table()["slot"]) == ["1", "2", "10"]

    occ = f.occupancy().set_index(["barn", "pen"])
    assert occ.loc[("1동", "A열"), "n"] == 2 and occ.loc[("1동", "A열"), "free"] == 1

    # 등록이 분석 경로를 정한다: 스톨/군사는 다른 모듈, 분만틀은 대상 외
    route = f.analysis_route().set_index(["barn", "pen"])
    assert route.loc[("1동", "A열"), "module"] == "stall_estrus"
    assert "motion_tracker" in route.loc[("2동", "1방"), "module"]
    f.add_barn("3동", "분만사").add_pen("3동", "분만실", "crate", 2)
    route = f.analysis_route().set_index(["barn", "pen"])
    assert not bool(route.loc[("3동", "분만실"), "estrus_target"]), \
        "분만사에 발정 판정을 돌리려 함"

    f.remove("A")
    assert f.locate("A") is None and len(f.table()) == 2

    # 번식 상태 결합 + 배치 오류 검출
    import herd_board as hb
    demo = fr.demo_farm()
    ids = sorted(demo._where)
    recs = hb.generate_demo(n=len(ids) + 40, today="2026-08-10")[:len(ids)]
    for r, i in zip(recs, ids):
        r["id"] = i
    herd = hb.build_herd(recs, today="2026-08-10")
    t = demo.table(herd)
    assert len(t) == len(ids) and "stage_h" in t.columns
    assert t["id"].nunique() == len(ids), "관리표에 개체 중복"
    mp = demo.misplaced(herd)
    assert len(mp) and {"id", "loc", "reason"} <= set(mp.columns)
    # 분만사의 포유돈은 정상 — 오류로 잡히면 안 된다
    ok = t[(t["stage"] == "분만사") & (t["stage_h"] == "포유")]["id"]
    assert not set(ok) & set(mp["id"]), "정상 배치가 오류로 잡힘"


def test_barn_queue() -> None:
    """작업동별 조치 큐: 단일 판정·동 순서·준비물."""
    import breeding_ledger as bl
    import build_barn_map as bm
    today = "2026-08-10"
    farm, herd, scheds, scores = bl.build_demo(today)
    led = bl.ledger(farm, herd, scheds, scores, today=today)

    # 판정은 한 곳에만 — 도면과 큐가 같은 수를 세야 한다(23 vs 68 회귀)
    assert bm.cell_status is bl.action_status
    n_map = sum(1 for r in led.to_dict("records") if bl.is_actionable(r))
    q = bl.barn_queue(led)
    assert sum(g["n"] for g in q) == n_map, "큐 합계가 도면 조치 대상과 불일치"
    assert n_map < len(led), "전 개체가 조치 대상"

    # 동은 겹치지 않고, 동 안은 긴급도 내림차순
    barns = [g["barn"] for g in q]
    assert len(barns) == len(set(barns))
    for g in q:
        u = [r["urgency"] for r in g["rows"]]
        assert u == sorted(u, reverse=True), f"{g['barn']} 동 내부 정렬 깨짐"
        assert g["n"] == len(g["rows"])
    # 가장 급한 개체가 있는 동이 먼저
    tops = [g["top_urgency"] for g in q]
    assert tops == sorted(tops, reverse=True)
    assert [g["visit_order"] for g in q] == list(range(1, len(q) + 1))

    # 준비물: 발정 관찰과 재발정 확인은 둘 다 웅돈 — 한 줄로 합쳐야 한다
    assert bl.SUPPLIES["발정 관찰"] == bl.SUPPLIES["재발정 확인"] == "웅돈"
    for g in q:
        tasks = [r["next_task"] for r in g["rows"]]
        want = sum(1 for t in tasks if bl.SUPPLIES.get(t) == "웅돈")
        assert g["supplies"].get("웅돈", 0) == want, f"{g['barn']} 웅돈 수 불일치"

    # 동선 순서: 등록 순서를 따른다
    route = list(farm.barns)
    rq = bl.barn_queue(led, order="route", route=route)
    seen = [g["barn"] for g in rq]
    assert seen == [b for b in route if b in seen], "동선 순서가 지켜지지 않음"


def test_work_log() -> None:
    """작업 로그: 추가전용·취소 반영·큐 정정·적기 준수."""
    import tempfile
    import breeding_ledger as bl
    import work_log as wl
    today = "2026-08-10"
    farm, herd, scheds, scores = bl.build_demo(today)
    led = bl.ledger(farm, herd, scheds, scores, today=today)

    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.csv")
        assert len(wl.load(path)) == 0
        wl.record("A", "교배", "2026-08-10", operator="김", path=path,
                  planned_date="2026-08-09")
        wl.record("B", "임신감정", "2026-08-10", path=path)
        lg = wl.load(path)
        assert len(lg) == 2 and list(lg.columns) == wl.COLS
        assert wl.done_keys(lg) == {("A", "교배"), ("B", "임신감정")}
        # 취소를 덧붙이면 완료가 무효가 된다(기록은 지우지 않는다)
        wl.record("A", "교배", "2026-08-10", result="취소", path=path)
        lg2 = wl.load(path)
        assert len(lg2) == 3, "취소가 기존 행을 덮어썼다 — 추가전용이 깨짐"
        assert ("A", "교배") not in wl.done_keys(lg2)
        try:
            wl.record("C", "교배", today, result="없는결과", path=path)
            raise AssertionError("잘못된 result 가 허용됨")
        except ValueError:
            pass

    # 합성 로그로 큐 정정
    log = wl.generate_demo(scheds, today=today)
    assert len(log) and set(log["result"]) <= set(wl.RESULTS)
    before = sum(1 for r in led.to_dict("records") if bl.is_actionable(r))
    led2 = wl.apply_to_ledger(led, log)
    after = sum(1 for r in led2.to_dict("records") if bl.is_actionable(r))
    assert "done" in led2.columns
    assert after <= before, "로그를 반영했는데 조치 대상이 늘었다"
    if int(led2["done"].sum()):
        assert after < before, "완료 기록이 있는데 큐가 줄지 않았다"
    # done 은 반드시 큐에서 빠져야 한다(긴급도만 0 으로 내리면 안 빠졌다)
    assert not any(bl.is_actionable(r) for r in led2.to_dict("records")
                   if r["done"])

    c = wl.compliance(log)
    assert len(c) and (c["on_time_rate"].between(0, 1)).all()
    assert (c["on_time"] + c["late"] + c["early"] <= c["n"]).all()
    # 교배는 허용 폭이 가장 좁아야 한다
    assert wl.ON_TIME["교배"] < wl.ON_TIME["임신감정"]

    s = wl.summary(log, days=14, today=today)
    assert s["n"] >= 0 and len(s["daily"]) == 14
    assert sum(x["n"] for x in s["daily"]) == s["n"]
    assert len(wl.summary(wl.load("/nonexistent.csv"))) == 1  # {"n":0}


def test_pregnancy_check() -> None:
    """임신진단 3단계: 캐스케이드 보존·조기검출 이득·초음파 의존성."""
    import pregnancy_check as pc
    shares = sum(c[4] for c in pc.CHECKPOINTS)
    assert abs(shares - 1.0) < 1e-9, f"재발 비율 합이 {shares} (1.0 이어야)"
    # 1차 관문은 초음파가 아니라 발정체크 — 이 프로젝트의 근거
    assert pc.CHECKPOINTS[0][5] == "재발정 확인" and pc.CHECKPOINTS[0][4] == 0.80

    rows = pc.detection_cascade()
    total = sum(r["caught"] for r in rows) + rows[-1]["missed_forward"]
    assert abs(total - 1.0) < 1e-6, f"캐스케이드 총합 {total} — 재발돈이 사라졌다"
    assert (rows[0]["npd_if_caught"] < rows[1]["npd_if_caught"]
            < rows[2]["npd_if_caught"]), "늦게 잡을수록 공태일이 길어야 한다"

    # 민감도가 높을수록 기대 공태일이 짧다
    good = pc.npd_from_returns(pc.CCTV_SENSITIVITY)
    poor = pc.npd_from_returns(pc.DEFAULT_SENSITIVITY)
    assert good < poor, "3주 검출을 개선했는데 공태일이 줄지 않음"
    assert 18 <= good <= 114

    v = pc.value_of_early(300)
    assert v["won_saved_year"] > 0 and v["npd_saved_per_return"] > 0
    # 초음파가 부실할수록 3주 개선의 가치가 커진다(과장 방지용 회귀)
    strict = pc.value_of_early(300,
                               base_sens={"3주": .70, "5주": .95, "8~10주": .90},
                               improved_sens={"3주": .92, "5주": .95, "8~10주": .90})
    none_us = pc.value_of_early(300,
                                base_sens={"3주": .70, "5주": .0, "8~10주": .90},
                                improved_sens={"3주": .92, "5주": .0, "8~10주": .90})
    assert none_us["won_saved_year"] > strict["won_saved_year"], \
        "초음파 유무와 무관하게 같은 이득이 나옴 — 캐스케이드가 작동하지 않는다"

    tasks = pc.checkpoint_tasks("2026-08-16")
    assert len(tasks) == 3
    assert [t["date"] for t in tasks] == sorted(t["date"] for t in tasks)
    assert tasks[0]["priority"] > tasks[1]["priority"], \
        "80% 를 잡는 관문이 더 급해야 한다"

    # 캘린더에 3단계가 실제로 반영됐는지
    import repro_calendar as rc
    sched = rc.schedule_from_service("2026-08-16")
    cps = [t for t in sched if t["task"] in ("재발정 확인", "임신감정")]
    assert len(cps) == 3, f"캘린더에 체크포인트가 {len(cps)}개"


def test_herd_board() -> None:
    """모돈군 현황판: 단계 판정·주차 파이프라인·산차 구성·도태·전입 계획."""
    from datetime import date, timedelta
    import herd_board as hb
    herd = hb.build_herd(hb.generate_demo(n=200, today="2026-08-10"),
                         today="2026-08-10")
    assert len(herd) == 200
    sc = hb.stage_counts(herd)
    assert sum(sc.values()) == 200
    # 단계 판정 회귀: 이유까지 끝난 모돈이 '임신'으로 남으면 공태가 0이 된다
    assert sc["공태"] > 0, "공태돈이 한 두도 없다 — 최근 사건 판정이 깨졌다"
    assert sc["임신"] > 0 and sc["포유"] > 0

    t0 = date(2026, 8, 10)
    one = hb.build_herd([{"id": "X", "parity": 3,
                          "service_date": t0 - timedelta(days=160),
                          "farrow_date": t0 - timedelta(days=45),
                          "weaning_date": t0 - timedelta(days=17)}], today=t0)
    assert one.loc[0, "stage"] == "공태" and one.loc[0, "npd"] == 17

    wb = hb.weekly_board(herd, today="2026-08-10")
    assert len(wb) == 17 and (wb["farrow"] >= 0).all()
    # 확정 판정 회귀: 주 '끝'을 역산해야 한다. 마지막 주는 아직 교배로 메울 수 있다
    assert not bool(wb.iloc[-1]["locked"]), "메울 수 있는 주가 확정 손실로 잡힘"
    assert bool(wb.iloc[0]["locked"])

    pp = hb.parity_profile(herd)
    assert abs(pp["target_share"].sum() - 1.0) < 1e-9, "목표 산차 구성 합이 1이 아님"
    assert pp["n"].sum() == int((herd["parity"] > 0).sum()), "산차 집계 누락/중복"

    cc = hb.cull_candidates(herd)
    assert len(cc) and (cc["score"].diff().dropna() <= 0).all(), "점수 내림차순 아님"
    assert cc["reason"].str.len().gt(0).all()

    gi = hb.gilt_intake_plan(herd, months=6, today="2026-08-10")
    a = gi.attrs
    # 용량 상한 회귀: 적체가 아무리 커도 월 전입이 상한을 넘으면 안 된다
    assert (gi["need"] <= a["monthly_cap"] + 1).all(), "월 전입이 격리사 용량 초과"
    assert (gi["backlog_left"].diff().dropna() <= 0).all(), "적체가 늘어남"
    assert a["months_to_clear"] is None or a["months_to_clear"] >= 1

    st = hb.service_target(herd, today="2026-08-10")
    assert st["service_target_week"] > st["farrow_target_week"], \
        "수태 실패분을 감안하면 교배 목표가 분만 목표보다 커야 한다"


def test_breeding_ledger() -> None:
    """통합 관리표: 완료 추론·조치 가능 지연·모순 검출·향후 일정·작업량."""
    from datetime import date, timedelta
    import breeding_ledger as bl
    today = "2026-08-10"
    farm, herd, scheds, scores = bl.build_demo(today)
    led = bl.ledger(farm, herd, scheds, scores, today=today)
    assert len(led) == len(farm.table()), "관리표 행 수가 배치 두수와 다름"
    assert led["id"].nunique() == len(led), "개체 중복"
    for c in ("loc", "stage", "estrus", "pregnancy", "next_task", "d_day",
              "action", "conflict", "urgency"):
        assert c in led.columns, f"{c} 열 없음"

    # 완료 추론 회귀: 분만한 모돈에게 '교배 142일 경과' 를 띄우면 안 된다
    assert (led["overdue_days"] <= bl.OVERDUE_HORIZON).all(), \
        "조치 불가능한 과거 작업이 지연 큐에 남아 있다"
    lact = led[led["stage"] == "포유"]
    assert not (lact["overdue"] == "교배").any(), \
        "이미 분만한 모돈이 교배 미실시로 잡힘"

    # 후보돈에게 '이유' 작업이 생기면 안 된다
    gilts = set(led[led["stage"] == "후보"]["id"])
    for g in gilts:
        assert not any(t["task"] == "이유" and t["date"] <= rc_date(today)
                       for t in scheds[g]), f"{g}: 후보돈에 이유 작업"

    # 시한작업 우선: 오늘 교배해야 할 개체가 단순 지연 건보다 위에 있어야 한다
    ai_today = led[(led["next_task"] == "교배") & (led["d_day"] == 0)]
    if len(ai_today):
        routine = led[(led["next_task"] == "임신감정") & (led["d_day"] > 5)]
        if len(routine):
            assert ai_today["urgency"].max() > routine["urgency"].max(), \
                "오늘 교배가 여유 있는 임신감정보다 아래로 밀림"

    # 모순: 임신 중 발정 신호는 별도로 남아야 한다(곱해서 뭉개지 않는다)
    cf = bl.conflicts(led)
    hot_preg = led[(led["estrus_score"] >= bl.ESTRUS_HI)
                   & (led["stage"].isin(("임신", "포유")))]
    assert len(cf) == len(hot_preg), "임신 중 발정 신호가 누락됨"
    if len(cf):
        assert cf["conflict"].str.len().gt(0).all()

    up = bl.upcoming(scheds, today=today, days=14, farm=farm)
    assert len(up) and (up["d_day"].between(0, 14)).all()
    assert up["d_day"].is_monotonic_increasing
    assert up["loc"].str.len().gt(0).all(), "향후 일정에 위치가 비었다"

    wl = bl.workload(scheds, today=today, days=14)
    assert "합계" in wl.columns and len(wl)
    task_cols = [c for c in wl.columns if c not in ("date", "합계")]
    # 표가 전부 0 으로 찍히던 회귀(공백 든 한글 컬럼명 접근 실패)
    assert wl[task_cols].to_numpy().sum() > 0, "작업량 표가 비었다"
    assert (wl[task_cols].sum(axis=1) == wl["합계"]).all(), "합계 불일치"
    assert wl["합계"].sum() == len(up), "작업량 총합이 향후 일정 건수와 다름"


def test_posture_crop_feats() -> None:
    """크롭 외형 피처: 차원·결정성·자세 구분력 + 파일명 회귀."""
    import numpy as np
    import posture_crop_feats as pcf
    rng = np.random.default_rng(0)

    # 가로로 긴 밝은 띠(옆으로 누운 몸통) vs 세로로 긴 띠 — 방향 피처가 달라야 한다
    horiz = np.full((pcf.SZ, pcf.SZ), 40, dtype=np.uint8)
    horiz[20:28, 6:42] = 200
    vert = np.full((pcf.SZ, pcf.SZ), 40, dtype=np.uint8)
    vert[6:42, 20:28] = 200
    fh, fv = pcf._crop_feats(horiz), pcf._crop_feats(vert)
    assert fh.shape == (len(pcf.CROP_COLS),) == fv.shape
    assert np.isfinite(fh).all() and np.isfinite(fv).all()
    i_cos = pcf.CROP_COLS.index("sil_cos2t")
    assert abs(fh[i_cos] - fv[i_cos]) > 0.5, "가로/세로 실루엣이 구분되지 않음"
    i_el = pcf.CROP_COLS.index("sil_elong")
    assert fh[i_el] > 1.5 and fv[i_el] > 1.5, "긴 띠인데 장단축비가 1 근처"

    # 결정적이어야 한다(같은 입력 → 같은 출력)
    assert np.allclose(fh, pcf._crop_feats(horiz))
    # 균일 크롭은 그래디언트가 없다
    flat = pcf._crop_feats(np.full((pcf.SZ, pcf.SZ), 128, dtype=np.uint8))
    assert flat[pcf.CROP_COLS.index("edge_den")] == 0.0

    # 파일명 회귀: image_id 에 이미 확장자가 있는데 .jpg 를 덧붙여 전량 누락됐었다.
    # 절반 이상 실패하면 0 행렬을 조용히 캐시하지 말고 터져야 한다.
    import pandas as pd
    bad = pd.DataFrame([{"image_id": "없는파일.jpg", "x": 0, "y": 0,
                         "w": 10, "h": 10}])
    try:
        pcf.extract(bad, {"d": "/nonexistent"}, verbose=False)
        raise AssertionError("전량 누락인데 예외가 나지 않음")
    except RuntimeError:
        pass


def test_posture_crossview() -> None:
    """교차-뷰 프로토콜: 뷰 정규화의 무누수성·3클래스 매핑·상한 계산."""
    import numpy as np
    import posture_crossview as pcv
    import posture_features as pf

    # 5클래스 → 발정 3클래스 매핑이 stall_estrus 어휘와 맞아야 한다
    import stall_estrus as se
    for v in set(pcv.TO_ESTRUS.values()):
        assert se._canon(v) == v, f"{v} 가 stall_estrus 어휘와 불일치"
    assert pcv.TO_ESTRUS["Lateral_lying_left"] == \
        pcv.TO_ESTRUS["Lateral_lying_right"] == "lying"

    # 좌우 횡와를 못 가른다는 가정의 상한: 1 - 비중/2
    import pandas as pd
    df = pd.DataFrame({"cls": ["Lateral_lying_left"] * 2
                       + ["Lateral_lying_right"] * 2 + ["Standing"] * 6})
    c = pcv.ceiling_from_lr(df)
    assert abs(c["lr_share"] - 0.4) < 1e-9 and abs(c["ceiling"] - 0.8) < 1e-9

    # 뷰 정규화는 뷰 단위로 독립이어야 한다 — 한 뷰를 바꿔도 다른 뷰 결과는 그대로
    F = np.array([[1.0, 5.0], [3.0, 7.0], [10.0, 1.0], [20.0, 3.0]])
    v = np.array(["a", "a", "b", "b"])
    n1 = pcv.view_normalize(F, v)
    F2 = F.copy(); F2[2:] *= 100.0
    n2 = pcv.view_normalize(F2, v)
    assert np.allclose(n1[:2], n2[:2]), "다른 뷰의 값이 결과에 새어 들어감"
    for grp in ("a", "b"):
        blk = n1[v == grp]
        assert abs(blk.mean()) < 1e-9, "뷰 내 평균이 0 이 아님"
    # 상수 열에서 0 나눗셈이 나면 안 된다
    assert np.isfinite(pcv.view_normalize(np.ones((4, 2)), v)).all()


def test_posture_report() -> None:
    """자세 병목 리포트: SVG 렌더러 + 자체완결 HTML(캐시 있을 때만 전체 생성)."""
    import os
    import numpy as np
    import build_posture_report as bpr
    import posture_crossview as pcv

    # 혼동행렬 렌더러: 행 정규화라 각 행의 표시값 합이 1 이어야 한다
    labels = ["Standing", "Sternal_lying"]
    svg = bpr.confusion_svg(labels, [[3, 1], [2, 2]], 300)
    assert svg.startswith("<svg") and "0.75" in svg and "0.50" in svg
    # 합이 0 인 행이 있어도 0 나눗셈으로 죽지 않아야 한다
    assert bpr.confusion_svg(labels, [[0, 0], [1, 1]], 300).startswith("<svg")

    bars = bpr.grouped_bars([("a", {"acc_w": 0.5, "mf1_w": 0.2}, False),
                             ("b", {"acc_w": 0.7, "mf1_w": 0.4}, True)],
                            width=400, ref=0.45)
    assert bars.startswith("<svg") and "0.700" in bars
    # 값이 전부 0 이어도 죽지 않아야 한다(mx=0 나눗셈)
    assert bpr.grouped_bars([("z", {"acc_w": 0.0, "mf1_w": 0.0}, False)],
                            width=300).startswith("<svg")

    folds = [{"view": "v1", "n_test": 100, "acc": 0.7, "mf1": 0.5},
             {"view": "v2", "n_test": 50, "acc": 0.4, "mf1": 0.3}]
    assert bpr.fold_svg(folds, 400).startswith("<svg")

    # 전체 생성은 결과 캐시가 있을 때만(케글 데이터 없는 환경 배려)
    if not os.path.exists(pcv.RESULTS):
        return
    assert bpr.main() == 0
    page = open(bpr.OUT, encoding="utf-8").read()
    assert page.startswith("<!DOCTYPE html>") and page.rstrip().endswith("</html>")
    assert os.path.getsize(bpr.OUT) > 8000
    for bad in ("http://", "https://", "<script src", "cdn."):
        assert bad not in page, f"외부 참조 {bad}"
    assert "prefers-color-scheme" in page
    # 폐기한 누수 수치를 성과처럼 다시 싣지 않았는지
    assert "0.642" in page and "폐기" in page, "0.642 폐기 사실이 빠졌다"

    r = pcv.run_all()
    for k in ("baseline", "configs", "pen", "ceiling", "confusion_geom"):
        assert k in r, f"{k} 없음"
    cm = np.array(r["confusion_geom"]["matrix"])
    assert cm.sum() > 0 and cm.shape[0] == cm.shape[1] == len(r["classes"])
    # 좌/우 횡와가 실제로 갈리는지(동전던지기 주장의 근거)
    labs = r["confusion_geom"]["labels"]
    li, ri = labs.index("Lateral_lying_left"), labs.index("Lateral_lying_right")
    assert cm[li][ri] > 0 and cm[ri][li] > 0, "좌우 혼동이 없다 — 주장과 불일치"


def test_barn_environment() -> None:
    """THI 계산·구간 판정·착상기 위험군 교차."""
    import barn_environment as be
    import farm_registry as fr
    import herd_board as hb
    # 같은 온도라도 습도가 높으면 THI 가 높다(온도만으로 판정하면 안 되는 이유)
    assert be.thi(30, 80) > be.thi(30, 40)
    assert be.thi(20, 60) < be.thi(30, 60)
    assert be.band(90)[0] == "중증" and be.band(60)[0] == "적정"
    assert be.band(80)[0] == "중등도" and be.band(76)[0] == "경증"

    env = be.assess({"A": (30.0, 80.0), "B": (18.0, 55.0)})
    a = env.set_index("barn")
    assert bool(a.loc["A", "heat_stress"]) and not bool(a.loc["B", "heat_stress"])
    assert a.loc["A", "wei_penalty_d"] > a.loc["B", "wei_penalty_d"]
    assert (env["thi"] > 0).all()

    farm = fr.demo_farm()
    ids = sorted(farm._where)
    recs = hb.generate_demo(n=len(ids) + 40, today="2026-08-10")[:len(ids)]
    for r, i in zip(recs, ids):
        r["id"] = i
    herd = hb.build_herd(recs, today="2026-08-10")
    hot = be.assess(be.demo_readings(hot_summer=True))
    risk = be.at_risk_services(herd, hot, farm)
    lo, hi = be.IMPLANTATION_WINDOW
    if len(risk):
        # 일 단위여야 한다(주차로 재면 7일 단위로 뭉개져 경계가 흐려진다)
        assert risk["days_since_service"].between(lo, hi).all()
        assert (risk["days_since_service"] % 7 != 0).any(), "주 단위로 뭉개졌다"
    # 서늘하면 위험군이 없어야 한다
    cool = be.assess(be.demo_readings(hot_summer=False))
    assert not len(be.at_risk_services(herd, cool, farm))


def test_dashboard_builders() -> None:
    """새 웹 뷰 2종이 자체완결 HTML 로 생성되는지 + 상태 판정 회귀."""
    import os
    import build_barn_map as bm
    import build_breeding_console as bc
    import breeding_ledger as bl

    today = "2026-08-10"
    farm, herd, scheds, scores = bl.build_demo(today)
    led = bl.ledger(farm, herd, scheds, scores, today=today)

    # 결측 판정 회귀: pandas 를 거친 None 은 float NaN 이 되고 bool(nan) 은 True.
    # 그대로 두면 전 개체가 '경보'로 칠해진다(실제로 68/68 이 그랬다).
    assert not bm._present(float("nan")) and not bm._present(None)
    assert bm._present("x") and bm._present(0)
    pairs = [bm.cell_status(r) for r in led.to_dict("records")]
    kinds = {s for s, _ in pairs}
    assert "정상" in kinds, "조치 없음 개체가 하나도 없다 — 결측 판정이 깨졌다"
    n_alert = sum(1 for s, _ in pairs if s == "경보")
    assert n_alert == len(bl.conflicts(led)), "도면 경보 수가 모순 목록과 불일치"
    assert n_alert < len(led), "전 개체가 경보"

    # 지연은 색이 아니라 테두리 — 오늘 교배할 개체가 지연 색으로 덮이면 안 된다
    ai_today = [r for r in led.to_dict("records")
                if r["next_task"] == "교배" and r["d_day"] == 0
                and (r["overdue_days"] or 0) > 0]
    for r in ai_today:
        st, late = bm.cell_status(r)
        assert st == "교배" and late, "지연이 임박한 교배를 덮어씀"
    assert "지연" not in bm.STATUS, "지연이 색 범례에 남아 있다"

    layout = bm.build_layout(farm, led)
    total = sum(len(p["cells"]) for b in layout.values() for p in b["pens"])
    assert total == len(farm.table()), "도면 칸 수가 배치 두수와 다름"

    # 앱 사용 화면: 숫자가 다른 뷰와 어긋나면 "지어낸 값 없음" 전제가 깨진다
    import build_app_screens as bas
    assert bas.main() == 0
    app = open(bas.OUT, encoding="utf-8").read()
    n_act = sum(1 for s, late in pairs if s not in ("정상", "공실") or late)
    assert f'<b>{n_act}</b><span>조치 대상</span>' in app, \
        f"앱 화면의 조치 대상 수가 도면과 불일치(도면 {n_act})"
    assert f'<b>{len(bl.conflicts(led))}</b><span>경보</span>' in app

    # 교배기록 화면의 날짜는 그 개체의 실제 일정에서 나와야 한다
    import repro_calendar as rc2
    sid, wean, _sc = bas.pick_service_case(herd, scores)
    est = rc2.schedule_from_weaning(wean)
    est_ai = [t for t in est if t["task"] == "교배"][0]
    assert f'{est_ai["date"]:%Y-%m-%d}' in app, "예정일이 실제 일정과 다름"
    assert f'{wean:%Y-%m-%d}' in app, "이유일이 화면에 없음"

    # 동작 프로토타입: 심는 데이터가 유효한 JSON 이고 다른 뷰와 값이 맞는지
    import json
    import build_app_prototype as bap
    P = bap.build_payload()
    for k in ("animals", "sched", "barns", "board", "kpi", "ai",
              "statusColors", "stageColors"):
        assert k in P, f"payload 에 {k} 없음"
    assert len(P["animals"]) == len(led)
    assert P["kpi"]["nAct"] == n_act, "프로토타입 조치 대상 수가 도면과 불일치"
    assert P["kpi"]["nConf"] == len(bl.conflicts(led))
    # NaN 이 새면 JS 에서 truthy 로 잘못 동작한다 — allow_nan=False 로 잡는다
    json.dumps(P, allow_nan=False)
    assert all(a["conflict"] is None or isinstance(a["conflict"], str)
               for a in P["animals"]), "conflict 에 NaN 이 남았다"
    ids = {a["id"] for a in P["animals"]}
    assert all(s["id"] in ids for b in P["barns"] for p in b["pens"]
               for s in p["slots"]), "도면 칸이 없는 개체를 가리킨다"
    assert set(P["sched"]) >= ids, "일정이 없는 개체가 있다"
    assert bap.main() == 0
    proto = open(bap.OUT, encoding="utf-8").read()
    for bad in ("http://", "https://", "<script src", "cdn."):
        assert bad not in proto, f"프로토타입에 외부 참조 {bad}"
    assert "prefers-color-scheme" in proto

    for mod in (bc, bm, bas):
        assert mod.main() == 0
        assert os.path.exists(mod.OUT) and os.path.getsize(mod.OUT) > 8000
        page = open(mod.OUT, encoding="utf-8").read()
        assert page.startswith("<!DOCTYPE html>") and page.rstrip().endswith("</html>")
        # 자체완결: 외부 리소스를 부르면 안 된다
        for bad in ("http://", "https://", "<script src", "cdn."):
            assert bad not in page, f"{os.path.basename(mod.OUT)} 에 외부 참조 {bad}"
        assert 'prefers-color-scheme' in page, "다크 모드 대응 없음"


def rc_date(x):
    import repro_calendar as rc
    return rc._d(x)


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
             test_estrus_calendar_link, test_estrus_contrast_eval,
             test_keypoints_parser_pose, test_pose_vs_behavior_eval,
             test_motion_tracker, test_box_merge, test_temporal_features,
             test_breeding_timing, test_stall_estrus, test_feeding_monitor,
             test_repro_calendar, test_pregnancy_check, test_herd_board,
             test_barn_queue, test_work_log,
             test_farm_registry, test_breeding_ledger, test_barn_environment,
             test_posture_crop_feats, test_posture_crossview, test_posture_report,
             test_dashboard_builders]
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
