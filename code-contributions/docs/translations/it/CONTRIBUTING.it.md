# Passaggi per contribuire

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

## Crea il fork di questo repository cliccando sul pulsante `fork`

## Scarica (`clone`) il fork di questo repository

Nel tuo fork di questo repository, premi sul pulsante `Code`. seleziona SSH e poi clicca sull'icona per copiare.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Apri un terminale ed esegui il comando `git clone`

```bash
git clone "url che hai copiato"
```

> [!IMPORTANT]
> Nei passaggi seguenti, quando vedi `<il-tuo-id-github>` sostituiscilo con il tuo ID GitHub.
> Ad esempio, se il tuo ID GitHub fosse `aaronsw`,  
> `git switch -c add-<il-tuo-id-github>` diventa `git switch -c add-aaronsw`  
> `contributors/<it-tuo-id-github>.html` diventa `contributors/aaronsw.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy url" />

## Crea un branch (ramo)

Vai nella cartella del repository se non ci sei già

```bash
cd code-contributions
```

Crea un branch (ramo) con il comando `git switch`

```bash
git switch -c add-<il-tuo-id-github>
```


## Crea la tua card

Puoi aggiungere la tua carta come file HTML nella cartella `contributors`. Crea un file con il tuo username nella cartella `contributors`. Puoi copiare il seguente template per iniziare.

`contributors/<il-tuo-id-github>.html`
```html
<article>
  <h3>Il tuo username</h3>
  <p>Una breve bio su di te (opzionale)</p>
  <h4>I linguaggi di programmazione che uso</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Gli strumenti che uso</h4>
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

## Aggiungi la tua card nella lista dei contributori

Aggiungi il nome del file che hai creato all'interno del file `scripts/contributors.js`

`scripts/contributors.js`
```js
const contributorFiles = [
  "<il-tuo-github-id>.html", // Aggiungi il nome del tuo file qui
  "roshanjossey.html",
  "gokultp.html",
];
```


## Controlla le tue modifiche in un browser web

Puoi vedere le tue modifiche aprendo `index.html` in un browser web. Dovresti essere in grado di vedere la nuova carta che hai aggiunto nei passaggi precedenti. 

Puoi continuare a modificare la tua card e aggiornare la pagina per vedere le modifiche.

## Crea un commit

Prima, aggiungi le tue modifiche al branch con il comando `git add`

```bash
git add contributors/<il-tuo-github-id>.html
```

Ora crea un commit con il comando `git commit`

```bash
git commit -m "add <il-tuo-github-id>"
```

## Invia (`push`) le modifiche a GitHub

```bash
git push -u origin add-<il-tuo-github-id>
```

## Invia le tue modifiche per essere revisionate

Se vai nel tuo repository su GitHub, vedrai il pulsante `Compare & pull request`. Premilo.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Ora invia la tua pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />


Riceverai una notifica email quando le modifiche saranno approvate.

