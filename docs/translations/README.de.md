[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

Dieses Projekt zielt darauf ab, Anfängern den Einstieg zu erleichtern und sie bei ihrem ersten Beitrag zu unterstützen. Wenn du deinen ersten Beitrag leisten möchten, befolge die folgenden Schritte.

_Wenn du nicht weißt wie man das Terminal/CMD bedient, [hier findest du Anleitungen für GUI Tools.](#Anleitungen-für-andere-Tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Forke dieses Repository" />

#### Wenn du Git nicht auf deinem System installiert hast, [installiere es](https://...github.com/en/get-started/quickstart/set-up-git).

## Forke dieses Repository

Forke dieses Repository indem du auf den Fork Button oben auf dieser Seite klickst.
Dies wird eine Kopie dieses Repository's in deinem Account erstellen.

## Klone das Repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Klone dieses Repository" />

Klone jetzt das geforkte Repository auf deinen Computer. Gehe zu deinem Github Account, öffne das geforkte Repository, drücke auf den Code Button, dann auf den SSH Tab und dann drücke auf das _copy url to clipboard_ icon.

Öffne ein Terminal Fenster und führe den folgenden Git Befehl aus:

```bash
git clone "kopierte url"
```

wobei "kopierte url" (ohne die Anführungszeichen) die url zu diesem Repository ist (deine Fork von diesem Projekt). Im vorherigen Schritt siehst du wie du diese erhälst .

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL in die Zwischenablage kopieren" />

Zum Beispiel:

```bash
git clone git@github.com:das-bist-du/erster-Beitrag.git
```

wobei `das-bist-du` dein Github Nutzername ist. Hier kopierst du den Inhalt des first-contributions Repository's auf Github auf deinen Computer.

## Erstelle einen Zweig

Wechsle zum Repository Ordner (wenn du nicht bereits dort bist):

```bash
cd first-contributions
```

Erstelle nun einen Zweig, indem du den `git switch` Befehl benutzst:

```bash
git switch -c dein-neuer-zweig-name
```

Zum Beispiel:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>Wenn du auf irgendeinen Fehler bei der Nutzung von git switch stößt, drücke hier:</strong> </summary>

Wenn die Fehlermeldung "Git: `switch` is not a git command. See `git –help`" erscheint, liegt dies wahrscheinlich daran das du eine veraltete Version von Git nutzt.

In diesem Fall versuche stattdessen `git checkout` zu nutzen:

```bash
git checkout -b dein-neuer-zweig-name
```

</details>

## Make necessary changes and commit those changes

Öffne nun die Datei `Contributors.md` in einem Texteditor und füge deinen Namen hinzu. Füge ihn nicht ganz am Anfang oder am Ende hinzu, sondern irgendwo dazwischen, mittendrin. Speichere jetzt die Datei.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Wenn du in den Projektordner gehst und den Befehl `git status`, ausführst werden dir die Änderungen angezeigt.

Füge diese Änderungen nun zu dem Zweig hinzu den du gerade erstellt hast, indem du den Befehl `git add` ausführst.

```bash
git add Contributors.md
```

Jetzt commite diese Änderungen mit dem `git commit` Befehl:

```bash
git commit -m "Add your-name to Contributors list"
```

ersetze `your-name` mit deinem Namen.

## Änderungen auf Github pushen

Übertrage deine Änderungen mit `git push`:

```bash
git push -u origin dein-zweig-name
```

ersetze `dein-zweig-name` mit dem Namen des Zweiges den du vorhin erstellt hast.

<details>
<summary> <strong>Solltest du auf irgendwelche Fehler beim Pushen stoßen, drücke hier:</strong> </summary>

- ### Authentifizierungs Fehler
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Gehe zu [GitHub's tutorial](https://...github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) wie du einen ssh Key zu deinem Account hinzufügst und konfigurierst.
  Außerdem, kannst du 'git remote -v' ausführen um deine Remote Addresse anzuzeigen.
  
  Wenn es so aussieht:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>
  
  ändere es mit diesem Befehl:
  ```bash
  git remote set-url origin git@github.com:dein-nutzername/dein_repo.git
  ```
  Ansonsten wirst du noch immer aufgefordert Passwort und Benutzername einzugeben und bekommst einen Authentifizierungs Fehler.
</details>

## Reiche deine Änderungen für ein Review ein

Wenn du jetzt zu deinem Repository auf Github gehts, wirst du einen `Compare & pull request` Knopf sehen. Drücke diesen Knopf.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="erstelle eine Pull-Request" />

Jetzt, reiche deine Pull-Request ein.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Reiche deine Pull-Request ein" />

Bald werde ich alle deine Änderungen in den Haupt-Zweig dieses Projektes mergen. Du wirst eine Benachrichtigungs Email bekommen sobald die Änderungen gemerged wurden.

## Was nun?

Gratulation! Du hast gerade den Standard _Forken -> Klonen -> Bearbeiten -> Pull-Request_ Workflow durchgeführt, dem du als Beitragender oft begegnen wirst!

Feier deinen Beitrag und teile in mit deinen Freunden und Followern indem du hier drückst [web app](https://firstcontributions.github.io/#social-share).

Wenn du gerne mehr Übung hättest, schau dir [code contributions](https://github.com/roshanjossey/code-contributions) an.

Jetzt los gehts, mit Beiträgen zu anderen Projekten. Wir haben eine Liste von Projekten mit leichten Fehlern für Einsteiger bereitgestellt. Schau dir [die Liste der Projekte in der Web-App an](https://firstcontributions.github.io/#project-list) an.

### [Zusätzliches Material](../additional-material)

## Anleitungen für andere Tools

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)   | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)   | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)  | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

<p>Dieses Projekt wird unterstützt von:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
