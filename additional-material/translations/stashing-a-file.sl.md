# Shranjevanje za pozneje ( Stashing )

Kaj storiti, če delaš na velikem projektu, in moraš nenadoma zamenjati vejo, na kateri trenutno delaš, za neko drugo vejo? Koda, na kateri si delal, ni dokončana in dokler je ne preveriš dobro, ne želiš izvesti commit. Vendar se ne moreš premakniti na drugo vejo brez da bi izvedel commit, Git ti ne pusti prekiniti delovni tok ( workflow ). Kaj storiti? Kako preprečiti nepotreben commit in hkrati preskočiti na drugo vejo? Na to vprašanje odgovarja ta vodič.

## Shranjevanje svojega dela

Predpostavimo da delaš na veji projekta, kjer si naredil nekaj spremembe. Če uporabiš ukaz ```git status```, lahko vidiš kje so bile spremembe narejene.

```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```
Sedaj se želiš prestaviti na drugo vejo, vendar še nočeš izvesti commit s temi spremembami. Zato bi shranil spremembe za pozneje ( stash ).
Spremembe lahko shraniš na svoj stack z uporabo ukaza ```git stash```:

```
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")
```

Sedaj je tvoje delovno okolje ( working directory ) čisto. To lahko preveriš z uporabo ukaza ```git status```:

```
$ git status
# On branch master
nothing to commit, working directory clean
```

Sedaj se lahko prestaviš na katerokoli vejo in delaš naprej; tvoje shranjene spremembe so shranjene na stack-u. Spremembe, ki so shranjene na stack-u, si lahko ogledaš z uporabo ukaza ```git stash list```:

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

V primeru da želiš uveljaviti (re-apply) spremembe, ki si jih ravnokar shranil, lahko uporabiš ukaz ```git stash apply```. S tem ukazom lahko uveljaviš zadnjo shranjeno spremembo. Če želiš uveljaviti katerokoli drugo spremembo, jo moraš točno določiti: ```git stash apply <stash-name>```, kjer je ```<stash-name>``` ime spremembe, ki jo želiš uveljaviti.

```
$ git stash apply
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   index.html
#      modified:   lib/simplegit.rb
#
```

Git je sedaj spremenil datoteko, ki smo jo povrnili v prvotno stanje, ko smo spremembe shranili v stack. V tem primeru smo imeli čisto delovno okolje, ko smo poskusili uveljaviti stash, in uveljavili smo jih na isti veji, s katere smo jih shranili. Nič od tega, čisto delovno okolje in ista veja, ni nujno da uveljavimo spremembe iz stasha. Spremembe lahko shranimo na eni veji, se prestavimo na drugo vejo in tam uveljavimo iste spremembe. Lahko bi tudi spremenili ali odstranili datoteke v svojem delovnem okolju, ko bi uveljavili stash. V primeru da pride do sporov pri združevanju shranjenih sprememb v obstoječe datoteke, bo Git te spore javil.

Spremembe so bile uveljavljene, vendar datoteka, ki je bila pripravljena za commit, sedaj ni več pripravljena. Da dosežemo še to, moramo uporabiti ukaz ```git stash apply``` z ```--index```, da sporočimo ukazu da mora uveljaviti tudi to stanje. Ko uporabimo ta ukaz, se vrnemo v točno tako stanje, kot je bilo na začetku:

```
$ git stash apply --index
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Ukaz `apply` samo uveljavi spremembe, ki so bile shranjene, vendar te še vedno ostanejo na stack-u. Z ukazom ```git stash list``` si lahko prikažeš vsebino stack-a. Da nekaj z njega zbrišemo, uporabimo ukaz ```git stash drop```, ki mu dodamo ime stash-a.

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
```

Z ukazom ```git stash pop``` lahko hkrati uveljavimo spremembe in jih odstranimo s stack-a.

## Razveljavljanje Stash-a

V nekaterih primerih hočeš uveljaviti shranjene spremembe, nekaj narediti, in razveljaviti spremembe, ki so prišle iz stash-a. Git nima ukaza ```git unapply```, vendar je možno doseči isti učinek z kombiniranjem ukazov. Najprej prikažemo željeni stash in ga nato vzratno uveljavimo:

```$ git stash show -p stash@{0} | git apply -R```

Če ne določimo, kateri stash želimo, Git predvideva da želimo zadnjega:

```$ git stash show -p | git apply -R```

Lahko ustvariš alias in v bistvu dodaš ukaz ```stash-unapply``` v svoj Git. Na primer:

```
$ git config --global alias.stash-unapply '!git stash show -p | git apply -R'
$ git stash apply
$ #... work work work
$ git stash-unapply
```

## Ustvari vejo iz Stash-a

Če si shranil spremembe in jih nekaj časa pustil pri miru, vmes pa delal naprej na veji s katere si jih shranil, se ti lahko naredi da boš imel težave z uveljaljanjem sprememb. Če uveljavljaš spremembe na datoteki, ki si jo vmes spremenil, boš dobil spor pri združevanju in ga boš moral razrešiti. Obstaja lažji način povračanja sprememb iz stash-a z uporabo ukaza ```git stash branch```, ki ustvari novo vejo, pridobi commit na katerem si bil, ko si shranil spremembe, na njem uveljavi spremembe in potem zbriše stash, če je bil uspešno uveljavljen:

```
$ git stash branch testchanges
Switched to a new branch "testchanges"
# On branch testchanges
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
```

To je prikladna bližnjica s katero lahko enostavo pridobimo shranjene spremembe in jih uporabimo v novi veji.