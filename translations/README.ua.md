[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Перший внесок

Це важко. Це завжди важко, коли ви робите щось вперше. Особливо, коли ви працюєте над проектом з кимось, помилки будуть вдвічі неприємнішими. Але Open Source завжди пов’язаний з колективною роботою. Ми хочемо спростити шлях для початківців, які бажають зробити свій перший внесок.

Можна прочитати безліч інструкцій та переглянути сотні відео, але що може бути краще, ніж спробувати зробити внесок і не зламати нічого? Ціль цього проекту надати можливість новачкам зробити їх перший внесок. Запам’ятайте: чим більше ви розслаблені, тим краще ви вчитеся. Якщо ви хочете зробити свій перший внесок, просто слідуйте простим крокам нижче. Ми обіцяємо, це буде весело!

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Якщо ви ще не встановили GIT, тоді [ зробіть це негайно ]( https://help.github.com/articles/set-up-git/ ) :)

## Відгалужте репозиторій

Відгалужте свою власну копію цього репозиторія, натиснувши кнопку `fork` зверху цієї сторінки.
Це призведе до створення копії цього репозиторія у вашому акаунті.

## Клонуйте репозиторій

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Тепер клонуйте цей репозиторій на ваш комп’ютер. Натисніть на кнопку `clone`, а потім на іконку `copy to clipboard`.

Відкрийте термінал і виконайте наступні команди:

```
git clone "посилання, яке ви щойно скопіювали"
```
де `посилання, яке ви щойно скопіювали` (без кавичок) є адресою цього репозиторію. Дивіться попередній крок для того, щоб отримати цю адресу.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Наприклад:
```
git clone https://github.com/this-is-you/first-contributions.git
```
де `this-is-you` ваш GitHub нікнейм. Таким чином ви копіюєте вміст репозиторію з GitHub, в який збираєтесь зробити внесок, на ваш комп’ютер.

## Створюємо вітку

Перейдіть в директорію з репозиторієм на вашому комп’ютері (якщо ви ще цього не зробили):

```
cd first-contributions
```
Тепер створюємо вітку за допомогою команди `git checkout`:
```
git checkout -b <add-your-name>
```

Наприклад:
```
git checkout -b add-petro-church
```
(Назва вітки не повинна обов’язково містити слово *add*, але це має сенс, якщо майбутні зміни передбачають додавання чогось, наприклад, вашого імені в список контрибуторів.)

## Робимо необхідні зміни та записуємо їх в репозиторій

Тепер відкриваємо файл `Contributors.md` в текстовому редакторі, і додаємо ваше ім’я, а потім зберігаємо файл. Якщо ви перейдете в директорію проекту і виконаєте команду `git status`, ви побачите зміни. Додайте ці зміни до вітки, яку ви тільки що створили за допомогою команди `git add`:
```
git add Contributors.md
```

Тепер запишіть ці зміни за допомогою команди `git commit`:
```
git commit -m "Add <your-name> to Contributors list"
```
замініть `<your-name>` своїм іменем.

## Відправляємо зміни в GitHub

Відправте зміни на віддалений репозиторій в GitHub за допомогою команди `git push`:
```
git push origin <add-your-name>
```
замініть `<add-your-name>` назвою вітки, яку ви створили раніше.

## Відправляємо зміни на перевірку

Коли ви перейдети до свого репозиторія в GitHub, ви побачити кнопку `Compare & pull request`. Сміливо натисніть на цю кнопку.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Тепер зміни відправлені на перевірку і затвердження.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Скоро я об’єднаю ваші зміни з основною віткою цього репозиторія. Ви отримаєте листа коли це буде зроблено.

Основна вітка вашого репозиторія не буде змінена. Якщо ви хочете синхронізувати ваше відгалуження з моїм репозиторієм, слідуйте цієї інструкції.

## Зберігаємо свій репозиторій синхронізованим

 Спочатку перейдіть на основну вітку.
 ```
 git checkout master
 ```

 Потім додаєм мій репозиторій як `upstream remote url`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Таким чином ми повідомляємо git про те, що інша версія цього проекту існує за визначеною адресою і ми називаєм це  `upstream`. Як тільки зміни будуть об’єднані, заберіть нову версію мого репозиторію:
```
git fetch upstream
```
Таким чином ви забираєте всі зміни з мого репозиторію. Тепер ви повинні об’єднати, зміни які прийшли з мого репозиторію, в вашу основну вітку.
```
git rebase upstream/master
```
Таким чином ви приймаєте всі зміни до основної вітки. Якщо ви відправите зміни до GitHub, ваше відгалуження також буде мати ці зміни:
```
git push origin master
```
Зауважте, таким чином ви відправляєте зміни до віддаленого репозиторія, який був названий `origin`.

Тепер я об’єднав вашу вітку `<add-your-name>` з моєю основною віткою, а ви об’єднали мою основну вітку зі своєю основною віткою. Вітка, яку ви створювали для внесення змін більше не потрібна, ви можете видалити її:
```
git branch -d <add-your-name>
```
до того ж ви можете видалити і її віддалену версію також:
```
git push origin --delete <add-your-name>
```
Називати вітку в такий спосіб не обов’язково, однак це було зроблено з певною метою, щоб показати призначення цієї вітки. Існування будь-якої вітки може бути коротким, адже в кінці-кінців, всі вітки об’єднуються з основною віткою.

## Інструкції для інших інструментів


|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Що далі?

Ви можете приєднатися до нашої команди в slack, якщо ви потребуєте будь-якої допомоги або маєте якісь запитання. [Приєднатися до команди в slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
