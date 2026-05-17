[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="Xcode" src="https://developer.apple.com/assets/elements/icons/xcode/xcode-96x96_2x.png" width="100"> | Xcode Edition |
| --------------------------------------------------------------------------------------------------------------- | ------------- |

It's hard. It's always hard the first time you do something. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what comes better than actually doing the stuff without messing up anything. This project aims at providing guidance & simplifying the way rookies make their first contribution. Remember the more relaxed you are the better you learn. If you are looking for making your first contribution just follow the simple steps below. We promise you, it will be fun.

If you don't have Xcode on your machine, [install it from the Mac App Store](https://apps.apple.com/us/app/xcode/id497799835).

> **Note:** Xcode is available on macOS only. If you are on another platform, check out [tutorials using other tools](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools).

## Fork this repository

Fork this repo by clicking on the **Fork** button on the top right of this page on GitHub.
This will create a copy of this repository in your account.

## Clone the repository

Now clone this repo to your machine using Xcode.

IMPORTANT: DO NOT CLONE THE ORIGINAL REPO. Go to your fork and clone it.

On your fork's GitHub page, click the **Code** button and copy the HTTPS URL.

Open Xcode and from the menu bar choose **Source Control > Clone...**

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-clone-menu.png" alt="Source Control Clone menu" />

Paste the URL of your fork into the search/URL field at the top of the Clone dialog and press **Enter** (or **Return**).

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-clone-dialog.png" alt="Clone dialog with URL" />

Choose a local folder to save the repository and click **Clone**.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-clone-location.png" alt="Choose clone location" />

Xcode will clone the repository and open it. Because this is a Markdown project (not an Xcode project), Xcode opens it as a folder. You can navigate files in the Project navigator on the left.

## Create a branch

From the menu bar, choose **Source Control > New Branch...**

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-new-branch-menu.png" alt="New Branch menu item" />

In the dialog that appears, name your branch `add-your-name`. For example, `add-jane-smith`.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-new-branch-name.png" alt="Name the new branch" />

Click **Create** to create and switch to the new branch.

## Make necessary changes and commit those changes

Open `Contributors.md` from the Project navigator. Scroll to the bottom of the file and add your name using the following format:

```
- [Your Name](https://github.com/your-username)
```

For example, if your name is Jane Smith your entry should look like:

```
- [Jane Smith](https://github.com/janesmith)
```

Save the file with **Command + S**.

Now commit your changes. From the menu bar choose **Source Control > Commit...**

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-commit-menu.png" alt="Source Control Commit menu" />

The commit dialog will show your changed file (`Contributors.md`) with a checkmark. Make sure it is checked.

In the commit message field at the bottom, type:

```
Add <your-name> to Contributors list
```

Replace `<your-name>` with your actual name.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-commit-dialog.png" alt="Commit dialog with message" />

Click **Commit 1 File** to create the commit.

## Push changes to GitHub

From the menu bar choose **Source Control > Push...**

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-push-menu.png" alt="Source Control Push menu" />

In the dialog that appears, confirm your branch (`add-your-name`) is selected and click **Push**.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/xcode-tutorial/xcode-push-dialog.png" alt="Push dialog" />

If prompted, sign in with your GitHub credentials.

## Submit your changes for review

Go to your fork on GitHub in your browser. You'll see a **Compare & pull request** button — click it.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

Fill in a title and description for your pull request and click **Create pull request**.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

Soon a maintainer will merge your changes into the main branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats! You just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io#social-share).

### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Using Other Tools

[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
