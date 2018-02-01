<div dir="rtl">
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
</div>

# <div dir="rtl">مساهمتك الأولى</div>


<div dir="rtl">
الصعوبة متوقعة لما تبدأ أي مشروع جديد، خصوصاً لو كان المشروع بيتضمن ناس تانية، ودة بيخلي الوقوع في الخطأ مزعج ومتعب.
<br>
لكن المساهمة في مشاريع مفتوحة المصدر اسسها العمل الجماعي والعطاء.
<br>
في المشروع دة هدفنا هو تبسيط الطريق لأول مساهمة ليك.
</div>


<div dir="rtl">
ممكن تقرأ وتتفرج على فيديوهات على الإنترنت عشان تعرف تبدأ فى المساهمة للمشاريع مفتوحة المصدر، لكن هتستفيد أكتر لو عرفت تساهم في مشروع دلوقتي من غير خوف لحسن تعمل حاجة غلط. المشروع اللى انت فاتحه حاليا بيركز انه يوفرلك التوجيهات الأولية اللي هتحتجها عشان تبدأ أول مساهمة ليك. مش مشكلة تغلط المهم انك تتعلم من الغلط ودة الهدف هنا. تابع الخطوات واحدة واحدة ونوعدك انك هتستمتع.
</div>


*Read this in other languages: [English](../README.md), [Spanish](README.es.md), [Dutch](README.nl.md), [Hindi](README.hi.md), [Russian](README.ru.md), [Japanese](README.ja.md), [Vietnamese](README.vn.md), [Polish](README.pl.md), [Korean](README.ko.md), [German](README.de.md), [Simplified Chinese](README.chs.md), [Traditional Chinese](README.cht.md), [Greek](README.gr.md).*


<div dir="rtl">
لو ماكنش عندك git على جهازك <a href="https://help.github.com/articles/set-up-git/">حمله من هنا.</a>
</div>

## <div dir="rtl"> أفصل المشروع دة - Fork this Repository </div>
<img style="float: left;" width="300" src="../assets/fork.png" alt="fork this repository" />
<div dir="rtl">
خد نسخة من المشروع دة (أو افصله) عن طريق انك تدوس على Fork في أعلى الصفحة.
لو عملت كدة فأنت اخدت نسخة من الفولدر دة فى حسابك على github.
</div>

## <div dir="rtl"> إنسخ المشروع دة - Clone the repository </div>

<img style="float: left;" width="300" src="../assets/clone.png" alt="clone this repository" />

<div dir="rtl">
انسخ المشروع دة لجهازك.
اضغط Clone بعدين دوس على أيقونة Copy to clipboard
</div>
<img style="float: left;" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />
<div dir="rtl">
إفتح التريمنال وأكتب الأمر دة:
</div>

```
git clone "url you just copied"
```

<div dir="rtl">بدل "url you just copied" حط الرابط اللي نسخته من الخطوة اللي فاتت، الرابط دة بتاع المشروع اللي على حسابك فى github.</div>

<div dir="rtl">على سبيل المثال:</div>

```
git clone https://github.com/this-is-you/first-contributions.git
```

<div dir="rtl">
في هذا المثال دة لاحظ ان 'this-is-you' هيكون إسم حسابك في موقع github، الأمر دة هينسخ محتويات المشروع لجهازك الخاص عشان تقدر تعدل عليه بحرية في أي وقت.
</div>
<br>

## <div dir="rtl">  فصل فرع - Create a branch </div>


<div dir="rtl"> بما اننا عايزين نعمل تغيير فى الفايل اللى عملناله نسخة على الجهاز.. الأول ننتقل للفولدر اللي لسة نسخينه: </div>

```
cd first-contributions
```

<div dir="rtl"> قبل مانعمل التغيير هنعمل "فرع" وهنديله اسم زي كدة: </div>

```
git checkout -b "add-your-name"
```

<div dir="rtl">هتحط اسمك بدل your-name</div>

<div dir="rtl">مثلا:</div>

```
git checkout -b "add-alonzo-church"
```

<br>

## <div dir="rtl">غيّر التغيير اللي حابب تغيره:</div></h2>

<div dir="rtl">
التغيير اللي هتغيره فى الحالة دي انك تحط اسمك فى نهاية قايمة الأسماء فى فايل. افتح فايل اسمه "Contributors.md" بالـ text editor المفضل ليك وحط إسمك و إحفظ الفايل.
بعد كدة ارجع للترمينال وأكتب الأمر دة <code>git status</code>  الأمر دة بيظهر لك أي تغيرات حصلت في المشروع.
عشان تضيف التغيرات دي للفرع بتاعك هتستخدم الأمر دا <code>git add</code>.
</div>

```
git add Contributors.md
```

<div dir="rtl">حتى الأن انت عندك فرع فيه التغيير، عشان تبعت التغيير دة وتتمه  هيتعمل على خطوتين: الأولى انك تعمل للتغيير دة اسم فهتستخدم الأمر <code>git commit</code>.</div>

```
git commit -m "Add <your-name> to Contributors list"
```

<div dir="rtl"> إستبدل <code>&#60;your-name&#62;</code> بإسمك. </div>
<br>

## <div dir="rtl"> بعدين ترفع التغيررات - Push changes to Github </div>

<div dir="rtl">هترفع التغيررات عن طريق الأمر <code>git push</code></div>

```
git push origin "add-your-name"
```

<div dir="rtl">إستبدل <code>&#60;add-your-name&#62;</code> بإسم الفرع اللي انت لسة عامله .</div>


<br>
<h2 id="سلم-تغيراتك-للمراجعة"><a name="سلم-تغيراتك-للمراجعة" href="#سلم-تغيراتك-للمراجعة"></a><div dir="rtl">سلم تغيراتك للمراجعة</div></h2>


<div dir="rtl">في صفحة المشروع بتاعك على صفحتك الشخصية على github دوس على زرار <code>Compare &amp; pull request</code>. هو ماكنش  ظاهر قبل كدة.</div>

<img style="float: left;" src="../assets/compare-and-pull.png" alt="create a pull request" />

<div dir="rtl">دلوقتي هتسلم طلبك لصاحب المشروع الأساسي عشان يراجع عليه، في الحالة دي الطلب بتاعك هيوصلي. </div>

<img style="float: left;" src="../assets/submit-pull.png" alt="submit pull request" />

<div dir="rtl">بعد المراجعة هدمج تغيرراتك للفرع الرئيسي في المشروع. وهيتم تنبيهك عن طريق البريد الإلكتروني بدة.</div>

<div dir="rtl">لما يحصل وأقبل طلبك هتلاقي ان المشروع المنسوخ على حسابك مفيهوش التغيررات. فلازم تزامن المشروع الرئيسي باللي على حسابك بالخطوات دي:</div>

## <div dir="rtl">مزامنة نسختك مع المشروع الرئيسي</div>

 <div dir="rtl">الخطوة الأولى، روح للفرع الرئيسي.</div>

```
git checkout master
```

 <div dir="rtl">ثانياً،ضيف رابط المشروع الرئيسي كـ<code>upstream remote url</code>.</div>
 
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```

<div dir="rtl">بالطريقة دي احنا بنقول لgithub أن فيه نسخة تانية من المشروع دة في الرابط دة ونسميها <code>upstream</code>.
بعد ما أكون وافقت على تغيرراتك، لما تسحب النسخة الجديدة من المشروع عن طريق الأمر دة:
</div>

```
git fetch upstream
```

<div dir="rtl">هتقوم بسحب كل التغيررات من <code>(upstream remote)</code>.  دلوقت، لازم تدمج التحديثات الجديدة من فرعي لفرعك الرئيسي.</div>

```
git rebase upstream/master
```

<div dir="rtl">وهنا هنحط التغيررات للفرع الرئيسي عندك. لو رفعت التغيررات لفرعك الرئيسي هيتحديث مشروعك</div>

```
git push origin master
```

<div dir="rtl">لاحظ أنك بترفع ل <code>remote</code> إسمه <code>origin</code>.</div>
<br>

## <div dir="rtl">ممكن تستخدم أدوات تانية</div>

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## <div dir="rtl">طب اعمل ايه بعد كدة؟</div>

<div dir="rtl">ممكن تنضم للفريق على Slack لو حابب تساعد او عندك أسئلة. <a href="https://firstcontributions.herokuapp.com"> إنضم للفريق على Slack</a></div>

<br>

<div dir="rtl">ممكن بردو تشوف المشاريع دي ودور على مشاكل أو مميزات ممكن تحلها أو تضيفها، بالتوفيق.</div>

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
| [![Node.js](https://avatars1.githubusercontent.com/u/9950313?v=3&s=100)](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|[<img width="100" src="https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png">](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22)|
| [Node.js](https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |[Semantic-UI-React](https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22) |
