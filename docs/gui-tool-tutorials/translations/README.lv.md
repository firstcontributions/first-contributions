[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Pirmais devums

Kaut ko paveikt pirmo reizi vienmēr ir grūti. Turklāt pieļaut kļūdas, jo īpaši līdzdarbojoties ar citiem, nav patīkami. Mēs vēlamies vienkāršot veidu, kā jauni atvērtā koda līdzautori mācās un pievieno savu devumu pirmo reizi.

Rakstu lasīšana un pamācību skatīšanās var palīdzēt, tomēr nekas nav labāks par īstu darbību mācību vidē. Šī projekta mērķis ir sniegt norādījumus un vienkāršot veidu, kā iesācēji pievieno savu pirmo devumu. Ja tu vēlies līdzdarboties, seko turpmāk norādītajiem soļiem.

#### *Ja tu nejūties ērti ar komandrindu, [izmanto GUI rīku pamācības.]( #pamācības-citiem-rīkiem )*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Ja tavā datorā nav git, [uzinstalē to]( https://help.github.com/articles/set-up-git/).

## Izveido repozitorija atzarojumu

Izveido savu repozitorija atzarojumu, nospiežot *fork* pogu šīs lapas augšpusē.
Tādējādi tavā profilā tiks izveidota šī repozitorija kopija.

## Klonē repozitoriju

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Tagad klonē nokopēto repozitoriju savā datorā. Ej uz savu GitHub profilu, atver nokopēto repozitoriju, nospied *clone* pogu un tad nospied uz *copy to clipboard* ikonas.

Atver termināli un palaid šo git komandu:

```
git clone "tikko nokopētā saite"
```
kur "tikko nokopētā saite" (bez pēdiņām) ir url uz šo repozitoriju (tavs projekta atzarojums). Apskaties iepriekšējos soļos, kā dabūt url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Piemēram:
```
git clone https://github.com/tavs-vārds/first-contributions.git
```
kur `tavs-vārds` ir tavs GitHub lietotājvārds. Šādi tu kopē GitHub repozitorija *first-contributions* saturu savā datorā.

## Izveido zaru

Savā datorā nomaini repozitorija direktoriju (ja tu vēl neatrodies tajā):

```
cd first-contributions
```
Tagad izveido zaru ar `git checkout` komandu:
```
git checkout -b <ieliec-jaunā-zara-nosaukumu>
```

Piemēram:
```
git checkout -b add-alonzo-church
```
(Zara nosaukumā nav obligāti jābūt vārdam *add*, bet būtu lietderīgi to iekļaut, jo šī zara mērķis ir tava vārda pievienošana sarakstam.)

## Veic nepieciešamās izmaiņas un iesūti tās

Tagad atver `Contributors.md` failu teksta redaktorā un pievieno tam savu vārdu. Nepievieno to faila sākumā vai beigās, bet ievieto to kaut kur pa vidu. Pēc tam saglabā failu.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Ja tu dosies uz projekta direktoriju un izpildīsi komandu `git status`, tu redzēsi, ka tajā ir izmaiņas.


Pievieno šīs izmaiņas zaram, kuru tu tikko izveidoji, ar `git add` komandu:

```
git add Contributors.md
```

Tagad iesūti šīs izmaiņas ar `git commit` komandu:
```
git commit -m "Add <tavs-vārds> to Contributors list"
```
aizvietojot `<tavs-vārds>` ar savu vārdu.

## Pievieno izmaiņas GitHub

Pievieno savas izmaiņas ar komandu `git push`:
```
git push origin <ievieto-zara-nosaukumu>
```
aizvietojot `<ievieto-zara-nosaukumu>` ar zara, kuru tu iepriekš izveidoji, nosaukumu.

## Iesniedz izmaiņas pārskatīšanai

Ja tu dosies uz savu GitHub repozitoriju, tu redzēsi `Compare & pull request` pogu. Nospied to.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Tagad iesniedz pievienotās izmaiņas.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Jau pavisam drīz es pievienošu visas tavas izmaiņas šī projekta galvenajam (master) zaram. Tu saņemsi paziņojumu e-pastā, tiklīdz izmaiņas būs pievienotas.

## Un ko tagad?

Apsveicam! Tu tikko pabeidzi standarta  _fork -> clone -> edit -> PR_  darbplūsmu, ar kuru turpmāk bieži nāksies sastapties kā līdzautoram.

Pastāsti par savu devumu saviem draugiem un sekotājiem, izmantojot [mūsu vietni](https://firstcontributions.github.io/#social-share).

Tu vari pievienoties arī mūsu slack komandai, ja tev nepieciešama palīdzība vai ir kādi jautājumi. [Pievienojies slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Tagad tu vari līdzdarboties arī citos projektos. Mēs esam sastādījuši sarakstu ar projektiem, kuros ir vienkāršas problēmas, ar kurām tu varētu sākt. Izpēti [projektu sarakstu mūsu vietnē](https://firstcontributions.github.io/#project-list).

### [Papildu materiāli](../additional-material/git_workflow_scenarios/additional-material.md)


## Pamācības citiem rīkiem

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
