[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Ensimmäinen osallistumiseni

Tämän projektin tarkoitus on opastaa ensimmäisessä git -projektiin osallistumisessa. Se ei ole vaikeaa ja tässä dokumentissa on ohjeet, kuinka teet ensimmäisen osallistumisesi avoimen lähdekoodin projektissa.

Artikkeleiden sekä tutoriaalien läpikäynti voi auttaa, mutta mikä onkaan parempaa kuin käytännön harjoite todellisessa ympäristössä? Seuraa vain alla olevia ohjeita ja voit aloittaa matkasi avoimen lähdekoodin tukemisessa.

## Terminologiasta

Monet sanat ovat käännettävissä englannista suomenkieleen suoraan. Tämä niin sanottu *finglish* on liiankin tuttua meille, mutta tässä dokumentaatiossa on pyritty käyttämään suomenkielisiä sanoja, jotka ovat helppo ymmärtää ja jotka toivottavasti auttavat ohjeiden noudattamisessa. Käytämme englanninkielistä sanaa ohjeiden ohessa, jos ohje sillä kohtaa sitä vaatii. Ohessa muutama sana selitettynä.

- **Repository**: Arkisto,projekti. Repository on arkisto, jossa on kokoelma tiedostoja ja kansioita.
- **Contribution**: Osallistuminen arkistoon omalla työpanoksella.
- **Fork**: Haaroittaminen (haarukka). Tarkoittaa, että kopioidaan arkiston tiedostot omalle git-tilille.
- **Clone**: Kloonaaminen. Arkiston kopiointi omalle tai muulle koneelle.
- **Branch**: Haara. Git seuraa arkiston tiedostojen muutoksia ja nämä muutokset voidaan haaroittaa eli "forkata" halutulla tavalla. Mahdollistaa sen, että useat osallistujat voivat tehdä muutoksia arkistoon samanaikaisesti (ns. hajautettu kehitys).
- **Commit**: "Tekeminen","Sitoutuminen". Kun teet muutoksia arkiston tiedostoihin, sinun pitää sitoutua niihin. Eli sana "commit" tarkoittaa arkistossa sitä, että "sitoudumme tekemään tietyt muutokset arkistoon". Commit on git-komento ja halutut sitoutumiset voidaan aina valita tiedostokohtaisesti.
- **Push**: "Työntö". Projektin tiedostojen muutosten lähettäminen arkistoon.
- **Pull**: "Veto". Arkiston ajantasaisten tiedostojen nouto.
- **Pull request**: "Vetopyyntö". Pyyntö arkiston ylläpitäjille, että muutoksesi sulautettaisiin osaksi arkistoa, eli vedettäisiin osaksi arkistoa.

## Mitä teemme nyt?

Tämä ohje on osana GitHub-arkistoa. Tässä ohjeess:

1. Haaroitamme tämän arkiston ja kloonaamme sen koneelle (We will fork and clone the repository)
2. Haaroitamme arkiston (We will create a new branch)
3. Teemme muutoksia arkiston tiedostoihin ja sitoudumme niihin (We will make some changes, commit and push them)
4. Lähetämme vetopyynnön arkiston ylläpitäjille (We will send a pull request to the repository admins)

#### *Jos et osaa käyttää komentoriviä sulavasti, [täältä löytyy tutoriaaleja GUI-työkalujen käyttöön.]( #tutorials-using-other-tools )*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Jos sinulla ei ole git asennettuna koneellesi, [asenna se](https://help.github.com/articles/set-up-git/).

## Haaroita (forkkaa) tämä arkisto

Haaroita tämä arkisto klikkaamalla projektisivun yläkulmassa näkyvää painiketta "Fork". Tämä luo kopion arkistosta omalle GitHub -tilillesi.

## Kloonaa (clone) arkisto

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Seuraavaksi kloonataan juuri haaroitettu arkisto koneellesi. Mene GitHub -käyttäjäsivullesi, avaa juuri haaroittamasi arkisto ja klikkaa "Code" -painiketta jonka jälkeen kopioi osoite painamalla "Copy to clipboard" -ikonia.

Avaa komentorivi ja syötä seuraava git-komento:

```
git clone "Juuri kopioimasi URL"
```

"Juuri kopioimasi URL"-tekstin sijasta (ilman lainausmerkkejä) liitä arkiston URL äskeisestä vaiheesta.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Esimerkiksi:

```
git clone https://github.com/KÄYTTÄJÄNIMI/first-contributions.git
```

Kirjoita GitHub-käyttäjänimesi *KÄYTTÄJÄNIMI* tekstin paikalle. Tämä komento kloonaa arkiston koneellesi.

## Luo haara

Mene arkistosi tiedostokansioon koneellasi (ellet jo ole siellä).

```
cd first-contributions
```

Seuraavaksi luo haara komennolla `git checkout`:

```
git checkout -b <haarasi-nimi>
```

Esimerkiksi:

```
git checkout -b add-matti-meikalainen
```

Haaran nimeen ei välttämättä tarvitse sisällyttää sanaa *add*, mutta tässä se käy järkeen sillä tämän branchin tarkoitus on lisätä nimesi listaan.

## Tee tarvittavat muutokset sekä sitoudu niihin

Seuraavaksi avaa `Contributors.md` tiedosto tekstieditorissa ja lisää nimesi tiedostoon. Älä lisää sitä tiedoston alkuun taikka loppuun vaan keskelle. Seuraaksi tallenna tiedosto.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Jos menet arkiston kansioon koneellasi ja syötät komennon `git status`, näet muutokset.

Lisää nuo muutokset branchiin `git add` komennolla:

```
git add Contributors.md
```

Seuraavaksi sitoudu muutoksiin (`git commit`) komennolla:

```
git commit -m "Add <sinun-nimesi> to Contributors list"
```

Korvaamalla *<sinun-nimesi>*` nimelläsi. Huomaa, että muutoksiin pitää aina laittaa jokin kommentti. Voit määrätä tekstin itse, mutta muista, että sen tulisi olla asiallinen ja heijastaa tekemiäsi muutoksia.

## Muutosten työntö GitHubiin

Työnnä (`git push`) muutoksesi arkistoon komennolla:

```
git push origin <haarasi-nimi>
```

Korvaamalla *<haarasi-nimi>* nimellä jonka annoit haarallesi aikaisemmin.

## Jätä muutoksesi arvosteltavaksi

Jos menet arkistoon GitHub:ssa, näet `Compare & pull request` painikkeen.  Paina kyseistä painiketta.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Seuraavaksi suorita vetopyyntö (pull request). Toisin sanoen, pyydät arkiston ylläpitäjiä vetämään koodisi mukaan arkistoon.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Seuraavaksi muutoksesi sulautetaan tämän projektin päähaaraan. Tulet saamaan ilmoituksen sähköpostiisi kun muutoksesi ovat sulautettu. Kun saat sähköpostin, olet tehnyt ensimmäisen osallistumisesi arkistoon! Onneksi olkoon.

## Mihin seuraavaksi?

Onneksi olkoon! Olet juuri suorittanut tavanomaisen *Fork -> Clone -> Edit -> Pull Request* -työnkulun, joka tulee usein vastaasi git-projekteissa!

Juhlista osallistumistasi; jaa se ystävillesi ja seuraajillesi menemällä [Web Appiin](https://roshanjossey.github.io/first-contributions/#social-share).

Voit liittyä Slack tiimiimme, jos sinulla on kysyttävää. [Liity Slack tiimiin](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Jos haluaisit osallistua muihin projekteihin, olemme koonneet listan yksinkertaisista asioista, joita voisit työstää. [Lista löytyy Web-Appistamme](https://roshanjossey.github.io/first-contributions/#project-list).

### [Lisämateriaaleja](../additional-material/git_workflow_scenarios/additional-material.md)

## Muiden työkalujen tutoriaaleja

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|<a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a>|
|---|---|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](sourcetree-macos-tutorial.md)|[IntelliJ IDEA](github-windows-intellij-tutorial.md)|
