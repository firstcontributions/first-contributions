[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
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

```bash
git clone "ссылка на репозиторий"
```

Где "ссылка на репозиторий" (без кавычек) - это ссылка на ваш репозиторий. Посмотрите предыдущие шаги, чтобы получить эту ссылку.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="скопируйте ссылку в буфер обмена" />

Например:

```bash
git clone https://github.com/ваш-логин/first-contributions.git
```

Где `ваш логин` ваш логин на github'e. Таким образом вы копируете репозиторий 'first-contributions' с GitHub на ваш ПК.

## Создайте ветку

Перейдите в каталог репозитория на вашем компьютере, если вы еще не там.

```bash
cd first-contributions
```

Теперь создайте ветку с помощью команды `git checkout`

```bash
git checkout -b <add-your-name>
```

Например:

```bash
git checkout -b add-alonzo-church
```

(Синтаксически не требуется, чтобы название ветки содержало слово _add_, но это оправдано, поскольку подчеркивает назначение этой ветки: добавить ваше имя в список.)

## Внесите необходимые изменения и создайте коммит

Теперь откройте файл `Contributors.md` в вашем текстовом редакторе, впишите ваше имя и сохраните файл. Если вы перейдёте в директорию проекта и выполните `git status`, вы увидите изменения. Добавьте эти изменения с помощью команды `git add`.

```bash
git add Contributors.md
```

Теперь закоммитьте данные изменения с помощью команды `git commit`.

```bash
git commit -m "Add <your-name> to Contributors list"
```

Измените `<your-name>` на ваше имя

## Запушьте изменения на github

Запушьте ваши изменения с помощью `git push`

```bash
git push origin <add-your-name>
```

Измените `<add-your-name>` на имя ветки, которую вы создали ранее.

## Подтвердите изменения для ревью

Если вы зайдете в свой репозиторий на GitHub, вы увидите кнопку `Compare & pull request`. Нажмите на нее.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Создать запрос на изменение" />

Теперь подтвердите пулл-реквест.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Скоро я произведу объединение всех ваших изменений с основной веткой данного проекта. Вы получите сообщение по электронной почте, когда изменения будут приняты (смержены).

Основная ветка вашего репозитория не будет изменена. Для синхронизации выполните шаги, расположенные ниже.

## Синхронизируйте вашу ветку с данным репозиторием

Прежде всего перейдите в основную ветку:

```bash
git checkout main
```

Затем добавьте url моего репозитория в поле `upstream remote url`:

```bash
git remote add upstream https://github.com/Roshanjossey/first-contributions
```

Таким образом мы сообщим git'у, что существует другая версия данного проекта по определенной ссылке, и мы ее считаем мастером. Как только изменения смержены, подгрузите новую версию моего репозитория.

```bash
git fetch upstream
```

Таким образом мы забрали все изменения в моём ответвлении (upstream remote). После, вам нужно смержить новую версию моего репозитория с вашей мастер-веткой.

```bash
git rebase upstream/main
```

Так вы применяете все изменения, которые вы подтянули к вашей мастер-ветке. Если вы запушите сейчас мастер-ветку, ваше ответвление тоже будет содержать изменения.

```bash
git push origin main
```

Обратите внимание, что вы пушите в удаленный репозиторий origin.

На этом этапе я объединил вашу ветку `<add-your-name>` со своей мастер-веткой, а вы объединили свою мастер-ветку с моей. Ваша ветка больше не нужна, вы можете удалить её:

```bash
git branch -d <add-your-name>
```

Так же можете удалить её версию в удалённом репозитории:

```bash
git push origin --delete <add-your-name>
```

Это совершенно не обязательно, но название этой ветки отражает её довольно специфическое назначение. И продолжительность её жизни может быть соответствующе короткой.

## Использование других инструментов

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
