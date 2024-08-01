[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Први чекори

Тешко е. Секогаш е тешко кога нешто се прави за прв пат. Кога соработуваме со други луѓе, правењето грешки е непријатно. Затоа сакавме да го поедноставиме начинот на кој новите соработници на отворен код учат и допринесуваат за прв пат.

Читањето на статии и гледањето на видеа помага до некаде, но нема подобар начин за учење од вежбањето. Целта на овој проект е да се обезбеди вежба и да се поедностави начинот по кој почетниците допринесуваат отворен код. Ако сакате да го направите својот прв придонес, тогаш следете ги долунаведените чекори.

#### *Ако не сакате да користите command line (терминал), [овде имате упатства за GUI](#Вежби-за-користење-на-други-програми)*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Ако немате git на вашиот компјутер, [инсталирајте го]( https://help.github.com/articles/set-up-git/).

## Направете Разгранување (Fork) на ова складиште (repository)

Направете разгранување на складиштето со притискање на копчето "Fork" кое се наоѓа на горниот дел на оваа страница.
Вака ќе направите копија на складиштето во вашиот GitHub профил.

## Клонирајте го овоа складиште

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Сега треба да го клонирате складиштето во вашиот компјутер. Отидете во вашиот GitHub профил, отворете го разгранетото складиште,
кликнете на копчето "Clone" и копирајте го линкот. Исто така може да притиснете на иконата за копирање (Copy to clipboard)

Отворете го терминалот и воведете ја следната команда:

```
git clone "линкот кој го копиравте"
```
На местото на "линкот кој го копиравте" (без наводници) поставете го линкот на складиштето (Вашето Разгранување на овој проект). Погледнете ги претходните чекори за да видете како да го добиете линкот.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

На пример:
```
git clone https://github.com/vashiot-username/first-contributions.git
```
со преименување на `vashiot-username` во вашето корисничко име. Во овој чекор правите копија на складиштето first-contributions од GitHub кон вашиот компјутер.

## Создавање на гранка (branch)

Променете ја локацијата на складиштето во вашиот компјутер (Ако сеуште не сте ја промениле):

```
cd first-contributions
```
Сега создајте гранка со помош на командата `git checkout`:
```
git checkout -b <vnesete-ime-na-vashata-granka>
```

На пример:
```
git checkout -b add-alonzo-church
```
(Името на гранката не мора да го содржи зборот  *add*, но се препорачува, затоа што целта на оваа гранка е да го додадете вашето име во списокот.)

## Направете ги потребните промени и извршете (commit) ги

Сега отворете го фајлот `Contributors.md` во уредник за текст и додадете го вашето име. Не додавајте го на почетокот или крајот на фајлот. Поставете го некаде на средината. Зачувајте ги промените.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Ако ја извршете командата `git status` во директоријата на складиштето, ќе забележите дека има промени.


Зачувајте ги промените на создадената гранката со помош на командата `git add`:

```
git add Contributors.md
```

Сега извршете ги промените со командата `git commit`:
```
git commit -m "Add <vasheto-ime> to Contributors list"
```
со промена на `<vasheto-ime>` со вашето име.

## Поставете (Push) ги промените во GitHub

Поставете ги вашите промени со командата `git push`:
```
git push origin <vnesete-ime-na-vashata-granka>
```
со промена на `<vnesete-ime-na-vashata-granka>` во името на вашата гранка, која ја создадовте претходно.

## Поднесете ги вашите промени за преглед.

Ако отидете во вашето складиште во GitHub, ќе го забележите копчето `Compare & pull request`. Притиснете го.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Сега поднесете ги вашите промени за преглед.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Наскоро ќе ги спојам (merge) сите ваши промени во главната гранка (мастер branch) на овој проект. Ќе бидете известени по пат на електронска пошта за спојот на вашите промени.

## Што е следно?

Честитки! Само што ги завршивте _fork -> clone -> edit -> PR_ операции, со кои ќе се соочувате често како соработник!

Прославете ги вашите придонеси и споделете ги со пријатели и следители со посета на [веб-апликацијата](https://firstcontributions.github.io/#social-share).

Можете да станете дел од нашиот slack team ако ви треба помош или имате прашања  [Стани дел](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Сега е време да започнете да допринесувате кон други проекти. Ние имаме создадено список со лесни проекти за да започнете. [Види ја листата](https://firstcontributions.github.io/#project-list).

### [Дополнителен материал](../additional-material/git_workflow_scenarios/additional-material.md)


## Вежби за користење на други програми

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
