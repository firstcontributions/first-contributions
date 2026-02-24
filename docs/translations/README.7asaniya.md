[![teb9i T3AWN OPEN SOURCE](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Lmouchareka lewle
6abi3y 3nk ylin tbde v ey rwaye jdide lahy t3ud met3a9de, bikli 5ayev mn ta9la6, surtout ylin li t3ud techct9al m3a rwagij. ye9yr 4e simple ydur youda7 lk 8rk 3anou mahu b 4y sou3obe li knt chak!, lahy nshlou 3lik 4e w nvaslolk eydik vih yk youda7ulk les projets open source w tem tcharek v des autres projets.

rahou le plan 3nk tegra w tchouv des video wella coursat 3le youtube yk tt3alem, mais chbh lk na3tulk c'est cm1 yk ma ta9la6, 4e le projet lhedev menou 3ano ya36ik nasa2i7, kel ma cht9lt kthar, dur tt3alm 7att, lahy temchy 3le 4o l5ou6owat w dur nshllhu ye3jbok les open sources.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="connecti 3le 4e repo" />

ylin li t3ud ma 3ndk git v pchk , [ Nzlou ]( https://help.github.com/articles/set-up-git/ )mn 4y site.

## Gba8 4e projet 3ndk (esmhe hun Fork)

9mez 3le 4ik FORK kiv ma 8aher lk v capture yk t3ud 3ndk la version mn repo ngr comptak github.

## Telecharger 3ndk repo (Kismiwha clone )
## Nezel 3ndk 4i repo (esmhe clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Cloni repo" />

8rk, clonni repohk v pchk, 9mez 3le boton code w copi le lein (HTTPS houwe li hwyn w 6ales) rahy vm boton v zer l3arbi mn les lien hiye li tcopi

ew 8rk gis cmd (yla 3dt v widnows)  wella terminal (l mac w linux) w copie 4o les commandes li lahy na3at lk:

```bash
git clone "le lien li 3dt lo copier"
```
tgd t5aliha comme sa hhh "4k lien li copyt" (ma vih "") kteb vm le lien li copyt.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copier l'URL dans le presse-papier" />

yalthe t3ud comme sa:
```bash
git clone https://github.com/esmk_v_github/first-contributions.git
```
rah `esmk_v_github`  huwe esmk nte github.
8rk nte v 4y l5ou6we hamk tnezel 4y repo v pchk yk t3dl 3liha ta9yirat. 

## 3dl branche jdide lk nte

8rk ngr cmd wella terminal, d5el l 4k lmelef li 3ndk mnzlu (kteb 4y commande yk t3ud ngr 4i repo li nzlt )

```bash
cd first-contributions
```
8rk lahy na3atlk comment t3dl branche 5asa bik `git checkout` :
```bash
git checkout -b "esm_branchk"
```

Par exemple :
```bash
git checkout -b add-dedahi
```
(ma mohim 3nk dir add v esm la branche, mais la yk tvhm w twv)

## 3dl ta9yir v 4e le fichier Contributors

8rk gis 4e le fichier `Contributors.md` vet7u 3ndk v editor li tktb vih codatk(vs code, eclipse...), dir esmk vm.
ew rja3 chur cmd wella terminal w kteb `git status`, lahy tchuv ta9yirat li 3dlt. 8rk dirhm 3le branchk nte li mkivnk 3dlt add-dedahi b4i commande: `git add`

```bash
git add Contributors.md
```

sejelhe b `git commit`:
```bash
git commit -m "Add <esmk> to Contributors list"
```
dir v bel `<esmk>` esmk nte l7a9i9y (dedahi par exemple).

## PUSHIH

8rk lahy tepochi 4eli 3dlt v github b `git push` :

```bash
git push origin <esm_branchk>
```
ana knt msemiha add-dedahi, w nte dir v blhe 4eli knt dayer

## yk ta9yirat li 3dlt ynchavu

ylin tarja3 l github dur tchuv rwaye kiv `Compare & pull request`
9mez 3liha.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

9mez 3liha yk ychuvuhe nass li mes2ulin 3n 4i rwaye (4e projet open source).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

ylin 3dlt 4e, ydur yjik email ygulk 3nk cbn rahu 4eli 3dlt chavuh.

branche maink ma lahy ychangi vihe chy 8arke, ylin t3ud teb9i maink t3ud vihe 4e tali 3dlt 4o les etapes.

## 5aly maink vihe 4e ttally m3a contributors

apres rja3 lmain mchy 3n branchk nte add-dedahi

 ```bash
 git checkout main
 ```

dir lien repo as `upstream remote url` :

```bash
git remote add upstream https://github.com/smytk_d_github/first-contributions
```
dur tchuv ta9yirat 8ahru, ew 5asak 8rk ela dir version jdide mn repohk:

```bash
git fetch upstream
```

hun lahy nlwdu l ta9yirat li 5algin v le frok li 3dlt nte (upstream remote), 8rk 3ad 5asak ela tjma3 4e jdid m3a repohak (main) :
```bash
git rebase upstream/main
```
8rk ta9yirat 3adu cbn v main, ylin tepouchi ta9yirat lahy yndaro v fork li 3dlt 
```bash
git push origin main
```

8rk rane 5la6ne branchk `<add-brahim>` m3a le branch main l na7ne, w 5la6ne main na7ne m3a mainhm hume (nshll y3ud 4e wade7 lk sahby), ew 8rk 4k li 3dlt gbyl mn lwl `<add-votre-nom>` ma tlat 3dndhe 9ime, ila 3dt teb9y tem7ihe :
```bash
git branch -d <add-dedahi>
```
w tgd tem7ihe mli mn repo lekbire
```bash
git push origin --delete <add-votre-nom>
```
ma mohim tem7i branck ye9yr rahy 3dlt li 3lihe ma yalthe tbgue vm.

## Tutoriels bchi twichyat o5rin 
## Tutoriels l rwayat 5ryn


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |


