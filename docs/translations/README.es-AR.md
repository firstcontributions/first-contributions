[![Amor por el Código Abierto](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Licencia: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![Ayudantes de Código Abierto](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Primera Contribución

Es difícil... Hacer algo por primera vez siempre es difícil. Especialmente si colaboras con otros, cometer errores es inaceptable. Sin embargo, la colaboración y el trabajo en equipo son la esencia del "Código Abierto". Queremos facilitar a quienes contribuyen por primera vez a proyectos de código abierto el aprendizaje del proceso y el envío de sus contribuciones iniciales.

Leer artículos y ver tutoriales puede ser útil, pero ¿qué puede reemplazar la práctica? Este proyecto busca facilitar las cosas a quienes comienzan o contribuyen por primera vez y guiarlos. Recuerda: cuanto más cómodo te sientas, más fácil será aprender. Si contribuyes a un proyecto de GitHub por primera vez, simplemente sigue los sencillos pasos que se muestran a continuación. Te prometemos que será divertido.


Si no tienes Git instalado en tu ordenador, instálalo. ## Bifurcando el Proyecto

Haz clic en el botón "Bifurcar" en la esquina superior derecha de la página para bifurcar este proyecto. Esto creará una copia del proyecto en tu cuenta.

## Clonando el Repositorio

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Copiar (clonar) este repositorio a tu computadora" />

Ahora clona este repositorio a tu computadora. Ve a tu cuenta de GitHub, abre el repositorio que bifurcaste, haz clic en el botón "clonar" y luego en el icono *copiar al portapapeles*.

Abre el símbolo del sistema y ejecuta el siguiente comando git:

```bash
git clone "the-url-you-copied"
```
Reemplaza "the-url-you-copied" (sin las comillas) con el enlace que obtuviste de la página de GitHub del repositorio.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="Copiar la URL de este enlace al portapapeles" />

Por ejemplo:
```bash
git clone https://github.com/username/first-contributions.git
```
`username` es tu nombre de usuario de GitHub. Aquí copia el contenido del repositorio first-contributions de GitHub a tu ordenador.

## Creación de una rama

Si aún no está en la carpeta, navegue a la ubicación de la carpeta principal en el símbolo del sistema:

```bash
cd first-contributions
```
Cree una nueva rama con el comando `git checkout`:
```bash
git checkout -b <your-new-branch-name>
```
Por ejemplo:
```bash
git checkout -b add-aydin-cagri-dumlu
```
(La palabra *add* no es obligatoria en el nombre de la rama, pero como esta se crea para agregar su nombre a la lista de colaboradores, escribir "add" tiene sentido).

## Realización y confirmación de los cambios necesarios

Ahora, abra el archivo `Contributors.md` en un editor de texto. Debe estar familiarizado con Markdown, un lenguaje de marcado simple. Puedes consultar esta [hoja de referencia](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) para aprender a usarla.

Añade esta línea al final del archivo `Contributors.md`:

```markdown
- [Tu nombre](https://github.com/tu-nombre-de-usuario)
```
Por ejemplo:

```markdown
- [Ahmet Yılmaz](https://github.com/ahmet-yilmaz)
```

Asegúrate de que no haya espacios entre `](`. Guarda y cierra el archivo.

<img align="right" width="450" ​​​​src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="Resultado del comando git status ejecutado en el símbolo del sistema" />

Ve a la carpeta del proyecto en el símbolo del sistema y escribe el comando `git status` para ver los cambios realizados.

Añade estos cambios a la rama que creaste con el comando `git add`.

```bash
git add Contributors.md
```

Ahora confirma los cambios Usando el comando `git commit`. (commit):
```bash
git commit -m "<tu nombre> ha sido añadido a la lista de colaboradores"
```
Reemplaza `<tu nombre>` por tu nombre.

(Nota: Dado que trabajarás con personas de diferentes partes del mundo en el mundo del código abierto, puedes escribir el mensaje de confirmación en inglés).

## Subiendo cambios a GitHub

Sube tus cambios con el comando `git push`:
```bash
git push origin <add-your-branch-name>
```
Reemplaza `<add-your-branch-name>` por el nombre de la rama que creaste anteriormente.

## Envía tus cambios para revisión

En la página de GitHub del repositorio que creaste, verás el botón `Comparar y solicitar pull`. Pulsa este botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/