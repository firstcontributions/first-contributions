# Gitflow

Gitflow ist ein von Vincent Driessen entwickeltes Verzweigungsmodell für Git. Hier geht es um die Anforderungen und Anwendungsfälle von Gitflow.
Der Gitflow-Workflow definiert ein striktes Verzweigungsmodell, das auf die Projektveröffentlichung ausgerichtet ist und ein robustes Framework für die Verwaltung größerer Projekte bietet. Gitflow eignet sich ideal für Projekte mit einem festgelegten Veröffentlichungszyklus und für die DevOps-Best-Practice der kontinuierlichen Bereitstellung. Es weist verschiedenen Zweigen sehr spezifische Rollen zu und definiert, wie und wann sie interagieren sollen. Es verwendet einzelne Zweige für die Vorbereitung, Wartung und Aufzeichnung von Veröffentlichungen.


## Implementierung

1. **Entwicklungs- und Master-Branches**: Anstelle eines einzigen Master-Branches verwendet Git Flow zwei Branches, um die Historie des Projekts aufzuzeichnen. Es basiert auf zwei Haupt-Branches mit unbegrenzter Lebensdauer, nämlich Master und Develop:
  - **Master-Branch**: Der Master-Branch enthält den Produktionscode und speichert die offizielle Release-Historie.
  - **Develop-Branch**: Der Develop-Branch enthält den Vorproduktionscode und dient als Integrations-Branch für Features.
  - **Erstellen eines Develop-Zweigs**:<br />
    Ohne Verwendung der Gitflow-Erweiterungen:
    ```
    git branch develop
    git push -u origin develop
    ```
    Mit Verwendung der Gitflow-Erweiterungen: Bei Verwendung der Gitflow-Erweiterungsbibliothek wird durch Ausführen von `git flow init` in einem bestehenden Repository der Develop-Zweig erstellt.
    ```
    git flow init
    ```
2. **Feature-Zweig**: Jede neue Funktion sollte in einem eigenen Zweig gespeichert werden, der zur Sicherung/Zusammenarbeit in das zentrale Repository übertragen werden kann. Feature-Zweige verwenden den neuesten Entwicklungszweig als übergeordneten Zweig. Wenn eine Funktion fertiggestellt ist, wird sie wieder in den Entwicklungszweig integriert. Funktionen sollten niemals direkt mit dem Master-Zweig interagieren.
  - **Erstellen eines Feature-Zweigs**: <br />
    Ohne Gitflow-Erweiterungen:
    ```
    git checkout develop
    git checkout -b feature_branch
    ```
    Mit Gitflow-Erweiterungen:
    ```
    git flow feature start feature_branch
    ```
  - **Beenden eines Feature-Branches**: <br />
    Ohne Gitflow-Erweiterungen:
    ```
    git checkout develop
    git merge feature_branch
    ```
    Mit Gitflow-Erweiterungen:
    ```
    git flow feature finish feature_branch
    ```
3. **Release-Branch**: Sobald develop genügend Features für eine Veröffentlichung gesammelt hat (oder ein vorab festgelegter Veröffentlichungstermin näher rückt), erstellen wir einen Release-Branch aus develop. Mit der Erstellung dieses Branches beginnt der nächste Release-Zyklus, sodass ab diesem Zeitpunkt keine neuen Features mehr hinzugefügt werden können – nur Bugfixes, die Erstellung von Dokumentationen und andere release-orientierte Aufgaben sollten in diesem Branch durchgeführt werden. Der Release-Zweig kann vom Entwicklungszweig abzweigen und muss sowohl in den Master- als auch in den Entwicklungszweig integriert werden. <br />
Die Verwendung eines dedizierten Zweigs zur Vorbereitung von Releases ermöglicht es einem Team, das aktuelle Release zu optimieren, während ein anderes Team weiter an Funktionen für das nächste Release arbeitet.
  - **Erstellen eines Release-Zweigs**: <br />
    Ohne die Git-Flow-Erweiterungen:
    ```
    git checkout develop
    git checkout develop
    git checkout -b release/0.1.0
    ```
    Bei Verwendung der Git-Flow-Erweiterungen:
    ```
    git flow release start 0.1.0
    ```
    Wechsel zu einem neuen Branch „release/0.1.0”
  - **Beenden eines Release-Branches**: <br />
    Ohne Git-Flow-Erweiterungen:
    ```
    git checkout master
    git merge release/0.1.0
    ```
    Mit Git-Flow-Erweiterungen:
    ```
    git flow release finish 0.1.0
    ```
4. **Hotfix-Zweig**: Wartungs- oder „Hotfix”-Zweige werden verwendet, um Produktionsversionen schnell zu patchen. Hotfix-Zweige sind notwendig, um sofort auf einen unerwünschten Status des Master-Zweigs reagieren zu können. Hotfix-Branches ähneln Release-Branches und Feature-Branches, basieren jedoch auf dem Master statt auf dem Develop. Dies ist der einzige Branch, der direkt vom Master abzweigen sollte. Sobald die Korrektur abgeschlossen ist, sollte sie sowohl in den Master als auch in den Develop (oder den aktuellen Release-Branch) gemergt werden, und der Master-Branch sollte mit einer aktualisierten Versionsnummer getaggt werden.
  - **Erstellen eines Hotfix-Branches**: <br />
    Ohne Git-Flow-Erweiterungen:
```
git checkout master
git checkout -b hotfix_branch
```
Mit Git-Flow-Erweiterungen: 
```
git flow hotfix start hotfix_branch
```
- **Beenden eines Hotfix-Zweigs**: <br />
Ohne Git-Flow-Erweiterungen:
```
    git checkout master
    git merge hotfix_branch
    git checkout develop
    git merge hotfix_branch
    ```
    Mit Git-Flow-Erweiterungen:
    ```
    git branch -D hotfix_branch
    git flow hotfix finish hotfix_branch
    ```


## Vorteile

- Gewährleistet einen sauberen Zustand der Branches zu jedem Zeitpunkt im Lebenszyklus eines Projekts.
- Die Namenskonvention für Branches folgt einem systematischen Muster, wodurch sie leichter zu verstehen sind.
- Verfügt über Erweiterungen und Unterstützung für die meisten verwendeten Git-Tools.
- Ideal für die Verwaltung mehrerer Versionen in der Produktion.
- Hervorragend geeignet für einen release-basierten Software-Workflow.
- Bietet einen dedizierten Kanal für Hotfixes für die Produktion.
