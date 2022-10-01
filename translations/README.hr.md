[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvi doprinosi

Cilj ovog projekta je pojednostaviti i voditi početnike putem njihovog prvog doprinosa. Ako želite napraviti prvi doprinost, sljedite korake ispod ovog teksta.

#### _Ako niste na ti sa komandnom linoj (Command Prompt/Powershell/Git Bash na Windorsima odnosno terminal na MacOS) [mozete koristit ovaj link kroz GUI (Graphichal User Interface) alate.](#Uputstva-za-druge-alate)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Ukoliko nemate git instaliran na vašem računalu/laptopu, [instalirajte ga ovdje](https://help.github.com/articles/set-up-git/).

## Prikačite (Fork) repozitorij

Prikačite (fork) tako da kliknete na tipku _fork_ na vrhu stranice. Ovako ćete napraviti kopiju repozitorija na vašem Github profilu.

## Klonirajte repozitorijum

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Slijedeće, klonirajte repozitorij koji ste prethodno prikačili (fork). Posjetite svoj GitHub profil, otvorite repozitorij koji ste prikvačili, kliknite na _clone_ (kloniraj/kopiraj) tipku i kliknite na ikonu _copy to clipboard_.

Otvorite terminal (Command Prompt, Git Bash, Powershell...) i upišite sljedeće git komande:

```
git clone "url koji ste prethodno kopirali sa vašeg github profila" (bez navodnika i razmaka)
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Na primjer:

```
git clone https://github.com/vaš-profil/first-contributions.git
```

Gdje je umjesto `vaš-profil` upisano vaše _github_ korisničko ime. Ovim kopirate sadržaj repozitorija _first-contributions_ na vaše računalo/laptop.

## Stvori granu _branch_

Prebacite se u radnu mapu na vašem računualu/laptopu:

```
cd first-contributions (odnosno pratite mjesto gdje ste napravili radnu mapu ovog repozitorija)
```

Nakon toga zatim stvorite novu granu _branch_ koristeći `git checkout` naredbu:

```
git checkout -b <ime-vaše-nove-grane>
```

Na prijmer:

```
git checkout -b add-alonzo-church
```


## Napravite potrebne izmjene i potvrdite promjene

Otvorite `Contributors.md` datoteku u programu za uređivanje teskta i dodajte vaše ime. Nemojte dodavati ime na početku ili na kraju već ga stavite negdje u sredinu. Nakon toga spremite datoteku.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ukoliko odete u radnu mapu i izvršite naredbu `git status`, primjetiti će te da postoje promjene.

Dodajte ove promjene u granu koju ste prije napravili koristeći `git add` naredbe:

```
git add Contributors.md
```

Sada potvrdite ove promjene koristeći `git commit` narebu, tekst u "" iza -m je poruka kojom potvrđujete promjene:

```
git commit -m "Add <vaše-ime> to Contributors list"
```

Gdje umjesto `<vaše-ime>` upisujete svoje ime.

## Push changes to GitHub

Pošaljite izmjene na svojoj grani naredbom `git push`:

```
git push origin <ime-vaše-grane>
```

gdje umjesto `<ime-vaše-grane>` stavljate ime vaše grane koje ste prethodno izradili.

## Pošaljite izmjene na reviziju

Ukoliko odete na repozitorij GitHub profilu primjetiti će te `Compare & pull request` tipku. Kliknite tu tipku.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

a potom pošaljite zahtjev klikom na tipku _Create pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Nakon toga, administrator će spojiti promjene koje ste napravili na vašoj grani sa master granom projekta. Dobiti će te e-poruku potvrde kada se vaša grana spoji sa master(main) granom.

## Šta dalje?

Čestitamo! Završili ste standardni _fork -> clone -> edit -> PR_ tijek rada koji će vas pratiti kroz vaš čitav programerski život!

Proslavite tako što ćete podjeliti vaš doprinos sa prijateljima i sljedbenicima otvaranjem [stranice](https://firstcontributions.github.io/#social-share).

Pridružite se i našem Slack timu u slučaju da vam je potrebna ikakva pomoć, imate bilo kakva pitanja ili jednostavno želite biti dio zajednice developera. [Slack tim](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

A sada, možete početi sa doprinosima na drugim projektima. Napravili smo spisak projekata sa jednostavnim problemima na kojima možete početi raditi. Slijedite link na stranicu [the list of projects na našem sajtu](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](../additional-material/git_workflow_scenarios/additional-material.md)

## Uputstva za druge alate

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
