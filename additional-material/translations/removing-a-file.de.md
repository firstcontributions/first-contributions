# Entfernen einer Datei von Git

Manchmal möchtest du eine Datei aus Git entfernen, aber nicht von deinem Computer löschen. Dies kannst du mit dem folgenden Befehl erreichen:

``git rm <file> --cached``

## Was ist passiert?

Somit verfolgt Git die Änderungen in der entfernten Datei nicht mehr. Es nimmt an, dass du die Datei gelöscht hast. Wenn du aber nach der Datei in deinem Dateisystem suchst, wirst du feststellen, dass sie noch vorhanden ist.

Beachte, dass im obigen Beispiel `--cached` verwendet wurde. Hätten wir dies nicht hinzugefügt, würde Git die Datei nicht nur aus dem repository, sondern auch aus deinem Dateisystem entfernen.

Wenn du die Änderungen mit `git commit -m "Entferne file1.js"` überträgst und es in dein remote repository mithilfe von `git push origin master` pusht, wird die Datei entfernt werden.

## Zusätzliche Funktionen

- Falls du mehr als eine Datei entfernen möchtest, kannst du dies folgendermaßen erreichen:

  `git rm file1.js file2.js file3.js --cached`

- Du kannst den Platzhalter `*` nutzen, um ähnliche Dateien zu entfernen. In diesem Beispiel entfernst du alle .txt Dateien aus deinem lokalen repository:

  `git rm *.txt --cached`