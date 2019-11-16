[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Pierwsze kontrybucje

Zawsze jest ciężko, kiedy robisz coś po raz pierwszy. Szczególnie gdy współpracujesz z innymi ludźmi, ponieważ popełnianie błędów nie jest niczym przyjemnym. Jednak właśnie na współpracy opiera się idea otwartego oprogramowania. Chcemy nauczyć w prosty sposób nowych programistów jak wgrać swoją pierwszą zmianę w obcym projekcie.

Czytanie artykułów i oglądanie poradników może pomóc, ale czy jest coś lepszego niż spróbowanie czegoś samemu bez obaw, że się coś zepsuje? Ten projekt ma na celu dostarczyć nowicjuszom wskazówek i uprościć proces wgrania pierwszej zmiany. Pamiętaj: im bardziej jesteś zrelaksowany, tym lepiej się uczysz. Jeśli chcesz wgrać swoją pierwszą kontrybucję wykonaj kilka prostych kroków poniżej. Będzie fajnie, obiecujemy.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

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
Gdzie "wklej skopiowany adres" (bez cudzysłowia) to adres tego repozytorium. Zobacz poprzedni krok aby skopiować adres.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Przykład:
```
git clone https://github.com/to-ty/first-contributions.git
```
W miejscu 'to-ty' to twój login na githubie. W tym kroku ściągasz zawartość twojej kopii repozytorium first-contributions z githuba na swój komputer.

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

Otwórz plik `Contributors.md` w edytorze tekstu. Musisz znać Markdown, lekki język znaczników. Tu masz <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet">ściągawkę</a> gdzie znajdziesz informację jak używać języka Markdown.

Dodaj następującą linię na końcu `Contributors.md`

```
[Twoje imię](https://github.com/Twoja nazwa użytkownika)
```
Przykład: 
```
[John Doe](https://github.com/johndoe)
```

Upewnij się że nie ma spacji pomiędzy `](`. Zapisz plik i następnie go zamknij.

Jeżeli wejdziesz w folder ze swoim repozytorium i wykonasz komendę `git status`, zobaczysz, że są tam zmiany. Dodaj te zmiany do gałęzi którą właśnie utworzyłeś używając komendy `git add`:
```
`git add Contributors.md`
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

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Niedługo dodam proponowane przez ciebie zmiany do głównej gałęzi projektu. Zostaniesz powiadomiony mailowo kiedy zmiany zostaną scalone.

## Co dalej?

Świętuj swoją pierwszą zmianę i podziel się nią z przyjaciółmi i obserwującymi poprzez <a href="https://roshanjossey.github.io/first-contributions/#social-share" rel="nofollow">aplikację</a>.
Możesz dołączyć do naszego kanału slack w przypadku kiedy będziesz potrzebował pomocy albo miał jakieś pytania. <a href="https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY" rel="nofollow">Dołącz do slacka</a>.
Możesz teraz zacząc uczestniczyć w innych projektach. Przygotowaliśmy listę projektów z prostymi zadaniami które będą dobre na początek. Sprawdź <a href="https://roshanjossey.github.io/first-contributions/#project-list" rel="nofollow">listę projektów</a>.
 
### [Materiały dodatkowe](https://github.com/Roshanjossey/first-contributions/blob/master/additional-material/git_workflow_scenarios/additional-material.md) 
 
## Ćwiczenia przy użyciu innych narzędzi

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

