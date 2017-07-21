[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# First Contributions

It's hard. It's always hard the first time you do something. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what's better than actually doing the stuff without messing up anything? This project aims at providing guidance & simplifying the way rookies make their first contribution. Remember: the more relaxed you are, the better you learn. If you are looking to make your first contribution, just follow the simple steps below. We promise you, it will be fun.

<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />

*Read this in other languages: [Indonesian](translations/README.id.md), [Spanish](translations/README.es.md), [Dutch](translations/README.nl.md), [Hindi](translations/README.hi.md), [Russian](translations/README.ru.md), [Japanese](translations/README.ja.md), [Vietnamese](translations/README.vn.md), [Polish](translations/README.pl.md), [Korean](translations/README.ko.md), [German](translations/README.de.md), [Simplified Chinese](translations/README.chs.md), [Traditional Chinese](translations/README.cht.md), [Greek](translations/README.gr.md), [العربية](translations/README.ar.md), [Ukrainian](translations/README.ua.md) and [Português/Brasil](translations/README.pt_br.md).*

If you don't have git on your machine, [ install it ]( https://help.github.com/articles/set-up-git/ ).

## Fork this repository

Fork this repo by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

## Clone the repository

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

Now clone this repo to your machine. Click on the clone button and then click the *copy to clipboard* icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```
where "url you just copied" (without the quote marks) is the url to this repository. See the previous steps to obtain the url.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:
```
git clone https://github.com/this-is-you/first-contributions.git
```
where `this-is-you` is your GitHub username. Here you're copying the contents of the first-contributions repository in GitHub to your computer.

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd first-contributions
```
Now create a branch using the `git checkout` command:
```
git checkout -b <add-your-name>
```

For example:
```
git checkout -b add-alonzo-church
```
(The name of the branch does not need to have the word *add* in it, but it's a reasonable thing to include because the purpose of this branch is to add your name to a list.)

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, add your name to it, and then save the file. If you go to the project directory and execute the command `git status`, you'll see there are changes. Add those changes to the branch you just created using the `git add` command:
```
git add Contributors.md
```

Now commit those changes using the `git commit` command:
```
git commit -m "Add <your-name> to Contributors list"
```
replacing `<your-name>` with your name.

## Push changes to GitHub

Push your changes using the command `git push`:
```
git push origin <add-your-name>
```
replacing `<add-your-name>` with the name of the branch you created earlier.

## Submit your changes for review

If you go to your repository on GitHub, you'll see a  `Compare & pull request` button.  Click on that button.

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="assets/submit-pull.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

The master branch of your fork won't have the changes. In order to keep your fork synchronized with mine, follow the steps below.

## Keeping your fork synced with this repository

 First, switch to the master branch.
 ```
 git checkout master
 ```

 Then add my repo's url as `upstream remote url`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
This is a way of telling git that another version of this project exists in the specified url and we're calling it `upstream`. Once the changes are merged, fetch the new version of my repository:
```
git fetch upstream
```

Here we're fetching all the changes in my fork (upstream remote). Now, you need to merge the new revision of my repository into your master branch.
```
git rebase upstream/master
```
Here you're applying all the changes you fetched to master branch. If you push the master branch now, your fork will also have the changes:
```
git push origin master
```
Notice here you're pushing to the remote named origin.

At this point I have merged your branch `<add-your-name>` into my master branch, and you have merged my master branch into your own master branch.  Your branch is now no longer needed, so you may delete it:
```
git branch -d <add-your-name>
```
and you can delete the version of it in the remote repository, too:
```
git push origin --delete <add-your-name>
```
This isn't necessary, but the name of this branch shows its rather special purpose.  Its life can be made correspondingly short.

## Tutorials Using Other Tools


|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|

## Where to go from here?

You could also join our slack team in case you need any help or have any questions. [Join slack team](https://firstcontributions.herokuapp.com)

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
