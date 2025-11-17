[![KAY3BEK T3AWN OPEN SOURCE](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Awel Moucharaka

Fo9ma katbghi tbda chi 7aja jdida katkoun m39da flewl. Dik lkhouf anak tghlet ki3ssbek,5ossosan fach katkoun 5dam m3a nass o5rin. Walakin lblan dl open source w anak t5dm m3a nass f fra9i . Bghina , nsshlou 3likoum bach t3lmou tcharkou fchi projet open source b7al hada l awel mra .   

Rah blan tb9a t9ra kifach dir wla tchouf des tutoriels , walakin wach machi 7ssen nwriwk ki der bla matghlet ? Had lprojet l hadaf dyalou howa y3tek nassa2i7 w 5lik 3a9l : koulma knti mheden , ghat3lem 7ssen. Ila knti 3wal der awel i3ana , tbe3 had l5otowat w ra atsde9lk . Kanwa3dk , ghay3jbek l7al.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="connecter had repo" />

Ila makanch 3ndk git f pc dyalk, [ Telechargeh ]( https://help.github.com/articles/set-up-git/ )mn had site.

## Jbed had repo l3endek (kismiwha hna Fork)

Brek 3la dik FORK kima kaybanlk f tswira bach twli 3ndek b7al version dyal repo f compte dyalk .

## Telecharger 3ndk repo (Kismiwha clone )

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Clone d repo" />

Daba ,cloner repo dyalk l pc 3ndk. Brek 3la bottona d Clone w copier dik lien (HTTPS houwa sahel) ra kayna bottona 7da lien katcopiehlk nichan .

7el daba cmd (ila knti f windows) wla terminal (ila kan 3ndk mac wla 5dam b linux) w copier had les commandes li ghanwrik :

```
git clone "dik lien li 3ad copieti"
```
3andak t5liha hakak hhh "dik lien li 3ad copieti" (bla douk "") kteb tma lien li copieti fhemni . 

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copier l'URL dans le presse-papier" />

Atkoun b7al had chkel :
```
git clone https://github.com/smytk_dyal_github/first-contributions.git
```
rah `smytk_dyal_github`  hia smya li nta dayr. 
Daba nta fhad l5twa ghatelecharger ga3 had repo 3ndk f pc bach tbda tbeddel fiha. 

## Swb branche jdida dyalk

Daba f cmd nit wla terminal , d5l l dik lmilf li 3ad telechargeti (kteb had l3iba la ma3rftich d5l manuellement ) :

```
cd first-contributions
```
Daba ha kifach ghatswb branch dyalk `git checkout` :
```
git checkout -b "smya_dlbranch"
```

Par exemple :
```
git checkout -b add-brahim
```
(Machi darori tder f smya add , walakin gha bach nfhmo 3lach zdtiha)

## Bdl fl file d Contributors

Daba d5el l fichier dyal `Contributors.md` fchi editeur , zid smytk w chi lien ila bghiti (3andak der chi7aja 5ayba). Ila ktbti daba f dik cmd/terminal `git status`, aybanulk l3ibat li bdlti. Daba zidhoum l branch dyalk add-brahim bhad l3iba dyal `git add` :
```
git add Contributors.md
```

Sauvegardeha b `git commit`:
```
git commit -m "Add <smytk> to Contributors list"
```
der fblasst `<smytk>` smytk dbss7 (brahim matalan).

## PUSHIIII

Daba ghatpushi had lmodofication li derti l github b  `git push` :
```
git push origin <smya_dlbranch>
```
ana knt mssmiha add-brahim , nta bdlha bachma knti dayr .

## 7et les modifications bach ytchafo

Ila rj3ti l github atl9a dik l3iba dyal `Compare & pull request`
brek 3liha a5ay.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sf brek 3liha bach tle3 lnass li mss2oulin 3la hadchi.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Chwia mbe3d matjm3 dik lmodifications li derti . Aywslk mail ki9ololk fih ra safi dkchi dyalk nadi.

branche main dyalk maghaytbdel fiha walou daba . Ila bghiti ta main dyalk ykoun msynchroniser tbe3 had les étapes.

## 5li main dyalk synchronisé m3a contributors

B3da rje3 lmain matb9ach fdik add-brahim 
 ```
 git checkout main
 ```

zid lien d repo as `upstream remote url` :
```
git remote add upstream https://github.com/smytk_d_github/first-contributions
```
Ghi dik changes ydaro , 5ssk moraha tjbd version jdida dyal repo dyalk:
```
git fetch upstream
```

Hna kan9lbo 3la ga3 tghyirat li kaynin f lfork dyalk nta (upstream remote). Daba 3ad 5ssk tjm3 had jdida m3a repo dyalk (main) :
```
git rebase upstream/main
```
Daba ga3 tghyirat kaynin fl main. ila pushiti modifications aydaro ta f fork dyalk :
```
git push origin main
```

Daba ra jm3na branch dyal `<add-brahim>` m3a l main dyalna , w jm3na lmain dyalna m3a main dyalhom (yarbi tkoun fhmtini hh).Daba dik li drti flwl dyal `<add-votre-nom>` mab9atch 3ndha fa2ida , ila bghiti t7ydha :
```
git branch -d <add-brahim>
```
w ymklk t7yda ta mn repo li b3ida :
```
git push origin --delete <add-votre-nom>
```
Machi darori t7yd lbranch walakin raha salat 5smtha ma3ndha lach tb9a tma .

## Tutoriels bchi twichyat o5rin 


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

## Fin nmchi daba ?

Ymklkoum tjiw l slack fin kayna lfr9a d hadchi kaml , n9do n3awnokom w njawbo 3la chi ass2ila    [Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

