[![开源之爱](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![许可证: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions（第一次贡献）

| <img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" width="40"> | Intellij IDEA |
| ---------------------------------------------------------------------------------------------------------------------- | ------------- |

第一次做某事总是困难的。尤其是在协作时，犯错误并不是一件舒服的事。但开源的本质就是协作与共同进步。我们希望简化新手学习与第一次参与开源项目的过程。

阅读文章和观看教程是有帮助的，但没有什么比“亲手实践又不会搞砸项目”更好的学习方式了。这个项目的目标是为新手提供指导，并简化他们第一次做出贡献的过程。记住：越放松，学习效果越好。如果你正在寻找第一次开源贡献的机会，只需按照以下简单的步骤操作。我们保证这将是一段有趣的旅程。

如果你还没有安装 IntelliJ IDEA，[点击这里安装](https://www.jetbrains.com/idea/download/#section=windows)。

**注意：** 本教程使用的是 IntelliJ IDEA（版本 2019.3.2）在 Windows 10 系统上操作。教程中后续涉及的一些快捷键在 macOS 或 Linux 上可能会有所不同。

---

## Fork 这个仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

点击页面右上角的 Fork 按钮 Fork 此仓库。这将在你的 GitHub 账户中创建一个此项目的副本。

GitHub 会记录你 Fork 的仓库与原始仓库之间的关系。你可以把你的副本看作是一个工作副本。

大多数顶层 GitHub 仓库（即不是 Fork 而来的）只有一小部分核心团队成员可以直接提交更改。其他所有贡献者必须 Fork 该仓库，修改后提交 Pull Request 请求将更改合并回主仓库。一旦主仓库管理员批准这些更改，它们将被合并，而你将瞬间收获名誉与财富！稍后我们会介绍如何创建 Pull Request。

---

## 克隆你的仓库

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

下一步是将你的仓库克隆到本地，这样你就可以开始修改内容了。IntelliJ IDEA 需要你的仓库 URL，因此点击仓库页面上的 "Code" 按钮，然后点击“复制”图标。

**注意：** 新手经常犯的一个错误是克隆了原始仓库而不是自己的 Fork 仓库。请确认你复制的是你自己的仓库地址。

现在打开 IntelliJ IDEA。

IntelliJ IDEA 允许你检出（Git 中的 clone）一个已有的仓库，并基于下载的内容创建新项目。

在主菜单中选择 `VCS | Get from Version Control`，或者在没有打开项目时点击欢迎界面中的 `Get from Version Control`。

在打开的对话框中，粘贴你仓库的远程地址（你也可以点击 “Test” 测试连接），或从左侧选择一个 VCS 托管服务。如果你已登录某个服务，它会自动列出你可克隆的仓库。

点击 “Clone”。如果你想基于克隆的源代码创建 IntelliJ 项目，在确认对话框中点击 “Yes”。Git 根目录将自动设置为项目根目录。

如果项目包含子模块，它们也会被克隆并注册为项目根。

**重要提示：** 确保克隆的是你自己的 Fork 仓库，而不是原始仓库，否则不会生效。

---

## 创建分支

在 Git 中，分支是一种强大的机制，允许你从主开发线中分离出来，比如开发一个新功能或为发布冻结某个版本等。

在 IntelliJ IDEA 中，所有与分支相关的操作都可以在 Git 分支弹出窗口中完成。点击状态栏中的 Git 小部件，或按 `Ctrl+Shift+\`` 唤出它。

当前检出的分支名称会显示在状态栏的 Git 小部件中。

在弹出窗口中选择 `New Branch`。

在弹出对话框中输入分支名称，确保勾选 “Checkout branch” 选项，这样你会自动切换到新建分支。

新分支会从当前的 HEAD 开始。如果你想从某个旧提交创建分支，可以在 `Version Control` 工具窗口的 `Log` 选项卡（快捷键 Alt+9）中选择一个提交，然后右键选择 `New Branch`。

---

## 进行必要的修改

打开 `Contributors.md` 文件，在文件中的任意位置添加你的名字。该文件使用的是 GitHub Flavored Markdown (GFM) 语法，是 Markdown 的一种扩展格式。

你可以复制其他贡献者的格式，并修改成你的名字，以确保语法正确 —— 有时语法会比较严格。

---

## 提交并推送更改到 GitHub

在 `Version Control` 工具窗口的 `Local Changes` 选项卡中，选择你要提交的文件或整个更改列表，按下 `Ctrl+K` 或点击工具栏上的 `Commit` 按钮。

在弹出的提交对话框中，会列出你自上次提交以来的所有更改文件及新增文件。

输入有意义的提交信息。

你可以按 `Ctrl+M` 打开提交历史，从中选择最近用过的提交信息。

你也可以在推送前随时修改提交信息。

按 `Ctrl+Shift+K` 或从主菜单选择 `VCS | Git | Push`。弹出的 `Push Commits` 窗口会列出当前分支所有未推送的提交。

---

## 提交 Pull Request 请求代码审查

此时你已完成了修改，但这些更改仍然只存在于你自己的仓库中。接下来我们将向原始仓库提交合并请求。

在你的 GitHub 仓库页面上，你会看到一个 “Compare & pull request” 的按钮。点击它。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="创建 Pull Request" />

接下来提交你的 Pull Request。

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="提交 Pull Request" />

不久之后，你的更改就会被合并到主仓库的 master 分支中。一旦合并成功，你会收到邮件通知。

---

## 接下来可以做什么？

恭喜！你刚刚完成了标准的 _fork -> clone -> 编辑 -> PR_ 流程，这将是你未来开源贡献中非常常见的工作流程！

庆祝一下你的首次贡献，并通过 [web app](https://firstcontributions.github.io#social-share) 与好友分享你的成就吧！

如果你有任何问题，欢迎加入我们的 Slack 团队：[加入 Slack 团队](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

---

### [附加资料](../additional-material/git_workflow_scenarios/additional-material.md)

## 使用其他工具的教程
[返回主页](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
