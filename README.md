




اقرأ هاد الدليل بلغات ثانية من هون
.

<kbd><img title="Shqip" alt="Shqip" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/al.svg" width="22">
</kbd>

<!-- (language list stays unchanged) -->
First Contributions

هالمشروع هدفه يسهّل ويرشد المبتدئين كيف يعملوا أول مساهمة إلهم. إذا حابب تعمل أول مساهمة إلك، اتبع الخطوات اللي تحت.

إذا مش مرتاح باستخدام سطر الأوامر، هون شروحات باستخدام أدوات بواجهة رسومية.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />
إذا ما عندك git على جهازك، نزّله من هون
.
Fork this repository

اعمل Fork لهالمستودع عن طريق الضغط على زر fork الموجود فوق الصفحة.
هيك بصير عندك نسخة من المستودع على حسابك.

Clone the repository
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the repository" />

هلا انسخ المستودع اللي عملتله fork على جهازك. روح على حسابك في GitHub، افتح المستودع، اضغط على زر code، بعدين تبويب SSH، وبعدين اضغط على أيقونة نسخ الرابط.

افتح التيرمنال ونفّذ أمر git التالي:

git clone "url you just copied"


حيث إن "url you just copied" (بدون علامات اقتباس) هو رابط المستودع تبعك. راجع الخطوات السابقة عشان تجيب الرابط.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

مثال:

git clone git@github.com:this-is-you/first-contributions.git


حيث إن this-is-you هو اسم المستخدم تبعك على GitHub. هيك بتكون نسخت محتوى المستودع على جهازك.

Create a branch

غيّر المسار لمجلد المشروع على جهازك (إذا مش فيه):

cd first-contributions


هلا اعمل فرع جديد باستخدام الأمر git switch:

git switch -c your-new-branch-name


مثال:

git switch -c add-alonzo-church

<details> <summary> <strong>إذا طلعلك خطأ مع git switch، اضغط هون:</strong> </summary>

إذا ظهر الخطأ
"Git: switch is not a git command. See git –help"
غالبًا نسخة git عندك قديمة.

في هالحالة استخدم git checkout بدلها:

git checkout -b your-new-branch-name

</details>
Make necessary changes and commit those changes

افتح ملف Contributors.md بمحرر نصوص، وأضف اسمك فيه. لا تحطه لا بالبداية ولا بالنهاية، خليه بأي مكان بالنص. بعدين احفظ الملف.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

لما تنفّذ الأمر git status، رح تشوف إن في تغييرات.

أضف التغييرات باستخدام الأمر:

git add Contributors.md


وبعدين اعمل commit:

git commit -m "Add your-name to Contributors list"


بدّل your-name باسمك.

Push changes to GitHub

ادفع التغييرات باستخدام:

git push -u origin your-branch-name


بدّل your-branch-name باسم الفرع اللي عملته.

<details> <summary> <strong>إذا واجهتك مشاكل أثناء الدفع، اضغط هون:</strong> </summary>
Authentication Error

لو طلعلك خطأ بخصوص كلمة المرور، GitHub بطّل يدعم تسجيل الدخول بكلمة السر، ولازم تستخدم Personal Access Token أو SSH key.

راجع الشرح الرسمي من GitHub لإعداد مفتاح SSH.

</details>
Submit your changes for review

روح على مستودعك في GitHub، رح تلاقي زر Compare & pull request. اضغط عليه.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

بعدها قدّم الـ pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

قريبًا رح يتم دمج التغييرات تبعتك بالفرع الرئيسي، ورح يوصلك إيميل تأكيد.

Where to go from here?

مبروك! هيك خلّصت العملية الكاملة:
fork → clone → edit → pull request
وهاي الخطوات رح تستخدمها دايمًا كمساهم.

احتفل بمساهمتك وشاركها مع أصحابك من خلال web app
.

إذا حابب تتدرّب أكثر، شوف code contributions
.

وهلا بلّشنا! جمعنالك قائمة مشاريع فيها issues سهلة للبداية، تقدر تشوفها من قائمة المشاريع
.

مواد إضافية
Tutorials Using Other Tools

(الجدول والروابط بدون أي تغيير)