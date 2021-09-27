[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Prvi doprinos

Teško je. Prvi pokušaji su uvjek teški. Ukoliko surađuješ sa drugima, još je lakše napraviti grešku kada je sustav kompleksniji. Cilj ovog projekta je da olakšamo proces kroz koji novo-pečeni programeri/developeri doprinose zajednici otvorenog koda (eng. open source), te kroz vrlo jednostavan primjer naučimo taj proces.

Blogovi i tutorijali mogu da pomoći, ali ništa nije bolje nego uzeti stvari u svoje ruke i zaista doprinjeti zajednici otvorenog koda. Ukoliko ste se prepoznali u tekstu iznad, pratite sljedeće korake.


#### *Ako vam je komandna linija (terminal) još uvijek stran pojam, [možete korititi github GUI alate.]( #tutorials-using-other-tools )*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Napravite fork repozitorijuma" />

Ukoliko nemate git instaliran na vašem uređaju, [instalirajte ga ovdje]( https://help.github.com/articles/set-up-git/).

## Terminologija git pojmova na hrvatskom je blago rečeno smjeh pa ih neću niti koristiti.
Više možete dobiti ovdje src= "https://github.com/tkrajina/uvod-u-git/blob/master/terminologija.tex"/>

## Napravite fork (kopiju ovog) repozitorija

Napravite (fork) tako što ćete kliknuti na dugme *fork* u gornjem desnom kutu. Ovime ste napravili i preuzeli kopiju ovog projekta na svoj github profil.

## Klonirajte repozitorij

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Sada ćemo klonirati taj repozitorij sa svog github profila u terminal ili programski editor kao što je VsCode na svom uređaju, ovaj korak će preuzeti cijeli projekt na vašem računalo.

Otvorite terminal i upišite sledeće git komande:

```
git clone "url you just copied"
```
Umjesto "url you just copied" (bez navodnika i razmaka) upišite ili samo ubacite link koji ste kopirali u prethodnom koraku.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Na primjer:
```
git clone https://github.com/this-is-you/first-contributions.git
```
Gde je umjesto `this-is-you` vaše korisničko ime.

## Grana *branch*

Prebacite se u radni direktorij na vašoj mašini:
```
cd first-contributions
```
napravite novo grananje *branch* koristeći `git checkout` comandu:
```
git checkout -b <ovdje stavite ime svoje grane/branch>
```

Na primer:
```
git checkout -b add-tomislav-tomislav
```
(Naziv grane ne mora da sadržavati *add* na početku, ali je prigodno uključiti ga jer je svrha ove grane da se doda vaše ime na listu.

## Napravite potrebne izmjene i potvrdite promjene

Otvorite `Contributors.md` dokument u tekst editoru i dodajte vaše ime. Nemojte dodavati svoje ime na sam početak ili kraj. Stavite ga negdje u sredinu. Nakon toga spremite promjene.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Vratite se u radni direktorij i izvršite komandu `git status`,vidjet ćete da postoje promjene.

Dodajte ove promjene u granu koju ste gore napravili koristeći `git add` komandu:

```
git add Contributors.md
```

Sada potvrdite ove promjene koristeći `git commit` komandu:
```
git commit -m "Add <your-name> to Contributors list"
```
Gde umesto `<your-name>` upišete svoje ime.

## Push changes to GitHub

Pošaljite the promjene na svoj vlastiti GitHub račun `git push`:
```
git push origin <add-your-branch-name>
```
gde umjesto `<add-your-branch-name>` stavljate ime vaše grane koju ste napravili u prethodnim koracima.

## Pošaljite izmjene na reviziju

Ukoliko odete na ovaj repozitorij na vašem GitHub računu primjetiti ćete `Compare & pull request`  Kliknite na to dugme.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

zatim pošaljite zahtjev klikom na dugme *submit*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Nakon toga, ukoliko nije bilo grešaka(sukoba s ostatkom koda u projektu) vaš code će biti dodan u projekt a vi ćete biti obavješteni putem email-a o toj promjeni.

## Šta dalje?

Čestitke!  Završili ste standardni _fork -> clone -> edit -> PR_ slijed koji će koristiti kroz vaš čitav programerski život!

Možete podeliti vaš doprinos sa prijateljima i pratiteljima otvaranjem [stranice](https://firstcontributions.github.io/#social-share).

Pridružite se i našem Slack timu u slučaju da vam je potrebna pomoć ili imate bilo kakvih pitanja. [Slack tim](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

A sada, možemo početi sa doprinositi drugim projektima. Napravili smo popis projekata sa jednostavnim problemima na kojima možete dati svoj doprinos. Posjetite stranicu sa [the list of projects](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](../additional-material/git_workflow_scenarios/additional-material.md)

## Uputstva za druge alate

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/assets/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)|[Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)|[GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)|[Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)|