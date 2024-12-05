[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Pierwsze kontrybucje

Zawsze jest ciężko, kiedy robisz coś po raz pierwszy. Szczególnie gdy współpracujesz z innymi ludźmi, ponieważ popełnianie błędów nie jest niczym przyjemnym. Jednak właśnie na współpracy opiera się idea otwartego oprogramowania. Chcemy nauczyć w prosty sposób nowych programistów jak wgrać swoją pierwszą zmianę w obcym projekcie.

Czytanie artykułów i oglądanie poradników może pomóc, ale czy jest coś lepszego niż spróbowanie czegoś samemu bez obaw, że się coś zepsuje? Ten projekt ma na celu dostarczyć nowicjuszom wskazówek i uprościć proces wgrania pierwszej zmiany. Pamiętaj: im bardziej jesteś zrelaksowany, tym lepiej się uczysz. Jeśli chcesz wgrać swoją pierwszą kontrybucję wykonaj kilka prostych kroków poniżej. Będzie fajnie, obiecujemy.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Jeśli nie masz Gita na swoim komputerze, [ zainstaluj go ](https://help.github.com/articles/set-up-git/).

## Zrób fork repozytorium (`fork`)

Zrób fork tego repozytorium klikając przycisk `Fork` na górze tej strony. Stworzysz tym samym kopię tego repozytorium na swoim koncie.

## Sklonuj repozytorium (`clone`)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Teraz sklonuj repozytorium na swój komputer. Przejdź do swojego konta GitHub, otwórz skopiowane repozytorium, kliknij przycisk `Code`, a później ikonkę _skopiuj do schowka_.

Otwórz konsolę i uruchom komendę git:

```
git clone <skopiowany-adres>
```

Gdzie `<skopiowany-adres>` to adres tego repozytorium (twojej kopii tego projektu). Zobacz poprzedni krok aby skopiować adres.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Przykład:

```
git clone https://github.com/to-ty/first-contributions.git
```

W miejscu `to-ty` to twój login na GitHubie. W tym kroku ściągasz zawartość twojej kopii repozytorium `first-contributions` z githuba na swój komputer.

## Stwórz gałąź (`branch`)

Wejdź do folderu ze swoim repozytorium (jeżeli jeszcze tam nie jesteś):

```
cd first-contributions
```

Teraz utwórz nową gałąź wykonując polecenie `git switch`:

```
git switch -c <add-twoje-imie>
```

Przykład

```
git switch -c add-adam-kowalski
```

(Nazwa gałęzi nie musi zawierać słowa _add_, ale dobrze jest je dodać z racji tego, że celem tej gałęzi jest dodanie twojego imienia do listy.)

## Wprowadź zmiany i wgraj je

Otwórz plik `Contributors.md` w edytorze tekstu. Musisz znać Markdown, lekki język znaczników. Tu masz <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet">ściągawkę</a> gdzie znajdziesz informację jak go używać.

Dodaj następującą linię w `Contributors.md`

```
[Twoje imię](https://github.com/Twoja-nazwa-użytkownika)
```

Przykład:

```
[John Doe](https://github.com/johndoe)
```

Nie dodawaj jej na początku ani na końcu pliku. Umieść ją w dowolnym miejscu pomiędzy.

Upewnij się że nie ma spacji pomiędzy `](`. Zapisz plik i następnie go zamknij.

Jeżeli wejdziesz do folderu ze swoim repozytorium i wykonasz komendę `git status`, zobaczysz, że są tam zmiany. Dodaj te zmiany do gałęzi którą właśnie utworzyłeś używając komendy `git add`:

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
git push -u origin <add-twoje-imie>
```

Zastąp `<add-twoje-imie>` nazwą gałęzi, którą wcześniej utworzyłeś.

## Wyślij swoje zmiany do zatwierdzenia

W swoim repozytorium na GitHubie znajdziesz przycisk `Compare & pull request`. Kliknij go.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Teraz wyślij prośbę o scalenie.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Niedługo dodam proponowane przez ciebie zmiany do głównej gałęzi projektu. Zostaniesz powiadomiony mailowo kiedy zmiany zostaną scalone.

## Co dalej?

Brawo! Właśnie ukończyłeś standardowy workflow _fork -> clone -> edit -> pull request_, który często będziesz napotykać jako współtwórca!

Świętuj swoją pierwszą zmianę i podziel się nią z przyjaciółmi i obserwującymi poprzez <a href="https://firstcontributions.github.io/#social-share" rel="nofollow">aplikację</a>.

Możesz dołączyć do naszego kanału slack w przypadku kiedy będziesz potrzebował pomocy albo miał jakieś pytania. <a href="https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA" rel="nofollow">Dołącz do slacka</a>.

Możesz teraz zacząć uczestniczyć w innych projektach. Przygotowaliśmy listę projektów z prostymi zadaniami które będą dobre na początek. Sprawdź <a href="https://firstcontributions.github.io/#project-list" rel="nofollow">listę projektów</a>.

### [Materiały dodatkowe](../additional-material/git_workflow_scenarios/additional-material.md)

## Ćwiczenia przy użyciu innych narzędzi

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
