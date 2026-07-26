# Gitflow

Gitflow 是由 Vincent Driessen 创建的 Git 分支模型。本文将讨论 Gitflow 的要求和用例。<br />
Gitflow 工作流定义了一个围绕项目发布而设计的严格分支模型，提供了一个强大的框架来管理大型项目。Gitflow 特别适用于具有计划发布周期的项目以及 DevOps 最佳实践中的持续交付。它为不同的分支分配了非常具体的角色，并定义了它们应该如何以及何时互动。它使用独立的分支来准备、维护和记录发布。


## 实现

1. **Develop 和 Master Branches**：与单一的 master 分支不同，Git Flow 使用两个分支来记录项目的历史。它基于两个具有无限生命周期的主分支，即 master 和 develop：
  - **Master Branch**：master 分支包含生产代码并存储官方的发布历史。
  - **Develop Branch**：develop 分支包含预生产代码，作为功能的集成分支。
  - **创建 Develop Branch**：<br />
    不使用 Gitflow 扩展时：
    ```
    git branch develop
    git push -u origin develop
    ```
    使用 Gitflow 扩展时：当使用 gitflow 扩展库时，在现有的仓库中执行 `git flow init` 将创建 develop 分支。
    ```
    git flow init
    ```
2. **Feature Branch**：每个新功能应该放在它自己的分支上，可以推送到中央仓库以备份或协作。Feature 分支使用最新的 develop 作为其父分支。当功能完成时，它会合并回 develop。功能分支永远不应直接与 master 分支交互。
  - **创建 Feature Branch**： <br />
    不使用 git-flow 扩展时：
    ```
    git checkout develop
    git checkout -b feature_branch
    ```
    使用 gitflow 扩展时：
    ```
    git flow feature start feature_branch
    ```
  - **完成 Feature Branch**： <br />
    不使用 git-flow 扩展时：
    ```
    git checkout develop
    git merge feature_branch
    ```
    使用 git-flow 扩展时：
    ```
    git flow feature finish feature_branch
    ```
3. **Release Branch**：当 develop 分支包含足够的功能用于发布（或者接近预定的发布日期）时，我们会从 develop 分支派生出一个 release 分支。创建这个分支标志着下一个发布周期的开始，因此在此之后不能再添加新功能——只能添加 bug 修复、文档生成和其他与发布相关的任务。Release 分支应从 develop 分支派生，并必须同时合并到 master 和 develop 分支。<br />
使用专门的分支来准备发布使得一个团队可以在 polishing 当前发布时，另一个团队继续为下一个发布开发新功能。
  - **创建 Release Branch**： <br />
    不使用 git-flow 扩展时：
    ```
    git checkout develop
    git checkout develop
    git checkout -b release/0.1.0
    ```
    使用 git-flow 扩展时：
    ```
    git flow release start 0.1.0
    ```
    切换到新分支 'release/0.1.0'
  - **完成 Release Branch**： <br />
    不使用 git-flow 扩展时：
    ```
    git checkout master
    git merge release/0.1.0
    ```
    使用 git-flow 扩展时：
    ```
    git flow release finish 0.1.0
    ```
4. **Hotfix Branch**：维护或“hotfix”分支用于快速修复生产发布。Hotfix 分支对于立即解决 master 分支中的不希望出现的问题非常必要。Hotfix 分支与 release 分支和 feature 分支类似，不同之处在于它是基于 master 分支而非 develop 分支派生的。这是唯一一个应直接从 master 分支派生的分支。修复完成后，它应该同时合并到 master 和 develop（或当前的 release 分支），并且 master 分支应该打上更新的版本号标签。
  - **创建 Hotfix Branch**： <br />
    不使用 git-flow 扩展时：
    ```
    git checkout master
    git checkout -b hotfix_branch
    ```
    使用 git-flow 扩展时：
    ```
    git flow hotfix start hotfix_branch
    ```
  - **完成 Hotfix Branch**： <br />
    不使用 git-flow 扩展时：
    ```
    git checkout master
    git merge hotfix_branch
    git checkout develop
    git merge hotfix_branch
    ```
    使用 git-flow 扩展时：
    ```
    git branch -D hotfix_branch
    git flow hotfix finish hotfix_branch
    ```


## 优势

- 确保项目生命周期中的任何时刻分支状态保持清晰。
- 分支的命名约定遵循系统化模式，使其更容易理解。
- 支持大多数常用的 git 工具和扩展。
- 适合在生产中维护多个版本。
- 非常适合基于发布的软件工作流。
- 提供了专门用于生产热修复的渠道。


## 劣势

- Git 历史记录变得难以阅读。
- master 和 develop branch的分割被认为是冗余的，并使持续交付/集成变得更加困难。
- 不推荐用于维护生产中的单一版本。


## 总结

我们在这里讨论了 Git Flow 工作流。Git Flow 是你和你的团队可以使用的多种 Git 工作流之一。让我们总结一下 Git Flow 的整个工作流：
1. 从 master 创建一个 develop 分支。
2. 从 develop 创建功能分支。
3. 当功能完成时，将其合并到 develop 分支。
4. 从 develop 创建一个 release 分支。
5. 当 release 分支完成时，将其合并到 develop 和 master。
6. 如果 master 中发现问题，则从 master 创建一个 hotfix 分支。
7. 一旦 hotfix 完成，它将被合并到 develop 和 master。
