[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Pirmieji įnašai

Sunku. Visada sunku ką nors padaryti pirmą kartą. Ypač bendradarbiaujant, klaidų darymas nėra malonus dalykas. Tačiau atviras kodas - tai bendravimas ir bendradarbiavimas. Mes norime paprasčiau paaiškinti naujiesiems atvirojo kodo kūrėjams, kaip jie gali prisidėti pirmą kartą.

Galite pradėti skaityti straipsnius ir žiūrėti vadovus, bet kas gali būti geriau nei mokymasis darant be klaidų pirmą kartą? Šio projekto tikslas - suteikti patarimus ir supaprastinti tai, kaip naujokai daro pirmąjį indėlį. Prisiminkite: kuo labiau esate atsipalaidavęs, tuo geriau mokotės. Jei norite atlikti pirmąjį indėlį, atlikite toliau pateiktus paprastus veiksmus. Mes pažadame, tai bus smagu.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Jei neturite instaliuoto git, [ instaliuokite čia ]( https://help.github.com/articles/set-up-git/).

## Kopijuokite (fork) šią saugyklą

Kopijuokite saugyklą paspausdami šaknies simbolio mygtuką šio puslapio viršuje.
Tai sukurs šios saugyklos kopiją jūsų GitHub paskyroje.

## Klonuokite saugyklą

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Dabar klonuokite šią saugyklą į savo kompiuterį. Spustelėkite klonavimo mygtuką ir tada spustelėkite *copy to clipboard* piktogramą.

Atidarykite terminalą ir paleiskite šią git komandą:

```
git clone "kopijuota nuoroda"
```
kur "kopijuota nuoroda" (be citatos ženklų) yra url nuoroda jūsų saugyklai. Peržiūrėkite ankstesnius veiksmus, kad gautumėte url nuorodą.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Pavyzdžiui:
```
git clone https://github.com/tai-jus/first-contributions.git
```
kur `tai-jus` yra jūsų GitHub paskyros vartotojo vardas. Čia jūs kopijuojate first-contributions saugyklos turinį į "GitHub" aplanką savo kompiuteryje.

## Sukurkite šaką (branch)

Pakeiskite kompiuterio saugyklos katalogą (jei dar to nepadarėte anksčiau):

```
cd first-contributions
```
Dabar sukurkite šaką naudodami komandą `git checkout`:
```
git checkout -b <add-tavo-vardas>
```

Pavyzdžiui:
```
git checkout -b add-vardenis-pavardenis
```
(Saugyklos pavadinime neturi būti žodžio *add*, bet tai yra reikalinga, kadangi šios šakos (branch) paskirtis yra įtraukti savo vardą į sąrašą.)

## Atlikite reikiamus pakeitimus ir pridėkite (commit) šiuos pakeitimus

Dabar atidarykite failą `Contributors.md` teksto redaktoriuje, pridėkite prie jo savo vardą ir išsaugokite failą. Jei eisite į projekto katalogą ir paleisite komandą `git status`, pamatysite, kad yra pakeitimų. Pridėkite šiuos pakeitimus į ką tik sukurtą šaką (branch) komandos `git add` pagalba:
```
git add Contributors.md
```

Dabar atlikite šiuos pakeitimus naudodami komandą `git commit`:
```
git commit -m "Add <tavo-vardas> to Contributors list"
```
pakeisdami `<tavo-vardas>` savo vardu.

## Išsiųskite pakeitimus į GitHub

Išsiųskite pakeitimus komanda `git push`:
```
git push origin <add-tavo-vardas>
```
pakeisdami `<tavo-vardas>` anskčiau sukurtos šakos (branch) vardu.

## Pateikite pakeitimus peržiūrai

Eikite į savo saugyklą GitHub. Pamatysite mygtuką `Compare & pull request` (palyginti ir įtraukti užklausą). Spustelėkite šį mygtuką.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Dabar pateikite įtraukimo į pradinę saugyklą (pull) užklausą.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Netrukus projekto autorius sujungs visus jūsų šakos pakeitimus su šio projekto pagrindine šaka. Kai pakeitimai bus sujungti, gausite tai patvirtinantį el. laišką.

## Kas toliau?

Džiaukitės ir atkreipkite dėmesį į savo įnašą pasidalindami šia žinia su draugais [interneto aplikacijoje](https://roshanjossey.github.io/first-contributions/#social-share).

Prisijunkite prie mūsų "slack" komandos, jei jums reikia pagalbos ar turite klausimų. [Prisijungti prie slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Pradėkite tobulinti kitus projektus. Mes sukūrėme projektų sąrašą, kuriuose yra lengvai išsprendžiamų problemų. Peržiūrėkite [projektų sąrašą interneto aplikacijoje](https://roshanjossey.github.io/first-contributions/#project-list).

### [ Papildoma medžiaga ](../additional-material/git_workflow_scenarios/additional-material.md)


## Pamokos naudojant kitus įrankius

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

