# Configurazione di git

La prima volta che provi ad eseguire un commit utilizzando git, potresti ricevere un messaggio sul *prompt* come il seguente:  

```bash
$ git commit
*** Please tell me who you are.

Run

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
```

Git ha bisogno di sapere chi sei quando crei un commit. Quando lavori in collaborazione, dovresti essere in grado di vedere chi ha modificato quali parti del progetto e quando, è per questo che git è progettato per creare commit legati ad un nome e ad un email.  

Esistono diversi modi di fornire al comando `git commit` la tua email e il tuo nome, e ne esamineremo qui alcuni.  

### Configurazione globale

Quando memorizzi qualcosa nella configurazione globale, è accessibile a livello di sistema in tutti i repository su cui lavori. Questo è il metodo preferito e funziona per la maggior parte dei casi d'uso.  

Per memorizzare qualcosa nella configurazione globale, utilizziamo il comando `config` come segue:  

`$ git config --global <variable name> <value>`

Nel caso dei dettagli dell'utente, lo eseguiamo in questo modo:  

```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### Configurazione di repository

Come dice il nome, queste configurazioni sono limitate al tuo repository corrente. Se vuoi committare in un particolare repository, ad esempio, un progetto legato al lavoro, con l'email aziendale, puoi utilizzare questo metodo.  

Per memorizzare qualcosa nella configurazione del repository, usa il comando `config` senza il flag `--global` come segue:  

`$ git config <variable name> <value>`

Nel caso si tratti di dettagli dell'utente, lo usiamo nel modo seguente:  

```
$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
```

### Configurazione dalla riga di comando

Questi tipi di configurazione sono limitati al solo comando eseguito. Tutti i comandi git accettano argomenti `-c` prima del verbo di azione per impostare i dati di configurazione temporanei.  

Per memorizzare qualcosa nella configurazione della riga di comando, utilizza:  

`$ git -c <variable-1>=<value> -c <variable-2>=<value> <command>`

Nel nostro esempio eseguiremo il comando commit come segue:  

`git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Your commit message"`

### Note sulla precedenza

Tra i tre metodi descritti qui, l'ordine di precedenza è `command-line > repository > global`. Ciò significa che se una variabile è configurata sia nella riga di comando che a livello globale, il valore della riga di comando verrà utilizzato per l'operazione.  

### Oltre i dettagli dell'utente

Finora abbiamo trattato solo i dettagli dell'utente mentre lavoravamo con la configurazione. Tuttavia, sono disponibili molte altre opzioni. Alcune sono:  

1.  `core.editor` - per specificare il nome dell'editor di testo utilizzato per scrivere i messaggi di commit, ecc.  
2.  `commit.template` - per specificare un file nel sistema come modello di commit iniziale.  
3.  `color.ui` - per specificare un valore booleano per l'utilizzo dei colori nell'output di git.  

Abbiamo sintetizzato alcuni dettagli per facilitarne la comprensione. Per ulteriori approfondimenti, visita [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).  
