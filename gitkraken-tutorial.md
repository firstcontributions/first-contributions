[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# First Contributions

|<img alt="GitKraken" src="/assets/gk-icon.png" width="200">|GitKraken Edition|
|---|---|

It's hard. It's always hard the first time you do something. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what comes better than actually doing the stuff without messing up anything. This project aims at providing guidance & simplifying the way rookies make their first contribution. Remember the more relaxed you are the better you learn. If you are looking for making your first contribution just follow the simple steps below. We promise you, it will be fun.


## Git Kraken

Download [GitKraken](https://www.gitkraken.com), install and open it.


You should see the "Welcome to GitKraken" modal dialog - Sign in with GitHub and allow GitKraken access to your GitHub account.


<img style="float: right;" src="assets/gk-login.png" alt="login to GitHub" />

(optional) Go to File->Preferences and set your project directory to the root of your local repositories.


## Fork this repository

Fork this repo by clicking on the fork button on the top of this page.
<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />
This will create of copy of this repository in your account.


## Clone the repository

In GitKraken, go to File->Clone Repo.


<img style="float: right;" src="assets/gk-clone.png" alt="clone this repository" />


Select GitHub.com in the right pane.  Under your username, you should see first-contributions.  Click that repository and check the full path shown at the bottom of this pane.  

Once you're satisfied with the path, click "Clone the repo!".


## Create a branch

Click the branch button on the toolbar.

Name your branch add-your-name, for example: "add-william-sutton"

<img style="float: right;" src="assets/gk-branch.png" alt="name your branch" />


## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor and add your name to it, then save the file. 

If you have the repo open in GitKraken you'll see there are changes. Review and stage those changes by selecting the newest commit marked with "// WIP" and the number of files changed and the type of change.

<img style="float: right;" src="assets/gk-edit.png" alt="edit some file(s)" />

Review the files that have been changed and decide what you would like to stage.  Staging is important to tell git exactly what file changes you want associated with this commit.


<img style="float: right;" src="assets/gk-stage.png" alt="stage your changes" />


Once you have a good commit message ("Add <your-name> to Contributors list" sounds nice and descriptive) and are happy with your changes, you can hit "Stage all changes" to stage everything that's modified or "Stage File" to stage an individual file.


<img style="float: right;" src="assets/gk-commit.png" alt="clone this repository" />


If you change your mind, you can unstage those changes, or you can discard them all together.  WARNING: As the word discard implies, this is a destructive operation.  Only do this if you don't want any change from whatever repository you're in.

Hit commit.

Congratulations, you've commited changes to your local copy of your branch of your fork of first-contributions.  Onward!


## Push changes to GitHub

<img style="float: right;" src="assets/gk-push.png" alt="push your changes" />

Click the Push button on the toolbar.


## Submit your changes for review

If you go to your repository on github, you'll see  `Compare & pull request` button. click on that button.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="assets/submit-pull.png" alt="submit pull request" />

Now I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

Master branch of your fork won't have those changes. In order to keep your fork synced with mine, follow the steps below.

## Keeping your fork synced with this repository

 First, switch to master branch.
 
<img style="float: right;" src="assets/gk-checkoutsuccessful.png" alt="checkout success" />

 Double click on master on the left under origin.
 

 Then, add my repo's url as `upstream remote url`.
 
 
 
<img style="float: right;" src="assets/gk-clickaddremote.png" alt="click add remote" />

 Click on the '+' that reveals itself after you hover Remote on the left.
 
 
 
 
<img style="float: right;" src="assets/gk-addremote.png" alt="add remote dialog" />
 Select Roshanjossey/first-contributions and name the remote upstream.
 
 Click Add Remote.

 
 This is a way of telling git that another version of this project exists in the specified url and we're calling it upstream. Once the changes are merged, fetch the new version of my repository.

 
 Double click the master branch under upstream on the left.

 
<img style="float: right;" src="assets/gk-checkoutsuccessful.png" alt="checkout success" />
 

 
 
Here we're fetching all the changes in my fork (upstream remote). Now, you need to merge the new revision of my repository into your master branch.

Drag your master branch (marked by your profile picture) on top of the upstream's master.

<img style="float: right;" src="assets/gk-rebase.png" alt="rebasing to master" />

Here you're applying all the changes you fetched to master branch. If you push master branch now, your fork will also have the changes

Click push again, and this time make sure to select origin/master at the top

Notice here you're pushing to the remote named origin.


## Tutorials Using Other Tools

|<a href="README.md"><img alt="Command Line" src="http://cdn.osxdaily.com/wp-content/uploads/2014/08/terminal-icon-osx-150x150.png" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|
|---|---|---|
|[Command Line](README.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitHub Desktop](github-desktop-tutorial.md)|

## Where to go from here?

Here's some beginner level issues in popular repos that you can solve. Go ahead and go to those repos to learn more

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
