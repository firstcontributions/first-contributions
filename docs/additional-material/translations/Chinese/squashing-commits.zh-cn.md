# 什么是 Squashing（压缩提交）？

在 Git 中，**squashing（压缩提交）** 是指重写提交历史，把多个提交合并成一个提交，并添加一个描述性信息来说明这次更改的内容。  

在开源项目中，这通常是常见操作，因为分支的详细历史记录往往只对原始开发者有意义。  
压缩提交可以简化更改记录，也方便在需要时进行回滚。

# 如何进行提交压缩（Squash commits）？

首先，你可以执行 `git log` 命令，查看你当前分支中要合并的提交历史：

```
git log
```

你会看到类似这样的提交记录：

```
commit blablabla
Author: omguhh
Date:   10/10/20
    提交信息 1

commit blablabla2
Author: omguhh
Date:   10/10/20
    提交信息 2
```

现在你已经找到了要合并的提交，可以使用 ```git rebase```来进行压缩。假设你已经熟悉 ```git rebase```，我们可以通过 **交互模式（interactive mode）** 来进行操作：

```
git rebase -i
```

你也可以通过指定回溯的提交数来启动交互式 rebase，比如：

```
git rebase -i HEAD~2
```

执行该命令后，你将看到类似以下内容的交互式界面：

```
pick blablabla Changing test01.txt file
pick blablabla2 Adding dummy01.txt file

#
# 可用命令：
#  p, pick = 使用该提交
#  r, reword = 使用该提交，但修改提交信息
#  e, edit = 使用该提交，但中断以进行修改
#  s, squash = 使用该提交，但合并进前一个提交
#  f, fixup = 类似 squash，但忽略该提交信息
#  x, exec = 执行 shell 命令
#
# 你可以调整这些行的顺序，Git 会按顺序执行。
#
# 如果删除某一行，该提交将会丢失。
#
# 如果删除所有行，rebase 将会被取消。
#
# 空提交将会被注释掉。
```

所以，如果你想将 ```blablabla2``` 压缩到 ```blablablabla```，你应该将其改成如下形式：

```
pick blablabla 更改 test01.txt 文件
squash blablabla2 添加 dummy01.txt 文件

```

一切正常的话，你将看到如下合并提交的编辑界面：

```
# 这是两个提交的合并结果.
# 第一个提交的信息是：
提交信息 1

# 第二个提交的信息是：

提交信息 2
```

你可以在此自由修改合并提交的信息。  

退出并保存后，执行 `git log` 命令应显示你刚刚输入的合并信息，且这两个提交已被合并为一个。