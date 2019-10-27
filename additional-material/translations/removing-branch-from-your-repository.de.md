# Entfernen eines branch aus deinem repository

Wenn du das tutorial bis jetzt verfolgt hast, hat unser branch `<deinen-namen-hinzufügen>` seinen Zweck erfüllt und kann aus deinem lokalen repository gelöscht werden.

Das ist nicht zwingend nötig, doch der Name dieses branch zeugt von einem speziellen Zweck. Dessen Lebensdauer kann entsprechend kurz gestaltet werden.

Als erstes führen wir `<deinen-namen-hinzufügen>` mit deinem master branch zusammen. Gib folgendes ein, um dorthin zu wechseln:

```
git checkout master
```

Führe `<deinen-namen-hinzufügen>` mit dem master zusammen:

```
git merge <deinen-namen-hinzufügen> master
```

Entferne `<deinen-namen-hinzufügen>` aus deinem lokalen repository:

```
git branch -d <deinen-namen-hinzufügen>
```

Nun hast du den lokal gespeicherten `<deinen-namen-hinzufügen>` branch entfernt und alles sieht sauber und ordentlich aus. 

Allerdings hast du es noch immer in deinem GitHub fork.

Denk aber daran, dass du vor dem löschen dieses branch ein pull request an mein repository von diesem remote branch gesendet hast. Solange ich diese nicht zusammen geführt habe, solltest du es nicht löschen.

Wurden diese aber von mir zusammen geführt und du möchtest die remote branch löschen, dann führe folgendes aus:

```
git push origin --delete <deinen-namen-hinzufügen>
```

Jetzt weißt du, wie man branches aufräumt. Mit der Zeit werden meinem öffentlichen repository viele commits hinzugefügt werden, weshalb deine master branches (lokal und GitHub fork) nicht auf dem aktuellsten Stand sein werden.

Folge diesen Schritten, damit deine repositories immer synchron mit meinen sind:

#### [Halte dein fork mit dem repository synchronisiert](keeping-your-fork-synced-with-this-repository.de.md)