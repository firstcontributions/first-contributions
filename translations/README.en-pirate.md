[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# المساهمة الأولى

تكون الأمور صعبة في المرة الأولى التي تحاول فيها شيئًا جديدًا. خاصةً عند التعاون في بيئة مفتوحة، فقد يكون ارتكاب الأخطاء غير مريح. نحن نسعى لجعل عملية التعلم والمساهمة في المشاريع مفتوحة المصدر أسهل للأشخاص الذين يساهمون لأول مرة.

قراءة المقالات ومشاهدة الدروس تساعد، ولكن لا شيء يضاهي تجربة فعلية في بيئة تدريبية. هذا المشروع يهدف إلى توفير إرشادات تسهل خطوات المبتدئين لعمل مساهمتهم الأولى. إذا كنت تبحث عن المساهمة لأول مرة، اتبع الخطوات التالية.



<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

إذا لم يكن لديك git على جهازك، [قم بتثبيته](https://help.github.com/articles/set-up-git/).

## اعمل نسخة من هذا المستودع (Fork)

قم بإنشاء نسخة من المستودع بالنقر على زر "fork" في أعلى هذه الصفحة. سينشئ هذا نسخة من المستودع في حسابك الخاص.

## استنساخ المستودع


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

الآن قم باستنساخ المستودع إلى جهازك. انتقل إلى حسابك في GitHub، انقر على زر الاستنساخ ثم انقر على أيقونة النسخ إلى الحافظة.

افتح نافذة الأوامر ونفذ الأمر التالي:

```
git clone "رابط الذي نسخته للتو"
```

حيث "رابط الذي نسخته للتو" هو رابط المستودع (نسختك من هذا المشروع). راجع الخطوات السابقة للحصول على الرابط.


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

على سبيل المثال:


```
git clone https://github.com/هذا-اسمك/first-contributions.git
```

حيث هذا-اسمك هو اسم المستخدم الخاص بك في GitHub. هنا تقوم بنسخ محتويات مستودع first-contributions في GitHub إلى جهازك.


## أنشئ فرعًا

انتقل إلى مجلد المشروع على جهازك (إذا لم تكن هناك بالفعل):


```
cd first-contributions
```

الآن قم بإنشاء فرع باستخدام الأمر `git checkout`:


```
git checkout -b <اسم-الفرع-الجديد>
```

على سبيل المثال:

```
git checkout -b add-luke-oliff
```

(اسم الفرع ليس بالضرورة أن يحتوي على كلمة "add"، ولكن من المناسب إضافتها لأنه الغرض من الفرع هو إضافة اسمك إلى القائمة).

## قم بعمل التغييرات المطلوبة وأضفها
الآن افتح ملف Contributors.md في محرر النصوص، وأضف اسمك إليه في أي مكان في الوسط. ثم احفظ الملف.


<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

إذا انتقلت إلى مجلد المشروع ونفذت الأمر `git status`، سترى التغييرات.

أضف التغييرات إلى الفرع الذي أنشأته للتو باستخدام الأمر git add:

```
git add Contributors.md
```

ثم قم بإضافة تلك التغييرات باستخدام الأمر `git commit`:


```
git commit -m "Add <اسمك> to Contributors list"
```

استبدل <اسمك> باسمك.


## ادفع التغييرات إلى GitHub

ادفع التغييرات باستخدام الأمر `git push`:


```
git push origin <اسم-الفرع>
```

استبدل `<اسم-الفرع>` باسم الفرع الذي أنشأته سابقًا.


## قم بإرسال التغييرات للمراجعة

إذا انتقلت إلى المستودع في GitHub، سترى زرًا بعنوان `Compare & pull request`. انقر عليه.


<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

الآن قم بإرسال الطلب (pull request).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

سيتم دمج التغييرات الخاصة بك قريبًا في الفرع الرئيسي للمشروع، وستحصل على إشعار عبر البريد الإلكتروني بمجرد دمج التغييرات.

## ماذا بعد؟

أحسنت! لقد أتممت دورة fork -> clone -> edit -> PR الأساسية التي ستواجهها كثيرًا كمساهم!

احتفل بمساهمتك وشاركها مع أصدقائك من خلال زيارة تطبيق الويب  [web app](https://firstcontributions.github.io/#social-share).


يمكنك الانضمام إلى فريقنا على Slack في حال احتجت إلى مساعدة أو لديك أي أسئلة. انضم إلى فريقنا على Slack [Join our slack crew](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)..

الآن دعنا نساعدك على المساهمة في مشاريع أخرى. لقد جمعنا قائمة بالمشاريع مع بعض المشاكل السهلة للبدء. اطلع على [th' list o' projects in web app](https://firstcontributions.github.io/#project-list).

### [مواد إضافية](../additional-material/git_workflow_scenarios/additional-material.md)

## دروس باستخدام أدوات أخرى

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
