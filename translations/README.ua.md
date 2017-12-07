[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)

# Перший внесок

Це важко. Це завжди важко, коли ви робите щось вперше. Особливо, коли ви працюєте над проектом з кимось, помикли будуть вдвічі неприємнішими. Але Open Source завжди пов’язаний з колективною роботою. Ми хочемо спростити шлях для початківців, які бажають зробити свій перший внесок.

Можна прочитати безліч інструкцій та переглянути сотні відео, але що може бути краще, ніж спробувати зробити внесок і не зламати нічого? Ціль цього проекту надати можливість новачкам зробити їх перший внесок. Запам’ятайте: чим більше ви розслаблені, тим краще ви вчитеся. Якщо ви хочете зробити свій перший внесок, просто слідуйте простим крокам нижче. Ми обіцяємо, це буде весело!

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

*Read this in other languages: [English](../README.md), [Indonesian](README.id.md), [Spanish](README.es.md), [Dutch](README.nl.md), [Hindi](README.hi.md), [Japanese](README.ja.md), [Vietnamese](README.vn.md), [Polish](README.pl.md), [Korean](README.ko.md), [German](README.de.md), [Simplified Chinese](README.chs.md), [Traditional Chinese](README.cht.md), [Greek](README.gr.md), [العربية](README.ar.md), [Russian](README.ru.md).*

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

<img style="float: right;" src="../assets/submit-pull.png" alt="submit pull request" />

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

Тепер я обє’днав вашу вітку `<add-your-name>` з моєю основною віткою, а ви об’єднали мою основну вітку зі свією основною віткою. Вітка, яку ви створювали для внесення змін більше не потрібна, ви можете видалити її:
```
git branch -d <add-your-name>
```
до того ж ви можете видалити і її віддалену версію також:
```
git push origin --delete <add-your-name>
```
Називати вітку в такий спосіб не обов’язково, однак це було зроблено з певною метою, щоб показати призначення цієї вітки. Існування будь-якої вітки може бути коротким, адже в кінці-кінців, всі вітки об’єднуються з основною віткою.

## Інструкції для інших інструментів


|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Що далі?

Ви можете приєднатися до нашої команди в slack, якщо ви потребуєте будь-якої допомоги або маєте якісь запитання. [Приєднатися до команди в slack](https://firstcontributions.herokuapp.com)

Нижче список задач для початківців в популярних репозиторіях, які ви можете легко вирішити. Не соромтеся, переходьте в репозиторії, щоб дізнатися більше

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
