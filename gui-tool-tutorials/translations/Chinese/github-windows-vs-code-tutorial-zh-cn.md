[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |

万事开头难。特别是在与他人合作时，犯错误会让人感到难受。但开源就是协作和共同努力。我们希望简化新手开源贡献者第一次贡献的方式。

你可以通过阅读文章和观看教程来学习，但第一次真正地参与贡献并且不会破坏原有的内容，这种感受是文章视频带来不了的。该项目旨在提供指导并简化新手参与开源。请记住，越轻松，学得越好。如果您正在寻求首次贡献，只需按照以下简单步骤操作即可。我们向你保证，这会很有趣。

如果你的计算机还没有安装Visual Studio Code, 请[安装](https://code.visualstudio.com/download).

**注意**: 本教程是在 Windows 11 计算机上使用 Visual Studio Code（版本 1.87.2）制作的。在本教程的后面部分，我们将使用一些键盘快捷键。这些在其他操作系统 (macOS/Linux) 以及键盘语言（英国、德国等）上可能有所不同。

## Fork Repository（分叉仓库）

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

**注意**: `fork`一词并没有统一的翻译，有的翻译为“分叉”，有的翻译为“复刻”。在github的中文文档里， fork 被翻译为“分叉”，具体内涵可以查看[文档](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)，类似于创建备份的意思。为了交流的方便更推荐直接称之为 fork ，下文提到 fork 的地方都是指“分叉”这个操作。

单击此仓库的右上角的 Fork 按钮来此仓库。这将在您的 GitHub 帐户中创建此仓库的副本，您对其拥有完全的权限，包括删除等。

GitHub 会跟踪您 fork 的仓库与被 fork 仓库之间的关系。

大多数顶级 GitHub 仓库（即不是从其他仓库 fork 的仓库）都有一个可以直接提交更改的小型核心团队。

所有想要参与开源的其他贡献者必须 fork 该仓库并在他们自己的仓库中进行更改，然后创建 Pull Request （合并申请）将他们的更改合并到顶级仓库中。

如果顶级仓库管理员喜欢这些更改，它们将被合并。稍后将详细介绍如何执行此操作。

## Clone Repository（克隆仓库）

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

下一步是将你的仓库下载到你的计算机上，以便你可以开始进行更改。在你的仓库主页面单击 Code 按钮，您可以看到一个URL地址，点击最后面的一个复制按钮即可复制 URL。或者您也可以点击 URL 并按下 `Ctrl+C` 复制它。

**注意**: 新生经常会犯仓库克隆错误的问题，您需要克隆您的仓库，而不是被您fork的仓库。检查浏览器的地址栏并确保您正在克隆您的仓库。

现在打开 Visual Studio Code。按下 `F1` 打开如下所示的栏。请注意，文本字段中已经有一个 `>`（大于）符号。您还可以通过按 `CTRL+P` 进入输入提示，然后键入 `>` 字符。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

您可能会注意到下面列出了一些命令。这是原作者的历史记录，可以忽略它们。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

在搜索框输入 `git clone`，然后选择 `Git: Clone` 并按 `Enter`。

如果你安装了中文插件，则是 `Git: 克隆`。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

粘贴存储库的 URL 并按 `Enter` 。这将打开资源管理器，需要你告诉 Visual Studio Code 把下载的仓库放在哪里。

**再次提醒**: 确保它是您的仓库而不是原始仓库，否则您无法提交更改。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

您应该会在 Visual Studio Code 的右下角看到一个状态弹出窗口。完成后，您可以使用对话框中的按钮打开克隆的仓库（现在仓库被下载到您的计算机本地了）。

## Create a branch（创建分支）

按 `F1` 再次打开命令选项板。输入 `create branch` 并从其中选择 `Git: Create Branch`（中文插件是 `Git: 创建分支`） 命令。在下一步中输入新分支的名称，例如 `add-david-kroell` 。按 `Enter` 键，将创建分支并 checkout（签出）。如果您不知道 checkout（签出）是什么意思，请点击[这里](https://www.git-scm.com/docs/git-checkout/zh_HANS-CN)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## Make necessary changes

打开 Contributors.md 并将您的姓名添加到文件中的任意位置。该文件包含 GFM（GitHub Flavored Markdown），它是 <a href="https://en.wikipedia.org/wiki/Markdown">Markdown</a> 语法的专有风格。

也许您是第一次见到这种文件，但是不用担心，我会告诉您如何编辑它。

复制下面的代码，[] 中括号之间填入您 github 的昵称，() 小括号直接填入您 github 的主页链接，然后粘贴到 Contributors.md 文件中，使你填写的内容独立成行，也就是一行中只有你的填写的内容。`CTRL+S` 保存文件。

```markdown
- [您的昵称](你的github主页链接))
```


<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## Commit & Push （提交并推送到Github）

VS Code 的左侧是一个菜单，其中显示了 5 个图标。选择 version control/Source Control（中文插件：源代码管理） 图标。 您也可以按下`CTRL+SHIFT+G`快速打开。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

资源管理器显示上次提交后所有有更改文件。我们需要暂存文件，您可以在文件上面点击 `+` 来暂存该文件，也可以点击 CHAGES（中文插件：更改） 上的 `+` 按钮暂存所有文件。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

在刚刚的上方你可以看到有一个输入框，这是提交信息输入框，用来解释本次提交。例如 `Add <your-name> to Contributors list`，然后按 `Ctrl+Enter` 提交更改。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

现在您已经把您修改过的代码提交到了您的仓库。接下来我们需要把这些修改推送到 GitHub 上。点击 `...` 按钮，然后选择 `Push`（中文插件：推送）。不过第一次的您可能需要输入您的 GitHub 账号和密码。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## Pull Request（RP，合并请求）

此时的您所有的修改仅仅存在于你的仓库，一下步将提交到原始仓库中。

在您 GitHub 上的仓库中，您将看到新分支通知旁边的 Compare & pull request 按钮。单击该按钮。

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

现在您可以提交Pull Request（合并请求）了。

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

不就之后作者会将您的所有更改合并到该项目的 main 分支中。合并更改后，您将收到一封通知电子邮件。

## 下一步去哪?

恭喜！您刚刚完成了作为贡献者经常遇到的标准流程：fork -> 克隆 -> 编辑 -> PR！

庆祝您的在开源路上的第一次贡献吧，您也可以和您的亲朋好友分享这个[网站](https://firstcontributions.github.io#social-share)，帮助他们参与到开源中来。

如果您需要任何帮助或有任何疑问，可以加入我们的 Slack 团队。[加入 slack 群组](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

### [附加资料](../../../additional-material/translations/Chinese/additional-material.zh-cn.md)

## 使用其他工具的教程

[返回主页](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
