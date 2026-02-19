# Einen Commit in einen anderen Branch verschieben
Was passiert, wenn Sie eine Änderung committen und dann feststellen, dass Sie in einen anderen Branch committet haben?
Wie können Sie das ändern? Das erfahren Sie in diesem Tutorial.

## Die neuesten Commits in einen bestehenden Branch verschieben
Geben Sie dazu Folgendes ein:

```git reset HEAD~ --soft``` – Macht den letzten Commit rückgängig, lässt die Änderungen jedoch verfügbar.  
```git stash``` – Zeichnet den Zustand des Verzeichnisses auf.  

```git checkout name-des-richtigen-Branches``` – Wechselt zu einem anderen Branch.
```git stash pop``` – Entfernt den zuletzt zwischengespeicherten Status.  
```git add .``` – Oder versuchen Sie, einzelne Dateien hinzuzufügen.  
```git commit -m „Ihre Nachricht hier“``` – Speichert und committet die Änderungen.  

Jetzt befinden sich Ihre Änderungen im richtigen Branch.


### Die letzten Commits in einen neuen Branch verschieben
Geben Sie dazu Folgendes ein:  
```git branch newbranch``` -  Erstellt einen neuen Branch. Speichert alle Commits.  
```git reset --hard HEAD~#``` - Verschiebt master um # Commits zurück. Denken Sie daran, dass diese Commits aus master entfernt werden  
```git checkout newbranch``` - Wechselt zu dem von Ihnen erstellten Branch. Dieser enthält alle Commits.  

Denken Sie daran: Alle nicht festgeschriebenen Änderungen gehen VERLOREN.