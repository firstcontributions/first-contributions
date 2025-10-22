
# راهنمای مشارکت در پروژه

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="انشعاب از این مخزن" />

## 1. انشعاب (Fork) از مخزن

با کلیک روی دکمه Fork در بالای صفحه، یک کپی از این مخزن در حساب کاربری خود ایجاد کنید.

## 2. کلون کردن مخزن انشعاب گرفته شده

در مخزن انشعاب گرفته شده خود، روی دکمه Code کلیک کنید. تب SSH را انتخاب و سپس دکمه 'کپی به کلیپ‌بورد' را بزنید.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="کلون کردن مخزن" />
در ترمینال، دستور زیر را اجرا کنید:

```bash
git clone "آدرس-کپی-شده"
```

> [!مهم]
> در مراحل بعدی، هرجا `<your-github-id>` را دیدید، آن را با نام کاربری GitHub خود جایگزین کنید.
> مثلاً اگر نام کاربری شما `exampleuser` است:
> `git switch -c add-<your-github-id>` becomes `git switch -c add-exampleuser`  
> `contributors/<your-github-id>.html` becomes `contributors/exampleuser.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

## 3. ایجاد یک شاخه جدید

وارد دایرکتوری مخزن شوید:

```bash
cd code-contributions
```

سپس یک شاخه جدید ایجاد کنید:

```bash
git switch -c add-<نام-کاربری-شما>
```

## 4. ساخت کارت شخصی

می‌توانید یک فایل HTML در دایرکتوری contributors ایجاد کنید. از این الگو استفاده کنید:

`contributors/<نام-کاربری-شما>.html`
```html
<article>
  <h3>نام کاربری شما</h3>
  <p>یک توضیح کوتاه درباره خودتان (اختیاری)</p>
  
  <h4>زبان‌های برنامه‌نویسی که استفاده می‌کنم</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>ابزارهایی که استفاده می‌کنم</h4>
  <section class="container">
    <img class="icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg" />
    <img class="icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg" />
  </section>
</article>

<style>
  /* استایل‌های CSS */
</style>
```

## 5. اضافه کردن کارت به لیست مشارکت‌کنندگان

نام فایل ایجاد شده را به این فایل اضافه کنید:

`scripts/contributors.js`
```js
const contributorFiles = [
  "<نام-کاربری-شما>.html", // نام فایل خود را اینجا اضافه کنید
  "roshanjossey.html",
  "gokultp.html"
];
```

## 6. مشاهده تغییرات

با باز کردن فایل `index.html` در مرورگر می‌توانید تغییرات را مشاهده کنید.

## 7. ثبت تغییرات

ابتدا تغییرات را stage کنید:

```bash
git add contributors/<نام-کاربری-شما>.html
```

سپس commit کنید:

```bash
git commit -m "اضافه کردن <نام-کاربری-شما>"
```

## 8. ارسال تغییرات به GitHub

```bash
git push -u origin add-<نام-کاربری-شما>
```

## 9. ارسال درخواست ادغام (Pull Request)

در صفحه مخزن خود در GitHub، روی دکمه 'Compare & pull request' کلیک کنید و درخواست خود را ارسال نمایید.
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
پس از ادغام تغییرات، یک ایمیل دریافت خواهید کرد.
