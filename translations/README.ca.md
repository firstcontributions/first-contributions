[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primeres Contribucions

És difícil. Sempre es difícil fer una cosa per primera vegada. Sobretot quan es col·labora amb altres, ja que equivocar-se no és gens agradable. Volem simplificar la manera d'aprendre a contribuir i col·laborar en projectes de codi obert per primera vegada.

Llegir articles i mirar tutorials pot ser útil, però què millor que fer les coses en un entorn pràctic real? Aquest projecte és una guia per a principiants que vol simplificar la primera contribució a projectes de codi oberts. Si vols fer la teva primera contribució, segueix les instruccions que es mostren a continuació:

#### *Si no et sents còmode/a amb la línia d'ordres (*Command Line*), [aquí trobaràs tutorials utilitzant eines que tenen Interfície Gràfica (GUI)](#Tutorials-amb-Altres-Eines)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fer fork d'aquest repositori" />

Si no tens git al teu ordinador, l'hauràs d'[instal·lar]( https://help.github.com/articles/set-up-git/).

## Bifurca (*Fork*) aquest respositori

Fes una *fork* d'aquest repositori clicant al botó "*Fork*" a la part superior dreta d'aquesta pàgina.
Això crearà una còpia d'aquest repositori al teu compte de GitHub.

## Clona (*Clone*) el repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar aquest repositori" />

Clona aquest repositori al teu ordinador: ves al teu compte de GitHub, fes clic al botó clonar "*clone or download*" del repositori, i després clica a la icona de *copiar al porta-retalls*.

Obre una terminal/línia d'ordre i executa el següent comandament de git:

```
git clone "url que acabes de copiar"
```
on "url que acabeu de copiar" (sense cometes dobles) és la *url* per a aquest repositori (la vostra bifurcació o *fork* d'aquest projecte). Per obtenir la *url*, torna als passos anteriors.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al porta-retalls" />

Per exemple:
```
git clone https://github.com/aquest-soc-jo/first-contributions.git
```
on `aquest-soc-jo` és el teu nom d'usuari de GitHub. En aquest pas, estàs copiant el contingut del repositori *first-contributions* de GitHub al teu ordinador.

## Crea una branca (*branch*)

Canvieu al directori del repositori del vostre ordinador (si no hi esteu allà ja):

```
cd first-contributions
```
Crea una nova branca (*branch*) utilitzant el comandament `git checkout`:
```
git checkout -b <afegiu-el-nom-de-la-nova-branca>
```

Per exemple:
```
git checkout -b add-nom-cognom
```
(No fa falta que el nom de la branca contingui la paraula *add* però és recomanable, ja que l'objectiu d'aquesta branca és afegir el teu nom a la llista.)

## Fes els canvis necessaris i confirma (*commit*) els canvis

Obre l'arxiu `Contributors.md` en un editor de text i afegeix-hi el teu nom. No l'afegeixis ni al principi, ni al final de l'arxiu. Posa'l en qualsevol altre posició. Llavors desa l'arxiu.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Ara, si vas al directori del projecte i executes el comandament `git status`, veuràs els canvis.


Afegeix aquests canvis a la branca que acabes de crear utilitzant el comandament `git add`:

```
git add Contributors.md
```

Confirma (*commit*) els canvis utilitzant el comandament `git init`:
```
git commit -m "Add <el-meu-nom> to Contributors list"
```
reemplaçant `<el-meu-nom>` amb el teu nom.

## Empeny (*Push*) els canvis cap a GitHub

Envia els canvis utilitzant el comandament `git push`:
```
git push origin <afegiu-el-nom-de-la-branca>
```
reemplaçant  `<afegiu-el-nom-de-la-branca>` amb el nom de la branca que has creat anteriorment.

## Envia (*Submit*) els canvis per tal que siguin revisats

Si ara vas al teu respositori a GitHub, veuràs un botó  `Compare & pull request` (Compara i fes una solicitud d'incorporació). Fes clic en aquest botó.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crear una pull request" />

Envia la solicitud d'incorporació (*pull request*).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="envia la pull request" />

Quan un administrador vegi la solicitud, la revisarà i incorporarà els teus canvis a la branca principal (*main branch*) del projecte. Rebràs una notificació per correu electrònic quan els canvis s'hagin incorporat.

## I ara què?

Enhorabona! Acabes de completar el procés de treball principal que et trobaràs com a col·laborador de projectes de codi obert: *_fork -> clone -> edit -> PR_*.

Ara, celebra la teva contribució i comparteix-la amb els teus amics i seguidors anant a [la web](https://firstcontributions.github.io/#social-share).

Podeu unir-vos al nostre equip d'*slack* en cas de que necessiteu ajuda o tingueu alguna pregunta. [Unir-se a l'equip d'slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

A continuació, et pots preparar per contribuir a altres projectes. Hem reunit una llista de projectes amb tasques (*issues*) pendents fàcils per tal de poder començar. Fes un cop d'ull a [la llista de projectes aquí](https://firstcontributions.github.io/#project-list).

### [Material extra](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials utilitzant altres eines

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](https://www.jetbrains.com/idea/download/#section=windows)                                                                                                                   |
