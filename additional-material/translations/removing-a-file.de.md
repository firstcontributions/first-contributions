# Eine Datei von Git entfernen

Manchmal möchte man eine Datei von Git entfernen, sie aber nicht vom eigenen Computer löschen. Die ist mit dem folgenden Kommando möglich:

``git rm <Datei> --cached``

## Was genau passiert?

Git wird nicht mehr auf modifizierungen in der entfernten Datei reagieren. Soweit Git es versteht, haben sie die Datei gelöscht. Jedoch ist die Datei noch immer in ihrem Dateien-System vorhanden.

Wie sie sicher gemerkthaben, wird im obigen Beispiel die Flag `-cached` benutzt. Wenn wir diese Flag weglassen würden, würde Git die Datei nicht nur von der lokalen Repository löschen, sondern auf vom Dateien-Systems ihres Computers.

Wenn sie diese Modifizierung mit `git commit -m "Datei1.cpp entfernt."` commiten, und anschließend mit `git push origin master` zur Remote Repository pushen, wird die Remote Repository die Datei entfernen.

## Zusätliche Features

-   Wenn sie mehr als eine Datei entfernen möchten, können sie diese im Kommando angeben:

    `git rm datei1.cpp datei2.h datei3.txt --cached`

-   Sie können auch Wildcards(*) benutzen, um ähnliche Dateien zu entfernen. Zum Beispiel, wenn sie alle .cpp Dateien in ihrer
    Repository entferenen möchten:

    `git rm *.cpp --cached`
