[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-hfcq788y-QaXzXT5clBBWukXQyBhH4w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)  
#### _Leggilo in [altre lingue](../translations/Translations.md)._  
  
# 


# La prima contribuzione

È dura. È sempre difficile fare qualcosa per la prima volta. Specialmente quando si sta contribuendo sbagliare ci mette a disagio. L'Open Source, però, si basa sulla collaborazione e sul lavorare insieme. Per questo vogliamo semplificare il modo in cui i nuovi collaboratori imparano e contribuiscono per la prima volta a progetti Open Source.

Leggere articoli e guardare tutorial può essere utile, ma cosa c'è di meglio che provare a fare effettivamente le cose sul campo? Questo progetto punta ad essere una guida per i meno esperti. Ricorda: più sei rilassato, meglio imparerai. Se vuoi contribuire per la prima volta, segui i semplici passi elencati qui sotto. Ti promettiamo che sarà divertente.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="forka questo repo" />

Se non hai git sul tuo computer, [installalo](https://help.github.com/articles/set-up-git/).

## Forka questo repository

Forka questo _repo_ (abbreviazione di _repository_, ossia una cartella) cliccando sul bottone **_Fork_** in cima alla pagina.
Questo creerà una copia di questo repository nel tuo account.

## Clona il repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clona questo repository" />

Ora clona questo repo nel tuo computer. Clicca sul pulsante per clonare e poi fai click sull'icona _copy URL to clipboard_.

Apri il terminale e lancia il seguente comando git:

```
git clone "url appena copiato"
```
dove "url appena copiato" (senza le virgolette) è l'url di questo repository (il tuo fork di questo progetto). Leggi i precedenti passaggi per ottenere l'url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Per esempio:
```
git clone https://github.com/questo-sei-tu/first-contributions.git
```
dove `questo-sei-tu` è il tuo username GitHub. Qui stai copiando il contenuto del repository first-contributions da GitHub al tuo computer.

## Crea un branch

Entra nella cartella del repository sul tuo computer (se non lo hai già fatto):

```
cd first-contributions
```

Ora crea un branch usando il comando `git checkout`:

```
git checkout -b <aggiungi-il-tuo-nome>
```

Ad esempio:

```
git checkout -b aggiungi-alonzo-church
```

(Non è necessario inserire la parola _aggiungi_ nel nome del branch, ma in questo caso è ragionevole includerlo poiché lo scopo di questo branch è aggiungere il tuo nome alla lista. 
Lo scopo di nominare un branch è descrivere le modifiche che andremo ad effettuare, il nome deve essere quindi _parlante_ e non generico per facilitare il team con cui si collabora).

## Fai le modifiche necessarie e crea un commit

Ora apri il file `Contributors.md` in un editor, inserisci il tuo nome. Non aggiungere il nome all'inizio o alla fine del file, mettilo nel mezzo. Ora salva il file.

Se vai nella cartella del progetto ed esegui il comando `git status`, vedrai quali sono i cambiamenti.

Aggiungi le modifiche al branch appena creato usando il comando `git add`:

```
git add Contributors.md
```

Crea ora un commit che includa le modifiche da te fatte, usando il comando `git commit`:

```
git commit -m "Add <il-tuo-nome> to Contributors list"
```

cambiando `<il-tuo-nome>` con il tuo nome.

## Invia le modifiche a GitHub

Invia le tue modifiche con il comando `git push`:

```
git push origin <aggiungi-il-tuo-nome>
```

sostituendo `<aggiungi-il-tuo-nome>` con il nome del branch creato prima.

## Invia i tuoi cambiamenti per una revisione (review)

Se vai nel tuo repository su GitHub, vedrai il pulsante `Compare & pull request`.  Cliccalo.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Ora invia la Pull Request (abbreviato PR).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Presto incorporerò (*merge*) tutti i tuoi cambiamenti nel master branch di questo progetto. Ti arriverà una mail di notifica una volta che le modiche saranno state accettate.

## E ora cosa sono in grado di fare?

Congratulazione! Hai appena completato il flusso stardard _forka -> clona -> modifica -> pull request_ che incontrerai spesso come contributore!

Celebra la tua prima contribuzione e condividilo con i tuoi amici e _follower_ accedendo alla [web app](https://firstcontributions.github.io/#social-share).

Potrai unirti al nostro team slack in caso hai bisogno di aiuto o hai delle domande. [Unisciti al team](https://join.slack.com/t/firstcontributors/shared_invite/zt-iywfifau-_aMtdwTjBoMzQqzW8~YUUA).

Ora inizia a contribuire ad altri progetti. Abbiamo compilato un elenco di progetti con problemi tecnici semplici su cui puoi iniziare. Controlla [la lista dei progetti nella web app](https://firstcontributions.github.io/#project-list).

### [Informazioni aggiuntive](../additional-material\translations\additional-material.it.md)

## Tutorial usando altri tool

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="./../assets/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
