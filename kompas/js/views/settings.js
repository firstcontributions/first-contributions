(function (K) {
  'use strict';

  const ui = K.ui;
  const h = ui.h;

  function exportBackup() {
    const blob = new Blob([K.store.exportJSON()], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = h('a', { href: url, download: 'kompas-kopia-' + K.today() + '.json' });
    document.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    ui.toast('Kopia zapisana. Trzymaj ją gdzieś poza przeglądarką.');
  }

  function importBackup(file) {
    const reader = new FileReader();
    reader.onload = function () {
      ui.confirm({
        title: 'Wczytać kopię zapasową?',
        body: 'Obecne dane w przeglądarce zostaną zastąpione tym plikiem.',
        confirmLabel: 'Wczytaj',
        danger: true
      }).then(function (ok) {
        if (!ok) return;
        try {
          K.store.importJSON(String(reader.result));
          ui.toast('Wczytano kopię zapasową.');
        } catch (e) {
          ui.toast('Nie udało się wczytać pliku: ' + e.message);
        }
      });
    };
    reader.onerror = function () { ui.toast('Nie udało się odczytać pliku.'); };
    reader.readAsText(file);
  }

  function stats() {
    const s = K.store.state;
    return [
      [s.decisions.length, 'decyzja', 'decyzje', 'decyzji'],
      [s.thoughts.length, 'wpis w dzienniku', 'wpisy w dzienniku', 'wpisów w dzienniku'],
      [s.problems.length, 'rozłożony problem', 'rozłożone problemy', 'rozłożonych problemów'],
      [s.moods.length, 'dzień z zapisanym nastrojem', 'dni z zapisanym nastrojem', 'dni z zapisanym nastrojem']
    ];
  }

  function render() {
    const settings = K.store.state.settings;

    const fileInput = h('input', {
      type: 'file',
      accept: 'application/json,.json',
      style: { display: 'none' },
      onChange: function (e) {
        const file = e.target.files[0];
        if (file) importBackup(file);
        e.target.value = '';
      }
    });

    const themes = [['auto', 'Jak system'], ['light', 'Jasny'], ['dark', 'Ciemny']];

    return [
      h('div', { class: 'page-head' },
        h('div', null,
          h('h1', { text: 'Ustawienia' }),
          h('p', { class: 'muted', text: 'Twoje dane, Twoje urządzenie.' })
        )
      ),

      ui.card(null,
        ui.sectionTitle('Powitanie'),
        ui.field('Jak mam się do Ciebie zwracać?', ui.input({
          value: settings.name,
          placeholder: 'imię (możesz zostawić puste)',
          onInput: function (value) { settings.name = value; K.store.silent(function () {}); }
        }))
      ),

      ui.card(null,
        ui.sectionTitle('Wygląd'),
        h('div', { class: 'chips' }, themes.map(function (t) {
          return h('button', {
            type: 'button',
            class: 'chip' + (settings.theme === t[0] ? ' on' : ''),
            text: t[1],
            onClick: function () { K.store.update(function () { settings.theme = t[0]; }); }
          });
        }))
      ),

      ui.card(null,
        ui.sectionTitle('Kopia zapasowa', 'Wpisy siedzą w pamięci tej przeglądarki. Wyczyszczenie danych przeglądania albo tryb prywatny je zabierze — dlatego raz na jakiś czas zrób kopię.'),
        h('div', { class: 'row' },
          ui.button('Pobierz kopię', { variant: 'primary', icon: 'note', onClick: exportBackup }),
          ui.button('Wczytaj kopię', { onClick: function () { fileInput.click(); } }),
          fileInput
        ),
        h('hr', { class: 'divider' }),
        h('div', { class: 'stack sm' }, stats().map(function (row) {
          return h('p', { class: 'muted', text: row[0] + ' ' + ui.plural(row[0], row[1], row[2], row[3]) });
        })),
        K.store.persistent ? null : h('div', { class: 'callout warn', text: 'Ta przeglądarka blokuje zapis danych — wpisy znikną po zamknięciu karty. Sprawdź ustawienia prywatności albo tryb prywatny.' })
      ),

      ui.card(null,
        ui.sectionTitle('Czym to jest', null),
        h('p', { class: 'muted', text: 'Kompas to zestaw ćwiczeń, które porządkują myśli: waga decyzyjna, dziennik myśli, rozkładanie problemu, oddech. Nic tu nie ocenia i nic nie wychodzi do internetu — nie ma konta, serwera ani analityki.' }),
        h('div', { class: 'callout warn' },
          h('strong', { text: 'To nie jest terapia ani diagnoza. ' }),
          h('span', { text: 'Aplikacja nie zastąpi kontaktu z psychologiem czy psychiatrą. Jeśli ciężko jest długo albo pojawiają się myśli o zrobieniu sobie krzywdy — zadzwoń:' }),
          h('div', { class: 'stack sm', style: { marginTop: '8px' } }, K.data.helplines.map(function (line) {
            return h('p', { class: 'tiny' }, h('strong', { text: line[0] }), ' — ' + line[1]);
          }))
        )
      ),

      ui.card(null,
        ui.sectionTitle('Strefa czerwona'),
        h('div', { class: 'row' }, ui.button('Usuń wszystkie dane', {
          variant: 'danger',
          icon: 'trash',
          onClick: function () {
            ui.confirm({
              title: 'Usunąć wszystko?',
              body: 'Wszystkie decyzje, wpisy i nastroje znikną bezpowrotnie. Najpierw pobierz kopię, jeśli chcesz je zachować.',
              confirmLabel: 'Usuń wszystko',
              danger: true
            }).then(function (ok) {
              if (!ok) return;
              K.store.reset();
              ui.toast('Wyczyszczone.');
              K.go('pulpit');
            });
          }
        }))
      )
    ];
  }

  K.views = K.views || {};
  K.views.ustawienia = { render: render };
})(window.K = window.K || {});
