# 使用 Git Stash 暂存工作进度

如果你正在进行一个大型开发任务，突然需要切换分支去做其他事情，但当前代码还没写完、也没有测试，  
你可能并不希望提交这些不完整的更改。可 Git 不允许你直接切换分支，除非先处理这些更改。  
那该怎么办呢？如何避免提交未完成的代码，同时还能自由切换分支？

这就是本教程要讲解的内容。

## 暂存你的工作（Stashing）

假设你在项目的某个分支中修改了一些文件，此时运行  ```git status``` 可以看到：

```
$ git status
# 当前分支：master
# 暂存区中的更改：
#   (使用 "git reset HEAD <file>..." 来取消暂存)
#
#      修改:   index.html
#
# 未暂存的更改：
#   (使用 "git add <file>..." 来更新将要提交的内容)
#
#      修改:   lib/simplegit.rb
#
```

此时你想切换分支，但又不想提交更改。那就使用 ```git stash```:

```
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(要恢复这些更改，输入 "git stash apply")
```

现在你的工作目录是干净的，可以使用 ```git status``` 查看：

```
$ git status
# 当前分支：master
没有要提交的内容，工作目录干净
```

此时你可以切换到任意分支继续开发。你 stash 的内容被保存在一个栈（stack）中。你可以使用 ```git stash list``` 查看所有保存的 stash：

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

如果你想重新应用刚刚保存的 stash，可以使用 ```git stash apply```。默认情况下，它会应用最近一次保存的 stash。  
如果你想应用指定的 stash，可以使用命令 ```git stash apply <stash-name>```，将 `<stash-name>` 替换为对应名称：

```
$ git stash apply
# 当前分支：master
# 未暂存的更改：
#   (使用 "git add <file>..." 来更新将要提交的内容)
#
#      修改：   index.html
#      修改：   lib/simplegit.rb
#
```

你会发现 Git 恢复了你在执行 stash 时未提交的更改。  
在这个示例中，你在应用 stash 时处于干净的工作目录，且是在与 stash 创建时相同的分支；  
但请注意：**并不要求工作目录必须干净，也不需要在原分支才能成功应用 stash。**

你可以在一个分支中保存 stash，之后切换到另一个分支并重新应用它。  
即使当前工作目录中存在未提交的更改，也可以应用 stash；但如果某些内容无法干净地应用，Git 会提示合并冲突。

文件中的更改虽然恢复了，但之前已暂存（staged）的文件并没有恢复到暂存区。  
要恢复这些被暂存的更改，你需要使用带有 ```--index``` 参数的 ```git stash apply```：

```
$ git stash apply --index
# 当前分支： master
# 已暂存更改：
#   (使用 "git reset HEAD <file>..." 取消暂存)
#
#      修改：   index.html
#
# 未暂存更改：
#   (使用 "git add <file>..." to update what will be committed)
#
#      修改：   lib/simplegit.rb
#
```

`apply` 命令仅仅是恢复 stash 内容，它不会自动从 stash 栈中移除对应条目。

如果你想删除某个 stash，可以使用 ```git stash drop``` 并指定 stash 名称：

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
```

你也可以使用 ```git stash pop``` 命令，它会应用最后一次 stash 的内容并将其从栈中删除。

## 取消应用已应用的 Stash（Un-applying）

有时你应用了 stash，做了一些工作，但之后想要**撤销**刚刚恢复的 stash 更改。  
Git 并没有内建 ```git unapply``` 命令，但你可以使用“反向补丁”来实现类似效果：

```$ git stash show -p stash@{0} | git apply -R```

如果不指定 stash，Git 默认使用最新的 stash：

```$ git stash show -p | git apply -R```

你也可以为此配置一个快捷别名：

```
$ git config --global alias.stash-unapply '!git stash show -p | git apply -R'
$ git stash apply
$ #... 进行工作
$ git stash-unapply
```

## 从 Stash 创建新分支

如果你 stash 了某些更改，但后来继续在该分支上进行开发，  
再次应用 stash 时可能会因为文件已被修改而引发**冲突**。

如果你想更方便地重新测试 stash 的内容，可以使用 ```git stash branch``` 命令。  
它会执行以下操作：

1. 创建一个新分支；
2. 回到你 stash 时所在的提交；
3. 应用 stash 内容；
4. 应用成功后自动删除 stash。

示例：

```
$ git stash branch testchanges
Switched to a new branch "testchanges"
# 当前分支： testchanges
# 已暂存的更改：
#   (使用 "git reset HEAD <file>..." 取消暂存)
#
#      修改:   index.html
#
# 未暂存的更改：
#   (使用 "git add <file>..." 来更新将要提交的内容)
#
#      修改:   lib/simplegit.rb
#
Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
```

这是一个非常实用的快捷方式，可以轻松恢复你 stash 的内容，并在一个新分支中继续开发。