(function (K) {
  'use strict';

  const KEY = 'kompas.v1';
  const COLLECTIONS = ['moods', 'decisions', 'thoughts', 'problems', 'habits', 'calmLog'];
  const listeners = new Set();

  const empty = () => ({
    version: 1,
    createdAt: new Date().toISOString(),
    settings: { theme: 'auto', name: '' },
    moods: [],
    decisions: [],
    thoughts: [],
    problems: [],
    habits: [],
    calmLog: []
  });

  function canPersist() {
    try {
      localStorage.setItem(KEY + '.probe', '1');
      localStorage.removeItem(KEY + '.probe');
      return true;
    } catch (e) {
      return false;
    }
  }

  function normalize(data) {
    const base = empty();
    if (!data || typeof data !== 'object') return base;
    const out = Object.assign(base, data);
    out.settings = Object.assign(empty().settings, data.settings || {});
    COLLECTIONS.forEach(function (key) {
      if (!Array.isArray(out[key])) out[key] = [];
    });
    return out;
  }

  function read() {
    if (!persistent) return empty();
    try {
      const raw = localStorage.getItem(KEY);
      return raw ? normalize(JSON.parse(raw)) : empty();
    } catch (e) {
      console.warn('Kompas: nie udało się odczytać zapisanych danych.', e);
      return empty();
    }
  }

  let persistent = canPersist();
  let state = read();
  let pending = null;

  function write() {
    if (!persistent) return;
    try {
      localStorage.setItem(KEY, JSON.stringify(state));
    } catch (e) {
      persistent = false;
      if (K.ui) K.ui.toast('Nie mogę zapisać danych — pamięć przeglądarki jest pełna albo zablokowana.');
    }
  }

  function flush() {
    if (pending) {
      clearTimeout(pending);
      pending = null;
      write();
    }
  }

  K.store = {
    get state() { return state; },
    get persistent() { return persistent; },

    // Zmiana struktury danych: zapisz i odśwież widok.
    update: function (fn) {
      fn(state);
      flush();
      write();
      listeners.forEach(function (cb) { cb(state); });
    },

    // Edycja treści w locie (pisanie w polu) — zapis bez przerysowania widoku,
    // żeby nie gubić kursora w trakcie pisania.
    silent: function (fn) {
      fn(state);
      if (pending) clearTimeout(pending);
      pending = setTimeout(function () { pending = null; write(); }, 400);
    },

    onChange: function (cb) {
      listeners.add(cb);
      return function () { listeners.delete(cb); };
    },

    exportJSON: function () {
      flush();
      return JSON.stringify(state, null, 2);
    },

    importJSON: function (text) {
      const parsed = JSON.parse(text);
      if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
        throw new Error('To nie wygląda na kopię zapasową Kompasu.');
      }
      state = normalize(parsed);
      this.update(function () {});
    },

    reset: function () {
      state = empty();
      this.update(function () {});
    },

    flush: flush,

    count: function () {
      return COLLECTIONS.reduce(function (sum, key) {
        return sum + (key === 'habits' || key === 'calmLog' ? 0 : state[key].length);
      }, 0);
    }
  };

  window.addEventListener('beforeunload', flush);
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden') flush();
  });

  K.uid = function () {
    return Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
  };

  K.dayKey = function (date) {
    const d = date ? new Date(date) : new Date();
    return [
      d.getFullYear(),
      String(d.getMonth() + 1).padStart(2, '0'),
      String(d.getDate()).padStart(2, '0')
    ].join('-');
  };

  K.today = function () { return K.dayKey(); };

  K.shiftDay = function (dayKey, delta) {
    const parts = dayKey.split('-').map(Number);
    const d = new Date(parts[0], parts[1] - 1, parts[2] + delta);
    return K.dayKey(d);
  };

  K.daysBetween = function (aKey, bKey) {
    const a = new Date(aKey + 'T00:00:00');
    const b = new Date(bKey + 'T00:00:00');
    return Math.round((b - a) / 86400000);
  };
})(window.K = window.K || {});
