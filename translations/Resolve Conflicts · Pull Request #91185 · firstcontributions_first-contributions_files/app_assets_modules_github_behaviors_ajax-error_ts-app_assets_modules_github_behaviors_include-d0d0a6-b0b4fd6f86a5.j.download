"use strict";(globalThis.webpackChunk=globalThis.webpackChunk||[]).push([["app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-d0d0a6","ui_packages_soft-navigate_soft-navigate_ts"],{57765:(e,t,r)=>{r.d(t,{a:()=>o,n:()=>i});var n=r(97797);function i(){let e=document.getElementById("ajax-error-message");e&&(e.hidden=!1)}function o(){let e=document.getElementById("ajax-error-message");e&&(e.hidden=!0)}(0,n.on)("deprecatedAjaxError","[data-remote]",function(e){let{error:t,text:r}=e.detail;e.currentTarget===e.target&&"abort"!==t&&"canceled"!==t&&(/<html/.test(r)?(i(),e.stopImmediatePropagation()):setTimeout(function(){e.defaultPrevented||i()},0))}),(0,n.on)("deprecatedAjaxSend","[data-remote]",function(){o()}),(0,n.on)("click",".js-ajax-error-dismiss",function(){o()})},63452:(e,t,r)=>{r.d(t,{A:()=>l,L:()=>s});var n=r(17688),i=r(21403),o=r(97797),a=r(2132);let d=new WeakMap;function l(e){let t=e.closest(".js-render-needs-enrichment");t&&(t.classList.remove("render-error"),d.get(t)?.setLoading(!1))}function s(e,t){let r=e.closest(".js-render-needs-enrichment");return!!r&&(r.classList.add("render-error"),d.get(r)?.setError(!0,t))}function c(e,t,r){let i=r.identifier??"",o=new URL(e,window.location.origin);for(let[e,r]of Object.entries(t))o.searchParams.append(e,`${r}`);return o.hash=i,(0,n.qy)`
    <div
      class="render-container color-bg-transparent js-render-target p-0"
      data-identity="${i}"
      data-host="${o.origin}"
      data-type="${r.type}"
    >
      <iframe
        title="File display"
        role="presentation"
        class="render-viewer"
        src="${String(o)}"
        name="${i}"
        data-content="${r.contentJson}"
        sandbox="allow-scripts allow-same-origin allow-top-navigation allow-popups"
      >
      </iframe>
    </div>
  `}(0,i.lB)(".js-render-needs-enrichment",{constructor:HTMLElement,initialize:function(e){let t={color_mode:(0,a.PT)()},r=e.getAttribute("data-type"),i=e.getAttribute("data-src"),o=e.getAttribute("data-identity"),l=e.getElementsByClassName("js-render-enrichment-target")[0],s=e.getElementsByClassName("js-render-enrichment-loader")[0],u=l.closest("details"),m=document.createElement("div");m.classList.add("js-render-enrichment-fallback"),e.appendChild(m);let f=l.firstElementChild;m.appendChild(f);let h={setLoading(e){s.hidden=!e},setError:(e,t)=>(h.setLoading(!1),!1!==e&&(f.classList.toggle("render-plaintext-hidden",!e),!!t&&((0,n.XX)([t,f],m),!0)))};d.set(e,h);let p=l.getAttribute("data-plain"),g=l.getAttribute("data-json");if(null==g||null==p)throw h.setError(!0,(0,n.qy)`<p class="flash flash-error">Unable to render rich display</p>`),Error(`Expected to see input data for type: ${r}`);let v=c(i,t,{type:r,identifier:o,contentJson:g}),y=c(i,t,{type:r,identifier:`${o}-fullscreen`,contentJson:g}),b=function(e,t,r){let i=(0,n.qy)`<clipboard-copy
    aria-label="Copy ${r.type} code"
    .value=${e}
    class="btn my-2 js-clipboard-copy p-0 d-inline-flex tooltipped-no-delay"
    role="button"
    data-copy-feedback="Copied!"
    data-tooltip-direction="s"
  >
    <svg
      aria-hidden="true"
      height="16"
      viewBox="0 0 16 16"
      version="1.1"
      width="16"
      class="octicon octicon-copy js-clipboard-copy-icon m-2"
    >
      <path
        fill-rule="evenodd"
        d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"
      ></path>
      <path
        fill-rule="evenodd"
        d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"
      ></path>
    </svg>
    <svg
      aria-hidden="true"
      height="16"
      viewBox="0 0 16 16"
      version="1.1"
      width="16"
      class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2"
    >
      <path
        fill-rule="evenodd"
        d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"
      ></path>
    </svg>
  </clipboard-copy>`,o=(0,n.qy)`
    <details class="details-reset details-overlay details-overlay-dark" style="display: contents">
      <summary
        role="button"
        aria-label="Open dialog"
        class="btn my-2 mr-2 p-0 d-inline-flex"
        aria-haspopup="dialog"
        @click="${t}"
      >
        <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" class="octicon m-2">
          <path
            fill-rule="evenodd"
            d="M3.72 3.72a.75.75 0 011.06 1.06L2.56 7h10.88l-2.22-2.22a.75.75 0 011.06-1.06l3.5 3.5a.75.75 0 010 1.06l-3.5 3.5a.75.75 0 11-1.06-1.06l2.22-2.22H2.56l2.22 2.22a.75.75 0 11-1.06 1.06l-3.5-3.5a.75.75 0 010-1.06l3.5-3.5z"
          ></path>
        </svg>
      </summary>
      <details-dialog
        class="Box Box--overlay render-full-screen d-flex flex-column anim-fade-in fast"
        aria-label="${r.type} rendered container"
      >
        <div>
          <button
            aria-label="Close dialog"
            data-close-dialog=""
            type="button"
            data-view-component="true"
            class="Link--muted btn-link position-absolute render-full-screen-close"
          >
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="currentColor"
              style="display:inline-block;vertical-align:text-bottom"
              class="octicon octicon-x"
            >
              <path
                fill-rule="evenodd"
                d="M5.72 5.72a.75.75 0 011.06 0L12 10.94l5.22-5.22a.75.75 0 111.06 1.06L13.06 12l5.22 5.22a.75.75 0 11-1.06 1.06L12 13.06l-5.22 5.22a.75.75 0 01-1.06-1.06L10.94 12 5.72 6.78a.75.75 0 010-1.06z"
              ></path>
            </svg>
          </button>
          <div class="Box-body border-0" role="presentation"></div>
        </div>
      </details-dialog>
    </details>
  `;return(0,n.qy)`<div class="position-absolute top-0 pr-2 right-0 d-flex flex-justify-end flex-items-center">
    ${o}${i}
  </div>`}(p,()=>{(0,n.XX)(y,l.getElementsByClassName("Box-body")[0])},{type:r});u&&!u.open?u.ontoggle=()=>{u.open&&((0,n.XX)([b,v],l),u.ontoggle=null)}:(0,n.XX)([b,v],l)}}),(0,o.on)("preview:toggle:off",".js-previewable-comment-form",function(e){let t=e.currentTarget.querySelector(".js-render-needs-enrichment"),r=t?.querySelector(".js-render-enrichment-target");r&&(r.textContent="")}),(0,o.on)("preview:rendered",".js-previewable-comment-form",function(e){let t=e.currentTarget.querySelector(".js-render-needs-enrichment");t&&d.get(t)?.setLoading(!1)})},23711:(e,t,r)=>{r.d(t,{d:()=>c,s:()=>s});var n=r(79024),i=r(21403),o=r(97797);function a(e,t){let r=e.currentTarget;if(r instanceof Element){for(let e of r.querySelectorAll("[data-show-on-error]"))e instanceof HTMLElement&&(e.hidden=!t);for(let e of r.querySelectorAll("[data-hide-on-error]"))e instanceof HTMLElement&&(e.hidden=t)}}function d(e){a(e,!1)}function l(e){a(e,!0)}function s({currentTarget:e}){e instanceof Element&&c(e)}function c(e){let t=e.closest("details");t&&function(e){let t=e.getAttribute("data-deferred-details-content-url");if(t){e.removeAttribute("data-deferred-details-content-url");let r=e.querySelector("include-fragment, poll-include-fragment");r&&(r.src=t)}}(t)}(0,i.lB)("include-fragment, poll-include-fragment",{subscribe:e=>(0,n.Zz)((0,n.Rt)(e,"error",l),(0,n.Rt)(e,"loadstart",d))}),(0,o.on)("click","include-fragment button[data-retry-button]",({currentTarget:e})=>{e.closest("include-fragment").refetch()})},14152:(e,t,r)=>{r.d(t,{Qs:()=>y,hq:()=>l,zr:()=>b});var n=r(17688),i=r(63452),o=r(21403),a=r(66748),d=r(97564);function l(e){return!!e.querySelector('.js-render-target[data-type="ipynb"]')}let s=["is-render-pending","is-render-ready","is-render-loading","is-render-loaded"],c=["is-render-ready","is-render-loading","is-render-loaded","is-render-failed","is-render-failed-fatally"],u=new WeakMap;function m(e){let t=u.get(e);null!=t&&(t.load=t.hello=null,t.helloTimer&&(clearTimeout(t.helloTimer),t.helloTimer=null),t.loadTimer&&(clearTimeout(t.loadTimer),t.loadTimer=null))}let f=(0,d.G7)("viewscreen_post_message");function h(e,t=""){e.classList.remove(...s),e.classList.add("is-render-failed");let r=function(e){let t=(0,n.qy)`<p>Unable to render rich display</p>`;if(""!==e){let r=e.split("\n");t=(0,n.qy)`<p><b>Unable to render rich display</b></p>
      <p>${r.map(e=>(0,n.qy)`${e}<br />`)}</p>`}return(0,n.qy)`<div class="flash flash-error">${t}</div>`}(t);!1===(0,i.L)(e,r)&&function(e,t){let r=e.querySelector(".render-viewer-error");r&&(r.remove(),e.classList.remove("render-container"),(0,n.XX)(t,e))}(e,r),m(e)}function p(e,t=!1){!(!e||!(0,a.A)(e)||e.classList.contains("is-render-ready")||e.classList.contains("is-render-failed")||e.classList.contains("is-render-failed-fatally"))&&(!t||u.get(e)?.hello)&&h(e)}function g(e,t,r){return!!e&&!!e.postMessage&&(e.postMessage(JSON.stringify(t),f?r:"*"),!0)}function v(e){return t=>{if(!t.querySelector(".js-render-target"))return;let r=t.querySelector("iframe"),n=r?.contentWindow;if(n)return e(n)}}(0,o.lB)(".js-render-target",function(e){e.classList.remove(...c),e.style.height="auto",!u.get(e)?.load&&(m(e),u.get(e)||(u.set(e,{load:Date.now(),hello:null,helloTimer:window.setTimeout(p,1e4,e,!0),loadTimer:window.setTimeout(p,45e3,e)}),e.classList.add("is-render-automatic","is-render-requested")))}),window.addEventListener("message",function(e){let t=e.data;if(!t)return;if("string"==typeof t)try{t=JSON.parse(t)}catch{return}if("object"!=typeof t&&void 0!=t||"render"!==t.type||"string"!=typeof t.identity)return;let r=t.identity;if("string"!=typeof t.body)return;let n=t.body,o=function(e,t){for(let r of e.querySelectorAll(".js-render-target[data-identity][data-host]"))if(r.getAttribute("data-identity")===t)return r;return null}(document,r);if(!o||e.origin!==o.getAttribute("data-host"))return;let a=e.origin,d=null!=t.payload?t.payload:void 0,l=o.querySelector("iframe"),c=l?.contentWindow;switch(n){case"hello":if((u.get(o)||{untimed:!0}).hello=Date.now(),!c)return;g(c,{type:"render:cmd",body:{cmd:"ack",ack:!0}},a),g(c,{type:"render:cmd",body:{cmd:"branding",branding:!1}},a);break;case"error":h(o,d?.error);break;case"error:fatal":h(o,d?.error),o.classList.add("is-render-failed-fatal");break;case"error:invalid":h(o,d?.error),o.classList.add("is-render-failed-invalid");break;case"loading":o.classList.remove(...s),o.classList.add("is-render-loading");break;case"loaded":o.classList.remove(...s),o.classList.add("is-render-loaded");break;case"ready":(0,i.A)(o),o.classList.remove(...s),o.classList.add("is-render-ready"),d&&"number"==typeof d.height&&(o.style.height=`${d.height}px`,""!==location.hash&&window.dispatchEvent(new HashChangeEvent("hashchange"))),d?.ack===!0&&window.requestAnimationFrame(()=>{setTimeout(()=>{g(c,{type:"render:cmd",body:{cmd:"code_rendering_service:ready:ack","code_rendering_service:ready:ack":{}}},a)},0)});break;case"resize":d&&"number"==typeof d.height&&(o.style.height=`${d.height}px`);break;case"code_rendering_service:container:get_size":g(c,{type:"render:cmd",body:{cmd:"code_rendering_service:container:size","code_rendering_service:container:size":{width:o?.getBoundingClientRect().width}}},a);break;case"code_rendering_service:markdown:get_data":if(!c)return;!function(){let e;let t=l?.getAttribute("data-content")??"";try{e=JSON.parse(t)?.data}catch{e=null}e&&g(c,{type:"render:cmd",body:{cmd:"code_rendering_service:data:ready","code_rendering_service:data:ready":{data:e,width:o?.getBoundingClientRect().width}}},a)}()}});let y=v(e=>g(e,{type:"render:cmd",body:{cmd:"code_rendering_service:behaviour:expand_all"}},origin)),b=v(e=>g(e,{type:"render:cmd",body:{cmd:"code_rendering_service:behaviour:collapse_all"}},origin))},2132:(e,t,r)=>{r.d(t,{OQ:()=>a,PA:()=>l,PT:()=>u,Px:()=>s,to:()=>c});var n=r(5728),i=r(73480);function o(){(0,i.TV)("preferred_color_mode",a())}function a(){return d("dark")?"dark":d("light")?"light":void 0}function d(e){return window.matchMedia&&window.matchMedia(`(prefers-color-scheme: ${e})`).matches}function l(e){let t=document.querySelector("html[data-color-mode]");t&&t.setAttribute("data-color-mode",e)}function s(e,t){let r=document.querySelector("html[data-color-mode]");r&&r.setAttribute(`data-${t}-theme`,e)}function c(e){let t=document.querySelector("html[data-color-mode]");if(t)return t.getAttribute(`data-${e}-theme`)}function u(e="light"){let t=function(){let e=document.querySelector("html[data-color-mode]");if(e)return e.getAttribute("data-color-mode")}();return("auto"===t?a():t)??e}(async()=>{if(await n.G,o(),window.matchMedia){let e=window.matchMedia("(prefers-color-scheme: dark)");e?.addEventListener?e.addEventListener("change",o):e.addListener(o)}})()},7572:(e,t,r)=>{r.d(t,{C:()=>a,i:()=>d});var n=r(97156),i=r(97564),o=r(46493);function a(e,t){(0,i.G7)("arianotify_comprehensive_migration")?d(l(e),{...t,element:t?.element??e}):(0,i.G7)("primer_live_region_element")&&t?.element===void 0?(0,o.Cj)(e,{politeness:t?.assertive?"assertive":"polite"}):d(l(e),t)}function d(e,t){let{assertive:r,element:a}=t??{};(0,i.G7)("arianotify_comprehensive_migration")&&"ariaNotify"in Element.prototype?(a||document.body).ariaNotify(e,{interrupt:t?.assertive?"all":"none"}):(0,i.G7)("primer_live_region_element")&&void 0===a?(0,o.iP)(e,{politeness:r?"assertive":"polite"}):function(e,t,r){let i=r??n.XC?.querySelector(t?"#js-global-screen-reader-notice-assertive":"#js-global-screen-reader-notice");i&&(i.textContent===e?i.textContent=`${e}\u00A0`:i.textContent=e)}(e,r,a)}function l(e){return(e.getAttribute("aria-label")||e.innerText||"").trim()}},73480:(e,t,r)=>{function n(e){return i(e)[0]}function i(e){let t=[];for(let r of function(){try{return document.cookie.split(";")}catch{return[]}}()){let[n,i]=r.trim().split("=");e===n&&void 0!==i&&t.push({key:n,value:i})}return t}function o(e,t,r=null,n=!1,i="lax"){let o=document.domain;if(null==o)throw Error("Unable to get document domain");o.endsWith(".github.com")&&(o="github.com");let a="https:"===location.protocol?"; secure":"",d=r?`; expires=${r}`:"";!1===n&&(o=`.${o}`);try{document.cookie=`${e}=${t}; path=/; domain=${o}${d}${a}; samesite=${i}`}catch{}}function a(e,t=!1){let r=document.domain;if(null==r)throw Error("Unable to get document domain");r.endsWith(".github.com")&&(r="github.com");let n=new Date(Date.now()-1).toUTCString(),i="https:"===location.protocol?"; secure":"",o=`; expires=${n}`;!1===t&&(r=`.${r}`);try{document.cookie=`${e}=''; path=/; domain=${r}${o}${i}`}catch{}}r.d(t,{OR:()=>i,Ri:()=>n,TV:()=>o,Yj:()=>a})},18558:(e,t,r)=>{r.d(t,{JC:()=>n.JC,KK:()=>n.KK,SK:()=>o,Vy:()=>n.Vy,ai:()=>n.ai,oc:()=>n.oc,rd:()=>n.rd});var n=r(50515);let i=/(?:^|,)((?:[^,]|,(?=\+| |$))*(?:,(?=,))?)/g;function o(e){return Array.from(e.matchAll(i)).map(([,e])=>e)}},67327:(e,t,r)=>{r.d(t,{Kq:()=>SoftNavErrorEvent,RQ:()=>SoftNavEndEvent,ni:()=>SoftNavSuccessEvent,sW:()=>SoftNavStartEvent});var n=r(27260);let i=class SoftNavEvent extends Event{constructor(e,t){super(t),this.mechanism=e}};let SoftNavStartEvent=class SoftNavStartEvent extends i{constructor(e){super(e,n.z.START)}};let SoftNavSuccessEvent=class SoftNavSuccessEvent extends i{constructor(e,t){super(e,n.z.SUCCESS),this.visitCount=t}};let SoftNavErrorEvent=class SoftNavErrorEvent extends i{constructor(e,t){super(e,n.z.ERROR),this.error=t}};let SoftNavEndEvent=class SoftNavEndEvent extends i{constructor(e){super(e,n.z.END)}}},56725:(e,t,r)=>{r.d(t,{Bu:()=>h,SC:()=>s,Ti:()=>m,iS:()=>c,k5:()=>l,o4:()=>u,rZ:()=>f});var n=r(27260),i=r(67327),o=r(47175),a=r(54861);let d=0;function l(){d=0,document.dispatchEvent(new Event(n.z.INITIAL)),(0,a.xT)()}function s(e){(0,a.LM)()||(document.dispatchEvent(new Event(n.z.PROGRESS_BAR.START)),document.dispatchEvent(new i.sW(e)),(0,a.Vy)(e),(0,a.ZW)(),(0,a.HK)(),(0,o.E5)())}function c(e={}){g(e)&&(d+=1,document.dispatchEvent(new i.ni((0,a.di)(),d)),m(e))}function u(e={}){if(!g(e))return;d=0;let t=(0,a.my)()||a.BW;document.dispatchEvent(new i.Kq((0,a.di)(),t)),p(),(0,o.Cd)(t),(0,a.xT)()}function m(e={}){if(!g(e))return;let t=(0,a.di)();p(),document.dispatchEvent(new i.RQ(t)),(0,a.Ff)(),(0,a.JA)(t)}function f(e={}){g(e)&&((0,o.Im)(),document.dispatchEvent(new Event(n.z.RENDER)))}function h(){document.dispatchEvent(new Event(n.z.FRAME_UPDATE))}function p(){document.dispatchEvent(new Event(n.z.PROGRESS_BAR.END))}function g({skipIfGoingToReactApp:e,allowedMechanisms:t=[]}={}){return(0,a.LM)()&&(0===t.length||t.includes((0,a.di)()))&&(!e||!(0,a.gc)())}},47175:(e,t,r)=>{r.d(t,{Cd:()=>l,E5:()=>d,Im:()=>s,nW:()=>a});var n=r(51528),i=r(54861);let o="stats:soft-nav-duration",a={turbo:"TURBO",react:"REACT","turbo.frame":"FRAME",ui:"UI",hard:"HARD"};function d(){performance.clearResourceTimings(),performance.mark(o)}function l(e){(0,n.i)({turboFailureReason:e,turboStartUrl:(0,i.dR)(),turboEndUrl:window.location.href})}function s(){let e=function(){if(0===performance.getEntriesByName(o).length)return null;performance.measure(o,o);let e=performance.getEntriesByName(o).pop();return e?e.duration:null}();if(!e)return;let t=a[(0,i.di)()],r=Math.round(e);t===a.react&&document.dispatchEvent(new CustomEvent("staffbar-update",{detail:{duration:r}})),(0,n.i)({requestUrl:window.location.href,softNavigationTiming:{mechanism:t,destination:(0,i.fX)()||"rails",duration:r,initiator:(0,i.Pv)()||"rails"}})}},63120:(e,t,r)=>{r.d(t,{softNavigate:()=>o});var n=r(56725),i=r(7332);let o=(e,t)=>{(0,n.SC)("turbo"),(0,i.YR)(e,{...t})}},79024:(e,t,r)=>{r.d(t,{Rt:()=>n,Zz:()=>i,yU:()=>Subscription});let Subscription=class Subscription{constructor(e){this.closed=!1,this.unsubscribe=()=>{e(),this.closed=!0}}};function n(e,t,r,n={capture:!1}){return e.addEventListener(t,r,n),new Subscription(()=>{e.removeEventListener(t,r,n)})}function i(...e){return new Subscription(()=>{for(let t of e)t.unsubscribe()})}},66748:(e,t,r)=>{r.d(t,{A:()=>n});function n(e){return!(e.offsetWidth<=0&&e.offsetHeight<=0)}}}]);
//# sourceMappingURL=app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-d0d0a6-bd940022099d.js.map