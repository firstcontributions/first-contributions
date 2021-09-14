[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Ilk marta loyihaga hissa qo'shish

Qiyin. Yangi narsani boshlash har doim qiyin. Xato qilish hammaga ham yoqmaydi, ayniqsa jamoada ishlayotgan bo'lsangiz. Hamma ochiq manbali loyihalar hamkorlik va o'zaro birgalikda ishlashni talab qiladi. Loyihamiz orqali yangi dasturchilarni o'qitish va o'zaro birgalikda ishlash uchun dastlabki qadamlarni yengillashtirishni maqsad qilganmiz.

Maqolalar va o'quv qo'llanmalarni o'qish yordam berishi mumkin, lekin chalkashliklarga yo'l qo'ymasdan haqiqiy amaliy tajribadan yaxshiroq. Loyihaning maqsadi - yangi yollanganlarga to'g'ri yo'l -yo'riq berish, shuningdek, ularga birinchi hissa qo'shish imkoniyatini berish. Esingizda bo'lsin, siz qanchalik stresssiz bo'lsangiz, shunchalik yaxshi o'rganasiz. Agar siz birinchi sarmoya kiritish imkoniyatini izlayotgan bo'lsangiz, quyidagi oddiy amallarni bajaring. Bu qiziqarli bo'lishiga va'da beramiz.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />


Agar kompyuteringizda git o'rnatilgan bo'lmasa, [ quyidagi havola orqali o'rnating ]( https://help.github.com/articles/set-up-git/ )

## Fork (tarmoq) yarating

Sahifaning yuqori qismidagi `fork` tugmachasini bosib, o'z repozitoriyangizda "fork" yarating. Bu orqali o'z akkauntingizda ushbu repozitoriyaning nusxasini yaratib olaasiz.

## Repozitoriyani klonlashtiring

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Endi omborni kompyuteringizga klonlang. Havolani nusxalash uchun `clone` tugmachasini, so'ng `copy to clipboard` belgisini bosing.

Terminalni oching va quyidagi git buyrug'ini kiriting:

```
git clone "url you just copied"
```
Bu yerda "url you just copied" (qo'shtirnoqlarsiz) - sizning akkauntingizdagi repozitoriyaga havoladir. Ushbu havolani olish uchun oldingi qadamlarni ko'rib chiqing.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Masalan:
```
git clone https://github.com/this-is-you/first-contributions.git
```
Bu yerdagi `this-is-you` - Sizning github'dagi loginingizdir. Bu orqali Siz GitHub'dan "first-contributions" repozitoriyasini o'z shaxsiy kompyuteringizga ko'chirib olasiz.

## Branch (bo'lim) yarating

Kompyuteringizdagi repozitoriya katalogi ichiga o'ting, agar hali buni bajarmagan bo'lsangiz.

```
cd first-contributions
```
Endi `git checkout` buyrug'i orqali alohida yangi branch yarating.

```
git checkout -b <add-your-name>
```

Masalan:
```
git checkout -b add-bek-roz
```
(Sintaktik jihatdan, branch nomi add* so'zini o'z ichiga olishi shart emas. Lekin ma'no jihatidan olib qaralganda, branch'ning bunday nomlanishidan asl maqsad Sizning ismingizni ro'yxatga qo'shishligini anglatadi.)

## Kerakli o'zgarishlarni amalga oshiring va kommit (yangilik qo'shish) yarating

Endi matn muharririda `Contributors.md` faylini oching, ismingizni kiriting va faylni saqlang. Agar siz loyiha katalogiga kirsangiz va `git status` ni ishga tushirsangiz, o'zgarishlarni ko'rasiz. Bu o'zgartirishlarni `git add` buyrug'i yordamida qo'shing.

```
git add Contributors.md
```

Endi bu o'zgarishlarni `git commit` buyruq yordamida kommit qiling.
```
git commit -m "Add <your-name> to Contributors list"
```
Quyidagi `<your-name>` o'rniga o'z ismingizni kiriting.

## O'zgartirishlarni github'ga kommit qiling.

O'zgartirishlaringizni `git push` bilan push (yuklash) qiling.
```
git push origin <add-your-name>
```
Quyidagi `<add-your-name>` o'rniga oldinroq Siz yaratgan branch nomini kiriting.

## Ko'rib chiqish uchun o'zgarishlarni tasdiqlang

GitHub'dagi o'z repozitoriyangizga kirsangiz, `Compare & pull request` tugmasini ko'rasiz. Shu tugmaning ustiga bosing.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Endi pull-request (o'zgarishlarni bosh repozitoriyaga qabul qilish taklifi)ni tasdiqlang.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Tez orada men sizning barcha o'zgarishlaringizni ushbu loyihaning asosiy bo'limiga qo'shaman. O'zgarishlar qabul qilinganda (chiqarilganda) elektron pochtangizga xabar keladi.

Sizning repozitoriyangizda branch (tarmoq) holati o'zgarmaydi. Sinxronizatsiya qilish uchun quyidagi amallarni bajaring.

## O'z branch'ingiz holatini mazkur bosh repozitoriya bilan sinxronlashtiring.

Birinchi, asosiy branch'ga o'ting:
```
git checkout master
```
Shundan so'ng, `upstream remote url` dan keyingi matn kiritish maydoniga mening repozitoriyam URL manzilini kiriting:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Таким образом мы сообщим git'у, что существует другая версия данного проекта по определенной ссылке, и мы ее считаем мастером. Как только изменения смержены, подгрузите новую версию моего репозитория.
Bu orqali biz git tizimiga ushbu loyihaning boshqa versiyasi mazkur havolada mavjud ekanligi va biz uni "master" (eng asosiy branch)  deb hisoblashimizni bildiramiz. O'zgarishlar birlashtirilgandan so'ng, mening repozitoriyamning yangi versiyasini yuklab oling.
```
git fetch upstream
```
Shu orqali Siz mendagi branch holatidagi o'zgarishlarni qabul qilib olasiz (upstream remote). Shundan so'ng, 
mening repozitoriyam yangi versiyasi bilan Sizning branch'ingizni birlashtirish lozim bo'ladi.
```
git rebase upstream/master
```
Bu sizning ustaxonangizga kiritilgan barcha o'zgarishlarni qo'llaydi. Agar siz hozir asosiy filialni bossangiz, sizning filialingiz ham o'zgarishlarni o'z ichiga oladi.
```
git push origin master
```
E'tibor bering, siz uzoqdan joylashgan omborga o'tmoqchisiz.

Shu nuqtada, men sizning `<add-your-name>` bo'limini o'zimning asosiy bo'limim bilan birlashtirdim, siz esa o'z filialingizni meniki bilan birlashtirdingiz. Sizning filialingiz endi kerak emas, uni o'chirib tashlashingiz mumkin:
```
git branch -d <add-your-name>
```
Siz uning versiyasini masofaviy omborda ham o'chirib tashlashingiz mumkin:
```
git push origin --delete <add-your-name>
```
Bu mutlaqo ixtiyoriy, lekin bu filialning nomi uning aniq maqsadini aks ettiradi. Va uning umri mos ravishda qisqa bo'lishi mumkin.

## Boshqa vositalardan foydalanish

| <a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a> |
| ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../github-windows-vs2017-tutorial.md)                                                                                                                              | [GitKraken](../gitkraken-tutorial.md)                                                                |


## Bunday keyin nima qilish kerak?

Quyidagi havolalarda bir nechta mashhur repozitoriyalar berilgan. Ular orqali yangi dasturchilar uchun topshiriqlarni topishingiz mumkin. Endi ko'proq ma'lumot olish uchun mazkur repozitoriyalarga o'tamiz. Qani, ketdik!

| [![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22) | [![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                       | [<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)                       | [![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)         | [![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)      | [<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie) | [<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)          | [![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)                                                                | [Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                                                                                      | [react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)                                                                                         | [habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                         | [scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                    | [Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)                                                                                                                                                                        | [numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)                                                                                                 | [elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)                                                                |
| [![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)             | [![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)                                                                              | [![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)                         | [![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)        | [![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                        | [![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)                                                                                                 | [![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer) | [![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)                           |
| [homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)                                                                            | [Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)                                                                                                                                             | [vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)                                                                                        | [Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)                                                                       | [OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)                                                                                      | [PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)                                                                                                                                                                 | [coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)                                                                 | [moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)                                                                                          |
| [![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)                | [![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                | [![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22) | [![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only) | [![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22) | [![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)                                                                                                               | [![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                               | [<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)                     |
| [ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)                                                                               | [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                                                                               | [webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)                                                                | [hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)                                                                | [pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)                                                                | [neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)                                                                                                                                                                              | [babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)                                                                                              | [brackets](https://github.com/adobe/brackets/labels/Starter%20bug)                                                                                                                     |
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)    | [<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/public/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)                                                                   | [Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)                                                                                         |
