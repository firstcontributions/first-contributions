[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Erste Beiträge

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


Es ist schwer. Es ist immer schwer, wenn man etwas zum ersten Mal macht. Vor allem, wenn man mit anderen zusammenarbeitet, ist es nicht angenehm, Fehler zu machen. Aber bei Open Source geht es gerade um Zusammenarbeit und gemeinsames Arbeiten. Wir wollten neuen Open-Source-Mitwirkenden den Einstieg erleichtern, damit sie lernen und zum ersten Mal einen Beitrag leisten können.

Das Lesen von Artikeln und das Anschauen von Tutorials kann hilfreich sein, aber nichts ist besser, als die Dinge einfach auszuprobieren, ohne etwas zu vermasseln. Dieses Projekt zielt darauf ab, Anfängern eine Anleitung zu bieten und ihnen den Weg zu ihrem ersten Beitrag zu erleichtern. Denke daran: Je entspannter Du bist, desto besser lernst Du. Wenn Du Deinen ersten Beitrag leisten möchtest, folge einfach den folgenden einfachen Schritten. Wir versprechen Dir, es wird Spaß machen.

Wenn du Visual Studio Code nicht auf deinem Computer installiert hast, [installiere es jetzt.](https://code.visualstudio.com/download).

**Anmerkung:** Dieses Tutorial wurde mit Visual Studio Code (Version 1.27.2) auf einem Windows 10-Rechner erstellt. Später in diesem Tutorial werden wir einige Tastaturkürzel verwenden. Diese können sich je nach Betriebssystem (macOS/Linux) und Tastatursprache (UK, DE usw.) unterscheiden. Du kannst Deine Liste der Tastaturkürzel durchsuchen, indem Du in der Befehlspalette nach „shortcut” suchst.

## Dieses Repository forken

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Forke dieses Repository, indem Du oben rechts auf dieser Seite auf die Schaltfläche „Fork“ klickst. Dadurch wird eine Kopie dieses Repositorys in Ihrem GitHub-Konto erstellt.

GitHub verfolgt die Beziehung zwischen Ihrem Repository und dem Repository, von dem Sie es geforkt haben. Sie können sich Ihr Repository als Arbeitskopie vorstellen.

Die meisten Top-Level-Repositorys auf GitHub (d. h. solche, die nicht von einem anderen Repository geforkt wurden) haben ein kleines Kernteam von Personen, welche Änderungen direkt committen können. Alle anderen Mitwirkenden müssen das Repo forken und Änderungen im Fork vornehmen, dann einen Pull Request erstellen, um zu beantragen, dass ihre Änderungen wieder in das Top-Level-Repo übernommen werden. Wenn dem Administrator des Top-Level-Repos die Änderungen gefallen, werden sie übernommen und Du wirst sofort berühmt und reich! Mehr dazu später.

## Das Repository klonen

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Der nächste Schritt besteht darin, Dein Repository auf Deinen Computer zu klonen, damit Du Änderungen vornehmen kannst. VS Code benötigt die URL Deines Repositories, also klicke auf die Schaltfläche „Code“ und dann auf das Symbol „In die Zwischenablage kopieren“.

**ACHTUNG:** Ein Fehler, den neue Mitwirkende oft machen, ist, dass sie das Repository, von dem sie geforkt haben klonen an Stelle ihres eigenen. Überprüfe die Adressleiste Deines Browsers und stelle sicher, dass Du Dein Repository klonst.

Öffne nun Visual Studio Code. Die Willkommensseite von VS Code wird angezeigt. Drücke `F1`, um die Leiste zu öffnen, die unten gezeigt wird. Beachte, dass bereits ein `>` (größer als) Zeichen im Textfeld steht. Du kannst auch über `CTRL-P` zum Eingabeaufforderung gelangen und das `>`-Zeichen eingeben.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

Vielleicht bemerkst Du, dass bereits einige obskure Befehle aufgelistet sind. Das sind meine zuletzt verwendeten Befehle. Also kümmere Dich nicht darum.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

Nun tippe `git clone`, nur `git` oder `clone` (es funktioniert wie eine Suche).
Wähle den Eintrag `Git: Clone` aus und drücke `Enter`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

Füge die URL Deines Repositories ein und drücke `Enter`. Dadurch wird der Datei-Explorer geöffnet, in dem Du auswählen kannst, wo das Git-Repository gespeichert werden soll.

**Wichtig**: Achte darauf, dass es sich um das geforkte Repository handelt und nicht um das Original, da es sonst nicht funktioniert.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

Du solltest eine Statusmeldung in der unteren rechten Ecke von Visual Studio Code sehen. Nachdem der Vorgang abgeschlossen ist, kannst Du das geklonte Repository (jetzt ein Ordner auf Deinem Computer) mit den Schaltflächen im Dialogfeld öffnen.

## Erstelle einen Branch

Öffne die Befehls-Palette erneut, indem Du `F1` drückst. Tippe `branch` ein und wähle den Befehl `create branch` aus. Im nächsten Schritt gib den Namen Deines neuen Branches ein, zum Beispiel `add-david-kroell`. Drücke `Enter`, um den Branch zu erstellen. Der Branch ist auch bereits ausgecheckt. [Was bedeutet checkout?](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## Nötige Änderungen vornehmen

Öffne `Contributors.md` in einem Texteditor und füge Deinen Namen hinzu. Achte darauf, dass Du den Namen nicht am Anfang oder am Ende der Datei hinzufügst. Speichere die Datei anschließend.
Diese Datei enthält GFM (GitHub Flavored Markdown), eine proprietäre Variante der <a href="https://en.wikipedia.org/wiki/Markdown">Markdown-Syntax</a>.

Kopiere eine der anderen Mitwirkenden-Zeilen und passe sie mit Deinem Namen an, um sicherzustellen, dass die Syntax korrekt ist - sie kann schwierig sein. Speichere die Datei, um die Änderung zu registrieren.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## Änderungen committen und zu GitHub pushen

Auf der linken Seite von VS Code befindet sich ein Menü mit 5 Symbolen. Wähle das Versionskontroll-/Quellcodeverwaltungssymbol aus.
(Shortcut: `Ctrl + Shift + G`)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

Der Datei-Explorer zeigt alle Dateien an, die seit dem letzten Commit geändert wurden. Wenn Du mit der Maus über die Dateien fährst und auf das `+` (Plus) klickst, werden die Dateien zum Staging hinzugefügt.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

Tippe etwas in die Zeile oben im Explorer und drücke das Häkchen. Die Änderungen sind jetzt in Deiner lokalen Kopie committed. Jetzt müssen die Änderungen zurück zu GitHub gepusht werden.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

Klicke auf das Drei-Punkte-Symbol, um das Menü zu öffnen, in dem Du die Option `Publish Branch` auswählst. Dadurch sollte ein Dialogfeld geöffnet werden, in dem Du Deine GitHub-Anmeldeinformationen eingeben kannst.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## Änderungen zur Überprüfung absenden

An diesem Punkt hast Du Deine Änderung abgeschlossen, aber sie befindet sich noch nur in Deinem Repository. Dieser Schritt zeigt Dir, wie Du eine Anfrage an den Administrator des Top-Level-Repos stellen kannst, um Deine Änderung zusammenzuführen.

In Deinem Repository auf GitHub siehst Du neben der Benachrichtigung über den neuen Branch die Schaltfläche `Compare & pull request`. Klicke auf diese Schaltfläche.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sende jetzt den Pull Request ab.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Ich werde nun Deine Änderungen in den Master-Branch dieses Projekts mergen. Du erhältst eine E-Mail, sobald dies geschehen ist.

## Und jetzt?

Herzlichen Glückwunsch! Du hast gerade den Standard-Workflow _fork -> clone -> edit -> PR_ abgeschlossen, den Du als Contributor häufig antreffen wirst!

Feiere Deinen Beitrag zum Projekt und teile ihn mit Deinen Freunden und Followern über unsere [Web-App](https://firstcontributions.github.io#social-share).

Du kannst dem Slack-Team beitreten, falls Du Hilfe benötigst oder Fragen hast. [Slack-Team beitreten](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Weiterführende Materialien](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials mit anderen Tools
[Zurück zur Hauptseite](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
