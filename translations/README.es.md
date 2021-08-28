<<<<<<< HEAD
﻿[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
=======
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
>>>>>>> upstream/master
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeras Contribuciones

<<<<<<< HEAD
Es difícil. Siempre resulta difícil cuando se comienza a hacer algo por primera vez. 
Principalmente cuando colaboras con otros, pues cometer errores no es nada agradable.
Sin embargo el código abierto tiene que ver con la colaboración y el trabajo conjunto. 
Nuestro objetivo es simplificar la forma en la que los nuevos contribuidores del 
"open source" aprenden y contribuyen por primera vez.

Leer artículos y ver tutoriales puede ayudar, pero qué mejor es hacer las cosas
sin romper nada. Este proyecto se enfoca en ser una guía y en simplificar la 
forma en la que los novatos hacen su primera contribución. Recuerda: mientras 
más relajado estés, aprenderás mejor. Si quieres hacer tu primera contribución 
sólo sigue los sencillos pasos que se muestran a continuación. 
Te lo prometemos, será divertido. 

<img align="right" width="300" src="../assets/fork.png" alt="fork de éste repositorio" />

Si no tienes git en tu máquina, [ instálalo ]( https://help.github.com/articles/set-up-git/ )

## Bifurca(*Fork*) este repositorio

Haz *fork* de este repo haciendo click en el botón "Fork" que está arriba de esta página.
Esto creará una copia de este repositorio en tu cuenta.

## Clona(*Clone*) el repositorio

<img align="right" width="300" src="../assets/clone.png" alt="clonar este repositorio" />

Ahora clona este repo en tu equipo. Haz click en el botón "*Clone*" y luego haz click en el ícono para copiar al portapapeles(clipboard)
=======
Es complicado. Resulta difícil la primera vez que haces algo, especialmente cuando colaboras con otros, pues cometer errores no es nada agradable. Nuestro objetivo es simplificar la forma en la que los nuevos contribuidores de _codigo abierto_ aprenden y contribuyen por primera vez.

Leer artículos y ver tutoriales puede ayudar, pero, ¿Qué mejor que hacer las cosas en un entorno de prácticas? Este proyecto se enfoca en ser una guía y en simplificar la forma en la que los principiantes hacen su primera contribución. Si quieres hacer tu primera contribución, sigue los pasos que se muestran a continuación.

#### *Si no estás familiarizado con la línea de comandos, [aquí hay tutoriales usando herramientas con Interfaz Gráfica (GUI)]( #tutoriales-con-otras-herramientas )*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork de este repositorio" />

Si no tienes git en tu equipo, puedes encontrar instrucciones para instalarlo en [este enlace]( https://help.github.com/articles/set-up-git/ ).

## Bifurca (*Fork*) este repositorio

Haz un *fork* de este repositorio haciendo click en el botón "*Fork*" en la parte superior derecha en esta página.
Esto creará una copia de este repositorio en tu cuenta.

## Clona (*Clone*) el repositorio

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositorio" />

Ahora clona este repositorio en tu equipo. Dirígete a tu cuenta de GitHub, haz click en el botón "*clone or download*" y luego haz click en el icono para *copiar al portapapeles*.
>>>>>>> upstream/master

Abre tu consola o terminal y ejecuta el siguiente comando de git:

```
<<<<<<< HEAD
git clone "url que copiaste"
```
Donde "url que copiaste" (sin las comillas) es la url a este repositorio. Mire los pasos previos para obtener la url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copiar URL a clipboard" />

Por ejemplo:
```
git clone https://github.com/éste-eres-tu/first-contributions.git
```
Donde "éste-eres-tu" es tu usuario de GitHub. Aquí estás copiando los contenidos del repositorio first-contributions en GitHub a tu computador

## Crea una rama (*Branch*)

Cambia al directorio del repositorio en tu computador si es que no estás ahí.
=======
git clone "url que acabas de copiar"
```

Donde pone "url que acabas de copiar" (sin las comillas dobles) es la *url* a este repositorio (tu *fork* a este proyecto). Mira los pasos previos para obtener la *url*.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

Por ejemplo:
```
git clone https://github.com/este-eres-tu/first-contributions.git
```
La parte de `este-eres-tu` la reemplazarás con tu usuario de GitHub. Aquí estás copiando los contenidos del repositorio *first-contributions* en GitHub a tu equipo.

## Crea una rama (*Branch*)

Cambia al directorio del repositorio en tu equipo (si es que no estás ahí ya).
>>>>>>> upstream/master

```
cd first-contributions
```

<<<<<<< HEAD
Ahora crea una branch usando `git checkout command`

=======
Ahora crea una rama (*branch*) usando el comando  `git checkout`:
>>>>>>> upstream/master
```
git checkout -b <añade tu nombre>
```

<<<<<<< HEAD
Por ejemplo
```
git checkout -b add-alonzo-church
```

## Haz los cambios necesarios y confirma (*Commit*) esos cambios

Ahora abre el archivo `Contributors.md` en un editor de texto y añade tu nombre, luego guarda el archivo. Si vas al directorio del proyecto y haces `git status`, verás que hay cambios. Agrega esos cambios usando el comando `git add` que está abajo.
=======
Por ejemplo:
```
git checkout -b add-alonzo-church
```
(El nombre de la rama no tiene por qué contener la palabra *add*, pero es razonable que lo tenga porque el objetivo de esta rama es añadir tu nombre a la lista.)

## Haz los cambios necesarios y confirma (*Commit*) esos cambios

Abre el archivo `Contributors.md` en un editor de texto y añade tu nombre. No lo añadas ni al principio ni al final del archivo, hazlo en cualquier otro sitio. Guarda el archivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Si vas al directorio del proyecto y ejecutas el comando  `git status`, verás que hay cambios.

Agrega esos cambios a la rama (*branch*) que creaste anteriormente usando el comando `git add`:

>>>>>>> upstream/master
```
git add Contributors.md
```

<<<<<<< HEAD
Ahora puedes hacer commit sobre los cambios con el comando `git commit`
```
git commit -m "Add <tu-nombre> to Contributors list"
```
cambia `<tu-nombre>` con tu nombre

## Manda (*Push*) tus cambios a GitHub

Haz *push* de tus cambios usando el comando `git push`
```
git push origin <añade-tu-nombre>
```
Cambia `<añade-tu-nombre>` con el nombre de la branch que creaste antes
=======
Ahora haz un *commit* sobre estos cambios ejecutando el comando `git commit`:
```
git commit -m "Add <tu-nombre> to Contributors list"
```
cambiando `<tu-nombre>` con tu nombre.

## Manda (*Push*) tus cambios a GitHub

Haz *push* de tus cambios usando el comando `git push`:
```
git push origin <añade-el-nombre-de-la-rama>
```
Reemplaza `<añade-el-nombre-de-la-rama>` con el nombre de la rama que creaste anteriormente.
>>>>>>> upstream/master

## Envía (*Submit*) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz click sobre este botón.

<<<<<<< HEAD
<img style="float: right;" src="../assets/compare-and-pull.png" alt="crea una pull request" />

Ahora crea la pull request

<img style="float: right;" src="../assets/submit-pull.png" alt="sube la pull request" />

Ahora yo estaré fusionando tus cambios (haciendo *merge*) en la master branch de este proyecto. Recibirás una notificación por correo cuando los cambios hayan sido fusionados.


## ¿A dónde ir desde aquí?

Celebra tu contribución y compártela con tus amigos y seguidores yendo a [web app](https://roshanjossey.github.io/first-contributions/#social-share).

También podrías unirte a nuestro *equipo* Slack en caso de que necesites alguna ayuda o tengas alguna pregunta. [Únete a nuestro Slack](https://firstcontributions.herokuapp.com)

Ahora empieza a contribuir a otros proyectos. Hemos reunido una lista de proyectos con *issues* para que puedas empezar. Compruébalas en [lista de proyectos en la web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [ Material adicional ](../additional-material/git_workflow_senarios/additional-material.md)
=======
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crea una pull request" />

Ahora envía la *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="enviar la pull request" />

Pronto estaré fusionando tus cambios (haciendo *merge*) con la rama master de este proyecto. Recibirás una notificación por correo electrónico cuando los cambios hayan sido fusionados.

## ¿Cuáles son los siguientes pasos?

¡Enhorabuena! ¡Has completado el flujo de trabajo *_fork -> clone -> edit -> PR_* que encontrarás habitualmente como contribuidor!

Celebra tu contribución y compártela con tus amigos y seguidores yendo a [web app](https://roshanjossey.github.io/first-contributions/#social-share).

También podrías unirte a nuestro *equipo* de Slack en caso de que necesites ayuda o tengas alguna pregunta. [Únete a nuestro Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Ahora empieza a contribuir a otros proyectos. Hemos reunido una lista de proyectos con *issues* sencillas para que puedas empezar. Échale un ojo a la [lista de proyectos en la aplicación web](https://firstcontributions.github.io/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)
>>>>>>> upstream/master


## Tutoriales con otras herramientas

<<<<<<< HEAD
|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|


## Auto promoción

Si te gustó este proyecto, marcalo como favorito con una estrella en [GitHub](https://github.com/Roshanjossey/first-contributions).
Si te sientes muy agradecido, sigue a [Roshan](https://roshanjossey.github.io/) en
[Twitter](https://twitter.com/sudo__bangbang) y
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
=======
| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
>>>>>>> upstream/master
