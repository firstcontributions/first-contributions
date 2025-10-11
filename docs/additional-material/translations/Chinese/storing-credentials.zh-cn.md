# 存储凭据（用户名与密码）

你可能遇到过这样的烦恼——每次访问仓库都要输入用户名和密码，这很麻烦，而且若耗时过长还会打断你的工作流。  
但其实没必要如此繁琐。

这里我们介绍一种常见的方式： [git credential cache](https://git-scm.com/docs/git-credential-cache)。

**注意：** 请遵循你所在单位或学校的安全策略。

## 凭据缓存（Caching）

我们可以使用 Git 的 credential cache 来存储用户名和密码。

**警告：** 此方法会将凭据以*明文*形式保存在你电脑的硬盘上。  
任何人都可以访问该文件，比如恶意的 NPM 模块。

### 全局凭据缓存

如果你希望为所有仓库启用凭据缓存，只需执行以下命令：

```
$ git config --global credential.helper cache
```

**提醒：** 请遵循你所在单位或学校的安全策略。

### 仓库级别的凭据缓存

如果你只想为当前仓库启用缓存，可以使用以下命令：

```
$ git config credential.helper cache
```

**提醒：** 请遵循你所在单位或学校的安全策略。

### 缓存超时时间

如果不指定缓存时间，凭据可能会被永久保留在内存中。  
你可以通过以下命令设置缓存的持续时间（单位为秒）：

```
git config credential.helper 'cache --timeout=<timeout>'
```

使用此 helper，凭据只会存储在内存中，不会写入磁盘，且在指定时间后会自动清除。  
默认超时时间是 900 秒（15 分钟）。

#### 参考资料：
[Stack Overflow](https://stackoverflow.com/questions/35942754/how-can-i-save-username-and-password-in-git)

### [附加材料](additional-material.md)