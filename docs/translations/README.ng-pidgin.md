[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

Dis project dey to make am simple and guide beginners how dem go make their first contribution. If you wan make your first contribution, follow these steps wey dey below.

_If command line no dey comfortable for you, [see tutorials wey use GUI tools here.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### If you no get git for your machine, [install am](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Fork this repository

Fork this repository by clicking on the fork button for the top of this page.
Dis one go create copy of dis repository for your account.

## Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Now clone the forked repository go your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```bash
git clone "url wey you just copy"
```

where "url wey you just copy" (without the quotation marks) na the url to this repository (your fork of this project). See the previous steps to get the url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:

```
git clone git@github.com:this-is-you/first-contributions.git

```

where this-is-you na your GitHub username. Here you dey copy the contents of the first-contributions repository for GitHub go your computer.

## Create a branch
Change go the repository directory for your computer (if you no dey there already):

```
cd first-contributions

```

Now create a branch using the git switch command:

```
git switch -c your-new-branch-name

```

For example:

```
git switch -c add-desmond-ezo-ojile

```

## Make necessary changes and commit those changes
Now open Contributors.md file for a text editor, add your name to am. No add am for the beginning or end of the file. Put am anywhere for middle. Now, save the file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />
If you go to the project directory and run the command git status, you go see say changes dey.

Add those changes to the branch wey you just create using the git add command:

```
git add Contributors.md

```
Now commit those changes using the git commit command:

```
git commit -m "Add your-name to Contributors list"

```

replace your-name with your own name.

## Push changes to GitHub
Push your changes using the command git push:

```
git push -u origin your-branch-name

```

replace your-branch-name with the name of the branch wey you create before.

<details>
<summary> <strong>If you get any errors while pushing, click here:</strong> </summary>

## Authentication Error
   <pre>remote: Support for password authentication don remove since August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
Go to GitHub's tutorial on how to generate and add SSH key to your account.
</details>

## Submit your changes for review
If you go to your repository on GitHub, you go see Compare & pull request button. Click on that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />
Now submit the pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
Soon I go merge all your changes into the main branch of this project. You go get notification email once the changes don merge.

## Where to go from here?
Congrats!