[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|

Esta es una guía para nosotros, los nerds de terminales, que queremos hacer todo en el terminal, y gracias a [Github-CLI](https://cli.github.com/), podemos lograrlo, recordando tu primera contribución. ¡Debe ser divertido, gratificante y motivador para seguir adelante!

Esta guía es un poco más desafiante ya que no usamos ninguna interfaz gráfica, pero aún así es muy divertida y ¡definitivamente puedes seguirla!

El primer requisito es tener:
- Git instalado (cómo instalar [git](https://git-scm.com/downloads))
- Cuenta de Github

Ahora vamos a necesitar instalar el `github-cli` En nuestro sistema siguiendo la [documentación oficial](https://github.com/cli/cli#installation)

Después, debemos iniciar sesión en **CLI** (Interfaz de Línea de Comandos) usando el siguiente comando:
```bash 
gh auth login
```

Sigue las instrucciones y estamos listos.!

# Bifurcar este repositorio
Es tan fácil como ejecutar este comando:

```bash
gh repo fork firstcontributions/first-contributions
```
**Importante: Te preguntará si también quieres clonarlo, selecciona la opción "sí"**

# Crea tu sucursal
Haremos este paso con git, así que ingresa este comando reemplazando el nombre con tu nombre, por ejemplo:
```bash 
git switch -c add-john-doe
```

# Realizar los cambios necesarios y confirmar esos cambios.
Ahora puede abrir el archivo `Contributors.md` en un editor de texto y agregarle su nombre. Coloque su nombre en cualquier lugar entre el principio y el final, luego guarde el archivo.

En el directorio del proyecto ejecute `git status` y verá los cambios.
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

Agrega esos cambios a la rama que acabas de crear usando el comando `git add`:
`git add Contributors.md`

Ahora confirma esos cambios usando el comando `git commit`:
`git commit -m "Add your-name to Contributors list`
reemplazando `your-name` con tu nombre.

# Enviar cambios a github
Empuje sus cambios usando el comando `git push`:

```
git push origin -u your-branch-name
```

reemplazando `your-branch-name` con el nombre de la sucursal que creaste anteriormente.

<details>
<summary> <strong>Si tienes algún error al hacer pull, haz click aquí</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Visita [Tutorial de github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

</details>

# Envíe sus cambios para su revisión
Ahora, ejecutar este comando en el directorio de nuestro repositorio nos permitirá crear una solicitud de extracción para revisión:

```bash 
gh pr create --repo firstcontributions/first-contributions
```

Después de eso, envíe la solicitud de extracción.

Puede usar el comando `gh status` para ver la solicitud de extracción mencionada en acción.

## ¿A dónde ir desde aquí?

¡Felicidades! ¡Acabas de completar el flujo de trabajo estándar _fork -> clone -> edit -> pull request_ workflow que encontrarás a menudo como colaborador!

Celebre su contribución y compártala con sus amigos y seguidores en [aplicación web](https://firstcontributions.github.io/#social-share).

Puedes unirte a nuestro equipo de Slack si necesitas ayuda o tienes alguna pregunta. [Únase al equipo de Slack] (https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

Ahora comencemos a contribuir a otros proyectos. Hemos compilado una lista de proyectos con problemas sencillos con los que puede comenzar. Consulte [la lista de proyectos en la aplicación web] (https://firstcontributions.github.io/#project-list).

### [Material adicional](additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriales usando otras herramientas

[Regresa a la página principal](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
