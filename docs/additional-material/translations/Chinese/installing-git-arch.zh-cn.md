# 在 Arch Linux 上安装 Git

要在 Arch Linux 上安装 Git，可以使用包管理器 pacman。首先，打开终端并使用以下命令更新系统：

```shell
$ sudo pacman -Syu
```

接下来，运行以下命令安装 Git：

```shell
$ sudo pacman -S git
```

要确认 Git 是否正确安装，运行以下命令：

```shell
$ git --version
```

你应该会看到类似以下的输出：

```shell
Output
$ git version 2.34.1
```

# 设置 Git

配置可以通过使用 git config 命令来完成。
具体来说，你需要提供你的名字和电子邮件地址，因为 Git 会将这些信息嵌入到你做的每个提交中。
你可以通过输入以下命令来添加这些信息：

现在我们已经完成了 Git 的安装，让我们使用 "git config" 命令配置 Git 以供首次使用。
我们需要确保你的用户名和电子邮件地址设置正确。要设置它们，使用以下命令：

```shell
$ git config --global user.name "Your Name"
$ git config --global user.email "youremail@domain.com"
```

你可以通过在终端中输入以下命令来显示所有已设置的配置项：

```shell
$ git config --list
```

如果所有配置字段已按照你的需求设置，输出应该类似于：

```shell
user.name=Your Name
user.email=youremail@domain.com
```

# 持久化 Git 凭证

默认情况下，Git 每次与远程仓库交互时都会提示你重新输入用户名和密码。你可以配置 Git 来缓存或存储你的凭证，以避免这种情况。以下是两种常用的方法：

### 1. 凭证缓存

Git 可以将你的凭证暂时存储在内存中，这样你就不需要频繁地重新输入它们。运行以下命令启用凭证缓存：

```shell
$ git config --global credential.helper cache
```

默认情况下，凭证会缓存 15 分钟。要调整超时时间（例如，1 小时），可以使用：

```shell
$ git config --global credential.helper 'cache --timeout=3600'
```

---

### 2. 凭证存储

如果你更倾向于将凭证永久存储为明文（不太安全，但方便），可以使用以下命令：

```shell
$ git config --global credential.helper store
```

使用此方法时，你的凭证将以明文形式保存在 `~/.git-credentials` 文件中。特别是在共享或公共计算机上使用此方法时，请小心操作。