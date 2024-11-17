"use strict";(globalThis.webpackChunk=globalThis.webpackChunk||[]).push([["vendors-node_modules_oddbird_popover-polyfill_dist_popover_js"],{59136:()=>{var e=class extends Event{oldState;newState;constructor(e,{oldState:t="",newState:o="",...n}={}){super(e,n),this.oldState=String(t||""),this.newState=String(o||"")}},t=new WeakMap;function o(o,n,r){t.set(o,setTimeout(()=>{t.has(o)&&o.dispatchEvent(new e("toggle",{cancelable:!1,oldState:n,newState:r}))},0))}var n=globalThis.ShadowRoot||function(){},r=globalThis.HTMLDialogElement||function(){},i=new WeakMap,l=new WeakMap,a=new WeakMap;function p(e){return a.get(e)||"hidden"}var u=new WeakMap;function s(e,t){return!("auto"!==e.popover&&"manual"!==e.popover||!e.isConnected||t&&"showing"!==p(e)||!t&&"hidden"!==p(e)||e instanceof r&&e.hasAttribute("open"))&&document.fullscreenElement!==e}function c(e){return e?Array.from(l.get(e.ownerDocument)||[]).indexOf(e)+1:0}function f(e){let t=l.get(e);for(let e of t||[]){if(e.isConnected)return e;t.delete(e)}return null}function d(e){return"function"==typeof e.getRootNode?e.getRootNode():e.parentNode?d(e.parentNode):e}function h(e){for(;e;){if(e instanceof HTMLElement&&"auto"===e.popover&&"showing"===a.get(e))return e;if((e=e instanceof Element&&e.assignedSlot||e.parentElement||d(e))instanceof n&&(e=e.host),e instanceof Document)return}}var g=new WeakMap;function m(t){if(!s(t,!1))return;let r=t.ownerDocument;if(!t.dispatchEvent(new e("beforetoggle",{cancelable:!0,oldState:"closed",newState:"open"}))||!s(t,!1))return;let p=!1;if("auto"===t.popover){let e=t.getAttribute("popover");if(b(function(e){let t=new Map,o=0;for(let n of l.get(e.ownerDocument)||[])t.set(n,o),o+=1;t.set(e,o),o+=1;let n=null;return function(e){let o=h(e);if(null===o)return;let r=t.get(o);(null===n||t.get(n)<r)&&(n=o)}(e.parentElement||d(e)),n}(t)||r,!1,!0),e!==t.getAttribute("popover")||!s(t,!1))return}f(r)||(p=!0),g.delete(t);let c=r.activeElement;t.classList.add(":popover-open"),a.set(t,"showing"),i.has(r)||i.set(r,new Set),i.get(r).add(t),(function(e){if(e.shadowRoot&&!0!==e.shadowRoot.delegatesFocus)return null;let t=e;t.shadowRoot&&(t=t.shadowRoot);let o=t.querySelector("[autofocus]");if(o)return o;for(let e of t.querySelectorAll("slot"))for(let t of e.assignedElements({flatten:!0})){if(t.hasAttribute("autofocus"))return t;if(o=t.querySelector("[autofocus]"))return o}let r=e.ownerDocument.createTreeWalker(t,NodeFilter.SHOW_ELEMENT),i=r.currentNode;for(;i;){var l;if(!((l=i).hidden||l instanceof n||(l instanceof HTMLButtonElement||l instanceof HTMLInputElement||l instanceof HTMLSelectElement||l instanceof HTMLTextAreaElement||l instanceof HTMLOptGroupElement||l instanceof HTMLOptionElement||l instanceof HTMLFieldSetElement)&&l.disabled||l instanceof HTMLInputElement&&"hidden"===l.type||l instanceof HTMLAnchorElement&&""===l.href)&&"number"==typeof l.tabIndex&&-1!==l.tabIndex)return i;i=r.nextNode()}})(t)?.focus(),"auto"===t.popover&&(l.has(r)||l.set(r,new Set),l.get(r).add(t),S(u.get(t),!0)),p&&c&&"auto"===t.popover&&g.set(t,c),o(t,"closed","open")}function v(t,n=!1,r=!1){if(!s(t,!0))return;let p=t.ownerDocument;if("auto"===t.popover&&(b(t,n,r),!s(t,!0))||(S(u.get(t),!1),u.delete(t),r&&(t.dispatchEvent(new e("beforetoggle",{oldState:"open",newState:"closed"})),!s(t,!0))))return;i.get(p)?.delete(t),l.get(p)?.delete(t),t.classList.remove(":popover-open"),a.set(t,"hidden"),r&&o(t,"open","closed");let c=g.get(t);c&&(g.delete(t),n&&c.focus())}function w(e,t=!1,o=!1){let n=f(e);for(;n;)v(n,t,o),n=f(e)}function b(e,t,o){let n=e.ownerDocument||e;if(e instanceof Document)return w(n,t,o);let r=null,i=!1;for(let t of l.get(n)||[])if(t===e)i=!0;else if(i){r=t;break}if(!i)return w(n,t,o);for(;r&&"showing"===p(r)&&l.get(n)?.size;)v(r,t,o)}var E=new WeakMap;function y(e){if(!e.isTrusted)return;let t=e.composedPath()[0];if(!t)return;let o=t.ownerDocument;if(!f(o))return;let r=function(e){let t=h(e),o=function(e){for(;e;){let t=e.popoverTargetElement;if(t instanceof HTMLElement)return t;if((e=e.parentElement||d(e))instanceof n&&(e=e.host),e instanceof Document)return}}(e);return c(t)>c(o)?t:o}(t);if(r&&"pointerdown"===e.type)E.set(o,r);else if("pointerup"===e.type){let e=E.get(o)===r;E.delete(o),e&&b(r||o,!1,!0)}}var T=new WeakMap;function S(e,t=!1){if(!e)return;T.has(e)||T.set(e,e.getAttribute("aria-expanded"));let o=e.popoverTargetElement;if(o instanceof HTMLElement&&"auto"===o.popover)e.setAttribute("aria-expanded",String(t));else{let t=T.get(e);t?e.setAttribute("aria-expanded",t):e.removeAttribute("aria-expanded")}}var M=globalThis.ShadowRoot||function(){};function L(e,t,o){let n=e[t];Object.defineProperty(e,t,{value(e){return n.call(this,o(e))}})}var A=/(^|[^\\]):popover-open\b/g,k=null;function H(e){let t=function(){let e="function"==typeof globalThis.CSSLayerBlockRule;return`
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
`}();if(null===k)try{(k=new CSSStyleSheet).replaceSync(t)}catch{k=!1}if(!1===k){let o=document.createElement("style");o.textContent=t,e instanceof Document?e.head.prepend(o):e.prepend(o)}else e.adoptedStyleSheets=[k,...e.adoptedStyleSheets]}"undefined"!=typeof HTMLElement&&"object"==typeof HTMLElement.prototype&&"popover"in HTMLElement.prototype||function(){var t;if("undefined"==typeof window)return;function o(e){return e?.includes(":popover-open")&&(e=e.replace(A,"$1.\\:popover-open")),e}window.ToggleEvent=window.ToggleEvent||e,L(Document.prototype,"querySelector",o),L(Document.prototype,"querySelectorAll",o),L(Element.prototype,"querySelector",o),L(Element.prototype,"querySelectorAll",o),L(Element.prototype,"matches",o),L(Element.prototype,"closest",o),L(DocumentFragment.prototype,"querySelectorAll",o),Object.defineProperties(HTMLElement.prototype,{popover:{enumerable:!0,configurable:!0,get(){if(!this.hasAttribute("popover"))return null;let e=(this.getAttribute("popover")||"").toLowerCase();return""===e||"auto"==e?"auto":"manual"},set(e){this.setAttribute("popover",e)}},showPopover:{enumerable:!0,configurable:!0,value(){m(this)}},hidePopover:{enumerable:!0,configurable:!0,value(){v(this,!0,!0)}},togglePopover:{enumerable:!0,configurable:!0,value(e){"showing"===a.get(this)&&void 0===e||!1===e?v(this,!0,!0):(void 0===e||!0===e)&&m(this)}}});let n=Element.prototype.attachShadow;n&&Object.defineProperties(Element.prototype,{attachShadow:{enumerable:!0,configurable:!0,writable:!0,value(e){let t=n.call(this,e);return H(t),t}}});let r=HTMLElement.prototype.attachInternals;r&&Object.defineProperties(HTMLElement.prototype,{attachInternals:{enumerable:!0,configurable:!0,writable:!0,value(){let e=r.call(this);return e.shadowRoot&&H(e.shadowRoot),e}}});let i=new WeakMap;function l(e){Object.defineProperties(e.prototype,{popoverTargetElement:{enumerable:!0,configurable:!0,set(e){if(null===e)this.removeAttribute("popovertarget"),i.delete(this);else if(e instanceof Element)this.setAttribute("popovertarget",""),i.set(this,e);else throw TypeError("popoverTargetElement must be an element or null")},get(){if("button"!==this.localName&&"input"!==this.localName||"input"===this.localName&&"reset"!==this.type&&"image"!==this.type&&"button"!==this.type||this.disabled||this.form&&"submit"===this.type)return null;let e=i.get(this);if(e&&e.isConnected)return e;if(e&&!e.isConnected)return i.delete(this),null;let t=d(this),o=this.getAttribute("popovertarget");return(t instanceof Document||t instanceof M)&&o&&t.getElementById(o)||null}},popoverTargetAction:{enumerable:!0,configurable:!0,get(){let e=(this.getAttribute("popovertargetaction")||"").toLowerCase();return"show"===e||"hide"===e?e:"toggle"},set(e){this.setAttribute("popovertargetaction",e)}}})}l(HTMLButtonElement),l(HTMLInputElement),(t=document).addEventListener("click",e=>{let t=e.composedPath(),o=t[0];if(!(o instanceof Element)||o?.shadowRoot)return;let n=d(o);if(!(n instanceof M||n instanceof Document))return;let r=t.find(e=>e.matches?.("[popovertargetaction],[popovertarget]"));if(r){(function(e){let t=e.popoverTargetElement;if(!(t instanceof HTMLElement))return;let o=p(t);("show"!==e.popoverTargetAction||"showing"!==o)&&("hide"!==e.popoverTargetAction||"hidden"!==o)&&("showing"===o?v(t,!0,!0):s(t,!1)&&(u.set(t,e),m(t)))})(r),e.preventDefault();return}}),t.addEventListener("keydown",e=>{let t=e.key,o=e.target;!e.defaultPrevented&&o&&("Escape"===t||"Esc"===t)&&b(o.ownerDocument,!0,!0)}),t.addEventListener("pointerdown",y),t.addEventListener("pointerup",y),H(document)}()}}]);
//# sourceMappingURL=vendors-node_modules_oddbird_popover-polyfill_dist_popover_js-ceaa757e974e.js.map