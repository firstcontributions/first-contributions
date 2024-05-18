# Povrnitev commit-a

Povrnitev commit-a pomeni, da ustvarimo nov commit, ki odstrani vse spremembe, ki smo jih napravili v prejšnjem commit-u. Kot da bi naredili ```CTRL + Z ``` v Git-u.

Povrnitev v Git-u je sorazmerno enostavna, ker je vsak commit, ki ga pošljemo v oddaljen repository, povezan s svojim unikatnim alfanumeričnim SHA (Secure Hash Algorithm) ključem.
To pomeni da lahko povrnemu vsak commit, če le imamo njegov SHA.
V vsakem primeru pa moramo biti previdni pri povračanju, ker si lahko poškodujemo repository.

Da lahko izberemo SHA točno določenega commit-a, ki ga hočemo odstraniti, nam zelo prav pride seznam vseh commit-ov, ki smo jih napravili.
Ta seznam dobimo s tem ukazom:
```git log --oneline ```
Ukaz ```git log``` bi nam prav tako vrnil SHA, vendar v daljši obliki izpisa. 
Uporaba zastavice ```--oneline ``` Git-u pove da hočemo pregleden izpis v eni vrstici.

Prvih 7 znakov v vsaki vrstici izpisa se imenuje skrajšani hash commit-a.

Za primer, to je izpis ```git log --oneline ``` za ta repository:
```
389004d added spacing in title
c1b9fc1 Merge branch 'master' into tutorials
77eaafd added tutorial for reverting a commit
```

To nam torej pokaže, da lahko z ```git log --oneline```, pridobimo seznam vseh commit-ov narejenih v repository-ju s prvimi 7 znaki njihovih SHA.

No, sedaj lahko poskusimo zbrisati commit "added spacing in title" z naslednjimi koraki:

*   Kopiraj SHA commit-a, v tem primeru ```389004d```
*   Potem uporabi ukaz ```git revert 389004d```

Sedaj se zažene naš urejevalnik besedila in nas pozove naj uredimo komentar commit-a.
Lahko se odločiš, da pustiš privzeto sporočilo Git-a, ki se začne z besedo `Revert`, ali pa spremeniš komentar po svojih željah.

*   Nato shranimo in zapremo urejevalnik besedila.
*   Vrnemo se v ukazno vrstico.
*   Uporabimo ukaz ```git push origin <branch-name>``` da pošljemo spremembe na GitHub.

In to je to, spremembe bodo odstranjene. V tem primeru bi se moj repository povrnil na stanje v commit-u ```c1b9fc1```.