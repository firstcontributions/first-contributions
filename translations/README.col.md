[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeras Contribuciones

Uy, la cosa está complicada. La primera vez que uno le mete la ficha a algo nuevo es re difícil, ¿sí o qué? Más cuando toca camellar con otra gente, porque nadie quiere meter las patas y quedar como un guevón. Nosotros queremos es que los pipiolos que le quieren entrar al código abierto la tengan más suave para aprender y aportar su granito de arena.

Bacano leer artículos y ver tutoriales y toda esa vaina, pero nada como aprender haciendo, ¿o no? Este proyecto es una guía re chévere para que los novatos le cojan el tiro a esto de contribuir por primera vez. Si quieres estrenar tus pinitos en esto, sigue estos pasos al pie de la letra:

#### _Si no le has cogido el tiro a la consola,[acá tenés tutoriales con herramientas más amigables (GUI)](#Tutoriales-con-otras-herramientas)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork de este repositorio" />

Si no tenés git en tu aparato, podés encontrar cómo instalarlo en[este link](https://docs.github.com/es/get-started/quickstart/set-up-git).

## Hacele un (_Fork_) a este repositorio

Dale click al botón de "_Fork_" allá arriba a la derecha de esta página.
Eso te va a crear una copia de este repositorio en tu cuenta, facilito.

## Clona (_Clone_) el repositorio Forkeado

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositorio" />

Ahora toca clonar este repositorio en tu compu. Andate a tu cuenta de GitHub, dale al botón de "_clone or download_" y después al iconito para _copiar al portapapeles_.

Abre tu consola o terminal y ejecuta el siguiente comando de git:

```
git clone "url que acabas de copiar"
```

Donde dice "url que acabas de copiar" (sin las comillas, ojo) es la _url_ de este repositorio (tu _fork_ del proyecto). Mira los pasos de antes para sacar la _url_.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

Por ejemplo:

```
git clone https://github.com/este-eres-tu/first-contributions.git
```

Cambiá `este-eres-tu` por tu usuario de GitHub. Acá estás copiando todo el contenido del repositorio _first-contributions_ de GitHub a tu compu.

## Crea una rama (_Branch_)

Metete al directorio del repositorio en tu compu (si no estás ya ahí).

```
cd first-contributions
```

Ahora crea una rama (_branch_) usando el comando `git checkout`:

```
git checkout -b <añade tu nombre>
```

Por ejemplo:

```
git checkout -b add-alonzo-church
```

(No es obligatorio que el nombre de la rama tenga la palabra add, pero tiene sentido ponerla porque la idea de esta rama es agregar tu nombre a la lista.)

## Hacé los cambios necesarios y confirmalos (_Commit_)

Abrí el archivo `Contributors.md` en un editor de texto y agregá tu nombre. No lo pongas ni al principio ni al final del archivo, metelo en cualquier otro lado. Guardá el archivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Si vas al directorio del proyecto y ejecutas el comando `git status`, verás que hay cambios.

Agrega esos cambios a la rama (_branch_) que creaste anteriormente usando el comando `git add`:

```
git add Contributors.md
```

Ahora hacele un _commit_ a esos cambios ejecutando el comando `git commit`:

```
git commit -m "Add <tu-nombre> to Contributors list"
```

cambiando `<tu-nombre>` por tu nombre, obviamente.

## Subí (_Push_) tus cambios a GitHub

Mandale un _push_ de tus cambios usando el comando `git push`:

```
git push origin <añade-el-nombre-de-la-rama>
```

Reemplaza `<añade-el-nombre-de-la-rama>` con el nombre de la rama que creaste antes.

## Mandá (_Submit_) tus cambios para que los revisen

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Dale click sobre este botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crea una pull request" />

Ahora mandá la _pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="enviar la pull request" />

Dentro de poco voy a estar fusionando tus cambios (haciendo merge) con la rama master de este proyecto. Te va a llegar un correo cuando los cambios estén fusionados.

## ¿Y ahora qué sigue?

¡Felicitaciones parcero! ¡Le diste la vuelta completa al proceso _fork -> clone -> edit -> PR_ que vas a usar un montón como contribuidor!

Celebrá tu aporte y compartilo con tus amigos y seguidores en la.[web app](https://firstcontributions.github.io/#social-share).

También te podés unir a nuestro equipo de Slack si necesitás una mano o tenés alguna pregunta.[Unite a nuestro Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Ahora dale, empezá a contribuir a otros proyectos. Armamos una lista de proyectos con issues fáciles para que arranques. Dale una mirada a la[lista de proyectos en la aplicación web](https://firstcontributions.github.io/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriales con otras herramientas

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
