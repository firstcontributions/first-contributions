[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvi doprinosi

Ovaj projekat ima za cilj da pruži konkretne korake i olakša način na koji početnici prilažu svoje prve doprinose (eng. contributions). Ukoliko ste se prepoznali u tekstu iznad i zelite da probate i doprinesete ovome ili nekom drugom projektu, pratite slijedece korake.

#### _Ukoliko niste bas sigurni u vas rad sa komandnom linijom/terminalom (terminal -> za macOs), [mozete koristit ovaj link kroz GUI alate.](#Uputstva-za-druge-alate)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Napravite fork repozitorijuma" />

Ukoliko nemate git instaliran na vašoj mašini, [instalirajte ga ovde](https://help.github.com/articles/set-up-git/).

## Uradite fork repozitorijuma

Uradite račvanje (fork) tako što ćete kliknuti na dugme _fork_ na vrhu stranice. Ovako pravite kopiju repozitorijuma na vašoj github stranici.

## Klonirajte repozitorijum

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Slijedeće, klonirajte repozitorijum koji ste prethodno račvali (fork). Posjetite svoj GitHub profil, otvorite repozitorijum koji ste račvali, kliknite na _clone_ (kloniraj/kopiraj) dugme i kliknite na ikonicu _copy to clipboard_.

Otvorite terminal i upišite slijedece git komande:

```
git clone "url koji ste prethodno kopirali sa vaseg github profila" (bez navodnika i razmaka)
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Na primjer:

```
git clone https://github.com/ovo-ste-vi/first-contributions.git
```

Gdje je umjesto `ovo-ste-vi` upisano vaše _github_ korisničko ime. Ovim kopirate sadržaj repozitorijuma _first-contributions_ na vašu mašinu.

## Pravljenje grane _branch_

Prebacite se u radni direktorij na vašoj mašini:

```
cd first-contributions (ili pratite gdje se tacno nalazi na vasoj masini)
```

Pa zatim napravite novo grananje _branch_ koristeći `git checkout` comandu:

```
git checkout -b <add-svoje-ime>
```

Na primer:

```
git checkout -b add-alonzo-church
```

(Naziv grane ne mora da sadrži _add_ na početku ili vase _ime_, ali je zgodno uključiti ga jer je svrha ove grane da doda vaše ime na listu.

## Napravite potrebne izmjene i potvrdite promjene

Otvorite `Contributors.md` fajl u tekst editoru i dodajte vaše ime. Nemojte dodavati ime na sam početak ili kraj. Stavite ga negdje u sredinu. Potom sačuvajte fajl.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ukoliko odete u radni direktorijum i izvršite komandu `git status`, primjetit ce te da postoje promjene.

Dodajte ove promjene u granu koju ste gore napravili koristeći `git add` komandu:

```
git add Contributors.md
```

Sada potvrdite ove promjene koristeći `git commit` komandu:

```
git commit -m "Add <tvoje-ime> to Contributors list"
```

Gdje umjesto `<tvoje-ime>` upisujete svoje ime.

## Push changes to GitHub

Pošaljite izmjene u repozitorijum na GitHub nalogu `git push`:

```
git push origin <dodaj-ime-svoje-grane>
```

gdje umjesto `<dodaj-ime-svoje-grane>` stavljate ime vašeg grananja koje ste prethodno napravili.

## Pošaljite izmjene na reviziju

Ukoliko odete na repozitorijum na vašem GitHub profilu primetićete `Compare & pull request` Dugme. Kliknite na njega.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

a potom pošaljite zahtjev klikom na dugme _Create pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Nakon toga, admin će spojiti promjene koje ste napravili sa master granom projekta. Dobićete mejl potvrde kada se grane spoje.

## Šta dalje?

Čestitamo! Završili ste standardni _fork -> clone -> edit -> PR_ tok koji će vas pratiti kroz vaš čitav programerski život!

Proslavite tako što ćete podjeliti vaš doprinos sa prijateljima i pratiocima otvaranjem [stranice](https://firstcontributions.github.io/#social-share).

Pridružite se i našem Slack timu u slučaju da vam je potrebna ikakva pomoć ili imate bilo kakvih pitanja. [Slack tim](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

A sada, možemo početi sa doprinosima drugim projektima. Napravili smo spisak projekata sa jednostavnim problemima na kojima možete početi da radite. Posetite stranicu sa [the list of projects na našem sajtu](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](../additional-material/git_workflow_scenarios/additional-material.md)

## Uputstva za druge alate

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
