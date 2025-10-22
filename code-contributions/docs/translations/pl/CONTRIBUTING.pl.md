
# Kroki do opublikowania

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

## Zrób fork repozytorium (`fork`)

## Sklonuj repozytorium (`clone`)

Sklonuj to zforkowane repozytorium ze swojego konta GitHub na swój komputer. Przejdź do swojego konta na skopiowane code-contributions repozytorium i kliknij na `code`, potem na `SSH` i w końcu `skopiuj do schowka.`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />
Otwórz konsolę i uruchom `git clone` komendę:

```bash
git clone <skopiowany URL>
```

> [!IMPORTANT]
> W następnych krokach, gdy zobaczysz `<twoje-github-id>`, powinno być to wymienione z twoim własnym GitHub ID (username).
> Na przykład, jeśli twój GitHub ID to `maryja`,  
> `git switch -c add-<twoje-github-id>` staję się `git switch -c add-maryja`  
> `contributors/<twoje-github-id>.html` staję się `contributors/maryja.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

## Stwórz gałąź (`branch`)

Przejdź do folderu repozytorium (jeżeli jeszcze tam nie jesteś):

```bash
cd code-contributions
```

Teraz utwórz nową gałąź wykonując polecenie `git switch`:

```bash
git switch -c add-<twoje-github-idd>
```


## Stwórz swoją kartę

Możesz dodać swoją kartę jako plik HTML do folderu **contributors**. Utwórz plik z nazwą `<twoje-github-id>.html` w folderze contributors. Skopiuj poniższy szablon do pomocy:

`contributors/<twoje-github-id>.html`
```html
<article>
  <h3>Twoje username</h3>
  <p>Krótki opis o tobie (opcjonalne)</p>
  <h4>Języki programowania, których używam</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Narzędzia, których używam</h4>
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
## Dodaj swoją kartę do listy kontributorów

Dodaj nazwe twojego pliku do `scripts/contributors.js` pliku.

`scripts/contributors.js`
```js
const contributorFiles = [
  "<your-github-id>.html", // dodaj nazwę twojego pliku
  "roshanjossey.html",
  "gokultp.html",
];
```

## Obejrzyj swoje zmiany w przeglądarce

Możesz obejrzeć zmiany otwierając `index.html` w swojej przeglądarace internetowej. Twoja nowa karta powinna być już widzialna po poprzednich krokach.

Możesz dodawać zmiany i odświeżać stronę, żeby je zobaczyć.

## Zapisz swoje zmiany (`commit`)

Jeżeli wejdziesz do folderu ze swoim repozytorium i wykonasz komendę `git status`, zobaczysz, że są tam zmiany. Dodaj te zmiany do gałęzi którą właśnie utworzyłeś używając komendy `git add`:

```bash
git add contributors/<twoje-github-id>.html
```

Teraz zapisz te zmiany wykonując komendę `git commit`:

```bash
git commit -m "add <twoje-github-id>"
```

## Wyślij zmiany na GitHub

```bash
git push -u origin add-<twoje-github-id>
```

## Wyślij zmiany do zatwierdzenia 

W swoim repozytorium na GitHubie znajdziesz przycisk `Compare & pull request`. Kliknij go.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Teraz wyślij prośbę o scalenie.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Zostaniesz powiadomiony mailowo kiedy zmiany zostaną scalone.
