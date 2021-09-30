[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" width="40"> | IntelliJ IDEA |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


Es dificil. Siempre es difícil la primera vez que haces algo. Especialmente cuando estás colaborando, cometer errores no es algo cómodo. Pero el código abierto tiene que ver con la colaboración y el trabajo conjunto. Queríamos simplificar la forma en que los nuevos colaboradores de código abierto aprenden y contribuyen por primera vez.

Leer artículos y ver tutoriales puede ayudar, pero ¿qué es mejor que hacer las cosas sin estropear nada? Este proyecto tiene como objetivo proporcionar orientación y simplificar la forma en que los novatos hacen su primera contribución. Recuerde que cuanto más relajado esté, mejor aprenderá. Si está buscando hacer su primera contribución, simplemente siga los sencillos pasos a continuación. Te lo prometemos, será divertido.

Si no tiene IntelliJ IDEA en su máquina, [instalarlo](https://www.jetbrains.com/idea/download/#section=windows)

** Aviso: ** Este tutorial se realizó con IntelliJ IDEA (versión 2019.3.2) en una máquina con Windows 10. Más adelante en este tutorial haremos uso de algunos atajos de teclado. Estos pueden diferir en otros sistemas operativos (macOS / Linux).

## Bifurca este repositorio

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="bifurcar este repositorio" />

Bifurque este repositorio haciendo clic en el botón de bifurcación en la parte superior derecha de esta página. Esto creará una copia de este repositorio en su cuenta de GitHub.

GitHub realiza un seguimiento de la relación entre su repositorio y el que lo ha bifurcado. Puede pensar en su repositorio como una copia de trabajo.

La mayoría de los repositorios de GitHub de nivel superior (es decir, los que no se bifurcan desde ningún otro repositorio) tienen un pequeño equipo central de personas que pueden realizar cambios directamente. Todos los demás contribuyentes deben bifurcar el repositorio y realizar cambios en el bifurcación, luego crear una solicitud de extracción para solicitar fusionar sus cambios en el repositorio de nivel superior. Si el administrador de repositorios de nivel superior aprueba los cambios, se fusionarán y usted obtendrá fama y fortuna instantáneamente. Más sobre cómo hacer eso más adelante.

## Clona tu repositorio

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositorio" />

El siguiente paso es clonar su repositorio en su máquina para que pueda comenzar a hacer cambios. IntelliJ IDEA necesita la URL de su repositorio, así que haga clic en el botón "clonar" y luego haga clic en el icono "copiar al portapapeles".

** CUIDADO: ** Un error que suelen cometer los nuevos contribuyentes es clonar el repositorio del que se bifurcó _from_ en lugar de clonar su repositorio. Verifique la barra de direcciones de su navegador y asegúrese de que está clonando su repositorio.

Ahora abra IntelliJ IDEA.

IntelliJ IDEA le permite verificar (en términos de Git, clonar) un repositorio existente y crear un nuevo proyecto basado en los datos que ha descargado.

En el menú principal, elija VCS | Obtener de Control de versiones o, si no hay ningún proyecto abierto actualmente, haga clic en Obtener de Control de versiones en la pantalla de bienvenida.

En el cuadro de diálogo Obtener del control de versiones, especifique la URL del repositorio remoto que desea clonar (puede hacer clic en Probar para asegurarse de que se pueda establecer la conexión con el control remoto) o seleccione uno de los servicios de alojamiento VCS de la izquierda. Si ya ha iniciado sesión en el servicio de alojamiento seleccionado, la finalización le sugerirá la lista de repositorios disponibles que puede clonar.

Haga clic en Clonar. Si desea crear un proyecto IntelliJ IDEA basado en las fuentes que ha clonado, haga clic en Sí en el cuadro de diálogo de confirmación. La asignación de raíz de Git se establecerá automáticamente en el directorio raíz del proyecto.

Si su proyecto contiene submódulos, también se clonarán y se registrarán automáticamente como raíces del proyecto.

** Importante **: asegúrese de que sea el repositorio bifurcado y no el original, de lo contrario no funcionará.

## Crea una sucursal

En Git, la ramificación es un mecanismo poderoso que le permite divergir de la línea de desarrollo principal, por ejemplo, cuando necesita trabajar en una función o congelar un cierto estado de una base de código para una versión, etc.

En IntelliJ IDEA, todas las operaciones con ramas se realizan en la ventana emergente Git Branches. Para invocarlo, haga clic en el widget de Git en la barra de estado o presione Ctrl + Shift + `.

La nueva rama comenzará desde el HEAD actual. Si desea iniciar una rama desde una confirmación anterior en lugar del HEAD de la rama actual, seleccione esta confirmación en la pestaña Registro de la ventana de la herramienta Control de versiones Alt + 9 y elija Nueva rama en el menú contextual.

## Realiza los cambios necesarios

Abra 'Contributors.md' y agregue su nombre en cualquier lugar del archivo. Este archivo contiene GFM (GitHub Flavored Markdown) que es una versión patentada del <a href="https://en.wikipedia.org/wiki/Markdown">reducción</a> sintaxis.

Copie uno de los otros colaboradores & apos; lines y modifíquelo con su nombre para asegurarse de obtener la sintaxis correcta; puede ser delicado.

## Confirmar y enviar cambios a GitHub

Seleccione los archivos que desea confirmar o una lista de cambios completa en la pestaña Cambios locales de la ventana de la herramienta Control de versiones Alt + 9 y presione Ctrl + K o haga clic en el botón Confirmar Confirmar en la barra de herramientas.

El cuadro de diálogo Confirmar cambios que se abre enumera todos los archivos que se han modificado desde la última confirmación, así como todos los archivos no versionados recién agregados.

Ingrese un mensaje de confirmación significativo.

Puede hacer clic en Confirmar historial de mensajes Confirmar historial de mensajes Ctrl + M para elegir de la lista de mensajes de confirmación recientes.

También puede editar el mensaje de confirmación más tarde antes de enviar la confirmación.

Presione Ctrl + Shift + K o elija VCS | Git | Empuje desde el menú principal. Se abre el cuadro de diálogo Push Commits que muestra todos los repositorios de Git (para proyectos de varios repositorios) y una lista de todas las confirmaciones realizadas en la rama actual en cada repositorio desde la última inserción.

## Envíe sus cambios para su revisión

En este punto, ha completado su cambio, pero aún reside en su repositorio. Este paso le mostrará cómo enviar una solicitud al administrador del repositorio de nivel superior para fusionar su cambio.

En su repositorio en GitHub, verá el botón `Comparar y solicitar extracción` junto a la notificación de la nueva rama. Haga clic en ese botón.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="crear una solicitud de extracción" />

Ahora envíe la solicitud de extracción.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="enviar solicitud de extracción" />

Pronto fusionaré todos tus cambios en la rama principal de este proyecto. Recibirá un correo electrónico de notificación una vez que se hayan combinado los cambios.

## ¿A dónde ir desde aquí?

¡Felicitaciones! ¡Acaba de completar el flujo de trabajo estándar _fork -> clonar -> editar -> PR_ que encontrará a menudo como colaborador!

Celebre su contribución y compártala con sus amigos y seguidores yendo a [Aplicación Web] (https://firstcontributions.github.io#social-share).

Puede unirse a nuestro equipo de slack en caso de que necesite ayuda o tenga alguna pregunta. [Únete al equipo de Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).


### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriales con otras herramientas
[Volver a la pagina principal](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)

