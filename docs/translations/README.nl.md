[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Eerste bijdragen

Dit project heeft als doel het versimpelen en het begeleiden van beginners in het maken van hun eerste bijdragen. Als je op het punt staat om je eerste bijdragen te maken, volg dan de onderstaande stappen.

_Als je je niet comfortable voelt met de command line, [zijn hier handleidingen voor het gebruik van GUI tools.](#handleidingen-voor-andere-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork deze repository" />

### Indien git nog niet op je systeem staat, [installeer het dan eerst](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Deze repository forken

Fork deze repository door op de fork-knop bovenaan deze pagina te klikken. Dit creëert een kopie van deze repository in jouw account.

## De repository clonen

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="kloon deze repository" />

Kloon nu de geforkte repository naar je systeem. Ga naar je GitHub-account, open de geforkte repository, klik op de code knop, dan op de SSH tab en klik the _kopieer url naar clipboard_ icon.

Open een terminal en voer het volgende git commando uit:

```bash
git clone "Gekopieerde repository url"
```

Waar "Gekopieerde repository url" (zonder aanhalingstekens) de url naar (jouw fork van) deze repository is. Zie de vorige stappen voor de url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="kopieer URL naar het klembord" />

Bijvoorbeeld:

```bash
git clone git@github.com:dit-ben-jij/first-contributions.git
```

Waar 'dit-ben-jij' staat, vul jij je GitHub gebruikersnaam is. Hiermee kopieer je de inhoud van de first-contributions repo op GitHub naar je systeem.

## Een branch aanmaken

Navigeer naar de map van de repository op je computer (mocht je daar niet al zijn):

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

<details>
<summary> <strong> Als je foutmeldingen krijgt bij het gebruik van git switch, klik dan hier:</strong> </summary> 
Als de foutmelding "Git: `switch` is not a git command. See `git –help`" verschijnt, komt dit waarschijnlijk doordat je een oudere versie van git gebruikt. 
Probeer in dit geval in plaats daarvan `git checkout` te gebruiken:  

```bash 
git checkout -b jouw-nieuwe-branch-naam 
```  
</details>


## Maak de benodigde wijzigingen en commit deze

Open nu het `Contributors.md` bestand in een teksteditor en voeg je naam toe. Doe dit niet aan het begin of eind, maar ergens in het midden. Sla vervolgens het bestand op.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="Uitvoer van git status" />

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
<summary> <strong>Als je foutmeldingen krijgt tijdens het pushen, klik hier:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) voor het genereren en configureren van een SSH-sleutel in je account. 

  Daarnaast kun je 'git remote -v' uitvoeren om je remote-adres te controleren.

  Als het er ongeveer zo uitziet:
  <pre>origin https://github.com/jouw-gebruikersnaam/jouw_repo.git (fetch)
  origin https://github.com/jouw-gebruikersnaam/jouw_repo.git (push)</pre>
  pas het dan aan met dit commando:

  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  Anders zal er nog steeds om een gebruikersnaam en wachtwoord worden gevraagd en krijg je een authenticatiefout.
</details>

## Verstuur je wijzigingen voor review

Als je naar je repository gaat op GitHub, zal je zien dat er een `Compare & pull request` knop staat. Klik hierop.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="creëer een pull request" />

Verstuur nu je pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="verstuur je pull request" />

Binnenkort zal ik al jouw wijzigingen samenvoegen in de main branch van dit project. Je ontvangt een e-mailmelding zodra de wijzigingen zijn samengevoegd.

## Hoe nu verder?

Gefeliciteerd! Je hebt zojuist de standaard _fork -> clone -> edit -> PR_ workflow doorlopen die je vaak zult tegenkomen als bijdrager!

Vier je bijdrage en deel het met je vrienden en volgers via de [web app](https://firstcontributions.github.io/#social-share).

Als je meer wilt oefenen, bekijk dan [code contributions](https://github.com/roshanjossey/code-contributions).

Laten we je nu op weg helpen om bij te dragen aan andere projecten. We hebben een lijst samengesteld van projecten met makkelijke issues waar je mee kunt beginnen. Bekijk [de lijst met projecten in de webapp](https://firstcontributions.github.io/#project-list).


## Handleidingen voor andere tools

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
