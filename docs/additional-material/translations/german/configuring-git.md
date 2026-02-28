# Git konfigurieren

Als Sie zum ersten Mal versucht haben, mit Git einen Commit durchzuführen, wurde möglicherweise eine Eingabeaufforderung wie die folgende angezeigt:

```bash
$ git commit
*** Bitte geben Sie an, wer Sie sind.

Führen Sie

git config --global user.email „you@example.com“
git config --global user.name „Ihr Name“

aus, um die Standardidentität Ihres Kontos festzulegen.
Lassen Sie --global weg, um die Identität nur in diesem Repository festzulegen.
```

Git muss wissen, wer Sie sind, wenn Sie einen Commit erstellen. Wenn Sie gemeinsam mit anderen arbeiten, sollten Sie sehen können, wer welche Teile des Projekts wann geändert hat. Daher wurde Git so konzipiert, dass Commits mit einem Namen und einer E-Mail-Adresse verknüpft werden.

Es gibt mehrere Möglichkeiten, dem Befehl `git commit` Ihre E-Mail-Adresse und Ihren Namen mitzuteilen. Im Folgenden werden wir einige davon durchgehen.

### Globale Konfiguration

Wenn Sie etwas in der globalen Konfiguration speichern, ist es systemweit in allen Repositorys, an denen Sie arbeiten, zugänglich. Dies ist die bevorzugte Methode und funktioniert in den meisten Anwendungsfällen.

Um etwas in der globalen Konfiguration zu speichern, verwenden Sie den Befehl `config` wie folgt:

`$ git config --global <Variablenname> <Wert>`

Im Falle von Benutzerdaten führen wir ihn wie folgt aus:

```
$ git config --global user.email „you@example.com“
$ git config --global user.name „Ihr Name“
```

### Repository-Konfiguration

Wie der Name schon sagt, gelten diese Konfigurationen nur für Ihr aktuelles Repository. Wenn Sie mit der E-Mail-Adresse Ihres Unternehmens einen Commit in einem bestimmten Repository vornehmen möchten, z. B. in einem arbeitsbezogenen Projekt, können Sie diese Methode verwenden.

Um etwas in der Repository-Konfiguration zu speichern, verwenden Sie den Befehl `config`, indem Sie das Flag `--global` wie folgt weglassen:

`$ git config <Variablenname> <Wert>`

Im Falle von Benutzerdaten führen wir den Befehl wie folgt aus:

```
$ git config user.email „you@alternate.com“
$ git config user.name „Ihr Name“
```

### Befehlszeilenkonfiguration

Diese Art von Konfigurationen gilt nur für den aktuellen Befehl. Alle Git-Befehle nehmen vor dem Aktionsverb ein `-c`-Argument entgegen, um temporäre Konfigurationsdaten festzulegen.

Um etwas in der Befehlszeilenkonfiguration zu speichern, führen Sie Ihren Befehl wie folgt aus:

`$ git -c <Variable-1>=<Wert> -c <Variable-2>=<Wert> <Befehl>`

In unserem Beispiel würden wir den Commit-Befehl wie folgt ausführen:

`git -c user.name=‚Ihr Name‘ -c user.email=‚you@example.com‘ commit -m „Ihre Commit-Nachricht“`

### Hinweis zur Priorität

Unter den drei hier beschriebenen Methoden lautet die Prioritätsreihenfolge `Befehlszeile > Repository > global`. Das bedeutet, dass, wenn eine Variable sowohl in der Befehlszeile als auch global konfiguriert ist, der Wert aus der Befehlszeile für die Operation verwendet wird.

## Über die Benutzerdaten hinaus

Bisher haben wir uns bei der Arbeit mit der Konfiguration nur mit den Benutzerdaten befasst. Es gibt jedoch noch einige andere Konfigurationsoptionen. Einige davon sind:

1.  `core.editor` – zum Festlegen des Namens des Editors, der zum Schreiben von Commit-Nachrichten usw. verwendet wird.
2.  `commit.template` – zum Festlegen einer Datei auf dem System als Vorlage für den ersten Commit.
3.  `color.ui` – zum Festlegen eines booleschen Werts für die Verwendung von Farben in der Ausgabe von Git.

Wir haben einige Details zum besseren Verständnis abstrahiert. Weitere Informationen finden Sie unter [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).
