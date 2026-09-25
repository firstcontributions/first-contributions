(function (K) {
  'use strict';

  const ui = K.ui;
  const h = ui.h;

  function all() { return K.store.state.decisions; }
  function find(id) { return all().filter(function (d) { return d.id === id; })[0]; }

  function isBlank(d) {
    return !d.title.trim() && !d.args.some(function (a) { return a.text.trim(); });
  }

  function score(d) {
    let pro = 0, con = 0;
    d.args.forEach(function (a) {
      if (!a.text.trim()) return;
      if (a.side === 'pro') pro += a.weight; else con += a.weight;
    });
    return { pro: pro, con: con, total: pro + con, diff: pro - con };
  }

  function create() {
    const decision = {
      id: K.uid(),
      ts: new Date().toISOString(),
      title: '',
      args: [
        { id: K.uid(), side: 'pro', text: '', weight: 3 },
        { id: K.uid(), side: 'con', text: '', weight: 3 }
      ],
      friend: '',
      worst: '',
      best: '',
      likely: '',
      status: 'open',
      choice: '',
      decidedAt: null,
      review: null
    };
    // Zapis bez przerysowania listy — inaczej sprzątanie pustych wpisów
    // usunęłoby świeżą decyzję, zanim otworzy się edytor.
    K.store.silent(function (s) { s.decisions.unshift(decision); });
    K.go('decyzje/' + decision.id);
  }

  /* ---------- lista ---------- */

  function renderList() {
    const stale = all().filter(isBlank);
    if (stale.length) {
      K.store.silent(function (s) {
        s.decisions = s.decisions.filter(function (d) { return !isBlank(d); });
      });
    }

    const items = all();
    const nodes = [
      h('div', { class: 'page-head' },
        h('div', null,
          h('h1', { text: 'Waga decyzyjna' }),
          h('p', { class: 'muted', text: 'Wyciągnij decyzję z głowy na papier. Zapisz argumenty, nadaj im wagę i zobacz, jak naprawdę rozkładają się szale.' })
        ),
        ui.button('Nowa decyzja', { variant: 'primary', icon: 'plus', onClick: create })
      )
    ];

    if (!items.length) {
      nodes.push(ui.empty('Nie masz jeszcze żadnej decyzji. Zacznij od tej, która najbardziej krąży Ci po głowie.', 'Dodaj pierwszą decyzję', create));
      return nodes;
    }

    nodes.push(h('div', { class: 'entry-list' }, items.map(function (d) {
      const s = score(d);
      const meta = [ui.relativeDate(d.ts)];
      if (s.total) meta.push('za ' + s.pro + ' : ' + s.con + ' przeciw');

      return h('button', { class: 'entry', onClick: function () { K.go('decyzje/' + d.id); } },
        ui.icon('scale'),
        h('div', { class: 'entry-body' },
          h('span', { class: 'entry-title', text: d.title.trim() || 'Decyzja bez nazwy' }),
          h('span', { class: 'entry-meta' }, meta.map(function (m) { return h('span', { text: m }); }))
        ),
        d.status === 'decided'
          ? h('span', { class: 'badge' + (d.review ? '' : ' warn'), text: d.review ? 'podjęta' : 'do przemyślenia' })
          : null
      );
    })));

    return nodes;
  }

  /* ---------- edytor ---------- */

  function weightPicker(arg, onChange) {
    const box = h('div', { class: 'weight', role: 'group', 'aria-label': 'Waga argumentu' });
    for (let i = 1; i <= 5; i++) {
      (function (value) {
        box.appendChild(h('button', {
          type: 'button',
          class: arg.weight === value ? 'on' : '',
          text: String(value),
          title: 'Waga ' + value + ' z 5',
          onClick: function () {
            arg.weight = value;
            box.querySelectorAll('button').forEach(function (b, idx) {
              b.classList.toggle('on', idx + 1 === value);
            });
            K.store.silent(function () {});
            onChange();
          }
        }));
      })(i);
    }
    return box;
  }

  function argRow(decision, arg, listEl, onChange) {
    const row = h('div', { class: 'arg-row stacked ' + (arg.side === 'pro' ? 'side-pro' : 'side-con') },
      ui.input({
        value: arg.text,
        placeholder: arg.side === 'pro' ? 'Co przemawia za?' : 'Co przemawia przeciw?',
        onInput: function (value) {
          arg.text = value;
          K.store.silent(function () {});
          onChange();
        }
      }),
      h('span', { class: 'tiny', text: 'jak mocno waży?' }),
      weightPicker(arg, onChange),
      ui.button('', {
        variant: 'icon',
        icon: 'trash',
        ariaLabel: 'Usuń argument',
        onClick: function () {
          const index = decision.args.indexOf(arg);
          if (index > -1) decision.args.splice(index, 1);
          K.store.silent(function () {});
          row.remove();
          onChange();
        }
      })
    );
    listEl.appendChild(row);
    return row;
  }

  function column(decision, side, onChange) {
    const listEl = h('div', { class: 'stack sm' });
    decision.args
      .filter(function (a) { return a.side === side; })
      .forEach(function (a) { argRow(decision, a, listEl, onChange); });

    return h('div', { class: 'card flat tight' },
      h('div', { class: 'row between' },
        h('h3', { text: side === 'pro' ? 'Za' : 'Przeciw' }),
        h('span', { class: 'badge ' + (side === 'pro' ? 'pro' : 'con'), text: side === 'pro' ? 'plusy' : 'minusy' })
      ),
      listEl,
      ui.button('Dodaj argument', {
        variant: 'ghost',
        icon: 'plus',
        onClick: function () {
          const arg = { id: K.uid(), side: side, text: '', weight: 3 };
          decision.args.push(arg);
          K.store.silent(function () {});
          const row = argRow(decision, arg, listEl, onChange);
          row.querySelector('input').focus();
          onChange();
        }
      })
    );
  }

  function balance(decision) {
    const box = h('div', { class: 'balance' });

    function paint() {
      const s = score(decision);
      box.textContent = '';

      if (!s.total) {
        box.appendChild(h('p', { class: 'muted', text: 'Wpisz argumenty i nadaj im wagę od 1 do 5 — szale pojawią się tutaj.' }));
        return;
      }

      const proPercent = Math.round((s.pro / s.total) * 100);
      box.appendChild(h('div', { class: 'balance-bar' },
        h('div', { class: 'pro', style: { width: proPercent + '%' }, text: s.pro ? String(s.pro) : '' }),
        h('div', { class: 'con', style: { width: (100 - proPercent) + '%' }, text: s.con ? String(s.con) : '' })
      ));

      let verdict;
      if (s.diff > 0) verdict = 'Szala przechyla się na ZA, o ' + s.diff + ' ' + ui.plural(s.diff, 'punkt', 'punkty', 'punktów') + '.';
      else if (s.diff < 0) verdict = 'Szala przechyla się na PRZECIW, o ' + Math.abs(s.diff) + ' ' + ui.plural(Math.abs(s.diff), 'punkt', 'punkty', 'punktów') + '.';
      else verdict = 'Remis — obie strony ważą dokładnie tyle samo.';

      box.appendChild(h('p', { class: 'verdict', text: verdict }));
      box.appendChild(h('div', { class: 'callout' },
        h('span', { text: 'Sprawdź teraz, co czujesz na widok tego wyniku: ulgę czy opór? Ta reakcja mówi o Twojej decyzji więcej niż same liczby.' })
      ));
    }

    paint();
    box.repaint = paint;
    return box;
  }

  function reflection(decision) {
    const p = K.data.prompts;
    function bind(key) {
      return function (value) {
        decision[key] = value;
        K.store.silent(function () {});
      };
    }
    return ui.card({ class: 'tight' },
      ui.sectionTitle('Zanim zdecydujesz', 'Cztery pytania, które zmieniają perspektywę.'),
      ui.field('Rada dla przyjaciela', ui.textarea({ value: decision.friend, placeholder: p.friend, onInput: bind('friend') })),
      h('div', { class: 'grid-3' },
        ui.field('Najgorszy scenariusz', ui.textarea({ rows: 2, value: decision.worst, placeholder: p.worst, onInput: bind('worst') })),
        ui.field('Najlepszy', ui.textarea({ rows: 2, value: decision.best, placeholder: p.best, onInput: bind('best') })),
        ui.field('Najbardziej prawdopodobny', ui.textarea({ rows: 2, value: decision.likely, placeholder: p.likely, onInput: bind('likely') }))
      )
    );
  }

  function outcome(decision) {
    if (decision.status !== 'decided') {
      const draft = { value: decision.choice || '' };
      return ui.card({ class: 'tight' },
        ui.sectionTitle('Decyzja', 'Kiedy poczujesz, że wiesz — zapisz to. Za kilka dni Kompas przypomni, żebyś sprawdził, jak z tym żyjesz.'),
        ui.textarea({
          rows: 2,
          value: draft.value,
          placeholder: 'Na co się decydujesz?',
          onInput: function (value) {
            draft.value = value;
            decision.choice = value;
            K.store.silent(function () {});
          }
        }),
        h('div', { class: 'row' }, ui.button('Zamykam temat — decyzja podjęta', {
          variant: 'primary',
          onClick: function () {
            if (!draft.value.trim()) {
              ui.toast('Najpierw zapisz, na co się decydujesz.');
              return;
            }
            K.store.update(function () {
              decision.choice = draft.value.trim();
              decision.status = 'decided';
              decision.decidedAt = new Date().toISOString();
            });
          }
        }))
      );
    }

    const daysSince = K.daysBetween(K.dayKey(decision.decidedAt), K.today());
    const kids = [
      ui.sectionTitle('Twoja decyzja', 'Podjęta ' + ui.relativeDate(decision.decidedAt) + '.'),
      h('p', { text: decision.choice })
    ];

    if (decision.review) {
      kids.push(h('hr', { class: 'divider' }));
      kids.push(h('p', { class: 'muted', text: 'Po czasie oceniłeś to na ' + decision.review.rating + '/5.' }));
      if (decision.review.note) kids.push(h('p', { text: decision.review.note }));
    } else if (daysSince >= 3) {
      const note = { value: '' };
      let rating = 4;
      const stars = h('div', { class: 'chips' });
      for (let i = 1; i <= 5; i++) {
        (function (value) {
          stars.appendChild(h('button', {
            class: 'chip' + (value === rating ? ' on' : ''),
            type: 'button',
            text: String(value),
            onClick: function () {
              rating = value;
              stars.querySelectorAll('.chip').forEach(function (c, idx) { c.classList.toggle('on', idx + 1 === value); });
            }
          }));
        })(i);
      }

      kids.push(h('hr', { class: 'divider' }));
      kids.push(ui.sectionTitle('Jak z tym żyjesz?', 'Minęło ' + daysSince + ' ' + ui.plural(daysSince, 'dzień', 'dni', 'dni') + '. Oceń od 1 do 5, jak dziś patrzysz na ten wybór.'));
      kids.push(stars);
      kids.push(ui.textarea({ rows: 2, placeholder: 'Czego się nauczyłeś?', onInput: function (v) { note.value = v; } }));
      kids.push(h('div', { class: 'row' }, ui.button('Zapisz ocenę', {
        variant: 'primary',
        onClick: function () {
          K.store.update(function () {
            decision.review = { ts: new Date().toISOString(), rating: rating, note: note.value.trim() };
          });
          ui.toast('Zapisane. Dobre decyzje poznaje się po czasie.');
        }
      })));
    }

    return ui.card({ class: 'tight' }, kids);
  }

  function renderEditor(decision) {
    const bar = balance(decision);
    const refresh = function () { bar.repaint(); };

    return [
      h('div', { class: 'row between' },
        ui.button('Wszystkie decyzje', { variant: 'ghost', icon: 'back', onClick: function () { K.go('decyzje'); } }),
        ui.button('Usuń', {
          variant: 'ghost',
          icon: 'trash',
          onClick: function () {
            ui.confirm({
              title: 'Usunąć tę decyzję?',
              body: 'Tego nie da się cofnąć.',
              confirmLabel: 'Usuń',
              danger: true
            }).then(function (ok) {
              if (!ok) return;
              K.store.update(function (s) {
                s.decisions = s.decisions.filter(function (d) { return d.id !== decision.id; });
              });
              K.go('decyzje');
            });
          }
        })
      ),
      ui.card(null,
        ui.field('Przed jaką decyzją stoisz?', ui.textarea({
          rows: 2,
          value: decision.title,
          placeholder: 'np. Czy zmienić pracę?',
          onInput: function (value) { decision.title = value; K.store.silent(function () {}); }
        })),
        bar
      ),
      h('div', { class: 'grid-2' },
        column(decision, 'pro', refresh),
        column(decision, 'con', refresh)
      ),
      reflection(decision),
      outcome(decision)
    ];
  }

  K.views = K.views || {};
  K.views.decyzje = {
    render: function (param) {
      const decision = param ? find(param) : null;
      return decision ? renderEditor(decision) : renderList();
    }
  };

  K.decisionScore = score;
})(window.K = window.K || {});
