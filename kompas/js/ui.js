(function (K) {
  'use strict';

  const ICONS = {
    compass: '<circle cx="12" cy="12" r="9"/><path d="m15.6 8.4-2.1 5.1-5.1 2.1 2.1-5.1z"/>',
    scale: '<path d="M12 4v16M8.5 20h7M4 7.5l8-1.5 8 1.5"/><path d="M4 7.5 1.5 13.5a2.5 2.5 0 0 0 5 0zM20 7.5l-2.5 6a2.5 2.5 0 0 0 5 0z"/>',
    thought: '<path d="M8.5 17.5A4.5 4.5 0 0 1 8 8.6a5 5 0 0 1 9.3-1.3 3.6 3.6 0 0 1-.3 10.2z"/><circle cx="6" cy="20" r="1.2"/>',
    bulb: '<path d="M9.5 18.5h5M10.5 21.5h3"/><path d="M12 2.5a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1.1 1.9h5c.1-.7.5-1.4 1.1-1.9A6 6 0 0 0 12 2.5z"/>',
    mood: '<circle cx="12" cy="12" r="9"/><path d="M8.2 14.2s1.4 1.8 3.8 1.8 3.8-1.8 3.8-1.8"/><path d="M9 9.6v.6M15 9.6v.6"/>',
    check: '<rect x="3" y="4" width="18" height="17" rx="3"/><path d="m8.5 12.5 2.4 2.4 4.6-5"/><path d="M8 2v3M16 2v3"/>',
    wind: '<path d="M3 8.5h11a3 3 0 1 0-3-3M3 12.5h15M3 16.5h8.5a3 3 0 1 1-3 3"/>',
    gear: '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v2.6M12 18.9v2.6M4.3 4.3l1.9 1.9M17.8 17.8l1.9 1.9M2.5 12h2.6M18.9 12h2.6M4.3 19.7l1.9-1.9M17.8 6.2l1.9-1.9"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    trash: '<path d="M4 7h16M10 4h4M6 7l1 13h10l1-13"/><path d="M10 11v6M14 11v6"/>',
    back: '<path d="M15 5l-7 7 7 7"/>',
    close: '<path d="M6 6l12 12M18 6L6 18"/>',
    note: '<path d="M5 4h11l4 4v12H5z"/><path d="M15 4v5h5M8.5 13h7M8.5 16.5h4"/>'
  };

  function icon(name, cls) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('fill', 'none');
    svg.setAttribute('stroke', 'currentColor');
    svg.setAttribute('stroke-width', '1.6');
    svg.setAttribute('stroke-linecap', 'round');
    svg.setAttribute('stroke-linejoin', 'round');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('class', 'icon' + (cls ? ' ' + cls : ''));
    svg.innerHTML = ICONS[name] || '';
    return svg;
  }

  function append(node, kids) {
    kids.forEach(function (child) {
      if (child === null || child === undefined || child === false || child === true) return;
      if (Array.isArray(child)) return append(node, child);
      node.appendChild(child.nodeType ? child : document.createTextNode(String(child)));
    });
  }

  function h(tag, props) {
    const node = document.createElement(tag);
    const kids = Array.prototype.slice.call(arguments, 2);
    if (props) {
      Object.keys(props).forEach(function (key) {
        const value = props[key];
        if (value === null || value === undefined || value === false) return;
        if (key === 'class') node.className = value;
        else if (key === 'text') node.textContent = value;
        else if (key === 'dataset') Object.assign(node.dataset, value);
        else if (key === 'style') Object.assign(node.style, value);
        else if (key === 'value') node.value = value;
        else if (key === 'checked' || key === 'disabled' || key === 'selected') node[key] = !!value;
        else if (key.indexOf('on') === 0 && typeof value === 'function') {
          node.addEventListener(key.slice(2).toLowerCase(), value);
        } else node.setAttribute(key, value === true ? '' : value);
      });
    }
    append(node, kids);
    return node;
  }

  function button(label, opts) {
    const o = opts || {};
    const el = h('button', {
      class: 'btn' + (o.variant ? ' btn-' + o.variant : ''),
      type: 'button',
      onClick: o.onClick,
      title: o.title,
      'aria-label': o.ariaLabel
    }, o.icon ? icon(o.icon) : null, label ? h('span', { text: label }) : null);
    return el;
  }

  function card(props) {
    const kids = Array.prototype.slice.call(arguments, 1);
    return h('section', { class: 'card' + (props && props.class ? ' ' + props.class : '') }, kids);
  }

  function sectionTitle(title, sub) {
    return h('div', { class: 'section-title' },
      h('h2', { text: title }),
      sub ? h('p', { class: 'muted', text: sub }) : null
    );
  }

  function field(label, control, hint) {
    return h('label', { class: 'field' },
      h('span', { class: 'field-label', text: label }),
      control,
      hint ? h('span', { class: 'field-hint', text: hint }) : null
    );
  }

  function autoGrow(el) {
    el.style.height = 'auto';
    el.style.height = Math.max(el.scrollHeight, 44) + 'px';
  }

  function textarea(opts) {
    const o = opts || {};
    const el = h('textarea', {
      class: 'input',
      rows: o.rows || 3,
      placeholder: o.placeholder || '',
      value: o.value || '',
      onInput: function (e) {
        autoGrow(el);
        if (o.onInput) o.onInput(e.target.value);
      }
    });
    requestAnimationFrame(function () { autoGrow(el); });
    return el;
  }

  function input(opts) {
    const o = opts || {};
    return h('input', {
      class: 'input',
      type: o.type || 'text',
      placeholder: o.placeholder || '',
      value: o.value === undefined ? '' : o.value,
      onInput: function (e) { if (o.onInput) o.onInput(e.target.value); }
    });
  }

  function empty(text, actionLabel, onAction) {
    return h('div', { class: 'empty' },
      h('p', { text: text }),
      actionLabel ? button(actionLabel, { variant: 'primary', icon: 'plus', onClick: onAction }) : null
    );
  }

  function toast(message) {
    const node = h('div', { class: 'toast', role: 'status', text: message });
    document.body.appendChild(node);
    requestAnimationFrame(function () { node.classList.add('show'); });
    setTimeout(function () {
      node.classList.remove('show');
      setTimeout(function () { node.remove(); }, 300);
    }, 2600);
  }

  function confirm(opts) {
    return new Promise(function (resolve) {
      function close(result) {
        overlay.remove();
        document.removeEventListener('keydown', onKey);
        resolve(result);
      }
      function onKey(e) { if (e.key === 'Escape') close(false); }

      const dialog = h('div', { class: 'dialog', role: 'dialog', 'aria-modal': 'true' },
        h('h3', { text: opts.title }),
        opts.body ? h('p', { class: 'muted', text: opts.body }) : null,
        h('div', { class: 'dialog-actions' },
          button(opts.cancelLabel || 'Anuluj', { onClick: function () { close(false); } }),
          button(opts.confirmLabel || 'Potwierdź', {
            variant: opts.danger ? 'danger' : 'primary',
            onClick: function () { close(true); }
          })
        )
      );
      const overlay = h('div', { class: 'overlay', onClick: function (e) { if (e.target === overlay) close(false); } }, dialog);
      document.body.appendChild(overlay);
      document.addEventListener('keydown', onKey);
      dialog.querySelector('.btn-primary, .btn-danger, .btn').focus();
    });
  }

  function relativeDate(iso) {
    const day = K.dayKey(iso);
    const diff = K.daysBetween(day, K.today());
    if (diff === 0) return 'dziś';
    if (diff === 1) return 'wczoraj';
    if (diff === 2) return 'przedwczoraj';
    if (diff > 0 && diff < 7) return diff + ' dni temu';
    return new Date(iso).toLocaleDateString('pl-PL', { day: 'numeric', month: 'long', year: 'numeric' });
  }

  function dayLabel(dayKey) {
    return new Date(dayKey + 'T00:00:00').toLocaleDateString('pl-PL', { weekday: 'short', day: 'numeric', month: 'short' });
  }

  function plural(n, one, few, many) {
    const mod10 = n % 10;
    const mod100 = n % 100;
    if (n === 1) return one;
    if (mod10 >= 2 && mod10 <= 4 && (mod100 < 10 || mod100 >= 20)) return few;
    return many;
  }

  K.ui = {
    h: h,
    icon: icon,
    button: button,
    card: card,
    sectionTitle: sectionTitle,
    field: field,
    textarea: textarea,
    input: input,
    empty: empty,
    toast: toast,
    confirm: confirm,
    relativeDate: relativeDate,
    dayLabel: dayLabel,
    plural: plural
  };
})(window.K = window.K || {});
