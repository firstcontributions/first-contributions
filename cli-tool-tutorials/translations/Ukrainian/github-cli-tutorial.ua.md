[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Перші внески

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | Інтерфейс командного рядка GitHub (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|

Це керівництво для нас, нердів, які хочуть робити все у терміналі, і завдяки [Github-CLI](https://cli.github.com/), ми можемо досягти цього, пам'ятаючи, що ваш перший внесок повинен бути цікавим, корисним та мотивувати до подальшої роботи!

Це керівництво трохи складніше, оскільки ми зовсім не використовуємо графічний інтерфейс, але це все ще дуже цікаво і ви точно зможете його виконати крок за кроком!

Перша умова - мати:
- Встановлений Git ([як встановити git](https://git-scm.com/downloads))
- Обліковий запис на Github

Тепер нам потрібно встановити інструмент `github-cli` у нашу систему, виконавши кроки з [офіційної документації](https://github.com/cli/cli#installation)

Після цього нам потрібно увійти до CLI, застосовуючи цю команду:
```bash
gh auth login
```

Дотримуйтесь інструкцій, і ми готові починати!

# Відгалужуємо репозиторій
Це робиться, всього навсього, за допомогою однієї команди:

```bash
gh repo fork firstcontributions/first-contributions
```
**Важливо: Якщо ви хочете одразу клонувати репозиторій, виберіть варіант "yes" **

# Створюємо свою гілку
Ми зробимо цей крок за допомогою git, тому введіть цю команду, замінивши `taras-shevchenko` на ваше ім'я:
```bash
git switch -c add-taras-shevchenko
```

# Вносимо необхідні зміни та записуємо їх 
Тепер ви можете відкрити файл `Contributors.md` в текстовому редакторі і додати до нього своє ім'я. Впишіть своє ім'я десь між початком і кінцем, а потім збережіть файл.

У директорії проекту виконайте команду `git status`, і ви побачите виконані зміни.
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

Додайте ці зміни до гілки, яку ви щойно створили, використовуючи команду `git add`:
`git add Contributors.md`

Тепер запишіть ці зміни за допомогою команди `git commit`:
`git commit -m "Add taras-shevchenko to Contributors list`
замінюючи `taras-shevchenko` на ваше ім'я.

# Відправляємо зміни в GitHub
Відправте свої зміни за допомогою команди `git push`:

```bash
git push origin -u your-branch-name
```

замініть `your-branch-name` ім'ям гілки, яку ви створили раніше.

<details>
<summary><strong>Якщо ви отримаєте помилки під час відправки, натисніть тут:</strong></summary>

- ### Помилка автентифікації
    <pre>remote: Підтримка автентифікації за допомогою пароля була припинена 13 серпня 2021 року. Замість цього використовуйте особистий токен доступу.
    remote: Будь ласка, перегляньте https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ для отримання більш докладної інформації.
    fatal: Автентифікація завершилася помилкою для 'https://github.com/<your-username>/first-contributions.git/'</pre>
    Перейдіть до [посібника GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) щодо створення та налаштування SSH-ключа для вашого облікового запису.

</details>

# Створюємо запит на рецензування своїх змін
Тепер, запускаючи цю команду у директорії нашого репозиторію, ми зможемо створити запит на витяг (pull request) для рецензування.

```bash
gh pr create --repo firstcontributions/first-contributions
```

Після цього подайте запит на витяг.

Ви можете використати команду `gh status`, щоб побачити ваш вищезгаданий запит на витяг у дії.

## Що далі?

Вітаємо! Ви щойно завершили стандартний робочий процес _fork -> clone -> edit -> pull request_, який часто зустрічається серед співавторів open source проектів!

Відзначте свій внесок та поділіться ним з друзями та підписниками, перейшовши до [веб-додатку](https://firstcontributions.github.io/#social-share).

Ви можете приєднатися до нашої [команди у Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA), якщо вам потрібна допомога чи у вас є які-небудь питання.

Тепер ви можете розпочати робити ваш внесок до інших проектів. Ми склали список проектів з легкими проблемами, з яких ви можете почати. [Посилання до списку проектів](https://firstcontributions.github.io/#project-list).

### [Додатковий матеріал](https://github.com/firstcontributions/first-contributions/blob/main/additional-material/git_workflow_scenarios/additional-material.md)

## Навчальні посібники з використанням інших інструментів

[Повернутися на головну сторінку](https://github.com/firstcontributions/first-contributions/blob/main/translations/README.ua.md#%D1%96%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D1%96%D1%97-%D0%B4%D0%BB%D1%8F-%D1%96%D0%BD%D1%88%D0%B8%D1%85-%D1%96%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%96%D0%B2)
