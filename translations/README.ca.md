[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primeres Contribucions

És difícil. Sempre ho és quan es fa algo per primera vegada. Especialment quan es col·labora amb altres, ja que efectuar errades no es gens agradable. Es vol simplificar la manera en que els col·laboradors de codi obert aprenen i contribueixen per primera vegada.

Llegir articles i mirar tutorials pot ser d'ajuda, però què millor que fer les coses en un entorn de pràctiques? Aquest projecte és una guia, simplificant la forma de fer la primera contribució per als principiants. Si voleu fer la primera contribució, seguiu les instruccions que es mostren a continuació: 

#### *Si no esteu còmode amb la línia d'ordres, [aquí hi ha tutorials utilitzant eines amb Interfaç Gràfica (GUI)](#Tutorials-amb-Altres-Eines)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fer fork d'aquest repsoitori" />

Si no disposeu de git en el vostre ordinador, [instal·leu-lo]( https://help.github.com/articles/set-up-git/).

## Bifurca (*Fork*) aquest respositori

Feu un *fork* d'aquest repositori clicant al botó "*Fork*" a la part superior dreta d'aquesta pàgina.
Això crearà una còpia d'aquest repositori en el seu compte.

## Clona (*Clone*) el repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar aquest repositori" />

Cloneu aquest repositori al vostre ordinador. Adreceu-vos al vostre compte de GitHub, cliqueu al botó clonar "*clone or download*" i després cliqueu a la icona de *copiar al porta-retalls*.

Obriu una terminal i executeu la següent comanda de git:

```
git clone "url que acabeu de copiar"
```
on "url que acabeu de copiar" (sense cometes dobles) és la *url* per a aquest respositori (el vostre *fork* d'aquest projecte). Veure els passos anteriors per a obtenir la *url*.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al porta-retalls" />

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

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


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

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crear una pull request" />

Envía la *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="envia la pull request" />

Aviat estaré fusionant els vostres canvis en la branca (*branch*) master d'aquest projecte. Rebreu una notificació per correu electrònic un cop els canvis hagin sigut fusionats.

## On anar des d'aquí?

Enhorabona! Acabeu de completar l'estàndard flux de treball *_fork -> clone -> edit -> PR_* que trobareu sovint com a col·laborador!

Celebreu la vostra contribució i compartiu-ho amb els vostres amics i seguidors anant a [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Podeu unir-vos al nostre equip d'*slack* en cas de que necessiteu ajuda o tingueu alguna pregunta. [Unir-se a l'equip d'slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Ara anem a preparar-nos per a contribuir a altres projectes. Hem reunit una llista de projectes amb îssues* facils per a que pugueu començar. Doneu un cop d'ull [la llista de projectes en la web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials amb Altres Eines

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](https://www.jetbrains.com/idea/download/#section=windows)                                                                                                                   |

