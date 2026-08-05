"""케글 돼지 데이터 종합 분석 리포트 (HTML).

두 케글 데이터셋을 양돈 분석 도구로 분석해 한 리포트로 정리한다.
  A) Edinburgh Pig Behaviour  — 행동 인식·활동·행동→발정 연계
  B) multi-view posture        — 자세 분류(내부/교차-뷰), 교차-데이터셋 검증

    python competition/src/build_analysis_report.py
출력: competition/dashboard/analysis_report.html
"""
from __future__ import annotations

import ast
import os
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GroupKFold, cross_val_predict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import estrus_link  # noqa: E402
import model_edinburgh_behavior as beh  # noqa: E402
import parse_edinburgh  # noqa: E402
import posture_eval  # noqa: E402
import view_align  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "analysis_report.html")
EDIN = os.path.join(ROOT, "competition", "data", "edinburgh_frames.csv")
COMP = ("/root/.cache/kagglehub/competitions/multi-view-pig-posture-recognition"
        "/multiview_pig_posture_recognition")


def analyze_edinburgh() -> dict:
    df = pd.read_csv(EDIN) if os.path.exists(EDIN) else \
        parse_edinburgh.parse_edinburgh(os.path.join(ROOT, "competition/data/edinburgh"))
    df = df[df["behavior"].notna() & df["centroid_x"].notna()]
    dm = beh.add_motion(df)
    behdist = df["behavior"].value_counts()
    act_by = (dm.groupby("behavior")["speed"].mean().sort_values(ascending=False))

    # 행동 인식(개체 분리)
    vc = df["behavior"].value_counts()
    keep = set(vc[vc >= beh.MIN_COUNT].index)
    d2 = dm.copy(); d2["behavior"] = d2["behavior"].where(d2["behavior"].isin(keep), "other")
    feats = ["bbox_w", "bbox_h", "aspect_ratio", "area", "speed", "accel",
             "darea", "centroid_x", "centroid_y"]
    d2 = d2.dropna(subset=feats)
    clf = RandomForestClassifier(n_estimators=200, min_samples_leaf=2,
                                 class_weight="balanced", n_jobs=-1, random_state=42)
    pred = cross_val_predict(clf, d2[feats], d2["behavior"], cv=GroupKFold(5),
                             groups=d2["individual_id"], n_jobs=-1)
    acc = accuracy_score(d2["behavior"], pred)
    mf1 = f1_score(d2["behavior"], pred, average="macro", zero_division=0)

    link = estrus_link.behavior_estrus_index(df)
    return {
        "n_rec": int(df["recording"].nunique()),
        "n_ind": int(df["individual_id"].nunique()),
        "n_frames": int(len(df)),
        "n_beh": int(df["behavior"].nunique()),
        "behdist": [(b, int(c), c / len(df)) for b, c in behdist.items()],
        "act_by": [(b, float(v)) for b, v in act_by.items()],
        "beh_acc": round(acc, 3), "beh_mf1": round(mf1, 3),
        "estrus_hi": int((link["estrus_index"] >= 0.6).sum()),
        "estrus_top": link[["individual_id", "estrus_index", "estrus_drivers"]]
        .head(5).values.tolist(),
    }


def analyze_posture() -> dict:
    classes = open(os.path.join(COMP, "pig_posture_classes.txt")).read().split()
    d = view_align.load(COMP)                      # train1+train2, view/cls/aspect
    clsdist = d["cls"].value_counts()
    aspect_by = d.groupby("cls")["aspect"].mean().sort_values(ascending=False)

    # 내부(train1→train2) 5클래스
    import ast as _a
    def prep(fn):
        x = pd.read_csv(os.path.join(COMP, fn))
        bb = x["bbox"].apply(_a.literal_eval)
        x["w"] = bb.apply(lambda b: b[2]); x["h"] = bb.apply(lambda b: b[3])
        x["cls"] = x["class_id"].apply(lambda i: classes[i]); return x
    tr, te = prep("train1.csv"), prep("train2.csv")
    fx = lambda z: posture_eval._feats(z["w"], z["h"], z["w"] * z["h"])
    c = RandomForestClassifier(n_estimators=200, min_samples_leaf=5,
                               class_weight="balanced", n_jobs=-1, random_state=42)
    c.fit(fx(tr), tr["cls"]); p = c.predict(fx(te))
    indom = accuracy_score(te["cls"], p)

    # 교차-뷰(뷰 정합 전/후)
    tmask = d["view"].isin(view_align.HELD_OUT_VIEWS).to_numpy()
    def cv(feat_fn):
        X = feat_fn(d)
        m = RandomForestClassifier(n_estimators=200, min_samples_leaf=3,
                                   class_weight="balanced", n_jobs=-1, random_state=42)
        m.fit(X[~tmask], d["cls"][~tmask]); pr = m.predict(X[tmask])
        return accuracy_score(d["cls"][tmask], pr)
    v_before = cv(view_align.baseline_feats)
    v_after = cv(view_align.view_aligned_feats)

    # 교차-데이터셋(Edinburgh→대회, 3클래스 공통)
    src = posture_eval.load_source(EDIN)
    comp = posture_eval.load_competition(COMP)
    Xs = posture_eval._feats(src["w"], src["h"], src["w"] * src["h"])
    Xt = posture_eval._feats(comp["w"], comp["h"], comp["w"] * comp["h"])
    cc = RandomForestClassifier(n_estimators=200, min_samples_leaf=5,
                                class_weight="balanced", n_jobs=-1, random_state=42)
    cc.fit(Xs, src["posture"]); pc = cc.predict(Xt)
    cross = accuracy_score(comp["posture"], pc)

    return {
        "n_img": int(d["image_id"].nunique()) if "image_id" in d else None,
        "n_box": int(len(d)), "n_cls": len(classes), "n_view": int(d["view"].nunique()),
        "clsdist": [(b, int(c), c / len(d)) for b, c in clsdist.items()],
        "aspect_by": [(b, float(v)) for b, v in aspect_by.items()],
        "indomain": round(indom, 3),
        "view_before": round(v_before, 3), "view_after": round(v_after, 3),
        "cross": round(cross, 3),
    }


# ---------------- HTML ----------------
def bars(rows, val_fmt, color="var(--activity)"):
    mx = max((v for *_, v in [(r[0], r[-1]) for r in rows]), default=1) or 1
    out = []
    for r in rows:
        label = r[0]; val = r[-1]
        out.append(f'<div class="hbar"><span title="{label}">{label}</span>'
                   f'<div class="track"><div class="fill" style="width:{val/mx*100:.1f}%;background:{color}"></div></div>'
                   f'<b>{val_fmt(val)}</b></div>')
    return "".join(out)


def build_html(E: dict, P: dict) -> str:
    kpi = lambda v, l: f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div></div>'
    est_rows = "".join(
        f'<tr><td>{i}</td><td><b>{idx:.0%}</b></td><td>{dr}</td></tr>'
        for i, idx, dr in E["estrus_top"])
    cmp_rows = [("자세 내부(train1→train2)", P["indomain"]),
                ("교차-뷰 정합 전", P["view_before"]),
                ("교차-뷰 정합 후", P["view_after"]),
                ("교차-데이터셋(Edin→대회)", P["cross"])]
    return f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>케글 돼지 데이터 분석 리포트</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#f2f2ee;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--activity:#2a78d6;--score:#eb6834;--good:#0ca30c;}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--activity:#3987e5;--score:#d95926;}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--activity:#3987e5;--score:#d95926;}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:22px}}
.wrap{{max-width:1000px;margin:0 auto}}h1{{font-size:1.5rem}}h2{{font-size:1.05rem;margin:22px 0 10px}}.sub{{color:var(--ink2);font-size:.9rem;margin:4px 0 8px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:10px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:11px;padding:11px 13px}}.kpi .v{{font-size:1.35rem;font-weight:700}}.kpi .l{{font-size:.72rem;color:var(--muted)}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px;margin-bottom:14px}}
.hbar{{display:grid;grid-template-columns:150px 1fr 60px;align-items:center;gap:8px;margin:4px 0;font-size:.8rem}}
.hbar .track{{background:var(--surface2);border-radius:6px;height:13px;overflow:hidden}}.hbar .fill{{height:100%;border-radius:6px}}
table{{width:100%;border-collapse:collapse;font-size:.82rem}}td,th{{text-align:left;padding:6px 9px;border-bottom:1px solid var(--surface2)}}
.note{{font-size:.76rem;color:var(--muted);margin-top:8px;line-height:1.5}}
.insight{{background:color-mix(in srgb,var(--activity) 8%,transparent);border-left:3px solid var(--activity);padding:9px 12px;border-radius:6px;font-size:.85rem;margin:8px 0}}
</style></head><body><div class="wrap">
<h1>🐖 케글 돼지 데이터 분석 리포트</h1>
<div class="sub">양돈 분석 도구로 두 케글 데이터셋을 분석. 행동 인식 → 발정 연계, 자세 분류의 일반화(내부·교차-뷰·교차-데이터셋).</div>

<h2>A. Edinburgh Pig Behaviour — 행동·활동·발정</h2>
<div class="kpis">{kpi(E['n_ind'],'개체(pig)')}{kpi(E['n_rec'],'녹화')}{kpi(f"{E['n_frames']:,}",'프레임')}{kpi(E['n_beh'],'행동 종류')}{kpi(E['beh_acc'],'행동인식 정확도')}{kpi(E['beh_mf1'],'Macro-F1')}</div>
<div class="card"><b style="font-size:.85rem">행동 분포</b>{bars(E['behdist'], lambda v:f'{v:.0%}')}</div>
<div class="card"><b style="font-size:.85rem">행동별 평균 활동량(이동속도 px/frame)</b>{bars(E['act_by'], lambda v:f'{v:.1f}', 'var(--score)')}
<div class="insight">활동량이 큰 행동(run·walk·investigating)과 작은 행동(lying·sleep)이 뚜렷이 갈린다 → <b>활동량이 발정(restlessness) 신호의 핵심</b>.</div></div>
<div class="card"><b style="font-size:.85rem">행동→발정 연계: 의심 상위 5두</b> (지수≥0.6: {E['estrus_hi']}두)
<table><tr><th>개체</th><th>발정지수</th><th>유발 행동</th></tr>{est_rows}</table></div>

<h2>B. Multi-view Posture — 자세 분류와 일반화</h2>
<div class="kpis">{kpi(f"{P['n_box']:,}",'bbox(개체)')}{kpi(P['n_cls'],'자세 클래스')}{kpi(P['n_view'],'카메라 뷰')}{kpi(P['indomain'],'내부 정확도')}{kpi(P['cross'],'교차-데이터셋')}</div>
<div class="card"><b style="font-size:.85rem">자세 클래스 분포</b>{bars(P['clsdist'], lambda v:f'{v:.0%}')}</div>
<div class="card"><b style="font-size:.85rem">자세별 평균 종횡비(w/h)</b>{bars(P['aspect_by'], lambda v:f'{v:.2f}', 'var(--score)')}
<div class="insight">측와위(lying)는 종횡비↑(넓음), standing은↓(컴팩트) → 기하만으로도 lying/standing 부분 구분 가능(sitting은 겹침).</div></div>
<div class="card"><b style="font-size:.85rem">일반화 성능 비교(정확도)</b>{bars(cmp_rows, lambda v:f'{v:.3f}', 'var(--good)')}
<div class="insight">내부(같은 뷰) {P['indomain']:.2f} ≫ 교차-뷰 {P['view_after']:.2f} ≈ 교차-데이터셋 {P['cross']:.2f}. <b>뷰·도메인이 바뀌면 기하 피처만으론 성능이 급락</b> → 외형(크롭 CNN)·뷰 정합 필요. 뷰 정합(aspect z-정규화)만으론 {P['view_before']:.3f}→{P['view_after']:.3f}로 미미.</div></div>

<h2>종합 인사이트</h2>
<div class="card" style="font-size:.86rem;line-height:1.7">
1. <b>행동→발정 연계는 실데이터로 타당</b>: 활동량·탐색 행동이 발정 신호와 정렬. 발정 정답(AI Hub 71471) 결합 시 지도 보정으로 확정 가능.<br>
2. <b>일반화가 관건</b>: 자세/행동 모델은 같은 뷰·도메인에선 쓸 만하나, 새 카메라·새 농장으로 가면 급락. 대회 성적의 핵심은 <b>교차-뷰/도메인 강건성</b>.<br>
3. <b>다음 레버</b>: bbox 크롭 외형(CNN) 피처, 시간 윈도우 시퀀스 모델, 멀티뷰 정합.
</div>
<div class="note">데이터: Kaggle Edinburgh Pig Behaviour(CC BY-NC 4.0), multi-view-pig-posture-recognition. 검증: 개체 분리 GroupKFold / held-out 뷰 / 교차-데이터셋. 생성 리포트는 커밋 제외.</div>
</div></body></html>"""


def main() -> int:
    print("Edinburgh 분석 중..."); E = analyze_edinburgh()
    print("멀티뷰 자세 분석 중..."); P = analyze_posture()
    html = build_html(E, P)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"\n리포트 생성: {OUT} ({os.path.getsize(OUT)/1024:.0f}KB)")
    print(f"[Edinburgh] 개체 {E['n_ind']} · 행동인식 {E['beh_acc']}/{E['beh_mf1']} · 발정의심 {E['estrus_hi']}두")
    print(f"[Posture] 내부 {P['indomain']} · 교차뷰 {P['view_before']}→{P['view_after']} · 교차데이터셋 {P['cross']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
