[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# První příspěvek

Život je těžký. Obzvláště když něco děláte poprvé. V případě, že na něčem spolupracujete, není dělání chyb něco, co by vám dělalo radost. My bychom rádi zjednodušili cestu novým přispěvatelům do open-source při jejich učení se jak na to.

Čtení článků nebo zhlédnutí video návodů jsou také cesty, ale co je lepší než si danou věc přímo osahat na vlastní kůži v reálném prostředí? Tento projekt je zaměřen na poskytnutí pomoci začátečníkům s jejich prvním přispěním do open-source. Pokud jste jím právě vy, následujte kroky popsané níže.

#### *Pokud nemáte rádi příkazovou řádku, [zde najdete návody na použití nástrojů s GUI (grafické uživatelské rozhraní)](#Návod-za-použití-dalších-nástrojů)*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="forkněte tento repozitář" />

Pokud namáte nainstalovaný git, [nainstalujte si jej]( https://help.github.com/articles/set-up-git/).

## Forkněte tento repozitář

Forkněte (vytvoření kopie z originálu, z anglického *fork* – *vidlička*, jako vytvoření nové odnože) tento repozitář kliknutím na tlačítko **Fork** nahoře na této stránce. Tím vytvoříte kopii tohoto repozitáře na svém vlastním GitHub účtu.

## Naklonujte repozitář

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="naklonujte tento repozitář" />

Nyní naklonujte (anglicky *clone*) forknutý repozitář na váš počítač, naklonování není nic jiného než stáhnutí obrazu repozitáře k vám na počítač. Na vašem GitHub účtu si otevřete forknutý repozitář, klikněte na tlačítko **Clone or download** a následně v okýnku, které se objeví, klikněte na tlačítko s ikonkou **copy to clipboard** vedle URL adresy, čímž si ji zkopírujete do schránky.

Teď otevřete terminál a spusťte následující příkaz:

```
git clone "url které jste právě zkopírovali"

```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="zkopírujte adresu do schránky" />

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

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme//git-status.png" alt="git status" />

Pokud teď v příkazové řádce spustíte příkaz `git status`, uvidíte jaké změny byly v repozitáři provedeny.

Tyto změny do dané větvě přidáte příkazem `git add`:

```
git add Contributors.md
```

Zbývá už jen potvrdit (anglicky *commit*) změny příkazem `git commit`:

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

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme//compare-and-pull.png" alt="vytvořte pull request" />

Teď vytvořte žádost o přetažení vaší větve do originálního repozitáře (anglicky *pull request*).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme//submit-pull-request.png" alt="potvrďte pull request" />

Brzy budou správci provádět zapracování vašich změn do hlavní (anglicky *master*) větve tohoto projektu. Až se do ní vaše změny dostanou, dostanete e-mailové upozornění.

## Kam dále?

Blahopřejeme! Právě jste dokončili standardní _fork -> clone -> edit ->_ průběh práce (anglicky *workflow*), se kterým se jako přispěvatel do projektů setkáte dennodenně.

Oslavte svůj první příspěvek se svými přáteli a následovníky přes [webovou aplikaci](https://firstcontributions.github.io/#social-share).

Pokud byste chtěli více praxe, můžete zkusit [code contributions](https://github.com/roshanjossey/code-contributions).

Nyní vám už nic nebrání v příspívání do ostatních projektů. Připravili jsme pro vás seznam projektů, které mají jednoduché záležitosti k vyřešení/naprogramování, se kterými můžete začít. Podívejte se [zde](https://firstcontributions.github.io/#project-list).

### [Další materiály](../additional-material/git_workflow_scenarios/additional-material.md)


## Návod za použití dalších nástrojů

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
