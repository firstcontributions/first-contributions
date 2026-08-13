"""PC 통합 콘솔 — 사무실에서 쓰는 화면 여섯을 **한 파일**로 합친다.

뷰가 파일로 흩어져 있으면 실제 업무에서 창을 옮겨 다녀야 한다. 모바일 앱
화면(app_prototype·app_screens)은 성격이 달라 제외하고, **PC 에서 진행하는
것만** 사이드바 하나로 묶는다.

## 왜 DOM 을 이어붙이지 않고 iframe 인가

여섯 뷰가 전부 `.card` `.wrap` `.sub` 같은 **같은 클래스명**을 쓰고, 각자
전역 스코프에 스크립트를 깐다(`document.querySelectorAll(".fbtn")` 식).
한 문서에 이어붙이면 CSS 가 서로를 덮고 이벤트 핸들러가 남의 요소를 잡는다.
`srcdoc` iframe 은 문서를 통째로 격리하므로 **각 뷰를 한 글자도 고치지 않고**
넣을 수 있다.

원본 HTML 은 base64 로 실어 둔다. 문자열로 그냥 넣으면 따옴표·백틱·
`</script>` 를 전부 이스케이프해야 하는데, 뷰마다 스크립트 블록이 있어
한 군데만 새도 파일 전체가 깨진다.

## 테마

각 뷰는 이미 `prefers-color-scheme` 과 `[data-theme]` 을 함께 본다. 상단
토글을 누르면 iframe 에 넣기 **전에** 문자열에서 `<html ...>` 에
`data-theme` 을 박는다. `contentDocument` 로 건드리면 file:// 에서 오리진
문제가 날 수 있어 문자열 주입 쪽이 안전하다.

    python competition/src/build_pc_suite.py
출력: competition/dashboard/pc_suite.html
"""
from __future__ import annotations

import base64
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DASH = os.path.join(ROOT, "dashboard")
OUT = os.path.join(DASH, "pc_suite.html")

# 모바일(app_prototype·app_screens)은 뺀다. 아래 여섯이 PC 에서 진행하는 것.
# 순서 = 실제 업무 순서: 오늘 할 일 → 번식 → 도면 → 흐름 → 진단 → 검증.
VIEWS = [
    ("pc_console.html", "관리 콘솔", "🖥️",
     "오늘의 작업 큐 · 일괄 처리 · 작업지시서"),
    ("breeding_console.html", "번식 관리", "📋",
     "조치 큐 · 17주 파이프라인 · 임신진단 · 교배 적기"),
    ("barn_map.html", "도면 관제", "🗺️",
     "배치도 위에 사육현황 · THI · 오늘의 업무"),
    ("pigflow_console.html", "돈군흐름", "🔄",
     "분만틀 역산 설계 · 필요 돈방 · 점유 간트 · what-if"),
    ("farm_diagnosis.html", "실측 진단", "📉",
     "466농장 분포 대비 거리 · 두수 · 원/년"),
    ("posture_report.html", "자세 병목", "🧍",
     "누수 수치 폐기 · 원리적 상한 · 하류 전파"),
]


def load(name: str) -> str | None:
    p = os.path.join(DASH, name)
    if not os.path.exists(p):
        return None
    return open(p, encoding="utf-8").read()


def strip_bom(s: str) -> str:
    return s[1:] if s and s[0] == "﻿" else s


def b64(s: str) -> str:
    return base64.b64encode(s.encode("utf-8")).decode("ascii")


def main() -> int:
    loaded, missing = [], []
    for name, label, icon, desc in VIEWS:
        html = load(name)
        if html is None:
            missing.append(name)
            continue
        loaded.append((name, label, icon, desc, strip_bom(html)))

    if not loaded:
        print("합칠 뷰가 하나도 없다. build_all.sh 를 먼저 돌릴 것.")
        return 1

    nav = "".join(
        f'<button class="nav" data-i="{i}" title="{desc}">'
        f'<span class="ic">{icon}</span><span class="tx">'
        f'<b>{label}</b><i>{desc}</i></span>'
        f'<kbd>{i+1}</kbd></button>'
        for i, (_n, label, icon, desc, _h) in enumerate(loaded))

    docs = ",\n".join(f'"{b64(h)}"' for *_x, h in loaded)
    titles = ",".join(f'"{label}"' for _n, label, _i, _d, _h in loaded)
    files = ",".join(f'"{n}"' for n, *_r in loaded)

    warn = ""
    if missing:
        warn = ('<div class="warn">데이터가 없어 빠진 화면: '
                + " · ".join(missing)
                + ' — <code>bash competition/build_all.sh</code> 로 생성</div>')

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>양돈 AI — PC 통합 콘솔</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#f2f2ee;
--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12);
--accent:#2a78d6}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{
--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;--ink:#fff;--ink2:#c3c2b7;
--muted:#898781;--border:rgba(255,255,255,.14);--accent:#3987e5}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#242422;
--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14);
--accent:#3987e5}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{height:100%}}
body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;
background:var(--page);color:var(--ink);display:grid;
grid-template-columns:246px 1fr;grid-template-rows:100%;overflow:hidden}}
aside{{background:var(--surface);border-right:1px solid var(--border);
display:flex;flex-direction:column;min-height:0}}
.brand{{padding:15px 16px 11px;border-bottom:1px solid var(--border)}}
.brand b{{font-size:.98rem;letter-spacing:-.01em;display:block}}
.brand i{{font-style:normal;font-size:.72rem;color:var(--muted)}}
.navs{{flex:1;overflow-y:auto;padding:8px 8px 4px}}
.nav{{display:flex;align-items:center;gap:9px;width:100%;text-align:left;
font:inherit;cursor:pointer;background:none;border:0;border-radius:9px;
padding:8px 9px;color:var(--ink2);margin-bottom:2px}}
.nav:hover{{background:var(--surface2)}}
.nav.on{{background:var(--accent);color:#fff}}
.nav.on i,.nav.on kbd{{color:rgba(255,255,255,.82)}}
.ic{{font-size:1.05rem;line-height:1;flex:none}}
.tx{{flex:1;min-width:0}}
.tx b{{display:block;font-size:.855rem;font-weight:600}}
.tx i{{display:block;font-style:normal;font-size:.68rem;color:var(--muted);
white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
kbd{{font:inherit;font-size:.66rem;color:var(--muted);border:1px solid
var(--border);border-radius:4px;padding:0 4px;flex:none}}
.foot{{padding:9px 14px 12px;border-top:1px solid var(--border);
font-size:.68rem;color:var(--muted);line-height:1.55}}
.tog{{font:inherit;font-size:.72rem;cursor:pointer;background:var(--surface2);
border:1px solid var(--border);border-radius:7px;padding:4px 9px;
color:var(--ink2);margin-bottom:7px}}
main{{display:flex;flex-direction:column;min-width:0;min-height:0}}
header{{display:flex;align-items:center;gap:10px;padding:9px 15px;
border-bottom:1px solid var(--border);background:var(--surface)}}
header h1{{font-size:.9rem;font-weight:600}}
header .f{{font-size:.7rem;color:var(--muted);margin-left:auto;
font-family:ui-monospace,monospace}}
.warn{{font-size:.72rem;color:#a85b00;padding:6px 15px;
background:rgba(232,163,61,.13);border-bottom:1px solid var(--border)}}
.stage{{flex:1;min-height:0;position:relative}}
iframe{{position:absolute;inset:0;width:100%;height:100%;border:0;
background:var(--page)}}
</style></head><body>
<aside>
  <div class="brand"><b>양돈 AI · PC 통합 콘솔</b>
  <i>사무실에서 진행하는 화면 {len(loaded)}개</i></div>
  <nav class="navs">{nav}</nav>
  <div class="foot"><button class="tog" id="tog">테마 전환</button>
  숫자키 1~{len(loaded)} 로 이동.<br>
  모바일 앱 화면은 제외했다 — 성격이 다르다.</div>
</aside>
<main>
  <header><h1 id="t"></h1><span class="f" id="f"></span></header>
  {warn}
  <div class="stage"><iframe id="fr" title="선택한 화면"></iframe></div>
</main>
<script>
const DOCS=[
{docs}
];
const T=[{titles}], F=[{files}];
const dec=new TextDecoder();
function unb64(s){{
  const bin=atob(s), u=new Uint8Array(bin.length);
  for(let i=0;i<bin.length;i++) u[i]=bin.charCodeAt(i);
  return dec.decode(u);
}}
// 테마는 iframe 에 넣기 **전에** 문자열의 <html> 에 박는다.
// contentDocument 로 건드리면 file:// 에서 오리진 문제가 난다.
function themed(html, mode){{
  if(!mode) return html;
  return html.replace(/<html\\b([^>]*)>/i,
    (m,a)=>'<html'+a.replace(/\\s*data-theme="[^"]*"/i,'')+
           ' data-theme="'+mode+'">');
}}
let cur=-1, mode=localStorage.getItem('pcsuite-theme')||'';
function apply(){{
  document.documentElement.setAttribute('data-theme', mode||'');
  if(!mode) document.documentElement.removeAttribute('data-theme');
}}
function show(i){{
  if(i===cur) return;
  cur=i;
  document.querySelectorAll('.nav').forEach(b=>
    b.classList.toggle('on', +b.dataset.i===i));
  document.getElementById('t').textContent=T[i];
  document.getElementById('f').textContent=F[i];
  document.getElementById('fr').srcdoc=themed(unb64(DOCS[i]), mode);
}}
document.querySelectorAll('.nav').forEach(b=>
  b.onclick=()=>show(+b.dataset.i));
document.getElementById('tog').onclick=()=>{{
  mode = mode==='dark' ? 'light' : (mode==='light' ? '' : 'dark');
  localStorage.setItem('pcsuite-theme', mode);
  apply();
  const i=cur; cur=-1; show(i);          // 현재 화면을 새 테마로 다시 그린다
}};
addEventListener('keydown', e=>{{
  if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA') return;
  const n=parseInt(e.key,10);
  if(n>=1 && n<=DOCS.length) show(n-1);
}});
apply(); show(0);
</script></body></html>"""

    os.makedirs(DASH, exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    mb = os.path.getsize(OUT) / 1048576
    print(f"PC 통합 콘솔 생성: {OUT} ({mb:.2f}MB)")
    print(f"  합친 화면 {len(loaded)}개: "
          + " · ".join(lbl for _n, lbl, _i, _d, _h in loaded))
    if missing:
        print(f"  빠짐 {len(missing)}개(데이터 필요): " + " · ".join(missing))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
