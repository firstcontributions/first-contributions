[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Ewak Ituga Omamot

Eiyin project enim roworiyin guide bwain etruganin omamot enim make ewak first contribution. Eiyin ngabuna enim etruganin first contribution, follow steps ebwak.

_If ngabuna enim ogeda command line, [ei tutorials ogeda GUI tools.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### If git ngabuna ogeda machine, [install git](https://docs.github.com/en/get-started/quickstart/set-up-git)

## Fork repository

Fork repository, click fork button top page. Enim create copy repository account ngabuna.

## Clone repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Eiyin clone forked repository machine ngabuna. Go GitHub account, open forked repository, click code button, click SSH tab, then click _copy to clipboard_ icon.

Open terminal, run command:

```
git clone "url you just copied"
```

"Url you just copied" (nogud quotation marks) enim url repository ngabuna (fork project). Oge steps ngabuna obwen url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:


```git clone git@github.com:this-is-you/first-contributions.git```

"this-is-you" enim GitHub username ngabuna. Eiyin ngabuna enim copy contents first-contributions repository GitHub computer ngabuna.

## Eiyin build branch

Change repository directory computer ngabuna (if ngabuna ogeda):

```cd first-contributions```

Eiyin create branch, use command:

```git switch -c your-new-branch-name```

Example:

```git switch -c add-alonzo-church```

<details>
<summary> <strong>If error using git switch, click here:</strong> </summary>

If error "Git: `switch` is not a git command. See `git –help`", git version ngabuna old.

Try `git checkout`:

```git checkout -b your-new-branch-name```

</details>

## Make changes and commit changes

Open `Contributors.md` file text editor, add name ngabuna. Not put begin or end file. Put anywhere in between. Save file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

If go project directory, execute `git status`, ngabuna enim see changes.

Add changes branch created, use command:

```git add Contributors.md```

Commit changes:

```git commit -m "Add your-name to Contributors list"```

"your-name" enim name ngabuna.

## Push changes GitHub

Push changes:

```git push -u origin your-branch-name```

"your-branch-name" enim name branch ngabuna created.

<details>
<summary> <strong>If error while pushing, click here:</strong> </summary>

- ### Authentication Error

     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on SSH key.

  Run 'git remote -v' check remote address.
  
  If like this:
  <pre>origin https://github.com/your-username/your_repo.git (fetch)
  origin https://github.com/your-username/your_repo.git (push)</pre>
  
  Change it:

  bash
  git remote set-url origin git@github.com:your-username/your_repo.git

  Otherwise, still prompt username and password, get authentication error.

</details>

## Submit changes for review

Go repository ngabuna GitHub, see `Compare & pull request` button. Click that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Submit pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Soon, changes ngabuna enim merge main branch project. Ngabuna enim get email notification after merged.

## Etuga ian makuri ewak?

Congrats! Ngabuna enim complete ewak _fork -> clone -> edit -> pull request_ workflow usually contributor enim do!

Celebrate contribution ngabuna, share with friends bwain [web app](https://firstcontributions.github.io/#social-share).

Want more practice? Check [code contributions](https://github.com/roshanjossey/code-contributions).

Ngabuna ogeda? Check [list projects web app](https://firstcontributions.github.io/#project-list).

### [Additional material](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Using Other Tools

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Eiyin project enim support by:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
