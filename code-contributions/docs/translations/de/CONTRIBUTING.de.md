# Schritte zum Beitrag

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

## Forken Sie dieses Repository, indem Sie auf die Schaltfläche fork klicken.

## Klonen Sie Ihren Fork von diesem Repository.

Klicken Sie in Ihrem Fork des Repositorys auf die Schaltfläche code. Wählen Sie die Registerkarte SSH und klicken Sie dann auf die Schaltfläche „In die Zwischenablage kopieren“.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />
Öffnen Sie ein Terminal und führen Sie den Befehl `git clone` aus

```bash
git clone „url you copied“
```

> [!IMPORTANT]
> Wenn Sie in den folgenden Schritten `<Ihre-github-id>` sehen, sollten Sie diese durch Ihre GitHub-ID ersetzen.  
> Wenn Ihre GitHub-ID zum Beispiel `aaronsw` lautet,  
> `git switch -c add-<ihre-github-id>` wird zu `git switch -c add-aaronsw`  
> `contributors/<Ihre-Github-ID>.html` wird zu `contributors/aaronsw.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL in die Zwischenablage kopieren" />

## Erstellen Sie einen Zweig

Wechseln Sie in das Repository-Verzeichnis, falls Sie nicht schon dort sind

```bash
cd code-contributions
```

Erzeugen Sie einen Zweig mit dem `git switch` Befehl

```bash
git switch -c add-<Ihre-github-id>
```


## Erstellen Sie Ihre Karte

Sie können Ihre Karte als HTML-Datei im Contributors-Verzeichnis hinzufügen. Erstellen Sie eine Datei mit Ihrem Benutzernamen im contributors-Verzeichnis. Sie können die folgende Vorlage kopieren, um zu beginnen.

`contributors/<Ihre-github-id>.html`
```html
<article>
  <h3>Dein Benutzername</h3>
  <p>Ein kleiner Lebenslauf über dick (optional)</p>
  <h4>Progamming-Sprachen, die ich benutze</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Tools, die ich benutze</h4>
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
## Add your card to contributors list

Add the name of the file you created to `scripts/contributors.js` file.

`scripts/contributors.js`
```js
const contributorFiles = [
  "<your-github-id>.html", // füge hier deinen Dateinamen ein
  "roshanjossey.html",
  "gokultp.html",
];
```

## Betrachten Sie Ihre Änderungen in einem Webbrowser

Sie können Ihre Änderungen sehen, indem Sie „index.html“ in einem Webbrowser öffnen. Sie sollten die neue Karte sehen können, die Sie in den vorherigen Schritten hinzugefügt haben.

Sie können weitere Änderungen an Ihrer Karte vornehmen und die Registerkarte des Webbrowsers aktualisieren, um die Änderungen zu sehen.

## Übertragen Sie Ihre Änderungen

Übertragen Sie zunächst Ihre Änderungen mit dem Befehl `git add`

```bash
git add contributors/<Ihre-github-id>.html
```

Übertragen Sie nun Ihre Änderungen mit dem Befehl `git commit`

```bash
git commit -m „add <ihre-github-id>“
```

## Pushen Sie Ihre Änderungen auf GitHub

```bash
git push -u origin add-<ihre-github-id>
```

## Übermitteln Sie Ihre Änderungen zur Überprüfung

Wenn Sie zu Ihrem Repository auf GitHub gehen, sehen Sie eine Schaltfläche „Vergleichen & Pull-Anfrage“. Klicken Sie auf diese Schaltfläche.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Reichen Sie nun den Pull-Request ein.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Sie erhalten eine Benachrichtigung per E-Mail, sobald die Änderungen zusammengeführt worden sind.