[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvi doprinosi

Ovaj projekt ima za cilj pojednostaviti i usmjeriti početnike daju svoj prvi doprinos (eng. _contribution_). Ako želite dati svoj prvi doprinos, slijedite ispod navedene korake.

#### _Ukoliko niste bas sigurni u vas rad sa komandnom linijom/terminalom (terminal -> za macOs), [mozete koristit ovaj link kroz GUI alate.](#tutorials-using-other-tools)_

_Ako niste upoznati s komandnom linijom, [evo tutorijala za GUI alate.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Napravite fork repozitorija" />

#### Ako nemate git instaliran na vašem računalu, [instalirajte ga ovdje](https://help.github.com/articles/set-up-git/).

## Forkajte ovaj repozitorij

Forkajte ovaj repozitorij klikom na dugme _fork_ na vrhu stranice. Ovim potezom napravit ćete kopiju repozitorija na vašem računu.

## Klonirajte repozitorij

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Nadalje, klonirajte repozitorij koji ste prethodno forkali. Posjetite svoj GitHub profil, otvorite repozitorij koji ste forkali, kliknite na _code_ dugme, a zatim na ikonicu _copy to clipboard_.

Otvorite terminal i upišite sljedeće git naredbe:

```
git clone "url koji ste upravo kopirali"
```

gdje je "url koji ste upravo kopirali" (bez navodnika) poveznica na ovaj repozitorij (Vaš fork ovog projekta). Pogledajte prethodne korake za dohvaćanje url-a.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Na primjer:

```
git clone https://github.com/ovo-ste-vi/first-contributions.git
```

gdje je `ovo-ste-vi` Vaše GitHub korisničko ime. Ovim kopirate sadržaj repozitorija first-contributions na Vaše računalo.

## Izrada grane

Prebacite se u radni direktorij na Vašem računalu (ako već niste tu):

```
cd first-contributions
```

Pa zatim napravite novu granu koristeći `git checkout` naredbu:

```
git checkout -b <ime-nove-grane>
```

Na primjer:

```
git checkout -b add-zoran-milanovic
```

(Naziv grane ne mora sadržavati riječ _add_ u sebi, ali je zgodno uključiti ga jer je svrha ove grane dodavanje Vašeg imena na listu.)

## Napravite potrebne izmjene i potvrdite promjene

Otvorite `Contributors.md` datoteku u uređivaču teksta i dodajte Vaše ime. Nemojte dodavati ime na sam početak ili kraj. Stavite ga negdje u sredinu. Zatim spremite datoteku.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ako odete u radni direktorij i izvršite naredbu `git status`, primijetit ćete da postoje promjene.

Dodajte ove promjene u granu koju ste gore napravili koristeći `git add` naredbu:

```
git add Contributors.md
```

Sad potvrdite ove promjene koristeći `git commit` naredbu:

```
git commit -m "Add <tvoje-ime> to Contributors list"
```

gdje umjesto `<tvoje-ime>` upisujete svoje ime.

## Priložite promjene na GitHub

Priložite izmjene u repozitoriju na GitHub koristeći `git push`:

```
git push origin <dodaj-ime-svoje-grane>
```

gdje umjesto `<dodaj-ime-svoje-grane>` stavljate ime Vaše grane koje ste prethodno napravili.

## Pošaljite izmjene na pregled

Ako odete na repozitorij na Vašem GitHub profilu primijetit ćete `Compare & pull request` dugme. Kliknite na njega.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

a potom pošaljite zahtjev klikom na dugme _Create pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Nakon toga, admin će spojiti promjene koje ste napravili s master granom projekta. Dobit ćete mail potvrde kada se grane spoje.

## Što dalje?

Čestitamo! Završili ste standardni _fork -> clone -> edit -> PR_ tijek koji će Vas pratiti kroz Vaš čitav programerski život!

Proslavite tako što ćete podjeliti Vaš doprinos s prijateljima i pratiteljima otvaranjem [stranice](https://firstcontributions.github.io/#social-share).

Pridružite se i našem Slack timu u slučaju da Vam je potrebna ikakva pomoć ili imate bilo kakvih pitanja. [Slack tim](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

A sada, možemo početi s doprinosima drugim projektima. Napravili smo popis projekata s jednostavnim problemima na kojima možete početi s radom. Posjetite stranicu s [the list of projects na našoj stranici](https://firstcontributions.github.io/#project-list).

### [Dodatni materijali](../additional-material/git_workflow_scenarios/additional-material.md)

## Upute za druge alate

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
