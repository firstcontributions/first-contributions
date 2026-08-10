"""자세 인식 병목 리포트 — 무엇이 병목이었고 무엇을 고쳤는가.

교배사(스톨)는 돼지가 이동하지 못해 활동량 신호가 구조적으로 없다. 남는 건
자세와 그 변화이므로 **자세 정확도가 곧 교배사 발정 판정의 상한**이다. 이 뷰는
그 상한을 왜 못 올렸는지 분해하고, 무엇으로 얼마나 올렸는지 보인다.

이 리포트가 다른 성능 리포트와 다른 점: **개선폭보다 "어떤 숫자를 봐야 하는가"를
먼저 다룬다.** 기존에 보고하던 0.642 는 누수된 분할에서 나온 값이었고, 정직하게
재면 기존 모델은 다수 클래스만 찍는 기준선보다도 정확도가 낮았다. 그 사실을
숨기지 않고 첫 화면에 둔다.

  1) 폐기한 수치와 이유       누수 분할(이미지 3,090장 공유)
  2) 원리적 상한             좌/우 횡와는 bbox 로 구분 불가 → 5클래스 상한 0.861
  3) 기준선 대비 비교         다수 클래스 찍기 vs 기하 vs 개선
  4) 혼동행렬                동전던지기의 증거
  5) 폴드별 분산             한 번의 분할을 믿을 수 없는 이유
  6) 하류 전파               자세 개선 → 발정 판정 AUC

    python competition/src/build_posture_report.py
출력: competition/dashboard/posture_report.html  (외부 연결 불필요)
"""
from __future__ import annotations

import html as _html
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import posture_crossview as pcv  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "posture_report.html")
E = _html.escape
KO = {"Lateral_lying_left": "좌횡와", "Lateral_lying_right": "우횡와",
      "Sitting": "기좌", "Standing": "기립", "Sternal_lying": "복와"}

# 하류 전파(stall_estrus.degrade 실측, 스톨 200개·시드 20회)
PROPAGATION = [(1.000, "완벽 (참고)", 0.804, 0.000),
               (0.636, "개선 후", 0.709, 0.016),
               (0.547, "다수 클래스", 0.699, 0.029),
               (0.513, "기존 (기하만)", 0.684, 0.028)]


def grouped_bars(rows, width=860, bar_h=17, gap=5, group_gap=14,
                 series=(("acc_w", "정확도", "#2a78d6"),
                         ("mf1_w", "Macro-F1", "#e8a33d")),
                 ref=None, ref_label="기준선") -> str:
    """구성별 묶음 막대. rows = [(라벨, {키:값}, 강조여부)]."""
    lbl_w, val_w = 190, 54
    plot = width - lbl_w - val_w
    mx = max(max(v.get(k, 0) for k, _n, _c in series) for _l, v, _h in rows) or 1
    mx = max(mx, ref or 0) * 1.12
    gh = len(series) * bar_h + (len(series) - 1) * gap
    h = len(rows) * (gh + group_gap) + 24
    p = []
    if ref:
        rx = lbl_w + plot * ref / mx
        p.append(f'<line x1="{rx:.1f}" y1="6" x2="{rx:.1f}" y2="{h - 20}" '
                 f'stroke="#d03b3b" stroke-dasharray="4 3" stroke-width="1.3"/>'
                 f'<text x="{rx + 4:.1f}" y="{h - 8}" class="tk" fill="#d03b3b">'
                 f'{ref_label} {ref:.3f}</text>')
    y = 8
    for lab, vals, hi in rows:
        p.append(f'<text x="{lbl_w - 8}" y="{y + gh / 2 + 4}" '
                 f'class="{"bl hi" if hi else "bl"}" text-anchor="end">'
                 f'{E(lab)}</text>')
        for j, (k, _name, col) in enumerate(series):
            v = vals.get(k, 0.0)
            w = max(1.5, plot * v / mx)
            yy = y + j * (bar_h + gap)
            p.append(f'<rect x="{lbl_w}" y="{yy}" width="{w:.1f}" '
                     f'height="{bar_h}" rx="3" fill="{col}" '
                     f'fill-opacity="{"1" if hi else ".72"}"/>'
                     f'<text x="{lbl_w + w + 6:.1f}" y="{yy + bar_h - 4}" '
                     f'class="bv">{v:.3f}</text>')
        y += gh + group_gap
    leg = " ".join(f'<tspan fill="{c}">■</tspan> {n}' for _k, n, c in series)
    p.append(f'<text x="{lbl_w}" y="{h - 6}" class="tk">{leg}</text>')
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" role="img">'
            f'{"".join(p)}</svg>')


def confusion_svg(labels, matrix, width=560) -> str:
    """행 정규화 혼동행렬 — 대각이 정답. 좌/우 횡와 칸을 강조한다."""
    n = len(labels)
    pad_l, pad_t = 74, 66
    cell = (width - pad_l - 10) / n
    h = pad_t + cell * n + 14
    M = np.array(matrix, dtype=float)
    row = M.sum(axis=1, keepdims=True)
    row[row == 0] = 1
    P = M / row
    p = []
    for j, lab in enumerate(labels):
        x = pad_l + j * cell + cell / 2
        p.append(f'<text x="{x}" y="{pad_t - 8}" class="cx" '
                 f'transform="rotate(-35 {x} {pad_t - 8})">{E(KO.get(lab, lab))}</text>')
    for i, lab in enumerate(labels):
        yy = pad_t + i * cell + cell / 2 + 4
        p.append(f'<text x="{pad_l - 8}" y="{yy}" class="cy" '
                 f'text-anchor="end">{E(KO.get(lab, lab))}</text>')
        for j in range(n):
            v = P[i, j]
            x = pad_l + j * cell
            y = pad_t + i * cell
            op = 0.08 + 0.9 * v
            col = "#1baf7a" if i == j else "#d03b3b"
            p.append(f'<g><title>{E(KO.get(lab, lab))} → '
                     f'{E(KO.get(labels[j], labels[j]))}: {int(M[i, j])}건 '
                     f'({v:.0%})</title>'
                     f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell - 1.5:.1f}" '
                     f'height="{cell - 1.5:.1f}" rx="3" fill="{col}" '
                     f'fill-opacity="{op:.2f}"/>'
                     f'<text x="{x + cell / 2:.1f}" y="{y + cell / 2 + 4:.1f}" '
                     f'class="cv">{v:.2f}</text></g>')
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" '
            f'style="max-width:{width}px" role="img" '
            f'aria-label="교차-뷰 혼동행렬">{"".join(p)}</svg>')


def fold_svg(folds, width=860) -> str:
    """폴드별 정확도 — 분산이 크다는 사실 자체가 메시지."""
    h, pad_l, pad_b = 178, 130, 26
    n = len(folds)
    bh = (h - pad_b - 8) / n
    accs = [f["acc"] for f in folds]
    mean = float(np.mean(accs))
    plot = width - pad_l - 56
    p = [f'<line x1="{pad_l + plot * mean:.1f}" y1="4" '
         f'x2="{pad_l + plot * mean:.1f}" y2="{h - pad_b}" stroke="var(--muted)" '
         f'stroke-dasharray="4 3"/>'
         f'<text x="{pad_l + plot * mean + 4:.1f}" y="{h - pad_b + 14}" '
         f'class="tk">단순평균 {mean:.3f}</text>']
    for i, f in enumerate(sorted(folds, key=lambda r: -r["acc"])):
        y = 6 + i * bh
        w = max(2.0, plot * f["acc"])
        p.append(f'<text x="{pad_l - 8}" y="{y + bh / 2 + 3}" class="bl" '
                 f'text-anchor="end">{E(f["view"])}</text>'
                 f'<rect x="{pad_l}" y="{y}" width="{w:.1f}" '
                 f'height="{bh - 5:.1f}" rx="3" fill="#2a78d6" '
                 f'fill-opacity=".8"><title>{E(f["view"])} · 검증 '
                 f'{f["n_test"]:,}건</title></rect>'
                 f'<text x="{pad_l + w + 6:.1f}" y="{y + bh / 2 + 3}" '
                 f'class="bv">{f["acc"]:.3f} <tspan class="tk">'
                 f'(n={f["n_test"]:,})</tspan></text>')
    return (f'<svg viewBox="0 0 {width} {h}" width="100%" role="img">'
            f'{"".join(p)}</svg>')


def main() -> int:
    r = pcv.run_all(rebuild="--rebuild" in sys.argv)
    base, cfgs = r["baseline"], r["configs"]
    best = max(cfgs, key=lambda c: c["cls3"]["acc_w"])
    geom = cfgs[0]
    ceil = r["ceiling"]

    rows5 = [("다수 클래스만 찍기", base["cls"], False)] + [
        (c["tag"], c["cls"], c is best) for c in cfgs]
    rows3 = [("다수 클래스만 찍기", base["cls3"], False)] + [
        (c["tag"], c["cls3"], c is best) for c in cfgs]

    pen_rows = "".join(
        f'<tr><td>{E(p["tag"])}</td><td>{p["cls"]:.3f}</td>'
        f'<td>{p["cls_mf1"]:.3f}</td><td><b>{p["cls3"]:.3f}</b></td>'
        f'<td>{p["cls3_mf1"]:.3f}</td></tr>' for p in r["pen"])

    prop_rows = "".join(
        f'<tr><td>{a:.3f}</td><td>{E(lab)}</td>'
        f'<td><b>{auc:.3f}</b>{f" ± {sd:.3f}" if sd else ""}</td></tr>'
        for a, lab, auc, sd in PROPAGATION)
    p_best = next(x[2] for x in PROPAGATION if x[0] == 0.636)
    p_old = next(x[2] for x in PROPAGATION if x[0] == 0.513)
    p_perf = next(x[2] for x in PROPAGATION if x[0] == 1.0)
    recov = (p_best - p_old) / (p_perf - p_old)

    kpis = [
        ("폐기", "이전 보고값 0.642", "누수 분할 — 이미지 3,090장 공유"),
        (f'{ceil["ceiling"]:.3f}', "5클래스 원리적 상한",
         f'좌/우 횡와 {ceil["lr_share"]:.1%} 는 bbox 로 구분 불가'),
        (f'{best["cls3"]["acc_w"]:.3f}', "발정 3클래스 (개선)",
         f'기존 {geom["cls3"]["acc_w"]:.3f} · 기준선 {base["cls3"]["acc_w"]:.3f}'),
        (f'+{p_best - p_old:.3f}', "발정 판정 AUC 이득",
         f'{p_old:.3f} → {p_best:.3f} (격차의 {recov:.0%} 회수)'),
    ]
    kpi_html = "".join(
        f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div>'
        f'<div class="d">{d}</div></div>' for v, l, d in kpis)

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>자세 인식 병목 리포트</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#eeeeea;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--accent:#2a78d6}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:1000px;margin:0 auto}}h1{{font-size:1.55rem;letter-spacing:-.02em}}
.sub{{color:var(--ink2);font-size:.92rem;margin:5px 0 4px}}
h2{{font-size:1.02rem;margin:24px 0 4px}}.h2d{{font-size:.8rem;color:var(--muted);margin-bottom:12px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:16px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:13px 15px}}
.kpi .v{{font-size:1.65rem;font-weight:700;letter-spacing:-.02em}}.kpi .l{{font-size:.8rem;font-weight:600;margin-top:1px}}.kpi .d{{font-size:.7rem;color:var(--muted);margin-top:3px}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:13px;padding:17px 18px;margin-bottom:14px;overflow-x:auto}}
.warn{{border-left:4px solid #d03b3b;background:color-mix(in srgb,#d03b3b 6%,var(--surface))}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
@media(max-width:800px){{.two{{grid-template-columns:1fr}}}}
table{{width:100%;border-collapse:collapse;font-size:.83rem;margin-top:4px}}
td,th{{text-align:left;padding:7px 9px;border-bottom:1px solid var(--surface2);vertical-align:top;white-space:nowrap}}
th{{color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.03em}}
.note{{font-size:.73rem;color:var(--muted);margin-top:10px;line-height:1.6}}
.bl{{font-size:11.5px;fill:var(--ink2)}}.bl.hi{{fill:var(--ink);font-weight:700}}
.bv{{font-size:11px;font-weight:600;fill:var(--ink)}}
.tk{{font-size:10px;font-weight:600;fill:var(--muted)}}
.cx{{font-size:10.5px;fill:var(--ink2);text-anchor:start}}
.cy{{font-size:10.5px;fill:var(--ink2)}}
.cv{{font-size:10px;fill:var(--ink);text-anchor:middle;opacity:.85}}
</style></head><body><div class="wrap">
<h1>🧍 자세 인식 병목 리포트</h1>
<div class="sub">교배사(스톨)는 돼지가 이동하지 못해 <b>활동량 신호가 구조적으로 없다</b>. 남는 건 자세와 그 변화이므로 <b>자세 정확도가 곧 교배사 발정 판정의 상한</b>이다.</div>
<div class="kpis">{kpi_html}</div>

<h2>1. 먼저, 폐기한 수치</h2>
<div class="card warn">
<b>이전에 보고하던 자세 정확도 0.642 는 누수된 분할에서 나온 값이라 폐기했다.</b>
원 프로토콜(train1 학습 → train2 검증)은 두 파일이 <b>이미지 3,090장</b>을 공유한다.
같은 프레임이 학습과 검증에 모두 들어가면 위치 피처가 정답을 외운다.
못 본 카메라로 다시 재면 0.4 대다.
<div class="note">개선폭을 보고하기 전에 기준선부터 바로잡는 것이 순서다. 아래 수치는
전부 <b>뷰별 leave-one-out({len(r["folds"])}폴드)</b> — 검증 카메라는 학습에 한 번도 등장하지 않는다.</div>
</div>

<h2>2. 원리적 상한 — 좌/우 횡와는 bbox 로 구분할 수 없다</h2>
<div class="h2d">좌횡와와 우횡와는 <b>둘 다 옆으로 누운 같은 모양의 상자</b>다. 상자만 봐서는 원리상 구분이 불가능하고, 모델은 실제로 동전을 던진다(아래 혼동행렬).</div>
<div class="card">
전체의 <b>{ceil["lr_share"]:.1%}</b> 가 이 두 클래스다 → 완전히 못 가른다고 보면
5클래스 정확도의 상한은 <b>{ceil["ceiling"]:.3f}</b> 이지 1.0 이 아니다.
<div class="note">그리고 <b>발정 판정에는 좌우가 아무 의미가 없다</b> — <code>stall_estrus</code> 는 어차피
기립/기좌/횡와로 뭉친다. 즉 이 손실은 모델의 한계가 아니라 <b>과제 정의</b>의 문제이며,
응용 지표는 3클래스로 봐야 한다.</div>
</div>

<h2>3. 기준선 대비 — 정확도만 보면 안 된다</h2>
<div class="h2d">기존 기하 전용 모델은 5클래스 {geom["cls"]["acc_w"]:.3f} 인데, <b>다수 클래스만 찍어도 {base["cls"]["acc_w"]:.3f}</b> 다. 정확도 기준으로는 기준선보다 못하다. 클래스가 치우쳐 정확도가 신호를 가린다 — 판별력은 Macro-F1 에서 드러난다.</div>
<div class="two">
<div><div class="h2d"><b>5클래스</b> (원본 과제)</div>
<div class="card">{grouped_bars(rows5, width=470, ref=base["cls"]["acc_w"], ref_label="기준선 acc")}</div></div>
<div><div class="h2d"><b>발정 3클래스</b> (응용 지표)</div>
<div class="card">{grouped_bars(rows3, width=470, ref=base["cls3"]["acc_w"], ref_label="기준선 acc")}</div></div>
</div>
<div class="card">
<b>개선 결과 ({E(best["tag"])})</b><br>
5클래스 acc {geom["cls"]["acc_w"]:.3f} → <b>{best["cls"]["acc_w"]:.3f}</b>
({best["cls"]["acc_w"] - geom["cls"]["acc_w"]:+.3f}) ·
MF1 {geom["cls"]["mf1_w"]:.3f} → <b>{best["cls"]["mf1_w"]:.3f}</b>
({best["cls"]["mf1_w"] - geom["cls"]["mf1_w"]:+.3f})<br>
발정 3클래스 acc {geom["cls3"]["acc_w"]:.3f} → <b>{best["cls3"]["acc_w"]:.3f}</b>
({best["cls3"]["acc_w"] - geom["cls3"]["acc_w"]:+.3f}) ·
MF1 {geom["cls3"]["mf1_w"]:.3f} → <b>{best["cls3"]["mf1_w"]:.3f}</b>
({best["cls3"]["mf1_w"] - geom["cls3"]["mf1_w"]:+.3f})
<div class="note"><b>두 수단의 상호작용이 예상 밖이었다.</b> 뷰 정규화 단독은
{cfgs[1]["cls3"]["acc_w"] - geom["cls3"]["acc_w"]:+.3f} 로 오히려 해로운데, 크롭 외형과 합치면
{best["cls3"]["acc_w"] - geom["cls3"]["acc_w"]:+.3f} 가 된다. 기하 피처는 이미 프레임 상대값이라 정규화할 여지가 없고,
카메라별 밝기·대비 편차를 안고 있는 건 크롭 쪽이기 때문이다.</div>
</div>

<h2>4. 혼동행렬 — 동전던지기의 증거</h2>
<div class="h2d">행 = 정답, 열 = 예측(행 기준 비율). 좌횡와 행을 보면 좌·우로 거의 반씩 갈린다. 초록 대각이 정답, 붉을수록 오분류.</div>
<div class="two">
<div><div class="h2d">기하만 (기존)</div>
<div class="card">{confusion_svg(r["confusion_geom"]["labels"], r["confusion_geom"]["matrix"], 470)}</div></div>
<div><div class="h2d">기하 + 크롭 + 뷰 정규화</div>
<div class="card">{confusion_svg(r["confusion_best"]["labels"], r["confusion_best"]["matrix"], 470)}</div></div>
</div>

<h2>5. 폴드별 분산 — 한 번의 분할을 믿을 수 없는 이유</h2>
<div class="h2d">기존 코드는 뷰 8개 중 마지막 2개만 held-out 으로 썼는데 <b>그 둘이 전체의 42%</b> 였다. 카메라마다 난이도가 크게 다르므로 한 번의 임의 분할로 낸 수치로는 개선을 잴 수 없다.</div>
<div class="card">{fold_svg(best["folds3"])}
<div class="note">최선 구성 · 발정 3클래스 기준. 가중평균 {best["cls3"]["acc_w"]:.3f}
(검증 표본 수로 가중). 단순평균과 다른 것은 폴드 크기가 크게 다르기 때문이다.</div></div>

<h2>6. 더 엄정한 조건 — 돈방째 held-out</h2>
<div class="h2d">카메라만 빼면 <b>같은 돈방의 다른 카메라가 같은 돼지를 비춘다</b>. '새 농장'에 가장 가까운 조건은 돈방을 통째로 빼는 것이다.</div>
<div class="card"><table><thead><tr><th>구성</th><th>5클래스 acc</th><th>5클래스 MF1</th><th>3클래스 acc</th><th>3클래스 MF1</th></tr></thead>
<tbody>{pen_rows}</tbody></table>
<div class="note">더 엄정한 조건에서도 개선이 유지된다.</div></div>

<h2>7. 하류 전파 — 발정 판정은 얼마나 좋아지는가</h2>
<div class="h2d">자세는 그 자체가 목적이 아니다. <code>stall_estrus</code> 에 자세 오류를 주입해 발정 판정 AUC 까지 밀어서 재야 개선이 값을 하는지 알 수 있다(스톨 200개·시드 20회).</div>
<div class="card"><table><thead><tr><th>자세 3클래스 정확도</th><th>구성</th><th>발정 판정 AUC</th></tr></thead>
<tbody>{prop_rows}</tbody></table>
<div class="note">자세 {0.513:.3f}→{0.636:.3f} 개선이 발정 AUC 를 <b>{p_best - p_old:+.3f}</b> 올린다 —
완벽한 자세까지의 격차 {p_perf - p_old:.3f} 중 <b>{recov:.0%}</b> 회수. 전파가 1:1 이 아닌 것은
자세 오차가 시계열 통계(전환율·부동 비율)로 집계되며 일부 상쇄되기 때문이다.<br>
<b>이 측정도 처음엔 틀렸다.</b> 스톨 24개·시드 5회로 재니 시드 분산에 <b>순서가 뒤집혀</b>
정확도가 낮은 쪽의 AUC 가 더 높게 나왔다. 그대로 뒀으면 거짓 결론을 실을 뻔했다.</div></div>

<div class="note">※ 데이터: multi-view pig posture recognition {r["n_boxes"]:,}박스 · 이미지 {r["n_images"]:,} · 뷰 {r["n_views"]}개.<br>
※ 뷰 정규화는 검증 뷰의 <b>입력 분포만</b> 쓰는 무감독 보정이며 라벨을 쓰지 않는다. 현장 절차와 같다(설치 → 녹화 수집 → 통계 산출 → 판정). 다만 통계를 안정적으로 뽑을 프레임이 필요하므로 단발 이미지 추론에는 쓸 수 없다.<br>
※ 하류 전파의 오류 모형은 균등 추출 단순화다. 실제 혼동은 비대칭(횡와↔기립)이라 어림치다.</div>
</div></body></html>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"자세 병목 리포트 생성: {OUT} ({os.path.getsize(OUT) // 1024}KB)")
    print(f"  폴드 {len(r['folds'])} · 구성 {len(cfgs)} · "
          f"발정 3클래스 {geom['cls3']['acc_w']:.3f} → {best['cls3']['acc_w']:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
