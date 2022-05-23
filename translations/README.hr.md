[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvi doprinosi

Ovaj projekt ima za cilj usmjeriti početnike pri davanju svog prvog doprinosa. Ako želite dati svoj prvi doprinos, slijedite navedene korake.

#### _Ukoliko niste sigurni u svoj rad sa naredbenim retkom/terminalom, [možete koristiti ovaj vodič koji koristi GUI alate.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Napravite fork repozitorijuma" />

Ukoliko nemate git instaliran na vašem računalu, [instalirajte ga ovdije](https://help.github.com/articles/set-up-git/).

## Račvarite (fork) spremište (respository)

Račvarite spremište tako da kliknete na gumb _fork_ na vrhu ove stranice. Time ćete kopirati spremište na vašoj github stranici.

## Klonirajte (clone) spremište

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Nakon toga, klonirajte spremište koji ste prethodno račvarili. Posjetite svoj GitHub profil, otvorite spremište koje ste račvalili, kliknite na _clone_ (kloniraj/kopiraj) dugme i kliknite na ikonu _copy to clipboard_.

Otvorite naredbeni redak i unesite slijedeće git komande:

```
git clone "url koji ste prethodno kopirali sa vašeg github profila" (bez navodnika i razmaka)
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Na primjer:

```
git clone https://github.com/ovo-ste-vi/first-contributions.git
```

Umjesto `ovo-ste-vi` trebalo bi pisati vaše _github_ korisničko ime. Ovim kopirate sadržaj spremišta _first-contributions_ na vaše računalo.

## Kreiranje grane (branch)

Promjenite vašu radnu mapu (ako već niste):

```
cd first-contributions
```
Zatim napravite novu grananu koristeći `git checkout` komandu:

```
git checkout -b <add-svoje-ime>
```

Na primer:

```
git checkout -b add-zoran-milanovic
```

(Naziv grane ne mora sadržavati _add_ na početku niti _vaše ime_, ali bi bilo razumno pošto je svrha ove grane da doda vaše ime na listu.

## Napravite potrebne izmjene i potvrdite promjene

Otvorite `Contributors.md` datoteku u uređivaču teksta i dodajte vaše ime. Nemojte dodavati ime na sam početak ili kraj. Stavite ga negdje u sredinu. Potom spremite datoteku.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ukoliko odete u radnu mapu i pokrenete komandu `git status`, primjetiti ćete da postoji promjena.

Dodajte te promjene u granu koju ste prije napravili koristeći `git add` komandu:

```
git add Contributors.md
```

Onda potvrdite te promjene koristeći `git commit` komandu:

```
git commit -m "Add <vaše-ime> to Contributors list"
```

Umjesto `<vaše-ime>` upišite svoje ime.

## Pošaljite (push) izmjene na GitHub

Pošaljite izmjene na GitHub komandom `git push`:

```
git push origin <dodaj-ime-svoje-grane>
```

Umjesto `<dodaj-ime-svoje-grane>` upišite ime vaše grane koju ste prethodno napravili.

## Pošaljite izmjene na pregled

Ukoliko odete na spremište na vašem GitHub profilu primetiti ćete `Compare & pull request` dugme. Kliknite na njega.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Potom pošaljite zahtjev klikom na dugme _Create pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Nakon toga, admin će spojiti promjene koje ste napravili sa master granom projekta. Dobiti ćete mail potvrde kada se grane spoje.

## Što dalje?

Čestitamo! Odradili ste standardni _fork -> clone -> edit -> pull_ tok na koji ćete često naići prilikom davanja doprinosa!

Proslavite dijeljenjem vašeg doprinosa sa prijateljima i pratiteljima na ovoj [web stranici](https://firstcontributions.github.io/#social-share).

Pridružite se i našem Slack timu u slučaju da vam je potrebna bilo kakva pomoć ili ukoliko imate bilo kakvih pitanja. [Slack tim](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

A sada, možete početi sa doprinosima na drugim projektima. Napravili smo spisak projekata sa jednostavnim problemima na kojima možete početi. Posijetite stranicu sa [listom projekta](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](../additional-material/git_workflow_scenarios/additional-material.md)

## Uputstva za druge alate

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
