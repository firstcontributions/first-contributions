# Cos'è un conflitto di unione (merge)?

Quando provi a mergiare un altro ramo nel tuo attuale ramo di lavoro, stai prendendo dei cambiamenti da un altro contesto combinandoli con i tuoi file di lavoro correnti.  
Se due persone hanno cambiato le stesse linee nello stesso file, o se una persona ha deciso di eliminarlo mentre l'altra persona ha deciso di modificarlo, Git non può sapere qual'è la versione corretta, quindi contrassegnerà il file come in conflitto - il quale andrà risolto prima di poter continuare il lavoro.  

# Come risolvere un conflitto di unione?

Quando ti trovi un conflitto di unione, git evidenzierà l'area problematica nel file racchiudendola in “<<<<<<<< HEAD” e “>>>>>>>>>>[other branch name]”  

Il contenuto dopo il primo marcatore proviene dal ramo di lavoro corrente. Dopo le parentesi angolari, Git ci mostra l'origine (da quale branch) delle modifiche. Una linea con "=======" separa le due modifiche in conflitto.  
Il nostro compito ora è di correggere queste linee: una volta finito, il file dovrebbe essere esattamente come nelle nostre intenzioni. Si consiglia di consultarsi con l'autore delle modifiche in conflitto per decidere quale versione dovrà essere quella finale. Potrebbe essere una delle due oppure un misto fra le due.  

e.g. :
```
 <<<<<<< HEAD:mergetest
 This is my third line
 =======
 This is a fourth line I am adding
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Indica l'inizio delle righe dove si trova il conflitto. Il primo gruppo di linee sono le righe del file che stavi cercando di modificare per unire i cambiamenti.  
`=======`: Indica il punto di interruzione usato per la comparazione. Suddivide i cambiamenti che l'utente ha committato (sopra) e i cambiamenti che provengono dal merge (sotto) per differenziare visibilmente le modifiche.  
`>>>>>>>`: Indica la fine delle linee che hanno un conflitto di unione.  

Puoi risolvere il conflitto editando il file e poi unire manualmente le parti del file che git ha avuto problemi a mergiare. Questo può significare scartare le tue modifiche o quelle di qualcun altro o andare avanti con un mix delle due. Sarà inoltre necessario eliminare '<<<<<<<', '=======', e '>>>>>>>' dal file.  

Una volta risolto il conflitto, esegui un `git add`. Non dimenticare di eseguire i test, poiché dovrai verificare di averlo risolto.  

Puoi anche scaricare diversi plugin, a seconda dell'IDE che stai utilizzando, per risolvere più facilmente i conflitti.  

# Come annullare un merge?
Se vuoi annullare un merge, esegui `git merge —abort`
