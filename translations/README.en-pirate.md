[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

'tis hard. 'tis always hard th' first time ya do somethin'. Especially when ya be collaboratin', makin' mistakes ain't a comfortable thin'. We wanted t' simplify th' way new open-source contributors learn & contribute fer th' first time.

Readin' tales & watchin' tutorials can help, but wha's better than actually doin' th' stuff in a practice environment? This project aims at providin' guidance & simplifyin' th' way beginners make der first contribution. If ya be lookin' t' make yer first contribution, follow th' steps below.

#### *If ya're nah comfortable wit' command line, [here be tutorials usin' GUI tools.](#Tutorials-Usin'-Other-Tools)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

If ya don't 'ave git on yer machine, [install it](https://help.github.com/articles/set-up-git/).

## Fork this repository

Fork this repo by skewerin' on th' fork button on th' top o' this page.
This will create a copy o' this repository in yer account.

## Clone th' repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Now clone this repo t' yer machine. Go t' yer GitHub account, skewer on th' clone button 'n then skewer th' *copy t' clipboard* icon.

Open a terminal 'n run th' followin' git command:

```
git clone "url ya jus' copied"
```

where "url ya jus' copied" (without th' quote marks) be th' url t' this repository (yer fork o' this project). See th' previous steps t' obtain th' url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Fer example:

```
git clone https://github.com/this-be-ya/first-contributions.git
```

where `this-be-ya` be yer GitHub username. Here ya're copyin' th' contents o' th' first-contributions repository in GitHub t' yer 'puter.

## Create a branch

Change t' th' repository directory on yer 'puter (if ya be nah already thar):

```
cd first-contributions
```

Now create a branch usin' th' `git checkout` command:

```
git checkout -b <add-your-new-branch-name>
```

Fer example:

```
git checkout -b add-luke-oliff
```

(Th' name o' th' branch does nah needs t' 'ave th' word *add* in 't, but 'tis a reasonable thin' t' include 'cause th' purpose o' this branch be t' add yer name t' a list.)

## Make necessary changes 'n commit those changes

Now open `Contributors.md` file in a text editor, add yer name t' it. Don't add it at th' beginnin' or end o' th' file. Put it anywhere in between. Now, save th' file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

If ya go t' th' project directory 'n execute th' command `git status`, ya'll see thar are changes.

Add those changes t' th' branch ya jus' created usin' th' `git add` command:

```
git add Contributors.md
```

Now commit those changes usin' th' `git commit` command:

```
git commit -m "Add <yer-name> t' Contributors list"
```

replacing `<yer-name>` with your name.

## Push changes t' GitHub

Push yer changes usin' th' command `git push`:

```
git push origin <add-yer-branch-name>
```

replacin' `<add-yer-branch-name>` wit' th' name o' th' branch ya created earlier.

## Submit yer changes fer review

If ya go t' yer repository on GitHub, ya'll see a  `Compare & pull request` button.  Click on that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Now submit th' pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Soon I'll be mergin' all yer changes into th' master branch o' this project. Ye will get a notification email once th' changes 'ave been merged.

## Where t' go from here?

Well done! Ye jus' completed th' standard _fork -> clone -> edit -> PR_ workflow that ya'll encounter often as a contributor!

Celebrate yer contribution 'n share it wit' yer hearties 'n followers by goin' t' [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Ye could join our slack crew in case ya needs any help or 'ave any riddles. [Join our slack crew](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Now let's get ya started wit' contributin' t' other projects. We've compiled a list o' projects wit' easy issues ya can get started on. Check out [th' list o' projects in web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Usin' Other Tools

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|
