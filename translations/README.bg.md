[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Първи стъпки

Трудно е. Когато правиш нещо за пръв път винаги е трудно. Още повече, когато се работи съвместно с други хора. Затова решихме да опростим процеса на учене за новобранците в допринасянето към отворен софтуер.

Четенето на статии и гледането на видео уроци помага, но има ли по-добър учител от практиката в защитена среда? Целта на този проект е да напътства и опрости първите стъпки на новобранците в участието и приноса към отворен софтуер. Ако искате да направите първата си контрибуция и да станете част от обществото на отворен софтуер, следвайте стъпките по-долу.

#### *Ако не се чувствате комфортно използвайки command line (терминал), [ето и уроци за използването на програми с графичен интерфейс](#Уроци-за-иползването-на-други-приложения)*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Ако нямате git на вашия компютър, [инсталирайте го]( https://help.github.com/articles/set-up-git/).

## Направете Разклонение (Fork) на това хранилище (repository)

Направете разклонение на хранилището като натиснете бутона "Fork" в горната част на тази страница.
Това ще направи копие на това хранилище във вашия GitHub профил.

## Клонирайте това хранилище

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Сега клонирайте локално на вашия компютър разклоненото хранилище. Отидете във вашия GitHub профил, отворете разклоненото хранилище,
кликнете на бутона 'Clone' и копирайте линка или натиснете иконката 'copy to clipboard' (копирай в клипборда).

Отворете терминал и въведете следната команда

```
git clone "линка който току-що копирахте"
```
като на мястото на  "URL-а който току-що копирахте" (без кавичките) поставете линка към това хранилище (Вашето Разклонение на този проект). Вижте
предните стъпки за това как да се сдобиете с линка.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Например:
```
git clone https://github.com/this-is-you/first-contributions.git
```
Като на мястото на `this-is-you` се намира вашето потребителско име. В тази стъпка вие направихте копие на съдържанието на GitHub хванилището на 'first contributions' във вашия компютър.

## Създайте клон (branch)

Стигнете до местоположението във вашия компютър, където копирахте хранилището (ако вече не се намирате там):

```
cd first-contributions
```
Сега създайте клон използвайки командата `git switch -c`:
```
git switch -c <add-your-new-branch-name>
```

Например:
```
git switch -c add-alonzo-church
```
(Името на клона не е задължително да съдържа думата *add*, но е препоръчително, защото целта на този клон е да добавите името си към списък.)

## Направете нужните промени и ги commit-нете

Сега отворете файла `Contributors.md` в текстов редактор и добавете името си в него. Не го добавяйте в началото или края на файла. Поставете го някъде посредата. Сега запазете промените.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Ако навигирате през терминала до директорията на проекта и въведете командата `git status`, ще видите че има променени файлове.


ДОбавете тези промени към клона, който създадохте, използвайки командата `git add`:

```
git add Contributors.md
```

Сега commit-нете тези промени с командата `git commit`:
```
git commit -m "Add <your-name> to Contributors list"
```
като смените `<your-name>` с вашето име.

## Качете (Push) промените в GitHub

Качете вашите промени като въведете командата `git push`:
```
git push origin <add-your-branch-name>
```
сменяйки `<add-your-branch-name>` с името на клона, който създадохте по-рано.

## Предайте вашите промени за рецензия

Ако отидете във вашето хранилище в GitHub, ще видите бутона  `Compare & pull request`. Натиснете го.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Сега предайте вашите промени за рецензия.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Скоро аз ще слея (merge) всички ваши промени в главния клон (мастер branch) на този проект. Вие ще бъдете уведомени по електронната поща когато това се случи.

## От тук накъде?

Поздравления!  Вие току що изпълнихте стандарните _fork -> clone -> edit -> PR_ операции, които ще срещнете като сътрудник!

Отпразнувайте вашия принос и го споделете с приятели и последователи като посетите [уеб приложението](https://firstcontributions.github.io/#social-share).

Можете да се присъедините към нашия slack team в случай, че имате допълнителни въпроси или нужда от помощ [Присъединете се към slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Време да започнете да допринасяте и към други приекти. Ние сме съставили списък с проекти съдържащи лесни проблеми, които са лесни за начало. Проверете  [списъка от приекти в уеб приложението](https://firstcontributions.github.io/#project-list).

### [Допълнителни материали](../additional-material/git_workflow_scenarios/additional-material.md)


## Уроци за иползването на други приложения

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
