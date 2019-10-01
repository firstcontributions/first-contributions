[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

Teško je. Uvek je teško kada prvi put nešto učinite. Posebno kada sarađujete, praviti greške nije prijatna stvar. Želeli smo da pojednostavimo način na koji novi saradnici otvorenog koda po prvi put uče i doprinose.

Čitanje članaka i gledanje tutorijala mogu vam pomoći, ali šta je bolje nego zapravo raditi stvari u praktičnom okruženju? Ovaj projekat ima za cilj da pruži smernice i pojednostavi način na koji početnici daju svoj prvi doprinos. Ako želite da date svoj prvi doprinos, sledite dole navedene korake.

#### *Ukoliko niste vešti sa komandnom linijom, [evo par alternativa koje koriste grafički korisnički interfejs.]( #tutorials-using-other-tools )*

#### *Pročitajte ovo na [drugim jezicima](translations/Translations.md).*

[🇮🇳](translations/README.hi.md) [🇲🇲](translations/README.mm_unicode.md) [🇮🇩](translations/README.id.md) [🇫🇷](translations/README.fr.md) [🇪🇸](translations/README.es.md) [<img src="assets/catalan1.png" width="22">](translations/README.ca.md) [🇳🇱](translations/README.nl.md) [🇷🇺](translations/README.ru.md) [🇯🇵](translations/README.ja.md) [🇻🇳](translations/README.vn.md) [🇵🇱](translations/README.pl.md) [🇮🇷](translations/README.fa.md) [🇮🇷](translations/README.fa.en.md) [🇰🇷 🇰🇵](translations/README.ko.md) [🇩🇪](translations/README.de.md) [🇨🇳](translations/README.chs.md) [🇹🇼](translations/README.cht.md) [🇬🇷](translations/README.gr.md) [🇺🇦](translations/README.ua.md) [🇧🇷](translations/README.pt_br.md) [🇵🇹](translations/README.pt-pt.md) [🇮🇹](translations/README.it.md) [🇹🇭](translations/README.th.md) [🏴󠁥󠁳󠁧󠁡󠁿](translations/README.gl.md) [🇵🇰](translations/README.ur.md) [:bangladesh:](translations/README.bn.md) [🇲🇩 🇷🇴](translations/README.ro.md) [rs](translations/README.rs.md) [🇹🇷](translations/README.tr.md) [🇸🇪](translations/README.se.md) [:slovenia:](translations/README.sl.md) [🇮🇱](translations/README.hb.md) [<img src="assets/pirate.png" width="22">](translations/README.en-pirate.md)

<img align="right" width="300" src="assets/fork.png" alt="kopirajte ovo skladište" />

Ako nemate git na vašoj mašini, [instalirajte ga](https://help.github.com/articles/set-up-git/).

## Kopirajte ovo skladište

Kopirajte ovo skladište klikom na dugme `Fork` na vrhu ove stranice.
Ovo će stvoriti kopiju ovog skladišta na vašem nalogu.

## Klonirajte ovo skladište

<img align="right" width="300" src="assets/clone.png" alt="klonirajte ovo skladište" />

Sada klonirajte ovo skladište na vaš kompjuter. Idite na svoj GitHub nalog, otvorite klonirano skladište, kliknite na `Clone or Download` dugme, a zatim kliknite na ikonicu *copy to clipboard* sa desne strane URL-a.

Otvorite terminal i pokrenite sledeću git komandu:

```
git clone "URL koji ste upravo kopirali"
```
gde je „URL koji ste upravo kopirali“ (bez navodnika) URL u ovo skladište (vašu kopiju ovog projekta). Pogledajte prethodne korake za dobijanje URL-a.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:
```
git clone https://github.com/vaš-nadimak-za-github/first-contributions.git
```
gde je `vaš-nadimak-za-github` vaše GitHub korisničko ime. Ovde kopirate sadržaj skladišta sa GitHub-a na svoj računar.

## Napravite novu granu

Promenite u direktorijum na računaru (ako ga već niste):

```
cd first-contributions
```
Sada kreirajte granu pomoću `git checkout` komande:
```
git checkout -b <ime-vaše-grane>
```

Na primer:
```
git checkout -b add-alonzo-church
```
(Ime grane ne mora da sadrži reč *add* u sebi, ali je razumna stvar koju treba uključiti jer je svrha ove grane dodati vaše ime listi.)

## Izvršite potrebne promene i `commit-ujte` te promene

Sada otvorite datoteku `Contributors.md` u tekst editoru i dodajte joj svoje ime. Ne dodajte ga na početku ili na kraju datoteke. Stavite ga bilo gde između. Sada, sačuvajte datoteku.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />


Ako odete u direktorij projekta i izvršite naredbu `git status`, videćete da postoje promene.


Dodajte te promene u granu koju ste upravo stvorili pomoću komande `git add`:

```
git add Contributors.md
```

Sada izvršite te promene koristeći naredbu `git commit`:
```
git commit -m "Add <vaše-ime> to Contributors list"
```
zamenite `<vaše-ime>` svojim imenom.

## `Push` izmene na GitHub

`Push` izmene pomoću komande `git push`:
```
git push origin <ime-vaše-grane>
```
zamenjujući `<ime-vaše-grane>` imenom grane koju ste kreirali ranije.

## Pošaljite svoje promene na pregled

Ako odete u svoje skladište na GitHub-u, videćete dugme „Compare & pull request“. Kliknite na to dugme.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Sada podnesite `pull request`.

<img style="float: right;" src="assets/submit-pull.png" alt="submit pull request" />

Uskoro ću sve vaše promene spojiti u glavnu granu ovog projekta. Dobit ćete e-mail sa obaveštenjem kada se promene objedine.

## Izbrišite granu nakon spajanja sa glavnom granom

Možete sigurno da izbrišete vašu granu `<ime-vaše-grane>` nakon spajanja sa glavnom granom. Videćete dugme za brisanje grane:

<img style="float: right;" src="assets/delete-branch-after-pr.png" alt="delete branch after PR is merged" />

Ako je zahtev za povlačenje zatvoren bez spajanja, GitHub će vas upozoriti na brisanje nepotpunih obaveza i dugme će izgledati ovako:

<img style="float: right;" src="assets/delete-branch-warning.png" alt="delete branch after PR is not merged" />

## Sledeci koraci?

Čestitamo! Upravo ste završili standardan _fork -> clone -> edit -> PR_ tok rada sa kojim ćete se često susretati kao saradnik!

Proslavite svoj doprinos i podelite ga sa prijateljima i pratiocima tako što ćete ići na [web aplikaciju](https://roshanjossey.github.io/first-contributions/#social-share).

Možete se pridružiti našem slack timu u slučaju da vam treba pomoć ili imate pitanja. [Pridružite se slack timu](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Sada započnimo sa doprinosom drugim projektima. Sastavili smo listu projekata sa lakšim pitanjima sa kojima možete početi. Proveri [listu projekata u web aplikaciji](https://roshanjossey.github.io/first-contributions/#project-list).

### [Dodatni materijal](additional-material/git_workflow_scenarios/additional-material.md)


## Vodiči pomoću drugih alata

| <a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a> | <a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a> |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| [GitHub Desktop](github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](github-windows-vs2017-tutorial.md)                                                                                                                              | [GitKraken](gitkraken-tutorial.md)                                                              |

## Samopromocija

Ako vam se svideo ovaj projekat, dajte mu zvezdicu na [GitHub-u](https://github.com/Roshanjossey/first-contributions).
Ako se osećate posebno dobrotvorno, sledite [Roshan](https://roshanjossey.github.io/) na
[Twitter-u](https://twitter.com/sudo__bangbang) i
[GitHub-u](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>