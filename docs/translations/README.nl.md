[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Eerste bijdragen

Dit project heeft als doel het versimpelen en het begeleiden van beginners in het maken van hun eerste bijdragen. Als je op het punt staat om je eerste bijdragen te maken, volg dan onderstaande stappen.

_Als je je niet comfortable voelt met de command line, vind je [hier handleidingen voor het gebruik van GUI tools.](#handleidingen-voor-andere-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork deze repository" />

### Indien je git nog niet hebt op je systeem, [installeer het dan eerst](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Deze repository forken

Fork deze repository door op de fork knop te klikken. Dit creëert een kopie van deze repository in jouw account.

## De repository clonen

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="kloon deze repository" />

Kloon nu deze repository naar je systeem. Klik op de kloon knop en dan op het kopiëren naar klembord icoon.

Open een terminal en voer het volgende git commando uit:

```bash
git clone "Gekopieerde repository url"
```

Waar "Gekopieerde repository url" (zonder aanhalingstekens) de url naar (jouw fork van) deze repository is. Zie de vorige stappen om de url te vinden.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="kopieer URL naar het klembord" />

Bijvoorbeeld:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

Waar 'this-is-you' staat, vul jij je GitHub gebruikersnaam is. Hiermee kopieer je de inhoud van de first-contributions repo op GitHub naar je systeem.

## Een branch aanmaken

Navigeer naar de map van de repository op je systeem (mocht je daar niet al zijn).

```bash
cd first-contributions
```

Maak nu een branch aan door middel van het `git switch` commando:

```bash
git switch -c je-nieuwe-branch-naam
```

Bijvoorbeeld:

```bash
git switch -c add-alonzo-church
```

## Maak de benodigde wijzigingen en commit deze

Open nu het `Contributors.md` bestand in een teksteditor en voeg je naam toe. Doe dit niet aan het begin of eind, maar ergens in het midden. Sla vervolgens het bestand op.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Als je naar de projectmap gaat en `git status` doet, zul je zien dat er wijzigingen zijn. 

Voeg deze toe aan je branch met behulp van onderstaand `git add` commando.

```bash
git add Contributors.md
```

Commit nu deze wijzigingen door onderstaand `git commit` commando te gebruiken.

```bash
git commit -m "Add jouw-naam to Contributors list"
```

vervang `jouw-naam` met jouw naam

## Push de wijzigingen naar GitHub

Push je wijzigingen met `git push`:

```bash
git push -u origin je-nieuwe-branch-naam
```

Vervang `je-nieuwe-branch-naam` met de naam van de branch die je eerder hebt aangemaakt.


<details>
<summary> <strong>Als je foutmeldingen krijgt tijdens het pushen, klik dan hier:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Ga naar [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) voor het genereren en configureren van een SSH-sleutel in je account.

</details>

## Verstuur je wijzigingen voor review

Als je naar je repository gaat op GitHub, zal je zien dat er een `Compare & pull request` knop staat. Klik hierop.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="creëer een pull request" />

Verstuur nu je pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="verstuur je pull request" />

Nu ga ik (de beheerder) al je wijzigingen mergen in de master branch van dit project. Als de veranderingen gemerged zijn, zul je hier een e-mailnotificatie over ontvangen.

## Hoe nu verder?

Gefeliciteerd! Je hebt zojuist de standaard _fork -> clone -> edit -> PR_ workflow doorlopen die je vaak zult tegenkomen als bijdrager!

Vier je bijdrage en deel het met je vrienden en volgers via de [web app](https://firstcontributions.github.io/#social-share).

Mocht je nog vragen of hulp nodig hebben dan kun je je aanmelden voor ons [Slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Laten we je nu op weg helpen met het bijdragen aan andere projecten. We hebben een lijst samengesteld met projecten die makkelijke issues bevatten waar je aan kunt werken. Bekijk [de lijst op de web app](https://firstcontributions.github.io/#project-list)

## Handleidingen voor andere tools

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |


<p>Dit project is gesponsord door:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
