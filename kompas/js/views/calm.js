(function (K) {
  'use strict';

  const ui = K.ui;
  const h = ui.h;

  const PATTERNS = {
    '4-7-8': { label: 'Oddech 4-7-8', hint: 'Wycisza układ nerwowy. Dobry przed snem albo po kłótni.', phases: [['Wdech', 4], ['Zatrzymaj', 7], ['Wydech', 8]] },
    'box': { label: 'Oddech kwadratowy', hint: 'Używany przez ratowników i wojsko, żeby odzyskać skupienie.', phases: [['Wdech', 4], ['Zatrzymaj', 4], ['Wydech', 4], ['Zatrzymaj', 4]] }
  };

  const GROUNDING = [
    { count: 5, label: 'rzeczy, które widzisz', placeholder: 'np. lampa na biurku' },
    { count: 4, label: 'dźwięki, które słyszysz', placeholder: 'np. lodówka' },
    { count: 3, label: 'rzeczy, których możesz dotknąć', placeholder: 'np. koc' },
    { count: 2, label: 'zapachy, które czujesz', placeholder: 'np. kawa' },
    { count: 1, label: 'rzecz, którą możesz posmakować', placeholder: 'np. woda' }
  ];

  let timers = [];
  let mode = 'oddech';

  function clearTimers() {
    timers.forEach(clearTimeout);
    timers = [];
  }

  function logSession(kind, detail) {
    K.store.silent(function (s) {
      s.calmLog.unshift({ id: K.uid(), ts: new Date().toISOString(), kind: kind, detail: detail });
      if (s.calmLog.length > 300) s.calmLog.length = 300;
    });
  }

  /* ---------- oddech ---------- */

  function breathing() {
    let patternKey = '4-7-8';
    let running = false;
    let cycles = 0;

    const circle = h('div', { class: 'breath-circle' });
    const phaseLabel = h('div', { class: 'breath-phase' },
      h('strong', { text: 'Gotowy?' }),
      h('span', { class: 'muted', text: 'Usiądź wygodnie i naciśnij start.' })
    );
    const counter = h('p', { class: 'muted', text: '' });

    function setPhase(name, seconds) {
      phaseLabel.textContent = '';
      phaseLabel.appendChild(h('strong', { text: name }));
      phaseLabel.appendChild(h('span', { class: 'muted', text: seconds + ' s' }));
    }

    function runPhase(index) {
      if (!running) return;
      const phases = PATTERNS[patternKey].phases;
      const phase = phases[index % phases.length];
      const name = phase[0];
      const seconds = phase[1];

      setPhase(name, seconds);
      circle.style.transitionDuration = seconds + 's';
      if (name === 'Wdech') circle.style.transform = 'scale(1.9)';
      else if (name === 'Wydech') circle.style.transform = 'scale(1)';

      let left = seconds;
      circle.textContent = String(left);
      function tick() {
        if (!running) return;
        left--;
        if (left > 0) {
          circle.textContent = String(left);
          timers.push(setTimeout(tick, 1000));
        }
      }
      timers.push(setTimeout(tick, 1000));

      timers.push(setTimeout(function () {
        if (!running) return;
        if ((index + 1) % phases.length === 0) {
          cycles++;
          counter.textContent = 'Ukończone cykle: ' + cycles;
        }
        runPhase(index + 1);
      }, seconds * 1000));
    }

    function stop() {
      running = false;
      clearTimers();
      circle.style.transitionDuration = '.6s';
      circle.style.transform = 'scale(1)';
      circle.textContent = '';
      phaseLabel.textContent = '';
      phaseLabel.appendChild(h('strong', { text: cycles ? 'Dobra robota' : 'Gotowy?' }));
      phaseLabel.appendChild(h('span', { class: 'muted', text: cycles ? 'Zauważ, czy coś się zmieniło w ciele.' : 'Usiądź wygodnie i naciśnij start.' }));
      startBtn.querySelector('span').textContent = 'Start';
      if (cycles) logSession('oddech', cycles + ' ' + ui.plural(cycles, 'cykl', 'cykle', 'cykli'));
    }

    function start() {
      running = true;
      cycles = 0;
      counter.textContent = '';
      startBtn.querySelector('span').textContent = 'Zatrzymaj';
      runPhase(0);
    }

    const startBtn = ui.button('Start', {
      variant: 'primary',
      onClick: function () { running ? stop() : start(); }
    });

    const patternChips = h('div', { class: 'chips' }, Object.keys(PATTERNS).map(function (key) {
      return h('button', {
        type: 'button',
        class: 'chip' + (key === patternKey ? ' on' : ''),
        text: PATTERNS[key].label,
        onClick: function (e) {
          if (running) stop();
          patternKey = key;
          hint.textContent = PATTERNS[key].hint;
          patternChips.querySelectorAll('.chip').forEach(function (c) { c.classList.remove('on'); });
          e.currentTarget.classList.add('on');
        }
      });
    }));

    const hint = h('p', { class: 'muted', text: PATTERNS[patternKey].hint });

    return ui.card(null,
      patternChips,
      hint,
      h('div', { class: 'breath-stage' }, circle),
      phaseLabel,
      h('div', { class: 'row', style: { justifyContent: 'center' } }, startBtn),
      counter
    );
  }

  /* ---------- uziemienie 5-4-3-2-1 ---------- */

  function grounding() {
    let step = 0;
    const box = h('div', { class: 'stack' });

    function paint() {
      box.textContent = '';

      if (step >= GROUNDING.length) {
        box.appendChild(h('div', { class: 'stack sm' },
          h('h3', { text: 'Jesteś tutaj.' }),
          h('p', { class: 'muted', text: 'Twoja uwaga wróciła do teraz. Jeśli nadal jest ciężko — przejdź to jeszcze raz, wolniej.' }),
          h('div', { class: 'row' },
            ui.button('Jeszcze raz', { onClick: function () { step = 0; paint(); } }),
            ui.button('Zapisz nastrój', { variant: 'primary', onClick: function () { K.go('nastroj'); } })
          )
        ));
        logSession('uziemienie', 'pełne 5-4-3-2-1');
        return;
      }

      const current = GROUNDING[step];
      const inputs = h('div', { class: 'stack sm' });
      for (let i = 0; i < current.count; i++) {
        inputs.appendChild(ui.input({ placeholder: current.placeholder }));
      }

      box.appendChild(h('div', { class: 'stack' },
        h('div', { class: 'step-dots' }, GROUNDING.map(function (_, i) {
          return h('i', { class: i <= step ? 'on' : '' });
        })),
        h('h3', { text: 'Wymień ' + current.count + ' ' + current.label }),
        h('p', { class: 'muted', text: 'Nie musisz wpisywać — wystarczy, że nazwiesz je w głowie. Pola są, jeśli tak łatwiej.' }),
        inputs,
        h('div', { class: 'row' },
          step > 0 ? ui.button('Wstecz', { icon: 'back', onClick: function () { step--; paint(); } }) : null,
          ui.button(step === GROUNDING.length - 1 ? 'Koniec' : 'Dalej', {
            variant: 'primary',
            onClick: function () { step++; paint(); }
          })
        )
      ));
      const first = inputs.querySelector('input');
      if (first) first.focus();
    }

    paint();
    return ui.card(null,
      h('p', { class: 'muted', text: 'Ćwiczenie na moment, gdy myśli gonią albo ciało jest w panice. Sprowadza uwagę z głowy do zmysłów.' }),
      box
    );
  }

  /* ---------- widok ---------- */

  function render() {
    const content = h('div', null);

    function paint() {
      clearTimers();
      content.textContent = '';
      content.appendChild(mode === 'oddech' ? breathing() : grounding());
    }

    const tabs = h('div', { class: 'chips' }, [
      ['oddech', 'Oddech'],
      ['uziemienie', 'Uziemienie 5-4-3-2-1']
    ].map(function (pair) {
      return h('button', {
        type: 'button',
        class: 'chip' + (mode === pair[0] ? ' on' : ''),
        text: pair[1],
        onClick: function () {
          mode = pair[0];
          tabs.querySelectorAll('.chip').forEach(function (c, i) {
            c.classList.toggle('on', (i === 0 ? 'oddech' : 'uziemienie') === mode);
          });
          paint();
        }
      });
    }));

    paint();

    const used = K.store.state.calmLog.length;

    return [
      h('div', { class: 'page-head' },
        h('div', null,
          h('h1', { text: 'Uspokój się' }),
          h('p', { class: 'muted', text: 'Gdy emocje są na dziesiątkę, żadne rozkładanie problemu nie zadziała. Najpierw ciało, potem głowa.' })
        )
      ),
      tabs,
      content,
      used ? h('p', { class: 'tiny', text: 'Skorzystałeś z tych ćwiczeń ' + used + ' ' + ui.plural(used, 'raz', 'razy', 'razy') + '.' }) : null
    ];
  }

  K.views = K.views || {};
  K.views.spokoj = {
    render: render,
    destroy: clearTimers
  };
})(window.K = window.K || {});
