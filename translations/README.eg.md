[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
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


#### *Read this in [other languages](../Translations.md)* 


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

<img style="float: left;" src="../assets/submit-pull-request.png" alt="submit pull request" />

<div dir="rtl">بعد المراجعة هدمج تغيرراتك للفرع الرئيسي في المشروع. وهيتم تنبيهك عن طريق البريد الإلكتروني بدة.</div>

<div dir="rtl">لما يحصل وأقبل طلبك هتلاقي ان المشروع المنسوخ على حسابك مفيهوش التغيررات. فلازم تزامن المشروع الرئيسي باللي على حسابك بالخطوات دي:</div>


## <div dir="rtl">طب اعمل ايه بعد كدة؟</div>

<div dir="rtl">
 احتفل بأول مساهمة ليك، أعمل شير مع صحابك ومتابعينك عن طريق زيارة <a href="https://roshanjossey.github.io/first-contributions/#social-share">الموقع دة. </a>
</div>

<div dir="rtl">ممكن تنضم للفريق على Slack لو حابب تساعد او عندك أسئلة. <a href="https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY"> إنضم للفريق على Slack</a></div>

<br>

<div dir="rtl">يلا نخليك تبدأ تساهم في مشاريع بجد؟ عملنا قائمة بمشاريع بمشاكل بسيطة ممكن تبدأ بيها النهاردة.</div>
<div dir="rtl">شوف <a href="https://roshanjossey.github.io/first-contributions/#project-list">قائمة المشاريع على الموقع. </a> </div>

## <div dir="rtl"><a href="../additional-material/additional-material.md">حاجات وأدوات زيادة</a></div>

## <div dir="rtl">لو هتستخدم ادوات تانية ممكن تتعلم من هنا</div>

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|
