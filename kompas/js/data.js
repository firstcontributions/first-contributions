(function (K) {
  'use strict';

  K.data = {
    moodLevels: [
      { score: 1, label: 'Bardzo źle', color: 'var(--m1)' },
      { score: 2, label: 'Słabo', color: 'var(--m2)' },
      { score: 3, label: 'Tak sobie', color: 'var(--m3)' },
      { score: 4, label: 'Dobrze', color: 'var(--m4)' },
      { score: 5, label: 'Świetnie', color: 'var(--m5)' }
    ],

    emotions: {
      'Trudne': ['lęk', 'smutek', 'złość', 'wstyd', 'wina', 'samotność', 'przeciążenie', 'bezradność', 'rozczarowanie', 'zazdrość', 'pustka', 'napięcie'],
      'Dobre': ['spokój', 'radość', 'wdzięczność', 'nadzieja', 'duma', 'ulga', 'ciekawość', 'bliskość', 'energia', 'zadowolenie']
    },

    // Klasyczne zniekształcenia poznawcze — nazwa + jednozdaniowe wyjaśnienie.
    distortions: [
      ['Czarno-białe myślenie', 'Albo sukces, albo totalna porażka — bez odcieni pomiędzy.'],
      ['Katastrofizacja', 'Z góry zakładam najgorszy możliwy scenariusz.'],
      ['Czytanie w myślach', 'Jestem pewien, co inni o mnie myślą, choć tego nie sprawdziłem.'],
      ['Wróżenie z fusów', 'Przewiduję przyszłość i traktuję tę przepowiednię jak fakt.'],
      ['Nadmierne uogólnianie', 'Z jednej sytuacji robię regułę: "zawsze", "nigdy", "wszyscy".'],
      ['Filtr negatywny', 'Widzę tylko to, co poszło źle, i pomijam resztę.'],
      ['Pomniejszanie pozytywów', '"To się nie liczy", "każdy by tak potrafił".'],
      ['Personalizacja', 'Biorę na siebie odpowiedzialność za rzeczy, na które nie miałem wpływu.'],
      ['Powinienem / muszę', 'Traktuję siebie zbiorem sztywnych nakazów, a potem karzę się za ich złamanie.'],
      ['Etykietowanie', 'Zamiast opisać zachowanie, przyklejam sobie etykietę: "jestem beznadziejny".'],
      ['Rozumowanie emocjonalne', 'Skoro tak to czuję, to musi być prawda.'],
      ['Porównywanie się', 'Zestawiam swoje kulisy z cudzą wersją na pokaz.']
    ],

    // Pytania, które w rozmowie zadałby terapeuta — tu są podpowiedziami w polach.
    prompts: {
      situation: 'Co się wydarzyło? Sama sytuacja, bez ocen — jak zapis z kamery.',
      thought: 'Co przeleciało Ci przez głowę w tamtym momencie?',
      evidenceFor: 'Jakie fakty przemawiają za tą myślą?',
      evidenceAgainst: 'Jakie fakty jej przeczą? Co powiedziałby ktoś, kto Cię lubi?',
      balanced: 'Jak brzmi wersja, która mieści oba zestawy faktów?',
      friend: 'Gdyby przyszedł do Ciebie przyjaciel z dokładnie tym problemem — co byś mu powiedział?',
      worst: 'Najgorszy scenariusz — i co wtedy zrobisz?',
      best: 'Najlepszy scenariusz.',
      likely: 'Najbardziej prawdopodobny scenariusz.',
      control: 'Co w tej sprawie zależy ode mnie?',
      noControl: 'Czego nie kontroluję i mogę odpuścić?'
    },

    nav: [
      { id: 'pulpit', label: 'Pulpit', icon: 'compass' },
      { id: 'decyzje', label: 'Waga decyzyjna', icon: 'scale' },
      { id: 'mysli', label: 'Dziennik myśli', icon: 'thought' },
      { id: 'problemy', label: 'Rozłóż problem', icon: 'bulb' },
      { id: 'nastroj', label: 'Nastrój', icon: 'mood' },
      { id: 'nawyki', label: 'Małe kroki', icon: 'check' },
      { id: 'spokoj', label: 'Uspokój się', icon: 'wind' },
      { id: 'ustawienia', label: 'Ustawienia', icon: 'gear' }
    ],

    helplines: [
      ['112', 'numer alarmowy'],
      ['800 70 2222', 'Centrum Wsparcia dla osób w kryzysie psychicznym, całodobowo i bezpłatnie'],
      ['116 123', 'kryzysowy telefon zaufania dla dorosłych'],
      ['116 111', 'telefon zaufania dla dzieci i młodzieży']
    ]
  };
})(window.K = window.K || {});
