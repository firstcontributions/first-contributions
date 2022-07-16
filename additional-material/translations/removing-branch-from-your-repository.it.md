# Rimuovere un ramo (branch) dal tuo repository

Se hai seguito il tutorial fino ad ora, il nostro ramo `<add-your-name>` ha esaurito il suo scopo, è ora di eliminarlo dal repository della tua macchina locale. Ciò non è strettamente necessario, ma lo scopo piuttosto specifico del ramo è stato assolto, possiamo quindi eliminarlo.  

Per prima cosa, unisci il tuo `<add-your-name>` al tuo ramo principale, quindi vai al tuo ramo principale:  
```
git checkout master
```

Unisci `<add-your-name>` al tuo ramo principale:
```
git merge <add-your-name> master
```

Rimuovi `<add-your-name>` dal repository della tua macchina locale:  
```
git branch -d <add-your-name>
```

Ora hai cancellato il ramo `<add-your-name>` dalla tua macchina locale e tutto è in ordine.
Sebbene, a questo punto, dovresti avere ancora il  ramo `<add-your-name>` nel tuo fork di GitHub. Tuttavia, prima di eliminarlo, non dimenticare di aver già inviato una "*Pull request*" al mio repository da questo ramo remoto. Quindi, a meno che io non lo abbia già unito, non cancellare questo branch.  

Se, quando avrò unito il tuo branch, vorrai cancellare il ramo remoto, usa:  
```
git push origin --delete <add-your-name>
```

Ora sai come tenere in ordine i tuoi rami.  
Con il tempo, molti commit saranno aggiunti al mio repository pubblico. E i rami principali dei branch della tua macchina locale e del tuo fork GitHub non saranno più aggiornati. Per mantenere i tuoi repository sincronizzati con il mio, segui i passaggi seguenti:  

#### [Mantieni il tuo fork sincronizzato con il repository](keeping-your-fork-synced-with-this-repository.it.md)
