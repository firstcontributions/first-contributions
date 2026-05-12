[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# 第一次贡献

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub 命令行界面（CLI） |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

本指南专为我们这些终端爱好者而写——我们希望在终端中完成一切操作。借助 [Github-CLI](https://cli.github.com/)，这完全可以实现！记住，你的第一次贡献应该是有趣的、有成就感的，并能激励你继续前行！

本指南略有挑战性，因为我们完全不使用任何图形界面，但依然非常有趣，你完全可以跟着做！

首先需要满足以下条件：

- 已安装 Git（如何安装 [git](https://git-scm.com/downloads)）
- 拥有 Github 账号

接下来，我们需要按照[官方文档](https://github.com/cli/cli#installation)在系统中安装 `github-cli` 工具。

安装完成后，我们需要在 CLI 中登录，输入以下命令：

```bash
gh auth login
```

按照提示操作，即可准备就绪！

# Fork 此仓库

只需运行以下命令即可：

```bash
gh repo fork firstcontributions/first-contributions
```

**重要提示：系统会询问你是否同时克隆仓库，请选择"是"。**

# 创建你的分支

我们将使用 git 完成此步骤，输入以下命令并将名字替换为你自己的名字，例如：

```bash
git switch -c add-john-doe
```

# 进行必要的修改并提交

现在你可以用文本编辑器打开 `Contributors.md` 文件，并将你的名字添加进去。将名字放在文件开头和结尾之间的任意位置，然后保存文件。

在项目目录中执行 `git status`，你将看到所做的更改。
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

使用 `git add` 命令将这些更改添加到你刚创建的分支：
`git add Contributors.md`

然后使用 `git commit` 命令提交这些更改：
`git commit -m "Add your-name to Contributors list`
将 `your-name` 替换为你的名字。

# 将更改推送到 Github

使用 `git push` 命令推送你的更改：

```
git push origin -u your-branch-name
```

将 `your-branch-name` 替换为你之前创建的分支名称。

<details>
<summary> <strong>如果推送时出现错误，请点击此处：</strong> </summary>

- ### 身份验证错误
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  请参考 [GitHub 教程](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)，生成 SSH 密钥并将其配置到你的账号。

</details>

# 提交你的更改以供审核

在仓库目录中运行以下命令，即可创建一个供审核的 Pull Request：

```bash
gh pr create --repo firstcontributions/first-contributions
```

之后提交该 Pull Request。

你可以使用 `gh status` 命令查看你的 Pull Request 状态。

## 接下来做什么？

恭喜你！你刚刚完成了作为贡献者常见的标准工作流程：_fork -> 克隆 -> 编辑 -> pull request_！

前往 [网页应用](https://firstcontributions.github.io/#social-share)，庆祝你的贡献并与朋友和关注者分享吧！

如果你想继续练习，请查看[代码贡献](https://github.com/roshanjossey/code-contributions)。

现在让我们开始为其他项目做贡献吧！我们整理了一份包含简单问题的项目列表供你入门。请查看[网页应用中的项目列表](https://firstcontributions.github.io/#project-list)。

### [附加资料](https://github.com/firstcontributions/first-contributions/blob/main/docs/additional-material/git_workflow_scenarios/additional-material.md)

[返回主页](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)