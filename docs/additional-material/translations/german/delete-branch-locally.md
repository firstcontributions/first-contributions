# Löschen eines lokal erstellten Branches

Dies ist nützlich, wenn Sie versehentlich einen Branch-Namen falsch geschrieben haben.

Dies kann auf *3* Arten erfolgen

```
git branch -D <branch_name>
```

```
git branch --delete --force <branch_name>  # Entspricht -D
```

```
git branch --delete  <Zweigname>         # Fehler beim Aufheben der Zusammenführung
```

-D steht für --delete --force, wodurch der Zweig auch dann gelöscht wird, wenn er nicht zusammengeführt wurde (zwangsweise Löschung). Sie können jedoch auch -d verwenden, was für --delete steht und einen Fehler entsprechend dem Status der Zweigzusammenführung auslöst...