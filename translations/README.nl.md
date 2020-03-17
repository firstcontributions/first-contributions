[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Eerste bijdragen

De eerste keer dat je iets nieuws probeert is altijd lastig, helemaal wanneer je samen werkt - kan het maken van fouten erg vervelend zijn. Maar in open-source ontkom je niet aan samenwerken. We willen het graag makkelijker maken om te leren en bij te dragen voor de eerste keer aan een open-source project.

Het kan helpen om de artikelen te lezen en de video's te bekijken, maar niets is beter dan het gelijk te doen terwijl je leert en je niet de kans hebt om een fout te maken. Dit project richt zich op het begeleiden en het makkelijker maken voor beginners om hun eerste bijdrage te leveren aan een project. Onthoud: Hoe meer ontspannen je bent hoe beter je leert. Indien je op zoek bent om je eerste bijdrage te leveren aan open-source volg dan de onderstaande stappen. Wij beloven dat je het leuk zal vinden xxxx. 

<img align="right" width="300" src="../assets/fork.png" alt="fork deze repository" />

#### *Lees dit in [andere talen](../Translations.md)*

Indien je git nog niet hebt op je systeem, [ installeer het dan eerst ]( https://help.github.com/articles/set-up-git/ )

## Deze repository forken

Fork deze repository door op de fork knop te klikken. Dit creëert een kopie van deze repository in jouw account.

## De repository clonen

<img align="right" width="300" src="../assets/clone.png" alt="kloon deze repository" />

Kloon nu deze repository naar je systeem. Klik op de kloon knop en dan het kopiëren naar klembord icoon.

Open een terminal en voer volgend git commando uit:

```
git clone "url die je net kopieerde"
```
Waar "url die je net kopieerde" (zonder aanhalingstekens) de url naar (jouw fork van) deze repository is. Zie de vorige stappen om de url te vinden.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="kopieer URL naar het klembord" />

Bijvoorbeeld:
```
git clone https://github.com/this-is-you/first-contributions.git
```
Waar 'this-is-you' je GitHub gebruikersnaam is. Hiermee kopieer je inhoud van de first-contributions repo op GitHub naar je systeem.

## Een branch aanmaken

Navigeer naar de map van de repository op je systeem (mocht je daar niet al zijn).

```
cd first-contributions
```
Maak nu een branch aan door middel van het `git checkout command`
```
git checkout -b <je-nieuwe-branch-naam>
```

Bijvoorbeeld:
```
git checkout -b add-thibmaek
```
(De naam van de branch hoeft niet het woord *add* te bevatten. In dit voorbeeld is het wel te adviseren aangezien het doel van deze branch hiermee duidelijk wordt gemaakt.)

## Maak de benodigde wijzigingen en commit deze

Open nu het `Contributors.md` bestand in een teksteditor en voeg je naam toe. Doe dit niet aan het begin of eind, maar ergens in het midden. Sla vervolgens het bestand op.

Als je naar de projectmap gaat en `git status` doet, zul je zien dat er wijzigingen zijn. Voeg deze toe aan je branch met behulp van onderstaand `git add` commando.
```
git add Contributors.md
```

Commit nu deze wijzigingen door onderstaand `git commit` commando te gebruiken.
```
git commit -m "Add <jouw-naam> to Contributors list"
```
vervang `<jouw-naam>` met jouw naam

## Push de wijzigingen naar GitHub

Push je wijzigingen met `git push`
```
git push origin <je-nieuwe-branch-naam>
```
Vervang `<je-nieuwe-branch-naam>` met de naam van de branch die je eerder aanmaakte.

## Verstuur je wijzigingen voor review

Als je naar je repository gaat op GitHub, zal je zien dat er een `Compare & pull request` knop staat. Klik hierop.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="creëer een pull request" />

Verstuur nu je pull request.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="verstuur je pull request" />

Nu ga ik (de beheerder) al je wijzigingen mergen in de master branch van dit project. Als de veranderingen gemerged zijn, zul je hier een e-mailnotificatie over ontvangen.

## Je fork in sync houden met de hoofd-repository

Wanneer de pull request wordt geaccepteerd en gemerged, zal jouw fork de wijzigingen nog niet bevatten - hiervoor moet je nog een aantal extra stappen ondernemen.

Om beide repo's met elkaar in sync te houden voeg je de hoofd repo (mijne) url in als `upstream remote url`.
```
git remote add upstream https://github.com/firstcontributions/first-contributions
```
Hiermee vertel je git dat er nog een andere versie van dit project bestaat op dit specifieke url punt en dat we het upstream zullen noemen. Wanneer de wijzigingen gemerged zijn, kun je de nieuwe versie ophalen (fetchen) van mijn repo.
```
git fetch upstream
```

Hiermee fetchen we alle wijzigingen in mijn fork (upstream remote). Nu zal je de nieuwe revisie/versie van mijn repo moeten mergen in jouw master branch.
```
git rebase upstream/master
```
Dit voegt alle wijzigingen toe die je net fetchte van de master branch. Als je nu probeert je master branch te pushen, zal je fork al deze wijzigingen ook bevatten.
```
git push origin master
```
Merk op dat je in dit geval pusht naar de remote met de naam origin.

## Tutorials gebruiken Andere hulpmiddelen

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Hoe nu verder?

Gefeliciteerd! Je hebt zojuist de standaard _fork -> clone -> edit -> PR_ workflow doorlopen die je vaak zult tegenkomen als bijdrager!

Vier je bijdrage en deel het met je vrienden en volgers via de [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Mocht je nog vragen of hulp nodig hebben dan kun je je aanmelden voor ons [Slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Laten we je nu op weg helpen met het bijdragen aan andere projecten. We hebben een lijst samengesteld met projecten die makkelijke issues bevatten waar je aan kunt werken. Bekijk [de lijst op de web app](https://roshanjossey.github.io/first-contributions/#project-list)

Hier zijn enkele beginner-level issues in populaire repos die je kan proberen oplossen. Ga verder naar deze repos om meer te lezen.

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
