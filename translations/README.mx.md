[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primera contribuciones

Es complicado. Siempre resulta difícil la primera vez que haces algo. Principalmente cuando colaboras con otros, pues cometer errores no es agradable. Queremos simplificar la forma en la que los nuevos contribuidores de _open source_ aprenden y contribuyen por primera vez.

Leer artículos y ver tutoriales puede ayudar, pero ¿Qué mejor que hacer las cosas en un ambiente de prácticas?. Este proyecto se enfoca en guíar y en simplificar la forma en la que los principiantes hacen su primera contribución. Si buscas hacer tu primera contribución, sigue los pasos que se muestran a continuación.  

#### *Si no estás cómodo con la linea de comandos, [aqui hay unos tutoriales usando herramientas gráficas.]( #tutorials-using-other-tools )*

<<<<<<< HEAD
#### *Puedes leer esto [en otros lenguajes](translations/Translations.md).*

[🇮🇳](translations/README.hi.md)
[🇲🇲](translations/README.mm_unicode.md)
[🇮🇩](translations/README.id.md)
[🇫🇷](translations/README.fr.md)
[🇪🇸](translations/README.es.md)
[🇳🇱](translations/README.nl.md)
[🇱🇹](translations/README.lt.md)
[🇷🇺](translations/README.ru.md)
[🇯🇵](translations/README.ja.md)
[🇻🇳](translations/README.vn.md)
[🇵🇱](translations/README.pl.md)
[🇮🇷](translations/README.fa.md)
[🇮🇷](translations/README.fa.en.md)
[🇰🇷 🇰🇵](translations/README.ko.md)
[🇩🇪](translations/README.de.md)
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
[🏴󠁥󠁳󠁧󠁡󠁿](translations/README.gl.md)
[🇵🇰](translations/README.ur.md)
[:bangladesh:](translations/README.bn.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇹🇷](translations/README.tr.md)
[🇸🇪](translations/README.se.md)
[:slovenia:](translations/README.sl.md)
[🇮🇱](translations/README.hb.md)
[🇷🇸](translations/README.sr.md)


=======
>>>>>>> 612d3e442d0fc58798730e2b8c6e3623eabc13d9

<img align="right" width="300" src="../assets/fork.png" alt="fork de este repositorio" />

Si no tienes git en tu equipo, aquí las instrucciones para instalarlo en el [enlace]( https://help.github.com/articles/set-up-git/ )

## Dale Fork al repositorio

<<<<<<< HEAD
Fork this repo by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

=======
>>>>>>> 612d3e442d0fc58798730e2b8c6e3623eabc13d9
Dale "fork" a este repositorio dando click en el botón "*Fork*" en la parte superior derecha de la página.
Esto creará una copia de este repositorio en tu cuenta.

## Clona "Clone" el repositorio

<img align="right" width="300" src="../assets/clone.png" alt="clonar este repositorio" />

Ahora clona este repositorio en tu equipo. ve a tu cuenta de Github, y da click en el botón "*clone or download*" y luego da click en el ícono para *copiar*.

Abre tu consola o terminal y ejecuta el siguiente comando:

```
git clone "la url del repositorio que copiaste"
```

Donde "url que acabas de copiar" (sin las comillas dobles) es la *url* a este repositorio (tu *fork* a este proyecto). Mira los pasos previos para obtener la *url*.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

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

Ahora crea una rama (*branch*) usando el comando  `git checkout`:
```
git checkout -b <añade tu nombre>
```

Por ejemplo:
```
git checkout -b add-juan-perez
```
(El nombre de la rama no tiene por qué contener la palabra *add*, pero es razonable que lo tenga porque el objetivo de esta rama es añadir tu nombre a la lista.)

## Haz los cambios necesarios y salva (*Commit*) esos cambios

Abre el archivo `Contributors.md` en un editor de texto y añade tu nombre. No lo añadas ni al principio ni al final del archivo, hazlo en cualquier otro sitio. Guarda el archivo.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Si vas al directorio del proyecto y ejecutas el comando  `git status`,podrás ver los cambios ya reflejados.

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

mandar un *push* de tus cambios usando el comando `git push`:
```
git push origin <nombre-rama>
```
Reemplaza `<nombre-rama>` con el nombre de la rama que creaste anteriormente.

## Envía (*Submit*) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz click sobre este botón.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="crea una pull request" />

Ahora envía el *pull request*.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="enviar la pull request" />

Pronto estaré combinando tus cambios (haciendo *merge*) con la rama master de este proyecto. Recibirás una notificación por correo electrónico cuando los cambios hayan sido combinados.

## ¿Cuáles son los siguientes pasos?

¡Felicidades! ¡Has completado la linea de trabajo *_fork -> clone -> edit -> PR_* que encontrarás habitualmente como contribuidor!

Festeja tu contribución y compártela con tus amigos y seguidores yendo a [web app](https://roshanjossey.github.io/first-contributions/#social-share).

También podrías unirte a nuestro *equipo* de Slack en caso de que necesites ayuda o tengas alguna pregunta. [Únete a nuestro Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Ahora empieza a contribuir a otros proyectos. Hemos reunido una lista de proyectos con *issues* sencillas para que puedas empezar. Échale un ojo a la [lista de proyectos en la web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriales con otras herramientas

<<<<<<< HEAD
|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|
=======
|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|
>>>>>>> 612d3e442d0fc58798730e2b8c6e3623eabc13d9
