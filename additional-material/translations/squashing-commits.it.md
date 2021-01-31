# Che cos'è il compattamento (Squashing)

In git, il compattamento (squashing) si riferisce alla riscrittura della cronologia dei commit. Perciò alla fine si otterrà un solo commit con un'unica descrizione delle modifiche apportate.  
Di solito viene eseguito nei progetti open source perché gran parte della storia di un ramo dei progetti open source è rilevante solo per lo sviluppatore che l'ha creato, e questo comando fornisce un modo semplice per descrivere i cambiamenti fatti e anche annullarli se necessario.  

# Come si esegue il compattamento dei commit?

Per prima cosa, effettua un git log per rivedere i commit che vorrai unire nel tuo ramo corrente.  

```
git log
```

Dovresti vedere una serie di commit in questo modo:  

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

Ora che vedi i commit che desideri unire in uno, possiamo procedere eseguendo un ```git rebase```. Supponiamo tu sia già familiare con ```git rebase```, possiamo iniziare a compattare i commit nella modalità interattiva di git rebase che puoi attivare in questo modo:  

```
git rebase -i
```

Ora, con il rebase interattivo puoi specificare il punto iniziale e finale di quanto indietro vuoi andare con i commit. In questo modo:  

```
git rebase -i HEAD~2
```

L'esecuzione di questo comando ti mostrerà qualcosa come il seguente:  

```
pick blablabla Changing test01.txt file
pick blablabla2 Adding dummy01.txt file

#
# Comandi:
#  p, pick = tieni il commit
#  r, reword = tieni il commit, ma modifica il messaggio di commit
#  e, edit = tieni il commit, ma fermati per modificare (*amend*)
#  s, squash = tieni il commit, ma compattalo nel precedente commit
#  f, fixup = come "squash", ma scarta il messaggio di log di questo commit
#  x, exec = esegui il comando (il resto della linea) usando la shell
#
# Queste linee possono essere riordinate; saranno eseguite dall'alto verso il basso.
#
# Se rimuovi una linea qui QUESTO COMMIT SARA' PERSO.
#
# Tuttavia, se rimuovi tutto, il rebase sarà annullato.
#
# Nota che i commit vuoti sono commentati
```

Perciò se vuoi compattare ```blablabla2``` in ```blablablabla```, dovrai cambiare come segue:  

```
pick blablabla Changing test01.txt file
squash blablabla2 Adding dummy01.txt file

```

Se tutto andrà bene, otterrai un risultato simile a questo:  

```
# Questa è una combinazione di 2 commit.
# Il primo messaggio di commit è:
commit message 1

# Questo è il messaggio del secondo commit:

commit message 2
```

Che puoi liberamente cambiare prima di decidere di uscire dall'editor per salvare le modifiche.  

Eseguire nuovamente git log dovrebbe mostrarti il messaggio di commit, che hai inserito prima di uscire dalla schermata, con i commit uniti in uno solo.  
