Prvi doprinos otvorenom kodu

Ovo može biti teško. Kada prvi put nešto radite, posebno u saradnji s drugima, nije uvijek prijatno praviti greške. Ali open source je upravo o saradnji i zajedničkom učenju.
Želimo da početnicima olakšamo učenje i pravljenje prvog doprinosa otvorenom kodu.

Čitanje članaka i gledanje tutorijala može pomoći, ali ništa ne može zamijeniti praktičan rad u stvarnom okruženju.
Cilj ovog projekta je da vodi početnike i pojednostavi proces njihovog prvog doprinosa. Ako želite da napravite svoj prvi doprinos, slijedite korake ispod.

Ako vam komandna linija nije prijatna, ovdje su tutorijali koji koriste GUI alate
.
Forkujte ovaj repozitorijum

Forkujte ovaj repozitorijum klikom na dugme Fork na vrhu stranice.
Ovim ćete napraviti kopiju repozitorijuma na svom GitHub nalogu.

Klonirajte repozitorijum

Sada klonirajte forkovani repozitorijum na svoj računar.
Otvorite vaš GitHub nalog, uđite u forkovani repozitorijum, kliknite na dugme Code, zatim na SSH, i kopirajte URL.

U terminalu pokrenite sljedeću komandu:

git clone "url koji ste upravo kopirali"


Primjer:

git clone git@github.com:your-username/first-contributions.git


Ovim kopirate sadržaj repozitorijuma sa GitHuba na vaš računar.

Kreirajte novu granu (branch)

Pređite u direktorijum repozitorijuma:

cd first-contributions


Zatim kreirajte novu granu:

git switch -c add-your-name


Primjer:

git switch -c add-alonzo-church


Ako git switch ne radi, koristite:

git checkout -b add-your-name

Napravite izmjene i sačuvajte ih

Otvorite fajl Contributors.md u editoru teksta i dodajte svoje ime.
Ne dodajte ga na početak ili kraj fajla — stavite ga negdje u sredinu. Sačuvajte fajl.

Provjerite status:

git status


Dodajte izmjene:

git add Contributors.md


Sačuvajte izmjene (commit):

git commit -m "Add your-name to Contributors list"


Zamijenite your-name svojim imenom.

Pošaljite izmjene na GitHub
git push -u origin your-branch-name


Ako dobijete grešku vezanu za autentifikaciju, koristite SSH ključ ili personal access token.

Pošaljite Pull Request

Na GitHub stranici vašeg repozitorijuma kliknite na Compare & pull request, a zatim pošaljite zahtjev.

Nakon pregleda, vaše izmjene će biti spojene u glavni repozitorijum.
Dobićete email obavještenje kada se to desi.

Šta dalje?

Čestitamo! 🎉
Upravo ste završili standardni fork → clone → edit → pull request proces.

Podijelite svoj uspjeh sa prijateljima putem web aplikacije
.

Ako želite više vježbe, pogledajte:
👉 https://github.com/roshanjossey/code-contributions

Sada ste spremni da doprinosite i drugim open-source projektima 🚀
