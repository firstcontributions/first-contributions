[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

It's hard. It's always hard the first time that you try something new. Especially when collaborating, making mistakes is very uncomfortable. We wanted to simplify the way that new open-source contributors could learn to contribute for the first time.

Reading and watching tutorials helps, but how much better would it be to practice what you are learning by going through the process in the real environment? This project aims to provide guidance and to simplify the way beginners make their first contribution. If you are looking to make your first contribution, follow the steps below.

#### *If you're not comfortable with typing in command line programs, this link will take you to the section below to find [the tutorials that use a Graphic User Interface program]( #tutorials-using-other-tools )*

#### *Read this in [other languages](translations/Translations.md).*

[🇮🇳](translations/README.hi.md)
[🇲🇲](translations/README.mm_unicode.md)
[🇮🇩](translations/README.id.md)
[🇫🇷](translations/README.fr.md)
[🇪🇸](translations/README.es.md)
[<img src="assets/catalan1.png" width="22">](translations/README.ca.md)
[🇳🇱](translations/README.nl.md)
[🇱🇹](translations/README.lt.md)
[🇷🇺](translations/README.ru.md)
[:slovakia:](translations/README.slk.md)
[🇯🇵](translations/README.ja.md)
[🇻🇳](translations/README.vn.md)
[🇵🇱](translations/README.pl.md)
[🇮🇷](translations/README.fa.md)
[🇮🇷](translations/README.fa.en.md)
[🇰🇷 🇰🇵](translations/README.ko.md)
[🇩🇪](translations/README.de.md)
[🇩🇰](translations/README.da.md)
[🇨🇳](translations/README.chs.md)
[🇹🇼](translations/README.cht.md)
[🇬🇷](translations/README.gr.md)
[🇪🇬](translations/README.eg.md)
[🇸🇦](translations/README.ar.md)
[🇺🇦](translations/README.ua.md)
[🇧🇷](translations/README.pt_br.md)
[🇵🇹](translations/README.pt-pt.md)
[🇮🇹](translations/README.it.md)
[🇹🇭](translations/README.th.md)
[🏴](translations/README.gl.md)
[🇵🇰](translations/README.ur.md)
[:bangladesh:](translations/README.bn.md)
[🇲🇩 🇷🇴](translations/README.ro.md)
[🇹🇷](translations/README.tr.md)
[🇸🇪](translations/README.se.md)
[:slovenia:](translations/README.sl.md)
[🇮🇱](translations/README.hb.md)
[🇨🇿](translations/README.cs.md)
[<img src="assets/pirate.png" width="22">](translations/README.en-pirate.md)
[🇲🇽](translations/README.mx.md)



<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />

If you don't have git on your machine, [install it]( https://help.github.com/articles/set-up-git/).

## Fork this repository

Fork this repo by clicking on the fork button on the top of this page.
This will create a copy of this repository and open it in your account.

## Clone the repository

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

Now clone the forked repo to your machine. From your GitHub account, open the forked repo and click on the *Clone or Download* button, and then click the *Copy to Clipboard* icon.

Open a terminal program such as Git CMD and enter the following text, using the freshly copied url:
```
git clone url_you_just_copied
```
where `url_you_just_copied` is the url to your forked version of this repository. See the previous steps to obtain the url.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:
```
git clone https://github.com/this_is_you/first-contributions.git
```
The copied url will contain your GitHub username at `this_is_you`. This step copies the contents of your forked repository `first-contributions` to your computer. For PC, this will likely make a folder in the `C:\Users\your_computer_user_name folder` 

## Create a branch

Enter into the local copy of the repository through the command line by typing and entering:
```
cd first-contributions
```

With a PC, it will look like:
```
C:\Users\your_computer_user_name\first-contributions>
```

Create a branch (-b) and name it by typing and entering:
```
git checkout -b add-your-new-branch-name
```

Replace add-your-new-branch-name with a good title for what you are doing with that branch. For example, we want to add the name Alonzo Church, so we will call it:
```
git checkout -b add-alonzo-church
```
The name of the branch does not need the word *add* in it, but since this tutorial's end result is to add your name to a list, it makes sense to name it so.

## Make necessary changes and commit those changes

Navigate to your local repository. For PC, you will likely find it here: `C:\Users\your_computer_user_name\first-contributions`. Use a text editor to open the file called `Contributors.md`. Add your name to it. Put your name in a similar format anywhere inbetween the beginning and the end, but not *at* the beginning *or* end of the file. 
Save the file.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />


Go back to your terminal program and type in:

```
git status
```
Notice the changes shown in red text.

To add the changes to the branch you just created, type and enter:

```
git add Contributors.md
```

We are specifically adding only the Contributors.md file here. If you had multiple files you can use the shortcut of `git add .` 

Like a good programmer, when you commit changes, you add the reason for the changes. So we will commit with a message (-m):
```
git commit -m "Add your_name to Contributors list"
```
replacing `your_name` with your actual name.

## Push changes to GitHub

Remember before, when you created a branch? Copy the name of the branch into your clipboard so we can use it in the next step. To push your changes to your copy of the online repository, use `git push` and paste in your branch name like follows:
```
git push origin add-your-branch-name
```
Make sure that `add-your-branch-name` is the name of the branch you created earlier.

## Submit your changes for review

Go to your repository on GitHub and now you will see an alert bar with a  `Compare & pull request` button. Click the button.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Normally you would add description in the "Write" section, explaining what you did, but for this project you can leave it blank. Click the green button to `Create pull request`.

<img style="float: right;" src="assets/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging any of your changes into the master branch of this project. You will get a notification email once the changes have been merged. I'd love to hear your thoughts on the process! 

## Where to go from here?

Congrats!  You just completed the standard _fork -> clone -> edit -> Pull Request_ workflow that you'll encounter often as a contributor! If you liked this project, give it a star so other new contributors can find it easier. 

Celebrate your contribution and share it with your friends and followers by going to our [web app](https://roshanjossey.github.io/first-contributions/#social-share).

If you need any help or have any questions, you could join our slack team: [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Graphic User Interface (GUI) Tools

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Self-Promotion

If you liked this project, star it on [GitHub](https://github.com/Roshanjossey/first-contributions).
If you're feeling especially charitable, follow [Roshan](https://roshanjossey.github.io/) on
[Twitter](https://twitter.com/sudo__bangbang) and
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
