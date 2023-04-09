[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)



# Erste Beiträge

Dieses Projekt zielt darauf ab, die Art und Weise zu vereinfachen und anzuleiten, wie Anfänger ihren ersten Beitrag leisten. Wenn Sie Ihren ersten Beitrag leisten möchten, befolgen Sie die nachstehenden Schritte

_Wenn Sie mit der Befehlszeile nicht vertraut sind, [here are tutorials using GUI tools.](#tutorials-using-other-tools)_


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Wenn Sie Git nicht auf Ihrem Computer haben, [install it](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Forken Sie dieses Repository

Forken Sie dieses Repository, indem Sie auf die Fork-Schaltfläche oben auf dieser Seite klicken.
Dadurch wird eine Kopie dieses Repositorys in Ihrem Konto erstellt.

## Klonen Sie das Repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Klonen Sie nun das gegabelte Repository auf Ihren Computer. Gehen Sie zu Ihrem GitHub-Konto, öffnen Sie das Fork-Repository, klicken Sie auf die Code-Schaltfläche und dann auf das Symbol _in die Zwischenablage kopieren_.

Öffnen Sie ein Terminal und führen Sie den folgenden Git-Befehl aus:

```
git clone "URL, die du gerade kopiert hast"
```

wobei "URL, die Sie gerade kopiert haben" (ohne die Anführungszeichen) die URL zu diesem Repository (Ihr Fork dieses Projekts) ist. Sehen Sie sich die vorherigen Schritte an, um die URL zu erhalten.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Zum Beispiel:

```
git clone https://github.com/this-is-you/first-contributions.git
```

wobei `this-is-you` Ihr GitHub-Benutzername ist. Hier kopieren Sie den Inhalt des first-contributions-Repositorys auf GitHub auf Ihren Computer.

## Erstellen Sie einen Zweig

Wechseln Sie auf Ihrem Computer in das Repository-Verzeichnis (falls Sie sich noch nicht dort befinden):

```
cd first-contributions
```

Erstellen Sie nun einen Zweig mit dem Befehl `git switch`:

```
git switch -c your-new-branch-name
```

Zum Beispiel:

```
git switch -c add-alonzo-church
```

## Nehmen Sie notwendige Änderungen vor und übernehmen Sie diese Änderungen

Jetzt offen `Contributors.md` Datei in einem Texteditor, fügen Sie Ihren Namen hinzu. Fügen Sie es nicht am Anfang oder Ende der Datei hinzu. Legen Sie es irgendwo dazwischen. Speichern Sie nun die Datei.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Wenn Sie in das Projektverzeichnis gehen und den Befehl ausführen `git status`, Sie werden sehen, dass es Änderungen gibt.

Fügen Sie diese Änderungen dem Zweig hinzu, den Sie gerade erstellt haben, indem Sie die `git add` Befehl:

```
git add Contributors.md
```
Bestätigen Sie diese Änderungen nun mit der `git commit` Befehl:

```
git commit -m "Add your-name to Contributors list"
```

ersetzen `your-name` mit deinem Namen.

## Pushen Sie Änderungen an GitHub

Pushen Sie Ihre Änderungen mit dem Befehl `git push`:

```
git push -u origin your-branch-name
```

ersetzen `your-branch-name` mit dem Namen des Zweigs, den Sie zuvor erstellt haben.

<details>
<summary> <strong>If you get any errors while pushing, click here:</strong> </summary>

- ### Authentifizierungsfehler
     <pre>remote: Die Unterstützung für die Passwortauthentifizierung wurde am 13. August 2021 entfernt. Bitte verwenden Sie stattdessen ein persönliches Zugriffstoken.
  remote: Bitte sehen https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ für mehr Informationen.
  fatal: Authentifizierung fehlgeschlagen für 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Gehe zu [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) beim Generieren und Konfigurieren eines SSH-Schlüssels für Ihr Konto.

</details>

## Reichen Sie Ihre Änderungen zur Überprüfung ein

Wenn Sie auf GitHub zu Ihrem Repository gehen, sehen Sie a `Compare & pull request` Taste. Klicken Sie auf diese Schaltfläche.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Senden Sie nun den Pull-Request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Bald werde ich alle Ihre Änderungen im Hauptzweig dieses Projekts zusammenführen. Sie erhalten eine Benachrichtigungs-E-Mail, sobald die Änderungen zusammengeführt wurden.

## Wohin von hier aus?

Herzlichen Glückwunsch! Sie haben gerade den Standard abgeschlossen _fork -> clone -> edit -> pull request_ Arbeitsablauf, dem Sie als Mitwirkender oft begegnen werden!

Feiern Sie Ihren Beitrag und teilen Sie ihn mit Ihren Freunden und Followern, indem Sie auf gehen [web app](https://firstcontributions.github.io/#social-share).

Sie können unserem Slack-Team beitreten, wenn Sie Hilfe benötigen oder Fragen haben. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Beginnen wir jetzt damit, zu anderen Projekten beizutragen. Wir haben eine Liste von Projekten mit einfachen Problemen zusammengestellt, mit denen Sie beginnen können. Kasse [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Zusätzliches Material](additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials mit anderen Tools

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
