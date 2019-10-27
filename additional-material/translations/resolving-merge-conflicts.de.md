# Was ist ein merge Konflikt?

Wenn du versuchst, einen anderen branch in deinen aktuellen branch einzufügen, nimmst du Änderungen aus einem anderen Kontext und kombinierst diese mit deinen aktuellen Arbeitsdateien.

Wenn zwei Personen die gleichen Zeilen in derselben Datei geändert haben, oder wenn eine Person beschlossen hat, sie zu löschen, während die andere Person beschlossen hat, sie zu ändern, kann Git nicht feststellen, welche Version die richtige ist. 

Git markiert die Datei dann als Konflikt - den du lösen musst, bevor du deine Arbeit fortsetzen kannst.

# Wie löse ich einen merge Konflikt?

Bei einem merge Konflikt markiert Git den problematischen Bereich wie folgt:

`<<<<<<<<<<<<`, und `>>>>>>>>>>`[anderer branch Name]`

Der Inhalt nach der ersten Markierung stammt aus deinem aktuellen Arbeitszweig. Nach den spitzen Klammern sagt uns Git, woher (von welchem branch) die Änderungen kamen. 

Eine Zeile mit `=============`, trennt die beiden widersprüchlichen Änderungen.

Unsere Aufgabe ist es nun, diese Zeilen zu bereinigen: Wenn wir fertig sind, sollte die Datei genau so aussehen, wie wir es uns wünschen. 

Es ist daher ratsam, sich an die Person zu wenden, welche die widersprüchlichen Änderungen erzeugt hat, um zu entscheiden, welche Version endgültig sein soll. Es könnte entweder eine deiner Versionen sein - oder vielleicht eine Mischung aus beidem.

Beispiel:

```
<<<<<<< HEAD:mergetest
Dies ist die dritte Zeile
=======
Diese vierte Zeile füge ich hinzu
>>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Gibt den Anfang der Zeilen an, die einen merge Konflikt hatten. Der erste Satz von Zeilen sind die Zeilen aus der Datei, in die du versucht hast, die Änderungen einzubinden.  

`=======`: Gibt den Haltepunkt an, der für den Vergleich verwendet wird. Zerlegt Änderungen, die der Benutzer (oben) an Änderungen aus dem Zusammenführen (unten) vorgenommen hat, um die Unterschiede visuell zu veranschaulichen.  

`>>>>>>>`: Zeigt das Ende der Zeilen an, die einen merge Konflikt hatten.  

Du löst einen Konflikt, indem du die Datei bearbeitest und dann die Teile der Datei, die Git nicht zusammenführen konnte, manuell zusammenführst. 

Dies kann bedeuten, dass du entweder deine Änderungen oder die von jemand anderem verwirfst oder mit einer Mischung aus beidem weitermachst. 

Du musst auch die `<<<<<<<<<<<<`, `=============`, und `>>>>>>>>>>` in der Datei löschen.

Sobald du den Konflikt gelöst hast, führe `git add` aus. Vergiss nicht, die Tests durchzuführen, da du sicherstellen musst, dass du den Konflikt gelöst hast.

Du kannst auch verschiedene Plug-Ins herunterladen, abhängig von der IDE (integrated development environment), die du verwendest, um Konflikte beim Zusammenführen einfacher zu lösen.

# Wie mache ich ein merge rückgängig?

Führe `git merge -abort` aus, um einen merge rückgängig zu machen.