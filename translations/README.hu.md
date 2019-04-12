[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Első közreműködések

Nehéz. Mindent nehéz elkezdeni. Különösen akkor, amikor hozzájárulsz valamihez, hibákat véteni nem a legkellemesebb dolog. Egyszerűsíteni akartuk hogyan tanulnak és hogyan működnek közre a kezdő közreműködők.

Cikkek olvasása és útmutató videók nézése segít, de mi lehet jobb mint ha saját magad csinálod egy gyakorló környezetben? Ennek a projektnek a célja, hogy segítséget nyújtson és egyszerűsítse, hogyan hozzák létre a kezdők az első közreműködésüket.

#### *Ha nem érzed magad kényelemben a parancssorral, [a GUI-okat alkalmazó útmutatókat itt találod.]( #tutorials-using-other-tools )*

#### *Olvasd ezt [más nyelveken](translations/Translations.md) is.*

[🇮🇳](translations/Translations.md)
[🇲🇲](translations/README.mm_unicode.md)
[🇮🇩](translations/README.id.md)
[🇫🇷](translations/README.fr.md)
[🇪🇸](translations/README.es.md)
[<img src="assets/catalan1.png" width="22">](translations/README.ca.md)
[🇳🇱](translations/README.nl.md)
[🇱🇹](translations/README.lt.md)
[🇷🇺](translations/README.ru.md)
[🇧🇬](translations/README.bg.md)
[:slovakia:](translations/README.slk.md)
[🇯🇵](translations/README.ja.md)
[🇻🇳](translations/README.vn.md)
[🇵🇱](translations/README.pl.md)
[🇮🇷](translations/README.fa.md)
[🇮🇷](translations/README.fa.en.md)
[🇰🇷 🇰🇵](translations/README.ko.md)
[🇩🇪](translations/README.de.md)
[🇩🇰](translations/README.da.md)
[🇨🇳](translations/README.chs.md)
[🇹🇼](translations/README.cht.md)
[🇬🇷](translations/README.gr.md)
[🇪🇬](translations/README.eg.md)
[🇸🇦](translations/README.ar.md)
[🇺🇦](translations/README.ua.md)
[🇧🇷](translations/README.pt_br.md)
[🇵🇹](translations/README.pt-pt.md)
[🇮🇹](translations/README.it.md)
[🇹🇭](translations/README.th.md)
[🏴](translations/README.gl.md)
[🇳🇵](translations/README.np.md)
[🇵🇰](translations/README.ur.md)
[:bangladesh:](translations/README.bn.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇹🇷](translations/README.tr.md)
[🇸🇪](translations/README.se.md)
[🇲🇾](translations/README.my.md)
[:slovenia:](translations/README.sl.md)
[🇮🇱](translations/README.hb.md)
[🇨🇿](translations/README.cs.md)
[<img src="assets/pirate.png" width="22">](translations/README.en-pirate.md)
[🇲🇽](translations/README.mx.md)
[🇵🇭](translations/README.tl.md)
[🇿🇦](translations/README.zul.md)
[🇿🇦](translations/README.afk.md)
[🇰🇪](translations/README.kws.md)
[🇳🇬](translations/README.igb.md)


<img align="right" width="300" src="assets/fork.png" alt='"forkold" ezt a tárolót' />

Ha nincs Git telepítve a gépedre, [telepítsd]( https://help.github.com/articles/set-up-git/)!

## "Forkold" ezt a tárolót

Forkold/villázd ezt a tárolót azzal, hogy a Fork gombra kattintassz az oldal tetején.
Ez egy másolatot készít a tárolóról a te fiókodba.

## Klónozd a tárolót

<img align="right" width="300" src="assets/clone.png" alt="klónozd ezt a tárolót" />

Most klónozd a villázott tárolót a gépedre. Menj a GitHub fiókodra, nyisd meg a villázott tárolót, kattints a Clone gombra azután kattints a *copy to clipboard* ikonra.

Nyiss egy terminált és futtasd az alábbi git parancsot:

```
git clone "url amit kimásoltál"
```
Helyettesítsd be az "url amit kimásoltál" szöveget (idézőjelek nélkül) az urlre amit kimásoltál. Az előző lépések leírják, hogyan szerezd meg az url-t.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="másold az URL-t a vágólapra" />

Például:
```
git clone https://github.com/ez-te-vagy/first-contributions.git
```
Helyettesítsd be az "ez-te-vagy" szöveget a GitHub felhasználónevedre. Ebben az esetben a first-contributions nevű tárolót másolod a gépedre.

## Hozz létre egy ágat

Menj a tároló könyvtárába/mappájába a számítógépeden (ha még nem vagy ott):

```
cd first-contributions
```
Most pedig hozz létre egy új ágat a `git checkout` paranccsal:
```
git checkout -b <az-uj-ag-neve>
```

Például:
```
git checkout -b add-alonzo-church
```
(Az új ág nevének nem kell tartalmaznia az *add* szót, de célszerű, mivel ennek az ágnak a feladata, hogy a nevedet hozzáadja egy listához.)

## Módosítsd a szükséges fájlokat és jelöld ki a változtatásokat

Most pedig nyisd meg a `Contributors.md` fájt egy szövegszerkesztőben és add hozzá a neved. Ne írd a fájl elejére vagy a végére, csak szúrd be valahova. Ha sikerült, mentsd el a fájlt.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />


Hogyha a projekt könyvtárában vagy és lefuttatod a `git status` parancsot, látni fogod, hogy változásokat ír.


Add hozzá a módosításokat az ághoz, amit az előbb csináltál a `git add` paranccsal:

```
git add Contributors.md
```

Most pedig jelöld ki a változásokat:
```
git commit -m "<te-neved> hozzaadva a kozremukodok listajahoz"
```
Cseréld ki a `<te-neved>`-et a neveddel.

## Töltsd fel a változtatásokat a GitHubra

Töltsd fel a változtatásaidat a `git push` paranccsal:
```
git push origin <ird-ide-az-ag-nevet>
```
Cseréld ki az `<ird-ide-az-ag-nevet>` szöveget az ág nevével amit korábban létrehoztál.

## Nyújtsd be a változtatásaidat ellenőrzésre

Ha felmész a tárolód oldalára a GitHubon, látni fogsz egy `Compare & pull request` (Hasonlítsd össze és nyiss behúzási kérelmet) gombot. Kattints rá.

<img style="float: right;" src="assets/compare-and-pull.png" alt="hozz létre egy behúzási kérelmet" />

Küldd el a behúzási kérelmet.

<img style="float: right;" src="assets/submit-pull-request.png" alt="küldd el a behúzási kérelmet" />

Nemsoká minden változtatásod be fogom olvasztani a projekt mester ágába. Kapni fogsz egy emailt, amikor ez megtörténik.

## Hogyan tovább?

Gratulálok!  Elvégezted az általános _forkold -> klónozd -> módosítsd -> PR_ munkafolyamatot, amivel gyakran fogsz találkozni egy közreműködőként!

Ünnepeld meg a közreműködésed és oszd meg a barátaiddal és követőiddel a [webes alkalmazáson](https://firstcontributions.github.io/#social-share).

Csatlakozhatsz a Slack csoportunkba ha segítségre szorulsz vagy van egyéb kérdesed. [Csatlakozz a Slack csoportba](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Most pedig kezdjünk el közreműködni más projekten is. Összeállítottunk egy listát olyan projektekből, amelyekhez könnyű hozzájárulni. Nézd meg [a projektek listáját a webes alkalmazáson](https://firstcontributions.github.io/#project-list).

### [További olvasnivaló](additional-material/git_workflow_scenarios/additional-material.md)


## Útmutatók más eszközök használatával

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Önreklámozás

Ha tetszett ez a projekt, adj neki egy csillagot a [GitHub-on](https://github.com/Roshanjossey/first-contributions).
Hogyha különösen jótékony kedvben vagy, kövesd [Roshan-t](https://roshanjossey.github.io/)
[Twitter-en](https://twitter.com/sudo__bangbang) és
[GitHub-on](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
