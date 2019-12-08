[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="/assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Første bidrag

Det er alltid vanskelig å gjøre noe for første gang. Spesielt når man samarbeider med andre kan det være tungt å gjøre feil. Vi ønsker å gjøre det lettere for nybegynnere å bidra til open-source.

Å lese artikler og se videoer kan hjelpe, men hva kan vel være bedre enn å gjøre det i praksis? Dette prosjektet håper å kunne tilby en enkel veiledning og gjøre det lett for nybegynnere å gi sitt første bidrag. Følg trinnene nedenfor hvis du ønsker å gi ditt første bidrag til dette prosjektet.

#### *Hvis du ikke er komfortabel med terminal, [så finnes det andre metoder](#veiledning-for-andre-verktøy).*

#### *Les dette på [andre språk (other languages)](/translations/Translations.md).*

<img align="right" width="300" src="/assets/fork.png" alt="fork this repository" />

Om du ikke har git installert på din maskin, [følg denne veiledningen](https://help.github.com/articles/set-up-git/).

## Fork dette prosjektet

Fork prosjektet ved å klikke på "fork" knappen på toppen av denne siden. Dette vil legge til en kopi av dette prosjektet til din GitHub konto (prosjekter kalles repository på GitHub).

## Clone prosjektet

<img align="right" width="300" src="/assets/clone.png" alt="clone this repository" />

Nå skal vi klone prosjektet fra GitHub til din maskin. Gå til din GitHub konto og åpne din nye fork, deretter klikk på "clone" knappen og kopier linken.

Åpne en terminal/kommandolinje og kjør følgende git kommando:
```
git clone <din-link>
```
Erstatt `<din-link>` med linken du kopierte i forrige trinn.

<br><img align="right" width="300" src="/assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Eksempel:
```
git clone https://github.com/ditt-brukernavn/first-contributions.git
```
hvor `ditt-brukernavn` er ditt GitHub brukernavn. Her kopierer vi innholdet i first-contributions prosjektet fra din GitHub konto til din lokale maskin.

## Opprett en branch

Naviger terminalen inn i prosjektet (hvis du ikke er der allerede):
```
cd first-contributions
```

Opprett en branch med `git checkout` kommandoen:
```
git checkout -b <navn-til-branch-her>
```

Eksempel:
```
git checkout -b add-alonzo-church
```
Navnet på din branch behøver ikke å inneholde ordet *add*, men det gir mening å inkludere det i denne sammenhengen. Endre "alonzo-church" til ditt navn.

## Lag endringer og commit dem

Åpne filen `Contributors.md` i et program for å redigere tekst og legg til ditt navn i listen. Ikke legg det til i begynnelsen eller slutten av filen, legg det til hvor som helst i mellom. Når du har gjort dette kan du lagre filen.

<img align="right" width="450" src="/assets/git-status.png" alt="git status" />


Hvis du åpner terminalen igjen og kjører kommandoen `git status`, vil du se dine endringer.


Legg endringene til i din nye branch med kommandoen `git add`:
```
git add Contributors.md
```

Commit endringene med kommandoen `git commit`:
```
git commit -m "Add <ditt-navn> to Contributors list"
```
Erstatt `<ditt-navn>` med ditt navn.

## Push endringene til GitHub

Push til GitHub med kommandoen `git push`:
```
git push origin <navn-på-din-branch>
```
Erstatt `<navn-på-din-branch>` med navnet på branch som du opprettet tidligere.

## Send inn endringene for gjennomgang

Hvis du går til ditt prosjekt på GitHub, vil du se en `Compare & pull request` knapp. Klikk på den for å opprette en pull request.

<img style="float: right;" src="/assets/compare-and-pull.png" alt="create a pull request" />

Send inn din pull request når du er klar.

<img style="float: right;" src="/assets/submit-pull-request.png" alt="submit pull request" />

Snart vil jeg merge dine endringer inn i master branch av mitt prosjekt. Du vil motta en notifikasjon på epost når dine endringer er lagt til.

## Hva nå?

Gratulerer! Du har gjennomført standardprosessen for _fork -> clone -> edit -> PR_, en prosess du vil møte på ofte!

Feir ditt bidrag og del det med dine venner og følgere ved å gå til [web app](https://firstcontributions.github.io/#social-share).

Behøver du hjelp eller vil stille spørsmål så kan du bli med i vår slack-gruppe. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

Nå kan du gå videre og bidra til andre open-source prosjekter. Vi har satt sammen en liste med enkle og overkommelige problemer du kan starte med. Sjekk den ut her: [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Ekstramateriale](/additional-material/git_workflow_scenarios/additional-material.md)


## Veiledning for andre verktøy

|<a href="/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="/gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](/github-desktop-tutorial.md)|[Visual Studio 2017](/github-windows-vs2017-tutorial.md)|[GitKraken](/gitkraken-tutorial.md)|[Visual Studio Code](/github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](/sourcetree-macos-tutorial.md)|
