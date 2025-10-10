# 💻 دليل GitHub CLI (الواجهة سطر الأوامر)

مرحبًا بك في دليل استخدام **GitHub CLI**!  
هذا الدليل موجه لمحبي سطر الأوامر الذين يفضلون العمل بدون واجهة رسومية.  
بفضل أداة **GitHub CLI (gh)**، يمكنك تنفيذ جميع مهام GitHub من خلال الطرفية بسهولة.

---

## 🧰 المتطلبات الأساسية

قبل البدء، تأكد من توفر ما يلي:

- أن يكون **Git** مثبتًا على جهازك ([كيفية التثبيت](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
- أن تمتلك **حساب GitHub** فعال
- أن تقوم بتثبيت أداة **GitHub CLI**

لتثبيت أداة GitHub CLI، اتبع التعليمات الرسمية من [الوثائق هنا](https://cli.github.com/manual/installation).

---

## 🔐 تسجيل الدخول إلى GitHub CLI

بعد تثبيت الأداة، قم بتسجيل الدخول باستخدام الأمر التالي:

```bash
gh auth login
ثم اتبع التعليمات لتسجيل الدخول إلى حسابك على GitHub.

🍴 عمل Fork للمستودع
قم بعمل fork للمستودع الرسمي باستخدام الأمر التالي:

bash
Copy code
gh repo fork firstcontributions/first-contributions
سيُطلب منك تأكيد ما إذا كنت ترغب في استنساخ المستودع محليًا.
اختر الخيار yes عندما يُطلب منك ذلك.

🌿 إنشاء فرع جديد
قم بإنشاء فرع جديد لإضافة تعديلاتك، مثلًا:

bash
Copy code
git switch -c add-your-name
استبدل add-your-name باسمك أو وصف مختصر للتعديل الذي ستقوم به.

✍️ إجراء التعديلات
افتح ملف Contributors.md باستخدام أي محرر نصوص، ثم أضف اسمك ضمن قائمة المساهمين.
بعد ذلك، تحقق من حالة الملفات المعدلة:

bash
Copy code
git status
أضف الملف الذي عدلته إلى مرحلة الإعداد (staging):

bash
Copy code
git add Contributors.md
ثم قم بتثبيت التغيير (commit):

bash
Copy code
git commit -m "إضافة اسمي إلى قائمة المساهمين"
🚀 رفع التغييرات إلى GitHub
ادفع (push) التغييرات إلى الفرع الجديد على GitHub:

bash
Copy code
git push origin -u add-your-name
🔁 إنشاء Pull Request
الآن يمكنك إنشاء Pull Request لمراجعة التعديلات من قبل المشرفين على المشروع.
يمكنك فعل ذلك مباشرة من خلال سطر الأوامر باستخدام:

bash
Copy code
gh pr create --repo firstcontributions/first-contributions
اتبع التعليمات التي تظهر في الطرفية لكتابة عنوان ووصف لطلب الدمج (Pull Request)، ثم أرسله للمراجعة.

🎉 تهانينا!
لقد أكملت دورة المساهمة الكاملة:
Fork → Clone → Edit → Pull Request

شارك إنجازك مع أصدقائك وابدأ بالمساهمة في مشاريع أخرى مفتوحة المصدر 🚀
الخطوات التي تعلمتها هنا هي الأساس الذي ستستخدمه في جميع مساهماتك القادمة.

📚 موارد إضافية
الموقع الرسمي للمشروع

مجموعة Slack للدعم

وثائق GitHub CLI الرسمية

🏁 الخلاصة
من خلال هذا الدليل، أصبحت الآن قادرًا على استخدام GitHub CLI لإدارة مساهماتك دون الحاجة إلى واجهات رسومية.
استمر في المساهمة بانتظام، فكل تعديل صغير يُحدث فرقًا كبيرًا في عالم البرمجيات مفتوحة المصدر ❤️

© 2025 - هذا الدليل مترجم للعربية ضمن مشروع First Contributions
الترخيص: MIT License

yaml
Copy code

---

## 📦 بعد وضع الملف:
نفّذ الأوامر التالية لإنشاء ورفع التعديل:

```bash
git add docs/cli-tool-tutorials/github-cli-tutorials-arabic.md
git commit -m "إضافة ترجمة عربية لدليل GitHub CLI"
git push origin add-arabic-cli-tutorial
gh pr create --repo firstcontributions/first-contributions
