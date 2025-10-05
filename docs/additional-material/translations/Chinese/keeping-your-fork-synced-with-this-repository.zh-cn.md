# 保持你的分叉与该仓库同步

首先，应该理解完整同步的流程，这一点非常重要。在这个流程中，有三个不同的仓库：我的公共仓库在 GitHub 上 `github.com/firstcontributions/first-contributions.git`，你在 GitHub 上的仓库分叉 `github.com/Your-Name/first-contributions/`，以及你本地机器上的仓库，你应该在其中进行工作。这种合作方式通常用于开源项目，称为 `Triangle Workflows`。

<img style="float;" src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

为了保持你的两个仓库与我的公共仓库同步，我们首先需要将公共仓库的内容拉取并与本地机器上的仓库合并。
我们的第二步是将你的本地仓库推送到你的 GitHub 分叉。如前所述，只有通过你的分叉你才能发起一个“拉取请求”。因此，你的 GitHub 分叉是最后更新的仓库。

现在，让我们看看如何做到这一点：

首先，你必须确保自己处于主分支上。要知道自己当前在哪个分支，可以检查的第一行：
```
git status
```
如果你不在主分支上，输入以下命令切换到主分支：
```
git checkout main
```

然后，你应该将我的公共仓库添加到你的 Git 仓库中，使用 `add upstream remote-url`：
```
git remote add upstream https://github.com/firstcontributions/first-contributions.git
```
这告诉 Git，指定的 URL 位置有该项目的另一个版本，并且我们将其命名为 `upstream`。一旦你的 Git 配置了上游仓库，你就可以拉取公共仓库的最新版本：
```
git fetch upstream
```

你刚刚拉取了我仓库的最新版本（`upstream` 远程仓库）。现在，你需要将公共仓库的内容合并到你的主分支中：
```
git rebase upstream/main
```
在这里，你正在将公共仓库合并到你的主分支。现在，你本地机器上的主分支已更新。最后，如果你将主分支推送到你的 GitHub 分叉，那么你的 GitHub 分叉也会更新：
```
git push origin main
```
请注意，这里你推送的是名为 `origin` 的远程仓库。

如果你想同时将我仓库的最新更改（`upstream` 远程仓库）拉取并合并到你本地的分支中，可以直接使用：
```
git pull upstream main
```

到目前为止，你的所有仓库都已更新。做得很好！每当你的 GitHub 仓库提示你比公共仓库落后几个提交时，你都应该执行这些操作。
