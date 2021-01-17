# Annullare un commit locale (Undo-ing)

Per annullare un commit locale, tutto quello che devi fare è:  
```
git reset
```

Questo comando resetterà la tua *staging area* con il commit più recente, ma i cambiamenti fatti alla tua *working directory* non verranno cambiati. Quindi tu potrai ancora ri-committare il tuo precedente commit.  

Puoi inoltre eseguire questo comando:  
```
git reset <file>
```
Il comando rimuoverà solo il file specificato dalla *staging area*, ma le modifiche fatte sul file rimarranno.  

Esempio dell'uso di ```git reset```  
```
# Fai dei cambiamenti in index.php e tutorial.php
# Aggiungi i file nella staging area
$ git add .
# Ti ricordi che entrambi i file devono essere committati separatamente
# Unstage tutorial.php
$ git reset tutorial.php
# Committi prima index.php 
$ git commit -m "Changed index.php"
# Committi tutorial.php adesso
$ git add tutorial.php
$ git commit -m "Changed tutorial.php"
```

Mettiamo il caso che hai incasinato il tuo repository locale e vuoi solo ripristinarlo all'ultimo commit.
In questo caso puoi eseguire il seguente comando:  
```
git reset --hard
```
Il comando non solo ripristinerà la tua *staging area*, ma annullerà tutti i cambiamenti sui file all'ultimo commit.  
La modalità ```--hard``` dice anche a Git di annullare tutte le modifiche nella tua *working directory*.  
Dovresti eseguirlo solo quando sei veramente sicuro di gettar via tutto il tuo lavoro in locale.  

Esempio dell'uso di ```git reset --hard```  
```
# Decidi di iniziare un esperimento pazzo
# Crei un nuovo file 'crazy.php' e aggiungi del codice all'interno
# Committi crazy.php
$ git add crazy.php
$ git commit -m "Started a crazy dev"
# Editi ancora il file crazy.php e hai cambiato un sacco di altri file
# Committi tutti i file tracciati da git
$ git add .
$ git commit -m "Continued dev"
# Hai testato e visto che le cose ti sono sfuggite di mano
# Decidi di rimuovere tutto
$ git reset --hard HEAD~2
```
Il comando ```git reset --hard HEAD~2``` sposta il ramo corrente indietro di 2 commit in una sola volta annullando tutte le modifiche che hai fatto e rimuovendo i 2 *snapshots* che abbiamo appena creato nella cronologia del progetto.  

P.s. Non eseguire mai ```git reset --hard``` se hai già inviato i tuoi commit ad un repository condiviso poiché causerà problemi a tutti sul quel repository.  
