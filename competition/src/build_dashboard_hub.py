"""통합 대시보드 허브 — 6개 웹 뷰 + 리포트를 한 랜딩에서 네비게이션.

각 뷰는 자체완결 HTML(대용량, 커밋 제외)로 별도 생성된다. 이 허브(index.html)는
프로젝트 개요 KPI 와 각 뷰로 가는 카드 네비게이션을 제공한다. dashboard/ 폴더에서
index.html 을 열면 통합 앱처럼 이동한다.

    python competition/src/build_dashboard_hub.py
출력: competition/dashboard/index.html
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DASH = os.path.join(ROOT, "competition", "dashboard")
OUT = os.path.join(DASH, "index.html")

# 뷰 카드 (파일, 제목, 설명, 아이콘, 카테고리)
VIEWS = [
    ("reference_report.html", "발정 표준 리포트", "AI Hub 71471 발정 기준으로 케글 데이터 분석 + 실영상 근거", "🎯", "분석"),
    ("edinburgh.html", "활동·발정 모니터링", "개체 시계열 활동량 + 행동→발정 의심 지수", "📈", "분석"),
    ("analysis_report.html", "종합 분석 리포트", "행동 인식·자세 일반화(내부/교차-뷰/교차-데이터셋)", "📊", "분석"),
    ("behavior_gallery.html", "행동 확인 (실영상)", "6대 카메라 CCTV 피드(각 20초) + 행동 bbox+라벨", "🎬", "탐색"),
    ("posture_gallery.html", "자세 인식 (사진·영상)", "자세 5클래스 bbox(정답/예측) 사진·영상", "🧍", "탐색"),
    ("detection_viewer.html", "탐지 뷰어 (검색)", "파일명·축사번호로 검색 → 돼지 탐지 즉시 표시", "🔍", "탐색"),
    ("activity_analysis.html", "탐지 기반 행동분석", "축사·세션별 점유 heatmap + 활동량 추이", "🗺️", "분석"),
    ("gilt_dashboard.html", "후보돈 무발정 위험(합성)", "관리요인+CCTV 융합 무발정 위험 예측·처방(의사결정 프레임)", "🧪", "분석"),
]

KPIS = [
    ("3+", "데이터셋", "AI Hub 71471(참조) · Edinburgh · pig-detection"),
    ("0.49", "행동 인식 정확도", "외형 피처로 0.43→0.49 개선"),
    ("45,611", "돼지 탐지(bbox)", "pig-detection 8개 소스"),
    ("표준", "발정 판정 기준", "AI Hub 71471 발정행동"),
]


def main() -> int:
    kpi_html = "".join(
        f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div>'
        f'<div class="d">{d}</div></div>' for v, l, d in KPIS)

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>양돈 AI 통합 대시보드</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#f2f2ee;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);--accent:#2a78d6}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:26px}}
.wrap{{max-width:1000px;margin:0 auto}}
.hero{{margin-bottom:20px}}h1{{font-size:1.7rem;letter-spacing:-.02em}}.sub{{color:var(--ink2);font-size:.95rem;margin-top:6px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:18px 0 8px}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:14px 16px}}
.kpi .v{{font-size:1.7rem;font-weight:700;letter-spacing:-.02em}}.kpi .l{{font-size:.82rem;font-weight:600;margin-top:1px}}.kpi .d{{font-size:.72rem;color:var(--muted);margin-top:3px}}
.flow{{background:var(--surface2);border-radius:10px;padding:12px 15px;font-size:.83rem;color:var(--ink2);margin:14px 0 22px}}
.flow b{{color:var(--ink)}}
h2{{font-size:.85rem;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin:18px 0 10px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}}
.card{{display:flex;align-items:center;gap:14px;background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:15px 16px;text-decoration:none;color:inherit;transition:border-color .12s,transform .12s}}
.card:hover{{border-color:var(--accent);transform:translateY(-1px)}}
.ci{{font-size:1.7rem;line-height:1}}.ct{{flex:1;min-width:0}}
.tt{{font-weight:700;font-size:1rem;display:flex;align-items:center;gap:7px;flex-wrap:wrap}}
.cat{{font-size:.66rem;font-weight:600;color:var(--accent);background:color-mix(in srgb,var(--accent) 14%,transparent);padding:1px 7px;border-radius:999px}}
.cd{{font-size:.8rem;color:var(--ink2);margin-top:3px}}.arw{{color:var(--muted);font-size:1.1rem}}
.miss{{font-size:.66rem;color:#d03b3b;background:color-mix(in srgb,#d03b3b 14%,transparent);padding:1px 7px;border-radius:999px}}
.note{{font-size:.74rem;color:var(--muted);margin-top:22px;line-height:1.6}}
</style></head><body><div class="wrap">
<div class="hero">
  <h1>🐖 양돈 AI 통합 대시보드</h1>
  <div class="sub">돈방 CCTV로 <b>돼지 탐지 → 행동 인식 → 발정 판정</b>. AI Hub 71471 발정행동을 기준으로 케글 실데이터를 분석.</div>
</div>
<div class="kpis">{kpi_html}</div>
<div class="flow">파이프라인: <b>탐지</b>(YOLO) → <b>추적/활동</b>(점유·활동량) → <b>행동 인식</b>(기하+모션+외형) → <b>발정 연계</b>(71471 표준) → <b>판정·근거</b>(리포트+실영상)</div>

<h2>분석 · 리포트</h2>
<div class="grid">{cards_by(cat="분석")}</div>
<h2>데이터 탐색 · 시각화</h2>
<div class="grid">{cards_by(cat="탐색")}</div>

<div class="note">※ 각 뷰는 자체완결 HTML 로 별도 생성됩니다(대용량, 저장소엔 미포함). 전체 생성:
<code>bash competition/build_all.sh</code> 후 이 폴더의 <code>index.html</code> 을 열면 통합 이동됩니다.
'미생성' 표시는 아직 생성 안 된 뷰입니다.</div>
</div></body></html>"""
    os.makedirs(DASH, exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"통합 허브 생성: {OUT}")
    present = sum(os.path.exists(os.path.join(DASH, v[0])) for v in VIEWS)
    print(f"  뷰 {len(VIEWS)}개 중 생성됨 {present}개")
    return 0


def cards_by(cat):
    out = ""
    for fn, title, desc, icon, c in VIEWS:
        if c != cat:
            continue
        exists = os.path.exists(os.path.join(DASH, fn))
        badge = "" if exists else '<span class="miss">미생성</span>'
        out += (f'<a class="card" href="{fn}"><div class="ci">{icon}</div>'
                f'<div class="ct"><div class="tt">{title}{badge}'
                f'<span class="cat">{cat}</span></div><div class="cd">{desc}</div></div>'
                f'<div class="arw">→</div></a>')
    return out


if __name__ == "__main__":
    raise SystemExit(main())
