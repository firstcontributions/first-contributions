# 在 Ubuntu OS 上安装 Git

默认情况下，Git 很可能已经在你的 Ubuntu 操作系统中安装好了。你可以通过打开终端并输入以下命令来确认：

```shell
$ git --version
```

如果你看到类似下面的输出，那么恭喜你！你已经成功安装了 Git。

```shell
Output
$ git version 2.34.1
```

如果适用于你，接下来可以继续进行 Git 配置,去[设置 Git](#设置-Git)。

如果输出中没有显示 Git 版本号，你仍然可以通过 Ubuntu 的 APT 包管理器来安装 Git。

首先，通过使用 apt 包管理工具更新本地包索引。返回到你的终端并输入以下命令。

```shell
$ sudo apt update
```

完成后，输入以下命令来安装 Git：

```shell
$ sudo apt install git
```

你可以通过运行以下命令并检查是否收到相关输出，来确认 Git 是否已正确安装：

```shell
$ git --version
```

```shell
Output
$ git version 2.34.1
```

Git 成功安装后，接下来可以配置 Git。

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

...

# 持久化 Git 凭证

默认情况下，Git 会在每次你推送到远程仓库时要求你输入用户名和密码。
在 Git 中，你可以配置凭证缓存，以避免每次输入用户名和密码。以下是实现这一目标的几种方法：

1. 凭证缓存：Git 提供了一个凭证缓存系统，可以在指定的时间内将你的凭证存储在内存中。这样，你就不需要每次与远程仓库交互时重新输入凭证。

要启用凭证缓存，你可以使用以下命令：

```shell
$ git config --global credential.helper cache
```

默认情况下，Git 会将凭证缓存 15 分钟。你可以通过指定 --timeout 选项并跟上所需的秒数来调整缓存超时时间。

例如，要将缓存超时设置为 1 小时（3600 秒），可以使用：

```shell
$ git config --global credential.helper 'cache --timeout=3600'

```

2. 凭证存储：这将 Git 的凭证助手设置为 "store"。使用这个凭证助手时，Git 会将远程仓库的凭证存储在磁盘上的一个明文文件中。这种方法是最简单的，但存储明文凭证的方式也是最不安全的。

```shell
$ git config --global crednetial.helper store
```

使用存储凭证助手时，输入的凭证会永久保存在 Linux 或 macOS 上的 ~/.git-credentials 文件中，或 Windows 上的 %USERPROFILE%\.git-credentials 文件中。这些凭证将以明文格式存储，这意味着如果有人获取到该文件，就可以读取凭证。

使用存储凭证助手的优点是，你每次与远程仓库交互时，不需要再次输入凭证。然而，特别是在使用共享或公共计算机时，请注意存储明文凭证的安全隐患。
