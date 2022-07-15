[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-hfcq788y-QaXzXT5clBBWukXQyBhH4w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvi doprinos

Ovaj projekat ima za cilj da pojednostavi i vodi početnike do njihovog prvog doprinosa. Ako želite da napravite vaš prvi doprinos, pratite korake ispod.  

_Ako nijeste navikli da koristite komandnu liniju, [evo tutorijala koji koristi GUI alatke.](#Tutorijali-koji-koriste-druge-alatke)_

<img  align="right"  width="300"  src="https://firstcontributions.github.io/assets/Readme/fork.png"  alt="napravite kopiju repozitorijuma"  />

#### Ako nemate git na svojoj mašini, [instalirajte ga ovdje](https://help.github.com/articles/set-up-git/).

## Napravite kopiju repozitorijuma

Napravite kopiju _(fork)_ ovog repozitorijuma tako što ćete kliknuti na dugme **fork** na vrhu stranice.

Ovo će kreirati kopiju ovog repozitorijuma na vašem nalogu.

## Klonirajte repozitorijum

<img  align="right"  width="300"  src="assets/clone.png"  alt="Klonirajte repozitorijum"  />

Sada klonirajte repozitorijum na vašu mašinu. Idite na vaš GitHub profil, otvorite kopiju repozitorijuma, kliknite na dugme **code** i kliknite ikonicu *copy to clipboard*.
  
Otvorite terminal i unesite sledeću git komandu:

```
git clone "url koji ste upravo kopirali"
```

Umjesto "url koji ste upravo kopirali" (bez znaka navoda) unesite url repozitorijuma koji ste kopirali u prethodnom koraku.

<img  align="right"  width="300"  src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png"  alt="Kopirajte URL"  />

Na primjer:

```
git clone https://github.com/korisnicko-ime/first-contributions.git
```

Umjesto `korisnicko-ime` napišite korisničko ime za vaš GitHub nalog. Na ovaj način kopirate sadržaj repozitorijuma na vašu mašinu.

## Kreiranje grane _(branch)_

Prebacite se u radni direktorijum na vašem računaru (ukoliko već nijeste tu):  

```
cd first-contributions
```

Sada kreirajte granu koristeći komadu `git checkout`:

```
git checkout -b ime-vase-grane

```
 
Na primjer:
  
```
git checkout -b add-nikola-popovic
```

(Ime grane ne mora sadržati riječ _add_, ali je to preporučljivo jer je poenta ove grane da se doda vaše ime na listu kontributora.) 

## Napravite potrebne promjene i potvrdite ih
  
Sada otvorite fajl `Contributors.md` u tekst editoru i dodajte vaše ime. Nemojte dodati svoje ime na početku ili na kraju fajla. Stavite ga bilo gdje između. Sada, sačuvajte fajl.
  
<img  align="right"  width="450"  src="assets/git-status.png"  alt="git status"  />

Ako se vratite na radni direktorijum i izvršite komandu `git status`, vidjećete da su prisutne promjene.  

Dodajte te promjene u granu koju ste kreirali u prethodnim koracima koristeći komandu `git add`: 

```
git add Contributors.md
```

Sada potvrdite te izmjene koristeći komandu `git commit` :

```
git commit -m "Add <your-name> to Contributors list"
```

Umjesto `<your-name>` napišite vaše ime.

## Pošaljite izmjene u repozitorijum

Pošaljite izmjene koje ste napravili u repozitorijum na GitHub-u koristeći komandu `git push`:

```
git push origin <add-ime-vase-grane>
```
  
Umjesto `<add-ime-vase-grane>` napišite ime grane koju ste kreirali ranije.

## Pošaljite vaše izmjene na provjeru

Ako odete na repozitorijum na GitHub-u, vidjećete dugme **Compare / Pull Request**. Kliknite to dugme.

<img  style="float: right;"  src="assets/compare-and-pull.png"  alt="Kreirajte pull request"  />

Sada pošaljite vaš pull request.

<img  style="float: right;"  src="assets/submit-pull-request.png"  alt="Pošaljite pull request"  />

Uskoro, ja ću spojiti promjene koje ste napravili sa master granom repozitorijuma. Dobićete mejl potvrde kada se grane spoje.
  
## Šta dalje?
 
Čestitamo! Upravo ste izvršili standradni _fork -> clone -> edit -> pull request_ proces koji ćete često gledati dok doprinosite kodu. 
  
Proslavite vaš doprinos i podijelite ga sa prijateljima i pratiocima kroz [stranicu](https://firstcontributions.github.io/#social-share).

Ukoliko vam je potrebna pomoć ili imate neka pitanja, možete da se priključite našem [Slack timu](https://join.slack.com/t/firstcontributors/shared_invite/zt-hfcq788y-QaXzXT5clBBWukXQyBhH4w).

Sada možete početi da doprinosite i drugim projektima. Sastavili smo listu projekata sa jednostavim problemima na kojima možete početi da radite. Pogledajte [listu projekata na stranici](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](additional-material/git_workflow_scenarios/additional-material.md)

## Tutorijali koji koriste druge alatke

| <a  href="gui-tool-tutorials/github-desktop-tutorial.md"><img  alt="GitHub Desktop"  src="https://desktop.github.com/images/desktop-icon.svg"  width="100"></a> | <a  href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img  alt="Visual Studio 2017"  src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg"  width="100"></a> | <a  href="gui-tool-tutorials/gitkraken-tutorial.md"><img  alt="GitKraken"  src="./assets/gk-icon.png"  width="100"></a> | <a  href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img  alt="VS Code"  src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg"  width=100></a> | <a  href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img  alt="Sourcetree App"  src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg"  width=100></a> | <a  href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img  alt="IntelliJ IDEA"  src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg"  width=100></a> |

| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md) |
