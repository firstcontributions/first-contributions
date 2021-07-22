# Annullare un commit locale (Undo-ing)

<<<<<<< HEAD
<<<<<<< HEAD
Per annullare un commit locale, l'unico comando da eseguire è:  
=======
Per annullare un commit locale, tutto quello che devi fare è:  
>>>>>>> 132c8610... Added it translate of undoing-a-commit
=======
Per annullare un commit locale, l'unico comando da eseguire è:  
>>>>>>> 48533364... Fix IT translation
```
git reset
```

<<<<<<< HEAD
<<<<<<< HEAD
Questo comando resetterà la tua *staging area* con il commit più recente, ma i cambiamenti fatti alla tua *working directory* non saranno modificati. Quindi potrai ancora ri-committare le tue modifiche. Altrimenti, se desideri solo rimuovere un file dal commit precedente, puoi eseguire questo comando:  
=======
Questo comando resetterà la tua *staging area* con il commit più recente, ma i cambiamenti fatti alla tua *working directory* non verranno cambiati. Quindi tu potrai ancora ri-committare il tuo precedente commit.  

Puoi inoltre eseguire questo comando:  
>>>>>>> 132c8610... Added it translate of undoing-a-commit
=======
Questo comando resetterà la tua *staging area* con il commit più recente, ma i cambiamenti fatti alla tua *working directory* non saranno modificati. Quindi potrai ancora ri-committare le tue modifiche. Altrimenti, se desideri solo rimuovere un file dal commit precedente, puoi eseguire questo comando:  
>>>>>>> 48533364... Fix IT translation
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

<<<<<<< HEAD
<<<<<<< HEAD
Mettiamo il caso tu abbia incasinato il tuo repository locale e voglia semplicemente ripristinarlo all'ultimo commit. In questo caso puoi eseguire il seguente comando:  
```
git reset --hard
```
Il comando non solo ripristinerà la tua *staging area*, ma ripristinerà tutti i cambiamenti sui file all'ultimo commit. La modalità ```--hard``` comunica a Git anche di annullare tutte le modifiche nella tua *working directory*. Dovresti eseguirlo solo nel caso tu sia veramente sicuro di voler gettar via tutto il tuo lavoro in locale.  
=======
Mettiamo il caso che hai incasinato il tuo repository locale e vuoi solo ripristinarlo all'ultimo commit.
In questo caso puoi eseguire il seguente comando:  
```
git reset --hard
```
Il comando non solo ripristinerà la tua *staging area*, ma annullerà tutti i cambiamenti sui file all'ultimo commit.  
La modalità ```--hard``` dice anche a Git di annullare tutte le modifiche nella tua *working directory*.  
Dovresti eseguirlo solo quando sei veramente sicuro di gettar via tutto il tuo lavoro in locale.  
>>>>>>> 132c8610... Added it translate of undoing-a-commit
=======
Mettiamo il caso tu abbia incasinato il tuo repository locale e voglia semplicemente ripristinarlo all'ultimo commit. In questo caso puoi eseguire il seguente comando:  
```
git reset --hard
```
Il comando non solo ripristinerà la tua *staging area*, ma ripristinerà tutti i cambiamenti sui file all'ultimo commit. La modalità ```--hard``` comunica a Git anche di annullare tutte le modifiche nella tua *working directory*. Dovresti eseguirlo solo nel caso tu sia veramente sicuro di voler gettar via tutto il tuo lavoro in locale.  
>>>>>>> 48533364... Fix IT translation

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
<<<<<<< HEAD
<<<<<<< HEAD
Il comando ```git reset --hard HEAD~2``` sposta il ramo corrente indietro di 2 commit in una sola volta, annullando tutte le modifiche che hai fatto e rimuovendo i 2 *snapshots* che abbiamo appena creato nella cronologia del progetto.  

P.s. Non eseguire mai ```git reset --hard``` se hai già inviato i tuoi commit ad un repository condiviso, altrimenti causerà problemi a tutti coloro che lavorano correntemente con quel repository.  
=======
Il comando ```git reset --hard HEAD~2``` sposta il ramo corrente indietro di 2 commit in una sola volta annullando tutte le modifiche che hai fatto e rimuovendo i 2 *snapshots* che abbiamo appena creato nella cronologia del progetto.  

P.s. Non eseguire mai ```git reset --hard``` se hai già inviato i tuoi commit ad un repository condiviso poiché causerà problemi a tutti sul quel repository.  
>>>>>>> 132c8610... Added it translate of undoing-a-commit
=======
Il comando ```git reset --hard HEAD~2``` sposta il ramo corrente indietro di 2 commit in una sola volta, annullando tutte le modifiche che hai fatto e rimuovendo i 2 *snapshots* che abbiamo appena creato nella cronologia del progetto.  

P.s. Non eseguire mai ```git reset --hard``` se hai già inviato i tuoi commit ad un repository condiviso, altrimenti causerà problemi a tutti coloro che lavorano correntemente con quel repository.  
>>>>>>> 48533364... Fix IT translation
