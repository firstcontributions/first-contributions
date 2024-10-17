[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeres contribucions

Aquest projecta apunta a simplificar i guiar la manera en la qual els principiants fan la seva primera contribució. Si estàs mirant per fer la teva primera contribució, segueix els passos següents.

_Si no et sents còmode utilitzant comands, [aquí hi ha tutorials utilitzen una interfaç gràfica d'usuari](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Si no tens Git instal·lat, [l'has d'instal·lar](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Bifurcar aquest repositori

Fes-ho clicant el botó de bifurcar (Fork) a damunt d'aquesta pàgina.
Això crearà una còpia d'aquest repositori a la teva conta de GitHub.

## Clonar aquest repositori

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Ara clona el repositori bifurcat al teu ordinador. Ves al teu compte de GitHub, obre el repositori, clica al botó de codi (Code) i clica la icona _Copiar al porta-retalls_.

Obra el Treminal i executa la següent comanda:

```bash
git clone "L'URL que has copiat"
```

En el lloc diu "L'URL que has copiat" (sense les cometes) és l'URL d'aquest repositori (la teva bifurcació del repositori). Pots mirar els passos previs per obtenir l'URL.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Per exemple:

```bash
git clone git@github.com:aquest-ets-tu/first-contributions.git
```

En el lloc que diu `aquest-ets-tu` es el teu nom d'usuari de GitHub. Aquí esteu copiant el contingut del dipòsit de primeres contribucions a GitHub al vostre ordinador.

## Crear una branca

Canvieu al directori del repositori del vostre ordinador (si encara no hi sou):

```bash
cd first-contributions
```

Ara feu una branca utilitzant la comanda de 'git switch':

```bash
git switch -c el-nom-de-la-nova-branca
```

Per exemple:

```bash
git switch -c add-alonzo-church
```

## Feu els canvis necessaris i comprometeu-los

Ara obriu el fitxer `Contributors.md` en un editor de text, afegiu-hi el vostre nom. No l'afegiu al principi o al final del fitxer. Posa-ho en qualsevol lloc intermedi. Ara, deseu el fitxer.

<img align="right" width="450" ​​src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Si aneu al directori del projecte i executeu l'ordre `git status`, veureu que hi ha canvis.

Afegiu aquests canvis a la branca que acabeu de crear amb l'ordre `git add`:

```bash
git add Contributors.md
```

Ara a cometre aquests canvis amb la comanda `git commit`:

```bash
git commit -m "Add el-teu-nom to Contributors list"
```

Canviant el-teu-nom per el teu nom.

## Posar els teus canvis a GitHub:

Fes-ho utilitzant la comanda `git push`:

```bash
git push -u origin Nom-de-la-teva-branca
```

Remplaca el Nom-de-la-teva-branca Amb el nom de la branca que heu utilitzat avans.

<details>
<summary> <strong>Si tens algun error, clica aquí:</strong> </summary>

- ### Error de autentificació
     <pre>remot: la compatibilitat amb l'autenticació de contrasenya es va eliminar el 13 d'agost de 2021. Feu servir un testimoni d'accés personal.
  remot: consulteu https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ per obtenir més informació.
  fatal: l'autenticació ha fallat per a "https://github.com/<your-username>/first-contributions.git/"</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

</details>

## Envia els teus canvis per verificar

Si vas al teu repositori de GitHub, Veuras un botó de `Comparar i enviar la solicitud(Compare & pull request)`. Clica aquell botó.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Ara fes la solicitud.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Aviat fusionaré tots els vostres canvis a la branca principal d'aquest projecte. Rebràs un correu electrònic de notificació un cop s'hagin combinat els canvis.

## Cap on anar ara?

Felicitats! Acabeu de completar el flux de treball estàndard _fork -> clon -> edit -> pull request_ que sovint trobareu com a col·laborador!

Celebra la teva contribució i comparteix-la amb els teus amics i seguidors anant a [aplicació web](https://firstcontributions.github.io/#social-share).

Pots unir-te al nostre equip de Slack si necessites ajuda o tens cap pregunta. [Uneix-te a l'equip de Slack](https://firstcontributors.slack.com/join/shared_invite/zt-29qhyr9lt-Bi7WLbgGIFqV7aCEG_grvg#/shared-invite/email).

Ara anem a començar a contribuir a altres projectes. Hem compilat una llista de projectes amb problemes senzills amb els quals podeu començar. Consulteu [la llista de projectes a l'aplicació web] (https://firstcontributions.github.io/#project-list).

### [Material adicional](additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Utilitzant altres eines:

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Aquest projecte està suportat per:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
