# Ripristino (o annullamento) di un commit (Revert)

Ripristinare un commit significa semplicemente creare un commit nuovo di zecca che annulla tutti i cambiamenti fatti nel precedente. E' come fare un ```CTRL + Z ``` su git.

Git semplifica il ripristino perché ogni commit inviato al tuo repository remoto ha una chiave alfanumerica univoca collegata, conosciuta come SHA (Secure Hash Algorithm). Questo significa che puoi ripristinare qualsiasi commit fintanto che hai lo SHA. Devi però stare attento a ripristinare ordinatamente per non rovinare il tuo repository.

Per scegliere lo SHA dello specifico commit che vuoi annullare, un log di tutti i commit che abbiamo fatto finora sarebbe utile. Per ottenerlo digitiamo il comando:
```git log --oneline ```
Lo otterremmo anche eseguendo il solo ```git log ``` ma in forma estesa. Tuttavia usando il flag ```--oneline ``` diciamo a git di visualizzarli in forma concisa (su una riga) per una facile lettura.

I primi 7 caratteri visualizzati eseguendo questo comando sono chiamati *hash di commit abbreviato*.  

Per esempio, di seguito è ciò che ottengo eseguendo ```git log --oneline ``` su questo repository:  
```
389004d added spacing in title
c1b9fc1 Merge branch 'master' into tutorials
77eaafd added tutorial for reverting a commit
```  
Questo ci mostra che con ```git log --oneline``` possiamo recuperare una lista di tutti i commit fatti sul repository insieme ai primi 7 caratteri del suo SHA.  

Ora, supponiamo che io voglia annullare il mio commit di "added spacing in title", in questo caso dovrei eseguire i passaggi seguenti:

*   Copiare lo SHA del commit che, in questo caso, è ```389004d```
*   Eseguire poi il comando ```git revert 389004d```

Questo aprirà il mio editor e mi chiederà di modificare il messaggio di commit. Posso lasciare il messaggio di commit default di git che inizia con la parola `Revert` o posso decidere di personalizzare il messaggio a mio piacimento.

*   Di seguito, salvare e chiudere l'editor di testo.  
*   Tornare alla riga di comando.  
*   Eseguire ```git push origin <branch-name>``` per inviare le modifiche ripristinate a GitHub.  

E questo è tutto, i cambiamenti saranno annullati. In questo caso, il mio repository verrà ripristinato a come appariva in ```c1b9fc1```  
