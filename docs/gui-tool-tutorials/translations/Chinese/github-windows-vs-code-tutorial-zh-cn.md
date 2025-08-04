[![开源之爱](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![许可证: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![开源助手](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 首次贡献 (First Contributions)

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |

这很难。第一次做任何事情总是困难的。尤其是当你与他人协作时，犯错可不是件让人舒服的事。但开源的核心正是协作与共同工作。我们希望能简化新的开源贡献者首次学习和贡献的方式。

阅读文章和观看教程会有所帮助，但有什么能比在不搞砸任何东西的情况下实际操作更好呢？本项目旨在为新手提供指导并简化他们进行首次贡献的方式。记住，你越放松，学得越好。如果你想进行首次贡献，只需按照下面的简单步骤操作。我们保证，这会很有趣。

如果你的机器上没有安装 Visual Studio Code，请先[安装它](https://code.visualstudio.com/download)。

**注意：** 本教程是在 Windows 10 机器上使用 Visual Studio Code (版本 1.27.2) 制作的。在本教程后面，我们将使用一些键盘快捷键。这些快捷键在其他操作系统 (macOS/Linux) 以及不同键盘语言 (英式、德式等) 上可能有所不同。你可以通过在命令面板 (Command Palette) 中搜索 "shortcut" 来查看你的快捷键列表。

## 派生 (Fork) 此仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

点击此页面右上角的 "Fork" 按钮来派生 (Fork) 这个仓库。这将在你的 GitHub 账户中创建此仓库的一个副本。

GitHub 会跟踪你的仓库与你派生它的原始仓库之间的关系。你可以把你的仓库看作一个工作副本。

大多数顶级 GitHub 仓库（即不是从其他仓库派生的仓库）都有一个核心团队，其成员可以直接提交更改。所有其他贡献者必须派生该仓库，在派生副本中进行更改，然后创建一个拉取请求 (Pull Request) 来请求将其更改合并回顶级仓库。如果顶级仓库的管理员喜欢这些更改，它们将被合并，你将获得即时的名望和财富！稍后会详细介绍如何操作。

## 克隆 (Clone) 你的仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

下一步是将你的仓库克隆 (Clone) 到本地机器上，以便开始进行更改。VS Code 需要你的仓库 URL，因此请点击 "Code" 按钮，然后点击 "复制到剪贴板" 图标。

**注意：** 新贡献者常犯的一个错误是克隆了你派生 *自* 的原始仓库，而不是克隆你自己的仓库。检查浏览器的地址栏，确保你克隆的是你自己的仓库（URL 中包含你的用户名）。

现在打开 Visual Studio Code。VS Code 的欢迎页面会出现。在那里按 `F1` 打开下面显示的栏。注意文本字段中已经有一个 `>`（大于）符号。你也可以通过按 `CTRL-P` 然后输入 `>` 字符来进入输入提示。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="Clone Popup (Command Popup)" />

你可能会注意到下面已经列出了一些晦涩的命令。这些是我最近使用的命令。所以暂时不用管它们。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="Clone repo" />

现在输入 `git clone`，只输入 `git` 或 `clone` 也可以（它会像搜索一样工作）。
选择 `Git: Clone` 条目并按 `Enter`。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

粘贴你的仓库 URL 并按 `Enter`。这将打开一个文件资源管理器，你可以选择 Git 仓库的存储位置。

**重要提示**：确保克隆的是你派生后的仓库，而不是原始仓库，否则无法正常工作。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="Status popup" />

你应该会在 Visual Studio Code 的右下角看到一个状态弹出窗口。完成后，你可以使用对话框中的按钮打开克隆的仓库（现在是你机器上的一个文件夹）。

## 创建一个分支 (Branch)

再次按 `F1` 打开命令面板 (Command Palette)。输入 `branch` 并从那里选择 `create branch` 命令。在下一步中输入你的新分支名称，例如 `add-david-kroell`。按 Enter，分支将被创建。该分支也会被自动检出 (checkout)。[检出 (checkout) 是什么意思？](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />

## 进行必要的更改

打开 `Contributors.md` 文件，并在文件任意位置添加你的名字。此文件包含 GFM (GitHub Flavored Markdown)，它是 [markdown](https://en.wikipedia.org/wiki/Markdown) 语法的 GitHub 特有版本。

复制其他贡献者的一行，并用你的名字修改它，以确保语法正确 - 它可能很挑剔。保存文件以注册更改。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />

## 提交 (Commit) 更改并将更改推送 (Push) 到 GitHub

在 VS Code 的左侧是一个显示 5 个图标的菜单。选择版本控制 / 源代码管理图标 (Source Control icon)。
(快捷键：Ctrl + Shift + G)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="Commit changes" />

文件资源管理器会显示自上次提交以来所有更改过的文件。将鼠标悬停在文件上并点击 `+`（加号）可以将文件暂存 (stage)。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="Stashed Files">

在资源管理器顶部的输入行中键入一些提交信息（例如 "Add <你的名字> to Contributors list"），然后点击勾选标记 (checkmark)。更改现在已提交 (commit) 到你的本地副本。接下来需要将这些更改推送 (push) 回 GitHub。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="Stashed Files">

使用三点图标打开菜单，在其中选择 `Publish Branch` 选项。这应该会打开一个对话框，让你输入 GitHub 凭据。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="Stashed Files">

## 提交你的更改以供审查

此时你已完成更改，但它仍然只存在于你的仓库中。此步骤将向你展示如何向顶级仓库的管理员提交请求以合并你的更改。

在你的 GitHub 仓库中，你会看到新分支通知旁边有一个 `Compare & pull request` 按钮。点击该按钮。

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

现在提交 (submit) 这个拉取请求 (Pull Request)。

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

很快，我会将所有更改合并 (merge) 到本项目的主分支 (master branch) 中。更改合并后，你将收到一封通知邮件。

## 下一步该做什么？

恭喜！你刚刚完成了一个标准的 *派生 (Fork) -> 克隆 (Clone) -> 编辑 (Edit) -> 提交拉取请求 (PR)* 工作流程，作为贡献者你会经常遇到它！

庆祝你的贡献，并通过访问 [web app](https://firstcontributions.github.io#social-share) 与你的朋友和关注者分享。

如果你需要任何帮助或有任何疑问，可以加入我们的 Slack 团队。[加入 Slack 团队](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)。

### [附加材料](../additional-material/git_workflow_scenarios/additional-material.md)

## 使用其他工具的教程
[返回主页](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
