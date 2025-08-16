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

## 📚 Table of Contents

- [Logging into GitHub via Git Bash](#logging-into-github-via-git-bash)
- [Managing Multiple GitHub Users](#managing-multiple-github-users-on-git-bash)
- [Fork this Repository](#fork-this-repository)
- [Clone the Repository](#clone-the-repository)
- [Create a Branch](#create-a-branch)
- [Make Changes & Commit](#make-necessary-changes-and-commit-those-changes)
- [Push Changes](#push-changes-to-github)
- [Submit a Pull Request](#submit-your-changes-for-review)
- [Where to Go Next](#where-to-go-from-here)

## Logging into GitHub via Git Bash

Before making your contribution, ensure you're logged in to GitHub on your terminal.

*Check your Git configuration:*
```bash
git config --global user.name
git config user.email
```
*Set your username and email (if not set)*
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Managing Multiple GitHub Users on Git Bash
If you're switching between multiple GitHub accounts (e.g., personal and work), Git Bash might use the wrong credentials.

Follow these steps to switch accounts:
### Remove Existing GitHub Credentials
Git on Windows saves login details via the Windows Credential Manager.

1. Open the Start Menu → search for Credential Manager

2. Go to Windows Credentials

3. Look for an entry like:

    git:https://github.com
5. Click Remove
### Clear Git Credential Helper (Optional)
In Git Bash:
```
git config --global --unset credential.helper
```
This prevents Git from auto-using the old credentials
### Set New GitHub Username and Email
```
git config --global user.name "YourNewUsername"
git config --global user.email "yournewemail@example.com"
```

> 💡 Tip: Use `--global` to apply a setting globally, or omit it to apply only to the current repository.

### Push to Trigger New Login
Make any commit, then push to GitHub:
```
git push origin main
```
You'll be prompted to enter:

* Your GitHub username

* A Personal Access Token (instead of a password)

Generate a token here: github.com/settings/tokens

## Fork this repository

Fork this repo by clicking on the fork button on the top right of this page.
This will create a copy of this repository in your account.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## Clone the repository

Now clone this repo to your machine.

IMPORTANT: DO NOT CLONE THE ORIGINAL REPO. Go to your fork and clone it.

To clone the repo, click on "Code" and then copy the string down below.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

Open the git bash application you just downloaded. It should look like the image down below if it's on a windows machine.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />

Go to the folder that you want to save this project on by using this command

```bash
cd <folder>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />

Use the string you copied in the step above to clone the repository using this command

```bash
git clone <repo-url>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

Navigate to the cloned repository folder and open it in VS Code or any text editor.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## Create a branch

Now create a branch by using this simple command. This command not only creates a branch for you but also lets you switch to that branch.

```bash
git checkout -b <branch-name>
```

Name your branch `<add-your-name>`. For example, "add-james-smith"

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="create a branch" />

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, scroll to the bottom of the page and add your name to it, then save the file.

Example: If your name is James Smith, It should look like this.

[James Smith](https://github.com/jamessmith)

You can see that there are changes to Contributors.md by simply running this command

```bash
git status
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="check the status" />

Now commit those changes:

First add the change you made to the staging area by using

```bash
git add file-name
```

Then write a commit message by using this command

```bash
git commit -m "Add your-name to the Contributors list"
```

Replace `<your-name>` with your name.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit changes" />

To see if your commit has been made you can run a simple `git log --oneline` command.

## Push changes to Github

Once you are done with the above steps you can push your changes by using this command

```bash
git push origin <branch-name>
```

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
