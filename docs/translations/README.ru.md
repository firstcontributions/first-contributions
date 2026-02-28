[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Первый вклад

Этот проект призван упростить и помочь новичкам сделать их первый вклад. Если вы хотите сделать свой первый вклад, следуйте шагам ниже.

_Если вы не уверены в работе с командной строкой, [вот руководства с использованием графических инструментов.](#руководства-с-использованием-других-инструментов)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="форк репозитория" />

#### Если у вас не установлен git, [установите его](https://docs.github.com/ru/get-started/quickstart/set-up-git).

## Форкните этот репозиторий

Форкните этот репозиторий, нажав на кнопку fork в верхней части этой страницы.
Это создаст копию этого репозитория в вашем аккаунте.

## Клонируйте репозиторий

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="клонирование репозитория" />

Теперь клонируйте форкнутый репозиторий на свой компьютер. Перейдите в свой аккаунт GitHub, откройте форкнутый репозиторий, нажмите на кнопку code, затем на вкладку SSH и нажмите на иконку _копировать URL в буфер обмена_.

Откройте терминал и выполните следующую git команду:

```bash
git clone "скопированный URL"
```

где "скопированный URL" (без кавычек) — это URL этого репозитория (вашего форка этого проекта). Смотрите предыдущие шаги, чтобы получить URL.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="копировать URL в буфер обмена" />

Например:

```bash
git clone git@github.com:ваше-имя/first-contributions.git
```

где `ваше-имя` — это ваше имя пользователя на GitHub. Здесь вы копируете содержимое репозитория first-contributions с GitHub на свой компьютер.

## Создайте ветку

Перейдите в директорию (папку) репозитория на вашем компьютере (если вы ещё не там):

```bash
cd first-contributions
```

Теперь создайте ветку, используя команду `git switch`:

```bash
git switch -c имя-вашей-новой-ветки
```

Например:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>Если вы получили ошибку при использовании git switch, нажмите здесь:</strong> </summary>

Если появляется сообщение об ошибке "Git: `switch` is not a git command. See `git –help`", скорее всего, вы используете старую версию git.

В этом случае попробуйте использовать `git checkout`:

```bash
git checkout -b имя-вашей-новой-ветки
```

</details>

## Внесите необходимые изменения и закоммитьте их

Теперь откройте файл `Contributors.md` в текстовом редакторе и добавьте в него своё имя. Не добавляйте его в начало или конец файла. Поместите его где-нибудь между ними. Теперь сохраните файл.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Если вы перейдёте в директорию (папку) проекта и выполните команду `git status`, вы увидите изменения.

Добавьте эти изменения в ветку, которую вы только что создали, используя команду `git add`:

```bash
git add Contributors.md
```

Теперь закоммитьте эти изменения, используя команду `git commit`:

```bash
git commit -m "Add ваше-имя to Contributors list"
```

заменив `ваше-имя` на своё имя.

## Отправьте изменения на GitHub

Отправьте свои изменения, используя команду `git push`:

```bash
git push -u origin имя-вашей-ветки
```

заменив `имя-вашей-ветки` на имя ветки, которую вы создали ранее.

<details>
<summary> <strong>Если вы получили ошибку при отправке, нажмите здесь:</strong> </summary>

- ### Ошибка аутентификации
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;ваше-имя&gt;/first-contributions.git/'</pre>
  Перейдите к [руководству GitHub](https://docs.github.com/ru/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) по генерации и настройке SSH ключа для вашего аккаунта.

  Также вы можете выполнить 'git remote -v', чтобы проверить адрес удалённого репозитория.
  
  Если он выглядит примерно так:
  <pre>origin	https://github.com/ваше-имя/ваш-репозиторий.git (fetch)
  origin	https://github.com/ваше-имя/ваш-репозиторий.git (push)</pre>
  
  измените его с помощью этой команды:
  ```bash
  git remote set-url origin git@github.com:ваше-имя/ваш-репозиторий.git
  ```
  Иначе вам всё равно будет предлагаться ввести имя пользователя и пароль, и вы получите ошибку аутентификации.
</details>

## Отправьте изменения на проверку

Если вы перейдёте в свой репозиторий на GitHub, вы увидите кнопку `Compare & pull request`. Нажмите на неё.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="сравнить и создать pull request" />

Теперь отправьте pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="отправить pull request" />

Вскоре я объединю все ваши изменения с основной веткой этого проекта. Вы получите уведомление по электронной почте, когда изменения будут объединены.

## Что дальше?

Поздравляем! Вы только что завершили стандартный процесс _форк -> клонирование -> редактирование -> pull request_, с которым вы часто будете сталкиваться как контрибьютор!

Отпразднуйте свой вклад и поделитесь им с друзьями и подписчиками, перейдя в [веб-приложение](https://firstcontributions.github.io/#social-share).

Если вы хотите больше практики, попробуйте [code contributions](https://github.com/roshanjossey/code-contributions).

Теперь давайте начнём вносить вклад в другие проекты. Мы составили список проектов с простыми задачами, с которых вы можете начать. Посмотрите [список проектов в веб-приложении](https://firstcontributions.github.io/#project-list).

### [Дополнительные материалы](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Руководства с использованием других инструментов

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |