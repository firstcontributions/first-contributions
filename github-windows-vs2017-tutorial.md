[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

|<img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Visual_Studio_2017_logo_and_wordmark.svg/2000px-Visual_Studio_2017_logo_and_wordmark.svg.png" width="200">|Visual Studio 2017 Edition|
|---|---|

It's hard. It's always hard the first time you do something. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what comes better than actually doing the stuff without messing up anything. This project aims at providing guidance & simplifying the way rookies make their first contribution. Remember the more relaxed you are the better you learn. If you are looking for making your first contribution just follow the simple steps below. We promise you, it will be fun.

If you don't have Visual Studio 2017 on your machine, [install it](https://www.visualstudio.com/downloads/).

## Fork this repository

<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />

Fork this repository by clicking on the fork button on the top of this page. This will create of copy of this repository in your GitHub account.

GitHub keeps track of the relationship between your repo and the one you forked it from.  You can think of your repo as a working copy.

Most top-level GitHub repos (i.e. ones not forked from any other repo) have a small core team of people who can directly commit changes.  All other contributors must fork the repo and make changes in the fork, then create a Pull Request to ask for their changes to be merged back into the top-level repo. If the top-level repo administrator likes the changes they will be merged and you will gain instant fame and fortune!  More on how to do that later.

## Clone your repository

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

The next step is to clone your repo down to your machine so you can begin making changes. Visual Studio needs the URL of your repo, so click the "clone" button and then click the "copy to clipboard" icon.

**CAREFUL:** One mistake that new contributors often make is to clone the repo you forked *from* rather than cloning your repo.  Check your browser's address bar and make sure you are cloning your repo.

It is now time to jump in to Visual Studio 2017!  You will be working in the Team Explorer tab for most of this tutorial.  If it is not open by default, click `View > Team Explorer` to open it.

<img src="assets/vs2017-01-clone1.png" alt="Team Explorer" />

Team Explorer has many views and there are navigation buttons located at the top to help you find the different areas.  To clone a repo, you need to be on the Connect view, which should be the default.  If you do not see the 'clone' button, click the green plug at the top.

Click the `Clone` option under **Local Git Repositories** and paste the URL to your repo in the text box.  This should be the URL you copied to your clipboard from GitHub previously.

Click the `Clone` button to initiate the process.

<img src="assets/vs2017-02-clone2.png" alt="Clone repo" />

When the process is complete you will be moved over to the Solution Explorer tab where you can see the contents of your repo.  Yours will look different than the screenshot below because things change!

<img src="assets/vs2017-03-clone3.png" alt="Solution Explorer" />

## Create a branch

Click back to the Team Explorer tab and use the main navigation dropdown to open the Branches view.

<img src="assets/vs2017-04-branch1.png" alt="Branches view" />

You should see the **first-contributions** repo and the default branch, which is called `master`.  Right-click on `master` and choose `New Local Branch From...`.

<img src="assets/vs2017-05-branch2.png" alt="New branch" />

Give your branch a name like `add-<your_name_here>`, for example: `add-alonzo-church`.

Leave the `Checkout branch` box checked and click the `Create Branch` button.

<img src="assets/vs2017-06-branch3.png" alt="Create branch" />

You should see your new branch in the list.

<img src="assets/vs2017-07-branch4.png" alt="See new branch" />

## Make necessary changes

Open `Contributors.md` and add your name to the end of the list. This file contains GFM (GitHub Flavored Markdown) which is a proprietary flavor of the <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a> syntax.

Copy one of the other contributors&apos; lines and modify it with your name to make sure you get the syntax right - it can be picky.

<img src="assets/vs2017-08-change1.png" alt="Add your name" />

## Commit & Push changes to GitHub

Switch back to Team Explorer and navigate to the Changes view.

<img src="assets/vs2017-09-commit1.png" alt="Changes" />

Enter the information you want to post with your commit and click `Save`. Visual Studio will remember it for future commits.

<img src="assets/vs2017-10-commit2.png" alt="Git user information" />

**NOTE:** Visual Studio uses a hidden folder called `.vs` to store your personal settings and preferences.  The contents of this folder **should not be saved in Git**.
If it has not been ignored already, you may need to tell Git to ignore this folder so it does not send it up to the repo.

This folder has already been ignored in this repo, so you should not have to perform this step...it is just here for your reference for future projects.

<img src="assets/vs2017-11-commit3.png" alt="Ignore vs folder" />

Now you should see a list of changed files and a textbox to type a commit comment.  Comments should be in brief but thorough.  There is nothing worse than reading through commit comments and seeing this: `"I updated some stuff"`. Take a few seconds to outline your commit.  Your team will thank you later, and you might even thank yourself!

Click `Commit All and Push` to perform a local commit and push your changes back up to your repo, all in one step.

**NOTE:** Commit can be performed separately from Push.  We do both here for convenience. Commit logs your changes locally but they will not be reflected in your GitHub repo until you Push.

<img src="assets/vs2017-12-commit4.png" alt="Commit and Push" />

The first time you Push to GitHub, Visual Studio will ask for your GitHub credentials.  They will be cached so you should not see this very often.

<img src="assets/vs2017-13-commit5.png" alt="Login" />

After the Push operation completes, open your repo in GitHub and you should see a message indicating a recently pushed branch.

You can view your changes by opening the `Branch: master` dropdown and selecting your new branch. Congratulations, you can share the branch URL with the world to show your progress!

<img src="assets/vs2017-14-commit6.png" alt="View pushed branch on GitHub" />

## Submit your changes for review

At this point you have completed your change but it still only resides in your repo.  This step will show you how to submit a request to the administrator of the top-level repo to merge your change.

In your repo on GitHub you'll see the `Compare & pull request` button next to the new branch notification. Click on that button.

<img src="assets/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img src="assets/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats!  You have just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://roshanjossey.github.io/first-contributions/#social-share).

You can join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Other Tools

|<a href="README.md"><img alt="Command Line" src="http://cdn.osxdaily.com/wp-content/uploads/2014/08/terminal-icon-osx-150x150.png" width="100"></a>|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[Command Line](README.md)|[GitHub Desktop](github-desktop-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](sourcetree-macos-tutorial.md)|



## Self-Promotion

If you liked this project, star it on [GitHub](https://github.com/Roshanjossey/first-contributions).
If you're feeling especially charitable, follow [Roshan](https://roshanjossey.github.io/) on
[Twitter](https://twitter.com/sudo__bangbang) and
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>

