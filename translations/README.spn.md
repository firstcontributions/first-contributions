# Primeras Contribuciones

Este proyecto tiene como objetivo simplificar y guiar a los principiantes en su primera contribución. Si estás buscando hacer tu primera contribución, sigue los pasos a continuación.

**Si no te sientes cómodo con la línea de comandos, [aquí tienes tutoriales que utilizan herramientas gráficas.](#tutoriales-usando-otras-herramientas)**

![fork this repository](https://firstcontributions.github.io/assets/Readme/fork.png)

### Si no tienes git en tu máquina, [instálalo](https://docs.github.com/es/get-started/quickstart/set-up-git).

## Haz un fork de este repositorio

Haz un fork de este repositorio haciendo clic en el botón de fork en la parte superior de esta página. Esto creará una copia de este repositorio en tu cuenta.

## Clona el repositorio

![clone this repository](https://firstcontributions.github.io/assets/Readme/clone.png)

Ahora clona el repositorio forkeado en tu máquina. Ve a tu cuenta de GitHub, abre el repositorio forkeado, haz clic en el botón de código y luego haz clic en el ícono de "copiar al portapapeles".

Abre una terminal y ejecuta el siguiente comando git:

```
git clone "URL que acabas de copiar"
```

Donde "URL que acabas de copiar" (sin las comillas) es la URL de este repositorio (tu fork de este proyecto). Consulta los pasos anteriores para obtener la URL.

![copy URL to clipboard](https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png)

Por ejemplo:

```
git clone git@github.com:this-is-you/first-contributions.git
```

Donde `this-is-you` es tu nombre de usuario de GitHub. Aquí estás copiando el contenido del repositorio first-contributions en GitHub a tu computadora.

## Crea una rama

Cambia al directorio del repositorio en tu computadora (si aún no estás allí):

```
cd first-contributions
```

Ahora crea una rama usando el comando `git switch`:

```
git switch -c nombre-de-tu-nueva-branch
```

Por ejemplo:

```
git switch -c agregar-alonzo-church
```

## Realiza los cambios necesarios y realiza el commit de esos cambios

Ahora abre el archivo `Contributors.md` en un editor de texto, agrega tu nombre a él. No lo agregues al principio o al final del archivo. Ponlo en cualquier lugar en medio. Ahora, guarda el archivo.

![git status](https://firstcontributions.github.io/assets/Readme/git-status.png)

Si vas al directorio del proyecto y ejecutas el comando `git status`, verás que hay cambios.

Añade esos cambios a la rama que acabas de crear utilizando el comando `git add`:

```
git add Contributors.md
```

Ahora realiza el commit de esos cambios utilizando el comando `git commit`:

```
git commit -m "Añade tu-nombre a la lista de Contribuidores"
```

Sustituye `tu-nombre` por tu nombre.

## Sube los cambios a GitHub

Sube tus cambios utilizando el comando `git push`:

```
git push -u origin nombre-de-tu-branch
```

Sustituye `nombre-de-tu-branch` por el nombre de la rama que creaste anteriormente.

<details>
<summary> **Si obtienes algún error al realizar la subida, haz clic aquí:** </summary>

- **Error de autenticación**
     <pre>remote: El soporte para la autenticación mediante contraseña se eliminó el 13 de agosto de 2021. Utiliza en su lugar un token de acceso personal.
  remote: Consulta https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ para obtener más información.
  fatal: Error de autenticación para 'https://github.com/<tu-nombre-de-usuario>/first-contributions.git/'</pre>
  Ve a [el tutorial de GitHub](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) sobre cómo generar y configurar una clave SSH para tu cuenta.

</details>

## Envía tus cambios para su revisión

Si vas a tu repositorio en GitHub, verás un botón de "Comparar y crear una solicitud de extracción". Haz clic en ese botón.

![create a pull request](https://firstcontributions.github.io/assets/Readme/compare-and-pull.png)

Ahora, envía la solicitud de extracción.

![submit pull request](https://firstcontributions.github.io/assets/Readme/submit-pull-request.png)

Pronto fusionaré todos tus cambios en la rama principal de este proyecto. Recibirás un correo electrónico de notificación una vez que los cambios se hayan fusionado.

## ¿Qué hacer a partir de aquí?

¡Felicidades! Acabas de completar el flujo de trabajo estándar "fork -> clonar -> editar -> solicitud de extracción" que a menudo encontrarás como contribuyente.

Celebra tu contribución y compártela con tus amigos y seguidores

 yendo a [la aplicación web](https://firstcontributions.github.io/#social-share).

Puedes unirte a nuestro equipo de Slack si necesitas ayuda o tienes alguna pregunta. [Únete al equipo de Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w).

Ahora, vamos a ayudarte a empezar a contribuir a otros proyectos. Hemos compilado una lista de proyectos con problemas sencillos en los que puedes empezar. Echa un vistazo a [la lista de proyectos en la aplicación web](https://firstcontributions.github.io/#project-list).

### [Material adicional](additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriales Usando Otras Herramientas

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
