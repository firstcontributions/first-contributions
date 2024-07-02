[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvi doprinosi

Cilj ovog projekta je da pruži jednostavne korake za početnike da naprave svoje prve doprinose. Ukoliko tražite da napravite prvi doprinos pratite sljedeće korake ispod.

#### _Ukoliko niste baš sigurni u vaš rad sa naredbnom linijom/terminalom, [ovdje možete pronaći tutorijale za GUI alate.](#Uputstva-za-druge-alate)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Napravite fork repozitorijuma" />

Ukoliko nemate git instaliran na vašom računalu, [instalirajte ga ovdje](https://help.github.com/articles/set-up-git/).

## Napravite fork repozitorija

Forkajte ovaj repozitorij tako da kliknete na dugme _fork_ na vrhu stranice. Ovako pravite kopiju repozitorija na vašoj github stranici.

## Klonirajte repozitorij

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Sada klonirajte repozitorij koji ste prethodno forkali. Posjetite svoj GitHub profil, otvorite repozitorij koji ste forkali, kliknite na _clone_ (kloniraj) dugme i kliknite na ikonicu _copy to clipboard_.

Otvorite terminal i upišite slijedeće git naredbe:

```
git clone "url koji ste sada kopirali"
```

gdje je "url koji ste sada kopirali" (bez navodnika) url na ovaj repozitorij (vaš fork ovog projekta). Pogledajte prethodne korake kako dohvatiti url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Na primjer:

```
git clone https://github.com/ovo-ste-vi/first-contributions.git
```

Gdje je umjesto `ovo-ste-vi` upisano vaše _github_ korisničko ime. Ovime kopirate sadržaj repozitorija _first-contributions_ na vaše računalo.

## Pravljenje grane _branch_

Prebacite se u radni direktorij na vašem računalu (ukoliko već niste tamo):

```
cd first-contributions
```

Pa zatim napravite novu granu _branch_ koristeći `git switch` comandu:

```
git switch -c add-svoje-ime
```

Na primjer:

```
git switch -c add-alonzo-church
```

## Napravite potrebne izmjene i potvrdite promjene

Otvorite `Contributors.md` datoteku u tekst editoru i dodajte vaše ime. Nemojte dodavati ime na sam početak ili kraj. Stavite ga negdje u sredinu. Potom sačuvajte datoteku.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ukoliko odete u radni direktorij i izvršite naredbu `git status`, primijetiti ćete da postoje promjene.

Dodajte ove promjene u granu koju ste gore napravili koristeći `git add` naredbu:

```
git add Contributors.md
```

Sada potvrdite ove promjene koristeći `git commit` naredbu:

```
git commit -m "Add tvoje-ime to Contributors list"
```

Gdje umjesto `tvoje-ime` upisujete svoje ime.

## Pushajte promjene na GitHub

Pošaljite promjene u repozitorij na GitHub-u koristeći naredbu `git push`:

```
git push origin -u ime-vaše-grane
```

gdje umjesto `ime-vaše-grane` stavljate ime vaše grane koje ste prethodno napravili.

## Pošaljite izmjene na pregled

Ukoliko odete na repozitorij na vašem GitHub profilu primijetit ćete `Compare & pull request` Dugme. Kliknite na njega.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

a zatim pošaljite zahtjev klikom na dugme _Create pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Nakon toga, vlasnik će spojiti promjene koje ste napravili sa master granom projekta. Dobit ćete mail potvrde kada se grane spoje.

## Što dalje?

Čestitamo! Završili ste standardni _fork -> clone -> edit -> PR_ tok koji će vas pratiti kroz vaš čitav programerski život!

Proslavite tako što ćete podjeliti vaš doprinos sa prijateljima i pratiocima otvaranjem [stranice](https://firstcontributions.github.io/#social-share).

Pridružite se i našem Slack timu u slučaju da vam je potrebna ikakva pomoć ili imate bilo kakvih pitanja. [Slack tim](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

A sada, možemo početi sa doprinosima drugim projektima. Napravili smo popis projekata sa jednostavnim problemima na kojima možete početi raditi. Posjetite [listu projekata na naštoj stranici](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](../additional-material/git_workflow_scenarios/additional-material.md)

## Uputstva za druge alate

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
