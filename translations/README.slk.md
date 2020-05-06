[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Prvé príspevky

Je to ťažké. Je to vždy ťažké, keď niečo robíš prvýkrát. Najmä vtedy, keď spolupracuješ, robiť chyby nie je pohodlná vec. Chceli sme zjednodušiť spôsob, akým sa noví prispievatelia do open source učia a prispievajú prvýkrát.

Čítanie článkov a sledovanie tutoriálov môže pomôcť, ale čo je lepšie, ako skutočne robiť veci v skúšobnom prostredí? Cieľom tohto projektu je poskytnúť usmernenie a zjednodušiť spôsob, akým prvýkrát prispievajú začiatočníci. Ak máš záujem o prvý príspevok, postupuj podľa nižšie uvedených krokov.

#### *Ak sa ti nedarí s príkazovým riadkom, [tu sú návody s nástrojmi grafického rozhrania.]( #návody-pomocou-iných-nástrojov )*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Ak nemáš na svojom počítači git, [nainštaluj ho]( https://help.github.com/articles/set-up-git/).

## Skopíruj toto úložisko

Skopíruj toto úložisko kliknutím na tlačidlo vidlice(fork) v hornej časti tejto stránky.
Tým sa vytvorí kópia tohto úložiska na tvojom účte.

## Stiahni toto úložisko

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Teraz stiahni toto úložisko do tvojho zariadenia. Prejdi do tvojho účtu GitHub, otvor skopírované úložisko, klikni na tlačidlo klonovania a potom klikni na ikonu * kopírovať do schránky *.

Otvor terminál a spusti nasledujúci git príkaz:

```
git clone "adresa, ktorú si práve skopíroval"
```
kde "adresa ktorú si práve skopíroval" (bez úvodzoviek) je adresa URL tohto úložiska (tvoja kópia tohto projektu). Pozri si predchádzajúce kroky na získanie adresy URL.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Napríklad:
```
git clone https://github.com/toto-si-ty/prve-prispevky.git
```
kde `toto-si-ty` je tvoje GitHub užívateľské meno. Tu skopíruješ obsah GitHub úložiska prve-prispevky do tvojho počítača.

## Vytvor vetvu

Prejdi do adresára úložiska v tvojom počítači (ak ešte nie si tam):

```
cd prve-prispevky
```
Teraz vytvor vetvu pomocou príkazu `git checkout`:
```
git checkout -b <pridaj-meno-tvojej-novej-vetvy>
```

Napríklad:
```
git checkout -b pridaj-ferko-mrkvicka
```
(Názov pobočky nemusí obsahovať slovo * pridaj *, ale je rozumné pridať ho, pretože účelom tejto pobočky je pridať tvoje meno do zoznamu.)

## Vykonaj potrebné zmeny a potvrď tieto zmeny

Teraz otvor súbor `Contributors.md` v textovom editore a pridaj do neho svoje meno. Nepridávaj ho na začiatok alebo na koniec súboru. Daj ho kdekoľvek medzi tým. Teraz súbor ulož.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Ak prejdeš do adresára projektu a vykonáš príkaz `git status`, uvidíš zmeny.

Pridaj tieto zmeny do vetvy, ktorú si práve vytvoril, pomocou príkazu `git add`:

```
git add Contributors.md
```

Teraz vykonaj tieto zmeny pomocou príkazu `git commit`:
```
git commit -m "Pridaj <tvoje-meno> do zoznamu pripievateľov"
```
nahraď `<tvoje-meno>` tvojim menon.

## Nahraj zmeny na GitHub

Nahraj svoje zmeny pomocou príkazu `git push`:
```
git push origin <pridaj-meno-tvojej-novej-vetvy>
```
nahraď `<pridaj-meno-tvojej-novej-vetvy>` názvom vetvy, ktorú si vytvoril skôr.

## Odošli svoje zmeny na kontrolu

Ak prejdeš do tvojho úložiska v službe GitHub, zobrazí sa tlačidlo `Compare & pull request`. Klikni na toto tlačidlo.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Teraz predlož požiadavku na vytiahnutie.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />


Čoskoro budem zlučovat všetky vaše zmeny do hlavnej pobočky tohto projektu. Po zlúčení zmien dostaneš upozornenie.

## Kam ísť odtiaľto?

Gratulujem! Práve si dokončil štandardný _fork -> klon -> upraviť -> PR_ pracovný postup, ktorý sa často stretneš ako prispievateľ!

Osláv svoj príspevok a zdieľaj ho so svojimi priateľmi a nasledníkmi [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Môžeš sa pripojiť k nášmu slack tímu v prípade, že potrebuješ nejakú pomoc alebo máš nejaké otázky. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Teraz začni s účasťou na iných projektoch. Vytvorili sme zoznam projektov s jednoduchými problémami, s ktorými môžeš začať. Pozri [zoznam projektov vo webovej aplikácii](https://roshanjossey.github.io/first-contributions/#project-list).

### [Dodatočný materiál](additional-material/git_workflow_scenarios/additional-material.md)


## Návody pomocou iných nástrojov

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

