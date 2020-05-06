# Razveljavljanje lokalnega commit-a

Vse kar rabiš storiti, da razveljaviš lokalni commit, je:
```
git reset
```
Ta ukaz bo resetiral stanje v čakalnici na tvoj zadnji commit, vendar bodo spremembe ostale v delovnem okolju. Če želiš, lahko ponovno ustvariš commit s temi spremembami.
Lahko pa tudi odstraniš samo eno datoteko s svojega prejšnjega commit-a. Uporabiš ukaz:
```
git reset <file>
```
Ukaz bo odstranil samo določeno datoteko s čakalnice, vendar bodo spremembe narejene na datoteki ostale.

Primer uporabe ```git reset```:
```
# Make changes in index.php and tutorial.php
# Add files into the staging area
$ git add .
# Remembered both files need to be committed separately
# Unstage tutorial.php
$ git reset tutorial.php
# Commit index.php first
$ git commit -m "Changed index.php"
# Commit tutorial.php now
$ git add tutorial.php
$ git commit -m "Changed tutorial.php"
```

Predpostavimo da si pokvaril svoj lokalni repository in ga želiš resetirati na svoj zadnji commit.
Lahko uporabiš spodnji ukaz:
```
git reset --hard
```
Ukaz bo izpraznil čakalnico in tudi povrnil vse spremembe v datotekah na stanje v zadnjem commit-u.
Možnost ```--hard``` pove Git-u da mora odstraniti tudi vse spremembe v delovnem okolju.
Ta ukaz uporabi samo takrat, ko si prepričan da želiš odstraniti vse spremembe nastale od zadnjega commit-a!

Primer uporabe ukaza ```git reset --hard```:
```
# Decided to start a crazy experiment
# Create a new file 'crazy.php' and add some code to it
# Commit crazy.php
$ git add crazy.php
$ git commit -m "Started a crazy dev"
# Edit crazy.php file again and changed a lot other files
# Commit all tracked files
$ git add .
$ git commit -m "Continued dev"
# Tested and things went out of hand
# Decided to remove the whole thing
$ git reset --hard HEAD~2
```
Ukaz ```git reset --hard HEAD~2``` premakne trenutno vejo nazaj za 2 commit-a in hkrati povrne vse spremembe na to točko. Odstrani tudi 2 posnetka, ki smo ju ravnokar ustvarili iz zgodovine projekta.

P.s: Nikoli ne izvedi ```git reset --hard``` , če si že poslal svoje commit-e v skupni repository, ker boš s tem ustvaril probleme vsem, ki uporabljajo ta repository!
