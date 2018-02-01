[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# Pierwsze kontrybucje

Zawsze jest ciężko, kiedy robisz coś po raz pierwszy. Szczególnie gdy współpracujesz z innymi ludźmi, popełnianie błędów nie jest niczym przyjemnym. Jednak właśnie na współpracy opiera się idea otwartego oprogramowania. Chcieliśmy uprościć dla nowych programistów proces nauki i wgrania swojej pierwszej zmiany w obcym projekcie.

Czytanie artykułów i oglądanie poradników może pomóc, ale czy jest coś lepszego niż spróbowanie czegoś samemu bez obaw, że się coś zepsuje? Ten projekt ma na celu dostarczyć wskazówek i uprościć wgranie pierwszej zmiany nowicjuszom. Pamiętaj: im bardziej jesteś zrelaksowany, tym lepiej się uczysz. Jeśli chcesz wgrać swoją pierwszą kontrybucję wykonaj kilka prostych kroków poniżej. Będzie fajnie, obiecujemy.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

*Przeczytaj w innych językach: [English](../README.md), [Indonesian](translations/README.id.md), [French](translations/README.fr.md), [Spanish](translations/README.es.md), [Dutch](translations/README.nl.md), [Hindi](translations/README.hi.md), [Russian](translations/README.ru.md), [Japanese](translations/README.ja.md), [Vietnamese](translations/README.vn.md), [Korean](translations/README.ko.md), [German](translations/README.de.md), [Simplified Chinese](translations/README.chs.md), [Traditional Chinese](translations/README.cht.md), [Greek](translations/README.gr.md), [العربية](translations/README.ar.md), [Ukrainian](translations/README.ua.md) and [Português/Brasil](translations/README.pt_br.md).*

Jeśli nie masz Gita na swoim komputerze, [ zainstaluj go ]( https://help.github.com/articles/set-up-git/ ).

## Utwórz fork repozytorium

Utwórz fork tego repozytorium klikając przycisk "Fork" na górze tej strony.
Stworzysz tym samym kopie tego repozytorium na swoim koncie.

## Sklonuj repozytorium

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Teraz sklonuj repozytorium na swój komputer. Kliknij na przycisk "clone" a później na ikonkę *skopiuj do schowka*.

Otwórz konsolę i uruchom komendę git:

```
git clone "wklej skopiowany adres"
```
Gdzie "wklej skopiowany adres" (bez cudzysłowów) to adres tego repozytorium. Zobacz poprzedni krok aby skopiować adres.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Przykład:
```
git clone https://github.com/to-ty/first-contributions.git
```
W miejscu 'to-ty' to Twój login na githubie. W tym kroku ściągasz zawartość Twojej kopii repozytorium first-contributions z githuba na swój komputer.

## Stwórz gałąź

Wejdź w folder ze swoim repozytorium (jeżeli jeszcze tam nie jesteś):

```
cd first-contributions
```
Teraz utwórz nową gałąź wykonując polecenie `git checkout`:
```
git checkout -b <add-twoje-imie>
```

Przykład
```
git checkout -b add-adam-kowalski
```
(Nazwa gałęzi nie musi zawierać słowa *add*, ale dobrze jest je dodać z racji tego, że celem tej gałęzi jest dodanie twojego imienia to listy.)

## Wprowadź zmiany i wgraj je

Otwórz plik `Contributors.md` w edytorze tekstu, dodaj swoje dane i zapisz go. Jeżeli będziesz w folderze repozytorium i uruchomisz polecenie `git status` zobaczysz, że pojawiły się zmiany. Dodaj te zmiany do wcześniej utworzonej gałęzi przy pomocy polecenia `git add`.
```
git add Contributors.md
```

Teraz zapisz te zmiany wykonując komendę `git commit`:
```
git commit -m "Add <twoje-imie> to Contributors list"
```
Zastąp `<twoje-imie>` swoim imieniem i nazwiskiem.

## Wyślij zmiany na GitHub

Wyślij swoje zmiany komendą `git push`:
```
git push origin <add-twoje-imie>
```
Zastąp `<add-twoje-imie>` nazwą gałęzi, którą wcześniej utworzyłeś.

## Wyślij swoje zmiany do zatwierdzenia

W swoim repozytorium na GitHubie znajdziesz przycisk `Compare & pull request`. Kliknij go.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Teraz wyślij prośbę o scalenie.

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

Niedługo dodam proponowane przez ciebie zmiany do głównej gałęzi projektu. Zostaniesz powiadomiony mailowo kiedy zmiany zostaną scalone.

Teraz, kiedy gałąź `<add-twoje-imie>` spełniła swoje zadanie, usuńmy ją.

## Usuń gałąź ze swojego repozytorium

Jeśli dotarłeś z poradnikiem do tego momentu, nasza gałąź `<add-twoje-imie>` spełniła swoje zadanie i pora usunąć ją z twojego komputera. Nie jest to koniecznie, ale sama nazwa gałęzi wskazuje na jej konkretny cel i tym samym naturalnie krótki żywot.

Najpierw połączy gałąź `<add-twoje-imie>` z gałęzią główną. Przejdź więc do gałęzi głównej:
```
git checkout master
```

Scal `<add-twoje-imie>` z master:
```
git merge <add-twoje-imie> master
```

Usuń `<add-twoje-imie>` z repozytorium na swoim komputerze:
```
git branch -d <add-twoje-imie>
```

Właśnie usunąłeś gałąź `<add-twoje-imie>` ze swojego komputery i wszystko wygląda schludnie.
Jednakże, nadal masz gałąź `<add-twoje-imie>` w swoim forku na GitHubie. Zanim ją usuniesz pamiętaj, że wysłałeś "Pull request" do mojego repozytorium z tej zdalnej gałęzi. Jeśli jeszcze jej nie scaliłem - nie usuwaj jej.

Jeśli scaliłem już twoją gałąź i chcesz ją usunąć, użyj:
```
git push origin --delete <add-twoje-imie>
```

Teraz już wiesz jak uporządkować swoje gałęzie.
Z czasem wiele zmian zostanie wprowadzonych do mojego publicznego repozytorium. Gałąź główna na twoim komputerze i w twoim forku repozytorium nie będą aktualne. Aby utrzymać swoje repozytoria zsynchronizowane z moim, wykonaj kroki poniżej.


## Utrzymywanie swojego forka zsynchronizowanego z tym repozytorium

Na początku musisz zrozumieć ideę pełnej synchronizacji. W tym wypadku istnieją 3 różne repozytoria: moje publiczne na Githubie `github.com/Roshanjossey/first-contributions/`, twój fork na Githubie `github.com/twoj-login/first-contributions/` i lokalne repozytorium na twoim komputerze, na którym pracujesz.

Aby zsynchronizować twoje 2 repozytoria z moim musisz wpierw ściągnąć i scalić publiczne repozytorium z tym na twoim komputerze.
Drugim krokiem jest wgranie twojego lokalnego repozytorium do forka na GitHubie. Jak już wcześniej widziałeś możesz poprosić o scalanie zmian (pull request) tylko ze swojego forka. Twój fork na GitHubie jest ostatnim repozytorium, które będzie zaktualizowane.

Ok, działamy:

Musisz znajdować się w głównej gałęzi swojego repozytorium (master). Sprawdź aktualną gałąź w pierwszej linijce po wpisaniu polecenia:
```
git status
```
jeśli nie jesteś w gałęzi master wpisz:
```
git checkout master
```

Dodaj moje publiczne repozytorium do swojego gita `add upstream remote-url`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Tym sposobem powiesz gitowi, że istnieje inna wersja tego repozytorium pod podanym adresem i nazywamy ją `upstream`. Gdy git zna już nazwę, ściągnijmy aktualną wersję publicznego repozytorium:
```
git fetch upstream
```

Właśnie ściągnąłeś najnowszą wersję mojego repozytorium (upstream remote). Teraz scal publiczne repozytorium do swojej gałęzi master.
```
git rebase upstream/master
```
W tym kroku scalasz publiczne repozytorium ze swoją gałęzią master. Twoja lokalna gałąź master jest aktualna. Teraz, kiedy wyślesz swoje zmiany do swojego forka na GitHubie, też będzie aktualny:
```
git push origin master
```
W tym momencie wysyłasz zmiany do nazwanej gałęzi zdalnej.

Wszystkie twoje repozytoria są aktualne. Dobra robota! Powinieneś wykonać ten proces za każdym razem, kiedy twoje repozytorium stwierdzi, że jest kilka zmian (commitów) do tyłu za publicznym repozytorium.

## Ćwiczenia przy użyciu innych narzędzi


|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Co dalej?

Możesz dołączyć do naszego Slacka jeśli potrzebujesz pomocy albo masz jakieś pytania (Wersja angielska). [Dołącz do Slacka](https://firstcontributions.herokuapp.com)

Oto lista kilku problemów w popularnych repozytoriach z którymi poradzi sobie osoba początkująca. Zajrzyj do nich żeby dowiedzieć się więcej

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
