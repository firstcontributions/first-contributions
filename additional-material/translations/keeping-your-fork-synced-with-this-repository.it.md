# Mantieni il tuo fork sincronizzato con il repository

Prima di tutto, devi comprendere il flow di una sincronizzazione completa, poiché è molto importante. In questo schema, ci sono 3 diversi repository: il mio repository pubblico su Github `github.com/firstcontributions/first-contributions.git`, il tuo fork del repository su GitHub `github.com/Your-Name/first-contributions/` e il repository sulla tua macchina locale da cui si suppone tu stia operando. Questo tipo di cooperazione è tipica dei progetti open source ed è chiamata `Triangle Workflows`.

<img style="float;" src="../../assets/triangle_workflow.png" alt="triangle workflow" />

Per mantenere aggiornati (*up-to-date*) i tuoi due repository con il mio repo pubblico, dobbiamo prima recuperare (*fetch*) ed unire (*merge*) il repository pubblico con il repository della tua macchina locale. Il secondo passo sarà quello di *pushare* il tuo repo locale al tuo fork su Github. Come visto in precedenza, è solo dal tuo fork che puoi effettuare una "pull request". Quindi il tuo fork su Github è l'ultimo repo ad essere aggiornato.

Vediamo ora come fare:  

Prima, devi essere nel tuo ramo (*branch*) *master*. Per sapere in quale ramo ti trovi, controlla la prima riga del comando:  
```
git status
```
e se non sei su *master* esegui:  
```
git checkout master
```
Quindi dovresti aggiungere il mio repo pubblico al tuo git con `add upstream remote-url`:  
```
git remote add upstream https://github.com/firstcontributions/first-contributions.git
```
Questo è un modo per dire a git che un'altra versione di questo progetto esiste nella URL specificata e la chiamiamo `upstream`. Una volta che il tuo git ha un nome, andiamo a prendere l'ultima versione del repository pubblico:  
```
git fetch upstream
```

Hai appena *fetchato* l'ultima versione del mio fork (`upstream` remoto). Ora devi unire il repository pubblico nel tuo ramo principale.  
```
git rebase upstream/master
```
Con questo comando stai unendo il repository pubblico con il tuo ramo principale. Il ramo principale della tua macchina locale è ora aggiornato. Infine, se *pushi* il ramo principale sul tuo fork, anche il tuo fork GitHub avrà le modifiche:
```
git push origin master
```
Nota il comando, tu stai *pushando* al ramo remoto chiamato `origin`.  

Quindi a questo punto, tutti i tuoi repository sono aggiornati. Ben fatto! Dovresti far questo ogni volta che il tuo repository GitHub ti dice che sei indietro di qualche commit.  
