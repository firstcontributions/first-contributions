[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Első közreműködés nyílt forráskódú projektben

Minden kezdet nehéz, ezért szeretnénk segíteni számodra az első lépésekben ahhoz, hogy bátran kódolj kooperatívan nyílt forráskódú projekteket. Senki sem szeret hibázni, de szerencsére itt most nyugodtan megteheted. A lényeg, hogy gyakorolj!

A projekt célja, hogy útmutatást nyújtson, egyszerűsítse és segítse a kezdők első lépéseit nyílt forráskódú szoftverek közös programozásában. Ha te is most készülsz először ilyet csinálni, segítünk neked, kövesd az alábbi lépéseket.

#### *Ha a parancssor kényelmetlen, [itt egy tutorial a GUI felület használatához.](#Oktatóanyagok-más-eszközök-használatával)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="forkold ezt a repót" />

Ha nincs a gépeden git, [telepítsd fel]( https://help.github.com/articles/set-up-git/).

## Ágaztasd ezt a repót (fork)

A Fork gomb kattintásával ágaztasd el ezt a repót.
Ezzel készítettél egy másolatot erről a reporól a te saját git fiókodba.

## Klónozd a repót (clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="klónozd ezt a repót" />

Most klónozd az elágaztatott repót a gépedre. Menj a GitHub fiókodra, nyisd meg a forkolt repositoryt, kattints a clone gombra, majd kattints a *copy to clipboard* ikonra.

Nyiss egy terminált és futtasd a következő parancsot:

```
git clone "url-amit-most-masoltal-le"
```
A "url-amit-most-masoltal-le" kifejezést, cseréld ki (idézőjelek nélkül) a vágólapra helyezett repository url címére (ami ebből a projektől ágazik). Az ágaztatás folyamatát lásd az előző lépésben.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="másold az URL címet a vágólapra" />

Például:
```
git clone https://github.com/a-te-git-neved/first-contributions.git
```
A `a-te-git-neved` lesz a GitHub felhasználóneved. Ezzel letöltöd a first-contributions repositoryt GitHub-ról a saját számítógépedre.

## Készíts egy ágat (branch)

Navigálj a repository könytárába (ha nem ott vagy jelenleg):

```
cd first-contributions
```

Most készítsünk egy ágat `git checkout` parancs használatával:

```
git switch -c <az-uj-branch-neve>
```

Például:
```
git switch -c add-gabor-takacs
```
(A branch nevében nem kötelező, hogy benne legyen az *add* szó, de észszerű belefoglalni, mert ennek az ágnak az a célja, hogy hozzáadja a nevünket egy listához.)

## Végezd el a szükséges változtatásokat és rögzítsd azokat (commit)

Nyisd meg a `Contributors.md` fájlt egy szövegszerkesztőben, majd add hozzá a neved. Ne a fájl elejére vagy végére helyezd, hanem a kettő közé. A kettő között bárhová teheted. Mentsd el a fájlt.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Ha a project könyvtárába navigálsz és futtatod a `git status` parancsot, akkor a következő módosításokat fogod látni:


Ezeket a módosításokat add hozzá a branchez a `git add` paranccsal:

```
git add Contributors.md
```

Commitoljuk a módosításokat a `git commit` paranccsal:
```
git commit -m "Add <a-te-neved> to Contributors list"
```
Helyettesítsd `<a-te-neved>` kifejezést a saját neveddel.

## Töltsd fel az elkészült változtatásokat a GitHub-ra (push)

Töltsd fel a változtatásokat a `git push` paranccsal:
```
git push origin <a-branch-neve>
```
Helyettesítsd az `<a-branch-neve>` kifejezést annak a branchnek a nevével, amit korábban létrehoztál.

## Küldd be a módosításaidat ellenőrzésre (pull request)

Ha a saját repódba navigálsz GitHub-on, látnod kell a `Compare & pull request` gombot. Kattints rá!

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="pull request készítése" />

Sikeresen elküldted a pull requested.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="pull request beküldése" />

Kis idő elteltével összevonja a változásokat a project fő ágában. Értesítést fogsz kapni emailben, ha a változások összefűzésre kerültek.

## Hogyan tovább?

Gratulálunk! Sikeresen teljesítetted az alapvető _fork -> clone -> edit -> PR_ folyamatot, melyet gyakran kell majd csinálnod közreműködőként!

Ünnepeld meg az első kooperációdat és oszd meg barátaiddal és követőiddel ennek a [web app](https://firstcontributions.github.io/#social-share)-nak a segítségével.

Bármilyen kérdésed van vagy segítségre lenne szükséged, csatlakozz slack csapatunkhoz. [Csatlakozz a slack csapathoz.](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Itt az idő egy másik projektben is közreműködni. Összeállítottunk egy listát azokról a projektekről, melyek könnyebb feladatokat tartalmaznak az induláshoz. Nézd meg a [projektek listáját](https://firstcontributions.github.io/#project-list) a webalkalmazásban.

### [Kiegészítő anyag](../additional-material/git_workflow_scenarios/additional-material.md)


## Oktatóanyagok más eszközök használatával

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
