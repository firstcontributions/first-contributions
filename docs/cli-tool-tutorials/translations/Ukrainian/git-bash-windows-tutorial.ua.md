[![Любов до Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![Ліцензія: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Помічники Open Source](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Перші внески

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Версія з Git Bash |
| ------------------------------------------------------------------------------------------------------------------ | ----------------- |

Це складно. Завжди складно робити щось уперше. Особливо, коли ви працюєте у команді — помилятися завжди некомфортно. Але open source — це саме про співпрацю та командну роботу. Ми хотіли спростити спосіб, у який новачки в open-source навчаються та роблять свій перший внесок.

Читати статті й дивитися відеоуроки корисно, але немає нічого кращого, ніж спробувати на практиці без ризику щось зіпсувати. Цей проєкт має на меті зробити зрозумілий посібник і спростити спосіб, у який новачки роблять свій перший внесок. Пам’ятайте: чим спокійніше вам, тим краще ви навчаєтесь. Якщо ви хочете зробити свій перший внесок — просто дотримуйтесь інструкцій нижче. Обіцяємо — це буде весело!

Якщо у вас немає Git Bash на Windows, [встановіть його](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## Форкніть цей репозиторій

Натисніть кнопку Fork у верхньому правому куті цієї сторінки.
Це створить копію репозиторію у вашому акаунті.

## Клонуйте репозиторій

Тепер клонуйте репозиторій на ваш комп'ютер.

ВАЖЛИВО: НЕ КЛОНУЙТЕ ОРИГІНАЛЬНИЙ РЕПОЗИТОРІЙ. Перейдіть до вашого форку і клонуте його.

Щоб клонувати, натисніть на "Code" і скопіюйте запропонований рядок.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

Відкрийте програму git bash, яку ви щойно встановили. Вона має виглядати як на наступній картинці, якщо ви використовуєте операційну систему Windows.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />

Перейдіть до папки, куди хочете зберегти проєкт, використовуючи наступну команду:

```bash
cd <папка>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />

Вставте скопійований раніше рядок і виконайте команду клонування:

```bash
git clone <url-репозиторію>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

Перейдіть у директорію репозиторію та відкрийте його у VS Code для редагування.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## Створіть гілку (branch)

Використайте наступну просту команду для створення гілки. Ця команда не тільки створює нову гілку, а також переходить на цю гілку.

```bash
git checkout -b <назва-гілки>
```

Назвіть свою гілку у форматі `<add-your-name>`, наприклад: `add-james-smith`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="create a branch" />

## Зробіть необхідні зміни і зафіксуйте їх (commit)

Відкрийте файл `Contributors.md` у текстовому редакторі, додайте ваше ім'я внизу сторінки і збережіть файл:

Приклад: якщо ваше ім’я — James Smith, результат повинен виглядати так.

\[James Smith](https://github.com/jamessmith)

Перевірте зміни командою:

```bash
git status
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="check the status" />

Зафіксуйте ці зміни:

Спочатку додайте зміну, яку ви зробили, до області індексації (staging area), використовуючи команду:

```bash
git add ім'я_файлу
```

Потім напишіть повідомлення до коміту за допомогою цієї команди:

```bash
git commit -m "Add <ваше-ім'я> to Contributors list"
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit changes" />

Щоб перевірити історію комітів:

```bash
git log --oneline
```

## Відправте зміни на GitHub

Коли ви завершите виконання наведених вище кроків, ви можете надіслати свої зміни за допомогою цієї команди:

```bash
git push origin <назва-гілки>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-push.png" alt="push changes" />

## Надішліть запит для перевірки

Перейдіть до вашого репозиторію на GitHub. Ви побачите кнопку "Compare & pull request". Натисніть її.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

Після цього відправте pull request.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

Незабаром ваші зміни буде об'єднано з основною гілкою проєкту. Ви отримаєте сповіщення електронною поштою після злиття вашої гілки з основною.

## Що далі?

Вітаємо! Ви щойно завершили стандартний процес: _fork -> clone -> edit -> PR_!

Поділіться своєю участю з друзями або підпишіться на нашу спільноту [web app](https://firstcontributions.github.io#social-share).

Приєднуйтесь до нашої Slack-групи, якщо у вас виникли питання або потрібна допомога: [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

### [Додаткові матеріали](../additional-material/git_workflow_scenarios/additional-material.md)

## Інструкції для інших інструментів

[Повернутись на головну сторінку](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
