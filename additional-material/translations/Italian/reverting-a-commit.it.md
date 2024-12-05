# ripristinare una commit

Ripristinare (*revert) una commit significa creare una nuova commit che elimina tutti
i cambiamenti apportati da quella precedente. È come fare un ```ctrl + Z``` su git.

Il ripristino è reso più semplice in git perchè ogni commit che invii (*push) nella tua repository remota ha un'unica chiave alfanumerica associata, questa chiave è chiamata SHA (Secure Hash Algorithm).
questo significa che puoi ripristinare una commit fintanto che possiedi la sua chiave SHA.
ad ogni modo, bisogna prestare attenzione a ripristinare le commit in modo ordinato in modo da non mettere in disordine la tua repository.

Per ottenere la chiave SHA della commit che vuoi ripristinare, viene in aiuto il log di tutte le commit che sono state fatte.
per ottenere questo log possiamo utilizzare il comando:
```git log --oneline ```
Usando il comando ```git log``` da solo si ottengono comunque le SHA (in formato lungo)
utilizzando però la flag ```--oneline ``` diciamo a git che vogliamo stampare a video un formato conciso (una linea) per facilitare la lettura.

I primi 7 caratteri stampati quando esegui questo comando rappresentano un abbreviazione dell'hash della commit.

Per esempio, questo è quello che ottengo quando eseguo ```git log --oneline ``` su questa repository:
```
389004d added spacing in title
c1b9fc1 Merge branch 'master' into tutorials
77eaafd added tutorial for reverting a commit
```

Questo esempio dimostra come con ```git log --oneline```, possiamo ottenere la lista di commit fatte sulla repository assieme ai primi 7 caratteri del suo SHA.

Supponiamo ora che io voglia ripristinare la commit "added spacing in title", per fare questo seguirei questi passaggi:

*   Copio lo SHA della commit che, in questo caso è ```389004d```
*   poi, eseguo il comando ```git revert 389004d```

Facendo questo si apre il mio editor di testo e mi viene chiesto di modificare il messaggio di commit.
Puoi decidere di lasciare il messaggio di default che inizia con la parola `Revert`
oppure puoi anche decidere di personalizzare il messaggio come preferisci.

*   In seguito, salvo il messaggio e chiudo l'editor di testo.
*   Vengo mandato nella linea di comando.
*   eseguo ```git push origin <branch-name>``` per inviare i cambiamenti ripristinati su Github.

E questo è tutto, i cambiamenti vengono eliminati. Nel mio caso, la repository viene ripristinata allo stesso stato di com'era in ```c1b9fc1```