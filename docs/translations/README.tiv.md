[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

Tom ne ngu wasen u pasen kpaa a tese mba hiihii gbenda u wan uwegh sha utom mba open source. Aluer u ngu keren u wan uwegh sha hiihii yô, dondo igbenda i i tese shin heen ne.

_Aluer u fa u pasen akaa sha command line ga yô, [ngun ne ka igbenda i u fatyô u dondon sha igbenda i GUI la.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Aluer u ngu a git sha mashin wou ga yô, [tsegha u](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Kopa repository ne sha account wou (Fork)

Hii u kpan repository ne (fork) sha u kenden uwegh sha 'fork' button u a lu sha ajiir a hene ijiir i dedoo i í lu sha gbaa u sha la. Ngun ne a ver kôpi u repository ne sha account wou.

## Kopa repository la va a mi sha mashin wou (Clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Hene yô, kopa (clone) repository u u sember fork la sha mashin wou. Za sha GitHub account wou, bugh repository u u sember fork la, kende uwegh sha 'Code' button la, nahan za sha ijiir i SSH la, keera kôpi u URL la (copy url to clipboard).

Bugh terminal wou nahan run (yila) git command ne:

```bash
git clone "URL u u sember kôpi la"
```

U tesen ikyav:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

Sha heen ne, `this-is-you` ka username wou u GitHub. U ngu kôpin akaa a a lu ker a repository u first-contributions la van a mi sha mashin wou.

## Dugh nongo u he (Create a branch)

Za ijiir i repository la i lu sha mashin wou la (aluer u ngu ker ga yô):

```bash
cd first-contributions
```

Hene yô, dugh nongo u he (branch) sha u pasen git command ne:

```bash
git switch -c iti-i-nongo-wou-u-he
```

U tesen ikyav:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>Aluer u zua a mbamgbe sha u pasen git switch yô, kende uwegh heen:</strong> </summary>

Aluer u zua a loho u a kaa ér "Git: `switch` is not a git command. See `git –help`" yô, ngu a lu nahan sha ci u u ngu pasen git u he ga.

Sha ci u ngula yô, nahan kar u pasen `git checkout` di:

```bash
git checkout -b iti-i-nongo-wou-u-he
```

</details>

## Eren mbamgbe mba u pasen kpaa u ver ve sha git (Commit)

Hene yô, bugh `Contributors.md` fail la sha text editor, nahan nger iti you sha mi. De ngeren i sha hiihii shin sha mkur u fail la ga. Nger i sha hen zwa ijiir i í lu hen atô la. Nahan, kosol fail la.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Aluer u za sha directory u project la nahan u pase command u `git status` yô, u nenge a mbampase mba u er la.

Ver mbampase mbara sha nongo u u sember dugh la sha u pasen command u `git add` ne:

```bash
git add Contributors.md
```

Hene yô, koso mbampase mbara sha u pasen command u `git commit` ne:

```bash
git commit -m "Add iti-you to Contributors list"
```

gema gware `iti-you` la nahan nger iti you.

## Tindi mbampase mbara sha GitHub (Push)

Tindi mbampase mbara sha u pasen command u `git push` ne:

```bash
git push -u origin iti-i-nongo-wou-la
```

gema gware `iti-i-nongo-wou-la` sha iti i nongo (branch) u u sember dugh la.

<details>
<summary> <strong>Aluer u zua a mbamgbe sha u pushes yô, kende uwegh heen:</strong> </summary>

- ### Mbamgbe mba Authentication
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  Za sha [GitHub tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) sha u fan kpaa u veren SSH key sha account wou.
  
  Nahan kpaa, u fatyô u pasen command u 'git remote -v' sha u nengen a ijiir i remote address wou.
  
  Aluer i lu nahan yô:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>
  
  gema i sha command ne:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  Aluer u er nahan ga yô, a lu keren username kpaa a password nahan a pase u mbamgbe mba authentication la.
</details>

## Na mbampase mbara sha u nengen a mi (Pull Request)

Aluer u za sha repository wou sha GitHub yô, u nenge a button u `Compare & pull request` la. Kende uwegh sha button la.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

Nahan na pull request la.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Sember yô, me koso mbampase mbara cii nahan me wa ve sha main branch u project ne. U zua a loho sha email aluer i koso mbampase mbara cii yô.

## Ka ijiir i nyi u zough a mi hene?

Mkom u msur uwegh! U sember completed standard workflow u _fork -> clone -> edit -> pull request_ u u lu dondon sha utom mba wan uwegh sha open source la!

Ember iwase you la nahan pase i sha ahurai wou kpaa a mbagenev sha u zan sha [web app](https://firstcontributions.github.io/#social-share).

Aluer u soo u pasen akaa agen yô, za sha [code contributions](https://github.com/roshanjossey/code-contributions).

Hene yô, se hii u wan uwegh sha utom mba mbagenev. Se ver ajiir a utom a a lu a mbamgbe a u fatyô u hiin sha mi yô. Nenge [nongo u utom mbara sha web app la](https://firstcontributions.github.io/#project-list).

### [Akaa agen a wasen](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Using Other Tools

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/960px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
