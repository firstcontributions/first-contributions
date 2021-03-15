# Rimuovere un file da Git

Può succedere che tu voglia rimuovere un file da Git, mantenendolo comunque nel tuo computer. Lo puoi fare eseguendo questo comando:

``git rm <file> --cached``

## Cosa fa questo comando?

Git non terrà più conto dei cambiamenti inclusi nel file rimosso. Per Git, è come se tu avessi cancellato il file. Se però vai a cercare il file nel tuo sistema, vedrai che comunque è ancora lì. 

Come vedi, nell'esempio qui sopra viene usato il flag `--cached`. Senza questo flag Git rimuoverebbe il file non solamente dal repository, ma anche dal tuo sistema. 

Se decidi di validare questo cambiamento con `git commit -m "Remove file1.js"` e successivamente invii le modifiche al repository remoto usando `git push origin master`, vedrai che il repository remoto avrà rimosso il file. 

## Funzioni aggiuntive

- Per rimuovere più di un file, puoi aggiungerli tutti allo stesso comando in questo modo:

    `git rm file1.js file2.js file3.js --cached`

- Puoi usare il metacarattere asterisco (*) per rimuovere i file simili tra loro. Per esempio, se vuoi rimuovere tutti i file con estensione .txt dal tuo repository locale puoi farlo così:

    `git rm *.txt --cached`
