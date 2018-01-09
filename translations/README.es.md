[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

# Primeras Contribuciones

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

Abre tu consola o terminal y ejecuta el siguiente comando de git:

```
git clone "url que copiaste"
```
Donde "url que copiaste" (sin las comillas) es la url a este repositorio. Mire los pasos previos para obtener la url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copiar URL a clipboard" />

Por ejemplo:
```
git clone https://github.com/éste-eres-tu/first-contributions.git
```
Donde "éste-eres-tu" es tu usuario de GitHub. Aquí estás copiando los contenidos del repositorio first-contributions en GitHub a tu computador

## Crear una rama(*Branch*)

Cambia al directorio del repositorio en tu computador si es que no estás ahí.

```
cd first-contributions
```

Ahora crea una branch usando `git checkout command`

```
git checkout -b <añade tu nombre>
```

Por ejemplo
```
git checkout -b add-alonzo-church
```

## Hacer los cambios necesarios y confirmar(*Commit*) esos cambios

Ahora abre el archivo `Contributors.md` en un editor de texto y añade tu nombre, luego guarda el archivo. Si vas al directorio del proyecto y haces `git status`, verás que hay cambios. Agrega esos cambios usando el comando `git add` que está abajo.
```
git add Contributors.md
```

Ahora puedes hacer commit sobre los cambios con el comando `git commit`
```
git commit -m "Add <tu-nombre> to Contributors list"
```
cambia `<tu-nombre>` con tu nombre

## Manda(*Push*) tus cambios a GitHub

Haz *push* de tus cambios usando el comando `git push`
```
git push origin <añade-tu-nombre>
```
Cambia `<añade-tu-nombre>` con el nombre de la branch que creaste antes

## Enviar(*Submit*) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz click sobre este botón.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="crea una pull request" />

Ahora crea la pull request

<img style="float: right;" src="../assets/submit-pull.png" alt="sube la pull request" />

Ahora yo estaré fusionando tus cambios (haciendo *merge*) en la master branch de este proyecto. Recibirás una notificación por correo cuando los cambios hayan sido fusionados.

La master branch de tu fork no tendrá esos cambios. Para mantener tu fork sincronizado con el mío, sigue los siguientes pasos.

### Manteniendo tu fork sincronizado con este repositorio

Primero, cambia a la master branch
```
git checkout master
```

Luego, agrega la url de mi repo como `upstream remote url`
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Esta es una forma de decirle a git que otra versión de este proyecto existe en la url especificada y que la llamaremos upstream. Una vez que los cambios sean agregados (cuando hice *merge*), recupera la nueva versión de mi repositorio.
```
git fetch upstream
```

Aquí estamos trayendo todos los cambios en mi fork (upstream remote). Ahora, necesitas agregar la nueva revisión de mi repositorio en tu master branch (harás *merge*)
```
git rebase upstream/master
```
Aquí estarás aplicando todos los cambios que recuperaste a la master branch. Si haces push de la master branch ahora, tu fork también tendrá los cambios
```
git push origin master
```
Notarás aquí que estás empujando(push) a la url remota llamada origin.

## Tutoriales con otras herramientas


|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## A dónde ir desde aquí?

También podrías unirte a nuestro *equipo* Slack en caso de que necesites alguna ayuda o tengas alguna pregunta. [Únete a nuestro Slack](https://firstcontributions.herokuapp.com)

Aquí hay algunas *issues* para principiantes en repositorios populares que podrías resolver. Anímate y ve a esos repos para aprender más

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
