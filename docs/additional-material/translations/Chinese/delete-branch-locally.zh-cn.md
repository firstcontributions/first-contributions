# 删除本地创建的分支

当你不小心拼错了分支名称时，这个操作会非常有用。

你可以通过 *3* 种方式来删除分支：

```
git branch -D <branch_name>
```

```
git branch --delete --force <branch_name>  # 与 -D 相同
```

```
git branch --delete  <branch_name>         # 如果未合并会报错
```

-D 代表 --delete --force，即即使分支未合并，也会强制删除该分支。你也可以使用 -d，它代表 --delete，当分支未合并时，会抛出错误。
