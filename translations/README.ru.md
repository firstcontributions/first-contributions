[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Первый вклад в проект

Сложно. Всегда сложно начинать что-то с самого начала. Довольно неприятно совершать ошибки, особенно если вы работаете в команде. Весь open source состоит из сотрудничества и совместной работы. Мы хотим облегчить первые шаги в обучении и сотрудничестве начинающим разработчикам.

Чтение статей и учебников может помочь, но что может быть лучше, чем настоящий практический опыт, без риска что-либо испортить? Цель этого проекта - должным образом направить молодых новобранцев, а также предоставить им возможность сделать их первый вклад. Помните: чем меньше вы напряжены, тем лучше вы учитесь. Если вы ищете возможность осуществить свой первый вклад, просто следуйте простым шагам, расположенным ниже. Обещаем, будет интересно.

Если вам нужна помощь с командной строкой, [это руководство использует инструменты графической операционной системы (GUI).](#Использование-других-инструментов)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="сделать ветку" />

Если у вас не установлен git на компьютере, [ установите его. ](https://help.github.com/articles/set-up-git/)

## Создайте ветку

Создайте собственную ветку, нажав на кнопку `fork` сверху этой страницы. Таким образом, вы создадите копию этого репозитория в своем аккаунте.

## Клонируйте репозиторий

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="клонировать репозиторий" />

Теперь клонируйте ваш репозиторий на ПК. Нажмите на кнопку `clone`, а затем на иконку `copy to clipboard`, чтобы скопировать ссылку.

Откройте терминал и запустите следующую git команду:

```
git clone "ссылка на репозиторий"
```

Где "ссылка на репозиторий" (без кавычек) - это ссылка на ваш репозиторий. Посмотрите предыдущие шаги, чтобы получить эту ссылку.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="скопируйте ссылку в буфер обмена" />

Например:

```
git clone https://github.com/ваш-логин/first-contributions.git
```

Где `ваш логин` ваш логин на github'e. Таким образом вы копируете репозиторий 'first-contributions' с GitHub на ваш ПК.

## Создайте ветку

Перейдите в каталог репозитория на вашем компьютере, если вы еще не там.

```
cd first-contributions
```

Теперь создайте ветку с помощью команды `git checkout`

```
git checkout -b <add-your-name>
```

Например:

```
git checkout -b add-alonzo-church
```

(Синтаксически не требуется, чтобы название ветки содержало слово _add_, но это оправдано, поскольку подчеркивает назначение этой ветки: добавить ваше имя в список.)

## Внесите необходимые изменения и создайте коммит

Теперь откройте файл `Contributors.md` в вашем текстовом редакторе, впишите ваше имя и сохраните файл. Если вы перейдёте в директорию проекта и выполните `git status`, вы увидите изменения. Добавьте эти изменения с помощью команды `git add`.

```
git add Contributors.md
```

Теперь закоммитьте данные изменения с помощью команды `git commit`.

```
git commit -m "Add <your-name> to Contributors list"
```

Измените `<your-name>` на ваше имя

## Запушьте изменения на github

Запушьте ваши изменения с помощью `git push`

```
git push origin <add-your-name>
```

Измените `<add-your-name>` на имя ветки, которую вы создали ранее.

## Подтвердите изменения для ревью

Если вы зайдете в свой репозиторий на GitHub, вы увидите кнопку `Compare & pull request`. Нажмите на нее.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Теперь подтвердите пулл-реквест.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Скоро я произведу объединение всех ваших изменений с основной веткой данного проекта. Вы получите сообщение по электронной почте, когда изменения будут приняты (смержены).

Основная ветка вашего репозитория не будет изменена. Для синхронизации выполните шаги, расположенные ниже.

## Синхронизируйте вашу ветку с данным репозиторием

Прежде всего перейдите в основную ветку:

```
git checkout main
```

Затем добавьте url моего репозитория в поле `upstream remote url`:

```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```

Таким образом мы сообщим git'у, что существует другая версия данного проекта по определенной ссылке, и мы ее считаем мастером. Как только изменения смержены, подгрузите новую версию моего репозитория.

```
git fetch upstream
```

Таким образом мы забрали все изменения в моём ответвлении (upstream remote). После, вам нужно смержить новую версию моего репозитория с вашей мастер-веткой.

```
git rebase upstream/main
```

Так вы применяете все изменения, которые вы подтянули к вашей мастер-ветке. Если вы запушите сейчас мастер-ветку, ваше ответвление тоже будет содержать изменения.

```
git push origin main
```

Обратите внимание, что вы пушите в удаленный репозиторий origin.

На этом этапе я объединил вашу ветку `<add-your-name>` со своей мастер-веткой, а вы объединили свою мастер-ветку с моей. Ваша ветка больше не нужна, вы можете удалить её:

```
git branch -d <add-your-name>
```

Так же можете удалить её версию в удалённом репозитории:

```
git push origin --delete <add-your-name>
```

Это совершенно не обязательно, но название этой ветки отражает её довольно специфическое назначение. И продолжительность её жизни может быть соответствующе короткой.

## Использование других инструментов

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

## Что дальше?

Ниже несколько популярных репозиториев, где вы можете найти задания для новичков. Вперёд, перейдите в репозитории, чтобы узнать больше.

| [![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22) | [![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                       | [<img width="100" src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)    | [![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)         | [![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)      | [<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie) | [<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)          | [![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)                                                                | [Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                                                                                      | [react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)                                                                                         | [habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                         | [scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                    | [Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)                                                                                                                                                                        | [numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)                                                                                                 | [elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)                                                                |
| [![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)             | [![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)                                                                              | [![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)                         | [![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)        | [![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                        | [![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)                                                                                                 | [![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer) | [![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)                           |
| [homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)                                                                            | [Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)                                                                                                                                             | [vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)                                                                                        | [Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)                                                                       | [OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                                      | [PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)                                                                                                                                                                 | [coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)                                                                 | [moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)                                                                                          |
| [![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)                | [![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                | [![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22) | [![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only) | [![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22) | [![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)                                                                                                               | [![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                               | [<img width="100" src="https://cdn.worldvectorlogo.com/logos/brackets-1.svg">](https://github.com/adobe/brackets/labels/Starter%20bug)                     |
| [ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)                                                                               | [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                                                                               | [webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)                                                                | [hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                                | [pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)                                                                | [neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)                                                                                                                                                                              | [babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                                                              | [brackets](https://github.com/adobe/brackets/labels/Starter%20bug)                                                                                                                     |
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)    | [<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/public/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)                                                                   | [Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)                                                                                         |
