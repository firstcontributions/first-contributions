
[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Første Bidrag

Det er alltid en utfordring å gjøre noe for første gang. Spesielt i samarbeid med andre kan det virke skremmende å gjøre feil. Vi ønsker å gjøre det enklere for nybegynnere å bidra til open source-prosjekter.

Å lese artikler og se videoer kan være nyttig, men hva er vel bedre enn å lære ved å gjøre? Dette prosjektet er ment som en enkel veiledning for å senke terskelen for nybegynnere som ønsker å gi sitt første bidrag. Følg trinnene nedenfor for å gi ditt første bidrag til dette prosjektet.

_Dersom du ikke er komfortabel med terminalen, [finnes det alternative metoder ved bruk av grafiske grensesnitt (GUI).](#tutorials-using-other-tools)_

#### Hvis du ikke har Git installert på maskinen din, [følg denne veiledningen](https://help.github.com/articles/set-up-git/).
<br/><br/>

## Fork prosjektet

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

«Fork» prosjektet ved å klikke på "Fork"-knappen øverst på siden. Dette vil opprette en kopi av prosjektet under din GitHub-konto (prosjekter kalles «repositories» på GitHub).
<br/><br/>
<br/><br/>

## Klon prosjektet

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Nå skal vi klone prosjektet fra GitHub til din maskin. Gå til din GitHub-konto og åpne din nylig «forkede» versjon. Klikk på "Clone"-knappen og kopier lenken.

Åpne en terminal eller kommandolinje og kjør følgende Git-kommando:

```bash
git clone "din-lenke"
```

Erstatt `<din-lenke>` med lenken du kopierte i forrige trinn.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Eksempel:

```bash
git clone https://github.com/ditt-brukernavn/first-contributions.git
```

Her er `ditt-brukernavn` ditt GitHub-brukernavn. Dette kopierer innholdet i «first-contributions»-prosjektet fra din GitHub-konto til din lokale maskin.
<br/><br/>
<br/><br/>

## Opprett en ny branch

Naviger terminalen til prosjektmappen (hvis du ikke allerede er der):

```bash
cd first-contributions
```

Opprett en ny branch ved hjelp av `git checkout`-kommandoen:

```bash
git checkout -b <navn-på-branch>
```

Eksempel:

```bash
git checkout -b legg-til-ditt-navn
```
Navnet på din branch trenger ikke å inneholde ordet «legg-til», men det gir mening i denne sammenhengen. Erstatt «legg-til-ditt-navn» med et beskrivende navn, gjerne inkludert ditt eget navn.
<br/><br/>

## Gjør de nødvendige endringene og «commit» dem

Åpne filen `Contributors.md` i et tekstredigeringsprogram og legg til ditt navn i listen. Plasser navnet ditt et sted i midten av listen, ikke i begynnelsen eller slutten. Når du er ferdig, lagre filen.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Hvis du åpner terminalen igjen og kjører kommandoen `git status`, vil du se endringene du har gjort.

«Stage» endringene til din nye branch med kommandoen `git add`:

```bash
git add Contributors.md
```

«Commit» endringene med kommandoen `git commit`:

```bash
git commit -m "Legg til <ditt-navn> i listen over bidragsytere"
```

Erstatt `<ditt-navn>` med ditt eget navn.
<br/><br/>

## «Push» endringene til GitHub

«Push» endringene til GitHub med kommandoen `git push`:

```bash
git push origin <navn-på-din-branch>
```

Erstatt `<navn-på-din-branch>` med navnet på branchen du opprettet tidligere.

<details>
<summary> <strong>Hvis du får feilmeldinger når du «pusher» til GitHub, klikk her:</strong> </summary>

- ### Autentiseringsfeil
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Gå til [GitHubs veiledning](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) for å generere og konfigurere en SSH-nøkkel for kontoen din.

</details>
<br/><br/>

## Send inn endringene for gjennomgang

Når du går til prosjektet ditt på GitHub, vil du se en «Compare & pull request»-knapp. Klikk på den for å opprette en «pull request».

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Send inn din «pull request» når du er klar.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Jeg vil snart «merge» endringene dine inn i «master»-branchen av prosjektet mitt. Du vil motta et e-postvarsel når endringene dine er lagt til.
<br/><br/>

## Hva nå?

Gratulerer! Du har fullført standardprosessen for _fork -> clone -> edit -> PR_, en prosess du kommer til å møte ofte!

Feire bidraget ditt og del det med venner og følgere ved å gå til [nettappen](https://firstcontributions.github.io/#social-share).

Hvis du trenger hjelp eller har spørsmål, kan du bli med i vår Slack-gruppe: [Bli med i Slack-gruppen](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Nå kan du gå videre og bidra til andre open source-prosjekter. Vi har satt sammen en liste med enkle og overkommelige oppgaver du kan starte med. Sjekk den ut her: [listen over prosjekter i nettappen](https://firstcontributions.github.io/#project-list).
<br/><br/>

### [Ekstramateriell](additional-material/git_workflow_scenarios/additional-material.md)

## Veiledninger for andre verktøy

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Dette prosjektet støttes av:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
