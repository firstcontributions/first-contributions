[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Første bidrag

Det er vanskelig. Det er alltid vanskelig å gjøre noe for første gang. Spesielt når man samarbeider er det ikke kjekt å gjøre tabber. Vi har lyst til å gjøre det enklere for nye bidragsytere for åpen kildekode å lære og bidra for første gang.

Å lese artikler eller se på opplæringsvideoer kan hjelpe, men hva er vel bedre enn å faktisk gjøre det i et praktisk miljø? Dette prosjektet ønsker å veilede og forenkle måten nybegynnere lager sitt første bidrag. Hvis du er interessert i å lage ditt første bidrag, følg stegene nedenfor.

#### *Hvis du er unkomfortabel med kommandolinjen, [her er noen guider av verktøy som bruker grafisk brukergrensesitt]( #tutorials-using-other-tools )


#### *Les dette i [andre språk](translations/Translations.md).*
[:bangladesh:](translations/README.bn.md)
[🇧🇬](translations/README.bg.md)
[🇧🇷](translations/README.pt_br.md)
[<img src="assets/catalan1.png" width="22">](translations/README.ca.md)
[🇨🇳](translations/README.chs.md)
[🇨🇿](translations/README.cs.md)
[🇩🇪](translations/README.de.md)
[🇩🇰](translations/README.da.md)
[🇪🇬](translations/README.eg.md)
[🇪🇸](translations/README.es.md)
[🇫🇷](translations/README.fr.md)
[🏴](translations/README.gl.md)
[🇬🇷](translations/README.gr.md)
[🇮🇩](translations/README.id.md)
[🇮🇱](translations/README.hb.md) 
[🇮🇳](translations/Translations.md)
[🇮🇷](translations/README.fa.md)
[🇮🇷](translations/README.fa.en.md)
[🇮🇹](translations/README.it.md)
[🇯🇵](translations/README.ja.md)
[🇰🇪](translations/README.kws.md)
[🇰🇷 🇰🇵](translations/README.ko.md)
[🇱🇹](translations/README.lt.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇲🇲](translations/README.mm_unicode.md)
[🇲🇽](translations/README.mx.md)
[🇲🇾](translations/README.my.md)
[🇳🇱](translations/README.nl.md)
[🇳🇬](translations/README.igb.md)
[🇳🇵](translations/README.np.md)
[🇵🇭](translations/README.tl.md)
[<img src="assets/pirate.png" width="22">](translations/README.en-pirate.md)
[🇵🇰](translations/README.ur.md)
[🇵🇱](translations/README.pl.md)
[🇵🇹](translations/README.pt-pt.md)
[🇷🇺](translations/README.ru.md)
[🇸🇦](translations/README.ar.md)
[🇸🇪](translations/README.se.md)
[:slovakia:](translations/README.slk.md)
[:slovenia:](translations/README.sl.md)
[🇹🇭](translations/README.th.md)
[🇹🇷](translations/README.tr.md)
[🇹🇼](translations/README.cht.md)
[🇺🇦](translations/README.ua.md)
[🇻🇳](translations/README.vn.md)
[🇿🇦](translations/README.zul.md)
[🇿🇦](translations/README.afk.md)
[🇰🇪](translations/README.kws.md)
[🇳🇬](translations/README.igb.md)
[🇱🇻](translations/README.lv.md)



<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />

Hvis du ikke har git på datamaskinen din, [installér det]( https://help.github.com/articles/set-up-git/).

(Norske oversettelser av git-begreper er hentet [herfra](https://github.com/Potrik98/git-pa-norsk).)

## Splitt denne kolleksjonen

Splitt denne kolleksjonen ved å trykke på "fork"-knappen på toppen av denne siden.
Da lages det en kopi av denne kolleksjonen på din bruker.

## Klon kolleksjonen

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

Klon sidespor kolleksjonen til din lokale datamaskin. Gå til GitHub-brukeren din, åpne kolleksjonen din, trykk på "clone"-knappen og deretter trykk på *kopier til utklippstavle*-ikonet.

Åpne en terminal og kjør følgende git kommando:

```
git clone "url du kopierte"
```
hvor "url du kopierte" (uten anførselstegn) er url-en til denne kolleksjonen(ditt sidespor av prosjektet).
Se forrige steg på hvordan man får tak i url-en.


<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

For eksempel:
```
git clone https://github.com/this-is-you/first-contributions.git
```
hvor `this-is-you` er ditt GitHub-brukernavn. Her kopierer du innholdet av kolleksjonen din fra kontoen din på GitHub til datamaskinen din.

## Lag en gren

Naviger til mappen hvor kolleksjonen ligger ved å kjøre denne kommandoen i ledetekst vinduet(hvis du ikke allerede er der):

```
cd first-contributions
```

Lag en gren ved hjelp av `git checkout` kommandoen:
```
git checkout -b <add-ditt-navn>
```

For eksempel:
```
git checkout -b add-alonzo-church
```
(Navnet på grenen trenger ikke å hete akkurat det, men det er fornuftig med tanke på at formålet med denne grenen er å legge til navnet ditt i en liste.)branch is to add your name to a list.)

## Lag de nødvendige endringene og bunt sammen de endringene

Åpne `Contributors.md` filen i et tekstredigeringsverktøy og legg til navnet ditt. Ikke legg det til i begynnelsen eller slutten, men et sted innimellom. Deretter lagre filen.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />

Hvis du går til kolleksjonsmappen og kjører kommandoen `git status`, vil du se at det har skjedd noen endringer.

Legg til disse endringene til grenen du lagde ved å kjøre kommandoen `git add`:

```
git add Contributors.md
```
Nå kan du bunte endringene sammen ved å kjøre `git commit`:
```
git commit -m "Add <your-name> to Contributors list"
```
ersatt `<your-name>` med ditt navn.

## Dytt endringene tilGitHub

Dytt endringene dine med  `git push`:
```
git push origin <add-ditt-grennavn>
```
erstatt `<add-ditt-grennavn>` med navnet på grenen du lagde tidligere.

## Send inn endringene dine til inspeksjon

Hvis du går til kolleksjonen din på GitHub, så vil du se en `Compare & pull request`-knapp. Trykk på den.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Send inn din fletteforespørsel.

<img style="float: right;" src="assets/submit-pull-request.png" alt="submit pull request" />

Snart kommer jeg til å flette inn endringene dine til dette prosjektets master-gren. Du kommer til å få et varsel på e-post når endringene har blitt sammenflettet.


## Hva nå?

Gratulerer! Du har nå gjennomført den utbredte _fork -> clone -> edit -> PR_ som du kommer til å støtte på ofte som en bidragsyter.

Feire bidraget ditt ved å dele det med venner og følgere ved å gå til [web app](https://firstcontributions.github.io/#social-share).

Du kan også bli med i vår Slack hvis du trenger hjelp eller har noen spørsmål. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

Nå la oss hjelpe deg i gang med dine neste bidrag. Vi har satt sammen en liste med prosjekter som har enkle problemer du kan bryne deg på. Sjekk ut [listen med prosjekter i web appen](https://firstcontributions.github.io/#project-list).


### [Ekstra materialer](additional-material/git_workflow_scenarios/additional-material.md)


## Guider med andre verktøy.

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](sourcetree-macos-tutorial.md)|
