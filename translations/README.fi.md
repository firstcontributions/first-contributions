[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Ensimmäiset kontribuutiot

Se on vaikeaa. Ensimmäiset kerrat ovat aina vaikeita. Etenkin tehdessä yhteistyötä, virheiden teko ei ole ollenkaan mukavaa. Me halusimme yksinkertaistaa tavan jolla avoimen lähdekoodin kontribuoijat oppivat sekä kontribuoivat ensimmäistä kertaa.

Artikkeleiden lukeminen sekä tutoriaalien katsominen voi auttaa, mutta mikä onkaan parempaa kuin käytännön harjoite harjoitusympäristössä? Tämä projekti tähtää avun tarjoamiseen sekä aloittelijoiden ensimmäisen kontribuution yksinkertaistamiseen. Jos olet aikeissa kontribuoida ensimmäistä kertaa, seuraa alla olevia ohjeita.

#### *Jos et osaa käyttää komentoriviä sulavasti, [täältä löytyy tutoriaaleja GUI-työkalujen käyttöön.](#Muiden-työkalujen-tutoriaaleja)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Jos sinulla ei ole git asennettuna koneellesi, [asenna se](https://help.github.com/articles/set-up-git/).

## Forkkaa tämä repositorio

Forkkaa tämä repositorio klikkaamalla yläkulmassa näkyvää painiketta "Fork". Tämä luo kopion tästä repositoriosta käyttäjällesi.

## Kloonaa repositorio

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Seuraavaksi kloonaa juuri forkkaamasi repositorio koneellesi. Mene GitHub käyttäjäsivuillesi, avaa forkkaamasi repositorio sekä klikkaa "Clone or download"-painiketta jonka jälkeen kopioi osoite painamalla "Copy to clipboard"-ikonia.

Avaa komentorivi ja syötä seuraava git-komento:

```
git clone "Juuri kopioimasi URL"
```

"Juuri kopioimasi URL"-tekstin sijasta (ilman lainausmerkkejä) pastea repositorion URL äskeisestä vaiheesta.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Esimerkiksi:

```
git clone https://github.com/nimesi/first-contributions.git
```

Kirjoita GitHub-käyttäjänimesi 'nimesi' teksin sijaan. Tämä komento kopioi sisällön GitHubisi first contributions-repositorion koneellesi.

## Luo branch

Mene repositoriosi kansioon koneellasi (ellet jo ole siellä).

```
cd first-contributions
```

Seuraavaksi luo branch komennolla `git checkout`:

```
git checkout -b <lisaa-sinun-branchin-nimi>
```

Esimerkiksi:

```
git checkout -b add-matti-meikalainen
```

(Branchin nimeen ei välttämättä tarvitse sisällyttää sanaa *add*, mutta tässä se käy järkeen sillä tämän branchin tarkoitus on lisätä nimesi listaan.)

## Tee tarvittavat muutokset sekä committoi ne

Seuraavaksi avaa `Contributors.md` tiedosto tekstieditorissa ja lisää nimesi tiedostoon. Älä lisää sitä tiedoston alkuun taikka loppuun vaan keskelle. Seuraaksi tallenna tiedosto.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Jos menet projektin kansioon ja syötät komennon `git status`, näet muutokset.

Lisää nuo muutokset branchiin `git add` komennolla:

```
git add Contributors.md
```

Seuraavaksi committoi muutokset `git commit` komennolla:

```
git commit -m "Add <sinun-nimesi> to Contributors list"
```

Korvaamalla `<sinun-nimesi>` nimelläsi.

## Muutosten pushaaminen GitHubiin

Pushaa muutoksesi komennolla `git push`:

```
git push origin <lisaa-branchisi-nimi>
```

Korvaamalla `<lisaa-branchisi-nimi>` nimellä jonka annoit branchillesi aikaisemmin.

## Jätä muutoksesi arvosteltavaksi

Jos menet repositorioosi GitHubissa, näet `Compare & pull request` painikkeen.  Paina tuota painiketta.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Seuraavaksi suorita pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Seuraavaksi mergeän muutoksesi tämän projektin master-branchiin. Tulet saamaan ilmoituksen sähköpostiisi kun muutokset ovat mergetty.

## Mihin seuraavaksi?

Onneksi olkoon! Olet juuri suorittanut tavanomaisen *Fork -> Clone -> Edit -> Pull Request* -työnkulun joka tulee vastaasi usein kontribuoijana!

Juhlista kontribuutiotasi ja jaa se ystävillesi ja followereillesi menemällä [Web Appiin](https://firstcontributions.github.io/#social-share).

Voit liittyä Slack tiimiimme jos sinulla on kysyttävää. [Liity Slack tiimiin](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Jos haluaisit kontribuoida muihin projekteihin, me olemme koonneet listan yksinkertaisista ensimmäisistä issueista työskenneltäväksesi. [Lista löytyy Web-Appistamme](https://firstcontributions.github.io/#project-list).

### [Lisämateriaaleja](../additional-material/git_workflow_scenarios/additional-material.md)

## Muiden työkalujen tutoriaaleja

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
