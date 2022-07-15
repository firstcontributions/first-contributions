[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)

# 第一次参与开源

万事开头难。尤其是和其他人合作时，犯错总是格外令人不舒服。不过，开源的本质就是和其他人合作。这个项目就是希望为初学者带来一个简单的方法去学习及参与开源项目。

你可以选择阅读文章和观看教程来得到帮助，但实际动手才是最好的学习方式。本项目旨在简化并指导初学者参与他们的第一次开源。记住：过程越轻松，学习效益越高。如果你想要做出第一次贡献，只需按照以下简单步骤操作即可。这将很好玩 :)

*如果你不喜欢使用命令行工具，[这里有使用图形化工具的教程]( #使用其他工具的教程)。*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

如果你的电脑上尚未安装 git ，请按照 [安装指引（英文）](https://help.github.com/articles/set-up-git/) 进行安装。

## Fork（复制）本代码仓库

点击图示中的按钮去 Fork 这个代码仓库。
这个操作会将代码仓库复制到你的账户名下。

## Clone（克隆）代码仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

接下来将复制后的代码仓库克隆到你的电脑上。点击图示中的绿色按钮，接着点击复制到剪切板按钮（将代码仓库地址复制下来）。

随后打开命令行窗口，敲入如下 git 命令：

```
git clone "刚才复制的 url 链接"
```
"刚才复制的 url 链接"（去掉双引号）就是复制到你账户名下的代码仓库地址。获取这链接地址的方法请见上一步。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

譬如：
```
git clone https://github.com/你的Github用户名/first-contributions.git
```

'你的 Github 用户名' 指的就是你的 Github 用户名。这一步，你将复制到你账户名下的 first-contributions 这个代码仓库克隆到本地电脑上。

## 新建一个代码分支

下面的命令能在命令行窗口中，把目录切换到 first-contributions 。

```
cd first-contributions
```

接下来使用 `git checkout` 命令新建一个代码分支：
```
git checkout -b <新分支的名称>
```

譬如：
```
git checkout -b add-myname
```

(新分支的名称不一定需要有 *add*。然而，在新分支的名称加入 *add* 是一件合理的事情，因为这个分支的目的是将你的名字添加到列表中。)

## 对代码进行修改，而后 Commit (提交) 修改

打开 `Contributors.md` 这个文件，更新文件内容，将你的名字加上去，保存修改。`git status` 这命令会列出被改动的文件。接着 `git add` 这命令则可以添加你的改动，就像如下这条命令。

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

```
git add Contributors.md
```

现在就可以使用 `git commit` 命令提交你的修改了。
```
git commit -m "Add <你的名字> to Contributors list"
```
将 `<你的名字>` 替换成你的名字

## 将改动 Push（发布）到 GitHub

使用 `git push` 命令发布代码
```
git push origin <分支的名称>
```
将 `<分支的名称>` 替换为之前新建的分支名称。

## 提出 Pull Request 将你的修改供他人审阅

前往 Github 你的代码仓库，你会看到一个 `Compare & pull request` 的按钮。点击该按钮。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

接着再点击 `Create pull request` 按钮，正式提交 pull request。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

不久之后，我便会把你所有的变化合并到这个项目的主分支。更改合并后，你会收到电子邮件通知。

### [ 更多资料 ](../additional-material/git_workflow_scenarios/additional-material.md)

## 接下来做什么呢？

为你第一次的贡献庆祝吧，不要忘记和你的朋友以及迷弟迷妹们分享我们的[网站](https://roshanjossey.github.io/first-contributions/#social-share)哟！

如果有任何疑问或想获得更多协助，欢迎加入我们的 [Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)！

还等什么，马上加入到其他项目的开发中去吧。为了方便你快速上手，我们收集了当前流行的众多代码仓库中，适合初学者解决的[问题列表](https://roshanjossey.github.io/first-contributions/#project-list)。

## 使用其他工具的教程

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)

