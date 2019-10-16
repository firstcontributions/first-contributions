[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)

# 第一次参与开源

万事起头难。特别是和其他人合作时，犯错格外令人不舒服。不过，开源的本质就是和其他人合作。我们希望为初学者带来一个简单的方法去学习及参与开源项目。

阅读文章和观看教程会有所帮助。不过，有什么方法能比实际动手做更好？本项目旨在指导初学者及简化初学者参与开源的方式。记住：过程越轻松，学习效益越高。如果你想要做出第一次贡献，只需按照以下简单步骤操作即可。我们答应你，这将很好玩 :)

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

如果你的电脑上尚未安装 git, 请按照这个[ 安装指引 ](https://help.github.com/articles/set-up-git/)进行安装。

## Fork（复制）本代码仓库

点击图示中的按钮去 Fork 这个代码仓库。
这个操作会将代码仓库复制到你的账户名下。

## Clone（克隆）代码仓库

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

接下来，将复制后的代码仓库克隆到你的电脑上。点击图示中的绿色按钮，接着点击复制到剪切板按钮（将代码仓库地址复制下来）

随后打开命令行窗口，敲入如下 git 命令：

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

下面的命令能在命令行窗口中，把目录切换到 first-contributions

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

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

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

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

不久之后，我便会把你所有的变化合并到这个项目的主分支。更改合并后，你会收到电子邮件通知。

### [ 更多资料 ](../additional-material/git_workflow_scenarios/additional-material.md)

## 接下来做什么呢？

为你第一次的贡献庆祝吧，不要忘记和你的朋友以及迷弟迷妹们分享我们的[网站](https://roshanjossey.github.io/first-contributions/#social-share)哟！

如果有任何疑问或想获得更多协助，欢迎加入我们的 [Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)！

还等什么，马上加入到其他项目的开发中去吧。为了方便你快速上手，我们收集了当前流行的众多代码仓库中，适合初学者解决的[问题列表](https://roshanjossey.github.io/first-contributions/#project-list)。

## 使用其他工具的教程

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>
|---|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|[Visual Studio Code](../github-windows-vs-code-tutorial.md)|

