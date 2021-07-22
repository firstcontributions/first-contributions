# Spostare un commit in un ramo (branch) diverso

Cosa fare se committi una modifica e ti accorgi che hai committato in un branch diverso?  
Come correggere l'errore? Ciò è spiegato qui di seguito. 

## Spostamento degli ultimi commit in un branch esistente
Per fare questo, digita:  

```git reset HEAD~ --soft``` - Annulla l'ultimo commit, ma lascia le modifiche disponibili.  
```git stash``` - Accantona (*stash*) lo stato della directory, conservandolo in vista di un successivo riutilizzo. 

```git checkout name-of-the-correct-branch``` - Passa all'altro branch.  
```git stash pop``` - Rimuove l'ultimo stato accantonato.  
```git add .``` - Oppure prova ad aggiungere singoli file.  
```git commit -m "your message here"``` - Salva e committa le modifiche.  

Ora le tue modifiche sono nel ramo corretto.  

## Spostamento degli ultimi commit in un nuovo Branch
Per fare ciò, digita:  
```git branch name-of-the-new-branch``` -  Crea un nuovo ramo salvando tutti i commit.  
```git reset --hard HEAD~#``` - Posiziona il ramo principale (*master*) indietro di # commit. Ricorda, questi commit saranno eliminati dal ramo principale.  
```git checkout name-of-the-new-branch``` - Porta sul nuovo ramo creato, il quale ha ora tutti i commit.  

Ricorda: eventuali modifiche non committate andranno PERSE.  
