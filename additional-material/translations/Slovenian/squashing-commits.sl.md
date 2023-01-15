# Kaj je stiskanje?

V Git-u stiskanje ( squashing ) pomeni popravljanje zgodovine svojih commit-ov, tako da na koncu ostaneš samo z enim commit-om in enim komentarjem narejenih sprememb.
To je običajni postopek v odprto kodnih projektih, ker je velik del zgodovine vsake veje pomemben samo programerju, ki jo je ustvaril. Poleg tega na ta način poenostavimo sledenje izvedenih sprememb in jih tudi lažje povrnemo v prejšnje stanje, če je to potrebno. 

# Kako stisneš commit-e?

Najprej uporabimo ukaz `git log` da lahko pregledamp commit-e v svoji veji, ki bi jih rad združili ( merge ).

```
git log
```

Videti bi morali serijo commit-ov, kot na primer:

```
commit blablabla
Author: omguhh
Date:   10/10/20
    Commit message 1

commit blablabla2
Author: omguhh
Date:   10/10/20
    Commit message 2
```

Sedaj, ko vidimo commit-e, ki jih želimo združiti v enega, lahko začnemo tako da uporabimo ukaz ```git rebase```. Predvidevam da že poznaš ukaz ```git rebase``` in lahko začnemo stiskanje commit-ov v interaktivnem načinu ukaza `git rebase`, ki ga aktiviramo tako:

```
git rebase -i
```
V interaktivnem načinu ukaza rebase lahko določimo začetno in končno točko do katere nazaj želimo iti. HEAD je začetna točka, "~2" pa pomeni da gremo dva commita nazaj v zgodovino. Ukaz se uporabi takole:

```
git rebase -i HEAD~2
```

Ko uporabimo ta ukaz, se nam bo prikazalo nekaj podobnega tem vrsticam:

```
pick blablabla Changing test01.txt file
pick blablabla2 Adding dummy01.txt file

#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

Ukazi navedeni v zgornjem sporočilu:
- p, pick = uporabi commit
- r, reword = uporabi commit, vendar uredi komentar
- e, edit = uporabi commit, vendar se ustavi za spremembo
- s, squash = uporabi commit, vendar ga stisni v prejšnji commit
- f, fixup = enak kot "squash", vendar zavrzi komentar tega commit-a
- x, exec = zaženi ukaz ( preostanek vrstice ) v shell-u

To pomeni da, če želimo stisniti ```blablabla2``` v ```blablablabla```, bi zgornje sporočilo spremenili tako:

```
pick blablabla Changing test01.txt file
squash blablabla2 Adding dummy01.txt file

```

Če gre vse po planu, dobimo rezultat, ki zgleda takole:

```
# This is a combination of 2 commits.
# The first commit's message is:
commit message 1

# This is the 2nd commit message:

commit message 2
```

To sporočilo lahko po želji spremenimo preden zapremo urejevalnik besedila, kar shrani spremembe.

Če še enkrat uporabimo ukaz `git log`, bi morali dobiti komentar commit-a, ki smo ga vnesli preden smo zaprli urejevalnik besedila, in commit-i bi morali biti združeni v enega.

