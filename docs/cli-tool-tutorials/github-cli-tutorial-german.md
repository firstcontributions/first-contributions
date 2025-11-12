[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![Lizenz: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Erste Beiträge

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub-Befehlszeilenschnittstelle (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |

Dies ist ein Leitfaden für alle, die lieber mit dem Terminal arbeiten. Dank [GitHub-CLI](https://cli.github.com/) kannst du alles direkt über die Kommandozeile erledigen. Denk daran: Dein erster Beitrag soll Spaß machen, lohnend sein und dich motivieren, weiterzumachen!

Diese Anleitung ist etwas anspruchsvoller, da wir keine grafische Benutzeroberfläche verwenden – aber sie ist trotzdem spannend und leicht nachvollziehbar!

Die Voraussetzungen sind:

- Git installiert ([Git herunterladen](https://git-scm.com/downloads))
- Ein GitHub-Konto

Jetzt müssen wir das `github-cli`-Tool auf unserem System installieren – folge dazu der offiziellen Dokumentation.

Anschließend müssen wir uns über die CLI anmelden. Gib diesen Befehl ein:

```bash
gh auth login
Folge den Anweisungen – und schon bist du bereit!

Dieses Repository forken
Das geht ganz einfach mit diesem Befehl:

bash
Copy code
gh repo fork firstcontributions/first-contributions
Wichtig: Es wird dich fragen, ob du das Repository auch klonen möchtest – wähle „Ja“.

Einen neuen Branch erstellen
Diesen Schritt machen wir mit git. Ersetze den Platzhalter mit deinem Namen, zum Beispiel: (ersetze „john-doe“ mit deinem Namen)

bash
Copy code
git switch -c add-john-doe
Notwendige Änderungen vornehmen und committen
Öffne nun die Datei Contributors.md in deinem Texteditor und füge deinen Namen hinzu – irgendwo zwischen den vorhandenen Namen. Speichere die Datei anschließend.

Führe in deinem Projektverzeichnis den Befehl git status aus, um die Änderungen zu sehen.

Füge deine Änderungen mit dem folgenden Befehl zur erstellten Branch hinzu:

bash
Copy code
git add Contributors.md
Dann committe die Änderungen mit:

bash
Copy code
git commit -m "Add your-name to Contributors list"
Ersetze your-name durch deinen tatsächlichen Namen.

Änderungen zu GitHub pushen
Nutze diesen Befehl, um deine Änderungen zu pushen:

bash
Copy code
git push origin -u your-branch-name
Ersetze your-branch-name mit dem Namen deines Branches, den du zuvor erstellt hast.

<details><summary><strong>Wenn du beim Pushen Fehler bekommst, klicke hier:</strong></summary></details>
Authentifizierungsfehler
yaml
Copy code
remote: Die Unterstützung für Passwortauthentifizierung wurde am 13. August 2021 entfernt.
Bitte verwende stattdessen ein Personal Access Token.
Weitere Informationen: https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/
fatal: Authentifizierung für 'https://github.com//first-contrib.git/' fehlgeschlagen
👉 Lies GitHubs Anleitung zum Erstellen und Konfigurieren eines SSH-Schlüssels.

Deine Änderungen zur Überprüfung einreichen
Mit diesem Befehl in deinem Repository-Verzeichnis kannst du eine Pull Request erstellen:

bash
Copy code
gh pr create --repo firstcontributions/first-contributions
Danach sende die Pull Request ab.

Um den Status deiner PR zu prüfen, kannst du den Befehl gh status verwenden.

Wie geht es weiter?
🎉 Herzlichen Glückwunsch! Du hast gerade den vollständigen Workflow „Fork -> Clone -> Edit -> Pull Request“ abgeschlossen – genau den, den du oft als Open-Source-Mitwirkender verwenden wirst!

Feiere deinen Beitrag und teile ihn mit deinen Freunden und Followern über die Web-App.

Wenn du Hilfe brauchst oder Fragen hast, tritt unserem Slack-Team bei:
Slack-Team beitreten

Jetzt kannst du mit dem Beitragen zu anderen Projekten beginnen!
Wir haben eine Liste einfacher Projekte zusammengestellt, mit denen du starten kannst:
Sieh dir die Projektliste in der Web-App an

Zusätzliches Material
Tutorials mit anderen Tools
Zurück zur Hauptseite

