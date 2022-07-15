# Creazione di un file .gitignore

Il file *.gitignore* è un file di testo che dice a Git quali file o cartelle ignorare in un progetto.  

Un file *.gitignore* locale è solitamente posizionato nella cartella radice di un progetto. Puoi anche creare un file *.gitignore* globale e qualsiasi voce in questo file verrà ignorata in tutti i tuoi repository Git.  

## Perché .gitignore
Ora potresti domandarti perché volere che git ignori certi file e cartelle. Questo perché non vogliamo che siano tracciati file come quelli di *build*, di cache, altri file di configurazione locale come i *node_modules*, di compilazione, file temporanei creati dall'*IDE*, ecc. Normalmente è usato per evitare di committare file temporanei della tua cartella di lavoro che non sono di utilità per i tuoi collaboratori.  

## Per iniziare
Per creare un file *.gitignore* locale, crea un file di testo e chiamalo ```.gitignore``` (ricordati di includere il ```.``` all'inizio). Poi modifica questo file in base alle tue necessità. Ciascuna nuova linea dovrebbe elencare un file o una cartella aggiuntiva che vuoi che Git ignori.  

Le voci in questo file possono anche seguire uno schema di corrispondenza (*matching pattern*).  

```
* è usato come un carattere jolly
/ è usato per ignorare i nomi di percorso relativi al file .gitignore
# è usato per aggiungere commenti a un file .gitignore

Questo è un esempio di come può essere un file .gitignore:

# Ignora i file di sistema MAC
.DS_store

# Ignora la cartella node_modules
node_modules

# Ignora tutti i file di testo
*.txt

# Ignora i file relativi alle API keys
.env

# Ignora i file di configurazione SASS
.sass-cache

```
Per aggiungere o cambiare il tuo file *.gitignore* globale, esegui il seguente comando:

```
git config --global core.excludesfile ~/.gitignore_global

```

Questo comando creerà il file ```~/.gitignore_global```. Ora puoi modificare questo file allo stesso modo di un file *.gitignore* locale. Tutti i tuoi repository locali ignoreranno i file e le cartelle elencate nel file *.gitignore* globale.  

## Come annullare il tracciamento dei file precedentemente committati dal nuovo .gitignore

Per annullare il tracciamento di un singolo file, ad esempio fermare il tracciamento del file, ma non cancellarlo dal sistema in uso:  

```
git rm --cached filename
```

Per annullare il tracciamento di ogni file nel *.gitignore*:  

Innanzitutto, committa tutte le modifiche in sospeso nel codice, e poi esegui:  

```
git rm -r --cached
```

Questo rimuove tutte le modifiche ai file nell'indice (*staging area*), poi esegui:  

```
git add .
```
Committa:

```
git commit -m ".gitignore is now working"
```

Per annullare ```git rm --cached filename```, usa ```git add filename```
