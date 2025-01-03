[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Eerste Bydraes

Dit is moeilik. Dit is altyd moeilik om die eerste keer iets te doen. Veral wanneer jy saamwerk, maak foute nie 'n gemaklike ding nie. Ons wou die manier waarop nuwe open source bydraers vir die eerste keer leer en bydra, vereenvoudig.

Lees artikels en kyk tutoriale kan help, maar wat is beter as om die goed in die praktyk te doen? Hierdie projek het ten doel om leiding te gee en die manier waarop beginners hul eerste bydrae maak, te vereenvoudig. As jy jou eerste bydrae wil maak, volg die onderstaande stappe.

#### *As jy nie gemaklik is met die opdraglyn nie, [is daar tutoriale wat GUI-instrumente gebruik.](#Bykomende-materiaal )*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

As jy nie git op jou masjien het nie, [installeer dit]( https://help.github.com/articles/set-up-git/).

## Vork hierdie bewaarplek

Vork hierdie repo deur op die vurk knoppie bo-aan hierdie bladsy te klik. Dit sal 'n kopie van hierdie repository in u rekening skep.

## Klone die repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Klone nou die vurk repo aan jou masjien. Gaan na jou GitHub-rekening, maak die vurk repo oop, klik op die kloonknop en klik dan op die kopie na die knipbord- ikoon.

Open 'n terminaal en voer die volgende git opdrag uit:

```
git clone "url you just copied"
```

waar "url jy net gekopieer" het (sonder die aanhalingstekens) is die url na hierdie repository (jou vurk van hierdie projek). Sien die vorige stappe om die url te verkry.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Byvoorbeeld:

```
git clone https://github.com/this-is-you/first-contributions.git
```

waar `this-is-youis` jou GitHub gebruikersnaam Hier kopieer jy die inhoud van die eerste bydrae repository in GitHub na jou rekenaar.

## Skep 'n tak

Verander na die repository gids op jou rekenaar (as jy nie reeds daar is nie):

```
cd first-contributions
```

Skep nou 'n tak met die git `checkout` opdrag:

```
git checkout -b <add-your-new-branch-name>
```

Byvoorbeeld:

```
git checkout -b add-alonzo-church
```

(Die naam van die tak hoef nie die woord by te voeg nie, maar dit is 'n redelike ding om in te sluit omdat die doel van hierdie tak is om jou naam by 'n lys te voeg.)

## Maak die nodige veranderinge en verbind die veranderinge

Nou oop `Contributors.md` lêer in 'n teksredigeerder, voeg jou naam daarby. Moet dit nie aan die begin of einde van die lêer byvoeg nie. Sit dit oral tussenin. Stoor nou die lêer.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

As u na die projekgids gaan en die opdrag uitvoer `git status`, sal u sien dat daar veranderinge is.


Voeg die veranderinge by die tak wat jy net geskep het deur die `git add` opdrag te gebruik:

```
git add Contributors.md
```

Doen nou die veranderinge deur die `git commit` opdrag te gebruik:

```
git commit -m "Add <your-name> to Contributors list"
```

vervang `<your-name>` met jou naam.

## Druk veranderinge na GitHub

Druk jou veranderinge deur die opdrag te gebruik `git push`:

```
git push origin <add-your-branch-name>
```

vervang `<add-your-branch-name>` met die naam van die tak wat jy vroeër geskep het.

## Dien jou veranderinge in vir hersiening

As jy na jou repository op GitHub gaan, sal jy 'n `Compare & pull` requestknoppie sien. Klik op daardie knoppie.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Dien nou die trekversoek in.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Binnekort sal ek al jou veranderinge in die meestertak van hierdie projek saamsmelt. U sal 'n kennisgewing-e-pos ontvang sodra die veranderinge saamgesmelt is.

## Waarheen gaan jy vandaan?

Geluk! Jy het net die standaardvurk voltooi -> klone -> wysig -> PR- werkvloei wat jy dikwels as 'n bydraer sal ervaar!

Vier jou bydrae en deel dit met jou vriende en volgelinge deur na die [webprogram te](https://firstcontributions.github.io/#social-share) gaan .

U kan by ons span aansluit indien u enige hulp nodig het of enige vrae het. [Sluit aan by 'n slapende span](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Kom ons begin met die bydrae tot ander projekte. Ons het 'n lys van projekte saamgestel met maklike probleme waarmee u kan begin. Kyk na [die lys van projekte in die web app](https://firstcontributions.github.io/#project-list).

### [Bykomende materiaal](../additional-material/git_workflow_scenarios/additional-material.md)

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visuele Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visuele Studio Kode](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
