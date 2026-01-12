[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Awel Contribution fil github bil tounsi 🇹🇳

Dima tesme3 bil term "contribute to open source" ama mata3rech kifh tebda? Houni bch tel9a bil 5otwa bil 5otwa kifh tebda wtkonlek 
awel contribution ta3melha 3al github bch tkon pratique tjareb wtchof kolchy b3inik.

_Ken mat7ebech tesa3mel el cmd, [hedhom tutorials o5rin testa3mel fihom des logiciles.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Edhaken moch sabeb git 3andek fil pc, [sobo mil lien hedha](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Forki el repo

Inzel 3ala "Fork" mil fo9 bch tforki el repository.
Haka iwali 3andek copie f compte mt3ek tejem tebedel fiha kima t7eb.

## Cloni el repo

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Tw cloni el repo li 3meltelha fork lil machine mte3ek. Imchi lil compte github 7el el forked repo inzel 3al button "code" b3d el ssh b3d copi lien el mawjoud.

Tw 7el terminal wekteb el commande hedhi 

```bash
git clone "lien li copito"
```
Win "lien li copito" (m8ir el quotation marks) 7ot lien lil repo li 3meltelha fork. chof steps li t3adew bch te5o el lien.

Par exemple: 
```bash
git clone git@github.com:this-is-you/first-contributions.git
```

Win this-is-you edheka nom mte3 el github mte3ek. honi 9e3ed tcopi el contenu mta3 the first-contributions repo 3al github lil pc mte3ek.

## A3mel branch jdid
Badel lil directory mta3 el repo fil pc mte3ek (edhaken moch deja 8ad):

```bash
cd first-contributions
```

Tw a3mel branch bil command `git switch`:

```bash
git switch -c your-new-branch-name
```

Par exemple:

```bash
git switch -c awel-contribution-github
```

<details>
<summary> <strong>Edhaken jek error wenti testa3mel fil git switch, Inzel lena:</strong> </summary>

Edhaken lerror "Git: `switch` is not a git command. See `git –help`" dhohret, yomken 5tr testa3mel fi version 9dima mta3 git.

Fil 7ala hedhi, jareb ista3mel `git checkout`:

```bash
git checkout -b your-new-branch-name
```

</details>


## A3mel les changements lezmin b3d commiti les changements

Tw 7el el file `Contributors.md` fil editor, zid ismek fiha. Mat7otoch milowel wala filo5er mta3 el file. 7ot fi plasa fil west. Tw, a3melo save.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ken temchi lil directory mta3 repo wtekteb el command `git status`, tw tchof fama changements saret.

Zid les changements hedhom lil branch eli 3meltha bil command `git add`:

```bash
git add Contributors.md
```
Tw a3mel commit lil les changements bil commande `git commit`:

```bash
git commit -m "Add your-name to Contributors list"
```
Badel `your-name` bismek.

## Pushi les changements 3al GitHub

A3mel push lil les changements bi ista3mel el command `git push`:

```bash
git push -u origin your-branch-name
```

Badel `your-branch-name` bi isem lbranch l3meltha se3a.

<details>
<summary> <strong>Edhaken jek error w9t tpushu, inzel lena:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  imchi el [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) kifh tgeneri wtconfiguri SSH key el compte mte3ek.

  Zeda, tejem t5adem 'git remote -v' bch tchof remote address mte3ek.
  
  Edhaken dhohretlek 7aja haka:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>
  
  bedelha bil command hedhi:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  Sinon bch yo93ed ijik el error mta3 el username wel password wel get authentication.
</details>

## Submiti les changements mte3ek lil review

Ken temchi lil repo mte3ek 3al github, tw  tchof button `Compare & pull request`. Enzel 3lih.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Tw a3mel sumbit lil pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

3ala 9rib tw na3mel merge lil les changements mete3ek lil main branch mta3 lprojet hedha. Tw tjik notification email ki tsir merge lil les changements.

## chnowa ta3mel taw?

Mabrouk! kamelt el workflow standard mta3 _fork -> clone -> edit -> pull request_ eli 3al a8leb yete7seblek ka contributor!

I7tefel w Cherek el contribution hedhi m3a s7abek wel followers 3al site [web app](https://firstcontributions.github.io/#social-share).

Edhaken t7eb practice akther, chof [code contributions](https://github.com/roshanjossey/code-contributions).

Tw 5al nebdew ncontributiw fi des projets o5rin. a3melna list fiha des projets fihom error sehlin tejem tebda bihom. Chof [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [material o5rin](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials bista3mel Tools o5rin

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>This project is supported by:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>