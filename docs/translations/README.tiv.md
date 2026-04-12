[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Mnyam u Mngem Mtem

A mngem a sha u wan u simplify u sha u guide u or mnyam we ka nyian u mngem mtem u ve. Mnyam we ka nyian u mngem mtem u ve, ka sha u follow u steps we ka ve.

_I sha u nyian u command line, [ka ve tutorials we ka use GUI tools.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />

#### Mnyam we ka nyian git u or machine u, [ka install u](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Mnyam u Fork a Repo a

Mnyam u fork a repo a ka u click u fork button we ka or top u page a.  
U sha mngem u copy u repo a u or account u.

## Mnyam u Clone a Repo a

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the repository" />

Nyian u clone u forked repo a u or machine u. Ka ve u GitHub account u, ka open u forked repo a, ka click u code button, ka ve u SSH tab, ka click u _copy url to clipboard_ icon.

Open a terminal and run the following git command:

```bash
git clone "url we ka copy"
```

U "url we ka copy" (ka ve quotation marks) sha u url u repo a (u fork u project a). Ka ve u steps we ka ve sha u obtain u url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Mnyam u example:

```bash
cd first-contributions
```

Ka mnyam u branch u using u `git switch` command:

```bash
git switch -c branch-u-we-ka-mnyam
```

Mnyam u example:

```bash
git switch -c mnyam-alonzo-church
```

<details>
<summary> <strong>Ka ve u get errors we ka using u git switch, ka click sha a:</strong> 
</summary>

Ka ve u error message "Git: `switch` sha u not a git command. Ka ve u `git –help`" ka appear, a sha u because ka using u older version u git.  

Nyian u case a, ka try u use u `git checkout` sha a:

```bash
git checkout -b branch-u-we-ka-mnyam
```

</details>

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, add your name to it. Don't add it at the beginning or end of the file. Put it anywhere in between. Now, save the file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="status u git" />

Ka ve u go sha u project directory a ka execute u command u `git status`, ka ve u see ka ve u changes.  

Ka add u changes a sha u branch we ka mnyam u using u `git add` command:

```bash
git add Contributors.md
```

Nyian ka commit u changes a using u `git commit` command:

```bash
git commit -m "Add u-name u sha Contributors list"
```

Ka ve u replace u `u-name` sha u name u.

## Ka Push u changes sha GitHub

Ka push u changes u using u command u `git push`:

```bash
git push -u origin branch-u-we-ka-mnyam
```

Ka ve u replace u `branch-u-we-ka-mnyam` sha u name u branch we ka mnyam u earlier.

<details>
<summary> <strong>Ka ve u get errors we ka pushing, ka click sha a:</strong> 
</summary>

### Error u Authentication
     <pre>remote: Support sha password authentication ka remove sha August 13, 2021. Ka ve u use u personal access token sha a.
  remote: Ka ve u see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ sha more information.
  fatal: Authentication failed sha 'https://github.com/<u-username>/first-contributions.git/'</pre>

Ka go sha [GitHub tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) sha mnyam u generate ka configure u SSH key sha account u.

Nyian, ka ve u run 'git remote -v' sha check u remote address u.

Ka ve a look anything like a:

<pre>origin	https://github.com/u-username/u_repo.git (fetch)
  origin	https://github.com/u-username/u_repo.git (push)</pre>

Ka change sha using u command a:

```bash
git remote set-url origin git@github.com:u-username/u_repo.git
```

Nyian ka ve u still get prompt sha username ka password ka get error u authentication.
</details>

## Ka Submit u changes sha review

Ka ve u go sha u repository u sha GitHub, ka ve u see u `Compare & pull request` button. Ka click sha u button a.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare ka mnyam pull request" />

Nyian ka submit u pull request a.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Soon ka ve u merge u changes u sha main branch u project a. Ka ve u get u notification email nyian ka merge u changes a.

## Ka ve u go sha nyian?

Congrats! Ka ve u complete u standard _fork -> clone -> edit -> pull request_ workflow we ka ve u encounter sha contributor!

Ka celebrate u contribution u ka share sha friends ka followers u by ka go sha [web app](https://firstcontributions.github.io/#social-share).

Ka ve u like more practice, ka checkout [code contributions](https://github.com/roshanjossey/code-contributions).

Nyian ka start u contributing sha other projects. Ka compile u list u projects we ka ve u easy issues we ka start sha a. Ka check sha [list u projects sha web app](https://firstcontributions.github.io/#project-list).

### [Material u Additional](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials we ka Using Other Tools

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> 
| <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> 
| <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> 
| <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> 
| <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> 
| <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md) 
| [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md) 
| [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md) 
| [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md) 
| [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md) 
| [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)