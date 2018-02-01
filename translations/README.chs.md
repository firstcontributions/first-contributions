[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# 第一次参与开源

万事起头难。特别是和其他人合作时，犯错格外令人不舒服。不过，开源的本质就是和其他人合作。我们希望为初学者带来一个简单的方法去学习及参与开源项目。

阅读文章和观看教程会有所帮助。不过，有什麽方法能比，在不会弄乱任何东西的情况下，实际动手做更好？本项目旨在指导初学者及简化初学者参与开源的方式。记住：过程越轻松，学习效益越高。如果你想要做出第一次贡献，只需按照以下简单步骤操作即可。我们答应你，这将很好玩 :)

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

*其他语言版本: [英语](../README.md), [西班牙语](README.es.md), [荷兰语](README.nl.md), [印度语](README.hi.md), [俄语](README.ru.md), [日语](README.ja.md), [越南语](README.vn.md), [波兰语](README.pl.md), [韩语](README.ko.md), [德语](README.de.md), [简体中文](README.chs.md), [繁体中文](README.cht.md), [Greek](README.gr.md).*

如果你的电脑上尚未安装 git, 请按照这个[ 安装指引 ](https://help.github.com/articles/set-up-git/)进行安装。

## Fork（复制）本代码仓库

点击图示中的按钮去 Fork 这个代码仓库。
这个操作会将代码仓库复制到你的账户名下。

## Clone（克隆）代码仓库

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

接下来，将复制後的代码仓库克隆到你的电脑上。点击图示中的绿色按钮，接着点击复制到剪切版按钮（将代码仓库地址复制下来）

随後打开命令行窗口，敲入如下 git 命令：

```
git clone "刚才复制的 url 链接"
```
"刚才复制的 url 链接"（去掉双引号）就是复制到你账户名下的代码仓库地址。获取这链接地址的方法请见上一步。

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

譬如：
```
git clone https://github.com/你的Github用户名/first-contributions.git
```

'你的 Github 用户名' 指的就是你的 Github 用户名。这一步，你将复制到你账户名下的 first-contributions 这个代码仓库克隆到本地电脑上。

## 新建一个分支

下面的命令能在命令行窗口中，把目録切换到 first-contributions 

```
cd first-contributions
```
接下来使用 `git checkout` 命令新建一个代码分支
```
git checkout -b <新分支的名称>
```

譬如：
```
git checkout -b add-myname
```

(新分支的名称不一定需要有* add *。然而，在新分支的名称加入* add *是一件合理的事情，因为这个分支的目的是将你的名字添加到列表中。)

## 对代码进行修改，而後 Commit (提交) 修改

打开 `Contributors.md` 这个文件，更新文件内容，将你的名字加上去，保存修改。`git status` 这命令会列出被改动的文件。接着 `git add` 这命令则可以添加你的改动，就像如下这条命令。
```
git add Contributors.md
```

现在就可以使用 `git commit` 命令 commit 你的修改了。
```
git commit -m "Add <你的名字> to Contributors list"
```
将 `<你的名字>` 替换为你的名字

## 将改动 Push（发布）到 GitHub

使用 `git push` 命令发布代码
```
git push origin <分支的名称>
```
将 `<分支的名称>` 替换为之前新建的分支名称。

## 提出 Pull Request 将你的修改供他人审阅

前往 Github 你的代码仓库，你会看到一个 `Compare & pull request` 的按钮。点击该按钮。

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

接着再点击 `Create pull request` 按钮，正式提交 pull request。

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

不久之後，我便会把你所有的变化合并到这个项目的主分支。更改合并後，你会收到通知电邮。

### [ 更多资料 ](additional-material/additional-material.md)

## 使用其他工具的教程

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|


## 接下来做什麽呢？ 

如果有任何疑问或想获得更多协助，欢迎加入我们的 [Slack](https://firstcontributions.herokuapp.com)！

通过下面这些链接，你能看到当前流行的众多代码仓库中，适合初学者解决的问题列表，还等什麽，去吧 :)

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |

