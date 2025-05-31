[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Pirmieji įnašai

Sunku. Visada sunku ką nors padaryti pirmą kartą. Ypač bendradarbiaujant, klaidų darymas nėra malonus dalykas. Tačiau atviras kodas - tai bendravimas ir bendradarbiavimas. Mes norime paprasčiau paaiškinti naujiesiems atvirojo kodo kūrėjams, kaip jie gali prisidėti pirmą kartą.

Galite pradėti skaityti straipsnius ir žiūrėti vadovus, bet kas gali būti geriau nei mokymasis darant be klaidų pirmą kartą? Šio projekto tikslas - suteikti patarimus ir supaprastinti tai, kaip naujokai atlieka savo pirmąjį indėlį. Prisiminkite: kuo labiau atsipalaidavę esate, tuo geriau mokotės. Jei norite atlikti pirmąjį indėlį, atlikite toliau pateiktus paprastus veiksmus. Mes pažadame, tai bus smagu.

_Jei nesate pratę dirbti su komandine eilute, [čia rasite vadovą, naudojantį GUI įrankius.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Jei neturite instaliuoto git, [instaliuokite čia](https://help.github.com/articles/set-up-git/).

## Kopijuokite (fork) šią saugyklą

Kopijuokite saugyklą paspausdami šaknies simbolio mygtuką šio puslapio viršuje.
Tai sukurs šios saugyklos kopiją jūsų GitHub paskyroje.

## Klonuokite saugyklą

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Dabar klonuokite šią saugyklą į savo kompiuterį. Spustelėkite klonavimo mygtuką ir tada spustelėkite *copy to clipboard* piktogramą.

Atidarykite terminalą ir paleiskite šią git komandą:

```
git clone "kątik nukopijuota nuoroda"
```
kur "kątik nukopijuota nuoroda" (be citatos ženklų) yra url nuoroda jūsų saugyklai (jūsų projekto kopijai). Peržiūrėkite ankstesnius veiksmus, kad gautumėte url nuorodą.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

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
Dabar sukurkite šaką naudodami komandą `git branch`:
```
git branch -c <tavo-sakos-vardas>
```

Pavyzdžiui:
```
git branch -c add-vardenis-pavardenis
```
(Saugyklos pavadinime neprivalo būti žodžio *add*, bet mes jį naudojame, kadangi šios šakos (branch) paskirtis yra įtraukti savo vardą į sąrašą.)

<details>
<summary> <strong>Jei gavote klaidos pranešimą naudodami git switch, spauskite čia:</strong> </summary>

Jei klaidos pranešimas yra "Git: `switch` is not a git command. See `git –help`", tikėtinai naudojate seną git versiją.

Tokiu atveju bandykite `git checkout`:

```bash
git checkout -b add-vardenis-pavardenis
```

</details>

## Atlikite reikiamus pakeitimus ir pridėkite (commit) šiuos pakeitimus

Dabar atidarykite failą `Contributors.md` teksto redaktoriuje ir pridėkite prie jo savo vardą. Nedėkite jo į failo pradžią ar pabaigą - įrašykite jį bet kur kitur faile. Galiausiai, išsaugokite failą. 

Jei eisite į projekto katalogą ir paleisite komandą `git status`, pamatysite, kad yra pakeitimų. Pridėkite šiuos pakeitimus į ką tik sukurtą šaką (branch) komandos `git add` pagalba:
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
git push origin <tavo-sakos-vardas>
```
pakeisdami `<tavo-sakos-vardas>` anskčiau sukurtos šakos (branch) vardu.

<details>
<summary> <strong>Jei gaunate klaidos pranešimą išsaugodami pakeitimus, spauskite čia:</strong> </summary>

- ### Autentifikacijos klaida
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  [GitHub vadovas](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) padės jums sugeneruoti ir sukonfiguruoti SSH raktą savo paskyroje.

  Taip pat, galbūt norėsite pabandyti 'git remote -v', skirtą patikrintite savo nuotolinį adresą (remote address).
  
  Jei jis atrodo taip ar panašiai:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>
  
  pakeiskite jį, naudodami komandą:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  Kitu atveju jūsų vis tiek sulauksite klausimo apie savo vartotojo vardą ir slaptažodį ir sulauksite autentifikacijos klaidos.
</details>

## Pateikite pakeitimus peržiūrai

Eikite į savo saugyklą GitHub. Pamatysite mygtuką `Compare & pull request` (palyginti ir įtraukti užklausą). Spustelėkite šį mygtuką.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Dabar pateikite įtraukimo į pradinę saugyklą (pull) užklausą.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Netrukus projekto autorius sujungs visus jūsų šakos pakeitimus su šio projekto pagrindine šaka. Kai pakeitimai bus sujungti, gausite tai patvirtinantį el. laišką.

## Kas toliau?

Džiaukitės ir atkreipkite dėmesį į savo įnašą pasidalindami šia žinia su draugais [interneto aplikacijoje](https://firstcontributions.github.io/#social-share).

Pradėkite tobulinti kitus projektus. Mes sukūrėme projektų sąrašą, kuriuose yra lengvai išsprendžiamų problemų. Peržiūrėkite [projektų sąrašą interneto aplikacijoje](https://firstcontributions.github.io/#project-list).

### [ Papildoma medžiaga ](../additional-material/git_workflow_scenarios/additional-material.md)


## Pamokos naudojant kitus įrankius

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
