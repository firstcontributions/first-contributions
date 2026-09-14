(function (K) {
  'use strict';

  const ui = K.ui;
  const h = ui.h;

  function all() { return K.store.state.problems; }
  function find(id) { return all().filter(function (p) { return p.id === id; })[0]; }

  function isBlank(p) {
    return !p.title.trim() && !p.ideas.some(function (i) { return i.text.trim(); });
  }

  function create() {
    const problem = {
      id: K.uid(),
      ts: new Date().toISOString(),
      title: '',
      control: '',
      noControl: '',
      ideas: [{ id: K.uid(), text: '' }],
      chosen: null,
      step: '',
      deadline: '',
      done: false
    };
    K.store.silent(function (s) { s.problems.unshift(problem); });
    K.go('problemy/' + problem.id);
  }

  function renderList() {
    if (all().some(isBlank)) {
      K.store.silent(function (s) {
        s.problems = s.problems.filter(function (p) { return !isBlank(p); });
      });
    }

    const items = all();
    const nodes = [
      h('div', { class: 'page-head' },
        h('div', null,
          h('h1', { text: 'Rozłóż problem' }),
          h('p', { class: 'muted', text: 'Wielkie "wszystko jest źle" nie da się rozwiązać. Da się rozwiązać jedną, konkretną rzecz — i od niej zacząć.' })
        ),
        ui.button('Nowy problem', { variant: 'primary', icon: 'plus', onClick: create })
      )
    ];

    if (!items.length) {
      nodes.push(ui.empty('Nic tu jeszcze nie ma. Gdy poczujesz się przytłoczony, rozłóż to na czynniki pierwsze.', 'Rozłóż pierwszy problem', create));
      return nodes;
    }

    nodes.push(h('div', { class: 'entry-list' }, items.map(function (p) {
      return h('button', { class: 'entry', onClick: function () { K.go('problemy/' + p.id); } },
        ui.icon('bulb'),
        h('div', { class: 'entry-body' },
          h('span', { class: 'entry-title', text: p.title.trim() || 'Problem bez nazwy' }),
          h('span', { class: 'entry-meta' },
            h('span', { text: ui.relativeDate(p.ts) }),
            p.step.trim() ? h('span', { text: 'krok: ' + p.step.trim() }) : null
          )
        ),
        p.done ? h('span', { class: 'badge pro', text: 'zrobione' }) : (p.step.trim() ? h('span', { class: 'badge', text: 'w planie' }) : null)
      );
    })));

    return nodes;
  }

  function ideaRow(problem, idea, listEl, repaint) {
    const row = h('div', { class: 'arg-row' },
      ui.input({
        value: idea.text,
        placeholder: 'Pomysł — nawet ten, który wydaje się głupi',
        onInput: function (value) { idea.text = value; K.store.silent(function () {}); }
      }),
      ui.button('Wybieram', {
        variant: problem.chosen === idea.id ? 'primary' : 'ghost',
        onClick: function () {
          K.store.update(function () {
            problem.chosen = problem.chosen === idea.id ? null : idea.id;
          });
        }
      }),
      ui.button('', {
        variant: 'icon',
        icon: 'trash',
        ariaLabel: 'Usuń pomysł',
        onClick: function () {
          const index = problem.ideas.indexOf(idea);
          if (index > -1) problem.ideas.splice(index, 1);
          if (problem.chosen === idea.id) problem.chosen = null;
          K.store.silent(function () {});
          row.remove();
          repaint();
        }
      })
    );
    listEl.appendChild(row);
    return row;
  }

  function renderEditor(problem) {
    const p = K.data.prompts;
    function bind(key) {
      return function (value) { problem[key] = value; K.store.silent(function () {}); };
    }

    const ideasEl = h('div', { class: 'stack sm' });
    const counter = h('p', { class: 'muted' });
    function repaint() {
      const n = problem.ideas.filter(function (i) { return i.text.trim(); }).length;
      counter.textContent = n < 3
        ? 'Wypisz co najmniej trzy. Pierwszy pomysł rzadko jest najlepszy.'
        : n + ' ' + ui.plural(n, 'pomysł', 'pomysły', 'pomysłów') + ' na stole. Teraz wybierz jeden.';
    }
    problem.ideas.forEach(function (idea) { ideaRow(problem, idea, ideasEl, repaint); });
    repaint();

    return [
      h('div', { class: 'row between' },
        ui.button('Wszystkie problemy', { variant: 'ghost', icon: 'back', onClick: function () { K.go('problemy'); } }),
        ui.button('Usuń', {
          variant: 'ghost',
          icon: 'trash',
          onClick: function () {
            ui.confirm({ title: 'Usunąć ten problem?', confirmLabel: 'Usuń', danger: true }).then(function (ok) {
              if (!ok) return;
              K.store.update(function (s) {
                s.problems = s.problems.filter(function (x) { return x.id !== problem.id; });
              });
              K.go('problemy');
            });
          }
        })
      ),

      ui.card(null,
        ui.sectionTitle('1. Nazwij to konkretnie', 'Zamiast "mam problem w pracy" — "nie wiem, jak powiedzieć szefowi, że nie wyrabiam".'),
        ui.textarea({ rows: 2, value: problem.title, placeholder: 'O co dokładnie chodzi?', onInput: bind('title') })
      ),

      ui.card(null,
        ui.sectionTitle('2. Co jest moje, a co nie', 'Energia zużyta na drugą kolumnę jest energią straconą.'),
        h('div', { class: 'grid-2' },
          ui.field('Zależy ode mnie', ui.textarea({ value: problem.control, placeholder: p.control, onInput: bind('control') })),
          ui.field('Nie zależy ode mnie', ui.textarea({ value: problem.noControl, placeholder: p.noControl, onInput: bind('noControl') }))
        )
      ),

      ui.card(null,
        ui.sectionTitle('3. Burza pomysłów', 'Na tym etapie nie oceniasz. Zapisujesz.'),
        ideasEl,
        counter,
        ui.button('Dodaj pomysł', {
          variant: 'ghost',
          icon: 'plus',
          onClick: function () {
            const idea = { id: K.uid(), text: '' };
            problem.ideas.push(idea);
            K.store.silent(function () {});
            const row = ideaRow(problem, idea, ideasEl, repaint);
            row.querySelector('input').focus();
            repaint();
          }
        })
      ),

      ui.card(null,
        ui.sectionTitle('4. Pierwszy mały krok', 'Tak mały, żeby dało się go zrobić w kwadrans.'),
        ui.textarea({ rows: 2, value: problem.step, placeholder: 'np. napisać jedno zdanie wiadomości i nie wysyłać', onInput: bind('step') }),
        ui.field('Kiedy?', h('input', {
          class: 'input',
          type: 'date',
          value: problem.deadline,
          onChange: function (e) { problem.deadline = e.target.value; K.store.silent(function () {}); }
        })),
        h('div', { class: 'row' }, ui.button(problem.done ? 'Zrobione' : 'Oznacz jako zrobione', {
          variant: problem.done ? 'primary' : undefined,
          onClick: function () {
            K.store.update(function () { problem.done = !problem.done; });
            if (!problem.done) return;
            ui.toast('Zrobione. To liczy się bardziej niż plan.');
          }
        }))
      )
    ];
  }

  K.views = K.views || {};
  K.views.problemy = {
    render: function (param) {
      const problem = param ? find(param) : null;
      return problem ? renderEditor(problem) : renderList();
    }
  };
})(window.K = window.K || {});
