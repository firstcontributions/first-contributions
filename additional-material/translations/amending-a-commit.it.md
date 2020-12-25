# Modifica di un commit (amend)

E se invii una modifica al tuo repository remoto e ti accorgi solo dopo di un errore di battitura nel messaggio di commit o hai dimenticato di aggiungere una linea nel tuo commit più recente.  
Come lo modifico? Questo è quello che spieghiamo in questo tutorial.  

## Modifica di un messaggio di commit recente dopo che hai effettuato il push su GitHub.  
Per fare questo senza aprire un file:
* Digita ```git commit --amend -m "seguito dal tuo nuovo messaggio di commit"```
* Esegui ```git push origin <branch-name>``` per committare le modifiche al repository.  

Nota: se tu digiti solamente  ```git commit --amend```, il tuo editor di testo si aprirà chiedendoti di modificare il messaggio di commit. Aggiungendo il flag ``-m`` eviti l'apertura dell'editor.  

## Modifica su un singolo commit

Quindi, cosa succede se ci dimentichiamo di apportare una piccola modifica ad un file, come cambiare una singola parola se abbiamo già pushato il commit al nostro repository remoto?  

Quello che mostro qui è un log dei miei commit:
```
g56123f create file bot file
a2235d updated contributor.md
a5da0d modified bot file
```

Facciamo che ho dimenticato di aggiungere una singola parola al file del bot.

Ci sono due modi per fare questo. Il primo è avere un commit completamente nuovo che contenga la modifica, in questo modo:
```
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
b0ca8f added single word to botfile
```
Il secondo modo è modificare (to amend) il commit a5da0d, aggiungere questa nuova parola e inviarlo a Github come un unico commit.
Il secondo modo risulta migliore poiché è solo un piccolo cambiamento.  

Per ottenere questo risultato, dovremo fare quanto segue:  
* Modificare il file. In questo caso modifico il botfile per includere la parola che ho omesso in precedenza.  
* Successivamente, aggiungi il file nell'area di staging con il comando ```git add <filename>```  

Normalmente dopo aver aggiunto i file all'area di staging, la prossima cosa che facciamo è *git commit -m "il nostro messaggio di commit"*, giusto?  

SIccome ciò che vogliamo ottenere in questo caso è modificare il commit precedente, dovremo eseguire questi comandi:

* ```git commit --amend```  
In questo modo verrà visualizzato l'editor di testo e verrà richiesto di modificare il messaggio. Puoi decidere di lasciare il messaggio com'era o di modificarlo.  
* Esci dall'editor  
* Esegui il push delle modifiche con ```git push origin <branch-name>```  

In questo modo entrambe le modifiche risulteranno in un unico commit.  

