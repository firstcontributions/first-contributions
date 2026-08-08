"""Edinburgh 실데이터 → 활동 모니터링 대시보드(HTML).

돈방 CCTV 실데이터로 개체별 활동량·행동 프로필을 시각화한다. 이는 발정 관찰
시스템의 '관찰 계층'(활동↑·정지↓ = 발정 의심)을 실데이터로 보여주는 화면이다.

    python competition/src/build_edinburgh_dashboard.py [frames.csv|라벨디렉터리]
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import GroupKFold, cross_val_predict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import estrus_link  # noqa: E402
import model_edinburgh_behavior as beh_mod  # noqa: E402
import parse_edinburgh  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
TEMPLATE = os.path.join(ROOT, "competition", "dashboard", "edinburgh_template.html")
OUT_HTML = os.path.join(ROOT, "competition", "dashboard", "edinburgh.html")

# 활동성 행동(발정 관찰 관점: 활동↑) vs 정지
ACTIVE = {"walk", "run", "investigating", "fight", "playwithtoy",
          "jumpontopof", "chase", "nose-to-nose"}


def load(arg: str | None) -> pd.DataFrame:
    if arg and os.path.isfile(arg):
        return pd.read_csv(arg)
    root = arg if (arg and os.path.isdir(arg)) else "competition/data/edinburgh"
    return parse_edinburgh.parse_edinburgh(root)


def build_data(df: pd.DataFrame) -> dict:
    df = df[df["behavior"].notna() & df["centroid_x"].notna()].copy()
    df = beh_mod.add_motion(df)

    # 활동량 정규화 기준(전체 속도 80분위)
    act_ref = float(np.nanpercentile(df["speed"], 80)) or 1.0

    # 행동 인식 성능(개체 분리 GroupKFold)
    vc = df["behavior"].value_counts()
    keep = set(vc[vc >= beh_mod.MIN_COUNT].index)
    dm = df.copy()
    dm["behavior"] = dm["behavior"].where(dm["behavior"].isin(keep), "other")
    feats = ["bbox_w", "bbox_h", "aspect_ratio", "area",
             "speed", "accel", "darea", "centroid_x", "centroid_y"]
    dm = dm.dropna(subset=feats)
    clf = RandomForestClassifier(n_estimators=200, min_samples_leaf=2,
                                 class_weight="balanced", n_jobs=-1,
                                 random_state=42)
    cv = GroupKFold(n_splits=5)
    pred = cross_val_predict(clf, dm[feats], dm["behavior"], cv=cv,
                             groups=dm["individual_id"], n_jobs=-1)
    acc = float((pred == dm["behavior"]).mean())
    macro = float(f1_score(dm["behavior"], pred, average="macro"))
    classes = sorted(dm["behavior"].unique())
    f1s = f1_score(dm["behavior"], pred, average=None, labels=classes,
                   zero_division=0)
    perclass = sorted(
        ({"behavior": c, "f1": round(float(f), 3),
          "support": int((dm["behavior"] == c).sum())}
         for c, f in zip(classes, f1s)),
        key=lambda d: d["support"], reverse=True)

    # 전체 행동 분포
    total = len(df)
    behavior_dist = [{"behavior": b, "count": int(c), "frac": round(c / total, 3)}
                     for b, c in df["behavior"].value_counts().items()]

    # 개체별 프로필
    individuals = []
    for uid, g in df.groupby("individual_id"):
        g = g.sort_values("frame_idx")
        frames = g["frame_idx"].astype(int).tolist()
        speed = g["speed"].fillna(0).to_numpy()
        # 롤링 활동 점수(윈도우 10, 0~1)
        score = []
        for i in range(len(speed)):
            lo = max(0, i - 9)
            score.append(round(float(min(speed[lo:i + 1].mean() / act_ref, 1)), 3))
        beh_frac = g["behavior"].value_counts(normalize=True)
        active_frac = float(g["behavior"].isin(ACTIVE).mean())
        # 고활동 지속 구간 시작(점수 0.5 이상 3연속)
        hi = None; run = 0
        for i, s in enumerate(score):
            run = run + 1 if s >= 0.5 else 0
            if run >= 3:
                hi = frames[i - 2]; break
        individuals.append({
            "id": uid, "recording": g["recording"].iloc[0],
            "n_frames": int(len(g)),
            "activity_mean": round(float(speed.mean()), 2),
            "activity_max": round(float(speed.max()), 2),
            "active_frac": round(active_frac, 3),
            "dominant": g["behavior"].mode().iloc[0],
            "behaviors": {b: round(float(f), 3) for b, f in beh_frac.items()},
            "frames": frames,
            "activity": [round(float(x), 1) for x in speed],
            "score": score,
            "high_activity_frame": hi,
        })
    # 행동 → 발정 연계: 개체별 발정 의심 지수 + 유발 행동
    link = estrus_link.behavior_estrus_index(df).set_index("individual_id")
    for g in individuals:
        r = link.loc[g["id"]] if g["id"] in link.index else None
        g["estrus_index"] = float(r["estrus_index"]) if r is not None else 0.0
        g["estrus_drivers"] = (r["estrus_drivers"] if r is not None else "-")
    individuals.sort(key=lambda d: d["estrus_index"], reverse=True)
    n_suspect = int(sum(1 for g in individuals if g["estrus_index"] >= 0.6))

    return {
        "meta": {
            "n_individuals": int(df["individual_id"].nunique()),
            "n_recordings": int(df["recording"].nunique()),
            "n_frames": int(total),
            "n_behaviors": int(df["behavior"].nunique()),
            "accuracy": round(acc, 3), "macro_f1": round(macro, 3),
            "act_ref": round(act_ref, 2), "n_suspect": n_suspect,
        },
        "behavior_dist": behavior_dist,
        "perclass": perclass,
        "individuals": individuals,
    }


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    df = load(arg)
    data = build_data(df)
    tpl = open(TEMPLATE, encoding="utf-8").read()
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
    open(OUT_HTML, "w", encoding="utf-8").write(html)
    m = data["meta"]
    print(f"대시보드 생성: {OUT_HTML}")
    print(f"  개체 {m['n_individuals']} · 녹화 {m['n_recordings']} · "
          f"프레임 {m['n_frames']} · 행동인식 정확도 {m['accuracy']}/"
          f"Macro-F1 {m['macro_f1']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
