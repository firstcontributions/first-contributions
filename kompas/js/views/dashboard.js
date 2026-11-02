(function (K) {
  'use strict';

  const ui = K.ui;
  const h = ui.h;

  function greeting() {
    const hour = new Date().getHours();
    if (hour < 5) return 'Jeszcze nie śpisz';
    if (hour < 11) return 'Dzień dobry';
    if (hour < 18) return 'Cześć';
    return 'Dobry wieczór';
  }

  function activeDays() {
    const s = K.store.state;
    const days = {};
    s.moods.forEach(function (m) { days[m.day] = true; });
    [s.decisions, s.thoughts, s.problems, s.calmLog].forEach(function (list) {
      list.forEach(function (item) { days[K.dayKey(item.ts)] = true; });
    });
    return days;
  }

  function streak() {
    const days = activeDays();
    let day = K.today();
    if (!days[day]) day = K.shiftDay(day, -1);
    let count = 0;
    while (days[day]) {
      count++;
      day = K.shiftDay(day, -1);
    }
    return count;
  }

  function pendingReviews() {
    return K.store.state.decisions.filter(function (d) {
      return d.status === 'decided' && !d.review && K.daysBetween(K.dayKey(d.decidedAt), K.today()) >= 3;
    });
  }

  function openSteps() {
    return K.store.state.problems.filter(function (p) {
      return !p.done && p.step.trim();
    });
  }

  function tile(route, iconName, title, text) {
    return h('button', {
      class: 'entry',
      onClick: function () { K.go(route); }
    },
      ui.icon(iconName),
      h('div', { class: 'entry-body' },
        h('span', { class: 'entry-title', text: title }),
        h('span', { class: 'muted', text: text })
      )
    );
  }

  function feed() {
    const s = K.store.state;
    const items = []
      .concat(s.decisions.map(function (d) {
        return { ts: d.ts, route: 'decyzje/' + d.id, icon: 'scale', label: d.title.trim() || 'Decyzja bez nazwy', kind: 'waga decyzyjna' };
      }))
      .concat(s.thoughts.map(function (t) {
        return { ts: t.ts, route: 'mysli/' + t.id, icon: 'thought', label: t.thought.trim() || t.situation.trim() || 'Wpis', kind: 'dziennik myśli' };
      }))
      .concat(s.problems.map(function (p) {
        return { ts: p.ts, route: 'problemy/' + p.id, icon: 'bulb', label: p.title.trim() || 'Problem', kind: 'rozłożony problem' };
      }))
      .sort(function (a, b) { return a.ts < b.ts ? 1 : -1; })
      .slice(0, 5);

    if (!items.length) return null;

    return ui.card(null,
      ui.sectionTitle('Ostatnio'),
      h('div', { class: 'entry-list' }, items.map(function (item) {
        return h('button', { class: 'entry', onClick: function () { K.go(item.route); } },
          ui.icon(item.icon),
          h('div', { class: 'entry-body' },
            h('span', { class: 'entry-title', text: item.label }),
            h('span', { class: 'entry-meta' },
              h('span', { text: item.kind }),
              h('span', { text: ui.relativeDate(item.ts) })
            )
          )
        );
      }))
    );
  }

  function render() {
    const s = K.store.state;
    const day = K.today();
    const mood = K.mood.forDay(day);
    const name = s.settings.name.trim();
    const days = streak();
    const reviews = pendingReviews();
    const steps = openSteps();
    const isNew = !s.decisions.length && !s.thoughts.length && !s.problems.length && !s.moods.length;

    const nodes = [
      h('div', { class: 'page-head' },
        h('div', null,
          h('h1', { text: greeting() + (name ? ', ' + name : '') + '.' }),
          h('p', { class: 'muted', text: days > 1 ? 'Zaglądasz tu ' + days + ' ' + ui.plural(days, 'dzień', 'dni', 'dni') + ' z rzędu.' : 'Masz tu spokojne miejsce, żeby się zatrzymać.' })
        )
      )
    ];

    if (isNew) {
      nodes.push(ui.card(null,
        ui.sectionTitle('Zacznijmy od tego, czym to jest'),
        h('p', { text: 'Kompas nie doradza i nie ocenia. Daje strukturę: pytania zadawane w odpowiedniej kolejności, które pomagają samemu zobaczyć sprawę jaśniej.' }),
        h('div', { class: 'stack sm' },
          h('p', { class: 'muted', text: 'Nie wiesz, co wybrać — otwórz wagę decyzyjną.' }),
          h('p', { class: 'muted', text: 'Kręci Ci się w głowie od jednej myśli — rozbierz ją w dzienniku myśli.' }),
          h('p', { class: 'muted', text: 'Wszystko naraz Cię przytłacza — rozłóż problem na części.' }),
          h('p', { class: 'muted', text: 'Emocje są na dziesiątkę — najpierw oddech.' })
        ),
        h('p', { class: 'tiny', text: 'Wszystko zapisuje się na tym urządzeniu i zostaje po zamknięciu karty.' })
      ));
    }

    nodes.push(ui.card(null,
      ui.sectionTitle(mood ? 'Dziś: ' + K.mood.levelOf(mood.score).label.toLowerCase() : 'Jak się dziś masz?',
        mood ? 'Możesz zmienić, jeśli dzień się zmienił.' : 'Jeden klik. Nic więcej dziś nie musisz.'),
      K.mood.picker(day, mood),
      mood ? h('div', { class: 'row' }, ui.button('Dopisz szczegóły', { variant: 'ghost', onClick: function () { K.go('nastroj'); } })) : null
    ));

    if (reviews.length) {
      nodes.push(ui.card({ class: 'tight' },
        ui.sectionTitle('Wróć do swojej decyzji', 'Podjąłeś ją jakiś czas temu. Jak z nią żyjesz?'),
        h('div', { class: 'entry-list' }, reviews.slice(0, 3).map(function (d) {
          return h('button', { class: 'entry', onClick: function () { K.go('decyzje/' + d.id); } },
            ui.icon('scale'),
            h('div', { class: 'entry-body' },
              h('span', { class: 'entry-title', text: d.title.trim() || d.choice }),
              h('span', { class: 'entry-meta' }, h('span', { text: 'zdecydowane ' + ui.relativeDate(d.decidedAt) }))
            ),
            h('span', { class: 'badge warn', text: 'oceń' })
          );
        }))
      ));
    }

    if (steps.length) {
      nodes.push(ui.card({ class: 'tight' },
        ui.sectionTitle('Zaplanowane kroki'),
        h('div', { class: 'entry-list' }, steps.slice(0, 3).map(function (p) {
          return h('button', { class: 'entry', onClick: function () { K.go('problemy/' + p.id); } },
            ui.icon('bulb'),
            h('div', { class: 'entry-body' },
              h('span', { class: 'entry-title', text: p.step.trim() }),
              h('span', { class: 'entry-meta' },
                h('span', { text: p.title.trim() || 'problem' }),
                p.deadline ? h('span', { text: 'na ' + ui.dayLabel(p.deadline) }) : null
              )
            )
          );
        }))
      ));
    }

    nodes.push(ui.card(null,
      ui.sectionTitle('Od czego zacząć?'),
      h('div', { class: 'entry-list' },
        tile('decyzje', 'scale', 'Nie wiem, co wybrać', 'Rozłóż decyzję na argumenty i nadaj im wagę.'),
        tile('mysli', 'thought', 'Jedna myśl nie daje mi spokoju', 'Sprawdź, ile w niej faktu, a ile lęku.'),
        tile('problemy', 'bulb', 'Wszystko naraz mnie przytłacza', 'Zejdź do jednego małego kroku.'),
        tile('spokoj', 'wind', 'Muszę się uspokoić teraz', 'Oddech i uziemienie na już.')
      )
    ));

    const recent = feed();
    if (recent) nodes.push(recent);

    return nodes;
  }

  K.views = K.views || {};
  K.views.pulpit = { render: render };
})(window.K = window.K || {});
