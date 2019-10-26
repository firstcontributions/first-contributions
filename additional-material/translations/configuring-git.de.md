# Konfiguration von Git

Sobald du zum ersten mal ein commit mit Git auszuführst, hast du vielleicht eine Aufforderung wie diese erhalten:

```bash
$ git commit
*** Please tell me who you are.

Run

git config --global user.email "du@beispiel.de"
git config --global user.name "dein Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
```

Git möchte wissen, wer du bist, wenn du ein commit erstellst. Wenn du kollaborativ arbeitest, solltest du sehen können, wer welche Teile des Projekts wann geändert hat. Git wurde so entwickelt, dass commits an einen Namen und eine E-Mail gebunden sind.

Es gibt mehrere Möglichkeiten, den Befehl `git commit` mit deiner E-Mail und deinem Namen zu versehen, und wir werden einige davon im Folgenden durchgehen.

### 1. Globale Konfiguration

Wenn du etwas in der globalen Konfiguration speicherst, ist es systemweit in allen repositories, an denen du arbeitest, zugänglich. Dies ist der bevorzugte Weg und funktioniert in den meisten Anwendungsfällen.

Um etwas in der globalen Konfiguration zu speichern, verwende den Befehl `config` wie folgt:

`$ git config --global <variable name> <value>`

Im Falle von Benutzerdaten gehen wir wie folgt vor:

```
$ git config --global user.email "du@beispiel.de"
$ git config --global user.name "dein Name"
```

### 2. Repository Konfiguration

Wie der Name schon sagt, wird diese Konfiguration auf dein aktuelles repository übertragen. Wenn du dich mit der E-Mail deines Unternehmens an ein bestimmtes repository (z.B. ein arbeitsbezogenes Projekt) binden möchtest, dann kannst du diese Methode verwenden.

Um etwas in der repository Konfiguration zu speichern, verwendest du den Befehl `config`, indem du `--global` auslässt:

`$ git config <variable name> <value>`

Im Falle von Benutzerdaten gehen wir wie folgt vor:

```
$ git config user.email "du@beispiel.de"
$ git config user.name "dein Name"
```

### 3. Befehlszeilen-Konfiguration

Diese Art von Konfiguration wird nur auf den aktuellen Befehl angewendet. Alle Git-Befehle nehmen `-c` Argumente vor dem Aktionsverb, um temporäre Konfigurationsdaten zu setzen.

Um etwas in der Befehlszeilen-Konfiguration zu speichern, führe den Befehl wie folgt aus:

`$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>`

In unserem Beispiel würden wir den Befehl `commit` wie folgt ausführen:

`git -c user.name='dein Name' -c user.email='du@beispiel.de' commit -m "deine commit Nachricht"`

### Hinweis zur Priorität

Unter den drei hier beschriebenen Methoden ist die Rangfolge `command-line > repository > global`. Das bedeutet, dass, wenn eine Variable sowohl in der Befehlszeile als auch global konfiguriert wird, der Befehlszeilenwert für die Operation verwendet wird.

## Über Benutzerdetails hinaus

Bisher haben wir uns bei der Arbeit mit der Konfiguration nur mit den Benutzerdaten beschäftigt. Es gibt jedoch noch einige andere Konfigurationsoptionen:

1. `core.editor` - um den Namen des text editors anzugeben, welcher z.B. zum Schreiben von commit Nachrichten verwendet wird.

2.  `commit.template` - um eine Datei im System als anfängliche commit Vorlage anzugeben.

3.  `color.ui` - um einen booleschen Wert für die Verwendung von Farben in Git anzugeben.

Wir haben einige Details zum besseren Verständnis abstrahiert. Für weitere Informationen besuche bitte [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).