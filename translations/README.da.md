[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Første bidrag

Det er svært. Det er altid svært når det er første gang. Specielt hvis man samarbejder er det ikke rart at begå fejl. Vi vil simplificere den store udfordring det er for nybegyndere at lære om open-source, og at lave deres f'rste bidrag.

At læse artikler og se video guides hjælper, men hvad er bedre end at bruge det i praksis? Dette projekt håber at kunne tilbyde vejledning og gøre det overkommeligt for alle at lave deres første open-source bidrag.

#### *Hvis du ikke er komfortabel med command line, [her er vejledninger til GUI værktøjer]( #tutorials-using-other-tools )*

#### *Læs dette i [andre sprog](translations/Translations.md).*

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
[🇵🇰](translations/README.ur.md)
[:bangladesh:](translations/README.bn.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇹🇷](translations/README.tr.md)
[🇸🇪](translations/README.se.md)
[:slovenia:](translations/README.sl.md)
[🇮🇱](translations/README.hb.md)
[<img src="assets/pirate.png" width="22">](translations/README.en-pirate.md)



<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />

Har du ikke Git på din maskine kan du [installere det]( https://help.github.com/articles/set-up-git/).

## Fork dette repository

Fork dette repo ved at klikke på "fork" knappen øverst på siden.
Dette vil lave en kopi af projektet i din Github konto.

## Clone dette repository

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

Næste trin er at "clone" dit nye repository til din maskine. Naviger til din Github account og åbn dit nye repository, derefter find "clone" øverst oppe og tryk på knappen. Tryk *copy to clipboard* ikonet.

Åbn en terminal og kør den følgende git command:

```
git clone "din url"
```

hvor "din url" skal erstattes med den URL du kopieret i forrige trin.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Eksempel:
```
git clone https://github.com/dit-brugernavn/first-contributions.git
```
Erstat 'dit-brugernavn' med dit GitHub brugernavn. Her kopierer vi indholdet af first-contributions repositoriet fra din Github konto, til din lokale PC.

## Opret en branch

Åbn en konsol og cd til dit lokale repository (hvis ikke du allerede er der):

```
cd first-contributions
```
Derefter opretter du en branch med kommandoen `git checkout`:
```
git checkout -b <add-your-change>
```

Eksempel:
```
git checkout -b add-alonzo-church
```
(Navnet på din branch behøver ikke at indeholde ordet *add*, men det giver mening at inkludere det her da branchen er til for at tilføje dit navn til en liste med navne.)

## Lav dine ændringer og commit dem

Åben filen `Contributors.md` i en text editor og tilføj dit navn til listen. Undgå at tilføje dit navn øverst eller nederst på listen, men helst et sted i mellem. Når dette er gjort så gem filen.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />


Hvis du går til konsollen og kører kommandoen `git status`, vil du se dine ændringer.


Tilføj disse ændringer til din branch med kommandoen `git add`:
```
git add Contributors.md
```

Derefter commit ændringerne med kommandoen `git commit`:
```
git commit -m "Add <dit-navn> to Contributors list"
```
Erstat `<dit-navn>` med dit Github brugernavn.

## Push ændringer til Github

Push dine ændringer til Github med kommandoen `git push`:
```
git push origin <add-din-branch>
```
Erstat `<add-din-branch>` med navnet på den branch du oprettede tidligere.

## Indgiv ændringer til inspektion

Hvis du går ind på dit repository på Github, så vil du se en `compare & pull request` knap. Klik på den.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Indgiv nu din pull request.

<img style="float: right;" src="assets/submit-pull-request.png" alt="submit pull request" />

Snart vil jeg merge dine ændringer ind i master branch'en af projektet. Du vil modtage en notifikation per email når dine ændringer er blevet merget.

## Hvor til nu?

Tillykke! Du har nu gennemført den udbredte _fork -> clone -> edit -> PR_ workflow som du vil støde oftest på som contributor!

Fejr dit bidrag og del det med dine venner og følgere ved at gå til [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Du er velkommen til at kigge forbi vores Slack hvis du mangler hjælp, eller har spørgsmål. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Tillad os også at hjælpe dig i gang med dine næste bidrag. Vi har kompileret en liste af projekter med letty, overkommelige problemer du kan starte ud med. Check den ud her: [the list of projects in web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [ekstra materiale](additional-material/git_workflow_scenarios/additional-material.md)


## Guides med andre værktøjer

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Selv-forfremmelse

Hvis du kan lide dette projekt så 'star' os på [GitHub](https://github.com/Roshanjossey/first-contributions).
Føler du dig ekstra generøs kan du følge os på [Roshan](https://roshanjossey.github.io/), på [Twitter](https://twitter.com/sudo__bangbang) og på [GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="https://github.com/firstcontributions/first-contributions/raw/master/assets/saasgrids-banner.png" width="500"></a>
