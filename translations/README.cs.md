[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# První příspěvek

Život je těžký. Obzvláště když něco děláte poprvé. V případě, že na něčem spolupracujete, není dělání chyb něco, co by vám dělalo radost. My bychom rádi zjednodušili cestu novým přispěvovatelům do open-source při jejich učení se jak na to.

Čtení článků nebo shlédnutí video návodů jsou také cesty, ale co je lepší než si danou věc přímo osahat na vlastní kůži v reálném prostředí? Tento projekt je zaměřen na poskytnutí pomoci začátečníkům s jejich prvním přispěním do open-source. Pokud jste jím právě vy, následujte kroky popsané níže.

#### *Pokud nemáte rádi příkazovou řádku, [zde najdete návody na použití nástrojů s GUI (grafické uživatelské rozhraní)]( #tutorials-using-other-tools )*

#### *Přečtěte si tento článek [v jiných jazycích](translations/Translations.md).*

[🇺🇸](README.md)
[🇮🇳](translations/README.hi.md)
[🇲🇲](translations/README.mm_unicode.md)
[🇮🇩](translations/README.id.md)
[🇫🇷](translations/README.fr.md)
[🇪🇸](translations/README.es.md)
[<img src="assets/catalan1.png" width="22">](translations/README.ca.md)
[🇳🇱](translations/README.nl.md)
[🇱🇹](translations/README.lt.md)
[🇷🇺](translations/README.ru.md)
[🇯🇵](translations/README.ja.md)
[🇻🇳](translations/README.vn.md)
[🇵🇱](translations/README.pl.md)
[🇮🇷](translations/README.fa.md)
[🇮🇷](translations/README.fa.en.md)
[🇰🇷 🇰🇵](translations/README.ko.md)
[🇩🇪](translations/README.de.md)
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
[🏴󠁥󠁳󠁧󠁡󠁿](translations/README.gl.md)
[🇵🇰](translations/README.ur.md)
[:bangladesh:](translations/README.bn.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇹🇷](translations/README.tr.md)
[🇸🇪](translations/README.se.md)
[:slovenia:](translations/README.sl.md)
[🇮🇱](translations/README.hb.md)
[<img src="../assets/pirate.png" width="22">](translations/README.en-pirate.md)


<img align="right" width="300" src="../assets/fork.png" alt="forkněte tento repozitář" />

Pokud namáte nainstalovaný git, [nainstalujte si jej]( https://help.github.com/articles/set-up-git/).

## Forkněte tento repozitář

Forkněte (vytvoření kopie z originálu, z anglického *fork* - *vidlička*, jako vytvoření nové odnože) tento repozitář kliknutím na tlačítko **Fork** nahoře na této stránce. Tím vytvoříte kopii tohoto repozitáře na svém vlastním GitHib účtu.

## Naklonujte repozitář

<img align="right" width="300" src="../assets/clone.png" alt="naklonujte tento repozitář" />

Nyní nakolujte (anglicky *clone*) forknutý repozitář na váš počítač, nakolování není nic jiného než stáhnutí obrazu repozitáře k vám na počítač. Na vašem GitHub účtu si otevřete forknutý repozitář, klikněte na tlačítko **Clone or download** a následně v okýnku, které se objeví, klikněte na tlačítko s ikonkou **copy to clipboard** vedle URL adresy, čímž si ji zkopírujete do schránky.

Teď otevřte terminál a spusťte následující příkaz:

```
git clone "url které jste právě zkopírovali"

```

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="zkopírujte adresu do schránky" />

Například:

```
git clone https://github.com/vase-username/first-contributions.git
```

Tímto na svém počítači vytvoříte složku se soubory daného repozitáře.

## Vytvořte větev

V příkazové řádce se přepněte do složky s repozitářem (pokud v ní už nejste)

```
cd first-contributions
```

Nyní vytvořte novou větev (anglicky *branch*) za použití příkazu `git checkout`:

```
git checkout -b <jmeno-nove-vetve>
```

Například:
```
git checkout -b pridani-meho-jmena
```

Jméno větve by mělo vypovídat o tom, co kód nebo cokoliv jiného do ní přidané bude dělat/vykonávat, případně proč se daná věc děje.

## Udělejte změny a zaznamenejte je

Otevřete soubor `Contributors.md` v textovém editoru a přidejte do něj své jméno. Napiště jej někam doprostřed a soubor uložte.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Pokud teď v příkazové řádce spustíte příkaz `git status`, uvidíte jaké změny byly v repozitáři provedeny.

Tyto změny do dané větvě přidáte příkazem `git add`: 

```
git add Contributors.md
```

Zbýva je teď už jen potvrdit (anglicky *commit*) příkazem `git commit`:

```
git commit -m "Add <vase-jmeno> to Contributors list"
```

Za přepínač `-m` se píše co dané změny představují, popis by měl být jednoduchý ale výstižný.

## Protlačte změny na GitHub

Nyní změny provedené lokálně na počítači protlačíme (anglicky *push*) na GitHub příkazem `git push`:

```
git push origin <jmeno-vasi-vetve>
```

## Předložte své změny k posouzení

Pokud se nyní podíváte do svého GitHub repozitáře, uvidíte tlačítko **Compare & pull request**. Klikněte na něj.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="vytvořte pull request" />

Teď vytvořte žádost o přetažení vaší větve do originálního repozitáře (anglicky *pull request*).

<img style="float: right;" src="../assets/submit-pull-request.png" alt="potvrďte pull request" />

Brzy budu provádět zapracování vašich změn do hlavní (anglicky *master*) větve tohoto projektu. Až se do ní vaše změny dostanou, dostanete emailové upozornění.

## Kam dále?

Blahopřejeme! Právě jste dokončili standardní _fork -> clone -> edit ->_ průběh práce (anglicky *workflow), se kterým se jako přispěvatel do projektů setkáte dennodenně.

Oslavte svůj první příspěvek se svými přáteli a následovníky přes [webovou aplikaci](https://roshanjossey.github.io/first-contributions/#social-share).

V případě, že byste měli jakékoliv otázky nebo potřebovali pomoct, můžete se [přidat k našemu Slack teamu]https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Nyní vám už nic nebrání v příspívání do ostatních projektů. Připravili jsme pro vás seznam projektů, které mají jednoduché záležitosti k vyřešení/naprogramování, se kterými můžete začít. Podívejte se [zde](https://roshanjossey.github.io/first-contributions/#project-list).

### [Další materiály](additional-material/git_workflow_scenarios/additional-material.md)


## Návod za použití dalších nástrojů

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Sebe propagace

Pokud se vm tento projket líbí, dejte mu hvězdičku na [GitHubu](https://github.com/Roshanjossey/first-contributions).
Stránky původního autora [Roshan](https://roshanjossey.github.io/).
[Stránky překladatele](https://bambusekd.cz).


<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
