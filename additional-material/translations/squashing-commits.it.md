# Che cos'è il compattamento (Squashing)

In git, il compattamento (squashing) si riferisce alla riscrittura della cronologia dei commit. Perciò alla fine si otterrà un solo commit con un'unica descrizione delle modifiche apportate.  
Di solito viene eseguito nei progetti open source perché gran parte della storia di un ramo dei progetti open source è rilevante solo per lo sviluppatore che l'ha creato, e questo comando fornisce un modo semplice per descrivere i cambiamenti fatti e anche annullarli se necessario.  

# Come si esegue il compattamento dei commit?

Per prima cosa, effettua un git log per rivedere i commit che vorrai unire nel tuo ramo corrente.  

```
git log
```

Tu dovresti vedere una serie di commit in questo modo:  

```
commit blablabla
Author: omguhh
Date:   10/10/20
    Commit message 1

commit blablabla2
Author: omguhh
Date:   10/10/20
    Commit message 2
```

Ora che vedi i commit che desidere unire in uno, possiamo procedere eseguendo un ```git rebase```. Supponiamo che tu sei già familiare con ```git rebase```, possiamo iniziare a compattare i commit nella modalità interattiva di git rebase che puoi attivare in questo modo:  

```
git rebase -i
```

Ora con il rebase interattivo puoi specificare il punto iniziale e finale di quanto indietro vuoi andare con i commit. In questo modo:  

```
git rebase -i HEAD~2
```

L'esecuzione di questo comando ti mostrarà qualcosa come il seguente:  

```
pick blablabla Changing test01.txt file
pick blablabla2 Adding dummy01.txt file

#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

Perciò se vuoi compattare ```blablabla2``` in ```blablablabla``` tu dovrai cambiare come segue:  

```
pick blablabla Changing test01.txt file
squash blablabla2 Adding dummy01.txt file

```

Se tutto andrà bene, tu otterrai un risultato che somiglia a questo:  

```
# This is a combination of 2 commits.
# The first commit's message is:
commit message 1

# This is the 2nd commit message:

commit message 2
```

Che puoi liberamente cambiare prima di decidere di uscire dall'editor per salvare le modifiche.  

Esegui nuovamente git log ti dovrebbe mostrare il messaggio di commit che hai inserito prima di uscire dalla schermata con i commit uniti in uno solo.  
