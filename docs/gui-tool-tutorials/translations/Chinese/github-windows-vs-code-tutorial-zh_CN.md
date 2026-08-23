[![开源之爱](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![许可证: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![开源助手](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 首次贡献

| <img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="40"> | Visual Studio Code |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


万事开头难。第一次做某件事情的时候总是很困难，尤其是在协作的时候，犯错并不是一件舒服的事情。但是开源的本质就是协作和共同工作。我们希望简化新的开源贡献者第一次学习和贡献的方式。

阅读文章和观看教程会有所帮助。但是，有什么比在不搞砸任何东西的情况下实际操作更好的呢？这个项目旨在提供指导并简化新手进行首次贡献的方式。记住：你越放松，学习效果就越好。如果你正在寻找进行你的第一次贡献，只需按照下面的简单步骤操作即可。我们保证，这会很有趣。

如果你的电脑上还没有安装 Visual Studio Code，请[点击此处安装](https://code.visualstudio.com/download)。

**注意：** 本教程是在 Windows 10 系统上使用 Visual Studio Code（版本 1.27.2）制作的。在本教程的后面部分，我们将使用一些键盘快捷键。这些快捷键在其他操作系统（macOS/Linux）以及不同的键盘语言（英国、德国等）上可能会有所不同。你可以通过在命令面板中搜索"快捷键"来查看你的快捷键列表。

## Fork 这个仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork 这个仓库" />

点击页面右上角的 fork 按钮来 fork 这个仓库。这会在你的 GitHub 账户中创建一个该仓库的副本。

GitHub 会记录你的仓库和你 fork 的源仓库之间的关系。你可以把你的仓库看作是一个工作副本。

大多数顶级 GitHub 仓库（即不是从其他仓库 fork 而来的仓库）都有一个小型的核心团队，可以直接提交更改。所有其他贡献者必须 fork 仓库，在 fork 后的仓库中进行更改，然后创建一个 Pull Request 来请求将他们的更改合并回顶级仓库。如果顶级仓库管理员喜欢这些更改，它们就会被合并，你会立即获得名气和财富！稍后我们会详细介绍如何做到这一点。

## 克隆你的仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="克隆这个仓库" />

下一步是将你的仓库克隆到你的电脑上，这样你就可以开始进行更改了。VS Code 需要你的仓库的 URL，所以点击 code 按钮，然后点击"复制到剪贴板"图标。

**注意：** 新贡献者常犯的一个错误是克隆你 fork 来源的仓库，而不是克隆你自己的仓库。检查你的浏览器地址栏，确保你克隆的是你自己的仓库。

现在打开 Visual Studio Code。VS Code 的欢迎页面会弹出。在那里按下 `F1` 打开下面显示的命令栏。注意文本字段中已经有一个 `>`（大于号）符号。你也可以通过按下 `CTRL-P` 然后输入 `>` 字符来打开输入提示。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone.png" alt="克隆弹出窗口（命令弹出窗口）" />

你可能会注意到下面已经列出了一些晦涩的命令。这些是我最近使用的命令，所以不用在意它们。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone1.png" alt="克隆仓库" />

现在输入 `git clone`，或者只输入 `git` 或 `clone`（它就像搜索一样工作）。
选择 `Git: Clone` 选项，然后按 `Enter` 键。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="粘贴仓库 URL" />

粘贴你仓库的 URL，然后按 `Enter` 键。这会打开一个文件资源管理器，你可以在其中选择 Git 仓库的存储位置。

**重要提示：** 确保这是你 fork 的仓库，而不是原始仓库，否则它将无法工作。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone3.png" alt="状态弹出窗口" />

你应该会在 Visual Studio Code 的右下角看到一个状态弹出窗口。完成后，你可以使用对话框中的按钮打开克隆的仓库（现在是你电脑上的一个文件夹）。

## 创建分支

再次按 `F1` 打开命令面板。输入 `branch`，然后从那里选择 `create branch` 命令。下一步输入你的新分支的名称，例如 `add-david-kroell`。按回车键，分支就会被创建。该分支也已经被检出。[什么是检出？](https://www.git-scm.com/docs/git-checkout)

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="分支命令面板" />

## 进行必要的更改

打开 `Contributors.md` 文件，在文件的任意位置添加你的名字。这个文件使用 GFM（GitHub 风格的 Markdown），这是 <a href="https://en.wikipedia.org/wiki/Markdown">Markdown</a> 语法的一个专有变体。

复制其他贡献者的某一行，然后用你的名字修改它，以确保语法正确——Markdown 对语法要求很严格。保存文件以记录更改。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="添加你的名字" />

## 提交并推送更改到 GitHub

在 VS Code 的左侧有一个显示 5 个图标的菜单。选择版本控制/源代码管理图标。
（快捷键：Ctrl + Shift + G）

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit.png" alt="提交更改" />

文件资源管理器会显示上次提交后所有被更改的文件。将鼠标悬停在文件上，点击 `+`（加号）就可以暂存文件。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-commit1.png" alt="暂存文件">

在资源管理器顶部的输入栏中输入一些内容，然后点击对勾按钮。现在更改已经提交到你的本地副本。接下来需要将更改推送回 GitHub。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="暂存文件">

使用三点图标打开菜单，在菜单中选择 `Publish Branch` 选项。这会打开一个对话框，让你输入你的 GitHub 凭据。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-gh-auth.png" alt="暂存文件">

## 提交你的更改以供审核

到目前为止，你已经完成了更改，但这些更改仍然只存在于你的仓库中。这一步将向你展示如何向顶级仓库的管理员提交请求，以合并你的更改。

在你 GitHub 上的仓库中，你会在新分支通知旁边看到 `Compare & pull request` 按钮。点击这个按钮。

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="创建一个 pull request" />

现在提交 pull request。

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="提交 pull request" />

我很快就会把你所有的更改合并到这个项目的主分支中。一旦更改被合并，你会收到一封通知邮件。

## 接下来去哪里？

恭喜你！你刚刚完成了作为贡献者经常会遇到的标准 _fork -> clone -> edit -> PR_ 工作流程！

你可以前往[网页应用](https://firstcontributions.github.io#social-share)庆祝你的贡献，并与你的朋友和关注者分享。

### [附加材料](../additional-material/git_workflow_scenarios/additional-material.md)

## 使用其他工具的教程

[返回主页](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)