# Halte dein fork mit dem repository synchronisiert

Zuerst sollte der Ablauf für eine vollständige Synchronisation verstanden werden. In diesem Schema gibt es drei verschiedene repositories: 

1. Das öffentliche repository auf GitHub:
`github.com/firstcontributions/first-contributions.git`.

2. Dein fork dieses repositories auf GitHub:
`github.com/Your-Name/first-contributions/`

3. Dein lokales repository, mit welchem du sehr wahrscheinlich arbeiten wirst. 

Diese Art der Zusammenarbeit ist typisch für open source Projekte und wird als "Triangle Workflows" bezeichnet.

<img style="float;" src="../../assets/triangle_workflow.png" alt="triangle workflow" />

Um deine beiden repositories mit meinem öffentlichen repository auf dem neuesten Stand zu bringen, müssen wir zuerst das öffentliche mit dem lokalen fetchen und zusammenführen.

Unser zweiter Schritt wird darin bestehen, dein lokales repository auf deine GitHub fork zu übertragen. Wie du bereits gesehen hast, kannst du nur von deiner fork aus ein pull request stellen. Deine GitHub fork ist also das letzte repository, welches aktualisiert wird.

Zuerst musst du dich in deinem master branch befinden. Dies kannst du folgendermaßen überprüfen:

```
git status
```

Falls du dich nicht bereits in der master branch befindest:

```
git checkout master
```

Nun fügst du das öffentliche repository mit `add upstream remote-url` hinzu:

```
git remote add upstream https://github.com/firstcontributions/first-contributions.git
```

Somit teilen wir Git mit, dass eine andere Version dieses Projekts in der angegebenen URL existiert, was sich `upstream` nennt. Sobald dein Git einen Namen hat, fetchen wir die neueste Version des öffentlichen repositories:

```
git fetch upstream
```

Nun hast du die aktuellste Version des fork gefetcht (`upstream` remote). Als nächstes führst du das öffentliche repository mit dem master branch zusammen:

```
git rebase upstream/master
```

Dein lokaler master branch ist nun auf dem neuesten Stand. Sobald du dein master branch in dein fork pusht, werden diese Änderungen in GitHub ebenfalls verfügbar sein:

```
git push origin master
```

Achte darauf, dass du es in das remote namens `origin` pusht.

Jetzt sind all deine repositories auf dem neuesten Stand. Gut gemacht! Führe diese Schritte aus, sobald dein GitHub repository dir mitteilt, dass du ein paar commits hinten liegst.