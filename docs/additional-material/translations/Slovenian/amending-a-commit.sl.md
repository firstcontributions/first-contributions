# Popravljanje Commita

Kaj narediti, če pošlješ commit v oddaljeni repository in potem ugotoviš da si se zatipkal ali pa pozabil dodati vrstico kode v svoj zadnji commit.
Kako to popraviti? O tem govori ta vodič.

## Spreminjanje komentarja commit-a, ki je bil pred kratkim poslan na GitHub
To lahko naredimo brez da bi odprli datoteko:
*   V terminal vpiši ```git commit --amend -m "followed by your new commit message"```
*   Zaženi ```git push origin <branch-name>``` da pošlješ commit s spremembo v repository.

Opomba: Če vtipkaš samo ```git commit --amend```, se odpre tvoj urejevalnik besedil in te pozove da spremeniš komentar commit-a.
Zastavica ``-m`` to prepreči.

## Sprememba enega commit-a

No, kaj storiti, če pozabimo narediti eno malo spremembo v datoteki, kot na primer spremeniti eno besedo, vendar smo že poslali commit v oddaljeni repository?

Prikaz praktičnega primera (zgodovina commit-ov tega repository-a):
```
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
```
Recimo da smo pozabili dodati eno samo besedo datoteki botfile.

Obstajata dva načina kako se stvari lotiti. Prvi primer je da naredimo nov commit, ki vsebuje spremembo:
```
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
b0ca8f added single word to botfile
```
Drugi način je, da spremenimo commit a5da0d, mu dodamo pozabljeno besedo in ga pošljemo v GitHub, vse skupaj kot en commit.
Drugi način nam je bolj všeč, ker imamo opravka z manjšo spremembo.

Da to dosežemo, storimo naslednje:
*   Spremenimo datoteko. V tem primeru bomo spremenili datoteko botfile in ji dodali spuščeno besedo.
*   Nato bomo dodali datoteko v čakalnico z ```git add <filename>```.

Običajno ko dodamo datoteke v čakalnico, je naslednji korak, da naredimo commit s komentarjem ( git commit -m "our commit message" ).
V tem primeru pa želimo popraviti že narejen commit, zato namesto tega izvedemo:

* ```git commit --amend```
 Ukaz nam v tem primeru prikaže urejevalnik besedila in nam omogoči da spremenimo komentar. Sami se odločimo, ali spremenimo komentar, ali pustimo prejšnjega.
* Zapustimo urejevalnik besedil.
* Pošljemo spremembe z `` `git push origin <branch-name>` ``.

Na ta način bosta obe spremembi združeni v enem commit-u.
