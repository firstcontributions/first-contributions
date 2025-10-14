[![حب البرمجيات مفتوحة المصدر](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![الترخيص: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![مساعدو المصدر المفتوح](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# المساهمات الأولى

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | واجهة سطر أوامر GitHub (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|

هذا الدليل مخصص لنا نحن محبي الطرفية 💻، الذين يرغبون في إنجاز كل شيء من خلال سطر الأوامر.  
بفضل أداة [GitHub CLI](https://cli.github.com/)، أصبح ذلك ممكنًا بكل سهولة.  
يجب أن تكون مساهمتك الأولى ممتعة، مشجعة، وتمنحك الدافع للاستمرار في عالم المشاريع مفتوحة المصدر!

هذا الدليل أكثر تفصيلاً قليلًا لأنه لا يعتمد على واجهة رسومية، لكنه يبقى ممتعًا وسهل المتابعة خطوة بخطوة. 🚀

---

## المتطلبات الأساسية

قبل أن نبدأ، تأكد من توفر ما يلي:
- تثبيت Git على جهازك (راجع [كيفية التثبيت](https://git-scm.com/downloads))
- حساب GitHub فعال

بعد ذلك، سنقوم بتثبيت أداة **GitHub CLI** من خلال اتباع [التعليمات الرسمية](https://github.com/cli/cli#installation).

ثم نقوم بتسجيل الدخول عبر الأمر التالي:

```bash
gh auth login
اتبع التعليمات على الشاشة، وستكون جاهزًا للعمل 🎉

عمل Fork لهذا المستودع
الأمر بسيط جدًا، فقط نفّذ الأمر التالي:

bash
Copy code
gh repo fork firstcontributions/first-contributions
💡 ملاحظة: سيُطلب منك ما إذا كنت ترغب أيضًا في استنساخه (clone)، اختر الخيار "yes"

إنشاء فرع خاص بك
سنقوم بهذه الخطوة باستخدام Git:

bash
Copy code
git switch -c add-your-name
استبدل your-name باسمك، مثل:

bash
Copy code
git switch -c add-okba14
إجراء التعديلات المطلوبة ورفعها
الآن افتح الملف Contributors.md في أي محرر نصوص، وأضف اسمك في أي مكان داخل الملف، ثم احفظ التغيير.

تحقق من حالة الملفات المعدلة:

bash
Copy code
git status
سترى أن الملف Contributors.md قد تم تغييره.
أضف التغيير إلى الفرع الجديد:

bash
Copy code
git add Contributors.md
ثم أنشئ commit جديد:

bash
Copy code
git commit -m "إضافة اسمك إلى قائمة المساهمين"
استبدل “اسمك” باسمك الحقيقي.

رفع التغييرات إلى GitHub
الآن لنرسل التغييرات إلى GitHub باستخدام:

bash
Copy code
git push origin -u اسم-الفرع
استبدل “اسم-الفرع” باسم الفرع الذي أنشأته سابقًا.

<details> <summary><strong>في حال واجهت أخطاء أثناء الرفع، اضغط هنا 👇</strong></summary>
خطأ في المصادقة (Authentication Error)
bash
Copy code
remote: Support for password authentication was removed on August 13, 2021.
Please use a personal access token instead.
fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'
لحل المشكلة، اتبع دليل GitHub الرسمي لإعداد مفتاح SSH وربطه بحسابك.

</details>
إرسال التغييرات للمراجعة
بعد رفع التعديلات، أنشئ Pull Request عبر الأمر التالي:

bash
Copy code
gh pr create --repo firstcontributions/first-contributions
ثم أرسل الطلب للمراجعة ✅
يمكنك أيضًا استخدام الأمر التالي للتحقق من حالة الطلب:

bash
Copy code
gh status
ماذا بعد؟ 🌱
مبروك! 🎉
لقد أنجزت بنجاح دورة العمل الكاملة:
Fork → Clone → تعديل → Pull Request

احتفل بمساهمتك وشاركها مع أصدقائك عبر تطبيق الويب.

وإذا احتجت لأي مساعدة أو نقاش، يمكنك الانضمام إلى مجتمعنا على Slack من خلال الرابط التالي:
👉 انضم إلى فريق Slack

تابع رحلتك 🚀
الآن بعد أن تعلمت الخطوات الأساسية، يمكنك المساهمة في مشاريع أخرى مفتوحة المصدر.
راجع قائمة المشاريع السهلة لتبدأ فورًا.

مواد إضافية
أدلة باستخدام أدوات أخرى
🔙 العودة إلى الصفحة الرئيسية

yaml
Copy code

---

> تمت الترجمة إلى العربية بواسطة: [Guiar Oqba](https://github.com/okba14) 🇩🇿  






