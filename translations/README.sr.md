[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Prvi prilog

Teško je. Prvi pokušaj je uvek težak. Kada sarađuješ sa drugima, napraviti greške je utoliko strašnije. Želeli bismo da olakšamo proces kroz koji novi programeri koji doprinose otvorenom softveru (eng. open source) uče i doprinose po prvi put.

Iako blogovi i tutorijali mogu da pomognu, ništa nije bolje nego uzeti stvari u svoje ruke i zaista doprinositi u trening-sredini. Ovaj projekat ima za cilj da pruži konkretne korake i olakša način na koji početnici prilažu svoje prve doprinose (eng. contributions). Ukoliko ste se prepoznali u tekstu iznad, pratite sledeće korake.


#### *Ako vam je nezgodno da čitate tekst u komandnoj liniji, [evo linka kroz GUI alate.](#Uputstva-za-druge-alate)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Napravite fork repozitorijuma" />

Ukoliko nemate git instaliran na vašoj mašini, [instalirajte ga ovde]( https://help.github.com/articles/set-up-git/).

## Napravite fork repozitorijuma

Napravite račvanje (fork) tako što ćete kliknuti na dugme *fork* na vrhu stranice. Ovako pravite kopiju repozitorijuma na vašoj strani.

## Klonirajte repozitorijum

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Sledeće, klonirajte repozitorijum koji ste prethodno račvali. Posetite svoj GitHub profil, otvorite repozitorijum koji ste račvali, kliknite na *clone* dugme i kliknite na ikonicu *copy to clipboard*.

Otvorite terminal i upišite sledeće git komande:

```
git clone "url you just copied"
```
Umesto "url you just copied" (bez navodnika i razmaka) upišite url repozitorijuma koji ste kopirali u prethodnom koraku.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Na primer:
```
git clone https://github.com/this-is-you/first-contributions.git
```
Gde je umesto `this-is-you` upisano vaše korisničko ime. Ovim kopirate sadržaj repozitorijuma *first-contributions* na vašu mašinu.

## Pravljenje grane *branch*

Prebacite se u radni direktorijum na vašoj mašini:
```
cd first-contributions
```
Pa zatim napravite novo grananje *branch* koristeći `git checkout` comandu:
```
git checkout -b <add-your-new-branch-name>
```

Na primer:
```
git checkout -b add-alonzo-church
```
(Naziv grane ne mora da sadrži *add* na početku, ali je zgodno uključiti ga jer je svrha ove grane da doda vaše ime na listu.)

## Napravite potrebne izmene i potvrdite promene

Otvorite `Contributors.md` fajl u tekst editoru i dodajte vaše ime. Nemojte dodavati ime na sam početak ili kraj. Stavite ga negde u sredinu. Potom sačuvajte fajl.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ukoliko odete u radni direktorijum i izvršite komandu `git status`,primetićete da postoje promene.

Dodajte ove promene u granu koju ste gore napravili koristeći `git add` komandu:

```
git add Contributors.md
```

Sada potvrdite ove promene koristeći `git commit` komandu:
```
git commit -m "Add <your-name> to Contributors list"
```
Gde umesto `<your-name>` upisujete svoje ime.

## Push changes to GitHub

Pošaljite izmene u repozitorijum na GitHub nalogu `git push`:
```
git push origin <add-your-branch-name>
```
gde umesto `<add-your-branch-name>` stavljate ime vašeg grananja.

## Pošaljite izmene na reviziju

Ukoliko odete na repozitorijum na vašem GitHub nalogu primetićete `Compare & pull request` Dugme. Kliknite na njega.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

a potom pošaljite zahtev klikom na dugme *submit*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Nakon toga, ja ću spojiti promene koje ste napravili sa master granom projekta. Dobićete mejl potvrde kada se grane spoje.

## Šta dalje?

Čestitamo!  Završili ste standardni _fork -> clone -> edit -> PR_ tok koji će vas pratiti kroz vaš čitav programerski život!

Proslavite tako što ćete podeliti vaš doprinos sa prijateljima i pratiocima otvaranjem [stranice](https://firstcontributions.github.io/#social-share).

Pridružite se i našem Slack timu u slučaju da vam je potrebna ikakva pomoć ili imate bilo kakvih pitanja. [Slack tim](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

A sada, možemo početi sa doprinosima drugim projektima. Napravili smo spisak projekata sa jednostavnim problemima na kojima možete početi da radite. Posetite stranicu sa [the list of projects na našem sajtu](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](../additional-material/git_workflow_scenarios/additional-material.md)

## Uputstva za druge alate

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)|[Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)|[GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)|[Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)|
