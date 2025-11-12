[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![Lizenz: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Erste Beiträge

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub-Befehlszeilenschnittstelle (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |

Es ist schwierig. Wenn Sie zum ersten Mal etwas tun, ist es immer schwierig. Besonders wenn Sie zusammenarbeiten, ist es nicht leicht, Fehler zu machen. Aber Open Source bedeutet Zusammenarbeit und gemeinsames Arbeiten. Wir wollten den Prozess der ersten Beitragstellung für neue Open-Source-Mitwirkende vereinfachen und ihnen helfen, sie auf einfache Weise zu lernen.Dies ist ein Leitfaden für alle, die lieber mit dem Terminal arbeiten. Dank [GitHub-CLI](https://cli.github.com/) kannst du alles direkt über die Kommandozeile erledigen. Denk daran: Dein erster Beitrag soll Spaß machen, lohnend sein und dich motivieren, weiterzumachen!



Das Lesen von Artikeln und Anschauen von Tutorials kann hilfreich sein, aber es gibt nichts Besseres, als tatsächlich zu arbeiten, ohne etwas zu vermasseln. Dieses Projekt zielt darauf ab, Orientierung zu geben und die Art zu vereinfachen, wie Anfänger ihren ersten Beitrag leisten. Denken Sie daran: Je entspannter Sie sind, desto besser werden Sie lernen. Wenn Sie Ihren ersten Beitrag leisten möchten, folgen Sie einfach den folgenden einfachen Schritten. Wir versprechen Ihnen, das wird Spaß machen.Diese Anleitung ist etwas anspruchsvoller, da wir keine grafische Benutzeroberfläche verwenden – aber sie ist trotzdem spannend und leicht nachvollziehbar!



Wenn Sie Git Bash auf Ihrem Windows-Computer nicht haben, [installieren Sie es](https://git-scm.com/download/win).Die Voraussetzungen sind:



<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />- Git installiert ([Git herunterladen](https://git-scm.com/downloads))

- Ein GitHub-Konto

## Dieses Repository forken

Jetzt müssen wir das `github-cli`-Tool auf unserem System installieren – folge dazu der offiziellen Dokumentation.

Forken Sie dieses Repository, indem Sie auf die Fork-Schaltfläche oben rechts auf dieser Seite klicken.

Dies erstellt eine Kopie dieses Repositories in Ihrem Konto.Anschließend müssen wir uns über die CLI anmelden. Gib diesen Befehl ein:



## Repository klonen```bash

gh auth login

Klonen Sie dieses Repository jetzt auf Ihren Computer.Folge den Anweisungen – und schon bist du bereit!



WICHTIG: Klonen Sie NICHT das Originalrepository. Gehen Sie zu Ihrer Fork und klonen Sie das.Dieses Repository forken

Das geht ganz einfach mit diesem Befehl:

Um das Repository zu klonen, klicken Sie auf "Code" und kopieren Sie dann die Zeichenkette unten.

bash

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />Copy code

gh repo fork firstcontributions/first-contributions

Öffnen Sie die Git Bash-Anwendung, die Sie gerade heruntergeladen haben. Auf einem Windows-Computer sieht es ungefähr so aus:Wichtig: Es wird dich fragen, ob du das Repository auch klonen möchtest – wähle „Ja“.



<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />Einen neuen Branch erstellen

Diesen Schritt machen wir mit git. Ersetze den Platzhalter mit deinem Namen, zum Beispiel: (ersetze „john-doe“ mit deinem Namen)

Navigieren Sie mithilfe dieses Befehls zu dem Ordner, in dem Sie dieses Projekt speichern möchten

bash

`cd <folder>`Copy code

git switch -c add-john-doe

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />Notwendige Änderungen vornehmen und committen

Öffne nun die Datei Contributors.md in deinem Texteditor und füge deinen Namen hinzu – irgendwo zwischen den vorhandenen Namen. Speichere die Datei anschließend.

Klonen Sie das Repository mit der Zeichenkette, die Sie im obigen Schritt kopiert haben, mit diesem Befehl

Führe in deinem Projektverzeichnis den Befehl git status aus, um die Änderungen zu sehen.

`git clone <repo-url>`

Füge deine Änderungen mit dem folgenden Befehl zur erstellten Branch hinzu:

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

bash

Gehen Sie zu dem Verzeichnis, in dem sich das Repository befindet, und öffnen Sie es in VS Code, um Ihre Änderungen vorzunehmen.Copy code

git add Contributors.md

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />Dann committe die Änderungen mit:



## Erstellen Sie einen Branchbash

Copy code

Erstellen Sie jetzt einen Branch mit diesem einfachen Befehl. Dieser Befehl erstellt nicht nur einen Branch für Sie, sondern hilft Ihnen auch, zu diesem Branch zu wechseln.git commit -m "Add your-name to Contributors list"

Ersetze your-name durch deinen tatsächlichen Namen.

```

git checkout -b <branch-name>Änderungen zu GitHub pushen

```Nutze diesen Befehl, um deine Änderungen zu pushen:



Geben Sie Ihrem Branch den Namen `<add-your-name>`. Zum Beispiel "add-james-smith"bash

Copy code

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="create a branch" />git push origin -u your-branch-name

Ersetze your-branch-name mit dem Namen deines Branches, den du zuvor erstellt hast.

## Nehmen Sie die erforderlichen Änderungen vor und übernehmen Sie diese

<details><summary><strong>Wenn du beim Pushen Fehler bekommst, klicke hier:</strong></summary></details>

Öffnen Sie jetzt die Datei `Contributors.md` in einem Texteditor, scrollen Sie zum Ende der Seite und fügen Sie Ihren Namen hinzu, speichern Sie dann die Datei.Authentifizierungsfehler

yaml

Beispiel: Wenn Ihr Name James Smith ist, sollte es wie folgt aussehen.Copy code

remote: Die Unterstützung für Passwortauthentifizierung wurde am 13. August 2021 entfernt.

[James Smith](https://github.com/jamessmith)Bitte verwende stattdessen ein Personal Access Token.

Weitere Informationen: https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/

Sie können sehen, dass Änderungen an Contributors.md vorgenommen wurden, indem Sie einfach diesen Befehl ausführenfatal: Authentifizierung für 'https://github.com//first-contrib.git/' fehlgeschlagen

👉 Lies GitHubs Anleitung zum Erstellen und Konfigurieren eines SSH-Schlüssels.

`git status`

Deine Änderungen zur Überprüfung einreichen

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="check the status" />Mit diesem Befehl in deinem Repository-Verzeichnis kannst du eine Pull Request erstellen:



Übernehmen Sie diese Änderungen jetzt:bash

Copy code

Fügen Sie zuerst die von Ihnen vorgenommenen Änderungen zum Staging-Bereich hinzugh pr create --repo firstcontributions/first-contributions

Danach sende die Pull Request ab.

`git add file-name`

Um den Status deiner PR zu prüfen, kannst du den Befehl gh status verwenden.

Schreiben Sie dann eine Commit-Nachricht mit diesem Befehl

Wie geht es weiter?

`git commit -m "Add your-name to Contributors list"`🎉 Herzlichen Glückwunsch! Du hast gerade den vollständigen Workflow „Fork -> Clone -> Edit -> Pull Request“ abgeschlossen – genau den, den du oft als Open-Source-Mitwirkender verwenden wirst!



Ersetzen Sie `<your-name>` durch Ihren Namen.Feiere deinen Beitrag und teile ihn mit deinen Freunden und Followern über die Web-App.



<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit changes" />Wenn du Hilfe brauchst oder Fragen hast, tritt unserem Slack-Team bei:

Slack-Team beitreten

Um zu sehen, ob Ihr Commit durchgeführt wurde, können Sie einen einfachen `git log --oneline` Befehl ausführen.

Jetzt kannst du mit dem Beitragen zu anderen Projekten beginnen!

## Übermitteln Sie Ihre Änderungen an githubWir haben eine Liste einfacher Projekte zusammengestellt, mit denen du starten kannst:

Sieh dir die Projektliste in der Web-App an

Sobald Sie die obigen Schritte abgeschlossen haben, können Sie Ihre Änderungen mit diesem Befehl übertragen

Zusätzliches Material

`git push origin <branch-name>`Tutorials mit anderen Tools

Zurück zur Hauptseite

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-push.png" alt="push changes" />


## Übermitteln Sie Ihre Änderungen zur Überprüfung

Wenn Sie zu Ihrem Repository auf GitHub gehen, sehen Sie eine Schaltfläche `Compare & pull request`. Klicken Sie auf diese Schaltfläche.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

Übermitteln Sie jetzt die Pull-Anfrage.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

Bald werde ich alle Ihre Änderungen mit dem Hauptbranch dieses Projekts zusammenführen. Sie erhalten eine Benachrichtigungs-E-Mail, sobald die Änderungen zusammengeführt werden.

## Wo geht es von hier aus weiter?

Herzlichen Glückwunsch! Sie haben gerade den Standard-Workflow _fork -> clone -> edit -> PR_ abgeschlossen, dem Sie als Mitwirkender häufig begegnen werden!

Feiern Sie Ihren Beitrag und teilen Sie ihn mit Ihren Freunden und Followern, indem Sie zur [Web-App](https://firstcontributions.github.io#social-share) gehen.

Wenn Sie Hilfe benötigen oder Fragen haben, können Sie unserem Slack-Team beitreten. [Treten Sie dem Slack-Team bei](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

### [Zusätzliches Material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials mit anderen Tools
[Zurück zur Hauptseite](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)

Zusätzliches Material
Tutorials mit anderen Tools
[Zurück zur Hauptseite](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)

