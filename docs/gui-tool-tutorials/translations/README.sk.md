[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvý príspevok

Život je ťažký. Obzvlášť keď niečo robíte prvýkrát. V prípade, že na niečom spolupracujete, nie je robenie chýb niečo, čo by vám robilo radosť. My by sme radi zjednodušili cestu novým prispievateľom do open-source pri ich učení sa ako na to.

Čítanie článkov alebo zhliadnutie video návodov sú tiež cesty, ale čo je lepšie ako si danú vec priamo ohmatať na vlastnej koži v reálnom prostredí? Tento projekt je zameraný na poskytnutie pomoci začiatočníkom s ich prvým prispením do open-source. Ak ste ním práve vy, nasledujte kroky popísané nižšie.

#### *Ak nemáte radi príkazový riadok, [tu nájdete návody na použitie nástrojov s GUI (grafické užívateľské rozhranie)](#Návod-za-použitie-ďalších-nástrojov)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="forknite tento repozitár" />

Ak máte nainštalovaný git, [nainštalujte si ho]( https://help.github.com/articles/set-up-git/).

## Forknite tento repozitár

Forknite (vytvorenie kópie z originálu, z anglického *fork* - *vidlička*, ako vytvorenie novej odnože) tento repozitár kliknutím na tlačidlo **Fork** hore na tejto stránke. Tým vytvoríte kópiu tohto repozitára na svojom vlastnom GitHib účte.

## Naklonujte repozitár

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="naklonujte tento repozitár" />

Teraz naklonujte (anglicky *clone*) forknutý repozitár na váš počítač, naklonovanie nie je nič iné ako stiahnutie obrazu repozitára k vám na počítač. Na vašom GitHub účte si otvoríte forknutý repozitár, kliknite na tlačidlo **Clone or download** a následne v okienku, ktoré sa objaví, kliknite na tlačidlo s ikonkou **copy to clipboard** vedľa URL adresy, čím si ju skopírujete do schránky.

Teraz otvorte terminál a spustite nasledujúci príkaz:

````
git clone "url ktoré ste práve skopírovali"

````

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="skopírujte adresu do schránky" />

Napríklad:

````
git clone https://github.com/vas-username/first-contributions.git
````

Týmto na svojom počítači vytvoríte priečinok so súbormi daného repozitára.

## Vytvorte vetvu

V príkazovom riadku sa prepnite do zložky s repozitárom (ak v nej už nie ste)

````
cd first-contributions
````

Teraz vytvorte novú vetvu (anglicky *branch*) za použitia príkazu `git checkout`:

````
git checkout -b <meno-novej-vetvy>
````

Napríklad:
````
git checkout -b pridanie-mojho-mena
````

Meno vetvy by malo vypovedať o tom, čo kód alebo čokoľvek iné do nej pridané bude robiť/vykonávať, prípadne prečo sa daná vec deje.

## Urobte zmeny a zaznamenajte ich

Otvorte súbor `Contributors.md` v textovom editore a pridajte do neho svoje meno. Napíšte ho niekam doprostred a súbor uložte.

<img align="right" width="450" ​​src="https://firstcontributions.github.io/assets/Readme//git-status.png" alt="git status" />

Pokiaľ teraz v príkazovom riadku spustíte príkaz `git status`, uvidíte aké zmeny boli v repozitári vykonané.

Tieto zmeny do danej vetvy pridáte príkazom `git add`:

````
git add Contributors.md
````

Zostáva už len potvrdiť (anglicky *commit*) zmeny príkazom `git commit`:

````
git commit -m "Add <vase-meno> to Contributors list"
````

Za prepínač `-m` sa píše čo dané zmeny predstavujú, popis by mal byť jednoduchý ale výstižný.

## Pretlačte zmeny na GitHub

Teraz zmeny vykonané lokálne na počítači pretlačíme (anglicky *push*) na GitHub príkazom `git push`:

````
git push origin <meno-vasej-vetvy>
````

## Predložte svoje zmeny na posúdenie

Pokiaľ sa teraz pozriete do svojho GitHub repozitára, uvidíte tlačidlo **Compare & pull request**. Kliknite naň.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme//compare-and-pull.png" alt="vytvorte pull request" />

Teraz vytvorte žiadosť o pretiahnutie vašej vetvy do originálneho repozitára (anglicky *pull request*).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme//submit-pull-request.png" alt="potvrďte pull request" />

Čoskoro budú správcovia vykonávať zapracovanie vašich zmien do hlavnej (anglicky *master*) vetvy tohto projektu. Až sa do nej vaše zmeny dostanú, dostanete emailové upozornenie.

## Kam ďalej?

Blahoželáme! Práve ste dokončili štandardný _fork -> clone -> edit ->_ priebeh práce (anglicky *workflow), s ktorým sa ako prispievateľ do projektov stretnete dennodenne.

Oslávte svoj prvý príspevok so svojimi priateľmi a nasledovníkmi cez [webovú aplikáciu](https://firstcontributions.github.io/#social-share).

V prípade, ak by ste mali akékoľvek otázky alebo potrebovali pomoc, môžete sa [pridat k našemu Slack teamu](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Teraz vám už nič nebráni v prispievaní do ostatných projektov. Pripravili sme pre vás zoznam projektov, ktoré majú jednoduché záležitosti na vyriešenie/naprogramovanie, s ktorými môžete začať. Pozrite sa [tu](https://firstcontributions.github.io/#project-list).

### [Ďalšie materiály](../additional-material/git_workflow_scenarios/additional-material.md)


## Návod za použitia ďalších nástrojov

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width=" 100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia /commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https:/ /firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md )|[Visual Studio Code](../github-windows-vs-code-tutorial.md)|