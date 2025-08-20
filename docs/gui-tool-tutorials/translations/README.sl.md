[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Prvi prispevek

Vsak začetek je težak. Ko sodeluješ z drugimi, so napake še veliko bolj neprijetne. Zato smo se odločili, da novincem olajšamo prispevanje k odprti kodi (ang. Open source).

Branje člankov in sledenje vodičem lahko pomaga, vendar je še vedno najbolje da nove veščine vadimo sami v varnem okolju. Namen tega projekta je da novince vodi in jim olajša prvi prispevek k odprti kodi. Če želite narediti prvi prispevek, sledite spodnjim korakom.

Angleški izrazi so v oklepajih, da dodajo kontekst vsebini.

#### *Če se ne počutite dobro v ukazni vrstici (ang. command line), so tukaj [navodila za uporabo orodij z grafičnim vmesnikom.]( #vodiči-za-uporabo-drugih-orodij )*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Če na svojem računalniku še nimaš "git", si ga [naloži]( https://help.github.com/articles/set-up-git/).

## Ustvari svojo različico repository-ja ( Fork this repository )

S pritiskom na gumb "Fork" na vrhu te strani, ustvari svojo različico repositorya ( pogosto skrajšano v "repo" ) v svojem GitHub računu.

## Kloniraj ta repository ( Clone the repository )

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Sedaj kloniraj ta repository na svoj računalnik. Pojdi v svoj GitHub račun in poišči svojo različico tega repositorya, klikni na gumb "Clone or download" in si kopiraj povezavo. Lahko uporabiš "Ctrl+C" ali pa klikni na ikono na desni strani povezave *copy to clipboard*.

Odpri terminal in se postavi v direktorij, v katerem želiš imeti svojo kopijo repositorya. Nato zaženi naslednji ukaz:

```
git clone "url naslov, ki si ga ravno skopiral"
```
"url naslov, ki si ga ravno skopiral" (brez navednic) je naslov, ki si ga skopiral na Githubu ( naslov tvoje različice projekta ). Glej prejšne korake da dobiš url naslov.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Primer:
```
git clone https://github.com/this-is-you/first-contributions.git
```
`this-is-you` je tvoje GitHub uporabniško ime. Ta ukaz skopira vsebino repositorya "first-contributions" z GitHuba v tvoj računalnik.

## Ustvari vejo ( Create a branch )

Prestavi se v direktorij repositorya na svojem računalniku (če še nisi v njem):

```
cd first-contributions
```
Sedaj ustvari vejo z uporabo ukaza `git checkout`:
```
git checkout -b <add-your-new-branch-name>
```

Primer:
```
git checkout -b add-janez-novak
```
(Ni potrebno da je v imenu veje *add*, vendar je v tem primeru smiselno, ker je namen veje da dodaš svoje ime na seznam.)

## Naredi spremembe in izvedi commmit teh sprememb ( Make necessary changes and commit those changes )

Odpri datoteko `Contributors.md` v urejevalniku besedila in dodaj svoje ime. Ne dodajaj ga na začetek ali konec datoteke, dodaj ga nekje vmes. Shrani datoteko.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Če se postaviš v direktorij projekta in izvedeš ukaz `git status`, vidiš da obstajajo spremembe v projektu.


Dodaj te spremembe veji, ki si jo ravno ustvaril, z ukazom `git add`:

```
git add Contributors.md
```

Sedaj izvedi commit teh sprememb z ukazom `git commit`:
```
git commit -m "Add <your-name> to Contributors list"
```
Zamenjaj `<your-name>` s svojim imenom. Tekst med navednicami je komentar spremembe, ki se shrani s spremembo.

## Pošlji spremembe na GitHub ( Push changes to GitHub )

Pošlji svoje spremembe z ukazom `git push`:
```
git push origin <add-your-branch-name>
```
Zamenjaj `<add-your-branch-name>` z imenom veje, ki si jo ustvaril.

## Vloži svoje spremembe v pregled ( Submit your changes for review )

Če preveriš svoj repository na GitHubu, vidiš gumb `Compare & pull request`. Klikni na ta gumb.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sedaj izvedi submit svojega pull requesta.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Kmalu bom združil tvoje spremembe v master vejo tega projekta. V svoj e-poštni nabiralnik boš dobil sporočilo, da so bile spremembe združene.

##  Kako nadaljevati? ( Where to go from here? )

Čestitke! Pravkar si končal običajni _fork -> clone -> edit -> PR_ potek dela, ki ga boš srečal kot sodelavec v odprto kodnih projektih!

Lahko se pridružiš naši slack ekipi, če rabiš pomoč ali imaš vprašanja. [Pridruži se slack ekipi](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Sedaj lahko začneš prispevati drugim projektom. Sestavili smo seznam projektov z enostavnimi problemi (issues), ki jih lahko začneš reševati. Preveri [seznam projektov v spletni aplikaciji](https://firstcontributions.github.io/#project-list).

### [Dodatne informacije](../additional-material/translations/Slovenian/additional-material.sl.md)


## Vodiči za uporabo drugih orodij

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
