# Halten Sie Ihren Fork mit diesem Repository synchronisiert

Zunächst einmal ist es wichtig, den Ablauf einer vollständigen Synchronisierung zu verstehen. In diesem Schema gibt es drei verschiedene Repositorys: mein öffentliches Repository auf GitHub `github.com/firstcontributions/first-contributions.git`, Ihr Fork des Repositorys auf GitHub `github.com/Ihr-Name/first-contributions/` und das Repository auf Ihrem lokalen Rechner, von dem aus Sie arbeiten sollen. Diese Art der Zusammenarbeit ist typisch für Open-Source-Projekte und wird als „Triangle Workflows“ bezeichnet.

<img style="float;" src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

Um Ihre beiden Repos auf dem neuesten Stand meines öffentlichen Repos zu halten, müssen wir zunächst das öffentliche Repo abrufen und mit dem Repo Ihres lokalen Rechners zusammenführen.
Unser zweiter Schritt besteht darin, Ihr lokales Repo in Ihren GitHub-Fork zu übertragen. Wie Sie bereits gesehen haben, können Sie nur von Ihrem Fork aus einen „Pull Request“ anfordern. Ihr GitHub-Fork ist also das letzte Repo, das aktualisiert werden muss.

Sehen wir uns nun an, wie das funktioniert:

Zunächst müssen Sie sich in Ihrem Hauptzweig befinden. Um zu erfahren, in welchem Zweig Sie sich befinden, überprüfen Sie die erste Zeile von:
```
git status
```
Wenn Sie sich noch nicht auf dem Hauptzweig befinden:
```
git checkout main
```

Dann sollten Sie mein öffentliches Repo mit `add upstream remote-url` zu Ihrem Git hinzufügen:
```
git remote add upstream https://github.com/firstcontributions/first-contributions.git
```
Auf diese Weise teilen Sie Git mit, dass eine andere Version dieses Projekts unter der angegebenen URL existiert und wir sie „upstream“ nennen. Sobald Ihr Git einen Namen hat, holen wir uns die neueste Version des öffentlichen Repositorys:
```
git fetch upstream
```

Sie haben gerade die neueste Version meines Forks (Remote „upstream“) abgerufen. Jetzt müssen Sie das öffentliche Repository in Ihren Hauptzweig einbinden.
```
git rebase upstream/main
```
Hier führen Sie das öffentliche Repository mit Ihrem Hauptzweig zusammen. Der Hauptzweig Ihres lokalen Rechners ist nun auf dem neuesten Stand. Wenn Sie schließlich Ihren Hauptzweig in Ihren Fork übertragen, werden die Änderungen auch in Ihrem GitHub-Fork übernommen:
```
git push origin main
```
Beachten Sie, dass Sie hier in den Remote namens „origin” übertragen.

Wenn Sie die neuesten Änderungen meines Forks (Remote „upstream”) gleichzeitig in Ihren lokalen Branch holen und zusammenführen möchten, können Sie direkt Folgendes ausführen:
```
git pull upstream main
```

Jetzt sind alle Ihre Repositorys auf dem neuesten Stand. Gut gemacht! Sie sollten dies jedes Mal tun, wenn Ihr GitHub-Repo Ihnen mitteilt, dass Sie ein paar Commits im Rückstand sind.