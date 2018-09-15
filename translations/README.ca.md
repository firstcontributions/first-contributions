[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primeres Contribucions

És difícil. Sempre ho és quan es fa algo per primera vegada. Especialment quan es col·labora amb altres, ja que efectuar errades no es gens agradable. Es vol simplificar la manera en que els col·laboradors de codi obert aprenen i contribueixen per primera vegada.

Llegir articles i mirar tutorials pot ser d'ajuda, però què millor que fer les coses en un entorn de pràctiques? Aquest projecte és una guia, simplificant la forma de fer la primera contribució per als principiants. Si voleu fer la primera contribució, seguiu les instruccions que es mostren a continuació: 

#### *Si no esteu còmode amb la línia d'ordres, [aquí hi ha tutorials utilitzant eines amb Interfaç Gràfica (GUI)]( #tutorials-using-other-tools )*

#### *Llegir en [altres idiomes](Translations.md).*

[🇬🇧](../README.md) [🇮🇳](README.hi.md) [🇲🇲](README.mm_unicode.md) [🇮🇩](README.id.md) [🇫🇷](README.fr.md) [🇪🇸](README.es.md) [🇳🇱](README.nl.md) [🇷🇺](README.ru.md) [🇯🇵](README.ja.md) [🇻🇳](README.vn.md) [🇵🇱](README.pl.md) [🇮🇷](README.fa.md) [🇮🇷](README.fa.en.md) [🇰🇷 🇰🇵](README.ko.md) [🇩🇪](README.de.md) [🇨🇳](README.chs.md) [🇹🇼](README.cht.md) [🇬🇷](README.gr.md) [🇺🇦](README.ua.md) [🇧🇷](README.pt_br.md) [🇵🇹](README.pt-pt.md) [🇮🇹](README.it.md) [🇹🇭](README.th.md) [🏴󠁥󠁳󠁧󠁡󠁿](README.gl.md) [🇵🇰](README.ur.md) [:bangladesh:](README.bn.md) [🇲🇩 🇷🇴](README.ro.md) [🇹🇷](README.tr.md) [🇸🇪](README.se.md) [🇮🇱](README.hb.md)

<img align="right" width="300" src="../assets/fork.png" alt="fer fork d'aquest repsoitori" />

Si no disposeu de git en el vostre ordinador, [instal·leu-lo]( https://help.github.com/articles/set-up-git/).

## Bifurca (*Fork*) aquest respositori

Feu un *fork* d'aquest repositori clicant al botó "*Fork*" a la part superior dreta d'aquesta pàgina.
Això crearà una còpia d'aquest repositori en el seu compte.

## Clona (*Clone*) el repositori

<img align="right" width="300" src="../assets/clone.png" alt="clonar aquest repositori" />

Cloneu aquest repositori al vostre ordinador. Adreceu-vos al vostre compte de GitHub, cliqueu al botó clonar "*clone or download*" i després cliqueu a la icona de *copiar al porta-retalls*.

Obriu una terminal i executeu la següent comanda de git:

```
git clone "url que acabeu de copiar"
```
on "url que acabeu de copiar" (sense cometes dobles) és la *url* per a aquest respositori (el vostre *fork* d'aquest projecte). Veure els passos anteriors per a obtenir la *url*.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copiar URL al porta-retalls" />

Per exemple:
```
git clone https://github.com/aquest-soc-jo/first-contributions.git
```
on `aquest-soc-jo` és el vostre nom d'usuari de GitHub. Aquí esteu copiant el contingut del repository *first-contributions* de GitHub al vostre ordinador.

## Crea una branca (*branch*)

Canvieu al directori del repositori del vostre ordinador (si no hi esteu allà ja):

```
cd first-contributions
```
Creeu una nova branca (*branch*) utilitzant la comanda `git checkout`:
```
git checkout -b <afegiu-el-nom-de-la-nova-branca>
```

Per exemple:
```
git checkout -b add-nom-cognom
```
(No és necessari que el nom de la branca contingui la paraula *add*, però es recomanable ja que el propòsit d'aquesta branca és afegir el seu nom a la llista.)

## Fer els canvis necessaris i confirmar (*commit*) els canvis

Obriu l'arxiu `Contributors.md` en un editor de text i afegeiu el vostre nom. No l'afegiu ni al principi ni al final de l'arxiu. Poseu-lo en qualsevol altre posició. Guardeu l'arxiu.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />


Si aneu al directori del projecte i executeu la comanda `git status`, veureu els canvis. 


Afegiu aquests canvis a la branca que acabeu de crear utilitzant la comanda `git add`:

```
git add Contributors.md
```

Confirmeu (*commit*) els canvis utilitzant la comanda `git init`:
```
git commit -m "Add <el-meu-nom> to Contributors list"
```
reemplaçant `<el-meu-nom>` amb el vostre nom.

## Envia (*Push*) els canvis a GitHub

Feu un *Push* dels canvis utilitzant la comanda  `git push`:
```
git push origin <afegiu-el-nom-de-la-branca>
```
reemplaçant  `<afegiu-el-nom-de-la-branca>` amb el nom de la branca que heu creat anteriorment.

## Submit your changes for review

If you go to your repository on GitHub, you'll see a  `Compare & pull request` button.  Click on that button.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="assets/submit-pull.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Delete the branch after pull request has been merged

You can safely delete your branch `<add-your-branch-name>` after the pull request has been merged. You'll see a button to delete the branch:

<img style="float: right;" src="assets/delete-branch-after-pr.png" alt="delete branch after PR is merged" />

If the Pull Request was closed without being merged, GitHub will warn you about deleting unmerged commits and the button will look like this:

<img style="float: right;" src="assets/delete-branch-warning.png" alt="delete branch after PR is not merged" />

## Where to go from here?

Congrats!  You just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://roshanjossey.github.io/first-contributions/#social-share).

You could join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Other Tools

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|

## Self-Promotion

If you liked this project, star it on [GitHub](https://github.com/Roshanjossey/first-contributions).
If you're feeling especially charitable, follow [Roshan](https://roshanjossey.github.io/) on
[Twitter](https://twitter.com/sudo__bangbang) and
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
