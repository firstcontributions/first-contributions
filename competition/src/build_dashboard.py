"""대시보드 데이터 생성 → competition/dashboard/index.html.

통합 파이프라인(CCTV 발정관찰 + 관리요인 → 무발정 위험/처방)과 시간 윈도우
발정 시작점 탐지 결과를 하나의 JSON 으로 만들어 템플릿에 주입한다.

    python competition/src/build_dashboard.py                       # 합성 시연
    python competition/src/build_dashboard.py <cctv_dir> <mgmt.csv> # 실데이터
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import estrus_onset  # noqa: E402
import model_gilt_anestrus as anestrus  # noqa: E402
import parse_aihub  # noqa: E402
import pipeline_gilt  # noqa: E402
import train as train_mod  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
OUT_HTML = os.path.join(ROOT, "competition", "dashboard", "index.html")
TEMPLATE = os.path.join(ROOT, "competition", "dashboard", "template.html")

FEATURE_KO = {
    "feed_adequacy": "사료 적정도", "water_adequacy": "음수 적정도",
    "facility_score": "시설 점수", "boar_exposure_min": "웅돈 접촉(분)",
    "nh3_ppm": "암모니아(ppm)", "temp_c": "기온(℃)", "humidity_pct": "습도(%)",
    "growth_disease_cnt": "성장기 질병력", "age_over_target": "초교배일령 경과",
    "backfat_mm": "등지방(mm)", "weight_kg": "체중(kg)",
    "activity_mean": "평균 활동량", "activity_std": "활동량 변동",
    "activity_max": "최대 활동량", "aspect_mean": "평균 종횡비",
    "bbox_area_mean": "평균 면적", "kp_spread_mean": "keypoint 산포",
    "n_frames": "관찰 프레임수",
}
for b in ("standing", "lying", "eating", "head_shaking", "tailing", "sitting"):
    FEATURE_KO[f"frac_{b}"] = f"행동:{b}"


def risk_band(p: float) -> str:
    return ("good" if p < 0.3 else "warning" if p < 0.5
            else "serious" if p < 0.7 else "critical")


def build_data(frames: pd.DataFrame, mgmt: pd.DataFrame) -> dict:
    signals = pipeline_gilt.build_cctv_signals(frames)
    df = mgmt.merge(signals, on="individual_id", how="inner").reset_index(drop=True)
    y = df["anestrus"].astype(int).to_numpy()

    drop = {"anestrus", "individual_id", "farm"}
    feats = [c for c in df.columns if c not in drop]
    num = [c for c in feats if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in feats if c not in num]
    cctv_cols = [c for c in signals.columns if c != "individual_id"]
    mgmt_cols = [c for c in mgmt.columns if c not in drop]

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    def auc_of(cols):
        pipe = train_mod.make_pipeline(
            [c for c in cols if c in num], [c for c in cols if c in cat],
            GradientBoostingClassifier(random_state=42))
        pr = cross_val_predict(pipe, df[cols], y, cv=cv,
                               method="predict_proba")[:, 1]
        return pr, roc_auc_score(y, pr)

    proba, auc_fusion = auc_of(num + cat)
    _, auc_cctv = auc_of(cctv_cols)
    _, auc_mgmt = auc_of(mgmt_cols)

    # 특성 중요도(융합 모델)
    pipe = train_mod.make_pipeline(num, cat,
                                   GradientBoostingClassifier(random_state=42))
    pipe.fit(df[num + cat], y)
    fnames = list(num) + (list(pipe.named_steps["pre"]
                          .named_transformers_["cat"].get_feature_names_out(cat))
                          if cat else [])
    imp = pipe.named_steps["model"].feature_importances_
    importance = sorted(({"feature": FEATURE_KO.get(f, f), "value": float(v)}
                         for f, v in zip(fnames, imp)),
                        key=lambda d: d["value"], reverse=True)[:8]

    # 발정 시작점 탐지 (활동량 기준 = 모집단 80분위)
    perframe = frames.sort_values(["individual_id", "frame_idx"]).copy()
    perframe["_act"] = (perframe.groupby("individual_id")[["centroid_x", "centroid_y"]]
                        .apply(lambda g: np.sqrt(g["centroid_x"].diff() ** 2
                               + g["centroid_y"].diff() ** 2)).reset_index(level=0,
                        drop=True))
    act_ref = float(np.nanpercentile(perframe["_act"].dropna(), 80)) or 25.0
    onsets = estrus_onset.detect_all(frames, act_ref=act_ref)

    df = df.copy()
    df["risk"] = proba
    gilts = []
    for _, r in df.sort_values("risk", ascending=False).iterrows():
        gid = r["individual_id"]
        o = onsets.get(str(gid), {})
        gilts.append({
            "id": gid,
            "farm": r["farm"],
            "risk": round(float(r["risk"]), 3),
            "band": risk_band(float(r["risk"])),
            "anestrus": int(r["anestrus"]),
            "onset_status": o.get("status", "?"),
            "onset_frame": o.get("onset_frame"),
            "frames": o.get("frames", []),
            "activity": o.get("activity", []),
            "score": o.get("score", []),
            "prescribe": [FEATURE_KO.get(f, f) for f in anestrus.prescribe(r)],
            "mgmt": {FEATURE_KO.get(c, c): (round(float(r[c]), 2)
                     if isinstance(r[c], (int, float, np.floating, np.integer))
                     else r[c])
                     for c in mgmt_cols},
        })

    # 발정률: CCTV 발정 시작점이 탐지된 개체 비율 (전체/농장별)
    n_estrus = sum(1 for g in gilts if g["onset_status"] == "estrus")
    n_no_onset = len(gilts) - n_estrus
    farms = []
    fdf = pd.DataFrame(gilts)
    for fname, fg in fdf.groupby("farm"):
        det = (fg["onset_status"] == "estrus").sum()
        farms.append({
            "farm": fname, "n": int(len(fg)),
            "estrus_rate": round(det / len(fg), 3),
            "anestrus_n": int((fg["onset_status"] == "anestrus").sum()),
            "risk_mean": round(float(fg["risk"].mean()), 3),
        })
    farms.sort(key=lambda d: d["estrus_rate"])   # 발정률 낮은(문제) 농장 먼저

    return {
        "meta": {
            "n_gilts": len(gilts),
            "estrus_rate": round(n_estrus / len(gilts), 3),
            "anestrus_rate": round(float(y.mean()), 3),
            "auc_fusion": round(auc_fusion, 3),
            "auc_cctv": round(auc_cctv, 3),
            "auc_mgmt": round(auc_mgmt, 3),
            "n_no_onset": n_no_onset,
            "threshold": 0.5,
            "act_ref": round(act_ref, 1),
        },
        "importance": importance,
        "farms": farms,
        "gilts": gilts,
    }


def main() -> int:
    if len(sys.argv) >= 3 and os.path.isdir(sys.argv[1]):
        frames = parse_aihub.parse_71471(sys.argv[1])
        mgmt = pd.read_csv(sys.argv[2])
        print(f"실데이터: {sys.argv[1]} + {sys.argv[2]}")
    else:
        frames, mgmt = pipeline_gilt.generate_joint(n_gilts=200, frames=20)
        print("(합성 시연) 조인트 데이터 생성")

    data = build_data(frames, mgmt)
    tpl = open(TEMPLATE, encoding="utf-8").read()
    html = tpl.replace("/*__DATA__*/null",
                       json.dumps(data, ensure_ascii=False))
    os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
    open(OUT_HTML, "w", encoding="utf-8").write(html)
    m = data["meta"]
    print(f"대시보드 생성: {OUT_HTML}")
    print(f"  후보돈 {m['n_gilts']}두 | 무발정률 {m['anestrus_rate']:.0%} | "
          f"융합 AUC {m['auc_fusion']} (CCTV {m['auc_cctv']}/관리 {m['auc_mgmt']}) | "
          f"발정 미탐지 {m['n_no_onset']}두")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
