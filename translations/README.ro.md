[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primele Contribuții

Este greu. Este întotdeauna greu când faci ceva pentru prima dată. Mai ales când colaborezi, a face greșeli nu este un lucru confortabil. Noi am vrut să simplificăm modul în care noii contribuitori în open source învață și contribuie pentru prima dată.

Citirea articolelor și vizionarea tutorialelor poate ajuta, dar ce este mai bine decât chiar să faci lucrurile fără a strica ceva? Acest proiect își propune să ofere îndrumare și sa simplifice modul în care începătorii își fac prima contribuție. Dacă dorești să faci prima ta contribuție, urmeaza pasii de mai jos.

#### *Citește în [alte limbi](Translations.md).*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Dacă nu ai git instalat, [ instalează-l ]( https://help.github.com/articles/set-up-git/ ).

## Ramifică repozitoriul (depozit)

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Ramifică acest repozitoriu (depozit) dând click pe butonul fork localizat în partea de sus a paginii.
Acesta va creea o copie a repozitoriului în contul tău.

## Clonează repozitoriul (depozit)

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Acum clonează acest repozitoriu pe computerul tău. Dute pe contul tau de GitHub, deschide repozitoriul, dă click pe butonul clone apoi clic pe *copiați în clipboard*.

Deschideți un terminal și executați următoarea comanda git:

```
git clone "adresa copiată"
```
Unde "adresa copiată" (fără de ghilimele) este adresa repozitoriului. Vezi pașii anteriori pentru a obține adresa.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

De exemplu:
```
git clone https://github.com/acesta-ești-tu/prima-contribuție.git
```
Unde `acesta-ești-tu` este numele tău de utilizator de pe GitHub. Aici tu copiezi conținutul repozitorului GitHub "prima-contribuție" pe calculatorul tău.

## Creează o Ramură

Schimbați directorul actual în repozitoriul de pe computer (dacă nu sunteți deja acolo):

```
cd prima-contribuție
```
Acum creați o ramură cu ajutorul comenzii `git checkout`:
```
git checkout -b <adaugă-numele-noii-ramuri>
```

De exemplu:
```
git checkout -b adaugă-alonzo-church
```
(Numele ramurii nu e obligatoriu să fie *adaugă*, dar e un lucru rezonabil de inclus deoarece scopul acestei ramuri este de a adăuga numele tău în lista.)

## Fă schimbările necesare și comite aceste schimbări

Acum deschide fișierul `Contributors.md` într-un editor de text (ca NotePad, Vim, nano, emacs, etc.), adaugă numele tău în el. Nu il adăuga la început sau la sfârșit, ci undeva între. Acum salvează fișierul.

<img align="right" width="300" src="../assets/git-status.png" alt="git status" />

Dacă accesezi directorul de proiect și execuți comanda `git status`, vei vedea că sunt schimbări.

Adaugă acele schimbări la ramura creată de tine cu comanda `git add`:
```
git add Contributors.md
```

Acum comite acele schimbări cu comanda `git commit`:
```
git commit -m "Adaugă <numele-tău> la lista de contribuitori"
```
schimbând `<numele-tău>` cu numele tău.

## Împinge Schimbările pe GitHub

Împinge schimbările tale cu comanda `git push`:
```
git push origin <adaugă-numele-ramurii-tale>
```
schimbând `<adaugă-numele-ramurii-tale>` cu numele ramurii create de tine anterior.

## Trimite modificările pentru examinare

Dacă mergi la repozitoriul tău de pe GitHub, vei vedea butonul `Compare & pull request`(Compară & trage cererea). Dă click pe buton.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Acum trimite solicitarea de tragere.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Curând eu voi îmbina toate schimbările tale în ramura principală a acestui proiect. Vei primi o notificare pe e-mail odată ce schimbările au fost fuzionate.

## Unde să mergi de aici?
Felicitări! Tocmai ai terminat procedura fork->clone->edit->PR pe care o vei întâlni de nenumărate ori.

Sărbătorește-ți contribuția și împărtășești-o cu prietenii și adepții tăi accesând [aplicația web](https://roshanjossey.github.io/first-contributions/#social-share).

Ai putea să te alături echipei noastre de pe Slack în cazul în care avei nevoie de ajutor sau avei întrebări. [Alătură-te echipei Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Acum, să începem să contribuim la alte proiecte. Am compilat o listă de proiecte cu probleme ușoare cu care puteți începe. Verifică  [lista de proiecte in aplicația web](https://roshanjossey.github.io/first-contributions/#project-list).

### [ Materiale adiționale ](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriale Folosind Alte Unelte

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Promovare-Personală

Dacă ți-a plăcut acest proiect, pune-i o stea pe [GitHub](https://github.com/Roshanjossey/first-contributions).
Dacă te simți deosebit de caritabil, urmariți [Roshan](https://roshanjossey.github.io/) pe
[Twitter](https://twitter.com/sudo__bangbang) și
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
