"""PC 관리 콘솔 — 사무실에서 쓰는 화면. 폰과 할 일이 다르다.

같은 데이터를 쓰지만 목적이 다르므로 레이아웃도 달라야 한다. 폰은 축사에서
한 손으로 한 건씩 처리하는 물건이고, PC 는 사무실에서 **여러 건을 한 번에**
다루는 물건이다. 폰 화면을 그대로 늘리면 둘 다 어정쩡해진다.

PC 에서만 되는 것 네 가지:
  1) **일괄 처리** — 체크박스로 여러 개체를 골라 한 번에 완료 처리. 축사에서
     10건을 끝내고 돌아와 한 번에 기록하는 것이 실제 흐름이다.
  2) **넓은 표** — 개체 목록을 정렬·필터하며 한 화면에 수십 행. 폰의 카드
     목록으로는 군 전체를 훑을 수 없다.
  3) **마스터-디테일** — 왼쪽에서 고르면 오른쪽에 상세가 뜬다. 화면 이동이
     없으니 여러 개체를 빠르게 비교할 수 있다.
  4) **작업지시서 인쇄** — 동별 작업 목록을 종이로 뽑아 들고 나간다. 축사에
     폰을 들고 들어가기 어려운 농장이 아직 많다.

키보드도 붙였다(j/k 이동, space 완료, / 검색) — 마우스만 쓰는 것보다 빠르다.

    python competition/src/build_pc_console.py
출력: competition/dashboard/pc_console.html  (외부 연결 불필요)
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from build_app_prototype import build_payload  # noqa: E402

OUT = os.path.join(ROOT, "competition", "dashboard", "pc_console.html")

CSS = """
:root{color-scheme:light;--page:#f4f4f2;--surf:#fff;--surf2:#f0f0ec;--ink:#0b0b0b;
--ink2:#52514e;--muted:#8d8b85;--border:rgba(11,11,11,.13);--accent:#2a78d6;
--sel:color-mix(in srgb,#2a78d6 12%,transparent)}
@media(prefers-color-scheme:dark){:root:where(:not([data-theme=light])){
--page:#0c0c0c;--surf:#171716;--surf2:#212120;--ink:#fff;--ink2:#c3c2b7;
--muted:#8d8b85;--border:rgba(255,255,255,.14);--accent:#3987e5;
--sel:color-mix(in srgb,#3987e5 20%,transparent)}}
:root[data-theme=dark]{--page:#0c0c0c;--surf:#171716;--surf2:#212120;--ink:#fff;
--ink2:#c3c2b7;--muted:#8d8b85;--border:rgba(255,255,255,.14);--accent:#3987e5;
--sel:color-mix(in srgb,#3987e5 20%,transparent)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;
background:var(--page);color:var(--ink);line-height:1.5;font-size:13px}
.shell{display:grid;grid-template-columns:186px 1fr 316px;height:100vh}
@media(max-width:1180px){.shell{grid-template-columns:60px 1fr 300px}
 .nav b{display:none}.brand span{display:none}}
@media(max-width:900px){.shell{grid-template-columns:60px 1fr}
 .detail{display:none}}
.side{background:var(--surf);border-right:1px solid var(--border);
display:flex;flex-direction:column;overflow:hidden}
.brand{padding:15px 14px 11px;font-weight:800;font-size:.95rem;
display:flex;align-items:center;gap:7px;letter-spacing:-.02em}
.nav{padding:4px 8px;flex:1;overflow-y:auto}
.nav a{display:flex;align-items:center;gap:9px;padding:8px 10px;border-radius:8px;
color:var(--ink2);text-decoration:none;font-size:.83rem;margin-bottom:2px;
cursor:pointer}
.nav a:hover{background:var(--surf2)}
.nav a.on{background:var(--sel);color:var(--accent);font-weight:700}
.nav i{font-style:normal;width:16px;text-align:center;font-size:1rem}
.nav .cnt{margin-left:auto;font-size:.68rem;color:var(--muted);font-weight:600}
.sidefoot{padding:10px 14px;border-top:1px solid var(--border);
font-size:.66rem;color:var(--muted);line-height:1.5}
.main{display:flex;flex-direction:column;overflow:hidden}
.top{display:flex;align-items:center;gap:9px;padding:11px 16px;
border-bottom:1px solid var(--border);background:var(--surf);flex-shrink:0}
.top h1{font-size:1.02rem;letter-spacing:-.01em}
.top .sp{flex:1}
.srch{padding:6px 10px;border-radius:7px;border:1px solid var(--border);
background:var(--surf2);color:var(--ink);font-size:.8rem;width:170px}
.btn{padding:6px 12px;border-radius:7px;border:1px solid var(--border);
background:var(--surf2);color:var(--ink);font-size:.78rem;cursor:pointer;
font-weight:600}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn.pri{background:var(--accent);color:#fff;border-color:var(--accent)}
.btn.pri:hover{opacity:.88;color:#fff}
.btn:disabled{opacity:.4;cursor:default}
.body{flex:1;overflow-y:auto;padding:14px 16px 26px}
.detail{background:var(--surf);border-left:1px solid var(--border);
overflow-y:auto;padding:14px}
table{width:100%;border-collapse:collapse;font-size:.8rem}
th{text-align:left;padding:6px 8px;color:var(--muted);font-size:.68rem;
text-transform:uppercase;letter-spacing:.04em;border-bottom:1px solid var(--border);
position:sticky;top:0;background:var(--page);cursor:pointer;user-select:none}
th:hover{color:var(--accent)}
td{padding:6px 8px;border-bottom:1px solid var(--surf2);white-space:nowrap}
tr.r{cursor:pointer}
tr.r:hover td{background:var(--surf2)}
tr.r.sel td{background:var(--sel)}
tr.r.cur td{box-shadow:inset 2px 0 0 var(--accent)}
tr.done td{opacity:.42;text-decoration:line-through}
.pill{font-size:.68rem;font-weight:700;padding:1px 7px;border-radius:999px;
white-space:nowrap}
.dotc{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px}
.bgrp{margin-bottom:16px}
.bgh{display:flex;align-items:center;gap:9px;padding:7px 8px;background:var(--surf);
border:1px solid var(--border);border-radius:9px 9px 0 0;font-size:.86rem}
.bord{background:var(--accent);color:#fff;width:19px;height:19px;border-radius:50%;
font-size:.66rem;display:flex;align-items:center;justify-content:center;font-weight:700}
.bsup{font-size:.7rem;color:var(--ink2);margin-left:auto}
.bcrit{font-size:.66rem;font-weight:700;color:#d03b3b;
background:rgba(208,59,59,.13);padding:1px 8px;border-radius:999px}
.bwrap{border:1px solid var(--border);border-top:0;border-radius:0 0 9px 9px;
overflow:hidden;background:var(--surf)}
.bwrap th{background:var(--surf);position:static}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));
gap:10px;margin-bottom:14px}
.kpi{background:var(--surf);border:1px solid var(--border);border-radius:10px;
padding:10px 12px}
.kpi b{display:block;font-size:1.5rem;letter-spacing:-.02em}
.kpi span{font-size:.7rem;color:var(--muted)}
.dh{font-size:1.35rem;font-weight:800;letter-spacing:-.02em}
.dsub{font-size:.74rem;color:var(--muted);margin-bottom:10px}
.dgrid{display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;margin-bottom:12px}
.dgrid span{display:block;font-size:.65rem;color:var(--muted)}
.dgrid b{font-size:.83rem}
.sect{font-size:.66rem;font-weight:700;color:var(--muted);margin:12px 0 5px;
text-transform:uppercase;letter-spacing:.04em}
.tli{display:flex;gap:7px;font-size:.74rem;padding:3px 0;
border-bottom:1px solid var(--surf2)}
.tli.est{color:var(--ink2)}
.tli .dot{width:10px;font-weight:700}
.tli .dt{width:38px;color:var(--muted);font-variant-numeric:tabular-nums}
.tli .tk{flex:1;font-weight:600}
.tli .dd{font-size:.66rem;color:var(--muted)}
.warn{border-left:3px solid #e0407f;background:color-mix(in srgb,#e0407f 8%,var(--surf2));
padding:8px 10px;border-radius:7px;font-size:.74rem;margin-bottom:10px}
.hint{font-size:.72rem;color:var(--ink2);background:var(--surf2);border-radius:8px;
padding:9px 11px;margin-top:14px;line-height:1.6}
.mbarn{background:var(--surf);border:1px solid var(--border);border-radius:10px;
padding:10px 12px;margin-bottom:10px}
.mh{font-size:.84rem;font-weight:700;margin-bottom:7px;display:flex;
justify-content:space-between}
.mpen{font-size:.68rem;color:var(--muted);margin:5px 0 3px}
.mcells{display:flex;flex-wrap:wrap;gap:4px}
.mcells i{width:26px;height:20px;border-radius:4px;font-style:normal;
font-size:.6rem;color:#fff;text-align:center;line-height:20px;cursor:pointer}
.mcells i:hover{outline:2px solid var(--ink)}
.mleg{display:flex;flex-wrap:wrap;gap:9px;margin-top:8px;font-size:.68rem;
color:var(--ink2)}
.mleg span{display:inline-flex;align-items:center;gap:4px}
.mleg i{width:10px;height:10px;border-radius:2px}
.chart{display:flex;align-items:flex-end;gap:4px;height:130px;
border-bottom:1px solid var(--border);position:relative;margin:8px 0 4px}
.wk{flex:1;display:flex;flex-direction:column;align-items:center;
justify-content:flex-end}
.wb{width:100%;border-radius:3px 3px 0 0;min-height:2px}
.wk span{font-size:.62rem;font-weight:700}
.wk em{font-size:.56rem;color:var(--muted);font-style:normal}
.tline{position:absolute;left:0;right:0;border-top:1px dashed #d03b3b}
.tline span{position:absolute;right:0;top:-12px;font-size:.6rem;color:#d03b3b;
font-weight:700}
.empty{color:var(--muted);padding:26px;text-align:center}
.kbd{display:inline-block;border:1px solid var(--border);border-bottom-width:2px;
border-radius:4px;padding:0 4px;font-size:.68rem;font-family:ui-monospace,monospace;
background:var(--surf2)}
@media print{
 .side,.top,.detail,.hint,.noprint{display:none!important}
 .shell{display:block;height:auto}.body{overflow:visible;padding:0}
 body{background:#fff;font-size:11px}
 .bgrp{break-inside:avoid;margin-bottom:10px}
 .prt{display:block!important;margin-bottom:12px}
 td,th{border-color:#ccc}
}
.prt{display:none}
"""

JS = r"""
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const el=(t,c,h)=>{const e=document.createElement(t);if(c)e.className=c;
 if(h!==undefined)e.innerHTML=h;return e;};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,
 c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const byId=Object.fromEntries(D.animals.map(a=>[a.id,a]));
const T0=new Date(D.today+'T00:00:00');
const dday=d=>d==null?'-':(d===0?'오늘':'D-'+d);
const dnum=iso=>Math.round((new Date(iso+'T00:00:00')-T0)/864e5);
const md=iso=>iso?iso.slice(5).replace('-','/'):'';

const LKEY='pig_worklog_v1';
const loadLog=()=>{try{return JSON.parse(localStorage.getItem(LKEY)||'[]');}
 catch(e){return[];}};
const saveLog=x=>{try{localStorage.setItem(LKEY,JSON.stringify(x));}catch(e){}};
function addLog(a,result){
  const g=loadLog();
  g.push({ts:new Date().toISOString().slice(0,19),id:a.id,task:a.task,
   result:result,loc:a.loc,planned:a.date,operator:'사무실'});
  saveLog(g);
}
const isDone=a=>loadLog().some(x=>x.id===a.id&&x.task===a.task&&x.result==='완료');

let route='home', sel=new Set(), cur=null, sortKey='id', sortAsc=true, q='';

function go(r){route=r;sel.clear();render();}
function pick(id){cur=id;renderDetail();
  $$('tr.r').forEach(t=>t.classList.toggle('cur',t.dataset.id===id));}

function remainByBarn(){
  return D.queue.map(g=>({...g,items:g.ids.map(i=>byId[i])
    .filter(a=>a&&!isDone(a))})).filter(g=>g.items.length);
}

function bulkBar(n){
  const b=el('div',null,'');
  const ok=el('button','btn pri',`선택 ${n}건 완료`);
  ok.disabled=!n;
  ok.onclick=()=>{sel.forEach(id=>{const a=byId[id];if(a)addLog(a,'완료');});
    sel.clear();render();};
  const sk=el('button','btn',`미실시`); sk.disabled=!n;
  sk.onclick=()=>{sel.forEach(id=>{const a=byId[id];if(a)addLog(a,'미실시');});
    sel.clear();render();};
  b.append(ok,document.createTextNode(' '),sk);
  return b;
}

function rowFor(a,withChk){
  const c=D.taskColors[a.task]||'#888';
  const done=isDone(a);
  const tr=el('tr','r'+(done?' done':'')+(sel.has(a.id)?' sel':''));
  tr.dataset.id=a.id;
  tr.innerHTML=
   (withChk?`<td><input type="checkbox" ${sel.has(a.id)?'checked':''}
     ${done?'disabled':''}></td>`:'')
   +`<td><b>${esc(a.id)}</b></td>
     <td>${esc(a.loc)}</td>
     <td><span class="pill" style="background:color-mix(in srgb,
      ${D.stageColors[a.stage]||'#888'} 18%,transparent);
      color:${D.stageColors[a.stage]||'#888'}">${esc(a.stage)}</span></td>
     <td style="color:${c};font-weight:600">${esc(a.task)}</td>
     <td>${dday(a.dday)}</td>
     <td>${esc(a.action)}</td>
     <td>${a.late?`<span class="pill" style="background:rgba(160,32,32,.13);
      color:#a02020">${a.lateDays}일</span>`:''}</td>`;
  if(withChk){
    const cb=tr.querySelector('input');
    cb.onclick=e=>{e.stopPropagation();
      cb.checked?sel.add(a.id):sel.delete(a.id);
      tr.classList.toggle('sel',cb.checked);
      $('#bulk').replaceChildren(bulkBar(sel.size));};
  }
  tr.onclick=()=>pick(a.id);
  return tr;
}

const HEAD=(chk)=>(chk?'<th style="width:28px"></th>':'')
 +'<th>개체</th><th>위치</th><th>단계</th><th>작업</th><th>D-day</th>'
 +'<th>조치</th><th>지연</th>';

function vHome(b){
  const grps=remainByBarn();
  const n=grps.reduce((s,g)=>s+g.items.length,0);
  const log=loadLog();
  b.appendChild(el('div','kpis',
    `<div class="kpi"><b>${n}</b><span>남은 조치</span></div>
     <div class="kpi"><b>${log.filter(x=>x.result==='완료').length}</b><span>완료 기록</span></div>
     <div class="kpi"><b>${D.kpi.nConf}</b><span>모순 경보</span></div>
     <div class="kpi"><b>${D.kpi.nRisk}</b><span>착상기 위험</span></div>`));
  b.appendChild(el('div','prt',
    `<b>작업지시서</b> · 기준일 ${D.today} · 총 ${n}건`));
  if(!grps.length){b.appendChild(el('div','empty','오늘 조치할 개체가 없습니다'));return;}
  grps.forEach(g=>{
    const sup=Object.entries(g.supplies).map(([s,k])=>`${esc(s)}×${k}`).join(' · ');
    const wrap=el('div','bgrp');
    wrap.appendChild(el('div','bgh',
      `<span class="bord">${g.order}</span><b>${esc(g.barn)}</b>
       <span style="color:var(--muted)">${g.items.length}건</span>
       ${g.crit?`<span class="bcrit">시한 ${g.crit}</span>`:''}
       <span class="bsup">준비물 · ${sup||'-'}</span>`));
    const tw=el('div','bwrap');
    const t=el('table',null,'<thead><tr>'+HEAD(true)+'</tr></thead>');
    const tb=el('tbody');
    g.items.forEach(a=>tb.appendChild(rowFor(a,true)));
    t.appendChild(tb); tw.appendChild(t); wrap.appendChild(tw);
    b.appendChild(wrap);
  });
  b.appendChild(el('div','hint',
    '<b>작업동별</b>로 묶었습니다 — 사람은 축사를 하나씩 도니까요. 동 순서는 '
    +'가장 급한 개체가 있는 동부터입니다. 체크해서 <b>여러 건을 한 번에</b> '
    +'완료 처리할 수 있고(축사에서 끝내고 돌아와 한 번에 기록하는 흐름), '
    +'상단 <b>인쇄</b>로 동별 작업지시서를 종이로 뽑을 수 있습니다.<br>'
    +'단축키 <span class="kbd">j</span>/<span class="kbd">k</span> 이동 · '
    +'<span class="kbd">space</span> 선택 · <span class="kbd">/</span> 검색'));
}

function vList(b){
  let rows=D.animals.filter(a=>!q||a.id.includes(q)||a.loc.includes(q)
    ||a.stage.includes(q));
  const dir=sortAsc?1:-1;
  rows.sort((x,y)=>{
    let A=x[sortKey],B=y[sortKey];
    if(A==null)A=''; if(B==null)B='';
    return (A>B?1:A<B?-1:0)*dir;});
  const t=el('table',null,
    `<thead><tr><th data-k="id">개체</th><th data-k="loc">위치</th>
     <th data-k="stage">단계</th><th data-k="parity">산차</th>
     <th data-k="estrus">발정</th><th data-k="preg">임신</th>
     <th data-k="task">작업</th><th data-k="dday">D-day</th></tr></thead>`);
  const tb=el('tbody');
  rows.forEach(a=>{
    const tr=el('tr','r'+(isDone(a)?' done':''));
    tr.dataset.id=a.id;
    tr.innerHTML=`<td><b>${esc(a.id)}</b></td><td>${esc(a.loc)}</td>
      <td><span class="dotc" style="background:${D.statusColors[a.status]}"></span>
       ${esc(a.stage)}</td><td>${a.parity}산</td>
      <td>${esc(a.estrus)} <span style="color:var(--muted)">${a.score.toFixed(2)}</span></td>
      <td>${esc(a.preg)}</td><td>${esc(a.task)}</td><td>${dday(a.dday)}</td>`;
    tr.onclick=()=>pick(a.id);
    tb.appendChild(tr);
  });
  t.appendChild(tb);
  t.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{
    const k=th.dataset.k;
    if(sortKey===k)sortAsc=!sortAsc; else{sortKey=k;sortAsc=true;}
    render();});
  b.appendChild(el('div','dsub',`${rows.length}두 · 열 제목을 눌러 정렬`));
  b.appendChild(t);
}

function vMap(b){
  D.barns.forEach(bn=>{
    const box=el('div','mbarn');
    box.appendChild(el('div','mh',
      `<span>${esc(bn.barn)} ${esc(bn.stage)}</span>`
      +(bn.thi!=null?`<span style="color:${bn.color};font-size:.72rem">
        ${bn.temp}℃ · ${bn.rh}% · THI ${bn.thi} ${esc(bn.level)}</span>`:'')));
    bn.pens.forEach(p=>{
      box.appendChild(el('div','mpen',
        `${esc(p.pen)} · ${esc(p.housing)} (${p.slots.length}/${p.cap})`));
      const row=el('div','mcells');
      p.slots.forEach(s=>{
        const a=byId[s.id]; if(!a)return;
        const i=el('i',null,esc(s.s));
        i.style.background=D.statusColors[a.status];
        if(a.late)i.style.border='2px solid #a02020';
        i.title=`${a.id} · ${a.stage} · ${a.task} ${dday(a.dday)}`;
        i.onclick=()=>pick(a.id);
        row.appendChild(i);
      });
      box.appendChild(row);
    });
    b.appendChild(box);
  });
  const leg=el('div','mleg');
  Object.entries(D.statusColors).forEach(([k,c])=>{if(k==='공실')return;
    leg.appendChild(el('span',null,`<i style="background:${c}"></i>${esc(k)}`));});
  leg.appendChild(el('span',null,'<i style="border:2px solid #a02020"></i>기한 경과'));
  b.appendChild(leg);
}

function vBoard(b){
  const k=D.kpi;
  b.appendChild(el('div','kpis',
    `<div class="kpi"><b>${k.nSows}</b><span>모돈</span></div>
     <div class="kpi"><b>${k.turnover}</b><span>회전율/년</span></div>
     <div class="kpi"><b>${k.svcTarget}</b><span>주간 교배목표</span></div>
     <div class="kpi"><b>${k.nCull}</b><span>도태 후보</span></div>`));
  b.appendChild(el('div','sect','주차별 분만 예정 (17주)'));
  const mx=Math.max(...D.board.map(x=>x.f),k.farrowTarget)||1;
  const ch=el('div','chart');
  D.board.forEach(x=>{
    const c=x.short&&x.locked?'#d03b3b':(x.short?'#e8a33d':'#2a78d6');
    const w=el('div','wk',
      `<div class="wb" style="height:${(96*x.f/mx).toFixed(0)}px;background:${c}"></div>
       <span>${x.f}</span><em>W${x.w}</em>`);
    w.title=`W${x.w} ${md(x.s)}~${md(x.e)} · 분만 ${x.f}복 (목표 ${x.t})`;
    ch.appendChild(w);
  });
  const tl=el('div','tline',`<span>목표 ${k.farrowTarget}</span>`);
  tl.style.bottom=(96*k.farrowTarget/mx).toFixed(0)+'px';
  ch.appendChild(tl); b.appendChild(ch);
  b.appendChild(el('div','sect','산차 구성 (목표 대비)'));
  const t=el('table',null,'<thead><tr><th>산차</th><th>두수</th><th>비율</th>'
    +'<th>목표</th><th>편차</th></tr></thead>');
  const tb=el('tbody');
  D.parity.forEach(p=>tb.appendChild(el('tr',null,
    `<td>${esc(p.p)}산</td><td>${p.n}</td><td>${(p.share*100).toFixed(1)}%</td>
     <td>${(p.target*100).toFixed(0)}%</td>
     <td style="color:${p.gap>3?'#d03b3b':(p.gap<-3?'#e8a33d':'var(--ink2)')}">
      ${p.gap>0?'+':''}${p.gap}</td>`)));
  t.appendChild(tb); b.appendChild(t);
  b.appendChild(el('div','sect','도태 후보'));
  const t2=el('table',null,'<thead><tr><th>개체</th><th>산차</th><th>점수</th>'
    +'<th>사유</th></tr></thead>');
  const tb2=el('tbody');
  D.cull.forEach(c=>{const tr=el('tr','r',
    `<td><b>${esc(c.id)}</b></td><td>${c.parity}산</td><td>${c.score}</td>
     <td>${esc(c.reason)}</td>`);
    tr.onclick=()=>pick(c.id); tb2.appendChild(tr);});
  t2.appendChild(tb2); b.appendChild(t2);
}

function vLog(b){
  const g=loadLog().slice().reverse();
  const done=g.filter(x=>x.result==='완료').length;
  b.appendChild(el('div','kpis',
    `<div class="kpi"><b>${g.length}</b><span>기록</span></div>
     <div class="kpi"><b>${done}</b><span>완료</span></div>
     <div class="kpi"><b>${g.length-done}</b><span>미실시</span></div>`));
  if(!g.length){b.appendChild(el('div','empty',
    '아직 기록이 없습니다. 오늘 할 일에서 완료 처리하면 여기 쌓입니다.'));return;}
  const t=el('table',null,'<thead><tr><th>일시</th><th>개체</th><th>작업</th>'
    +'<th>위치</th><th>예정일</th><th>지연</th><th>결과</th><th>작업자</th></tr></thead>');
  const tb=el('tbody');
  g.forEach(x=>{
    const late=x.planned?Math.round(
      (new Date(x.ts.slice(0,10))-new Date(x.planned))/864e5):null;
    tb.appendChild(el('tr',null,
      `<td>${esc(x.ts.slice(5,16).replace('T',' '))}</td>
       <td><b>${esc(x.id)}</b></td><td>${esc(x.task)}</td>
       <td>${esc(x.loc||'')}</td><td>${esc(x.planned||'-')}</td>
       <td>${late!=null&&late>0?`<span style="color:#a02020">+${late}일</span>`:''}</td>
       <td><span class="pill" style="background:${x.result==='완료'
        ?'color-mix(in srgb,#1baf7a 16%,transparent)':'var(--surf2)'};
        color:${x.result==='완료'?'#1baf7a':'var(--muted)'}">${esc(x.result)}</span></td>
       <td>${esc(x.operator||'')}</td>`));
  });
  t.appendChild(tb); b.appendChild(t);
  const clr=el('button','btn noprint','기록 전체 지우기');
  clr.style.marginTop='12px';
  clr.onclick=()=>{if(confirm('작업 로그를 모두 지웁니다.')){saveLog([]);render();}};
  b.appendChild(clr);
  b.appendChild(el('div','hint',
    '로그는 <b>추가만</b> 합니다 — 기록을 고치면 성적이 왜곡되므로 정정은 취소 '
    +'기록을 덧붙이는 방식입니다. 예정일 대비 지연이 쌓이면 적기 준수율이 되고, '
    +'그것이 수태율의 선행 지표입니다.'));
}

function renderDetail(){
  const d=$('#detail'); d.innerHTML='';
  if(!cur||!byId[cur]){
    d.appendChild(el('div','empty','왼쪽에서 개체를 선택하세요'));return;}
  const a=byId[cur];
  d.appendChild(el('div','dh',esc(a.id)));
  d.appendChild(el('div','dsub',esc(a.loc)));
  if(a.conflict)d.appendChild(el('div','warn','⚠️ '+esc(a.conflict)));
  d.appendChild(el('div','dgrid',
    `<div><span>단계</span><b>${esc(a.stage)}</b></div>
     <div><span>산차</span><b>${a.parity}산</b></div>
     <div><span>발정</span><b>${esc(a.estrus)} (${a.score.toFixed(2)})</b></div>
     <div><span>임신</span><b>${esc(a.preg)}</b></div>
     <div><span>다음 작업</span><b>${esc(a.task)}</b></div>
     <div><span>기한</span><b>${dday(a.dday)}</b></div>`));
  if(!isDone(a)){
    const ok=el('button','btn pri','이 작업 완료'); ok.style.width='100%';
    ok.onclick=()=>{addLog(a,'완료');render();};
    d.appendChild(ok);
  }else d.appendChild(el('div','dsub','✓ 완료 기록됨'));
  d.appendChild(el('div','sect','번식 일정'));
  (D.sched[a.id]||[]).forEach(t=>{
    const dd=dnum(t.d); if(dd<-40||dd>135)return;
    const c=D.taskColors[t.t]||'#888';
    d.appendChild(el('div','tli '+(t.e?'est':''),
      `<span class="dot" style="color:${c}">${t.e?'~':'●'}</span>
       <span class="dt">${md(t.d)}</span><span class="tk">${esc(t.t)}</span>
       <span class="dd">${dd>=0?dday(dd):(-dd)+'일 전'}</span>`));
  });
}

const VIEWS={home:vHome,list:vList,map:vMap,board:vBoard,log:vLog};
const TITLES={home:'오늘 할 일',list:'모돈 목록',map:'축사 도면',
 board:'현황판',log:'작업 로그'};

function render(){
  $('#title').textContent=TITLES[route];
  $$('.nav a').forEach(n=>n.classList.toggle('on',n.dataset.r===route));
  const b=$('#body'); b.innerHTML='';
  (VIEWS[route]||vHome)(b);
  $('#bulk').replaceChildren(route==='home'?bulkBar(sel.size):document.createTextNode(''));
  $('#srch').style.display=route==='list'?'':'none';
  const grps=remainByBarn();
  $('#c-home').textContent=grps.reduce((s,g)=>s+g.items.length,0);
  $('#c-list').textContent=D.animals.length;
  $('#c-log').textContent=loadLog().length;
  renderDetail();
}

$$('.nav a').forEach(n=>n.onclick=()=>go(n.dataset.r));
$('#srch').oninput=e=>{q=e.target.value.trim();render();};
$('#print').onclick=()=>window.print();

document.addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT')  {if(e.key==='Escape')e.target.blur();return;}
  if(e.key==='/'){e.preventDefault();go('list');$('#srch').focus();return;}
  const rows=$$('tr.r'); if(!rows.length)return;
  let i=rows.findIndex(r=>r.dataset.id===cur);
  if(e.key==='j'||e.key==='ArrowDown'){e.preventDefault();
    i=Math.min(rows.length-1,i+1);pick(rows[i].dataset.id);
    rows[i].scrollIntoView({block:'nearest'});}
  else if(e.key==='k'||e.key==='ArrowUp'){e.preventDefault();
    i=Math.max(0,i<0?0:i-1);pick(rows[i].dataset.id);
    rows[i].scrollIntoView({block:'nearest'});}
  else if(e.key===' '&&cur){e.preventDefault();
    sel.has(cur)?sel.delete(cur):sel.add(cur);render();
    const t=$$('tr.r').find(r=>r.dataset.id===cur);
    if(t){t.classList.add('cur');t.scrollIntoView({block:'nearest'});}}
});
render();
"""


def main() -> int:
    D = build_payload()
    data = json.dumps(D, ensure_ascii=False, separators=(",", ":"),
                      allow_nan=False)
    nav = [("home", "☰", "오늘 할 일"), ("list", "☷", "모돈 목록"),
           ("map", "▦", "축사 도면"), ("board", "▤", "현황판"),
           ("log", "✓", "작업 로그")]
    nav_html = "".join(
        f'<a data-r="{r}"><i>{i}</i><b>{n}</b>'
        f'<span class="cnt" id="c-{r}"></span></a>' for r, i, n in nav)

    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>양돈 번식관리 · PC 콘솔</title><style>{CSS}</style></head><body>
<div class="shell">
 <div class="side">
  <div class="brand">🐖 <span>번식관리 콘솔</span></div>
  <div class="nav">{nav_html}</div>
  <div class="sidefoot">기준일 {D["today"]}<br>모돈 {D["kpi"]["nSows"]}두 ·
   {len(D["barns"])}개 동<br>합성 데이터 시연</div>
 </div>
 <div class="main">
  <div class="top">
   <h1 id="title">오늘 할 일</h1>
   <span id="bulk"></span>
   <span class="sp"></span>
   <input class="srch" id="srch" placeholder="개체·위치·단계 검색 ( / )">
   <button class="btn" id="print">🖨 작업지시서 인쇄</button>
  </div>
  <div class="body" id="body"></div>
 </div>
 <div class="detail" id="detail"></div>
</div>
<script>const D={data};{JS}</script>
</body></html>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"PC 콘솔 생성: {OUT} ({os.path.getsize(OUT) // 1024}KB)")
    print(f"  개체 {len(D['animals'])}두 · 화면 5종 · 일괄처리·정렬·인쇄·단축키")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
