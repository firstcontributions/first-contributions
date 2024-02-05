[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

# 第一次参与开源项目

万事开头难。特别是和其他人合作时，出错往往会令人不适。不过，开源的本质就是和他人合作。这个项目的初衷就是为初学者提供一个简单的方法去学习以及参与开源项目。

你可以通过阅读文章和观看教程来得到帮助，但上手实操才是最好的学习方式。本项目旨在简化并指导初学者参与他们的第一次开源。记住：过程越轻松，学习效益越高。如果你想要做出第一次贡献，只需按照以下简单步骤操作即可。这将会是一个很有趣的过程 :)

_如果你对 command line（命令行）不熟悉，请参考以下的 [GUI 工具教程](#使用其他工具的教程)。_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### 如果你的电脑上未安装 git, 请参考 [GitHub 文档](https://docs.github.com/cn/get-started/quickstart/set-up-git) 进行安装。

## Fork（复制）本代码仓库

点击图示中的按钮去 Fork 这个代码仓库。
这个操作会将代码仓库复制到你的账户名下。

## Clone（克隆）代码仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

接下来将复制的代码仓库克隆到你的电脑上。点击图示中的绿色按钮，接着点击复制到剪切板按钮（将代码仓库地址复制下来）

随后打开命令行窗口，敲入如下 git 命令：

```
git clone "刚才复制的 url 链接"
```
"刚才复制的 url 链接"（去掉双引号）就是复制到你账户名下的代码仓库地址。获取该链接的方法详见上一步。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

譬如：
```bash
git clone git@github.com:<Github用户名>/first-contributions.git
```

'Github 用户名' 指的是你的 Github 用户名。这一步，这个操作将会克隆你账户名下 first-contributions 这个代码仓库到本地电脑上。

## 新建一个代码分支

在命令行窗口中把目录切换到 first-contributions

```bash
cd first-contributions
```
接下来使用 `git switch` 命令新建一个代码分支
```bash
git switch -c <新分支的名称>
```

譬如：
```bash
git switch -c add-myname
```

(新分支的名称不一定需要有 *add*。然而，在新分支的名称加入 *add* 是一件合理的事情，因为这个分支的目的是将你的名字添加到列表中。)

## 对代码进行修改，然后 Commit (提交) 修改

打开 `Contributors.md` 这个文件，更新文件内容，将你的名字加上去，保存修改。`git status` 这命令会列出被改动的文件。接着 `git add` 这命令则可以添加你的改动，就像如下这条命令。

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

```bash
git add Contributors.md
```

现在就可以使用 `git commit` 命令 commit 你的修改了。
```bash
git commit -m "Add <你的名字> to Contributors list"
```
将 `<你的名字>` 替换成你的名字

## 将改动 Push（推送）到 GitHub

使用 `git push` 命令推送代码
```bash
git push origin <分支的名称>
```
将 `<分支的名称>` 替换为之前新建的分支名称。

<details>
<summary> <strong>如果在 push（发布）过程中出 error（错误），点击这里</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  去 [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) 学习如何生成新的 SSH 密匙以及配置。

</details>

## 提出 Pull Request 将你的修改供他人审阅

前往你的 Github 代码仓库，你会看到一个 `Compare & pull request` 的按钮。点击该按钮。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

接着再点击 `Create pull request` 按钮，正式提交 pull request。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

不久之后，我便会把你所有的变化合并到这个项目的主分支。更改合并后，你会收到一封电子邮件通知。

### [ 更多资料 ](../additional-material/git_workflow_scenarios/additional-material.md)

## 接下来该做什么呢？

为你的第一次贡献庆祝吧，不要忘记和你的朋友以及你的小迷弟小迷妹们分享我们的[网站](https://roshanjossey.github.io/first-contributions/#social-share)哟！

如果有任何疑问或想获得更多协助，欢迎加入我们的 [Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)！

还在等什么，马上加入到其他项目的开发中去吧！为了方便你快速上手，我们收集了当前流行的众多代码仓库中，适合初学者解决的[问题列表](https://firstcontributions.github.io/#project-list)。

### [附加材料](additional-material/git_workflow_scenarios/additional-material.md)

## 使用其他工具的教程

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

<p>项目支持者:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
