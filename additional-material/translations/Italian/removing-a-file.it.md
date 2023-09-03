# Rimuovere un file da Git

Talvolta, potresti voler rimuovere un file da Git non eliminandolo dal tuo computer. Lo puoi fare utilizzando il seguente comando:

``git rm <file> --cached``

## Cosa fa questo comando?

Git non terrà più traccia dei cambiamenti inclusi nel file rimosso. Per Git, è come se tu avessi cancellato il file. Se però vai a cercare il file nel tuo sistema, vedrai che comunque è ancora lì. 

Come vedi, nell'esempio qui sopra viene usata la flag `--cached`. Senza questa flag, Git rimuoverebbe il file non solamente dal repository, ma anche dal tuo sistema. 

Se decidi di validare questo cambiamento con `git commit -m "Remove file1.js"` e successivamente inviare le modifiche al repository remoto usando `git push origin master`, vedrai che il repository remoto avrà rimosso il file. 

## Funzioni aggiuntive

- Se vuoi rimuovere più di un file, puoi aggiungerli tutti allo stesso comando in questo modo:

    `git rm file1.js file2.js file3.js --cached`

- Puoi usare il metacarattere asterisco (*) per rimuovere i file simili tra loro. Per esempio, se vuoi rimuovere tutti i file con estensione .txt dal tuo repository locale, puoi farlo così:

    `git rm *.txt --cached`
