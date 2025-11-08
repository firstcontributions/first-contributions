# 移动提交到不同的分支
假设你提交了一个更改，然后意识到你提交到了错误的分支。  
你该如何更改呢？这篇教程将为你解答。

## 将最新的提交移动到现有分支
为此，请输入以下命令：

```git reset HEAD~ --soft``` - 撤销上一个提交，但保留更改。
```git stash``` - 记录当前目录的状态。

```git checkout name-of-the-correct-branch``` - 切换到正确的分支。
```git stash pop``` - 恢复最近的存储状态。
```git add .``` - 或者尝试单独添加文件。 
```git commit -m "your message here"``` - 保存并提交更改。

现在你的更改已经在正确的分支上了。


### 将最新的提交移动到新分支
为此，请输入以下命令：
```git branch newbranch``` -  创建一个新分支，保存所有提交。
```git reset --hard HEAD~#``` - 将 master 分支回退 # 个提交。记住，这些提交将从 master 中消失。
```git checkout newbranch``` - 切换到你创建的新分支，所有提交都会在该分支中。

记住：任何未提交的更改将会丢失。
