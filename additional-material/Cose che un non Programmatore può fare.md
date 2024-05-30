# Cose che un non programmatore può fare
## Inizia ad ascoltare

Tutto nell'open source coinvolge altre persone.
Vuoi unirti a un team e questo significa capire la comunità e come funziona.
Entrare in un progetto e dire "Ciao, ecco cosa penso che questo progetto dovrebbe fare" di solito non è ben visto.
Alcuni progetti possono accogliere questo approccio, ma se il progetto è attivo da un po', le probabilità che questo atteggiamento sia accettato sono basse.
**Ascoltare è il modo migliore per sapere di cosa ha bisogno il progetto.**

1. **Unisciti a una mailing list**: Per molti progetti, la mailing list è il principale canale di comunicazione riguardo allo sviluppo del progetto.
Nei grandi progetti, ci sono molte mailing list tra cui scegliere.
Ad esempio, il progetto PostgreSQL ha non meno di 12 liste orientate agli utenti e sei liste per gli sviluppatori sulla sua pagina delle mailing list.
Suggerisco di seguire la lista principale orientata agli utenti e la lista dei core developer per iniziare ad ascoltare.

2. **Segui un blog**: I blog mantenuti dai core developer spesso forniscono informazioni su cosa ci sarà nelle prossime versioni e su cosa è stato necessario per arrivarci. Un sito "planet" aggrega notizie e post di blog da molte fonti legate al progetto. Se esiste un sito "planet", come planet.gnome.org o planet.mysql.com, inizia da lì. Cerca su Google "planet <nomedelprogetto>."

3. **Unisciti a un canale IRC**: Molti progetti open source hanno canali IRC (Internet Relay Chat) dedicati dove sviluppatori e utenti si incontrano per discutere problemi e sviluppo.
Controlla il sito web del progetto per i dettagli su come si chiama il canale e su quale rete IRC si trova.

**Lavora con i Ticket**  
Il codice è il cuore di qualsiasi progetto open source, ma non pensare che scrivere codice sia l'unico modo per contribuire.
La manutenzione del codice e dei sistemi circostanti spesso viene trascurata nella corsa a creare nuove funzionalità e correggere bug.
Guarda a queste aree come un modo semplice per entrare in un progetto.
La maggior parte dei progetti ha un sistema di ticket visibile al pubblico, collegato dalla pagina principale del sito web del progetto e incluso nella documentazione.
È il principale canale di comunicazione tra utenti e sviluppatori. Mantenendolo aggiornato è un ottimo modo per aiutare il progetto.
Potrebbe essere necessario ottenere permessi speciali nel sistema di ticketing, che la maggior parte dei leader del progetto sarà felice di darti quando dici che vuoi aiutare a ripulire i ticket.

4. **Diagnostica un bug**: I bug sono spesso riportati male.
Diagnosticare e triagolare un bug può aiutare a risparmiare tempo agli sviluppatori facendo il lavoro preliminare di capire i dettagli del problema.
Se un utente ha segnalato, "Il software non funziona quando faccio X", dedica del tempo a capire i dettagli di quel problema.
È ripetibile? Puoi creare una serie di passaggi per causare il problema ripetutamente? Puoi restringere il problema, come accade solo su un browser ma non su un altro, o su una distro ma non su un'altra?

Anche se non sai cosa causa il problema, lo sforzo che metti nel restringere le circostanze rende più facile per qualcun altro risolverlo.
Qualunque cosa scopri, aggiungila al ticket nel sistema di bug per tutti.

5. **Chiudi i bug risolti**: Spesso i bug vengono risolti nel codice ma i ticket riportati non vengono aggiornati nel sistema di ticketing.
Pulire questo disordine può richiedere tempo, ma è prezioso per l'intero progetto.

Inizia interrogando il sistema di ticket per ticket più vecchi di un anno e verifica se il bug esiste ancora.
Controlla il changelog del progetto per vedere se il bug è stato risolto e può essere chiuso.
Se è noto che è stato risolto, annota il numero di versione nel ticket e chiudilo.

Prova a ricreare il bug con l'ultima versione del software.
Se non può essere ricreato con l'ultima versione, annotalo nel ticket e chiudilo.
Se esiste ancora, annotalo nel ticket e lascialo aperto.

**Lavorare con il Codice**  
I programmatori di tutti i livelli di esperienza possono aiutare con il codice nel progetto.
Non pensare che devi essere un genio della programmazione per fare contributi reali al tuo progetto preferito.

Se il tuo lavoro comporta modifiche al codice, indaga sul metodo che il progetto usa per ottenere codice dai contributori.
Ogni progetto ha il proprio flusso di lavoro, quindi chiedi come fare prima di iniziare a inviare codice.

Ad esempio, il progetto PostgreSQL è molto rigoroso nel suo processo: le modifiche al codice vengono inviate sotto forma di patch a una mailing list dove i core developer scrutinano ogni aspetto del cambiamento. Dall'altra parte c'è un progetto come Parrot dove è facile ottenere privilegi di commit nel codice. Se il progetto utilizza GitHub, potrebbe esserci un flusso di lavoro che utilizza la funzionalità pull request di GitHub. Nessun progetto è uguale all'altro.

Ogni volta che modifichi il codice, assicurati di agire come un membro responsabile della comunità e mantieni il tuo stile di codice in linea con il resto del codice base. Il codice che aggiungi o modifichi dovrebbe sembrare come il resto. Potrebbe non piacerti lo stile delle parentesi o la gestione degli spazi per l'indentazione, ma è scortese inviare una modifica del codice che non rispetta gli standard esistenti. È come dire "Non mi piace il tuo stile e penso che il mio sia migliore, quindi dovresti farlo a modo mio."

6. **Testa una beta o una release candidate**: Qualsiasi progetto progettato per funzionare su più piattaforme può avere tutti i tipi di problemi di portabilità.
Quando una release si avvicina e viene pubblicata una beta o una release candidate, il leader del progetto spera che venga testata da molte persone su molte piattaforme diverse.
Puoi essere una di quelle persone e aiutare a garantire che il pacchetto funzioni sulla tua piattaforma.

Tipicamente devi solo scaricare, compilare e testare il software, ma il valore per il progetto può essere enorme se usi una distribuzione o un hardware non comune.
Solo riportando che la compilazione e il test funzionano, aiuti i leader del progetto a sapere che la release imminente è solida.

7. **Correggi un bug**: Questo è di solito dove i contributori che vogliono lavorare sul codice iniziano.
È semplice: trova un bug interessante nel sistema di ticket e prova a correggerlo nel codice.
Documenta la correzione nel codice se è appropriato.
È una buona idea aggiungere un test alla suite di test per verificare la parte di codice che hai corretto; alcuni progetti richiedono che le correzioni dei bug includano test. Tieni appunti mentre esplori questo codice non familiare. Anche se non riesci a correggere il bug, documenta nel ticket ciò che hai scoperto durante il tentativo di correzione. Ciò che trovi aiuta coloro che vengono dopo di te.

8. **Scrivi un test**: La maggior parte dei progetti ha una suite di test che testa il codice, ma è difficile immaginare una suite di test che non potrebbe avere più test aggiunti.
Utilizza uno strumento di copertura dei test come gcov per C, o Devel::Cover per Perl per identificare aree nel codice sorgente che non sono testate dalla suite di test.
Quindi, aggiungi un test alla suite per coprirle.

9. **Silenzia un avviso del compilatore**: Il processo di build per molti progetti basati su C spesso genera qualche avviso del compilatore sullo schermo.
Questi avvisi di solito non indicano un problema, ma possono sembrarlo.
Avere troppi avvisi può far sembrare il compilatore come il ragazzo che gridava "Al lupo!".
Verifica se il codice potrebbe effettivamente nascondere un bug. Se no, modificare il sorgente per silenziare aiuta a nascondere questi falsi positivi.

10. **Aggiungi un commento**:
Quando stai scavando nel codice, potresti trovare alcuni punti che sono confusi.
È probabile che se eri confuso tu, lo saranno anche altri. Documentali nel codice e invia una patch.

**Lavorare con la Documentazione**  
La documentazione è tipicamente la parte di un progetto che riceve meno attenzione.
Può anche soffrire del fatto di essere stata scritta dal punto di vista di coloro che sono familiari con il progetto, piuttosto che attraverso gli occhi di qualcuno che sta appena entrando.
Se hai mai letto documenti per un progetto in cui pensi, "Sembra che questo manuale presuma che io sappia già come usare il pacchetto," sai di cosa sto parlando.
Spesso un set di occhi freschi può evidenziare carenze nella documentazione che quelli vicini al progetto non notano.



11. **Crea un esempio**: Non esiste un progetto che abbia troppi esempi pratici.
Che sia un'API web, una libreria di routine, un'app GUI come Gimp o uno strumento da riga di comando,
un buon esempio di utilizzo corretto può spiegare più chiaramente e rapidamente l'uso corretto del software rispetto a pagine di documentazione.
Per un'API o una libreria, crea un programma di esempio che utilizza lo strumento. Questo potrebbe anche essere estratto dal codice che hai scritto, ridotto all'essenziale.
Per uno strumento, mostra esempi reali di come lo hai utilizzato nella tua vita quotidiana. Se sei orientato visivamente,
considera di creare una cattura dello schermo di un processo importante, come l'installazione dell'applicazione.

**Lavorare con la Comunità**  
L'open source riguarda solo in parte il codice. La comunità rende l'open source funzionante. Ecco modi in cui puoi aiutare a costruirla.

12. **Rispondi a una domanda**: Il modo migliore per aiutare a costruire la comunità è aiutare gli altri.
Rispondere a una domanda, soprattutto da qualcuno che sta appena iniziando, è cruciale per aiutare il progetto a crescere e prosperare.
Il tempo che dedichi ad aiutare un principiante, anche se sta facendo una domanda a cui potresti facilmente rispondere con un rapido "RTFM," ripaga nel lungo periodo nell'avere un altro membro attivo della comunità.
Tutti iniziano da qualche parte, e i progetti hanno bisogno di un costante afflusso di persone se vogliono rimanere vitali.

13. **Scrivi un post sul blog**:
Se hai un blog, scrivi delle tue esperienze con il progetto che stai utilizzando.
Racconta di un problema che hai affrontato utilizzando il software e di come lo hai risolto.
Aiuterai in due modi, sia mantenendo il progetto nelle menti degli altri intorno a te,
sia creando un record per chiunque altro abbia il tuo problema in futuro e cerchi sul web la risposta.
(Un blog delle tue avventure tecniche è anche un ottimo modo per mostrare l'esperienza nel mondo reale con il software in questione la prossima volta che cerchi un lavoro utilizzandolo.)

14. **Migliora un sito web**:
Se hai competenze in web design e puoi aiutare a migliorare il sito web, e quindi l'immagine pubblica del progetto, è tempo ben speso.
Forse il progetto potrebbe usare un restyling grafico, o un logo per identificare il progetto.
Queste possono essere competenze mancanti nella comunità. So che mi piacerebbe avere aiuto nel design grafico sui siti web dei miei progetti.
  
15. **Scrivi documentazione tecnica**:
Se puoi scrivere su come funziona un'applicazione o un pezzo di software, potresti scrivere documentazione tecnica su di essa. Specialmente i progetti open source che cercano di aggiornare, rinnovare, espandere o creare documentazione tecnica per il pubblico generale. Più scrivi in modo semplice, meglio è. La parte migliore è che non devi essere un programmatore per scrivere documentazione tecnica.

Soprattutto, ascolta ciò di cui le persone intorno a te discutono. Vedi se riesci a riconoscere una necessità pressante. Ad esempio, recentemente sulla mailing list degli sviluppatori di Parrot, è stato deciso di utilizzare GitHub come sistema di ticketing, abbandonando la vecchia installazione di Trac che avevano. Alcune persone erano contrarie al cambiamento perché non c'era modo di convertire i ticket nel sistema di GitHub. Dopo un giorno di discussioni, intervenni e dissi "Che ne dici se scrivo un convertitore?" Le persone erano entusiaste dell'idea. Ho passato del tempo a scrivere un programma di conversione per oltre 450 ticket, così non abbiamo perso nessuna cronologia dei ticket. È stato un grande successo. Sono riuscito a contribuire, e i core developer sono rimasti concentrati sul lavoro su Parrot.

16. **Insegna e aiuta gli altri**:
Il modo migliore per imparare di più su un argomento è provare a insegnarlo.
Il miglior insegnante è colui che può spiegare cose complesse con esempi semplici. Quindi devi cercare di essere il miglior insegnante per essere il miglior allievo e il migliore nel tuo mondo della programmazione. Insegnare agli altri ti farà sentire meglio con te stesso e ti aiuterà a migliorare le tue competenze e conoscenze nella tua professione. Quando ricevi aiuto da qualcuno non tenerlo per te stesso, condividilo con gli altri. Rendi il mondo un posto migliore in cui vivere.