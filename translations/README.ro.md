[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primele contribuții

Este greu. Este întotdeauna greu atunci când faci ceva pentru prima dată. Mai ales atunci când colaborezi. A face greșeli nu este un lucru confortabil. Însa cele mai importante aspecte în open source sunt colaborarea și lucrul în echipă. Noi am vrut să simplificăm modul în care noii contribuabili învață și contribuie pentru prima dată la un proiect open source.

Citirea articolelor și vizionarea tutorialelor pot ajuta, însa ce este mai bine decât să faci lucrurile fără a strica ceva? Acest proiect își propune să ofere îndrumare și o simplificare a modului în care începătorii fac prima lor  contribuție. Amintește-ți: cu cât ești mai relaxat, cu atât înveți mai bine. Dacă dorești să faci prima ta contribuție, urmează pur și simplu pașii de mai jos. Îți promit că va fi distractiv.

#### *Citește în [alte limbi](Translations.md).* 

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Dacă nu ai git instalat, [ instalează-l ]( https://help.github.com/articles/set-up-git/ ).

## Ramifică repozitoriul(depozitul)

Ramifică acest repository  (depozit) făcând clic pe butonul fork locat pe partea de sus a paginii.
Acesta va creea o copie a repozitoriului în contul tău.

## Clonează repozitoriul(depozitul)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Acum clonează acest repo pe computerul tău. Dă clic pe butonul clone apoi clic pe *copiați în clipboard*.

Deschide un terminal și executa următoarea comanda git: 

```
git clone "adresa copiată"
```
unde "adresa copiată" (fără ghilimele) este adresa repozitoriului. Vezi pașii anteriori pentru a obține adresa.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

De exemplu:
```
git clone https://github.com/acesta-ești-tu/prima-contribuție.git
```
Unde `acesta-ești-tu` este numele tău GitHub. Aici copiezi conținutul repozitorului GitHub "prima-contribuție" pe computerul tău.

## Creează o ramură

Schimba directorul în repozitoriu pe computer (dacă nu ești deja acolo):

```
cd prima-contribuție
```
Acum crează o ramură cu ajutorul comenzii `git checkout`:
```
git checkout -b <adaug-numele-tău>
```

De exemplu:
```
git checkout -b adaug-alonzo-church
```
(nu este obligatoriu ca numele ramurii să conțină cuvantul *adaug*, însă poate fi un lucru util și rezonabil, deoarece scopul acestei ramuri este de a adăuga numele tău în lista!)

## Fă schimbările necesare și comite-le

Acum deschide fișierul `Contributors.md` într-un editor de text (ca NotePad, Vim, nano, emacs, etc.), adaugă numele tău în el, apoi salvează fișierul. Dacă accesezi     de proiect și execuți comanda `git status`, vei vedea schimbări. Adaugă acele schimbări la ramura creată de tine cu comanda `git add`:
```
git add Contributors.md
```

Acum comite acele schimbări cu comanda `git commit`:
```
git commit -m "Adaug <numele-tău> la lista de contribuitori"
```
înlocuind `<numele-tău>` cu numele tău.

## Împinge modificările pe GitHub

Împinge modificările tale cu comanda `git push`:
```
git push origin <adaug-numele-tău>
```
înlocuind `<adaug-numele-tău>` cu numele ramurii create de tine anterior.

## Trimite modificările pentru examinare

Dacă pleci la repozitoriul tău de pe GitHub, vei vedea butonul `Compare & pull request`(Compară & trage cererea). Apasă clic pe el.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Acum trimite solicitarea de tragere.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

În scurt timp, eu voi adăuga toate modificările în ramura principală a acestui proiect. Vei primi un e-mail de notificare odată ce schimbările au fost fuzionate.

## Unde poți să mergi de aici?

Felicitări! Tocmai ai terminat de făcut pașii standard fork->clone->edit->pull request pe care îi vei întâlni în mod frecvent ca și contributor!

Sărbătorește-ți contribuția și împărtășește-o cu prietenii și cu fanii tai accesând [aplicația web](https://roshanjossey.github.io/first-contributions/#social-share).

Daca dorești, poți să te alături echipei noastre în cazul în care ai nevoie de ajutor sau ai întrebări. [Alătură-te echipei Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Acum, să începem să contribuim la alte proiecte. Am compilat o listă de proiecte cu probleme ușoare pe care le poți începe. Verifică  [lista de proiecte in aplicația web](https://roshanjossey.github.io/first-contributions/#project-list).

### [ Materiale adiționale ](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriale folosind alte unelte

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

