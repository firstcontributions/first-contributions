# Git unter Ubuntu installieren

Git ist wahrscheinlich bereits standardmäßig in Ihrem Ubuntu-Betriebssystem installiert. Sie können dies überprüfen, indem Sie Ihr Terminal starten und den folgenden Befehl in Ihr Terminal eingeben:

```shell
$ git --version
```

Wenn Sie eine Ausgabe ähnlich der folgenden erhalten, dann Voila! Sie haben Git bereits auf Ihrem Rechner installiert.

```shell
Ausgabe
$ git version 2.34.1
```

Wenn dies auf Sie zutrifft, fahren Sie mit dem Abschnitt [Einrichten von Git](#set-up-git) weiter unten fort.

Wenn die Git-Versionsnummer nicht wie oben gezeigt in der Ausgabe angezeigt wurde, können Sie Git dennoch mit dem Standard-Paketmanager APT von Ubuntu installieren.

Aktualisieren Sie zunächst Ihren lokalen Paketindex mit den apt-Paketverwaltungstools. Kehren Sie zu Ihrem Terminal zurück und geben Sie den folgenden Befehl ein.

```shell
$ sudo apt update
```

Geben Sie anschließend den folgenden Befehl ein, um Git zu installieren:

```shell
$ sudo apt install git
```

Sie können überprüfen, ob Sie Git korrekt installiert haben, indem Sie den folgenden Befehl ausführen und sicherstellen, dass Sie die entsprechende Ausgabe erhalten.

```shell
$ git --version
```

```shell
Ausgabe
$ git version 2.34.1
```

Nachdem Git erfolgreich installiert wurde, können Sie nun mit der Einrichtung fortfahren.

# Git einrichten

Die Konfiguration kann mit dem Befehl git config vorgenommen werden.
Insbesondere müssen Sie Ihren Namen und Ihre E-Mail-Adresse angeben, da Git diese Informationen in jeden Ihrer Commits einbettet.
Sie können diese Informationen hinzufügen, indem Sie Folgendes eingeben:

Nachdem wir nun die Installation von Git abgeschlossen haben, konfigurieren wir es für die erste Verwendung mit dem Befehl „git config”.
Wir müssen sicherstellen, dass Ihr Benutzername und Ihre E-Mail-Adresse korrekt eingestellt sind. Verwenden Sie dazu den folgenden Befehl:

```shell
$ git config --global user.name „Ihr Name“
$ git config --global user.email „youremail@domain.com“
```

Sie können alle festgelegten Konfigurationselemente anzeigen, indem Sie den folgenden Befehl in Ihrem Terminal eingeben:

```shell
$ git config --list
```

Wenn alle Konfigurationsfelder nach Ihren Wünschen eingerichtet wurden, sollte die Ausgabe in etwa so aussehen

```shell
user.name=Ihr Name
user.email=youremail@domain.com
```...



# Git-Anmeldedaten speichern

Standardmäßig fragt Git Sie jedes Mal nach Ihren Daten, wenn Sie etwas in ein Remote-Repository übertragen möchten.
In Git können Sie das Caching Ihrer Anmeldedaten konfigurieren, um die wiederholte Eingabe Ihres Benutzernamens und Passworts zu vermeiden. Dazu gibt es mehrere Methoden:

1. Caching von Anmeldedaten: Git bietet ein Caching-System für Anmeldedaten, das Ihre Anmeldedaten für einen bestimmten Zeitraum im Speicher ablegen kann. Auf diese Weise müssen Sie Ihre Daten nicht jedes Mal neu eingeben, wenn Sie mit einem Remote-Repository interagieren.

Um das Caching von Anmeldedaten zu aktivieren, können Sie den folgenden Befehl verwenden:

```shell
$ git config --global credential.helper cache
```

Standardmäßig speichert Git Ihre Anmeldedaten 15 Minuten lang im Cache. Sie können die Cache-Zeitüberschreitung anpassen, indem Sie die Option --timeout gefolgt von der gewünschten Anzahl von Sekunden angeben.

Um beispielsweise die Cache-Zeitüberschreitung auf 1 Stunde (3600 Sekunden) festzulegen, können Sie Folgendes verwenden:

```shell
$ git config --global credential.helper ‚cache --timeout=3600‘

```

2. Speichern von Anmeldedaten: Hiermit wird der Anmeldedaten-Helper von Git auf „store” gesetzt. Bei Verwendung dieses Anmeldedaten-Helpers speichert Git die Anmeldedaten für ein Remote-Repository in einer Klartextdatei auf der Festplatte. Diese Methode ist die einfachste, aber auch die unsicherste Option für die Speicherung von Anmeldedaten.

```shell
$ git config --global crednetial.helper store
```

Mit dem Credential-Helper „store” werden die für ein Remote-Repository eingegebenen Anmeldedaten dauerhaft in einer Datei gespeichert, die sich unter Linux oder macOS unter ~/.git-credentials und unter Windows unter %USERPROFILE%\.git-credentials befindet. Die Anmeldedaten werden im Klartextformat gespeichert, was bedeutet, dass sie lesbar sind, wenn jemand Zugriff auf die Datei erhält.

Der Vorteil der Verwendung des „store credential helper” besteht darin, dass Sie nicht bei jeder Interaktion mit dem Remote-Repository zur Eingabe Ihrer Anmeldedaten aufgefordert werden. Beachten Sie jedoch die Sicherheitsrisiken, die mit der Speicherung von Anmeldedaten im Klartext verbunden sind, insbesondere wenn Sie einen gemeinsam genutzten oder öffentlichen Computer verwenden.