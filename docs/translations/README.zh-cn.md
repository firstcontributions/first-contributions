[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# 第一次参与开源项目

万事开头难。特别是和其他人合作时，出错往往会令人不适。不过，开源的本质就是和他人合作。这个项目的初衷就是为初学者提供一个简单的方法去学习以及参与开源项目。

你可以通过阅读文章和观看教程来得到帮助，但上手实操才是最好的学习方式。本项目旨在简化并指导初学者参与他们的第一次开源。记住：过程越轻松，学习效益越高。如果你想要做出第一次贡献，只需按照以下简单步骤操作即可。这将会是一个很有趣的过程 :)

_如果你对 command line（命令行）不熟悉，请参考以下的 [GUI 工具教程](#使用其他工具的教程)。_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="复制此仓库代码" />

#### 如果你的电脑上未安装 Git，请参考 [GitHub 文档](https://docs.github.com/cn/get-started/quickstart/set-up-git) 进行安装。

## Fork（复制）本代码仓库

点击图示中的按钮去 Fork 这个代码仓库。
这个操作会将代码仓库复制到你的账户名下。

## Clone（克隆）代码仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="克隆此仓库代码" />

接下来将复制的代码仓库克隆到你的电脑上。在你的 GitHub 账户中打开复制的代码仓库，点击 Code 按钮，然后点击 SSH 标签页，接着点击 _复制到剪贴板_ 图标。

随后打开命令行窗口，敲入如下 Git 命令：

```bash
git clone "刚才复制的 URL 链接"
```
"刚才复制的 URL 链接"（去掉双引号）就是复制到你账户名下的代码仓库地址。获取该链接的方法详见上一步。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="将 URL 链接复制到剪贴板" />

譬如：
```bash
git clone git@github.com:<GitHub用户名>/first-contributions.git
```

'GitHub 用户名' 指的是你的 GitHub 用户名。这一步，这个操作将会克隆你账户名下 first-contributions 这个代码仓库到本地电脑上。

## 新建一个代码分支

在命令行窗口中把目录切换到 first-contributions。

```bash
cd first-contributions
```
接下来使用 `git switch` 命令新建一个代码分支：
```bash
git switch -c <新分支的名称>
```

譬如：
```bash
git switch -c add-myname
```

<details>
<summary> <strong>如果在运行 git switch 时报错，请点击这里：</strong> </summary>

如果出现错误信息 “Git: `switch` is not a git command. See `git --help`”（即提示 switch 不是 git 命令），可能是因为你使用的是旧版本的 Git。

在这种情况下，请尝试改用 `git checkout` 命令：

```bash
git checkout -b <新分支的名称>
```

</details>

(新分支的名称不一定需要有 *add*。然而，在新分支的名称加入 *add* 是一件合理的事情，因为这个分支的目的是将你的名字添加到列表中。)

## 对代码进行修改并提交修改

现在，在文本编辑器中打开 `Contributors.md` 文件，将你的名字添加到文件中。不要把名字加在文件的开头或结尾，请加在它们之间的任意位置。然后保存文件。

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="修改`Contributors.md`后的git状态" />

如果在项目目录下运行 `git status` 命令，你会看到有文件被修改了。

使用 `git add` 命令，将这些修改添加到刚才创建的分支中：

```bash
git add Contributors.md
```

现在就可以使用 `git commit` 命令提交你的修改了：
```bash
git commit -m "Add <你的名字> to Contributors list"
```
将 `<你的名字>` 替换成你的名字。

## 将改动 Push（推送）到 GitHub

使用 `git push` 命令推送代码：
```bash
git push -u origin <新分支的名称>
```
将 `<新分支的名称>` 替换为之前新建的分支名称。

<details>
<summary> <strong>如果在推送（push）过程中出现错误（error），点击这里：</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  去 [GitHub 教程](https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) 学习如何生成新的 SSH 密钥并进行配置。

  另外，你可能需要运行 `git remote -v` 来检查你的远程仓库地址。
  
  如果它看起来像这样：
  <pre>origin	https://github.com/your-username/first-contributions.git (fetch)
  origin	https://github.com/your-username/first-contributions.git (push)</pre>
  
  请使用以下命令进行修改：
  ```bash
  git remote set-url origin git@github.com:your-username/first-contributions.git
  ```
  否则你仍会被要求输入用户名和密码，从而导致认证错误。
</details>

## 提出 Pull Request 将你的修改供他人审阅

前往你的 GitHub 代码仓库，你会看到一个 `Compare & pull request` 的按钮。点击该按钮。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="创建 pull request" />

接着再点击 `Create pull request` 按钮，正式提交 pull request。

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="提交 pull request" />

我们就会把你所有的修改合并到这个项目的 main 分支。更改合并后，你会收到一封电子邮件通知。

## 接下来该做什么呢？

祝贺！你刚刚完成了作为贡献者经常会使用到的标准流程：_fork -> clone -> edit -> pull request_ ！

为你的第一次贡献庆祝吧，不要忘记和你的朋友以及你的关注者分享我们的 [Web 应用](https://firstcontributions.github.io/#social-share) 哟！

如果你想进行更多练习，请查看 [code contributions](https://github.com/roshanjossey/code-contributions)。

接下来，让我们带你开始参与到其他项目中来。我们整理了一份包含一些简单入门问题的项目清单，方便你快速上手。请查看这个 [项目清单](https://firstcontributions.github.io/#project-list)。

### [附加材料](../additional-material/git_workflow_scenarios/additional-material.md)

## 使用 GitHub Desktop

如果你不习惯使用命令行，[这里有一份使用 GitHub Desktop 的教程](../gui-tool-tutorials/translations/Chinese/github-desktop-tutorial.zh-cn.md)。

## 使用其他工具的教程

| <a href="../gui-tool-tutorials/translations/Chinese/github-desktop-tutorial.zh-cn.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/translations/Chinese/gitkraken-tutorial-zh-cn.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.zh-cn.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/translations/Chinese/github-desktop-tutorial.zh-cn.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/translations/Chinese/gitkraken-tutorial-zh-cn.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.zh-cn.md) |
