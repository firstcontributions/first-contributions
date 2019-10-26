# Verschieben eines commits in eine andere branch
Was wäre, wenn du ein commit änderst und feststellst, dass du dich in einer anderen branch befindest?
Wie kannst du das ändern? Darum geht es in diesem tutorial.

## 1. Verschieben des aktuellsten commits in eine existierende branch

Dafür musst du folgendes machen:

* ```git reset HEAD~ --soft``` - Macht das letzte commit rückgängig, die Änderungen sind aber weiterhin verfügbar.

* ```git stash``` - Hält den aktuellen Zustand des Verzeichnisses fest.

* ```git checkout name-der-korrekten-branch``` - Wechselt zu einer anderen branch.

* ```git stash pop``` - Entfernt den zuletzt festgehaltenen Zustand.

* ```git add .``` - Oder füge weitere Dateien hinzu.  

* ```git commit -m "deine commit nachricht"``` - Speichert und fügt deine Änderungen hinzu.  

Nun befinden sich deine Änderungen in der korrekten branch.

### 2. Moving the latest commits to a new Branch

Dafür musst du folgendes machen:

* ```git branch newbranch``` - Erstellt eine neue branch und speichert alle commits.

* ```git reset --hard HEAD~#``` - Schiebt den master zurück durch # commits. Achtung: Diese commits werden vom master entfernt werden!

* ```git checkout newbranch``` - Wechselt zur neu erstellten branch, welche alle commits enthält.

Denk daran: Alle nicht bestätigten Änderungen gehen VERLOREN!