## Primeras Contribuciones

Este proyecto tiene como objetivo simplificar y guiar la forma en que los principiantes hacen su primera contribución.
Si estás buscando hacer tu primera contribución, sigue los pasos a continuación.

Si no te sientes cómodo usando la línea de comandos, aquí hay tutoriales que usan herramientas gráficas (GUI).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="hacer fork de este repositorio" />
Si no tienes git instalado en tu equipo, instálalo
.
##Haz un fork de este repositorio

Haz un fork de este repositorio haciendo clic en el botón Fork en la parte superior de esta página.
Esto creará una copia de este repositorio en tu cuenta.

## Clona el repositorio
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositorio" />

Ahora clona el repositorio bifurcado en tu computador.
Ve a tu cuenta de GitHub, abre el repositorio bifurcado, haz clic en el botón Code, luego en la pestaña SSH y finalmente haz clic en el ícono copiar URL al portapapeles.

Abre una terminal y ejecuta el siguiente comando de git:


```bash
git clone "url que acabas de copiar"
```
donde "url que acabas de copiar" (sin las comillas) es la URL de este repositorio (tu fork de este proyecto).
Consulta los pasos anteriores para obtener la URL.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

Por ejemplo:


```bash
git clone git@github.com:this-is-you/first-contributions.git
```
donde este-eres-tú es tu nombre de usuario en GitHub.
Aquí estás copiando el contenido del repositorio first-contributions de GitHub a tu computador.

## Crea una rama

Cambia al directorio del repositorio en tu computador (si aún no estás allí):

```bash
cd first-contributions
```
Ahora crea una rama usando el comando:


```bash
git switch -c nombre-de-tu-nueva-rama
```
Por ejemplo:

```bash
git switch -c add-alonzo-church
```
<details> <summary><strong>Si obtienes algún error al usar git switch, haz clic aquí:</strong></summary>

Si aparece el mensaje de error “Git: switch is not a git command. See git –help”, probablemente estés usando una versión antigua de git.

En ese caso, usa este comando en su lugar:

```bash
git checkout -b nombre-de-tu-nueva-rama
```
</details>

## Realiza los cambios necesarios y confírmalos

Abre el archivo Contributors.md en un editor de texto y agrega tu nombre.
No lo pongas al inicio ni al final del archivo; agrégalo en cualquier parte intermedia.
Luego guarda el archivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="estado de git" />

Si vas al directorio del proyecto y ejecutas el comando git status, verás que hay cambios.

Agrega esos cambios a la rama que acabas de crear con:
```bash
git add Contributors.md
```
Ahora confirma los cambios usando:
```bash
git commit -m "Agrega tu-nombre a la lista de contribuyentes"
```
reemplazando tu-nombre con tu nombre real.

## Sube los cambios a GitHub

Sube tus cambios con el comando:

```bash
git push -u origin nombre-de-tu-rama
```
reemplazando nombre-de-tu-rama con el nombre de la rama que creaste anteriormente.

<details> <summary><strong>Si obtienes errores al hacer push, haz clic aquí:</strong></summary>

## Error de autenticación
<pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead. remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information. fatal: Authentication failed for 'https://github.com/&lt;tu-usuario&gt;/first-contributions.git/'</pre>

Ve al tutorial de GitHub
 sobre cómo generar y configurar una llave SSH en tu cuenta.

También puedes ejecutar git remote -v para verificar tu dirección remota.

Si se ve así:

<pre>origin https://github.com/tu-usuario/tu_repositorio.git (fetch) origin https://github.com/tu-usuario/tu_repositorio.git (push)</pre>

Cámbiala con este comando:
```bash
git remote set-url origin git@github.com:tu-usuario/tu_repositorio.git
```
De lo contrario, seguirás recibiendo solicitudes de usuario y contraseña y obtendrás un error de autenticación.

</details>

## Envía tus cambios para revisión

Si vas a tu repositorio en GitHub, verás un botón que dice Compare & pull request.
Haz clic en ese botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crear un pull request" />

Ahora envía el pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="enviar pull request" />

Pronto tus cambios serán fusionados en la rama principal del proyecto.
Recibirás un correo de notificación cuando eso ocurra.

## ¿Qué sigue?

¡Felicidades! 🎉
Acabas de completar el flujo de trabajo estándar de fork → clone → edit → pull request que verás con frecuencia como colaborador.

Celebra tu contribución y compártela con tus amigos y seguidores visitando la aplicación web
.

Si quieres más práctica, revisa code contributions
.

Ahora te ayudaremos a comenzar a contribuir a otros proyectos.
Hemos recopilado una lista de proyectos con problemas sencillos con los que puedes empezar.
Consulta la lista de proyectos en la aplicación web
.


### [Material adicional](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriales con otras herramientas

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

</p>
