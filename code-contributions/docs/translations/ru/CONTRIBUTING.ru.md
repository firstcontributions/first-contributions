# Шаги для создания контрибьюшена

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="создание собственной ветки" />

## Создайте собственную ветку, нажав на кнопку fork

## Клонируйте ваш репозиторий

Нажмите на кнопку code в своем репозитории. Выберите вкладку SSH и кликните на кнопку `copy to clipboard`.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="клонирование репозитория" />
Откройте терминал и запустите `git clone`

```bash
git clone "скопированная ссылка"
```

> [!Важно]
> В последующих шагах нужно заменить `<твой-github-id>` на ваш GitHub ID.  
> Например, если твой GitHub ID - `aaronsw`,  
> `git switch -c add-<твой-github-id>` becomes `git switch -c add-aaronsw`  
> `contributors/<твой-github-id>.html` becomes `contributors/aaronsw.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="копирование ссылки" />

## Создание ветки

Перейдите в каталог репозитория на вашем компьютере, если вы еще не там

```bash
cd code-contributions
```
Теперь создайте ветку с помощью команды `git switch`

```bash
git switch -c add-<твой-github-id>
```


## Создай свою карточку

Вы можете добавить свою карточку HTML файлом в папку contributors. Создайте файл с вашим юзернеймом в папке contributors. Для начала вы можете скопировать данный шаблон.

`contributors/<твой-github-id>.html`
```html
<article>
  <h3>Твой юзернейм</h3>
  <p>Небольшое "о себе" (опционально)</p>
  <h4>Языки программирования, которые я использую</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Технологии, которые я использую</h4>
  <section class="container">
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"
    />
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"
    />
  </section>
</article>
<style>
  body {
    font-family: sans-serif;
  }
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .badge {
    padding: 0.5rem;
    border-radius: 0.25rem;
  }
  .icon {
    width: 2rem;
  }
</style>

```
## Добавь свою карточку в список контрибьюшенов

Добавь название созданного файла в`scripts/contributors.js`.

`scripts/contributors.js`
```js
const contributorFiles = [
  "<твой-github-id>.html", // добавьте название своего файла сюда
  "roshanjossey.html",
  "gokultp.html",
];
```

## Посмотрите свои изменения в браузере

Вы можете увидеть свои изменения при открытии файла `index.html` в браузере. Вы должны увидеть карточку, созданную в предыдущих шагах.

Вы можете продолжать добавлять изменения в свою карточку и обновлять страницу для просмотра этих изменений.

## Подтвердите свои изменения

Добавьте изменения с помощью команды `git add`

```bash
git add contributors/<твой-github-id>.html
```

Далее сделайте коммит с помощью `git commit`

```bash
git commit -m "add <твой-github-id>"
```

## Запушьте изменения на GitHub

```bash
git push -u origin add-<твой-github-id>
```

## Подтвердите изменения для ревью

Если вы зайдете в свой репозиторий на GitHub, вы увидите кнопку `Compare & pull request`. Нажмите на нее.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="создание пулл-реквеста" />

Теперь подтвердите пулл-реквест.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="подтверждение пулл-реквеста" />

Вы получите сообщение по электронной почте, когда изменения будут приняты (смержены).
