# 撤销本地提交

要撤销本地提交，只需要运行以下命令：
```
git reset
```
此命令会将暂存区（staging area）重置为你最近的一次提交，但工作目录中的更改不会被影响。  
因此，你仍然可以重新提交这些更改。

如果你只是想从上一次提交中移除某个文件，可以使用以下命令：
```
git reset <文件名>
```
该命令只会将指定的文件从暂存区中移除，但文件中的更改仍然保留。

```git reset``` 使用示例：
```
# 修改了 index.php 和 tutorial.php
# 将文件添加到暂存区
$ git add .
# 想起来这两个文件应该分开提交
# 取消暂存 tutorial.php
$ git reset tutorial.php
# 先提交 index.php
$ git commit -m "Changed index.php"
# 现在提交 tutorial.php
$ git add tutorial.php
$ git commit -m "修改了 tutorial.php"
```

假设你把本地仓库搞乱了，只想恢复到最近一次提交的状态，  
你可以运行以下命令：
```
git reset --hard
```
这个命令不仅会重置暂存区，还会把工作目录中的所有更改回退到最近一次提交。
其中的 ```--hard``` 模式表示 Git 会同时撤销工作目录中的所有改动。
**只有当你确定想彻底丢弃本地的所有开发内容时，才应该使用这个命令。**

```git reset --hard``` 使用示例：
```
# 决定开始一个疯狂的实验
# 创建一个新文件 'crazy.php' 并写入一些代码
# 提交 crazy.php
$ git add crazy.php
$ git commit -m "开始了疯狂的开发"
# 再次编辑 crazy.php 并修改了很多其他文件
# 提交所有被跟踪的文件
$ git add .
$ git commit -m "继续开发"
# 测试后情况失控
# 决定把所有内容撤销
$ git reset --hard HEAD~2
```

```git reset --hard HEAD~2``` 会将当前分支回退两个提交点，  
同时撤销你所做的所有更改，并将这两个提交从项目历史中移除。

注意： 如果你已经将提交推送到了共享仓库，请不要执行 ```git reset --hard``` 因为这将对仓库中的其他人造成问题。