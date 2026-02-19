# Git unter Arch Linux installieren

Um Git unter Arch Linux zu installieren, können Sie den Paketmanager pacman verwenden. Öffnen Sie zunächst ein Terminal und aktualisieren Sie das System mit dem folgenden Befehl:

```shell
$ sudo pacman -Syu
```

Installieren Sie anschließend Git mit dem folgenden Befehl:

```shell
$ sudo pacman -S git
```

Um zu überprüfen, ob Git korrekt installiert wurde, führen Sie den folgenden Befehl aus:

```shell
$ git --version
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```shell
Ausgabe
$ git version 2.34.1
```

# Git einrichten

Die Konfiguration kann mit dem Befehl git config vorgenommen werden.
Insbesondere müssen Sie Ihren Namen und Ihre E-Mail-Adresse angeben, da Git diese Informationen in jeden Ihrer Commits einbettet.
Sie können diese Informationen hinzufügen, indem Sie Folgendes eingeben:

Nachdem wir nun die Installation von Git abgeschlossen haben, konfigurieren wir es für die erste Verwendung mit dem Befehl „git config”.
Wir müssen sicherstellen, dass Ihr Benutzername und Ihre E-Mail-Adresse korrekt eingestellt sind. Um diese einzustellen, verwenden Sie den folgenden Befehl:

```shell
$ git config --global user.name „Ihr Name”
$ git config --global user.email „youremail@domain.com”
```

Sie können alle festgelegten Konfigurationselemente anzeigen, indem Sie den folgenden Befehl in Ihrem Terminal eingeben:

```shell
$ git config --list
```

Wenn alle Konfigurationsfelder nach Ihren Wünschen eingerichtet wurden, sollte die Ausgabe in etwa so aussehen:

```shell
user.name=Ihr Name
user.email=youremail@domain.com
```

# Git-Anmeldedaten speichern

Standardmäßig fordert Git Sie bei jeder Interaktion mit einem Remote-Repository auf, Ihren Benutzernamen und Ihr Passwort erneut einzugeben. Sie können Git so konfigurieren, dass Ihre Anmeldedaten zwischengespeichert oder gespeichert werden, um dies zu vermeiden. Im Folgenden finden Sie zwei gängige Methoden:

### 1. Zwischenspeichern von Anmeldedaten

Git kann Ihre Anmeldedaten vorübergehend im Speicher ablegen, sodass Sie sie nicht häufig erneut eingeben müssen. Führen Sie den folgenden Befehl aus, um das Zwischenspeichern von Anmeldedaten zu aktivieren:

```shell
$ git config --global credential.helper cache
```

Standardmäßig werden Anmeldedaten 15 Minuten lang zwischengespeichert. Um die Zeitüberschreitung anzupassen (z. B. auf 1 Stunde), verwenden Sie:

```shell
$ git config --global credential.helper ‚cache --timeout=3600‘
```

---

### 2. Speichern von Anmeldedaten

Wenn Sie Ihre Anmeldedaten lieber dauerhaft im Klartext speichern möchten (weniger sicher, aber bequem), können Sie den folgenden Befehl verwenden:

```shell
$ git config --global credential.helper store
```

Bei dieser Methode werden Ihre Anmeldedaten im Klartext in `~/.git-credentials` gespeichert. Seien Sie bei dieser Vorgehensweise vorsichtig, insbesondere auf gemeinsam genutzten oder öffentlichen Computern.