[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Umusanzu Wa mbere

Uyu mushinga ugamije koroshya no kuyobora uburyo abatangizi batanga umusanzu wabo wa mbere. Niba ushaka gutanga umusanzu wawe wambere, kurikiza intambwe zikurikira.

_Niba utorohewe no gukoresha 'command line', [aha hari inyigisho zo gukoresha ibikoresho bya GUI.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Niba udafite git muri mudasobwa yawe, [yishyiremo](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Koporora(Fork) iyi ripozitori(repository)

Koporora(Fork) iyi ripozitori(repository) ukanze kuri buto(button) ya fork hejuru kuri iyi paji.
Ibi birakora kopi yiyi ripozitori(repository) kuri konte yawe.

## Manura(Clone) ya ripozitori(repository)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Noneho manura(Clone) ya ripozitori(repository) wa kopiye kuri mudasobwa yawe. Jya kurubuga rwawe rwa GitHub, Fungura ya ripozitori(repository) wa kopiye(Fork), kanda kuri 'code button', ubundi kuri 'SSH tab' hanyuma ukande kuri ' _copy url to clipboard_ '.

Fungura 'terminal' yawe ukore komande ya git ikurikira:

```bash
git clone "ya url wakoporoye"
```

Aho "ya url wakoporoye" (nta twuguruzo n’utwugarizo(quotation marks) ) ariyo url yiyi ripozitori(repository) (iyo wakoporoye(Fork) kuri uyu mushinga). Reba intambwe zabanjirije kugirango ubone url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Urugero:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

Aho `this-is-you` ari izina ukoresha kuri GitHub. Hano urimo gukoporora ibiri mububiko bwa first-contributions ripozitori(repository) kuri GitHub ubujyana muri mudasobwa yawe.

## Kora ishami(branch)

hindurira muri ya ripozitori(repository) aho iherereye muri mudasobwa yawe (niba utaragera aho):

```bash
cd first-contributions
```

Noneho kora ishami(branch) ukoresheje `git switch` komande(command):

```bash
git switch -c izina-rishya-ryishami-ryawe
```

Urugero:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>niba uri guhura n' imbogamizi mu gukoresha 'git switch', kanda aha:</strong> </summary>

Niba ubutumwa bw' imbogamizi ari "Git: `switch` is not a git command. See `git –help`" ,birashoboka ko uri gukoresha verisiyo(version) ishaje ya git.

Muri iki kibazo, gerageza gukoresha `git checkout` mu mwanya w' ibyabanje:

```bash
git checkout -b izina-rishya-ryishami-ryawe
```

</details>

## Kora impinduka zikenewe kandi wemeze(commit) izo mpinduka

Noneho fungura `Contributors.md` dosiye aho ukorera(text editor), wongereho izina ryawe. Nturyongere ku ntangiriro cyangwa ku iherezo rya dosiye. Yishyira ahari hose hagati. Noneho, bika(save) dosiye.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Nujya mu bubiko bw' uwo mushinga ubundi ugashyira mu bikorwa komande(command) `git status`, uribuhabone impinduka.

Ongera izo mpinduka ku ishami(branch) wari wakoze ukoresheje iyi `git add` komande(command):

```bash
git add Contributors.md
```

noneho emeza izo mpinduka ukoresheje `git commit` komande(command):

```bash
git commit -m "Kongera izina-ryawe kuri Contributors list"
```

gurana `izina-ryawe` n' izina ryawe ryanyaryo.

## Sunika(push) impinduka kuri GitHub

sunika(push) impinduka zawe ukoresheje komande(command) `git push`:

```bash
git push -u origin izina-rishya-ryishami-ryawe
```

gurana `izina-rishya-ryishami-ryawe` n' izina ry' ishami wakoze kare.

<details>
<summary> <strong>niba uri guhura n' imbogamizi mugihe usunika(push), Kanda aha:</strong> </summary>

- ### ikosa mu kwemererwa (Authentication Error)

  <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>

  Jya ku [inyigisho zo kuri GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) zivuga ku jeneretinga(generating) no gukomfigira(configuring) `SSH key` kuri konte(account) yawe.

  hanyuma uri bukenere gukora 'git remote -v' kugira ugenzura aderesi(address) yawe.

  Niba bisa nkibi:
    <pre>origin	https://github.com/your-username/your_repo.git (fetch)
    origin	https://github.com/your-username/your_repo.git (push)</pre>

  bihindure ukoresheje iyi komande(command):

  ```bash
  git remote set-url origin git@github.com:izina-ryawe-ukoresha/your_repo.git
  ```

  Bitabaye ibyo, urakomeza kubazwa izina ukoresha n' ijambobanga unakomeze ubone ikosa ryo kwemererwa(authentication error).
  </details>

## Ohereza impinduka zawe ngo zisubirwemo

Nujya kuri ripozitori(repository) yawe kuri GitHub, uribubone buto(button) ivuga `Compare & pull request`. Kanda kuri iyo buto(button).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Noneho ohereza ubusabe bw'ubufatanye(pull request).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Vuba ndahuza impinduka zawe zose ku ishami rikuru(main branch) ry'uyu mushinga. Uzabona imeri imenyesha impinduka nizimara guhuzwa..

## Ibyo Ukurikizaho?

Ndagushimiye! Warangije byuzuye _gukoporora(fork) -> kumanura(clone) -> gusubiramo(edit) -> gusaba ubufatanye(pull request)_ umurimo wasabwaga nk' umufatanyabikorwa!

Ishimire ubufatanye bwawe ndetse unabusangize inshuti zawe n' abagukurikira unyuze [ku rubuga(web app)](https://firstcontributions.github.io/#social-share).

Niba ushaka kwitoza bisumbyeho, reba aha [ibigenderwaho kugutanga umusanzu(code contributions)](https://github.com/roshanjossey/code-contributions).

Noneho reka tugutangire gutanga umusanzu muyindi mishinga. Twakoze urutonde rwimishinga ifite ibibazo byoroshye ushobora gutangira. Rebaho [urutonde rw'imishinga ku rubuga(web app)](https://firstcontributions.github.io/#project-list).

### [Inyigisho z'inyongera](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Inyigisho Ukoresheje Ibindi bikoresho

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Uyu mushinga uterwa inkunga na:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
