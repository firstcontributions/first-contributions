(function (K) {
  'use strict';

  const ui = K.ui;
  const h = ui.h;

  function forDay(day) {
    return K.store.state.moods.filter(function (m) { return m.day === day; })[0] || null;
  }

  function levelOf(score) {
    return K.data.moodLevels[score - 1];
  }

  function setScore(day, score) {
    K.store.update(function (s) {
      const existing = s.moods.filter(function (m) { return m.day === day; })[0];
      if (existing) {
        existing.score = score;
        existing.ts = new Date().toISOString();
      } else {
        s.moods.unshift({ id: K.uid(), day: day, ts: new Date().toISOString(), score: score, emotions: [], note: '' });
      }
    });
  }

  function picker(day, entry) {
    return h('div', { class: 'mood-picker' }, K.data.moodLevels.map(function (level) {
      return h('button', {
        type: 'button',
        class: 'mood-btn' + (entry && entry.score === level.score ? ' on' : ''),
        onClick: function () { setScore(day, level.score); },
        'aria-pressed': entry && entry.score === level.score ? 'true' : 'false'
      },
        h('span', { class: 'dot', style: { background: level.color } }),
        h('span', { text: level.label })
      );
    }));
  }

  function details(entry) {
    return h('div', { class: 'stack sm' },
      h('div', { class: 'chips' }, [].concat(K.data.emotions['Trudne'], K.data.emotions['Dobre']).map(function (name) {
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
      })),
      ui.textarea({
        rows: 2,
        value: entry.note,
        placeholder: 'Co dziś na Ciebie wpłynęło? Jedno zdanie wystarczy.',
        onInput: function (value) { entry.note = value; K.store.silent(function () {}); }
      })
    );
  }

  function chart(days) {
    const bars = [];
    let day = K.shiftDay(K.today(), -(days - 1));
    for (let i = 0; i < days; i++) {
      const entry = forDay(day);
      const level = entry ? levelOf(entry.score) : null;
      bars.push(h('div', {
        class: 'bar',
        title: ui.dayLabel(day) + (entry ? ' — ' + level.label : ' — brak wpisu')
      }, entry ? h('span', { style: { height: (entry.score / 5 * 100) + '%', background: level.color } }) : null));
      day = K.shiftDay(day, 1);
    }
    return h('div', { class: 'mood-chart' }, bars);
  }

  function average(days) {
    const from = K.shiftDay(K.today(), -(days - 1));
    const picked = K.store.state.moods.filter(function (m) { return m.day >= from; });
    if (!picked.length) return null;
    const sum = picked.reduce(function (acc, m) { return acc + m.score; }, 0);
    return Math.round((sum / picked.length) * 10) / 10;
  }

  function render() {
    const day = K.today();
    const entry = forDay(day);
    const avg = average(30);
    const moods = K.store.state.moods.slice().sort(function (a, b) { return a.day < b.day ? 1 : -1; });

    const nodes = [
      h('div', { class: 'page-head' },
        h('div', null,
          h('h1', { text: 'Nastrój' }),
          h('p', { class: 'muted', text: 'Jeden klik dziennie. Po miesiącu zobaczysz to, czego pamięć nie pokaże: że złe dni mijają.' })
        )
      ),
      ui.card(null,
        ui.sectionTitle('Jak jest dzisiaj?'),
        picker(day, entry),
        entry ? details(entry) : null
      )
    ];

    if (moods.length) {
      nodes.push(ui.card(null,
        ui.sectionTitle('Ostatnie 30 dni', avg !== null ? 'Średnia: ' + avg + ' na 5.' : null),
        chart(30)
      ));

      nodes.push(ui.card(null,
        ui.sectionTitle('Historia'),
        h('div', { class: 'entry-list' }, moods.slice(0, 60).map(function (m) {
          const level = levelOf(m.score);
          return h('div', { class: 'entry', style: { cursor: 'default' } },
            h('span', { class: 'dot', style: { background: level.color, width: '14px', height: '14px', borderRadius: '50%', marginTop: '5px', flex: 'none' } }),
            h('div', { class: 'entry-body' },
              h('span', { class: 'entry-title', text: ui.dayLabel(m.day) + ' — ' + level.label.toLowerCase() }),
              m.emotions.length ? h('span', { class: 'entry-meta' }, h('span', { text: m.emotions.join(', ') })) : null,
              m.note.trim() ? h('span', { class: 'muted', text: m.note }) : null
            )
          );
        }))
      ));
    }

    return nodes;
  }

  K.views = K.views || {};
  K.views.nastroj = { render: render };

  K.mood = { forDay: forDay, setScore: setScore, picker: picker, levelOf: levelOf, average: average };
})(window.K = window.K || {});
