# .gitignore

.gitignore 文件是一个文本文件，用于告诉 Git 在项目中哪些文件或文件夹应被忽略。

一个本地的 .gitignore 文件通常放置在项目的根目录下。你也可以创建一个全局的 .gitignore 文件，这样文件中的任何条目都会在你所有的 Git 仓库中被忽略。

## 为什么使用 .gitignore
现在你可能会想，为什么要让 Git 忽略某些文件和文件夹。原因是你不希望像构建文件、缓存文件、其他本地配置文件（例如 node_modules）、编译文件、IDE 创建的临时文件等被 Git 跟踪。通常，这样做是为了避免提交工作目录中的临时文件，这些文件对其他协作者没有用。

## 入门
要创建一个本地的 .gitignore 文件，创建一个文本文件并命名为 .gitignore（记得在文件名前加上 `.`）。然后根据需要编辑此文件。每一行都应该列出你希望 Git 忽略的文件或文件夹。

该文件中的条目也可以遵循匹配模式。

```
* 用作通配符匹配
/ 用于忽略相对于 .gitignore 文件的路径名
# 用于在 .gitignore 文件中添加注释

下面是 .gitignore 文件的一个示例：

# 忽略 Mac 系统文件
.DS_store

# 忽略 node_modules 文件夹
node_modules

# 忽略所有文本文件
*.txt

# 忽略与 API 密钥相关的文件
.env

# 忽略 SASS 配置文件
.sass-cache

```
要添加或更改全局 `.gitignore` 文件，运行以下命令：

```
git config --global core.excludesfile ~/.gitignore_global

```
这将创建文件 ~/.gitignore_global。现在，你可以像本地 .gitignore 文件一样编辑这个文件。你所有的 Git 仓库都会忽略全局 .gitignore 文件中列出的文件和文件夹。

## 如何取消跟踪已提交的文件

要取消跟踪单个文件，即停止跟踪该文件但不删除它，可以使用：

```
git rm --cached filename
```

要取消跟踪 .gitignore 中的每个文件：

首先，提交任何未提交的代码更改，然后运行：

```
git rm -r --cached
```

这将从索引（暂存区）中移除任何已更改的文件，然后运行：

```
git add .
```
Commit it:

```
git commit -m ".gitignore is now working"
```

要撤销 ```git rm --cached filename```，使用 ```git add filename```



