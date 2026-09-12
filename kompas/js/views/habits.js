(function (K) {
  'use strict';

  const ui = K.ui;
  const h = ui.h;

  function streak(habit) {
    let day = K.today();
    if (!habit.log[day]) day = K.shiftDay(day, -1);
    let count = 0;
    while (habit.log[day]) {
      count++;
      day = K.shiftDay(day, -1);
    }
    return count;
  }

  function lastDays(n) {
    const days = [];
    let day = K.shiftDay(K.today(), -(n - 1));
    for (let i = 0; i < n; i++) {
      days.push(day);
      day = K.shiftDay(day, 1);
    }
    return days;
  }

  function toggle(habit, day) {
    K.store.update(function () {
      if (habit.log[day]) delete habit.log[day];
      else habit.log[day] = true;
    });
  }

  function weekStrip(habit) {
    const today = K.today();
    return h('div', { class: 'week' }, lastDays(7).map(function (day) {
      const label = new Date(day + 'T00:00:00').toLocaleDateString('pl-PL', { weekday: 'narrow' });
      return h('button', {
        type: 'button',
        class: 'day-dot' + (habit.log[day] ? ' done' : '') + (day === today ? ' today' : ''),
        text: label,
        title: ui.dayLabel(day),
        onClick: function () { toggle(habit, day); }
      });
    }));
  }

  function render() {
    const habits = K.store.state.habits;

    const input = ui.input({ placeholder: 'np. 10 minut spaceru' });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') add();
    });

    function add() {
      const name = input.value.trim();
      if (!name) return;
      K.store.update(function (s) {
        s.habits.push({ id: K.uid(), name: name, createdAt: new Date().toISOString(), log: {} });
      });
    }

    const nodes = [
      h('div', { class: 'page-head' },
        h('div', null,
          h('h1', { text: 'Małe kroki' }),
          h('p', { class: 'muted', text: 'Nie chodzi o dyscyplinę, tylko o dowody. Każdy odhaczony dzień to dowód, że potrafisz.' })
        )
      ),
      ui.card({ class: 'tight' },
        ui.sectionTitle('Nowy krok', 'Im mniejszy, tym lepiej — ma być łatwiejszy do zrobienia niż do odpuszczenia.'),
        h('div', { class: 'row' },
          h('div', { style: { flex: '1', minWidth: '200px' } }, input),
          ui.button('Dodaj', { variant: 'primary', icon: 'plus', onClick: add })
        )
      )
    ];

    if (!habits.length) {
      nodes.push(ui.empty('Brak kroków. Zacznij od jednego, naprawdę małego.'));
      return nodes;
    }

    nodes.push(h('div', { class: 'stack sm' }, habits.map(function (habit) {
      const s = streak(habit);
      return h('div', { class: 'habit' },
        h('div', { class: 'habit-name' },
          h('strong', { text: habit.name }),
          h('span', { class: 'tiny', text: s ? 'seria: ' + s + ' ' + ui.plural(s, 'dzień', 'dni', 'dni') : 'jeszcze nie zaczęta' })
        ),
        weekStrip(habit),
        ui.button('', {
          variant: 'icon',
          icon: 'trash',
          ariaLabel: 'Usuń krok',
          onClick: function () {
            ui.confirm({
              title: 'Usunąć „' + habit.name + '"?',
              body: 'Historia odhaczonych dni też zniknie.',
              confirmLabel: 'Usuń',
              danger: true
            }).then(function (ok) {
              if (!ok) return;
              K.store.update(function (state) {
                state.habits = state.habits.filter(function (x) { return x.id !== habit.id; });
              });
            });
          }
        })
      );
    })));

    return nodes;
  }

  K.views = K.views || {};
  K.views.nawyki = { render: render };
  K.habitStreak = streak;
})(window.K = window.K || {});
