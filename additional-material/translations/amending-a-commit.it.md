# Modifica di un commit (amend)

Cosa fare se invii una modifica al tuo repository remoto e ti accorgi solo dopo di un errore nel messaggio di commit o di aver dimenticato di aggiungere una linea nel tuo commit più recente?  
Come correggere? Questo è quanto spiegato in questo tutorial.  

## Modifica di un messaggio di commit recente dopo aver effettuato il push su GitHub.  

Per fare questo senza aprire un file:
* Digita ```git commit --amend -m "seguito dal tuo nuovo messaggio di commit"```
* Esegui ```git push origin <branch-name>``` per committare le modifiche al repository.  

Nota: digitando soltanto  ```git commit --amend```, il tuo editor di testo si aprirà chiedendoti di modificare il messaggio di commit. Aggiungendo il flag ``-m`` lo si evita.  

## Modifica di un singolo commit

Cosa fare se abbiamo dimenticato di apportare una piccola modifica ad un file, come cambiare una singola parola, avendo già pushato il commit al nostro repository remoto?  

A scopo esemplificativo, questo è un log dei miei commit:
```
g56123f create file bot file
a2235d updated contributor.md
a5da0d modified bot file
```

In questo caso, il problema è che ho dimenticato di aggiungere una singola parola al file del bot.

Ci sono due modi per fare questo. Il primo è avere un commit completamente nuovo che contenga la modifica, ad esempio:
```
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
b0ca8f added single word to botfile
```
Il secondo è quello di modificare (to amend) il commit a5da0d, aggiungendo questa nuova parola e inviandolo a Github come un unico commit.
Questa opzione è preferibile, trattandosi solo di un piccolo cambiamento.  

Per ottenere questo risultato, dovremo fare quanto segue:  
* Modificare il file. In questo caso modifico il botfile per includere la parola che ho omesso in precedenza.  
* Successivamente, aggiungo il file nell'area di staging con il comando ```git add <filename>```  

Normalmente dopo aver aggiunto i file all'area di staging, il comando utilizzato successivamente è *git commit -m "il nostro messaggio di commit"*, giusto?  

Siccome ciò che vogliamo ottenere in questo caso è modificare il commit precedente, eseguiremo invece:

* ```git commit --amend```  
In questo modo verrà visualizzato l'editor di testo e verrà richiesto di modificare il messaggio. Puoi decidere di lasciare il messaggio com'era o di modificarlo.  
* Esci dall'editor  
* Esegui il push delle modifiche con ```git push origin <branch-name>```  

In questo modo entrambe le modifiche risulteranno in un unico commit.  

