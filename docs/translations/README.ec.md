[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Primeras Contribuciones

Este proyecto tiene como objetivo simplificar y guiar la forma en que los principiantes hacen su primera contribución. Si está buscando hacer su primera contribución, siga los pasos a continuación.


#### *Si no estás familiarizado con la línea de comandos, [aquí hay tutoriales usando herramientas con Interfaz Gráfica (GUI)](#tutoriales-usando-otras-herramientas)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork de este repositorio" />

En caso de no tener instalado Git en tu equipo, te dejo una [guia]( https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git) para instalarlo.

## Has un "Fork" de este repositorio

Presiona el boton "fork" de este repositorio en la parte superior derecha de la página. Al hacer esto, se crea una copia de este repositorio en tu cuenta de GitHub.

## Has un "Clone" del repositorio copiado

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositorio" />

Ahora clona el repositorio al que le hiciste un fork previamente, el URL del repositorio deberia estar asi `https://github.com/<tu-usuario>/first-contributions`. Entra en tu cuenta de Github, y has click en el botón `Code` y luego en la pestaña SSH y luego haz clic en el icono de _copiar al portapapeles_.

Abre tu terminal y ejecuta el siguiente comando git:

```
git clone "la url del repositorio que copiaste"
```

Donde "la url del repositorio que copiaste" (sin las comillas dobles) es la *url* a este repositorio (tu *fork* a este proyecto), se veria algo asi `https://github.com/<tu-usuario>/first-contributions.git` .

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

Por ejemplo:
```
git clone https://github.com/<tu-usuario>/first-contributions.git
```
Donde `<tu-usuario>` es tu nombre de usuario de GitHub. Con este comando estas copiando los contenidos del repositorio *first-contributions* de GitHub a tu equipo.

## Crea una rama (*Branch*)

Cambia al directorio del repositorio en tu equipo (si es que no estás ahí ya).

```
cd first-contributions
```

Ahora crea una rama (*branch*) usando el comando  `git checkout` o `git switch`:
```
git checkout -b <dale un nombre>
git switch -c <dale un nombre>
```

Por ejemplo:
```
git checkout -b add-julio-jaramillo
git switch -c add-julio-jaramillo
```
<details>
<summary> <strong>Si obtienes algún error usando git switch, haz clic aquí:</strong> </summary>

Si aparece el mensaje de error "Git: `switch` no es un comando git. Consulta `git –help`", es probable que estés usando una versión anterior de git.

En este caso, intenta usar git checkout en su lugar.
</details>

## Haz los cambios necesarios y has un "Commit" de esos cambios

Abre el archivo `Contributors.md` en un editor de texto y añade tu nombre. No lo añadas ni al principio ni al final del archivo, hazlo en cualquier otro sitio. Ahora guarda el archivo.

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


## Haz un "Push" de tus cambios a GitHub

Envía tus cambios usando el comando `git push`:
```
git push -u origin <nombre-rama>
```
Reemplaza `<nombre-rama>` con el nombre de la rama que creaste anteriormente.

<details>
<summary> <strong>Si obtienes algún error al enviar (Push), haz clic aquí:</strong> </summary>

- ### Error de Autenticación
    <pre>remote: El soporte para la autenticación de contraseña se eliminó el 13 de agosto de 2021. Utiliza un token de acceso personal en su lugar.
  remote: Consulta [https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/) para obtener más información.
  fatal: Fallo en la autenticación para '[https://github.com/](https://github.com/)<tu-usuario>/first-contributions.git/'</pre>
    Ve al [tutorial de GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) sobre cómo generar y configurar una clave SSH en tu cuenta.

    Además, es posible que desees ejecutar `git remote -v` para verificar tu dirección remota.
    
    Si se ve algo como esto:
    <pre>origin [https://github.com/tu-usuario/tu_repo.git] (fetch)  
  origin  [https://github.com/tu-usuario/tu_repo.git] (push)</pre>

    
    cámbialo usando este comando:
    ```bash
    git remote set-url origin git@github.com:tu-usuario/tu_repo.git
    ```
    De lo contrario, aún se te pedirá un nombre de usuario y contraseña y obtendrás un error de autenticación.
</details>

## Envía (*Submit*) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz clic sobre este botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crea una pull request" />

Ahora envía el *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="enviar la pull request" />

Pronto estaré combinando tus cambios (haciendo *merge*) con la rama master de este proyecto. Recibirás una notificación por correo electrónico cuando los cambios hayan sido combinados.

## ¿Cuáles son los siguientes pasos?

¡Felicidades! ¡Has completado la línea de trabajo *_fork -> clone -> edit -> PR_* que encontrarás habitualmente como contribuidor!

Festeja tu contribución y compártela con tus amigos y seguidores yendo a la [web app](https://firstcontributions.github.io/#social-share).

Si deseas más práctica, consulta [code contributions](https://github.com/roshanjossey/code-contributions).

Ahora empieza a contribuir a otros proyectos. Hemos reunido una lista de proyectos con *issues* sencillas para que puedas empezar. Échale un ojo a la [lista de proyectos en la web app](https://firstcontributions.github.io/#project-list).

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriales usando otras herramientas

|<a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|<a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a>|<a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|<a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a>|
|---|---|---|---|---|---|
|[GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)|[Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)|[GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)|[Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)| [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)|[IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)|
