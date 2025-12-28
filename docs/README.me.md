Prvi doprinosi

Ovaj projekat ima za cilj da pojednostavi i vodi početnike kroz njihov prvi doprinos open-source projektima. Ako želiš da napraviš svoj prvi doprinos, prati korake ispod.

Ako ti komandna linija nije prijatna za korišćenje, ovdje su tutorijali koji koriste GUI alate
.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork repozitorijuma" />
Ako nemaš git instaliran na svom računaru, instaliraj ga ovdje
.
Forkuj ovaj repozitorijum

Forkuj ovaj repozitorijum klikom na dugme Fork na vrhu stranice.
Time će se napraviti kopija ovog repozitorijuma na tvom GitHub nalogu.

Kloniraj repozitorijum
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="kloniraj repozitorijum" />

Sada kloniraj forkovani repozitorijum na svoj računar.
Idi na svoj GitHub nalog, otvori forkovani repozitorijum, klikni na dugme Code, zatim na karticu SSH i klikni na ikonu copy url to clipboard.

Otvori terminal i pokreni sljedeću git komandu:

git clone "url koji si upravo kopirao"


gdje je url koji si upravo kopirao URL ovog repozitorijuma (tvog forka).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="kopiraj URL u clipboard" />

Primjer:

git clone git@github.com:ovo-si-ti/first-contributions.git


gdje je ovo-si-ti tvoje GitHub korisničko ime.
Na ovaj način kopiraš sadržaj repozitorijuma first-contributions sa GitHuba na svoj računar.

Kreiraj granu (branch)

Promijeni direktorijum na repozitorijum na svom računaru:

cd first-contributions


Zatim kreiraj novu granu koristeći git switch komandu:

git switch -c ime-nove-grane


Primjer:

git switch -c add-alonzo-church


Ako dobiješ grešku da git switch ne postoji, koristi:

git checkout -b ime-nove-grane

Napravi izmjene i sačuvaj ih

Otvori fajl Contributors.md u tekst editoru i dodaj svoje ime u listu.
Nemoj ga dodavati na početak ili kraj — postavi ga bilo gdje između.

Provjeri status:

git status


Dodaj izmjene:

git add Contributors.md


Sačuvaj izmjene (commit):

git commit -m "Dodato moje ime u Contributors listu"

Pošalji izmjene na GitHub

Pošalji izmjene koristeći:

git push -u origin ime-tvoje-grane


gdje je ime-tvoje-grane naziv grane koju si ranije kreirao.

Greška pri autentifikaciji

GitHub više ne podržava prijavu lozinkom.
Potrebno je koristiti SSH ključ ili Personal Access Token.

Ako vidiš HTTPS URL u git remote -v, promijeni ga:

git remote set-url origin git@github.com:tvoje-korisnicko-ime/tvoj-repo.git


Detaljan vodič:
https://docs.github.com/en/authentication/connecting-to-github-with-ssh

Pošalji izmjene na pregled (Pull Request)

Na svom GitHub repozitorijumu klikni na dugme Compare & pull request.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and pull request" />

Zatim klikni na Submit pull request.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Nakon pregleda, izmjene će biti spojene u glavnu granu.
Dobićeš email obavještenje kada se to desi.

Šta dalje?

Čestitamo! 🎉
Upravo si završio standardni proces:

fork → clone → edit → pull request

Proslavi svoj doprinos i podijeli ga preko
https://firstcontributions.github.io/#social-share

Ako želiš još vježbe, pogledaj:
https://github.com/roshanjossey/code-contributions

Lista lakih projekata za početnike dostupna je ovdje:
https://firstcontributions.github.io/#project-list

Dodatni materijal

docs/additional-material/git_workflow_scenarios/additional-material.md