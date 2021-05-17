[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Pierwsze kontrybucje

Ten projekt ma na celu uproszczenie i poprowadzenie nowicjuszy przez ich pierwszą kontrybucję. Jeśli chcesz dokonać swojej pierwszej kontrybucji, wykonaj poniższe kroki.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

_Jeśli nie czujesz się komfortowo używając konsoli, [tutaj znajdziesz poradniki korzystające z narzędzi z graficznym interfejsem.](#ćwiczenia-przy-użyciu-innych-narzędzi)_

Jeśli nie masz Gita na swoim komputerze, [ zainstaluj go ]( https://help.github.com/articles/set-up-git/ ).

## Utwórz fork repozytorium (`fork`)

Utwórz fork tego repozytorium klikając przycisk `Fork` na górze tej strony. Stworzysz tym samym kopię tego repozytorium na swoim koncie.

## Sklonuj repozytorium (`clone`)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Teraz sklonuj repozytorium na swój komputer. Wejdź na swoje konto GitHub, otwórz fork repozytorium, kliknij przycisk `Code`, a później ikonkę *skopiuj do schowka*.

Otwórz konsolę i uruchom komendę git:

```
git clone "skopiowany-adres"
```
Gdzie "skopiowany-adres" (bez cudzysłowu) to adres tego repozytorium (Twojego forka tego projektu). Zobacz poprzedni krok aby skopiować adres.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Przykład:
```
git clone https://github.com/to-ty/first-contributions.git
```

gdzie `to-ty` to Twój login na GitHubie. W tym kroku ściągasz zawartość Twojej kopii repozytorium `first-contributions` z GitHuba na swój komputer.

## Stwórz gałąź (`branch`)

Wejdź do folderu ze swoim repozytorium (jeżeli jeszcze tam nie jesteś):

```
cd first-contributions
```
Teraz utwórz nową gałąź wykonując polecenie `git checkout`:

```
git checkout -b nazwa-twojej-gałęzi
```

Przykład:
```
git checkout -b add-adam-kowalski
```
(Nazwa gałęzi nie musi zawierać słowa *add*, ale dobrze jest je dodać z racji tego, że celem tej gałęzi jest dodanie Twojego imienia do listy.)

## Wprowadź zmiany i wgraj je

Otwórz plik `Contributors.md` w edytorze tekstu, dodaj do niego swoje imię. Nie dodawaj go na początku ani na końcu pliku. Wstaw je w dowolnym miejscu w środku. Teraz zapisz plik.

<img src="https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67" alt="git status" data-canonical-src="https://firstcontributions.github.io/assets/Readme/git-status.png" style="max-width:100%;" width="450" align="right">

Jeśli przejdziesz do folderu projektu i wykonasz komendę `git status`, zobaczysz zmiany.

Używając komendy `git add` dodaj te zmiany do gałęzi, którą niedawno stworzyłeś/aś:

```
git add Contributors.md
```

Teraz zapisz te zmiany wykonując komendę `git commit`:
```
git commit -m "Add <twoje-imię> to Contributors list"
```

zastępując `<twoje-imię>` swoim imieniem.

## Wyślij zmiany na GitHub

Wyślij swoje zmiany komendą `git push`:
```
git push origin <add-nazwa-twojej-gałęzi>
```
zastępując `<add-nazwa-twojej-gałęzi>` nazwą gałęzi, którą wcześniej utworzyłeś/aś.

## Wyślij swoje zmiany do zatwierdzenia

W swoim repozytorium na GitHubie znajdziesz przycisk `Compare & pull request`. Kliknij go.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Teraz wyślij prośbę o scalenie.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Niedługo dodam proponowane przez Ciebie zmiany do głównej gałęzi projektu. Zostaniesz powiadomiony/a mailowo kiedy zmiany zostaną scalone.

## Co dalej?

Gratuluję! Właśnie ukończyłeś/aś swój pierwszy cykl pracy _fork_ -> _klon_ -> _edycja_ -> _prośba o scalenie_, z którym często spotkasz się wnosząc wkład w projekty!

Świętuj swoją pierwszą zmianę i podziel się nią z przyjaciółmi i obserwującymi poprzez [aplikację](https://firstcontributions.github.io/#social-share).

Możesz dołączyć do naszego kanału slack w przypadku kiedy będziesz potrzebował pomocy albo miał(a) jakieś pytania. [Dołącz do slacka](https://join.slack.com/t/firstcontributors/shared_invite/zt-kpbyrmkk-JDkRtchcvRvQ0qK4iPmyvA).

Możesz teraz zacząc uczestniczyć w innych projektach. Przygotowaliśmy listę projektów z prostymi zadaniami które będą dobre na początek. Sprawdź [listę projektów](https://firstcontributions.github.io/#project-list).
 
### [Materiały dodatkowe](../additional-material/git_workflow_scenarios/additional-material.md) 
 
## Ćwiczenia przy użyciu innych narzędzi

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
