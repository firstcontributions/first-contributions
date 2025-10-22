# خطوات المساهمة

## قم بعمل Fork لهذا المستودع بالنقر على زر Fork

<p align="left">
  <img width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />
</p>

## قم بنسخ المستودع المفروع (Fork) من هذا المستودع.
في المستودع المفروع، انقر على زر code. اختر علامة التبويب SSH ثم انقر على زر `copy to clipboard`.

<div style="display: flex; justify-content: center; gap: 10px; text-align: center;">
  <img width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />
  <img width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />
</div>

افتح الطرفية (Terminal) وقم بتشغيل أمر `git clone`

```bash
git clone "الرابط الذي نسخته"
```
##
> [!IMPORTANT]  
> **هام!**  
> استبدل `<your-github-id>` بمعرّف GitHub الخاص بك عند ظهوره في الأوامر التالية.  
> على سبيل المثال، إذا كان معرّف GitHub الخاص بك هو `aaronsw`:  
> `git switch -c add-<your-github-id>` يصبح `git switch -c add-aaronsw`  
> `contributors/<your-github-id>.html` يصبح `contributors/aaronsw.html`

## قم بإنشاء فرع (Branch)

انتقل إلى دليل المستودع إذا لم تكن فيه بالفعل:

```bash
cd code-contributions
```

قم بإنشاء فرع باستخدام أمر `git switch`:

```bash
git switch -c add-<your-github-id>
```

## قم بإنشاء بطاقتك

يمكنك إضافة بطاقتك كملف HTML في دليل `contributors`. قم بإنشاء ملف باسم المستخدم الخاص بك في هذا الدليل. يمكنك نسخ القالب التالي للبدء:

`contributors/<your-github-id>.html`

```html
<article>
  <h3>اسم المستخدم الخاص بك</h3>
  <p>نبذة صغيرة عنك (اختياري)</p>
  <h4>لغات البرمجة التي أستخدمها</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>الأدوات التي أستخدمها</h4>
  <section class="container">
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"
    />
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"
    />
  </section>
</article>
<style>
  body {
    font-family: sans-serif;
  }
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .badge {
    padding: 0.5rem;
    border-radius: 0.25rem;
  }
  .icon {
    width: 2rem;
  }
</style>
```

## أضف بطاقتك إلى قائمة المساهمين

أضف اسم الملف الذي أنشأته إلى ملف `scripts/contributors.js`:

`scripts/contributors.js`

```js
const contributorFiles = [
  "<your-github-id>.html", // أضف اسم ملفك هنا
  "roshanjossey.html",
  "gokultp.html",
];
```

## عرض تغييراتك في متصفح الويب

يمكنك رؤية تغييراتك بفتح `index.html` في متصفح الويب. يجب أن تكون قادرًا على رؤية البطاقة الجديدة التي أضفتها في الخطوات السابقة.

يمكنك الاستمرار في إجراء تغييرات على بطاقتك وتحديث علامة تبويب المتصفح لرؤية هذه التغييرات.

## قم بتثبيت تغييراتك

أولاً قم بتجهيز تغييراتك باستخدام أمر `git add`:

```bash
git add contributors/<your-github-id>.html
```

الآن قم بتثبيت تغييراتك باستخدام أمر `git commit`:

```bash
git commit -m "add <your-github-id>"
```

## قم بدفع تغييراتك إلى GitHub

```bash
git push -u origin add-<your-github-id>
```

## قدم تغييراتك للمراجعة

إذا ذهبت إلى مستودعك على GitHub، سترى زر `Compare & pull request`. انقر على هذا الزر.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

الآن قم بتقديم طلب السحب (Pull Request).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

ستتلقى إشعارًا بالبريد الإلكتروني بمجرد دمج التغييرات.

