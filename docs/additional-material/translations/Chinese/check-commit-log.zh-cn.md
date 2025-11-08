# 查看提交日志

为了查看某个分支或某个文件的提交日志，可以使用以下命令：

`git log [options] [path]`

该命令的输出默认按逆时间顺序排列。

## 命令输出示例
```
$ git log
commit e3fabb30ab536bd5876461d8a749301a321e714f (HEAD -> check-commit-log-ko, upstream/main, origin/main, origin/HEAD, main)
Author: Dan Yunheum Seol yunheum.seol@mail.mcgill.ca
Date: Tue Jun 4 01:07:25 2024 -0400

    Add dan-seol to Contributors list (#84962)

commit 4af4ec8a56e057ce8768af77eda528453974d0bc
Author: Edgar Humberto Tijerina Tamez <168693312+EdgarHTT@users.noreply.github.com>
Date:   Mon Jun 3 23:06:05 2024 -0600

    Add Edgar Tijerina to Contributors list (#84961)
```


## 命令变体和选项
- 若要查看从某些特定提交 ids: <i>（例如 `foo` 和 `bar`）可达的提交，可以使用：</i><br>
    `git log foo bar `
- 也可以通过在提交 id 前添加 `^` 来排除某个提交<i>（例如 `baz`）：</i><br>
    `git log foo bar ^baz`
- 查看特定文件的提交日志：<br>
    `git log --all <filename>`
- 限制日志中提交的数量：<i>（例如 `5`）</i><br> 
    `git log -n 5`

## 参考
- [官方文档](https://git-scm.com/docs/git-log)
