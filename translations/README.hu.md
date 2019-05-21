[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Első hozzájárulás (contribution)

Mindig nehéz valamit elsőre csinálni. Kiváltképp igaz ez mikor együttműködünk valakivel, hibázni nem jó érzés. Ezzel a tananyaggal szeretnénk könyebbé tenni a folyamatot azon open-source contributoroknak (nyílt forráskódhoz hozzájárulóknak) akik még csak most kezdtek bele.

Cikkeket olvasni és oktató videókat nézni segít, de ami igazán segít az a valóságban gyakorolni a folyamatot. A projekt célja hogy segítséget nyújtson és leegyszerűsítse a folyamatot azok számára akik csak most kezdtek bele. Ha te is közéjük tartozol kövesd az alábbi lépéseket.

#### *Ha nem érzed magad magabiztosnak a parancssorban, [itt egy leírás GUI használatával]( #tutorials-using-other-tools )*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Ha még nincs git a gépeden, [installáld]( https://help.github.com/articles/set-up-git/).

## "Fork"old a repot

Kattints a "fork" gombra az oldal tetején, ezzel létrehozod a repo másolatát a saját fiókodban.

## Klónozd (Clone) a repot

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Most klónozd a forkolt repot a saját gépedre. Navigálj a GitHub fiókodra, nyisd meg a forkolt repot, kattints a "Clone" gombra, majd kattints a *copy to clipboard* (*Vágólapra másolás*) ikonra.

Nyisd meg a terminált és futtasd az alábbi git parancsot:

```
git clone "az url amit kimásoltál"
```
ahol "az url amit kimásoltál" (idézőjel nélkül) az url ami erre a repora (a saját forkolt projekted) mutat.
Az előző pontban láthatod, hogyan juthatsz hozzá az url-hez.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Például:
```
git clone https://github.com/ez-a-te-neved/first-contributions.git
```
ahol `ez-a-te-neved` a GitHub felhasználóneved. Ezen a ponton másolod a GitHub first-contributions repo tartalmát a saját gépedre.

## Hozz létre egy branch-ot

Navigálj a repo könyvtárába a gépeden (ha még nem ott vagy):

```
cd first-contributions
```
Most hozz lére egy branch-ot a `git checkout` paranccsal:
```
git checkout -b <szabadon-választott-branch-név>
```

Például:
```
git checkout -b kis-pista-hozzaadasa
```

## Eszközöld a szükséges változtatásokat majd commit-old őket

Nyisd meg a `Contributors.md` filet egy szövegszerkesztőben és add hozzá a neved. Ne a file elejére vagy végére add hanem tetszőlegesen valahova a kettő közé.
Mentsd el a filet.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Ha a projekt könyvtárban lefuttatod a `git status` parancsot, látni fogod a váltaztotásokat.

Add a változtatásokat az általad létrehozott branch-hoz `git add` paranccsal:

```
git add Contributors.md
```

Most commitold a változtatásokat a `git commit` paranccsal:
```
git commit -m "Add <a-te-neved> to Contributors list"
```
helyettesítsd `<a-te-neved>` a saját neveddel.

## Push-old a változtatásokat a GitHubra

Push-old a változtatásokat a `git push` paranccsal:
```
git push origin <a-branch-neve>
```
helyettesítsd `<a-branch-neve>` az általad létrehozott branch nevével.

## Küld a változtatásokat review-ra (felülvizsgálatra)

A repodba navigálva a GitHub-on, nyomd meg a `Compare & pull request` gombot.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Küld el a "pull request"-et.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Hamarosan merge-löm a változtatásaidat a projekt master branch-ába. Amint a változtatások mergelve lettek, kapsz egy email értesítést.  

## Hova tovább?

Gratulálok! Befejeztél egy általános _fork -> clone -> edit -> PR_ folyamatot, amivel gyakran találkozol majd mint contributor!

Ünnepeld meg és oszd meg barátaid és követőid között :  [weboldal](https://firstcontributions.github.io/#social-share).

Csatlakozz a Slack csoportunkhoz ha kérdésed van vagy segítségre van szükséged. [csatlakozz a Slack csoporthoz](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Most már készen állsz hogy más projektekhez is contributolj. Összeraktunk egy listát projektekről, ahol könnyű problémákkal kezdhetsz foglalkozni. [projekt lista](https://firstcontributions.github.io/#project-list).

### [Extra olvasnivalo](additional-material/git_workflow_scenarios/additional-material.md)


## Útmutatók ha más eszközöket használnál

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Ha tetszett a projekt

Ha tetszett a projekt csillagozd be [GitHub](https://github.com/Roshanjossey/first-contributions).
és kövess itt: [Roshan](https://roshanjossey.github.io/) itt:
[Twitter](https://twitter.com/sudo__bangbang) vagy itt:
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>