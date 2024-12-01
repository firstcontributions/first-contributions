[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primeras contribuciones

Siempre resulta difícil la primera vez que haces algo. Principalmente cuando colaboras con otros, ya que cometer errores no es agradable. Es por ello que, queremos hacer más sencilla la forma en la que los nuevos contribuyentes de _open source_ aprenden y contribuyen por primera vez.

Leer artículos y ver tutoriales puede ayudar, pero ¿qué mejor que hacer las cosas en un ambiente de prácticas? Este proyecto se enfoca en guiar y en simplificar la forma en la que los principiantes hacen su primera contribución. Si buscas hacer tu primera contribución, sigue los pasos que se muestran a continuación.  

#### *Si no estás cómodo con la línea de comandos, [aquí hay unos tutoriales usando herramientas gráficas.](#Tutoriales-con-otras-herramientas)*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork de este repositorio" />

Si no tienes Git en tu equipo, aquí las instrucciones para instalarlo en el [enlace]( https://help.github.com/articles/set-up-git/ )

## Dale Fork al repositorio

Dale "fork" a este repositorio dando clic en el botón "*Fork*" en la parte superior derecha de la página.
Esto creará una copia de este repositorio en tu cuenta.

## Clona "Clone" el repositorio

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositorio" />

Ahora clona este repositorio en tu equipo. Ve a tu cuenta de Github, y da clic en el botón "*clone or download*" y luego da clic en el ícono para *copiar*.

Abre tu consola o terminal y ejecuta el siguiente comando:

```
git clone "la url del repositorio que copiaste"
```

Donde "la url del repositorio que copiaste" (sin las comillas dobles) es la *url* a este repositorio (tu *fork* a este proyecto). Mira los pasos previos para obtener la *url*.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

Por ejemplo:
```
git clone https://github.com/usuarioGitHub/first-contributions.git
```
Donde `usuarioGitHub` es tu usuario de GitHub. Aquí estás copiando los contenidos del repositorio *first-contributions* en GitHub a tu equipo.

## Crea una rama (*Branch*)

Cambia al directorio del repositorio en tu equipo (si es que no estás ahí ya).

```
cd first-contributions
```

Ahora crea una rama (*branch*) usando el comando  `git switch`:
```
git switch -c <añade tu nombre>
```

Por ejemplo:
```
git switch -c add-juan-perez
```
(El nombre de la rama no tiene porqué contener la palabra *add*, pero es razonable que lo tenga porque el objetivo de esta rama es añadir tu nombre a la lista.)

## Haz los cambios necesarios y guarda (*Commit*) esos cambios

Abre el archivo `Contributors.md` en un editor de texto y añade tu nombre. No lo añadas ni al principio ni al final del archivo, hazlo en cualquier otro sitio. Guarda el archivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Si vas al directorio del proyecto y ejecutas el comando `git status`, podrás ver los cambios ya reflejados.

Agrega esos cambios a la rama (*branch*) que creaste antes usando el comando `git add`:

```
git add Contributors.md
```

Ahora puedes hacer un *commit* sobre estos cambios ejecutando el comando `git commit`:
```
git commit -m "Add <nombre> to Contributors list"
```
reemplazando `<nombre>` con tu nombre.


## Carga (*Push*) tus cambios a GitHub

Mandar un *push* de tus cambios usando el comando `git push`:
```
git push origin <nombre-rama>
```
Reemplaza `<nombre-rama>` con el nombre de la rama que creaste anteriormente.

## Envía (*Submit*) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz clic sobre este botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crea una pull request" />

Ahora envía el *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="enviar la pull request" />

Pronto estaré combinando tus cambios (haciendo *merge*) con la rama master de este proyecto. Recibirás una notificación por correo electrónico cuando los cambios hayan sido combinados.

## ¿Cuáles son los siguientes pasos?

¡Felicidades! ¡Has completado la línea de trabajo *_fork -> clone -> edit -> PR_* que encontrarás habitualmente como contribuidor!

Festeja tu contribución y compártela con tus amigos y seguidores yendo a [web app](https://firstcontributions.github.io/#social-share).

También podrías unirte a nuestro *equipo* de Slack en caso de que necesites ayuda o tengas alguna pregunta. [Únete a nuestro Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Ahora empieza a contribuir a otros proyectos. Hemos reunido una lista de proyectos con *issues* sencillas para que puedas empezar. Échale un ojo a la [lista de proyectos en la web app](https://firstcontributions.github.io/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriales con otras herramientas

|<a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|<a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a>|<a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|<a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a>|
|---|---|---|---|---|---|
|[GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)|[Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)|[GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)|[Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)| [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)|[IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)|
