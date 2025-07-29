[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Erste Beiträge

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Repository forken" />

Aller Anfang ist schwer. Gerade dann, wenn wir gemeinsam an etwas arbeiten, will niemand etwas Falsches tun. Aber Open Source dreht sich um Kooperation und lebt von den Beiträgen vieler Freiwilliger. Deshalb haben wir es uns zur Aufgabe gemacht, neuen Mitgliedern in der Open-Source-Gemeinde ihre ersten Schritte so einfach wie möglich zu machen.

Natürlich helfen die vorhandenen Artikel und Videoanleitungen. Aber was kann besser sein, als es einfach einmal auszuprobieren mit dem Wissen, dass man nichts kaputt machen kann? Dieses Projekt will Anfängern zeigen, wie sie möglichst einfach ihren ersten Beitrag leisten. Bedenke: Je entspannter du bist, desto besser lernst du. Wenn du deinen ersten Beitrag leisten möchtest, folge diesen einfachen Schritten. Wir versprechen dir, es wird Spaß machen.

Wenn du Git noch nicht installiert hast, [installiere es](https://help.github.com/articles/set-up-git/)

## Repository forken

Forke das Repository durch das Anklicken der Schaltfläche "Fork". Dadurch erhältst du deine eigene Version des Projektes in deinem Profil.

## Repository klonen

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Repository klonen" />

Klone das Repository auf deinen Computer. Klicke auf die Schaltfläche "Clone or download" und anschließend auf das "copy to clipboard"-Symbol.

Öffne eine Kommandozeile und gib den folgenden git-Befehl ein:

```
git clone "Deine kopierte URL"
```

Statt 'Deine kopierte URL' (ohne Anführungszeichen) füge die Repository-URL aus dem vorherigen Schritt ein.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL kopieren" />

Beispiel:

```
git clone https://github.com/dein-Name/first-contributions.git
```

An der Stelle 'dein-Name' muss dein GitHub-Nutzername stehen. Mit diesem Befehl kopierst du den Inhalt deines first-contributions-Repository von GitHub auf deinen Computer.

## Erstelle einen Branch

Wechsle zum Repository-Verzeichnis auf deinem Computer (falls du es nicht schon getan hast).

```
cd first-contributions
```

Erstelle nun einen Branch mit dem Befehl `git checkout`:

```
git checkout -b <add-dein-Name>
```

Beispiel:

```
git checkout -b add-max-mustermann
```

(Der Name des Branches muss nicht unbedingt das Wort _add_ beinhalten aber hier ist es sinnvoll, denn der Zweck deines Branches ist es ja, deinen Namen zur Liste hinzuzufügen.)

## Mache die nötigen Änderungen und committe sie

Öffne `Contributors.md` in einem Text-Editor und füge deine Namen hinzu. Beachte, dass du den Namen nicht am Anfang oder am Ende der Datei hinzufügst. Speichere die Datei anschließend.

Gibst du in der Kommandozeile nun `git status` ein, siehst du die Änderungen.

Füge die Änderungen mit dem Befehl `git add` zu deinem eben erstellten Branch hinzu:

```
git add Contributors.md
```

Nun committest du deine Änderungen mit `git commit`:

```
git commit -m "Add <dein-Name> to Contributors list"
```

Ersetze `<dein-Name>` mit deinem Namen.

## Pushe die Änderung zu GitHub

Pushe die Änderungen mit `git push`:

```
git push origin <add-dein-Name>
```

Ersetze `<add-dein-Name>` mit dem Namen des Branches, den du zuvor erstellt hast.

## Sende deine Änderungen zum Review

Wenn du jetzt zu deinem Repository auf GitHub gehst, siehst du einen Knopf `Compare & pull request`. Klicke darauf.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Erstelle einen pull request" />

Erstelle einen Pull Request indem du auf die Schaltfläche `Create pull request` klickst.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Pull Request senden" />

Roshan Jossey wird nun deine Änderungen in den Master Branch dieses Projekts mergen. Du erhältst eine E-Mail, sobald dies geschehen ist.

## Wie geht es weiter?

Glückwunsch! Du hast so eben den Standard-Workflow _Fork -> Clone -> Edit -> Pull Request_ beendet, der dir als Mitwirkender häufig begegnen wird.

Feiere deinen Beitrag zum Projekt und teile ihn mit deinen Freunden und Followern über unsere [Web-App](https://firstcontributions.github.io/#social-share).

Wenn Du noch mehr üben möchtest, schau Dir das [Code-Contributions Repository](https://github.com/roshanjossey/code-contributions) an.
Falls du jetzt zu anderen Projekten beitragen möchtest, dann haben wir für dich eine Liste von einfachen, ersten Issues zusammengestellt, an denen du arbeiten kannst. Diese Projekt-Liste findest du [in unserer Web-App](https://firstcontributions.github.io/#project-list).

## Tutorials mit anderen Tools

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
