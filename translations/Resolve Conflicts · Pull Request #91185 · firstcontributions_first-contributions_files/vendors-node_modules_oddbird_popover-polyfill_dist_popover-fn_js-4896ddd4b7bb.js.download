"use strict";(globalThis.webpackChunk=globalThis.webpackChunk||[]).push([["vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js"],{913:(e,t,o)=>{o.d(t,{Bb:()=>N,TT:()=>H});var n=class extends Event{oldState;newState;constructor(e,{oldState:t="",newState:o="",...n}={}){super(e,n),this.oldState=String(t||""),this.newState=String(o||"")}},r=new WeakMap;function i(e,t,o){r.set(e,setTimeout(()=>{r.has(e)&&e.dispatchEvent(new n("toggle",{cancelable:!1,oldState:t,newState:o}))},0))}var l=globalThis.ShadowRoot||function(){},a=globalThis.HTMLDialogElement||function(){},p=new WeakMap,u=new WeakMap,s=new WeakMap;function c(e){return s.get(e)||"hidden"}var f=new WeakMap;function d(e,t){return!("auto"!==e.popover&&"manual"!==e.popover||!e.isConnected||t&&"showing"!==c(e)||!t&&"hidden"!==c(e)||e instanceof a&&e.hasAttribute("open"))&&document.fullscreenElement!==e}function h(e){return e?Array.from(u.get(e.ownerDocument)||[]).indexOf(e)+1:0}function g(e){let t=u.get(e);for(let e of t||[]){if(e.isConnected)return e;t.delete(e)}return null}function m(e){return"function"==typeof e.getRootNode?e.getRootNode():e.parentNode?m(e.parentNode):e}function v(e){for(;e;){if(e instanceof HTMLElement&&"auto"===e.popover&&"showing"===s.get(e))return e;if((e=e instanceof Element&&e.assignedSlot||e.parentElement||m(e))instanceof l&&(e=e.host),e instanceof Document)return}}var w=new WeakMap;function b(e){if(!d(e,!1))return;let t=e.ownerDocument;if(!e.dispatchEvent(new n("beforetoggle",{cancelable:!0,oldState:"closed",newState:"open"}))||!d(e,!1))return;let o=!1;if("auto"===e.popover){let o=e.getAttribute("popover");if(T(function(e){let t=new Map,o=0;for(let n of u.get(e.ownerDocument)||[])t.set(n,o),o+=1;t.set(e,o),o+=1;let n=null;return function(e){let o=v(e);if(null===o)return;let r=t.get(o);(null===n||t.get(n)<r)&&(n=o)}(e.parentElement||m(e)),n}(e)||t,!1,!0),o!==e.getAttribute("popover")||!d(e,!1))return}g(t)||(o=!0),w.delete(e);let r=t.activeElement;e.classList.add(":popover-open"),s.set(e,"showing"),p.has(t)||p.set(t,new Set),p.get(t).add(e),(function(e){if(e.shadowRoot&&!0!==e.shadowRoot.delegatesFocus)return null;let t=e;t.shadowRoot&&(t=t.shadowRoot);let o=t.querySelector("[autofocus]");if(o)return o;for(let e of t.querySelectorAll("slot"))for(let t of e.assignedElements({flatten:!0})){if(t.hasAttribute("autofocus"))return t;if(o=t.querySelector("[autofocus]"))return o}let n=e.ownerDocument.createTreeWalker(t,NodeFilter.SHOW_ELEMENT),r=n.currentNode;for(;r;){var i;if(!((i=r).hidden||i instanceof l||(i instanceof HTMLButtonElement||i instanceof HTMLInputElement||i instanceof HTMLSelectElement||i instanceof HTMLTextAreaElement||i instanceof HTMLOptGroupElement||i instanceof HTMLOptionElement||i instanceof HTMLFieldSetElement)&&i.disabled||i instanceof HTMLInputElement&&"hidden"===i.type||i instanceof HTMLAnchorElement&&""===i.href)&&"number"==typeof i.tabIndex&&-1!==i.tabIndex)return r;r=n.nextNode()}})(e)?.focus(),"auto"===e.popover&&(u.has(t)||u.set(t,new Set),u.get(t).add(e),A(f.get(e),!0)),o&&r&&"auto"===e.popover&&w.set(e,r),i(e,"closed","open")}function E(e,t=!1,o=!1){if(!d(e,!0))return;let r=e.ownerDocument;if("auto"===e.popover&&(T(e,t,o),!d(e,!0))||(A(f.get(e),!1),f.delete(e),o&&(e.dispatchEvent(new n("beforetoggle",{oldState:"open",newState:"closed"})),!d(e,!0))))return;p.get(r)?.delete(e),u.get(r)?.delete(e),e.classList.remove(":popover-open"),s.set(e,"hidden"),o&&i(e,"open","closed");let l=w.get(e);l&&(w.delete(e),t&&l.focus())}function y(e,t=!1,o=!1){let n=g(e);for(;n;)E(n,t,o),n=g(e)}function T(e,t,o){let n=e.ownerDocument||e;if(e instanceof Document)return y(n,t,o);let r=null,i=!1;for(let t of u.get(n)||[])if(t===e)i=!0;else if(i){r=t;break}if(!i)return y(n,t,o);for(;r&&"showing"===c(r)&&u.get(n)?.size;)E(r,t,o)}var S=new WeakMap;function M(e){if(!e.isTrusted)return;let t=e.composedPath()[0];if(!t)return;let o=t.ownerDocument;if(!g(o))return;let n=function(e){let t=v(e),o=function(e){for(;e;){let t=e.popoverTargetElement;if(t instanceof HTMLElement)return t;if((e=e.parentElement||m(e))instanceof l&&(e=e.host),e instanceof Document)return}}(e);return h(t)>h(o)?t:o}(t);if(n&&"pointerdown"===e.type)S.set(o,n);else if("pointerup"===e.type){let e=S.get(o)===n;S.delete(o),e&&T(n||o,!1,!0)}}var L=new WeakMap;function A(e,t=!1){if(!e)return;L.has(e)||L.set(e,e.getAttribute("aria-expanded"));let o=e.popoverTargetElement;if(o instanceof HTMLElement&&"auto"===o.popover)e.setAttribute("aria-expanded",String(t));else{let t=L.get(e);t?e.setAttribute("aria-expanded",t):e.removeAttribute("aria-expanded")}}var k=globalThis.ShadowRoot||function(){};function H(){return"undefined"!=typeof HTMLElement&&"object"==typeof HTMLElement.prototype&&"popover"in HTMLElement.prototype}function D(e,t,o){let n=e[t];Object.defineProperty(e,t,{value(e){return n.call(this,o(e))}})}var x=/(^|[^\\]):popover-open\b/g,R=null;function C(e){let t=function(){let e="function"==typeof globalThis.CSSLayerBlockRule;return`
${e?"@layer popover-polyfill {":""}
  :where([popover]) {
    position: fixed;
    z-index: 2147483647;
    inset: 0;
    padding: 0.25em;
    width: fit-content;
    height: fit-content;
    border-width: initial;
    border-color: initial;
    border-image: initial;
    border-style: solid;
    background-color: canvas;
    color: canvastext;
    overflow: auto;
    margin: auto;
  }

  :where([popover]:not(.\\:popover-open)) {
    display: none;
  }

  :where(dialog[popover].\\:popover-open) {
    display: block;
  }

  :where(dialog[popover][open]) {
    display: revert;
  }

  :where([anchor].\\:popover-open) {
    inset: auto;
  }

  :where([anchor]:popover-open) {
    inset: auto;
  }

  @supports not (background-color: canvas) {
    :where([popover]) {
      background-color: white;
      color: black;
    }
  }

  @supports (width: -moz-fit-content) {
    :where([popover]) {
      width: -moz-fit-content;
      height: -moz-fit-content;
    }
  }

  @supports not (inset: 0) {
    :where([popover]) {
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
    }
  }
${e?"}":""}
`}();if(null===R)try{(R=new CSSStyleSheet).replaceSync(t)}catch{R=!1}if(!1===R){let o=document.createElement("style");o.textContent=t,e instanceof Document?e.head.prepend(o):e.prepend(o)}else e.adoptedStyleSheets=[R,...e.adoptedStyleSheets]}function N(){var e;if("undefined"==typeof window)return;function t(e){return e?.includes(":popover-open")&&(e=e.replace(x,"$1.\\:popover-open")),e}window.ToggleEvent=window.ToggleEvent||n,D(Document.prototype,"querySelector",t),D(Document.prototype,"querySelectorAll",t),D(Element.prototype,"querySelector",t),D(Element.prototype,"querySelectorAll",t),D(Element.prototype,"matches",t),D(Element.prototype,"closest",t),D(DocumentFragment.prototype,"querySelectorAll",t),Object.defineProperties(HTMLElement.prototype,{popover:{enumerable:!0,configurable:!0,get(){if(!this.hasAttribute("popover"))return null;let e=(this.getAttribute("popover")||"").toLowerCase();return""===e||"auto"==e?"auto":"manual"},set(e){this.setAttribute("popover",e)}},showPopover:{enumerable:!0,configurable:!0,value(){b(this)}},hidePopover:{enumerable:!0,configurable:!0,value(){E(this,!0,!0)}},togglePopover:{enumerable:!0,configurable:!0,value(e){"showing"===s.get(this)&&void 0===e||!1===e?E(this,!0,!0):(void 0===e||!0===e)&&b(this)}}});let o=Element.prototype.attachShadow;o&&Object.defineProperties(Element.prototype,{attachShadow:{enumerable:!0,configurable:!0,writable:!0,value(e){let t=o.call(this,e);return C(t),t}}});let r=HTMLElement.prototype.attachInternals;r&&Object.defineProperties(HTMLElement.prototype,{attachInternals:{enumerable:!0,configurable:!0,writable:!0,value(){let e=r.call(this);return e.shadowRoot&&C(e.shadowRoot),e}}});let i=new WeakMap;function l(e){Object.defineProperties(e.prototype,{popoverTargetElement:{enumerable:!0,configurable:!0,set(e){if(null===e)this.removeAttribute("popovertarget"),i.delete(this);else if(e instanceof Element)this.setAttribute("popovertarget",""),i.set(this,e);else throw TypeError("popoverTargetElement must be an element or null")},get(){if("button"!==this.localName&&"input"!==this.localName||"input"===this.localName&&"reset"!==this.type&&"image"!==this.type&&"button"!==this.type||this.disabled||this.form&&"submit"===this.type)return null;let e=i.get(this);if(e&&e.isConnected)return e;if(e&&!e.isConnected)return i.delete(this),null;let t=m(this),o=this.getAttribute("popovertarget");return(t instanceof Document||t instanceof k)&&o&&t.getElementById(o)||null}},popoverTargetAction:{enumerable:!0,configurable:!0,get(){let e=(this.getAttribute("popovertargetaction")||"").toLowerCase();return"show"===e||"hide"===e?e:"toggle"},set(e){this.setAttribute("popovertargetaction",e)}}})}l(HTMLButtonElement),l(HTMLInputElement),(e=document).addEventListener("click",e=>{let t=e.composedPath(),o=t[0];if(!(o instanceof Element)||o?.shadowRoot)return;let n=m(o);if(!(n instanceof k||n instanceof Document))return;let r=t.find(e=>e.matches?.("[popovertargetaction],[popovertarget]"));if(r){(function(e){let t=e.popoverTargetElement;if(!(t instanceof HTMLElement))return;let o=c(t);("show"!==e.popoverTargetAction||"showing"!==o)&&("hide"!==e.popoverTargetAction||"hidden"!==o)&&("showing"===o?E(t,!0,!0):d(t,!1)&&(f.set(t,e),b(t)))})(r),e.preventDefault();return}}),e.addEventListener("keydown",e=>{let t=e.key,o=e.target;!e.defaultPrevented&&o&&("Escape"===t||"Esc"===t)&&T(o.ownerDocument,!0,!0)}),e.addEventListener("pointerdown",M),e.addEventListener("pointerup",M),C(document)}}}]);
//# sourceMappingURL=vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-69f2eb65ecc6.js.map