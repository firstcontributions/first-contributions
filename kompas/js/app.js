(function (K) {
  'use strict';

  const h = K.ui.h;
  const icon = K.ui.icon;
  const DEFAULT_ROUTE = 'pulpit';

  let current = null;
  let mainEl = null;
  let navEl = null;

  function parseHash() {
    const raw = location.hash.replace(/^#\/?/, '');
    const parts = raw.split('/').filter(Boolean);
    const id = parts[0] && K.views[parts[0]] ? parts[0] : DEFAULT_ROUTE;
    return { id: id, param: parts[1] || null };
  }

  function applyTheme() {
    const theme = K.store.state.settings.theme || 'auto';
    if (theme === 'auto') document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', theme);
  }

  function buildSidebar() {
    navEl = h('nav', { class: 'nav' }, K.data.nav.map(function (item) {
      return h('a', { href: '#/' + item.id, dataset: { route: item.id } },
        icon(item.icon), h('span', { text: item.label }));
    }));

    return h('aside', { class: 'sidebar' },
      h('div', { class: 'brand' },
        h('div', { class: 'mark' }, icon('compass')),
        h('div', null,
          h('strong', { text: 'Kompas' }),
          h('span', { class: 'tiny', text: 'twoja prywatna przestrzeń' })
        )
      ),
      navEl,
      h('div', { class: 'sidebar-foot' },
        h('p', { class: 'tiny', text: 'Wszystko zostaje na tym urządzeniu. Nic nie wychodzi do sieci.' })
      )
    );
  }

  function markActive(id) {
    navEl.querySelectorAll('a').forEach(function (a) {
      a.classList.toggle('active', a.dataset.route === id);
    });
  }

  function render() {
    const route = parseHash();
    const view = K.views[route.id];

    if (current && current.view.destroy && (current.id !== route.id || current.param !== route.param)) {
      current.view.destroy();
    }

    const scrollTop = current && current.id === route.id ? window.scrollY : 0;
    current = { id: route.id, param: route.param, view: view };

    mainEl.textContent = '';
    mainEl.appendChild(h('div', { class: 'main-inner fade-in' }, view.render(route.param)));
    markActive(route.id);
    window.scrollTo(0, scrollTop);
  }

  function boot() {
    applyTheme();
    mainEl = h('main', { class: 'main' });
    const app = document.getElementById('app');
    app.appendChild(buildSidebar());
    app.appendChild(mainEl);

    window.addEventListener('hashchange', render);
    K.store.onChange(function () {
      applyTheme();
      render();
    });

    if (!location.hash) location.hash = '#/' + DEFAULT_ROUTE;
    render();

    if (!K.store.persistent) {
      K.ui.toast('Uwaga: przeglądarka blokuje zapis danych. Wpisy nie przetrwają zamknięcia karty.');
    }
  }

  K.go = function (path) { location.hash = '#/' + path; };
  K.refresh = render;

  // Offline działa tylko na http(s); z pliku na dysku nie ma czego rejestrować.
  if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('sw.js').catch(function () {});
    });
  }

  document.addEventListener('DOMContentLoaded', boot);
})(window.K = window.K || {});
