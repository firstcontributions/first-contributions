[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeras Contribuciones

Es complicado. Resulta difícil la primera vez que haces algo, especialmente cuando colaboras con otros, pues cometer errores no es nada agradable. Nuestro objetivo es simplificar la forma en la que los nuevos contribuidores de _codigo abierto_ aprenden y contribuyen por primera vez.

Leer artículos y ver tutoriales puede ayudar, pero, ¿Qué mejor que hacer las cosas en un entorno de prácticas? Este proyecto se enfoca en ser una guía y en simplificar la forma en la que los principiantes hacen su primera contribución. Si quieres hacer tu primera contribución, sigue los pasos que se muestran a continuación.

#### _Si no estás familiarizado con la línea de comandos, [aquí hay tutoriales usando herramientas con Interfaz Gráfica (GUI)](#Tutoriales-con-otras-herramientas)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork de este repositorio" />

Si no tienes git en tu equipo, puedes encontrar instrucciones para instalarlo en [este enlace](https://docs.github.com/es/get-started/quickstart/set-up-git).

## Bifurca (_Fork_) este repositorio

Haz un _fork_ de este repositorio haciendo click en el botón "_Fork_" en la parte superior derecha en esta página.
Esto creará una copia de este repositorio en tu cuenta.

## Clona (_Clone_) el repositorio bifurcado

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositorio" />

Ahora clona este repositorio en tu equipo. Dirígete a tu cuenta de GitHub, haz click en el botón "_clone or download_" y luego haz click en el icono para _copiar al portapapeles_.

Abre tu consola o terminal y ejecuta el siguiente comando de git:

```
git clone "url que acabas de copiar"
```

Donde pone "url que acabas de copiar" (sin las comillas dobles) es la _url_ a este repositorio (tu _fork_ a este proyecto). Mira los pasos previos para obtener la _url_.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

Por ejemplo:

```
git clone https://github.com/este-eres-tu/first-contributions.git
```

La parte de `este-eres-tu` la reemplazarás con tu usuario de GitHub. Aquí estás copiando los contenidos del repositorio _first-contributions_ en GitHub a tu equipo.

## Crea una rama (_Branch_)

Cambia al directorio del repositorio en tu equipo (si es que no estás ahí ya).

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

(El nombre de la rama no tiene por qué contener la palabra _add_, pero es razonable que lo tenga porque el objetivo de esta rama es añadir tu nombre a la lista.)

## Haz los cambios necesarios y confirma (_Commit_) esos cambios

Abre el archivo `Contributors.md` en un editor de texto y añade tu nombre. No lo añadas ni al principio ni al final del archivo, hazlo en cualquier otro sitio. Guarda el archivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Si vas al directorio del proyecto y ejecutas el comando `git status`, verás que hay cambios.

Agrega esos cambios a la rama (_branch_) que creaste anteriormente usando el comando `git add`:

```
git add Contributors.md
```

Ahora haz un _commit_ sobre estos cambios ejecutando el comando `git commit`:

```
git commit -m "Add <tu-nombre> to Contributors list"
```

cambiando `<tu-nombre>` con tu nombre.

## Sube (_Push_) tus cambios a GitHub

Haz _push_ de tus cambios usando el comando `git push`:

```
git push origin <añade-el-nombre-de-la-rama>
```

Reemplaza `<añade-el-nombre-de-la-rama>` con el nombre de la rama que creaste anteriormente.

## Envía (_Submit_) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz click sobre este botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crea una pull request" />

Ahora envía la _pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="enviar la pull request" />

Pronto estaré fusionando tus cambios (haciendo _merge_) con la rama master de este proyecto. Recibirás una notificación por correo electrónico cuando los cambios hayan sido fusionados.

## ¿Cuáles son los siguientes pasos?

¡Enhorabuena! ¡Has completado el flujo de trabajo _*fork -> clone -> edit -> PR*_ que encontrarás habitualmente como contribuidor!

Celebra tu contribución y compártela con tus amigos y seguidores yendo a [web app](https://firstcontributions.github.io/#social-share)).

También podrías unirte a nuestro _equipo_ de Slack en caso de que necesites ayuda o tengas alguna pregunta. [Únete a nuestro Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Ahora empieza a contribuir a otros proyectos. Hemos reunido una lista de proyectos con _issues_ sencillas para que puedas empezar. Échale un ojo a la [lista de proyectos en la aplicación web](https://firstcontributions.github.io/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriales con otras herramientas

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
