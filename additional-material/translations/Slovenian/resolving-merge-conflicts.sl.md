# Kaj je spor pri združevanju?

Ko poskusiš združiti drugo vejo v vejo v kateri trenutno delaš, vzameš spremembe iz drugega konteksta in jih združiš z datotekami s katerimi trenutno delaš.
Če dve osebi spremenita vrstico v isti datoteki, ali če se ena oseba odloči zbrisati datoteko medtem, ko se jo druga odloči spremeniti, Git ne ve več kaj je pravilno. Git bo označil datoteko kot spor. Spor, ki ga moraš razrešiti preden lahko nadaljuješ z delom.

# Kako razrešiti spor pri združevanje?

Ko Git zazna spor pri združevanju, bo mesto problema v datoteku označil tako, da ga bo obdal z:
“<<<<<<<< HEAD” and “>>>>>>>>>>[other branch name]”

Vsebina za prvo oznako bo izhajala iz tvoje trenutne veje. Nato sledi vrstica z "=======", tej pa sledi vsebina iz veje, ki je v nazkrižju s tvojo. Za tem pridejo znaki ">>>>>" in ime te druge veje.
Naša naloga je da uredimo te vrstice. Ko smo končali, naj bi datoteka izgledala točno tako, kot hočemo da izgleda. Lahko da se bo potrebno posvetovati s sodelavcem, ki je napisal vsebino, ki je v navzkrižju z našo, da se bomo lahko odločili katera koda je prava. Mogoče bo tvoja, mogoče bo njegova - ali pa mešanica obeh.

Primer:
```
 <<<<<<< HEAD:mergetest
 This is my third line
 =======
 This is a fourth line I am adding
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Nakazuje začetek vrstic, kjer je spor. Te vrstice so iz tvoje datoteke, ki si jo poskusil združiti.
`=======`: Nakazuje prelomno točko za primerjavo. Razdeli spremembe iz tvojega commit-a (zgoraj) in spremembe nekoga drugega (spodaj) za lažjo predstavo.
`>>>>>>>`: Nakazuje konec vrstic, kjer je spor.

Spor razrešiš z urejanjem datoteke in ročnim združevanjem delov datoteke, kjer je Git naletel na problem. To lahko pomeni da je potrebno zavreči tvoje spremembe, spremembe nekoga drugega ali pa ustvariti mešanico obeh. Prav tako je potrebno zbrisati '<<<<<<<', '=======', in '>>>>>>>'.

Ko je bil spor razrešen, uporabi ukaz `git add`. Ne pozabi izvesti teste, s katerimi se prepričaš da je bil spor pravilno razrešen.

Lahko si tudi namestiš različne plugine, ki so odvisni od tvojega IDE-ja, za lažje reševanje sporov.

# Kako razveljaviti združitev ( merge )?
Če želiš razveljaviti združitev uporabi ukaz `git merge —abort`.
