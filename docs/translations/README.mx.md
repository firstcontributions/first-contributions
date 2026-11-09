[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primeras contribuciones

Siempre resulta difícil la primera vez que haces algo. Principalmente cuando colaboras con otros, ya que cometer errores no es agradable. Es por ello que, queremos hacer más sencilla la forma en la que los nuevos contribuyentes de _open source_ aprenden y contribuyen por primera vez.

Leer artículos y ver tutoriales puede ayudar, pero ¿qué mejor que hacer las cosas en un ambiente de prácticas? Este proyecto se enfoca en guiar y en simplificar la forma en la que los principiantes hacen su primera contribución. Si buscas hacer tu primera contribución, sigue los pasos que se muestran a continuación.  

#### *Si no estás cómodo con la línea de comandos, [aquí hay unos tutoriales usando herramientas gráficas.](#tutoriales-con-otras-herramientas)*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Imagen de la interfaz de Github con el botón de Fork del repositorio encerrado en un rectángulo rojo" />

Si no tienes Git en tu equipo, [instálalo siguiendo estas instrucciones](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Dale Fork al repositorio

Dale "fork" a este repositorio dando clic en el botón "*Fork*" en la parte superior derecha de la página.
Esto creará una copia de este repositorio en tu cuenta.

## Clona (*Clone*) el repositorio

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Imagen de la interfaz del repositorio con el botón verde de Code encerrado en un rectángulo rojo" />

Ahora clona tu *fork* en tu equipo. Ve a tu cuenta de GitHub, abre tu *fork* del repositorio, da clic en el botón "*Code*", luego en la pestaña *SSH* y después en el ícono para *copiar* la url al portapapeles.

Abre tu consola o terminal y ejecuta el siguiente comando:

```
git clone "la url del repositorio que copiaste"
```

Donde "la url del repositorio que copiaste" (sin las comillas dobles) es la *url* a este repositorio (tu *fork* a este proyecto). Mira los pasos previos para obtener la *url*.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="Sección de GitHub para copiar repositorio, con la pestaña de SSH mostrándose y al lado un icono para copiar el URL al portapapeles" />

Por ejemplo:
```
git clone git@github.com:usuarioGitHub/first-contributions.git
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
(El nombre de la rama no tiene por qué contener la palabra *add*, pero es razonable que lo tenga porque el objetivo de esta rama es añadir tu nombre a la lista.)

## Haz los cambios necesarios y guarda (*Commit*) esos cambios

Abre el archivo `Contributors.md` en un editor de texto y añade tu nombre. No lo añadas ni al principio ni al final del archivo, hazlo en cualquier otro sitio. Guarda el archivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="Terminal mostrando el estado del repositorio después de un git status, mostrando que se realizaron cambios en Contributors.md" />

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

Manda tus cambios con un *push* usando el comando `git push`:
```
git push -u origin <nombre-rama>
```
Reemplaza `<nombre-rama>` con el nombre de la rama que creaste anteriormente.

<details>
<summary> <strong>Si aparece algún error al hacer push, da clic aquí:</strong> </summary>

- ### Error de autenticación
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  Consulta el [tutorial de GitHub](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) para generar una llave SSH y configurarla en tu cuenta.

  También te conviene ejecutar `git remote -v` para revisar tu dirección remota.

  Si se ve parecida a esto:
  <pre>origin	https://github.com/tu-usuario/tu_repo.git (fetch)
  origin	https://github.com/tu-usuario/tu_repo.git (push)</pre>

  cámbiala con este comando:
  ```bash
  git remote set-url origin git@github.com:tu-usuario/tu_repo.git
  ```
  De lo contrario, se te seguirá pidiendo usuario y contraseña, y obtendrás un error de autenticación.
</details>

## Envía (*Submit*) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz clic sobre este botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Imagen de la interfaz de Github con el mensaje `Compare & pull request` resaltado en un botón verde para crear una pull request" />

Ahora envía el *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Interfaz de pull request donde se comparan las ramas del fork con un mensaje verde que indica que se pueden fusionar automáticamente. Con el título de pull request y una sección para comentarios" />

Pronto estaré combinando tus cambios (haciendo *merge*) con la rama main de este proyecto. Recibirás una notificación por correo electrónico cuando los cambios hayan sido combinados.

## ¿Cuáles son los siguientes pasos?

¡Felicidades! ¡Has completado la línea de trabajo *_fork -> clone -> edit -> PR_* que encontrarás habitualmente como contribuidor!

Festeja tu contribución y compártela con tus amigos y seguidores yendo a [web app](https://firstcontributions.github.io/#social-share).

Si deseas más práctica, consulta [contribuciones de código](https://github.com/roshanjossey/code-contributions).

Ahora empieza a contribuir a otros proyectos. Hemos reunido una lista de proyectos con *issues* sencillas para que puedas empezar. Échale un ojo a la [lista de proyectos en la web app](https://firstcontributions.github.io/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriales con otras herramientas

|<a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|<a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a>|<a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|<a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a>|
|---|---|---|---|---|---|
|[GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)|[Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)|[GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)|[Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)| [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)|[IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)|
