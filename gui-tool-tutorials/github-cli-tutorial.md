[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="Github CLI" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width=200> | Github CLI |
| ------------------------------------------------------------ | ---------- |

It's hard. It's always hard, when you do something for the first time. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what comes better than actually doing the stuff without messing up anything. This project aims at providing guidance & simplifying the way rookies make their first contribution. Remember the more relaxed you are, the better you learn. If you are looking for making your first contribution just follow the simple steps below. We promise you, it will be fun.


## Github CLI

To install GitHub CLI on your system, visit the [official website](https://cli.github.com/) to download it directly or use the command-line to install the package into your system.

### Homebrew (MacOS, Linux)

~~~
brew install gh
~~~

### MacPorts (MacOS)

~~~
sudo port install gh
~~~

### Conda (MacOS, Linux, Windows)

~~~
conda install gh --channel conda-forge
~~~

Additional Conda installation options available on the [gh-feedstock page](https://github.com/conda-forge/gh-feedstock#installing-gh).

### Winget (Windows)

~~~
winget install gh
~~~

### Scoop (Windows)

~~~
scoop install gh
~~~

### Chocolatey (Windows)

~~~
choco install gh
~~~

## After installing Github CLI

~~~
gh --version
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590149-39338780-d825-11eb-8293-b730bb3e6c9e.png" alt="Github CLI version" />

## Fork this repository

Fork this repo in command line.

~~~
gh repo fork [repository-owner]/[repository-name]
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590154-3afd4b00-d825-11eb-91b0-99c28d87bfc7.png" alt="Fork repository via Github CLI" />

When you answered yes, begins forking the repository.

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590161-3c2e7800-d825-11eb-8e28-f60ecb6b8be7.png" alt="Fork repository via Github CLI" />

After the repository is forked. You can see the repository in the list.

~~~
gh repo list
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590165-3d5fa500-d825-11eb-98d0-a0d97fa6844c.png" alt="Repository List" />

## Create a branch

From now on, you can just use Git CLI.

Create a new branch.

~~~
git branch [your-new-branch-name]
~~~

Then switch the branch.

~~~
git switch [your-new-branch-name]
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590170-3e90d200-d825-11eb-8c51-12e0f1c0f903.png" alt="Create branch and switch" />

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, scroll to the bottom of the page and add your name to it, then save the file.

Then commit changes.

~~~
git commit -m "[commit-message]"
~~~

<img style="float: right;" src="https://user-images.githubusercontent.com/33862991/123590172-3f296880-d825-11eb-9c06-1d362b1bd5ff.png" alt="Commit changes" />

## Push changes to Github

Now you are ready to push your changes to github. This will be pushing it to your repository forked. 

First, push your commit to repository forked, copy of the project.

~~~
git push --set-upstream origin [your-branch-name]
~~~

![Push changes into repository forked](https://user-images.githubusercontent.com/33862991/123590173-3fc1ff00-d825-11eb-9980-66bb309f2c89.png)

## Submit your changes for review

Finally you can submit review your commit to repository. 

~~~
gh pr create [repository-owner]/[repository-name]
~~~

`-R` or `--repo` is command for target repository.

![Source : Github CLI](https://user-images.githubusercontent.com/33862991/123590175-40f32c00-d825-11eb-92c5-af0e6ba637fd.png)



You can check PR list.

~~~
gh pr list
~~~

![PR List in console](https://user-images.githubusercontent.com/33862991/123590174-405a9580-d825-11eb-8c2a-e607d2aa192f.png)

Check your pr in web browser.

![PR List in web view](https://user-images.githubusercontent.com/33862991/123590177-40f32c00-d825-11eb-81e9-66a2a9d79e3b.png)

If your commit has not problem, It will be merging all your changes into the master branch of this project. And then you will get a notification email once the changes have been merged.

## Where to go from here?

Congrats!  You have just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [our website](https://firstcontributions.github.io/#social-share).

For more advanced command-line instructions from GitHub CLI, visit the [official documentation](https://cli.github.com/manual/) or its [GitHub repository](https://github.com/cli/cli#installation).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Other Tools
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
