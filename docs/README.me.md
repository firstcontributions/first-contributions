[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Prvi doprinosi (First Contributions)

Teško je. Uvijek je teško kada nešto radite prvi put. Posebno kada sarađujete sa drugima, pravljenje grešaka nije prijatan osjećaj. Željeli smo da pojednostavimo način na koji novi saradnici u open-source zajednici uče i doprinose po prvi put.

Čitanje članaka i gledanje tutorijala može pomoći, ali šta je bolje od stvarnog rada u praktičnom okruženju? Ovaj projekat ima za cilj da pruži smjernice i olakša početnicima njihov prvi doprinos. Ako želite da napravite svoj prvi doprinos, pratite korake ispod.

#### *Ako se ne osjećate prijatno koristeći komandnu liniju (terminal), [ovdje su tutorijali koji koriste GUI alate.](#tutorijali-koristeći-druge-alate)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="forkuj ovaj repozitorijum" />

Ako nemate instaliran git na svom računaru, [instalirajte ga](https://help.github.com/articles/set-up-git/).

## 1. Forkujte (kopirajte) ovaj repozitorijum

Forkujte ovaj repozitorijum klikom na dugme **Fork** na vrhu ove stranice. Ovo će kreirati kopiju ovog repozitorijuma na vašem GitHub nalogu.

## 2. Klonirajte repozitorijum

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="napravi sopstvenu kopiju" />

Sada klonirajte ovaj repozitorijum na svoj računar. Idite na svoj GitHub nalog, otvorite forkovani repozitorijum, kliknite na dugme **Code**, a zatim kliknite na ikonicu *copy to clipboard* (kopiraj u clipboard).

Otvorite terminal i pokrenite sljedeću git komandu:

```bash
git clone "url koji ste upravo kopirali"

```

gdje je "url koji ste upravo kopirali" (bez navodnika) url do vašeg repozitorijuma (vaš fork ovog projekta). Pogledajte prethodne korake da dobijete ovaj url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="kopiraj link" />

Na primjer:

```bash
git clone [https://github.com/vase-korisnicko-ime/first-contributions.git](https://github.com/vase-korisnicko-ime/first-contributions.git)

```

gdje je `vase-korisnicko-ime` vaše GitHub korisničko ime. Ovim kopirate sadržaj first-contributions repozitorijuma sa GitHub-a na vaš računar.

## 3. Napravite novu granu (branch)

Prebacite se u direktorijum projekta na vašem računaru (ako već niste tamo):

```bash
cd first-contributions

```

Sada napravite novu granu koristeći komandu `git checkout`:

```bash
git checkout -b <ime-vaše-nove-grane>

```

Na primjer:

```bash
git checkout -b add-marko-markovic

```

(Ime grane ne mora da sadrži riječ *add*, ali je uobičajeno jer je svrha ove grane dodavanje vašeg imena na listu.)

## 4. Napravite izmjene i sačuvajte ih (commit)

Sada otvorite fajl `Contributors.md` u tekstualnom editoru i dodajte svoje ime u njega. Nemojte ga dodati na sam početak ili kraj fajla. Stavite ga bilo gdje između. Sačuvajte fajl.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="provjeri status" />

Ako odete u direktorijum projekta i pokrenete komandu `git status`, vidjećete da postoje izmjene.

Dodajte te izmjene u granu koju ste upravo kreirali koristeći komandu `git add`:

```bash
git add Contributors.md

```

Sada sačuvajte (commit-ujte) te izmjene koristeći komandu `git commit`:

```bash
git commit -m "Add <vase-ime> to Contributors list"

```

zamijenite `<vase-ime>` svojim imenom.

## 5. Pošaljite izmjene na GitHub (push)

Pošaljite svoje izmjene koristeći komandu `git push`:

```bash
git push origin <ime-vaše-grane>

```

zamijenite `<ime-vaše-grane>` imenom grane koju ste ranije kreirali.

## 6. Pošaljite izmjene na pregled (Pull Request)

Ako odete na svoj repozitorijum na GitHub-u, vidjećete dugme `Compare & pull request`. Kliknite na to dugme.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="podigni zastavu za pull request" />

Sada pošaljite pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="pošalji pull request kapetanu" />

Uskoro ću spojiti (merge) sve vaše izmjene u glavnu (master) granu ovog projekta. Dobićete obavještenje putem e-maila kada izmjene budu prihvaćene.

## Šta dalje?

Svaka čast! Upravo ste završili standardni ciklus *fork -> clone -> edit -> PR* koji ćete često sretati u svijetu otvorenog koda!

Proslavite svoj doprinos i podijelite ga sa prijateljima i pratiocima putem naše [web aplikacije](https://firstcontributions.github.io/#social-share).

Sada možemo početi sa doprinosima drugim projektima. Sastavili smo listu projekata sa jednostavnim zadacima (issues) na kojima možete početi. Pogledajte [listu projekata u web aplikaciji](https://firstcontributions.github.io/#project-list).

### [Dodatni materijal](https://www.google.com/search?q=../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorijali koristeći druge alate

| <a href="https://www.google.com/search?q=../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="https://www.google.com/search?q=../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="https://www.google.com/search?q=../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="https://www.google.com/search?q=../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="https://www.google.com/search?q=../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="https://www.google.com/search?q=../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](https://www.google.com/search?q=../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](https://www.google.com/search?q=../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](https://www.google.com/search?q=../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](https://www.google.com/search?q=../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](https://www.google.com/search?q=../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](https://www.google.com/search?q=../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
