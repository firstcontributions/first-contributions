[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primera Contribución

Es dificil. Siempre es difícil la primera vez que haces algo. Especialmente cuando estás colaborando, cometer errores no es algo cómodo. Queríamos simplificar la forma en que los nuevos colaboradores de código abierto aprenden y contribuyen por primera vez.

Leer artículos y ver tutoriales puede ayudar, pero ¿qué mejor que hacer las cosas en un entorno de práctica? Este proyecto tiene como objetivo proporcionar orientación y simplificar la forma en que los principiantes hacen su primera contribución. Si está buscando hacer su primera contribución, siga los pasos a continuación.

#### *Si no se siente cómodo con la línea de comandos, [aquí hay tutoriales que usan herramientas GUI.]( #tutorials-using-other-tools )*

#### *Lee esto en [otros idiomas](translations/Translations.md).*

[🇮🇳](translations/README.hi.md)
[🇲🇲](translations/README.mm_unicode.md)
[🇮🇩](translations/README.id.md)
[🇫🇷](translations/README.fr.md)
[🇪🇸](translations/README.es.md)
[<img src="assets/catalan1.png" width="22">](translations/README.ca.md)
[🇳🇱](translations/README.nl.md)
[🇱🇹](translations/README.lt.md)
[🇷🇺](translations/README.ru.md)
[:slovakia:](translations/README.slk.md)
[🇯🇵](translations/README.ja.md)
[🇻🇳](translations/README.vn.md)
[🇵🇱](translations/README.pl.md)
[🇮🇷](translations/README.fa.md)
[🇮🇷](translations/README.fa.en.md)
[🇰🇷 🇰🇵](translations/README.ko.md)
[🇩🇪](translations/README.de.md)
[🇩🇰](translations/README.da.md)
[🇨🇳](translations/README.chs.md)
[🇹🇼](translations/README.cht.md)
[🇬🇷](translations/README.gr.md)
[🇪🇬](translations/README.eg.md)
[🇸🇦](translations/README.ar.md)
[🇺🇦](translations/README.ua.md)
[🇧🇷](translations/README.pt_br.md)
[🇵🇹](translations/README.pt-pt.md)
[🇮🇹](translations/README.it.md)
[🇹🇭](translations/README.th.md)
[🏴](translations/README.gl.md)
[🇵🇰](translations/README.ur.md)
[:bangladesh:](translations/README.bn.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇹🇷](translations/README.tr.md)
[🇸🇪](translations/README.se.md)
[:slovenia:](translations/README.sl.md)
[🇮🇱](translations/README.hb.md)
[🇨🇿](translations/README.cs.md)
[<img src="assets/pirate.png" width="22">](translations/README.en-pirate.md)
[🇲🇽](translations/README.mx.md)
[🇨🇴](translations/README.co.md)



<img align="right" width="300" src="assets/fork.png" alt="Bifurca (*Fork*) este repositorio" />

Si no tienes git en tu computadora, [puede instalarlo]( https://help.github.com/articles/set-up-git/).

## Bifurca (*Fork*) este repositorio

Haz un fork de este repositorio haciendo click en el botón "Fork" en la parte superior derecha en esta página.
Esto creará una copia de este repositorio en tu cuenta. account.

## Clona (*Clone*) este repositorio

<img align="right" width="300" src="assets/clone.png" alt="Clona (*Clone*) este repositorio" />

Ahora clona este repositorio en tu equipo. Dirígete a tu cuenta de GitHub, haz click en el botón *"clone or download"* y luego haz click en el icono para *copiar al portapapeles*.

Abre tu consola o terminal y ejecuta el siguiente comando de git:

```
git clone "url que acabas de copiar"
```
Donde "url que acabas de copiar" (sin las comillas dobles) es la url a este repositorio (tu fork a este proyecto). Mira los pasos previos para obtener la url.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="Copiar la url al portapapeles" />

Por ejemplo:
```
git clone https://github.com/tu-usuario/first-contributions.git
```
Donde `tu-usuario` es tu usuario de GitHub. Aquí estás copiando los contenidos del repositorio first-contributions en GitHub a tu equipo.

## Crear una rama (*Branch*)

Cambia al directorio del repositorio en tu equipo (si es que no estás ahí ya):

```
cd first-contributions
```
Ahora crea una rama (*branch*) usando el comando `git checkout`:
```
git checkout -b <añade el nombre de tu nueva rama>
```

Por ejemplo:
```
git checkout -b nueva-rama
```
(El nombre de la rama no tiene por qué contener la palabra *add*, pero es razonable que lo tenga porque el objetivo de esta rama es añadir tu nombre a la lista.)

## Haz los cambios necesarios y confirma (*Commit*) esos cambios

Abre el archivo `Contributors.md` en un editor de texto y añade tu nombre. No lo añadas ni al principio ni al final del archivo, hazlo en cualquier otro sitio. Guarda el archivo.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />


Si vas al directorio del proyecto y ejecutas el comando `git status`, verás que hay cambios.

Agrega esos cambios a la rama (*branch*) que creaste anteriormente usando el comando `git add`:

```
git add Contributors.md
```

Ahora confirma tus cambios haciendo un *commit* sobre estos cambios ejecutando el comando `git commit`:
```
git commit -m "Add <tu-nombre> to Contributors list"
```
Cambiando `<tu nombre>` con tu nombre.

## Manda (*Push*) tus cambios a GitHub

Manda tus cambios (*push*) de tus cambios usando el comando `git push`:
```
git push origin <añade-el-nombre-de-tu-rama>
```
Reemplaza `<añade-el-nombre-de-tu-rama>` con el nombre de la rama que creaste anteriormente.

## Envía (*Submit*) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz click sobre este botón.

<img style="float: right;" src="assets/compare-and-pull.png" alt="Crear a pull request" />

Ahora envía el *pull request*.

<img style="float: right;" src="assets/submit-pull-request.png" alt="Envía el pull request" />

Pronto estaré mezclando tus cambios (haciendo *merge*) con la rama master de este proyecto. Recibirás una notificación por correo electrónico cuando los cambios hayan sido mezclados.

## ¿Cuáles son los siguientes pasos?

¡Felicidades! ¡Has completado el flujo de trabajo fork -> clone -> edit -> PR que encontrarás habitualmente como contribuidor!

Celebra tu contribución y compártela con tus amigos y seguidores yendo a [web app](https://roshanjossey.github.io/first-contributions/#social-share).

También podrías unirte a nuestro equipo de Slack en caso de que necesites ayuda o tengas alguna pregunta. [Únete a nuestro Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Ahora empieza a contribuir a otros proyectos. Hemos reunido una lista de proyectos con issues sencillas para que puedas empezar. Échale un ojo a la [lista de proyectos en el web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Material adicional](additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriales con otras herramientas

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Self-Promotion

ISi te gustó este proyecto, márcalo como favorito con una estrella en [GitHub](https://github.com/Roshanjossey/first-contributions).
. Si te sientes agradecido, sigue a [Roshan](https://roshanjossey.github.io/) en
[Twitter](https://twitter.com/sudo__bangbang) y
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
