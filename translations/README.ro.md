[![Surse Deschise Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![Licență: MIT](https://img.shields.io/badge/Licență-MIT-green)](https://opensource.org/licenses/MIT)
[![Contribuitori](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primele Contribuții

Acest proiect își propune să simplifice și să îndrume modul în care începătorii își fac prima contribuție. Dacă doriți să faceți prima contribuție, urmați pașii de mai jos.

_Dacă nu vă simțiți confortabil folosind linia de comandă, [aici sunt tutoriale folosind alte unelte (GUI)](#tutoriale-folosind-alte-unelte)._

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Realizați bifurcația depozitului" />

#### Dacă nu ai git instalat, [instalează-l](https://help.github.com/articles/set-up-git/).

## Realizați bifurcația depozitului

Efectuați bifurcația acestui depozit apăsând pe butonul `Fork` din partea de sus a acestei pagini.
Aceasta va crea o copie a acestui depozit în contul dvs.

## Clonați depozitul

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Clonați acest depozit" />

Acum clonați depozitul bifurcat pe computerul dvs. Mergeți în contul dvs. GitHub, deschideți depozitul bifurcat, apăsați pe butonul `Code` și apoi pe pictograma de _copiere în clipboard_.

Deschideți un terminal și executați următoarea comandă Git:

```bash
git clone "URL-ul pe care l-ați copiat"
```
unde `URL-ul pe care l-ați copiat` (fără ghilimele) este URL-ul către acest depozit (bifurcarea dvs. a acestui proiect). Consultați pașii anteriori pentru a obține URL-ul.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="Copiați URL-ul în clipboard" />

De exemplu:

```bash
git clone https://github.com/numele-tau/first-contributions.git
```
unde `numele-tau` reprezintă numele dvs. de utilizator GitHub. Aici copiați conținutul depozitului _first-contributions_ de pe GitHub pe computerul dvs.

## Creați o ramură

Schimbați directorul depozitului de pe computerul dvs. (dacă nu sunteți deja acolo):

```bash
cd first-contributions
```

Acum creați o ramură folosind comanda `git switch`:

```bash
git switch -c numele-noii-ramuri
```

De exemplu:

```bash
git switch -c adaug-alonzo-church
```

## Efectuați modificările necesare și comiteți acele modificări

Acum deschideți fișierul `Contributors.md` într-un editor de text, adăugați-vă numele în el. Nu-l adăugați la începutul sau la sfârșitul fișierului. Puneți-l oriunde între acestea. Apoi, salvați fișierul.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="Stare git" />

Dacă mergeți în directorul proiectului și executați comanda `git status`, veți vedea că există modificări.

Adăugați aceste modificări în ramura pe care tocmai ați creat-o folosind comanda `git add`:

```bash
git add Contributors.md
```

Acum comiteți acele modificări folosind comanda `git commit`:

```bash
git commit -m "Adaug numele-tau la lista de Contribuitori"
```
înlocuind `numele-tau` cu numele dvs.

## Încărcați modificările pe GitHub

Împinge schimbările tale cu comanda `git push`:

```bash
git push -u origin numele-ramurii-tale
```
înlocuind `numele-ramurii-tale` cu numele ramurii pe care ați creat-o anterior.

<details>
<summary> <strong>Dacă întâmpinați erori în timpul încărcării, apăsați aici:</strong> </summary>

  - ### Eroare de autentificare
   <pre>remote: Suportul pentru autentificarea prin parolă a fost eliminat la 13 august 2021. Vă rugăm să utilizați un token de acces personal în schimb.
remote: Vă rugăm să consultați https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ pentru mai multe informații.
fatal: Autentificare eșuată pentru 'https://github.com/<numele-tau>/first-contributions.git/'</pre>
înlocuind `numele-tau` cu numele dvs. de utilizator GitHub.

Mergeți la [tutorialul GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) pentru a genera și configura o cheie SSH pentru contul dvs.

</details>

## Trimiteți modificările pentru a fi revizuite

Dacă mergeți în depozitul dvs. de pe GitHub, veți vedea un buton `Compară și cereți trageri`. Faceți clic pe acest buton.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Creați o cerere de tragere" />

Acum trimiteți cererea de tragere.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Trimiteți cererea de tragere" />

În curând, voi integra toate modificările dvs. în ramura principală a acestui proiect. Veți primi o notificare prin e-mail odată ce modificările vor fi integrate.

## Unde să mergeți de aici?

Felicitări! Ați finalizat fluxul standard _fork -> clone -> edit -> pull request_ pe care îl veți întâlni adesea ca contributor!

Sărbătoriți-vă contribuția și partajați-o cu prietenii și urmăritorii dvs., accesând [aplicația web](https://firstcontributions.github.io/#social-share).

Puteți să vă alăturați echipei noastre Slack dacă aveți nevoie de ajutor sau aveți întrebări. [Alăturați-vă echipei Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w).

Acum să vă începem cu contribuția la alte proiecte. Am compilat o listă de proiecte cu probleme ușoare cu care puteți începe. Verificați [lista de proiecte din aplicația web](https://firstcontributions.github.io/#project-list).

### [Materiale suplimentare](additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriale Folosind Alte Unelte (GUI)

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Acest proiect este susținut de:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
