[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions (Caveman Speak)

Big brain first time scary. Tribe work together. Make mistake — ouch. This place help you learn give code to world **first time** with small steps.

Want big smart words? Read [normal English README](../../README.md).

#### *No like black box with letters? [Use clicky tools instead.](#tutorials-using-other-tools)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the cave" />

No git on rock computer? [Get git first](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Steal copy of repo (fork)

Hit **Fork** button top of page. Now repo live in **your** cave (your GitHub).

## Bring repo home (clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the cave" />

Open your fork. Green **Code** button. Copy link (SSH good).

Terminal say:

```bash
git clone "paste-url-here"
```

Paste = URL of **your** fork, not neighbor fork.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL" />

Example:

```bash
git clone git@github.com:you-name-here/first-contributions.git
```

`you-name-here` = your GitHub name. Repo now sit on your machine. Good.

## Make branch (new path)

Go into folder:

```bash
cd first-contributions
```

Make branch:

```bash
git switch -c your-branch-name
```

Example:

```bash
git switch -c add-grug-name
```

Branch name no must say `add` but tribe understand if you do.

<details>
<summary><strong>Old git say no <code>switch</code>? Click.</strong></summary>

Try old way:

```bash
git checkout -b your-branch-name
```

</details>

## Change file. Save. Commit.

Open `Contributors.md`. Put your name in middle somewhere — not first line, not last line. Save.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

```bash
git status
```

Show changes. Good.

```bash
git add Contributors.md
git commit -m "Add your-name to Contributors list"
```

Put real name where `your-name` go.

## Push to sky (GitHub)

```bash
git push -u origin your-branch-name
```

Use same branch name you made.

## Ask tribe chief (pull request)

On GitHub you see **Compare & pull request**. Smash button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and pull request" />

Send it.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Later merge happen. Email come. You happy. Tribe happy.

## What now?

You do **fork → clone → edit → pull request**. Same path many projects use.

Tell other cave friends: [share page](https://firstcontributions.github.io/#social-share).

More hunt for easy work: [project list](https://firstcontributions.github.io/#project-list).

Practice more code: [code contributions](https://github.com/roshanjossey/code-contributions).

### [Extra scrolls (git stuff)](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials using other tools

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
