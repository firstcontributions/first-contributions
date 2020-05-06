[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primele Contribuții

Este greu. Este întotdeauna greu când faci ceva pentru prima dată. Mai ales când colaborezi. A face greșeli nu este un lucru confortabil. Dar cel mai important în open source este colaborarea și lucrul în echipă. Noi am vrut să simplificăm modul în care noii contribuabili în open source învață și contribuie pentru prima dată.

Citirea articolelor și vizionarea tutorialelor poate ajuta, dar ce este mai bine decât să faci lucrurile fără a strica ceva? Acest proiect își propune să ofere îndrumare și simplificarea modului în care începătorii își fac prima contribuție. Amintește-ți: cu cât ești mai relaxat, cu atât mai bine înveți. Dacă dorești să faci prima ta contribuție, simplu urmați pașii de mai jos. Vă promit că va fi distractiv.

#### *Citește în [alte limbi](Translations.md).* 

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Dacă nu ai git instalat, [ instalează-l ]( https://help.github.com/articles/set-up-git/ ).

## Ramifică repozitoriul(depozit)

Ramifică acest repo(depozit) făcând clic pe butonul fork locat pe partea de sus a paginii.
Acesta va creea o copie a repozitoriului în contul tău.

## Clonează repozitoriul(depozit)

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Acum clonează acest repo pe computerul tău. Fă clic pe butonul clone apoi clic pe *copiați în clipboard*.

Deschideți un terminal și executați următoarea comanda git: 

```
git clone "adresa copiată"
```
Unde "adresa copiată" (Fără de ghilimele) este adresa repozitoriului. Vezi pașii anteriori pentru a obține adresa.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

De exemplu:
```
git clone https://github.com/acesta-ești-tu/prima-contribuție.git
```
Unde `acesta-ești-tu` este numele tău GitHub. Aici tu copiezi conținutul repozitorului GitHub "prima-contribuție" pe computerul tău.

## Creează o Ramură

Schimbați directorul în repozitoriu pe computer (dacă nu sunteți deja acolo):

```
cd prima-contribuție
```
Acum creați o ramură cu ajutorul comenzii `git checkout`:
```
git checkout -b <adaug-numele-tău>
```

De exemplu:
```
git checkout -b adaug-alonzo-church
```
(Numele ramurii nu e obligatoriu să fie *adaug*, dar e un lucru rezonabil pentru a include deoarece scopul acestei ramure este de a adăuga numele tău în lista!)

## Fă schimbările necesare si comite aceste schimbări

Acum deschide fișierul `Contributors.md` într-un editor de text (ca NotePad, Vim, nano, emacs, etc.), adaugă numele tău în el, apoi salvează fișierul. Dacă accesezi directorul de proiect și execuți comanda `git status`, vei vedea schimbări. Adaugă acele schimbări la ramura creată de tine cu comanda `git add`:
```
git add Contributors.md
```

Acum comite acele schimbări cu comanda `git commit`:
```
git commit -m "Adaug <numele-tău> la lista de contribuitori"
```
Schimbând `<numele-tău>` cu numele tău.

## Împinge Schimbările pe GitHub

Împinge schimbările tale cu comanda `git push`:
```
git push origin <adaug-numele-tău>
```
Schimbând `<adaug-numele-tău>` cu numele ramurii create de tine anterior.

## Trimite modificările pentru examinare

Dacă pleci la repozitoriul tău de pe GitHub, vei vedea butonul `Compare & pull request`(Compară & trage cererea). Fă clic pe el.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Acum trimiteți solicitarea de tragere.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Curând eu voi îmbina toate schimbările în ramura principală a acestui proiect. Veți primi un e-mail de notificare odată ce schimbările au fost fuzionate.

## De unde să mergi de aici?

Sărbătoriți-vă contribuția și împărtășiți-o cu prietenii și adepții dvs. accesând [aplicația web](https://roshanjossey.github.io/first-contributions/#social-share).

Ați putea să vă alăturați echipei noastre în cazul în care aveți nevoie de ajutor sau aveți întrebări. [Alătură-te echipei Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Acum, să începem să contribuiți la alte proiecte. Am compilat o listă de proiecte cu probleme ușoare pe care le puteți începe. Verifică  [lista de proiecte in aplicația web](https://roshanjossey.github.io/first-contributions/#project-list).

### [ Materiale adiționale ](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriale Folosind Alte Unelte

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

