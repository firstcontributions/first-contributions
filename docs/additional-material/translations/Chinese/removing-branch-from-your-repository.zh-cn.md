# 从你的仓库中移除分支

如果你已经按照教程进行到此，我们的 `<add-your-name>` 分支已经完成了它的使命，是时候将其从你本地机器的仓库中删除了。虽然这不是必须的，但该分支的名称显示了它的特殊用途，因此它的生命周期可以相应地短一些。

首先，让我们将你的 `<add-your-name>` 合并到你的 master 分支中，因此切换到 master 分支：
```
git checkout master
```

将  `<add-your-name>` 合并到 master:
```
git merge <add-your-name> master
```

 在你本地机器的仓库中移除`<add-your-name>` :
```
git branch -d <add-your-name>
```

现在你已经删除了你本地机器上的 `<add-your-name>` 分支，一切看起来整洁干净。
不过，在此时，你应该仍然在你的 GitHub 分叉中有 `<add-your-name>` 分支。然而，在删除之前，请记住，你是从这个远程分支向我的仓库提交了一个 "Pull request"。因此，除非我已经合并了这个请求，否则不要删除这个分支。

然而，如果我已经合并了你的分支，并且你想删除远程分支，可以使用：
```
git push origin --delete <add-your-name>
```

现在，你知道如何整理你的分支了。
随着时间的推移，我的公共仓库会添加很多提交。而你本地机器和 GitHub 分叉的 master 分支将不会保持同步。因此，为了保持你的仓库与我的同步，请按照下面的步骤进行操作。

#### [保持你的分叉与仓库同步](keeping-your-fork-synced-with-this-repository.zh-cn.md)
