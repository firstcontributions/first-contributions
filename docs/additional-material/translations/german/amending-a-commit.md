# Einen Commit ändern

Was tun, wenn Sie eine Änderung in Ihrem Remote-Repository committen und später feststellen, dass Sie einen Tippfehler in der Commit-Nachricht haben oder vergessen haben, eine Zeile in Ihrem letzten Commit hinzuzufügen?
Wie können Sie das bearbeiten? Das erfahren Sie in diesem Tutorial.

## Eine aktuelle Commit-Nachricht ändern, nachdem Sie sie an Github gepusht haben.
So gehen Sie vor, ohne eine Datei zu öffnen:
* Geben Sie Folgendes ein: ```git commit --amend -m „gefolgt von Ihrer neuen Commit-Nachricht“```
* Führen Sie ```git push origin <Branch-Name>``` aus, um die Änderungen im Repository zu committen.

Hinweis: Wenn Sie nur ```git commit --amend``` eingeben, wird Ihr Texteditor geöffnet und Sie werden aufgefordert, die Commit-Nachricht zu bearbeiten.
Durch Hinzufügen des Flags ``-m`` wird dies verhindert.

## Ändern eines einzelnen Commits

Was passiert also, wenn wir vergessen haben, eine kleine Änderung an einer Datei vorzunehmen, z. B. ein einzelnes Wort zu ändern, und wir den Commit bereits in unser Remote-Repository gepusht haben?

Zur Veranschaulichung hier ein Protokoll meiner Commits:
```
g56123f Datei bot file erstellen
a2235d contributor.md aktualisiert
a5da0d bot file geändert
```
Nehmen wir an, ich habe vergessen, ein einzelnes Wort zur Bot-Datei hinzuzufügen.

Es gibt zwei Möglichkeiten, dies zu beheben. Die erste besteht darin, einen völlig neuen Commit zu erstellen, der die Änderung wie folgt enthält:
```
g56123f Datei botfile erstellen
a2235d contributor.md aktualisiert
a5da0d botfile geändert
b0ca8f einzelnes Wort zu botfile hinzugefügt
```
Die zweite Möglichkeit besteht darin, den Commit a5da0d zu ändern, dieses neue Wort hinzuzufügen und  es als einen Commit an Github zu übertragen.
Die zweite Möglichkeit klingt besser, da es sich nur um eine geringfügige Änderung handelt.

Um dies zu erreichen, würden wir Folgendes tun:
*   Die Datei ändern. In diesem Fall werde ich die Botdatei ändern, um das zuvor ausgelassene Wort hinzuzufügen.
* Als Nächstes fügen wir die Datei mit ```git add <Dateiname>```

normalerweise zum Staging-Bereich hinzu. Nach dem Hinzufügen von Dateien zum Staging-Bereich führen wir normalerweise als Nächstes git commit -m „unsere Commit-Nachricht” aus, richtig?
Da wir hier jedoch den vorherigen Commit ändern möchten, führen wir stattdessen Folgendes aus:

* ```git commit --amend```
 Dadurch wird der Texteditor geöffnet und Sie werden aufgefordert, die Nachricht zu bearbeiten. Sie können die Nachricht unverändert lassen oder ändern.
* Beenden Sie den Editor.
* Übertragen Sie Ihre Änderungen mit ```git push origin <branch-name>```

Auf diese Weise würden beide Änderungen in einem einzigen Commit enthalten sein.

## Ändern von Commits auf dem Remote

Wenn der Commit, den Sie ändern möchten, bereits auf den Remote übertragen wurde, führt die Änderung dieses Commits dazu, dass Ihre lokale Historie von der Remote abweicht (da Sie im Grunde einen neuen Commit erstellen und den geänderten ersetzen). Da Sie den Commit auf dem Remote ändern möchten, müssen Sie die Remote-Historie auf Ihrem Branch überschreiben. Um dies zu erreichen, gehen Sie wie oben beschrieben vor, verwenden Sie jedoch beim Übertragen Ihres Commits auf den Remote den Befehl „force push“.

> **Warnung**  
> Durch das Force-Pushing auf den Remote werden Änderungen auf dem Remote überschrieben (und verworfen) und nur Ihre gepushten Commits beibehalten. Änderungen auf dem Remote, die andere Teammitglieder in der Zwischenzeit vorgenommen haben, werden ebenfalls überschrieben.

So ändern Sie den letzten aktuellen Commit auf dem Remote:

```bash
git add <Ihre geänderten Dateien>
git commit --amend -m „gefolgt von Ihrer neuen Commit-Nachricht“
git push --force
```

> Die Verwendung von `--force-with-lease` ist eine sicherere Option als `--force`, da dadurch vermieden wird, dass die Änderungen anderer Personen auf dem Remote-Branch überschrieben werden (sofern Sie dies nicht beabsichtigen).
