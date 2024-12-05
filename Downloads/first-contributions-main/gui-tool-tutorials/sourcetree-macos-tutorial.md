[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

|<img alt="SourceTree" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-logo.png" width="200">|Atlassian Sourcetree|
|---|---|

It's hard. It's always hard, when you do something for the first time. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what comes better than actually doing the stuff without messing up anything. This project aims at providing guidance & simplifying the way rookies make their first contribution. Remember the more relaxed you are, the better you learn. If you are looking for making your first contribution just follow the simple steps below. We promise you, it will be fun.


## Sourcetree

Please note, this tutorial is for MacOS. It is similar to Sourcetree on Windows but some things may look different.
<!--
	****************************************
	*** This is commented out until      ***
	*** a Windows tutorial can be created***
	****************************************
Please note, this tutorial is for MacOS. Please refer to the [Windows Tutorial]() for Sourcetree if that is what you want to use.
-->

Download [Sourcetree](https://www.sourcetreeapp.com), Install and open it.

You should see the "Sourcetree" modal dialog.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-1-main.png" alt="SourceTree Main" />

From here, you want to click on Remote. If this is the first installation, then you likely haven't connected your GitHub account yet. Do so by clicking the "Connect Button".

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-2-main-connect.png" alt="SourceTree Connect" />

The *Accounts* dialog will appear. Click "Add" in the lower left hand corner. Then select the appropriate settings to add GitHub (or any other account you want) to the client. After you selected your settings for GitHub, click "Connect Account."

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-4-accounts-add.png" alt="SourceTree Connect Add" />

This will open a page in your web browser. Follow the steps given to authorize your account.

## Fork this repository

Fork this repo by clicking on the fork button on the top of this page.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/fork.png" alt="fork this repository" />
This will create of copy of this repository in your account.


## Clone the repository

In Sourcetree, Click on the "Remote" button. This should load all of your GitHub repos which are listed on GitHub.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-5-cloning.png" alt="clone this repository" />

Once you click the "Clone" button, you will be presented with another view to define several different things.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-6-cloning-confirm.png" alt="clone this repository" />

1) **Source URL:** This is automatically filled and you don't need to change it. It is the URL from where your GitHub project resides.

2) **Destination Path:** This is the physical location on your computer where this project will be saved

3) **Name:** This is a "Bookmark" to how Sourcetree will reference your project. Think of it like a shortcut.

*Note: Normally the defaults in these fields are fine.*

**Once you are satisfied, click "Clone"**

This will bring up the main repo browser for your repository!

## Create a branch

Click the branch button on the toolbar.

Name your branch "add-your-name-to-contribution", for example: "add-sally-to-contribution".

To do this, click **Branch (1)** which launches the naming dialog. Then **Add your name (2)** as just described. Finally click **Create Branch**. This will create the branch for what you just named.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-7-branching.png" alt="name your branch" />


## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor and add your name to it, with your Github URL link, then save the file.

You should be able to see and review the file that have been changed and decide what you would like to stage.  Staging is important to tell git exactly what file changes you want associated with this commit.

*Note: If you do not see the file's diff, click **Uncommitted Files** at the top of your dialog*

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-8-viewing-changed-files.png" alt="edit some file(s)" />

Next click the **Commit** button on the top left of the dialog. This will show you your staging area.

Click the *Checkbox* to **add** the file to the staging area. Then enter a commit message.

*Note: You can also select files (both in the staging and unstaged areas) and add/remove files from the respective areas by using the spacebar*

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-9-committing.png" alt="stage your changes" />


Once you have added your changes and added a commit message, you can press the **Commit** button to finally make the commit.

Congratulations, you've committed all the changes to your local copy of your branch of your fork of first-contributions.  Onward!


## Push changes to GitHub

Now you are ready to push your changes to github. This will be pushing it to your own, forked, copy of the project. Follow the steps to push your branch up. First, click **Push (1)**, this will show the remote/push dialog. **Click (2)** the checkbox of your branch you want to push. Select **OK (3)** and this will push your commit up to Github.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/sourcetree-10-pushing.png" alt="origin or branch" />

## Submit your changes for review

If you go to your repository on github, you'll see  `Compare & pull request` button. Click on that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/sourcetree-macos-tutorial/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats!  You have just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io/#social-share).

You could join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).


### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Other Tools
[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
