[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Erste Beiträge

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub-Befehlszeilenschnittstelle (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |

Dies ist ein Leitfaden für alle, die lieber mit dem Terminal arbeiten. Wenn Sie zum ersten Mal etwas tun, ist es immer schwierig. Besonders wenn Sie zusammenarbeiten, ist es nicht leicht, Fehler zu machen. Aber Open Source bedeutet Zusammenarbeit und gemeinsames Arbeiten. Wir wollten den Prozess der ersten Beitragstellung für neue Open-Source-Mitwirkende vereinfachen und ihnen helfen, sie auf einfache Weise zu lernen.

Das Lesen von Artikeln und Anschauen von Tutorials kann hilfreich sein, aber es gibt nichts Besseres, als tatsächlich zu arbeiten, ohne etwas zu vermasseln. Dieses Projekt zielt darauf ab, Orientierung zu geben und die Art zu vereinfachen, wie Anfänger ihren ersten Beitrag leisten. Denken Sie daran: Je entspannter Sie sind, desto besser werden Sie lernen. Wenn Sie Ihren ersten Beitrag leisten möchten, folgen Sie einfach den folgenden einfachen Schritten. Wir versprechen Ihnen, das wird Spaß machen.

Der erste Voraussetzung ist:

- Git installiert ([Git herunterladen](https://git-scm.com/downloads))
- GitHub-Konto

Jetzt müssen wir das `github-cli`-Tool auf unserem System installieren – folgen Sie der offiziellen Dokumentation.

Danach müssen wir uns über die CLI anmelden. Geben Sie diesen Befehl ein:

```bash
gh auth login
```

Folgen Sie den Anweisungen und schon sind wir bereit!

# Dieses Repository forken

Dies ist ganz einfach mit diesem Befehl:

```bash
gh repo fork firstcontributions/first-contributions
```

**WICHTIG: Es wird Sie fragen, ob Sie das Repository auch klonen möchten, wählen Sie "Ja"**

# Erstellen Sie Ihren Branch

Wir machen diesen Schritt mit `git`. Geben Sie diesen Befehl ein und ersetzen Sie ihn durch Ihren Namen. Zum Beispiel: (Ersetzen Sie john-doe durch Ihren Namen)

```bash
git switch -c add-john-doe
```

# Nehmen Sie erforderliche Änderungen vor und führen Sie diese durch

Öffnen Sie jetzt die `Contributors.md`-Datei in einem Texteditor und fügen Sie Ihren Namen hinzu. Platzieren Sie Ihren Namen zwischen den bestehenden Namen, speichern Sie die Datei dann.

Führen Sie `git status` in Ihrem Projektverzeichnis aus und Sie werden die Änderungen sehen.

Fügen Sie diese Änderungen mit dem `git add`-Befehl zu dem von Ihnen erstellten Branch hinzu:
`git add Contributors.md`

Begehen Sie diese Änderungen nun mit dem `git commit`-Befehl: `git commit -m "Add your-name to Contributors list"`. Ersetzen Sie `your-name` durch Ihren Namen.

# Schieben Sie Änderungen zu GitHub

Verwenden Sie den `git push`-Befehl, um Ihre Änderungen zu übertragen:

```bash
git push origin -u your-branch-name
```

Ersetzen Sie `your-branch-name` durch den Namen des Branches, den Sie zuvor erstellt haben.

<details><summary><strong>Wenn Sie beim Verschieben Fehler bekommen, klicken Sie hier:</strong></summary></details>

- ### Authentifizierungsfehler
        Remote: Die Unterstützung für Passwortauthentifizierung wurde am 13. August 2021 entfernt. Verwenden Sie stattdessen bitte ein Personal Access Token. Remote: Weitere Informationen finden Sie unter https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/. Fatal: Authentifizierung für 'https://github.com//first-contrib.git/' fehlgeschlagen
  [GitHub-Anleitung zum Erstellen und Konfigurieren eines SSH-Schlüssels für Ihr Konto](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

# Reichen Sie Ihre Änderungen zur Überprüfung ein

Nun können Sie diesen Befehl in unserem Repository-Verzeichnis ausführen, um eine Pull-Anfrage zur Überprüfung zu erstellen:

```bash
gh pr create --repo firstcontributions/first-contributions
```

Danach reichen Sie die Pull-Anfrage ein.

Sie können den `gh status`-Befehl verwenden, um Ihren erwähnten Pull-Request in Aktion zu sehen.

## Wohin von hier?

Herzlichen Glückwunsch! Sie haben gerade den Standard-Workflow Fork -> Clone -> Bearbeiten -> Pull-Anfrage abgeschlossen, dem Sie häufig als Mitwirkender begegnen werden!

Feiern Sie Ihren Beitrag und teilen Sie ihn mit Ihren Freunden und Followern, indem Sie die [Web-App](https://firstcontributions.github.io/#social-share) besuchen.

Wenn Sie Hilfe benötigen oder Fragen haben, können Sie unserem Slack-Team beitreten. [Treten Sie dem Slack-Team bei](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

Jetzt können wir mit dem Beitrag zu anderen Projekten beginnen. Wir haben eine Liste von Projekten mit einfachen Problemen zusammengestellt, mit denen Sie anfangen können. [Sehen Sie sich die Liste der Projekte in der Web-App an](https://firstcontributions.github.io/#project-list).

### [Zusätzliches Material](additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials mit anderen Tools

[Zurück zur Hauptseite](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)

