[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Жобаға алғашқы үлес қосу

Бұл қиын. Бірдеңе істегенде бірінші кезекте әрқашан қиын. Қателіктер жасау өте жағымсыз, әсіресе командада жұмыс істесеңіз. Барлық open source проекттер ынтымақтастық пен бірегей жұмыстан тұрады. Біз бастаушы әзірлеушілер үшін оқыту мен бірлесіп жұмыс істеудегі алғашқы қадамдарды жеңілдеткіміз келеді.

Оқулықтарды және мақалаларды оқуға әрқашан болады, бірақ іс жүзінде тәжірибе ортасында жұмыс жасаудан гөрі не жақсы? Бұл жобаның мақсаты - жастарды дұрыс жолға қою, сондай-ақ оларға алғашқы үлес қосуға мүмкіндік беру. Егер сіз өзіңіздің алғашқы үлесіңізді жасау мүмкіндігін іздесеңіз, төмендегі қарапайым қадамдарды орындаңыз. Біз уәде етеміз, бұл қызықты болады.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />


Егерде сіздің компьютеріңізде git қосылмаған болса, [ оны қосыңыз ]( https://help.github.com/articles/set-up-git/ )

## Тармақты (fork) жасаңыз

Өзіңіздің тармағыңызды жасау үшін, беттің үстіңгі жағындағы `fork` түймесін басыңыз. Осылай сіз осы репозиторийдің өзіңіздің аккаутыңызда копиясын жасайсыз.

## Репозиторийді клондаңыз

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Енді бұл репозиторийді өз дербес компьютеріңізге клодаңыз. Сілтемені көшіру үшін `clone` батырмасын басыңыз, содан кейін `copy to clipboard` белгішесіне басыңыз.

Терминалды ашып, келесі git пәрмендіні іске қосыңыз:

```
git clone "url you just copied"
```
Бұл жерде "url you just copied" (тырнақшасыз) сіздің репозиторийңізге сілтеме. Бұл сілтемені алу үшін алдыңғы қадамдарды қараңыз.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Мысалы:
```
git clone https://github.com/this-is-you/first-contributions.git
```
Бұл жерде `this-is-you` сіздің github-тағы логин. Осылайша GitHub-тан сіздің компьютеріңізге 'first-contributions' репозиторийін көшіресіз.

## Тармақ жасаңыз

Егер сіз әлі сол жерде жоқ болсаңыз, компьютердегі репозиторий каталогына өтіңіз.

```
cd first-contributions
```
Енді `git checkout` команданың көмегімен тармақты құрыңыз.

```
git checkout -b <add-your-name>
```

Мысалы:
```
git checkout -b add-alonzo-church
```
(Синтаксистік түрде тармақта *add* сөзі болуы қажет емес, бірақ ол осы тармақтың мақсатына баса назар аударғандықтан негізделеді - атыңызды тізімге қосу.)

## Керек өзгерістерді жасаңыз да, коммит істеңіз

Енді мәтіндік редакторда `Contributors.md` файлын ашыңыз, атыңызды енгізіңіз және файлды сақтаңыз. Егер сіз жобалық каталогқа барып, `git status` орындасаңыз, өзгертулерді көресіз. Бұл өзгертулерді `git add` командасымен қосыңыз.

```
git add Contributors.md
```

Енді бұл өзгерістерды `git commit` командасымен коммиттаңыз.

```
git commit -m "Add <your-name> to Contributors list"
```
`<your-name>` өзіңіздің атыңызға ауыстырыңыз

## Өзгерістерді github'қа пуштаңыз

Өзгерістерді `git push` командасымен пуштаңыз
```
git push origin <add-your-name>
```
`<Add-your-name>` дегенді бұрын құрылған тармақ атына өзгертіңіз.

## Өзгерістерді ревью үшін растаңыз

Егер сіз GitHub-тағы репозиторийге кірсеңіз, `Compare & pull request` батырмасын көресіз. Оны басыңыз.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Енді пулл-реквестті растаңыз.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Көп ұзамай мен осы жобаның негізгі бөлімімен барлық өзгерістерді біріктіремін. Өзгерістер қабылданған кезде (мердж жасалғанда) электрондық хат аласыз.

## Ары қарай не?

Төменде сіз жаңадан келген тапсырмаларды таба алатын бірнеше танымал репозиторийлер бар. Қосымша ақпарат алу үшін репозиторийге барыңыз.

| [![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22) | [![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                       | [<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)                       | [![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)         | [![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)      | [<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie) | [<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)          | [![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)                                                                | [Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                                                                                      | [react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)                                                                                         | [habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                         | [scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                    | [Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)                                                                                                                                                                        | [numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)                                                                                                 | [elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)                                                                |
| [![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)             | [![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)                                                                              | [![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)                         | [![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)        | [![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                        | [![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)                                                                                                 | [![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer) | [![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)                           |
| [homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)                                                                            | [Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)                                                                                                                                             | [vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)                                                                                        | [Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)                                                                       | [OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                                      | [PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)                                                                                                                                                                 | [coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)                                                                 | [moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)                                                                                          |
| [![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)                | [![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                | [![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22) | [![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only) | [![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22) | [![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)                                                                                                               | [![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                               | [<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)                     |
| [ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)                                                                               | [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                                                                               | [webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)                                                                | [hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                                | [pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)                                                                | [neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)                                                                                                                                                                              | [babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                                                              | [brackets](https://github.com/adobe/brackets/labels/Starter%20bug)                                                                                                                     |
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)    | [<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/public/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)                                                                   | [Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)                                                                                         |

