[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Første bidrag

Det er svært. Det er altid svært når det er første gang. Specielt hvis man samarbejder er det ikke rart at begå fejl. Vi vil simplificere den store udfordring det er for nybegyndere at lære om open-source, og at lave deres første bidrag.

At læse artikler og se video guides hjælper, men hvad er bedre end at bruge det i praksis? Dette projekt håber at kunne tilbyde vejledning og gøre det overkommeligt for alle at lave deres første open-source bidrag.

#### *Hvis du ikke er komfortabel med command line, [her er vejledninger til GUI værktøjer](#Guides-med-andre-værktøjer)*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Har du ikke Git på din maskine kan du [installere det]( https://help.github.com/articles/set-up-git/).

## Fork dette repository

Fork dette repo ved at klikke på "fork" knappen øverst på siden.
Dette vil lave en kopi af projektet i din Github konto.

## Clone dette repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Næste trin er at "clone" dit nye repository til din maskine. Naviger til din Github account og åbn dit nye repository, derefter find "clone" øverst oppe og tryk på knappen. Tryk *copy to clipboard* ikonet.

Åbn en terminal og kør den følgende git command:

```
git clone "din url"
```

hvor "din url" skal erstattes med den URL du kopieret i forrige trin.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

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

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


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

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Indgiv nu din pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Snart vil jeg merge dine ændringer ind i master branch'en af projektet. Du vil modtage en notifikation per email når dine ændringer er blevet merget.

## Hvor til nu?

Tillykke! Du har nu gennemført den udbredte _fork -> clone -> edit -> PR_ workflow som du vil støde oftest på som contributor!

Fejr dit bidrag og del det med dine venner og følgere ved at gå til [web app](https://firstcontributions.github.io/#social-share).

Du er velkommen til at kigge forbi vores Slack hvis du mangler hjælp, eller har spørgsmål. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Tillad os også at hjælpe dig i gang med dine næste bidrag. Vi har kompileret en liste af projekter med letty, overkommelige problemer du kan starte ud med. Check den ud her: [the list of projects in web app](https://firstcontributions.github.io/#project-list).

### [ekstra materiale](../additional-material/git_workflow_scenarios/additional-material.md)


## Guides med andre værktøjer

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
