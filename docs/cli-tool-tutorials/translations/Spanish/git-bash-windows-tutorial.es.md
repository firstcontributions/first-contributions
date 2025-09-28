[![Amor por el Código Abierto](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![Licencia: MIT](https://img.shields.io/badge/Άδεια-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Contribuyentes de Código Abierto](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primeras Contribuciones

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Versión de Git Bash |
| ------------------------------------------------------------------------------------------------------------------ | --------------------- |

Es difícil. Siempre es difícil la primera vez que haces algo. Especialmente cuando colaboras, cometer errores puede ser incómodo. Pero el código abierto trata precisamente de colaboración y trabajo en conjunto. Queríamos simplificar el proceso mediante el cual nuevos colaboradores aprenden y hacen su primera contribución.

Leer artículos y ver tutoriales en video puede ayudar, pero no hay nada como aprender haciendo sin temor a equivocarte. Este proyecto busca proporcionar una guía clara y sencilla para que principiantes hagan su primera contribución. Recuerda, cuanto más relajado estés, mejor aprenderás. Si estás buscando hacer tu primera contribución, simplemente sigue estos pasos. Te prometemos que será divertido.

Si aún no tienes Git Bash en tu computadora con Windows, [descárgalo aquí](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="haz un fork de este repositorio" />

## Haz un fork de este repositorio

Haz clic en el botón "Fork" en la esquina superior derecha de esta página para crear una copia de este repositorio en tu cuenta.

## Clona tu repositorio

Ahora clona ese repositorio en tu computadora.

⚠️ IMPORTANTE: NO clones el repositorio original.

Ve a tu fork y clónalo.

Para hacerlo, haz clic en "Code" y copia el enlace.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copiar enlace" />

Abre la aplicación Git Bash que acabas de instalar. Debería lucir como la siguiente imagen si estás en Windows:

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="abrir terminal de git bash" />

Ve a la carpeta donde quieres guardar este proyecto usando el comando:

`cd <carpeta>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="entrar a la carpeta deseada" />

Usa el enlace copiado anteriormente para clonar tu repositorio:

`git clone <url-del-repositorio>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clonar repositorio" />

Ve al directorio recién clonado y ábrelo en Visual Studio Code para hacer tus cambios.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="entrar al repo clonado" />

## Crear una rama

Ahora crea una nueva rama usando este comando:

```
git checkout -b <nombre-de-tu-rama>
```

Ejemplo: `add-james-smith`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="crear rama" />

## Realiza los cambios necesarios

Abre el archivo `Contributors.md` en tu editor, ve al final del archivo y agrega tu nombre.

Ejemplo:
```md
[James Smith](https://github.com/jamessmith)
```

Para verificar los cambios:

```bash
git status
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="ver estado" />

Ahora haz commit de los cambios:

Primero agrega el archivo:

```bash
git add Contributors.md
```

Después crea el commit:

```bash
git commit -m "Agrego mi nombre a la lista de contribuidores"
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit de cambios" />

Para verificar el commit:

```bash
git log --oneline
```

## Sube tus cambios a GitHub

```bash
git push origin <nombre-de-tu-rama>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-push.png" alt="hacer push" />

## Envía tu Pull Request

Ve a tu repositorio en GitHub. Verás un botón que dice “Compare & pull request”. Haz clic allí.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="crear pull request" />

Completa el formulario y envía el Pull Request.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="enviar PR" />

Pronto tus cambios serán revisados e integrados al repositorio principal. Recibirás una notificación por correo.

## ¿Y ahora qué?

¡Felicidades! Has completado el flujo de trabajo clásico _fork → clone → editar → pull request_ que es común en el mundo del open source.

Celebra tu contribución compartiéndola con tus amigos o en redes. También puedes unirte al equipo en Slack para resolver dudas:  
👉 [Únete al Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

### [Material adicional](../additional-material/git_workflow_scenarios/additional-material.md)

## Guías para otras herramientas

[Volver a la página principal](https://github.com/firstcontributions/first-contributions/blob/main/translations/README.es.md#material-de-apoyo-para-otras-herramientas)
