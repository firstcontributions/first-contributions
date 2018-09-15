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

## Envía (*Submit*) els canvis per a ser revisats

Si aneu al vostre respositori a GitHub, veureu un botó  `Compare & pull request`. Cliqueu sobre aquest botó.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="crear una pull request" />

Envía la *pull request*.

<img style="float: right;" src="../assets/submit-pull.png" alt="envia la pull request" />

Aviat estaré fusionant els vostres canvis en la branca (*branch*) master d'aquest projecte. Rebreu una notificació per correu electrònic un cop els canvis hagin sigut fusionats.

## Eliminar la branca (*branch*) master després de que la *pull request* hagi sigut fusionada

Podeu eliminar de forma segura la branca (*branch*) `<afegiu-el-nom-de-la-branca>` un cop la *pull request* hagi sigut fusionada. Veureu un botó per a leiminar la branca (*branch*):

<img style="float: right;" src="../assets/delete-branch-after-pr.png" alt="eliminar branch un cop PR s'ha fusionat" />

Si la *Pull Request* ha sigut tancada sense haver estat fusionada, GitHub li advertirà sobre el fet d'eliminar *commits* no fusionats i el botó es veurà així:

<img style="float: right;" src="../assets/delete-branch-warning.png" alt="eliminar branca després de que la PR no estigui fusionada" />

## On anar des d'aquí?

Enhorabona! Acabeu de completar l'estàndard flux de treball *_fork -> clone -> edit -> PR_* que trobareu sovint com a col·laborador!

Celebreu la vostra contribució i compartiu-ho amb els vostres amics i seguidors anant a [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Podeu unir-vos al nostre equip d'*slack* en cas de que necessiteu ajuda o tingueu alguna pregunta. [Unir-se a l'equip d'slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Ara anem a preparar-nos per a contribuir a altres projectes. Hem reunit una llista de projectes amb îssues* facils per a que pugueu començar. Doneu un cop d'ull [la llista de projectes en la web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials amb Altres Eines

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Auto promoció

Si us ha agradat aquest projecte, marqueu-lo com a favorit amb una estrella a [GitHub](https://github.com/Roshanjossey/first-contributions).
Si us sentiu especialment agraïts, seguiu en [Roshan](https://roshanjossey.github.io/) a
[Twitter](https://twitter.com/sudo__bangbang) i
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
