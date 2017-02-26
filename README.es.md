# Primeras Contribuciones

Si no tienes git en tu equipo, [ instálalo ]( https://help.github.com/articles/set-up-git/ )

Haz Fork de este repositorio clicando en el botón fork

<img style="float: right;" width="300" src="assets/fork.png">

Ahora clona este repositorio a tu equipo. Haz click sobre el botón clone y luego en el icono copiar a clipboard

<img style="float: right;" width="300" src="assets/clone.png">
<img style="float: right;" width="300" src="assets/copy-to-clipboard.png">

Abre un terminal y escribe

```
git clone <url que tu has copiado>
```
Donde la url puede ser pegada desde el clipboard
Por ejemplo
```
git clone https://github.com/this-is-you/first-contributions.git
```
Aquí tú estas copiando el contenido del repositorio first-contributions en github a tu ordenador

Entra en ese directorio

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

Ahora abre el archivo `Contributors.md` en un editor de texto y añade tu nombre, guarda el archivo

Si vas al directorio del proyecto y haces `git status`, tú verás los cambios

Añade estos cambios con el comando `git add`

```
git add Contributors.md
```

Ahora puedes hacer commit sobre los cambios con el comando `git commit`

```
git commit -m "Add <tu-nombre> to Contributors list"
```
cambia `<tu-nombre>` con tu nombre

Puedes hacer Push en tus cambios con el comando `git push`

```
git push origin <añade-tu-nombre>
```
Cambia `<añade-tu-nombre>` con el nombre de la branch que creaste antes

Si vas a tu repositorio en github verás un botón para abrir una pull request. Haz click sobre ese botón

<img style="float: right;" src="assets/compare-and-pull.png">

Ahora submit la pull request 

<img style="float: right;" src="assets/submit-pull.png">

### Manten tu fork sincronizado con este repositorio

Ahora yo haré merge con tus cambios dentro de la master branch de este proyecto.
Luego tu fork no tendrá estos cambios. En orden a mantener tu fork sincronizado con el mío,

Añade la url de mi repositorio como `upstream remote url`

```
git remote add upstream https://github.com/multunus/first-contributions
```
Este es una manera de decirle a git que otra versión de este proyecto existe en esa url y nosotros estamos llamando a su upstream.

```
git fetch upstream
```
Aquí estamos trayendo todos los cambios en mi fork (upstream remote)

```
git rebase upstream/master
```
Aquí tú estas aplicando todos los cambios anteriores en master branch.
Si tú haces push en master branch ahora, tu fork también tendrá los cambios.
```
git push origin master
```
Date cuenta que aquí tú estas haciendo Push hacia el remoto llamado origin

[Tutorial for Github desktop app - English](github-desktop-tutorial.md)
