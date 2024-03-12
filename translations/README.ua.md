[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Перший внесок

Це важко. Це завжди важко - робити щось вперше. Проте якщо ви працюєте над проєктом з кимось, помилки будуть вдвічі неприємнішими. Але Open Source завжди пов’язаний з колективною роботою. Ми хочемо полегшити шлях для початківців, які бажають зробити свій перший внесок.

Можна прочитати безліч інструкцій та переглянути сотні відео, але що може бути краще, ніж спробувати зробити внесок не боячись нічого зламати? Ціль цього проєкту - надати можливість новачкам зробити їх перший внесок. Запам’ятайте: чим більше ви розслаблені, тим краще ви вчитеся. Якщо ви хочете зробити свій перший внесок, просто виконуйте прості кроки нижче. Ми обіцяємо, що це буде весело!

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Якщо ви ще не встановили GIT, тоді [ зробіть це негайно ]( https://help.github.com/articles/set-up-git/ ) :)

## Відгалужте репозиторій

Відгалужте свою власну копію цього репозиторію, натиснувши кнопку `fork` вгорі цієї сторінки.
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
де `this-is-you` - ваш GitHub нікнейм. Таким чином, ви копіюєте вміст репозиторію з GitHub, в який збираєтесь зробити внесок, на ваш комп’ютер.

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
git push origin <add-your-name>
```
замініть `<add-your-name>` назвою гілки, яку ви створили раніше.

## Відправляємо зміни на перевірку

Коли ви перейдете до свого репозиторію в GitHub, ви побачите кнопку `Compare & pull request`. Сміливо натисніть на неї.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Тепер зміни відправлені на перевірку і затвердження.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Згодом я об’єднаю ваші запропоновані зміни з основною гілкою цього репозиторію. Ви отримаєте листа, коли це буде зроблено.

Основна гілка вашого репозиторію не буде змінена. Якщо ви хочете синхронізувати ваше відгалуження з моїм репозиторієм, дотримуйтесь цієї інструкції.

## Тримаємо свій репозиторій синхронізованим

 Спочатку перейдіть на основну гілку.
 ```bash
 git checkout master
 ```

 Потім додайте мій репозиторій як `upstream remote url`:
```bash
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Таким чином ми повідомляємо git про те, що інша версія цього проєкту існує за визначеною адресою і ми називаємо це  `upstream`. Як тільки зміни будуть об’єднані, заберіть нову версію мого репозиторію:
```bash
git fetch upstream
```
Тобто ви забираєте всі зміни з мого репозиторію. Тепер ви повинні об’єднати зміни, які прийшли з мого репозиторію, у вашу основну гілку.
```bash
git rebase upstream/master
```
Цим ви приймаєте всі зміни до основної гілки. Якщо ви відправите зміни до GitHub, ваше відгалуження також буде містити ці зміни:
```bash
git push origin master
```
Зауважте, що ви відправляєте зміни до віддаленого репозиторію, який був названий `origin`.

Тепер я об’єднав вашу гілку `<add-your-name>` з моєю основною гілкою, а ви об’єднали мою основну гілку зі своєю основною гілкою. Гілка, яку ви створювали для внесення змін, більше не потрібна. Ви можете видалити її:
```bash
git branch -d <add-your-name>
```
Крім цього, ви можете видалити і її віддалену версію:
```bash
git push origin --delete <add-your-name>
```
Називати гілку в такий спосіб не обов’язково, однак це було зроблено з певною метою, аби показати призначення цієї гілки. Існування будь-якої гілки може бути коротким, адже врешті-решт, всі гілки об’єднуються з основною гілкою.

## Інструкції для інших інструментів

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

## Що далі?

Ви можете приєднатися до нашої команди в Slack, якщо ви потребуєте будь-якої допомоги або маєте якісь запитання. [Приєднатися до команди в Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
