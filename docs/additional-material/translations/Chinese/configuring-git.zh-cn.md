# 配置 git

第一次使用 git 提交时，你可能会看到如下提示：

```bash
$ git commit
*** 请告诉我你是谁。

运行

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

来设置你账户的默认身份。
如果只想在当前仓库设置身份，省略 --global。
```

Git 在创建提交时需要知道你是谁。当你在团队中协作时，你应该能够看到是谁修改了项目的哪些部分以及何时修改的，因此，Git 设计时就要求每个提交都与一个名字和电子邮件地址相关联。

有多种方法可以为 `git commit` 命令提供你的电子邮件和用户名，下面我们将介绍几种常用的方法。

### 全局配置 

当你将某个配置存储在全局配置中时，它在你工作的所有仓库中都是可访问的。这是推荐的方式，并且适用于大多数使用场景。

要将某个配置存储在全局配置中，你可以使用以下 `config` 命令：

`$ git config --global <variable name> <value>`

对于用户信息，我们可以运行：

```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### 仓库配置

顾名思义，这些配置仅作用于当前仓库。如果你想在某个特定仓库中提交，例如工作项目，并使用你公司的电子邮件地址，你可以使用这种方法。

要将某个配置存储在仓库配置中，可以在 `config` 命令中省略 `--global` 标志，如下所示：

`$ git config <variable name> <value>`

对于用户信息，我们可以运行：

```
$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
```

### 命令行配置

这些配置仅作用于当前命令。所有 git 命令在动作动词之前都可以使用 `-c` 参数来设置临时配置数据。

要在命令行配置中存储某个配置，按如下方式运行命令：

`$ git -c <variable-1>=<value> -c <variable-2>=<variable> <command>`

在我们的例子中，我们将提交命令改为：

`git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Your commit message"`

### 配置优先级说明

在这里描述的三种方法中，优先级顺序是 `command-line > repository > global`。这意味着，如果同一个变量在命令行和全局中都有配置，命令行的值将用于该操作。

### 超出用户信息

到目前为止，我们仅在配置中处理了用户信息。然而，还有许多其他配置选项。以下是一些常见的配置：

1. `core.editor` - 指定用于编写提交消息等的编辑器名称。
2. `commit.template` - 指定系统中作为初始提交模板的文件。
3. `color.ui` - 指定是否在 git 输出中使用颜色的布尔值。

为了便于理解，我们简化了一些细节。如果你想进一步了解，访问 [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)。


