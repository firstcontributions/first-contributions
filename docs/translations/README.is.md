# First-Contributions

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Fyrstu framlög

Þetta verkefni miðar að því að einfalda og leiðbeina byrjendum í gegnum fyrsta framlag þeirra. Ef þú vilt gera þitt fyrsta framlag, fylgdu þá skrefunum hér að neðan.

_Ef þú ert ekki þægileg(ur) með skipanalínu, [hér eru leiðbeiningar með því að nota GUI verkfæri.](#Leiðbeiningar-með-öðrum-verkfærum)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Ef þú ert ekki með Git uppsett á tölvunni þinni, [settu það upp](https://help.github.com/articles/set-up-git/).

## Forkaðu þetta geymsla

Forkaðu þessa geymslu með því að smella á "Fork" hnappinn efst á þessari síðu.
Þetta mun búa til afrit af geymslunni á þínum GitHub reikningi.

## Klónaðu geymsluna

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Núna klónaðu forkaða geymsluna á þína tölvu. Farðu á GitHub reikninginn þinn, opnaðu forkaða geymsluna, smelltu á "Code" hnappinn og smelltu síðan á "copy to clipboard" táknið.

Opnaðu terminal og keyrðu eftirfarandi git skipun:

```
git clone "url sem þú afritaðir"
```
þar sem "url sem þú afritaðir" (án gæsalappa) er slóðin á geymsluna (þitt fork af þessu verkefni). Sjá fyrri skref til að fá slóðina.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Til dæmis:
```
git clone https://github.com/þitt-notandanafn/first-contributions.git
```
þar sem `þitt-notandanafn` er þitt GitHub notandanafn. Hér ertu að afrita innihald first-contributions geymslunnar á GitHub yfir á þína tölvu.

## Búðu til grein

Farðu í geymsluskrána á tölvunni þinni (ef þú ert ekki þegar þar):

```
cd first-contributions
```
Nú búðu til grein með því að nota `git checkout` skipunina:
```
git checkout -b <bæta-við-þitt-nafn>
```

Til dæmis:
```
git checkout -b add-jon-jonsson
```
(Nafn greinarinnar þarf ekki að innihalda orðið *add* en það er skynsamlegt að hafa það með þar sem tilgangur þessarar greinar er að bæta nafninu þínu við lista yfir framlagsmenn.)

## Gerðu nauðsynlegar breytingar og commit-aðu þær

Nú opnaðu `Contributors.md` skrána í textaritli og bættu nafninu þínu við. Ekki bæta því við í upphafi eða enda skrárinnar. Settu það hvar sem passar miðað við stafrófsröð. Vistaðu síðan skrána.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ef þú ferð í verkefnismöppuna og framkvæmir skipunina `git status`, þá muntu sjá að það eru breytingar.

Bættu þessum breytingum við greinina sem þú bjóst til með `git add` skipuninni:

```
git add Contributors.md
```

Nú commit-aðu þessar breytingar með `git commit` skipuninni:
```
git commit -m "Add <þitt-nafn> to Contributors list"
```
og settu þitt nafn í staðinn fyrir `<þitt-nafn>`.

## Ýttu breytingunum á GitHub

Ýttu breytingunum þínum með `git push` skipuninni:
```
git push origin <nafn-á-grein-þinni>
```
og settu nafnið á greininni sem þú bjóst til áður í staðinn fyrir `<nafn-á-grein-þinni>`.

## Sendu inn breytingarnar þínar til yfirferðar

Ef þú ferð í geymsluna þína á GitHub, þá muntu sjá `Compare & pull request` hnapp. Smelltu á þann hnapp.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Nú sendu inn pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Fljótlega mun ég sameina allar breytingarnar þínar við aðalgrein þessa verkefnis. Þú færð tilkynningu í tölvupósti þegar breytingarnar hafa verið sameinaðar.

## Hvað næst?

Til hamingju! Þú hefur nú lokið við hefðbundið _fork -> clone -> edit -> pull request_ verkflæði sem þú munt oft rekast á sem framlagsmaður!

Fagnaðu framlagi þínu og deiltu því með vinum þínum og fylgjendum með því að fara á [vefappið](https://firstcontributions.github.io/#social-share).


### [Viðbótarefni](additional-material/git_workflow_scenarios/additional-material.md)

## Leiðbeiningar með öðrum verkfærum

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md) |
