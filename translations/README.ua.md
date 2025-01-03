[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Перший внесок

Цей проект спрямований на те, щоб спростити та спрямувати шлях новачків, які роблять свій перший внесок. Якщо ви хочете зробити свій перший внесок, виконайте наведені нижче дії.

_Якщо ви не вмієте працювати з командним рядком, [ось навчальні посібники з використанням інструментів GUI.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Якщо ви ще не встановили git, тоді [зробіть це](https://help.github.com/articles/set-up-git/).

## Форкніть репозиторій

Форкніть свою власну копію цього репозиторію, натиснувши кнопку `fork` вгорі цієї сторінки.
Таким чином, ви створите копію цього репозиторію у вашому акаунті.

## Клонуйте репозиторій

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Тепер клонуйте цей репозиторій на ваш комп’ютер. Натисніть на кнопку `clone`, а потім - на іконку `copy to clipboard`.

Відкрийте термінал і виконайте наступні команди:

```bash
git clone "посилання, яке ви щойно скопіювали"
```

де `посилання, яке ви щойно скопіювали` (без лапок) - адреса цього репозиторію. Дивіться попередній крок для того, щоб отримати цю адресу.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Наприклад:
```bash
git clone https://github.com/this-is-you/first-contributions.git
```

де `this-is-you` - ваш нікнейм з GitHub. Таким чином, ви копіюєте вміст репозиторію з GitHub, в який збираєтесь зробити внесок, на ваш комп’ютер.

## Створюємо гілку

Перейдіть в директорію з репозиторієм на вашому комп’ютері (якщо ви ще цього не зробили):

```bash
cd first-contributions
```

Тепер створюємо гілку за допомогою команди `git checkout`:

```bash
git checkout -b <add-your-name>
```

Наприклад:

```bash
git checkout -b add-petro-church
```

(Назва гілки не повинна обов’язково містити слово *add*, але це має сенс, якщо майбутні зміни передбачають додавання чогось, наприклад, вашого імені у список контрибуторів.)

## Робимо необхідні зміни та записуємо їх в репозиторій

Тепер відкриваємо файл `Contributors.md` в текстовому редакторі та додаємо ваше ім’я, а потім зберігаємо файл. Якщо ви перейдете в директорію проєкту і виконаєте команду `git status`, ви побачите зміни. Додайте ці зміни до гілки, яку ви тільки що створили, за допомогою команди `git add`:

```bash
git add Contributors.md
```

Тепер запишіть ці зміни за допомогою команди `git commit`:

```bash
git commit -m "Add <your-name> to Contributors list"
```

замініть `<your-name>` своїм іменем.

## Відправляємо зміни в GitHub

Відправте зміни на віддалений репозиторій в GitHub за допомогою команди `git push`:

```bash
git push -г origin <your-branch-name>
```

Замініть `<your-branch-name>` назвою гілки, яку ви створили раніше.

<details>
<summary> <strong>Якщо під час натискання виникають помилки, натисніть тут:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Перейдіть до [туторіалу GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) щодо створення та налаштування ключа SSH для вашого облікового запису.

</details>

## Відправляємо зміни на перевірку

Коли ви перейдете до свого репозиторію в GitHub, ви побачите кнопку `Compare & pull request`. Сміливо натисніть на неї.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Тепер зміни відправлені на перевірку і затвердження.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Згодом я об’єднаю ваші запропоновані зміни з основною гілкою цього репозиторію. Ви отримаєте повідомлення, коли це буде зроблено.

## Що далі?

Вітаю! Ви щойно виконали стандартний робочий процес _fork -> clone -> edit -> pull request_, з яким ви часто стикаєтеся як контрибутор!

Відзначте свій внесок і поділіться ним із друзями та читачами, перейшовши до [веб-програми](https://firstcontributions.github.io/#social-share).

Ви можете приєднатися до нашої команди Slack, якщо вам потрібна допомога або якщо виникнуть запитання. [Приєднайтеся до команди Slack](https://firstcontributors.slack.com/join/shared_invite/zt-29qhyr9lt-Bi7WLbgGIFqV7aCEG_grvg#/shared-invite/email).

Тепер давайте почнемо робити внески в інші проекти. Ми склали список проектів із простими проблемами, з яких ви можете почати. Перегляньте [список проектів у веб-додатку](https://firstcontributions.github.io/#project-list).

### [Додаткові матеріали](additional-material/git_workflow_scenarios/additional-material.md)

## Інструкції для інших інструментів

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

<p>Цей проект підтримується:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
