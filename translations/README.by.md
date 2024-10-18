[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Першы ўклад у праект

Складана. Заўсёды складана пачынаць нешта з самага пачатку. Даволі непрыемна рабіць памылкі, асабліва калі вы працуеце ў камандзе. Увесь open source складаецца з супрацоўніцтва і сумеснай працы. Мы хочам аблегчыць першыя крокі ў навучанні і супрацоўніцтве пачаткоўцам распрацоўнікам.

Чытанне артыкулаў і падручнікаў можа дапамагчы, але што можа быць лепш, чым сапраўдны практычны вопыт, без рызыкі што-небудзь сапсаваць. Мэта гэтага праекта - належным чынам накіраваць маладых навабранцаў, а таксама даць ім магчымасць зрабіць іх першы ўклад. Памятаеце: чым менш вы напружаныя, тым лепш вы вучыцеся. Калі вы шукаеце магчымасць ажыццявіць свой першы ўклад, проста прытрымлівайцеся простым крокам, размешчаным ніжэй. Абяцаем, будзе цікава.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />


Калі ў вас не ўсталяваны git на кампутары, [ ўсталюйце яго ]( https://help.github.com/articles/set-up-git/ )

## Стварыце асобную галінку

Стварыце асобную галінку, націснуўшы на кнопку `fork` зверху гэтай старонкі. Такім чынам вы створыце копію гэтага рэпазітара ў сваім запісе.

## Капіюйце рэпазітар

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Цяпер каб скапіяваць ваш рэпазітар на персанальны кампутар. Націсніце на кнопку `clone`, а затым на абразок `copy to clipboard`, каб скапіяваць спасылку.

Адкрыйце тэрмінал і запусціце наступную git каманду:

```
git clone "url you just copied"
```
Дзе "url you just copied" (без двукоссяў) гэта спасылка на ваш рэпазітар. Паглядзіце папярэднія крокі, каб атрымаць гэтую спасылку.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Напрыклад:
```
git clone https://github.com/this-is-you/first-contributions.git
```
Дзе `this-is-you` ваш лагін на github. Такім чынам вы капіруеце рэпазітар 'first-contributions' з GitHub на ваш персанальны кампутар.

## Стварыце галінку

Перайдзіце ў каталог рэпазітара на вашым кампутары, калі вы яшчэ не там.

```
cd first-contributions
```
Цяпер стварыце галінку, з дапамогай `каманды git checkout`

```
git checkout -b <add-your-name>
```

Напрыклад:
```
git checkout -b add-alonzo-church
```
(Сінтаксічную не патрабуецца, каб назва галіны ўтрымлівала слова * add *, але гэта апраўдана, паколькі падкрэслівае прызначэнне гэтай галіны - дадаць ваша імя ў спісы.)

## Занясіце неабходныя змены і стварыце commit

Цяпер адкрыйце файл `Contributors.md` ў вашым тэкставым рэдактары, запішыце ваша імя і захавайце файл. Калі вы пяройдзеце ў дырэкторыю праекта і выканайце `git status`, вы ўбачыце змены. Дадайце гэтыя змены з дапамогай каманды `git add`.

```
git add Contributors.md
```

Цяпер занясіце дадзеныя змены з дапамогай каманды `git commit`.
```
git commit -m "Add <your-name> to Contributors list"
```
Зменіце `<your-name>` на ваша імя

## Занясіце дадзеныя змены на github

Занясіце вашыя змены з дапамогай каманды `git push`
```
git push origin <add-your-name>
```
Зменіце `<add-your-name>` на імя галіны, якую вы стварылі раней.

## Пацвердзіце змены для праверкі вашага кода

Калі вы зойдзеце ў свой рэпазітар на GitHub, вы ўбачыце кнопку `Compare & pull request`. Націсніце на яе.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Цяпер пацвердзіце pull-request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Хутка я ўчыню аб'яднанне ўсіх вашых змяненняў з асноўнай галіной гэтага праекта. Вы атрымаеце паведамленне па электроннай пошце, калі змены будуць прынятыя (ўнесены ў галоўную галіну).

Асноўная галіна вашага рэпазітара не будзе зменена. Для сінхранізацыі выканайце крокі, размешчаныя ніжэй.

## Сінхранізуецца ваша адгалінаванне з дадзеным рэпазітаром

Перш за ўсё перайдзіце ў асноўную галіну:
```
git checkout master
```
Затым дадайце url майго рэпазітара ў полі `upstream remote url`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Такім чынам мы паведамім git, што існуе іншая версія дадзенага праекта па пэўнай спасылцы, і мы яе лічым майстрам. Як толькі змены смержены, падгрузіць новую версію майго рэпазітара.
```
git fetch upstream
```

Такім чынам мы забралі ўсе змены ў маім адгалінаванні (upstream remote). Пасля, вам трэба зліць новую версію майго рэпазітара з вашай майстар-галіной.
```
git rebase upstream/master
```
Так вы ўжываеце ўсе змены, якія вы падцягнулі да вашай майстар-галіны. Калі вы запушите зараз майстар-галіна, ваша адгалінаванне таксама будзе ўтрымліваць змены.
```
git push origin master
```
Звярніце ўвагу, што вы робіце push ў выдаленай рэпазітар origin.

На гэтым этапе я аб'яднаў вашу галіну `<add-your-name>` са сваёй майстар-галіной, а вы аб'ядналі сваю майстар-галіна з маёй. Ваша галіна больш не патрэбна, вы можаце выдаліць яе:
```
git branch -d <add-your-name>
```
Таксама можаце выдаліць яе версію ў аддаленым рэпазітары:
```
git push origin --delete <add-your-name>
```
Гэта зусім не абавязкова, але назва гэтай галіны адлюстроўвае яе даволі спецыфічнае прызначэнне. І працягласць яе жыцця можа быць адпаведна кароткай.

## Выкарыстанне іншых інструментаў

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |


## Што далей?

Ніжэй некалькі папулярных рэпазітароў, дзе вы можаце знайсці заданні для пачаткоўцаў. Наперад, перайдзіце ў рэпазітары, каб даведацца больш.

| [![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22) | [![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                       | [<img width="100" src="https://cdn.worldvectorlogo.com/logos/react-2.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)                       | [![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)         | [![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)      | [<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie) | [<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)          | [![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)                                                                | [Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                                                                                      | [react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)                                                                                         | [habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                         | [scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                    | [Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)                                                                                                                                                                        | [numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)                                                                                                 | [elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)                                                                |
| [![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)             | [![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)                                                                              | [![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)                         | [![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)        | [![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                        | [![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)                                                                                                 | [![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer) | [![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)                           |
| [homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)                                                                            | [Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)                                                                                                                                             | [vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)                                                                                        | [Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)                                                                       | [OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                                      | [PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)                                                                                                                                                                 | [coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)                                                                 | [moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)                                                                                          |
| [![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)                | [![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                | [![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22) | [![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only) | [![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22) | [![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)                                                                                                               | [![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                               | [<img width="100" src="https://cdn.worldvectorlogo.com/logos/brackets-1.svg">](https://github.com/adobe/brackets/labels/Starter%20bug)                     |
| [ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)                                                                               | [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                                                                               | [webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)                                                                | [hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                                | [pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)                                                                | [neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)                                                                                                                                                                              | [babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                                                              | [brackets](https://github.com/adobe/brackets/labels/Starter%20bug)                                                                                                                     |
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)    | [<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/public/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)                                                                   | [Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)                                                                                         |
