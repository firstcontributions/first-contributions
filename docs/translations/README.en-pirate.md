[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

'tis hard. 'tis always hard th' first time ye do somethin'. Especially when ye be collaboratin', makin' mistakes ain't a comfortable thin'. We wanted t' simplify th' way new open-source contributors learn & contribute fer th' first time.

Readin' tales & watchin' tutorials can help, but wha''s better than actually doin' th' stuff in a practice environment? This project aims at providin' guidance & simplifyin' th' way beginners make thar first contribution. If ye be lookin' t' make yer first contribution, follow th' steps below.

#### *If ye're nah comfortable wit' command line, [here be tutorials usin' GUI tools.](#Tutorials-Usin'-Other-Tools)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="plunder this code chest" />

If ye don't 'ave git on yer machine, [install it](https://help.github.com/articles/set-up-git/).

## Fork this repository

Fork this repo by skewerin' on th' fork button on th' top o' this page.
This will create a copy o' this repository in yer account.

## Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="make yer own copy o’ this treasure" />

Now clone this repo the on your machine. Go to your GitHub account, click on the clone button and then  click on *copy to clipboard* icon.

Open a terminal and run the following git command:

```bash
git clone "https://github.com/this-be-ye/first-contributions.git"
cd first-contributions
git checkout -b <add-your-branch-name>
git checkout -b add-luke-oliff
git add Contributors.md
git commit -m "Add <yer-name> to Contributors list"
git push origin <add-yer-branch-name>

```

where "url you copied" (without the quote marks) be the url for this repository (yes fork to this project). See the previous steps to obtain the url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="snatch the map link to yer clipboard" />

Fer example:

```bash
git clone https://github.com/this-be-ye/first-contributions.git
```

where `this-be-ye` be your GitHub username. Here you are copying the contents of the first-contributions repository in GitHub to your github acccount.

## Create a branch

Change the repository directory on your machine (if it already exists):

```bash
cd first-contributions
```

Now create a branch using the `git checkout` command:

```bash
git checkout -b <add-your-new-branch-name>
```

Fer example:

```bash
git checkout -b add-luke-oliff
```

(The name of the branch does not needs the and has the word *add* in it, but this a reasonable  include cause the purpose on this branch be t' add yer name t' a list.)

## Make necessary changes 'n commit those changes

Now open `Contributors.md` file in a text editor, add your name to it. Don't add it at the beginning or end at the file. Put it anywhere in between. Now, save the file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="check the ship’s log" />

If yes go to the project directory and execute the command `git status`, you will see the  changes.

Add those changes to the branch you just created using the `git add` command:

```bash
git add Contributors.md
```

Now commit those changes using the `git commit` command:

```bash
git commit -m "Add <yer-name> to Contributors list"
```

replacing `<your-name>` with your name.

## Push changes t' GitHub

Push your changes using the command `git push`:

```bash
git push origin <add-yer-branch-name>
```

replace `<add-your-branch-name>` with the name to the branch you created earlier.

## Submit yer changes fer review

If ye go to your repository on GitHub, you'll see a  `Compare & pull request` button.  Click on that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="raise a flag fer a pull request" />

Now submit the pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="send yer pull request to the captain" />

Soon It will merge all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where this go from here?

Well done! You just completed the standard _fork -> clone -> edit -> PR_ workflow that you will encounter often as a contributor!

Celebrate yer contribution and share it with yer hearties andn followers by going to [web app](https://firstcontributions.github.io/#social-share).

Now let's get ye started with contributing to other projects. We've compiled a list of projects with easy issues ye can get started on. Check out [the list of projects in web app](https://firstcontributions.github.io/#project-list).

### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Usin' Other Tools

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
