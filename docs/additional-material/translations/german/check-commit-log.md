# Commit-Protokoll überprüfen

Um das Commit-Protokoll für einen Branch oder eine Datei zu überprüfen, kann der folgende Befehl verwendet werden:

`git log [Optionen] [Pfad]`

Die Ausgabe dieses Befehls erfolgt standardmäßig in umgekehrter chronologischer Reihenfolge.

## Beispiel für die Befehlsausgabe
```
$ git log
commit e3fabb30ab536bd5876461d8a749301a321e714f (HEAD -> check-commit-log-ko, upstream/main, origin/main, origin/HEAD, main)
Autor: Dan Yunheum Seol <yunheum.seol@mail.mcgill.ca>
Datum:   Di, 4. Juni 01:07:25 2024 -0400

    dan-seol zur Liste der Mitwirkenden hinzufügen (#84962)

commit 4af4ec8a56e057ce8768af77eda528453974d0bc
Autor: Edgar Humberto Tijerina Tamez <168693312+EdgarHTT@users.noreply.github.com>
Datum:   Mo, 3. Juni 23:06:05 2024 -0600

    Edgar Tijerina zur Liste der Mitwirkenden hinzufügen (#84961)
```


## Befehlsvarianten und Optionen 
- Um die Commits auszuführen, die über bestimmte Commit-IDs erreichbar sind: <i>(In diesem Fall `foo` und `bar`)</i><br>
    `git log foo bar ` 
- Es ist auch möglich, die Commits zu entfernen, die von einer bestimmten Commit-ID aus erreichbar sind, indem man ein `^` vor die Commit-ID setzt: <i>(In diesem Fall `baz`)</i><br>
    `git log foo bar ^baz`
- Commit-Protokoll für eine bestimmte Datei: <br> 
    `git log --all <Dateiname>`
- Begrenzung der Anzahl der Commits im Protokoll: <i>(In diesem Fall `5`)</i><br> 
    `git log -n 5`

## Referenz
- [Offizielle Dokumentation](https://git-scm.com/docs/git-log)
