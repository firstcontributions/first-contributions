[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Git Bash Edition |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |

It's hard. It's always hard the first time you do something. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what comes better than actually doing the stuff without messing up anything. This project aims at providing guidance & simplifying the way rookies make their first contribution. Remember the more relaxed you are the better you learn. If you are looking for making your first contribution just follow the simple steps below. We promise you, it will be fun.

If you don't have Git Bash on your windows machine, [install it](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## Fork this repository

Fork this repo by clicking on the fork button on the top right of this page.
This will create a copy of this repository in your account.

## Clone the repository

Now clone this repo to your machine.

IMPORTANT: DO NOT CLONE THE ORIGINAL REPO. Go to your fork and clone it.

To clone the repo, click on "Code" and then copy the string down below.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

Open the git bash application you just downloaded. It should look like the image down below if its on a windows machine.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />

Go to the folder that you want to save this project on by uisng this command

`cd <folder>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />

Use the string you copied in the step above to clone the repository using this command

`git clone <repo-url>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

Go to the directory where the repo is and open it up on vs code to make your changes.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## Create a branch

Now create a branch by uing this simple command. This command not only creates a branch for you but also lets you switch to that branch.

```
git checkout -b <branch-name>
```

Name your branch `<add-your-name>`. For example, "add-james-smith"

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="create a branch" />

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, scroll to the bottom of the page and add your name to it, then save the file.

Example: If your name is James Smith, It should look like this.

\[James Smith](https://github.com/jamessmith)

You can see that there are changes to Contributors.md by simply running this command

`git status`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="check the status" />

Now commit those changes:

First add the change you made to the staging area by using

`git add file-name`

Then write a commit message by sing this command

`git commit -m "Add your-name to Contributors list"`

Replace `<your-name>` with your name.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit changes" />

To see if your commit has been made you can run a simple `git log --oneline` command.

## Push changes to github

Once you are done with the above steps you can push your changes by using this command

`git push origin <branch-name>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-push.png" alt="push changes" />

## Submit your changes for review

If you go to your repository on github, you'll see `Compare & pull request` button. click on that button.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats! You just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io#social-share).

You can join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Using Other Tools

[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)

# WHY USING BRANCHES DURING CONTRIBUTING

## What are branches.

Branches are simply pointers to a commit.

When you branch out, git is essentially making a new state of your current code, upon which you can work, without affecting the important main state of the code (which is in master branch).

When you are happy with your experiments, and want to merge you experiments in main code, you run git merge
<branch name> master.
This will tell git, to add in all changes from your experiment branch into master.

This way, while working in an open source project with a number of contributors, it becomes easy to merge the best suited code without altering the main code or master branch.

## How it works?

A branch represents an independent line of development. Branches serve as an abstraction for the edit/stage/commit process. You can think of them as a way to request a brand new working directory, staging area, and project history. New commits are recorded in the history for the current branch, which results in a fork in the history of the project.

The git branch command lets you create, list, rename, and delete branches. It doesn’t let you switch between branches or put a forked history back together again. For this reason, git branch is tightly integrated with the git checkout and git merge commands.

## Why to use branches?

If the question "Why do we use branching in version control like git?" still persists in your mind, here's a quick explanation:

Let's take a simple example to understand the branching strategy. A production car needs a paint job before its launch. Prior to its official sale, it was decided that the car would come in 'olive green' color as default. But some of the members in the manufacturing team decided to showcase the car in 'red' color. Hence an ambiguous situation arises and to avoid this problem branching was introduced.The red color paint job is like a branch to the master repository 'Car'. Pushing this branch will suggest the red color. If merged with the master repository the car will get the red color otherwise it will continue with olive green. Merging a contributors branch to the master repo of the organization depends on the project head.

## Example

Alice is working on Feature A and Bob is working on Feature B. Alice is halfway done with Feature A and has made a few commits in alice. However, Feature A is quite hard to implement so Alice decides that she should rather work on Feature C and makes a few commits onto alice. Bob finished Feature B and decides that he would like to tackle Feature A and so pulls alice into bob.

After Bob finishes Feature A he would like to merge bob into master. However, bob now contains Feature A, Feature B and parts of Feature C, but Feature C is not ready to be merged! It's easy to see that a workflow like this can lead to many confusing merge conflicts.

The trick is that instead of having personal branches one should have feature branches. Alice should have a branch for Feature A and Feature C and Bob should have a branch for Feature B and Feature A. That way they both can work on different features without tramping on each other's toes.

## How to create branches?

#### Create a branch

```
git branch AnyBranchName
```

A new branch will be created named AnyBranchName and all the file changes in this branch will not be affected in the main branch.
For detailed explanation refer [How to create branch](https://www.atlassian.com/git/tutorials/using-branches)

#### Delete the branch

```
git branch -d AnyBranchName
```

Branch name AnyBranchName will be deleted from the git repository.
Refer to [Removing branch from your repository](https://github.com/jashnimje/first-contributions/blob/7dcae72208e4b42fcf834b4f189fa8ee78238077/additional-material/git_workflow_scenarios/removing-branch-from-your-repository.md)
