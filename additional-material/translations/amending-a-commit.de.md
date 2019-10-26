# Änderung eines commits

Was wäre, wenn du eine Änderung an deinem remote repository vornimmst, nur um später festzustellen, dass du einen Tippfehler gemacht oder eine Textzeile vergessen hast?

Wie kann man das ändern? Darum geht es in diesem tutorial.

## Ändern einer kürzlich hinzugefügten commit Nachricht, nachdem du sie zu GitHub gepusht hast

Ohne eine neue Datei zu öffnen:

*   Gib folgendes ein: ```git commit --amend -m "deine neue commit nachricht"```
*   Führe ```git push origin <branch-name>``` aus, um die Änderungen deinem repository hinzuzufügen.

> Hinweis: Falls du nur ```git commit --amend``` eingibst, würde sich dein text editor öffnen und dich zur commit Nachricht führen. Durch hinzufügen von ``-m``kannst du dies verhindern.

## Modifizieren eines einzelnen commits

Was wäre, wenn wir vergessen hätten, eine kleine Änderung an einer Datei vorzunehmen, wie z.B. ein einzelnes Wort zu ändern und wir haben das commit bereits in unser remote repository gepusht?

Zur Veranschaulichung hier ein log meines commit:

```
g56123f create file bot file
a2235d updated contributor.md
a5da0d modified bot file
```

Nehmen wir an, dass ich ein einzelnes Wort vergessen hätte. Es gäbe zwei Möglichkeiten, dieses Problem zu lösen. 

Entweder ein komplett neues commit, welches die Änderung enthält:

```
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
b0ca8f added single word to botfile
```

Oder das ändern des a5da0d commit, indem man das neue Wort hinzufügt und diese Änderung zu GitHub pusht. Das scheint sinnvoller zu sein, da es sich nur um eine kleine Änderung handelt.

Das können wir folgendermaßen erreichen:

* Modifizieren der Datei. In diesem Fall modifiziere ich die bot Datei und füge das Wort hinzu, welches ich zuvor ausgelassen habe.

* Als nächstes füge ich die Datei der staging area mit ```git add <datei-name>``` hinzu.

Nachdem wir die Dateien der staging area hinzugefügt haben, wäre ```git commit -m "unsere commit nachricht"``` der nächste Schritt, richtig?
Aber da wir ein zuvor erstelltes commit ändern wollen, machen wir folgendes:

* Durch Eingabe von ```git commit --amend``` fordert dich dein text editor zum ändern der commit Nachricht auf. Du kannst sie entweder so lassen, oder ändern.

* Schließe deinen text editor.

* Pushe deine Änderungen mit ```git push origin <branch-name>```.

Auf diese Weise sind beide Änderungen in einem einzelnen commit enthalten.