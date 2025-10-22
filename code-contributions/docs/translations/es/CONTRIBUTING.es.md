# Pasos para Contribuir

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

## Haz un fork de este repositorio haciendo clic en el botón de fork

## Clona tu fork de este repositorio.

En tu fork de este repositorio, haz clic en el botón de código. Selecciona la pestaña SSH y luego haz clic en el botón `copiar al portapapeles`.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clona este repositorio" />
Open a terminal and run `git clone` command

```bash
git clone "url copiada"
```

> [!IMPORTANT]
> En los siguientes pasos, cuando veas `<tu-github-id>` debes reemplazarlo con tu ID de GitHub.  
> Por ejemplo, si tu ID de GitHub es `aaronsw`,  
> `git switch -c add-<tu-github-id>` se convierte en `git switch -c add-aaronsw`  
> `contributors/<tu-github-id>.html` se convierte en `contributors/aaronsw.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

## Crea una rama

Ve al directorio del repositorio si no estás allí ya

```bash
cd code-contributions
```

Crea una rama con el comando `git switch`

```bash
git switch -c add-<tu-github-id>
```

## Crea tu tarjeta

Puedes agregar tu tarjeta como un archivo HTML en el directorio de contribuyentes. Crea un archivo con tu nombre de usuario en el directorio de contribuyentes. Puedes copiar la siguiente plantilla para comenzar.

`contributors/<tu-github-id>.html`
```html
<article>
    <h3>Tu nombre de usuario</h3>
    <p>Una pequeña biografía sobre ti (opcional)</p>
    <h4>Lenguajes de programación que uso</h4>
    <section class="container">
        <div class="badge" style="background-color: #3874a4; color: white">
            Python
        </div>
        <div class="badge" style="background-color: #f7df1e; color: black;">
            JavaScript
        </div>
    </section>

    <h4>Herramientas que uso</h4>
    <section class="container">
        <img
            class="icon"
            src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"
        />
        <img
            class="icon"
            src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"
        />
    </section>
</article>
<style>
    body {
        font-family: sans-serif;
    }
    .container {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .badge {
        padding: 0.5rem;
        border-radius: 0.25rem;
    }
    .icon {
        width: 2rem;
    }
</style>
```
## Agrega tu tarjeta a la lista de contribuyentes

Agrega el nombre del archivo que creaste al archivo `scripts/contributors.js`.

`scripts/contributors.js`
```js
const contributorFiles = [
    "<tu-github-id>.html", // agrega el nombre de tu archivo aquí
    "roshanjossey.html",
    "gokultp.html",
];
```

## Ve tus cambios en un navegador web

Puedes ver tus cambios abriendo `index.html` en un navegador web. Deberías poder ver la nueva tarjeta que agregaste en los pasos anteriores.

Puedes continuar haciendo cambios a tu tarjeta y actualizar la pestaña del navegador para ver esos cambios.

## Confirma tus cambios

Primero prepara tus cambios con el comando `git add`

```bash
git add contributors/<tu-github-id>.html
```

Ahora confirma tus cambios con el comando `git commit`

```bash
git commit -m "add <tu-github-id>"
```

## Empuja tus cambios a GitHub

```bash
git push -u origin add-<tu-github-id>
```

## Envía tus cambios para revisión

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz clic en ese botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crear una solicitud de extracción" />

Ahora envía la solicitud de extracción.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="enviar solicitud de extracción" />

Recibirás un correo electrónico de notificación una vez que los cambios hayan sido fusionados.
