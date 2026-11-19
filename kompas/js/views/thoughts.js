(function (K) {
  'use strict';

  const ui = K.ui;
  const h = ui.h;

  function all() { return K.store.state.thoughts; }
  function find(id) { return all().filter(function (t) { return t.id === id; })[0]; }

  function isBlank(t) {
    return !t.situation.trim() && !t.thought.trim() && !t.balanced.trim();
  }

  function create() {
    const entry = {
      id: K.uid(),
      ts: new Date().toISOString(),
      situation: '',
      emotions: [],
      intensityBefore: 70,
      thought: '',
      distortions: [],
      evidenceFor: '',
      evidenceAgainst: '',
      balanced: '',
      intensityAfter: null
    };
    K.store.silent(function (s) { s.thoughts.unshift(entry); });
    K.go('mysli/' + entry.id);
  }

  /* ---------- lista ---------- */

  function renderList() {
    if (all().some(isBlank)) {
      K.store.silent(function (s) {
        s.thoughts = s.thoughts.filter(function (t) { return !isBlank(t); });
      });
    }

    const items = all();
    const nodes = [
      h('div', { class: 'page-head' },
        h('div', null,
          h('h1', { text: 'Dziennik myśli' }),
          h('p', { class: 'muted', text: 'Myśl to nie fakt. Rozbierz ją na części: co się wydarzyło, co sobie powiedziałeś i co na to dowody.' })
        ),
        ui.button('Nowy wpis', { variant: 'primary', icon: 'plus', onClick: create })
      )
    ];

    if (!items.length) {
      nodes.push(ui.empty('Pusto. Następnym razem, gdy coś Cię mocno ruszy, wróć tutaj i zapisz to na świeżo.', 'Zapisz pierwszą myśl', create));
      return nodes;
    }

    nodes.push(h('div', { class: 'entry-list' }, items.map(function (t) {
      const drop = t.intensityAfter !== null ? t.intensityBefore - t.intensityAfter : null;
      return h('button', { class: 'entry', onClick: function () { K.go('mysli/' + t.id); } },
        ui.icon('thought'),
        h('div', { class: 'entry-body' },
          h('span', { class: 'entry-title', text: t.thought.trim() || t.situation.trim() || 'Wpis bez treści' }),
          h('span', { class: 'entry-meta' },
            h('span', { text: ui.relativeDate(t.ts) }),
            t.emotions.length ? h('span', { text: t.emotions.slice(0, 3).join(', ') }) : null
          )
        ),
        drop !== null && drop > 0 ? h('span', { class: 'badge pro', text: '-' + drop + ' pkt' }) : null
      );
    })));

    return nodes;
  }

  /* ---------- elementy formularza ---------- */

  function emotionPicker(entry) {
    const box = h('div', { class: 'stack sm' });
    Object.keys(K.data.emotions).forEach(function (group) {
      box.appendChild(h('div', { class: 'chips' }, K.data.emotions[group].map(function (name) {
        return h('button', {
          type: 'button',
          class: 'chip' + (entry.emotions.indexOf(name) > -1 ? ' on' : ''),
          text: name,
          onClick: function (e) {
            const index = entry.emotions.indexOf(name);
            if (index > -1) entry.emotions.splice(index, 1);
            else entry.emotions.push(name);
            e.currentTarget.classList.toggle('on', index === -1);
            K.store.silent(function () {});
          }
        });
      })));
    });
    return box;
  }

  function intensitySlider(value, onChange) {
    const label = h('strong', { text: value + '%' });
    const slider = h('input', {
      type: 'range',
      min: '0',
      max: '100',
      step: '5',
      value: String(value),
      class: 'range',
      onInput: function (e) {
        const v = Number(e.target.value);
        label.textContent = v + '%';
        onChange(v);
      }
    });
    return h('div', { class: 'stack sm' }, slider, h('span', { class: 'muted' }, 'Siła: ', label));
  }

  function distortionPicker(entry) {
    const notes = h('div', { class: 'stack sm' });

    function paintNotes() {
      notes.textContent = '';
      K.data.distortions
        .filter(function (d) { return entry.distortions.indexOf(d[0]) > -1; })
        .forEach(function (d) {
          notes.appendChild(h('div', { class: 'callout' },
            h('strong', { text: d[0] + ': ' }),
            h('span', { text: d[1] })
          ));
        });
    }

    const chips = h('div', { class: 'chips' }, K.data.distortions.map(function (d) {
      return h('button', {
        type: 'button',
        class: 'chip' + (entry.distortions.indexOf(d[0]) > -1 ? ' on' : ''),
        text: d[0],
        title: d[1],
        onClick: function (e) {
          const index = entry.distortions.indexOf(d[0]);
          if (index > -1) entry.distortions.splice(index, 1);
          else entry.distortions.push(d[0]);
          e.currentTarget.classList.toggle('on', index === -1);
          K.store.silent(function () {});
          paintNotes();
        }
      });
    }));

    paintNotes();
    return h('div', { class: 'stack sm' }, chips, notes);
  }

  /* ---------- edytor ---------- */

  function renderEditor(entry) {
    const p = K.data.prompts;
    function bind(key) {
      return function (value) { entry[key] = value; K.store.silent(function () {}); };
    }

    const afterBox = h('div', { class: 'stack sm' });

    function paintAfter() {
      afterBox.textContent = '';
      if (entry.intensityAfter === null) {
        afterBox.appendChild(h('div', { class: 'row' }, ui.button('Sprawdź, ile w tym zostało', {
          onClick: function () {
            K.store.update(function () { entry.intensityAfter = entry.intensityBefore; });
          }
        })));
        return;
      }
      const summary = h('p', { class: 'verdict' });
      function paintSummary() {
        const d = entry.intensityBefore - entry.intensityAfter;
        summary.textContent = d > 0
          ? 'Spadek o ' + d + ' punktów. Tyle zrobiło samo nazwanie i sprawdzenie tej myśli.'
          : (d === 0 ? 'Na razie bez zmiany — i to też jest w porządku. Czasem trzeba wrócić do tego jutro.' : 'Wzrost o ' + Math.abs(d) + ' punktów. Może pod spodem jest jeszcze inna myśl?');
      }
      afterBox.appendChild(intensitySlider(entry.intensityAfter, function (v) {
        entry.intensityAfter = v;
        K.store.silent(function () {});
        paintSummary();
      }));
      afterBox.appendChild(summary);
      paintSummary();
    }

    paintAfter();

    return [
      h('div', { class: 'row between' },
        ui.button('Wszystkie wpisy', { variant: 'ghost', icon: 'back', onClick: function () { K.go('mysli'); } }),
        ui.button('Usuń', {
          variant: 'ghost',
          icon: 'trash',
          onClick: function () {
            ui.confirm({ title: 'Usunąć ten wpis?', confirmLabel: 'Usuń', danger: true }).then(function (ok) {
              if (!ok) return;
              K.store.update(function (s) {
                s.thoughts = s.thoughts.filter(function (t) { return t.id !== entry.id; });
              });
              K.go('mysli');
            });
          }
        })
      ),

      ui.card(null,
        ui.sectionTitle('1. Sytuacja', 'Fakty, nie oceny.'),
        ui.textarea({ value: entry.situation, placeholder: p.situation, onInput: bind('situation') })
      ),

      ui.card(null,
        ui.sectionTitle('2. Co poczułeś?'),
        emotionPicker(entry),
        intensitySlider(entry.intensityBefore, function (v) { entry.intensityBefore = v; K.store.silent(function () {}); })
      ),

      ui.card(null,
        ui.sectionTitle('3. Myśl automatyczna', 'Zdanie, które pojawiło się samo.'),
        ui.textarea({ value: entry.thought, placeholder: p.thought, onInput: bind('thought') })
      ),

      ui.card(null,
        ui.sectionTitle('4. Pułapki myślenia', 'Zaznacz te, które rozpoznajesz w swojej myśli.'),
        distortionPicker(entry)
      ),

      ui.card(null,
        ui.sectionTitle('5. Fakty', 'Sąd, nie kłótnia — obie strony dostają głos.'),
        h('div', { class: 'grid-2' },
          ui.field('Dowody za', ui.textarea({ value: entry.evidenceFor, placeholder: p.evidenceFor, onInput: bind('evidenceFor') })),
          ui.field('Dowody przeciw', ui.textarea({ value: entry.evidenceAgainst, placeholder: p.evidenceAgainst, onInput: bind('evidenceAgainst') }))
        )
      ),

      ui.card(null,
        ui.sectionTitle('6. Myśl zrównoważona', 'Nie na siłę pozytywna — po prostu prawdziwsza.'),
        ui.textarea({ value: entry.balanced, placeholder: p.balanced, onInput: bind('balanced') })
      ),

      ui.card(null,
        ui.sectionTitle('7. I jak teraz?', 'Wróć do emocji z punktu 2.'),
        afterBox
      )
    ];
  }

  K.views = K.views || {};
  K.views.mysli = {
    render: function (param) {
      const entry = param ? find(param) : null;
      return entry ? renderEditor(entry) : renderList();
    }
  };
})(window.K = window.K || {});
