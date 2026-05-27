[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _Soma ibi mu [ndimi zindi](Translations.md)._

# Umusanzu wa Mbere

Ni bigoye nagato buri gihe ubwa'mbere ukora ikintu. Cyane cyane iyo mukorana hamwe nabandi, gukora amakosa si ingorane. Twashakaga koroshya inzira nshya y'abafatanyabikorwa kumenya no gutanga umusanzu bwa mbere.

Gusoma inyandiko n'amashusho bishobora gufasha, ariko ni iki kiziza kurusha gukora ibintu nyabyo mu nzira y'ibikorwa by'inyigisho? Uyu mushinga ugamije gutanga amabwiriza no koroshya uburyo abasangizi bashya batanga umusanzu wabo wa mbere. Niba ushaka gutanga umusanzu wawe wa mbere, kurikira intambwe zikurikira.

#### _Niba utituje na command line, [hano hari amasomo akoresha ibikoresho bya GUI.](#Amasomo-Akoresha-Ibikoresho-Bindi)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Forkinga iyi repository" />

#### Niba udafite git kuri mudasobwa yawe, [yinjiza](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Forkinga iyi repository

Forkinga iyi repository ugenderera ku buto bwa fork hejuru y'iyi paji.
Bizohereza kopi y'iki repository mu konti yawe.

## Koporora (Clone) repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="koporora iyi repository" />

Ubu koporora repository ufashe kuri mudasobwa yawe. Jya ku konti yawe ya GitHub, fungura repository ufashe, kanda buto ya code, hanyuma ku ibendera rya SSH hanyuma ukande _kopi URL mu clipboard_.

Fungura terminal hanyuma ukore itegeko rikurikira rya git:

```bash
git clone "url wacyanditse"
```

aho "url wacyanditse" (nta nyandiko zikingira) ari url y'iyi repository (fork yawe y'iyi mushinga). Reba intambwe z'ibanze kugira ngo ubone url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="kopi URL mu clipboard" />

Urugero:

```bash
git clone git@github.com:uri-we/first-contributions.git
```

aho `uri-we` ari izina ryawe rya GitHub. Hano uri gukoporora ibiri mu repository bwa first-contributions kuri GitHub kuri mudasobwa yawe.

## Kora ishami (Branch)

Hindura ku repository bwawe kuri mudasobwa yawe (niba utahari):

```bash
cd first-contributions
```

Ubu kora ishami ukoresheje itegeko `git switch`:

```bash
git switch -c izina-ryawe-rishya-ry-ishami
```

Urugero:

```bash
git switch -c ongeraho-alonzo-church
```

<details>
<summary> <strong>Niba wahawe amakosa ukoresheje git switch, kanda hano:</strong> </summary>

Niba ubutumwa bw'ikosa "Git: `switch` si itegeko rya git. Reba `git --help`" bugaragara, birashoboka ko ukoresha verisiyo ya kera ya git.

Muri iki gihe, gerageza gukoresha `git checkout` aho:

```bash
git checkout -b izina-ryawe-rishya-ry-ishami
```

</details>

## Kora impinduka ngombwa hanyuma uzishire mu bikorwa

Ubu fungura dosiye `Contributors.md` mu murimo w'inyandiko, wongeraho izina ryawe. Ntiwongerere ku ntangiriro cyangwa ku mpera ya dosiye. Shyira ahantu hose hagati. Ubu bika dosiye.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Niba ujya mu repository bw'umushinga hanyuma ukore itegeko `git status`, uzabona hari impinduka.

Ongeraho izo mpinduka ku ishami watahuye ukoresheje itegeko `git add`:

```bash
git add Contributors.md
```

Ubu shyira izo mpinduka mu bikorwa ukoresheje itegeko `git commit`:

```bash
git commit -m "Ongeraho izina-ryawe ku rutonde rw'Abafatanyabikorwa"
```

usimbuye `izina-ryawe` n'izina ryawe.

## Kohereza impinduka kuri GitHub

Kohereza impinduka zawe ukoresheje itegeko `git push`:

```bash
git push -u origin izina-ryawe-ry-ishami
```

usimbuye `izina-ryawe-ry-ishami` n'izina ry'ishami waremye mbere.

<details>
<summary> <strong>Niba wahawe amakosa igihe ukohereza, kanda hano:</strong> </strong> </summary>

- ### Ikosa ryo Kwinjira

       <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.

  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;izina-ryawe&gt;/first-contributions.git/'</pre>
  Jya ku <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account">amashusho ya GitHub</a> yo gukora no gushyira umufunguzo wa SSH mu konti yawe.

  Nanone, ushobora gushaka kukora 'git remote -v' kugira ngo ugenzure aderesi yawe ya remote.

  Niba ibisa nk'ibi:
    <pre>origin	https://github.com/izina-ryawe/repository-bwawe.git (fetch)
    origin	https://github.com/izina-ryawe/repository-bwawe.git (push)</pre>

  hindura ukoresheje iri tegeko:

  ```bash
  git remote set-url origin git@github.com:izina-ryawe/repository-bwawe.git
  ```

  Bitabyaye uzakomeza gusezeranwa na username na password hanyuma uhawe ikosa ryo kwinjira.
  </details>

## Ohereza impinduka zawe kugira zisubirwemo

Niba ujya ku repository bwawe kuri GitHub, uzabona buto ya `Compare & pull request`. Kanda kuri iyo buto.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="kora pull request" />

Ubu ohereza pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="ohereza pull request" />

Vuba nzashyiraho impinduka zawe zose mu ishami nkuru y'uyu mushinga. Uzahabwa imeyili y'itangazo nzimpinduka zishyizweho.

## Uzajya he uhereye hano?

Mubyishimiye! Warangije inzira isanzwe ya _fork -> clone -> hindura -> pull request_ uzahura na yo kenshi nka mufatanyabikorwa!

Ibusu umusanzu wawe hanyuma usangire n'inshuti n'abakurikira bawe ujya ku [porogaramu ya interineti](https://firstcontributions.github.io/#social-share).

Niba ushaka gukora ibikorwa bingana, reba [code contributions](https://github.com/roshanjossey/code-contributions).

Ubu ni tugutangire gutanga umusanzu ku mishingaindi. Twateguye urutonde rw'imishinga ifite ibibazo byoroshye ushobora gutangira. Reba [urutonde rw'imishinga mu porogaramu ya interineti](https://firstcontributions.github.io/#project-list).

### [Ibikoresho biyongera](../additional-material/git_workflow_scenarios/additional-material.md)

## Amasomo Akoresha Ibikoresho Bindi

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/960px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
