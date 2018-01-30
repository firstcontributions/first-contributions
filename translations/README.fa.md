[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" src="https://firstcontributions.herokuapp.com/badge.svg">](https://firstcontributions.herokuapp.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

بخاطر ترجمه ضعیف شرمندم میتونین نسخه فینگلیش رو بخونین که قطعا بهتره
# اولین مشارکت

 سخته . همیشه سخته که برای اولین بار کاری رو انجام بدی. مخصوصا وقتی داری همکاری میکنی. اشتباه کردن چیز راحتی نیست. اما دنیای متن باز تماماً درباره مشارکت و همکاری هست. ما میخواستیم تا راه رو ساده کنیم تا مشارکت کننده های جدید این همکاری رو برای بار اول یاد بگیرن

خوندن مقالات و نگاه کردن ویدیو های آموزشی میتونه کمک کنه. اما چی از واقعاً انجام دادن کار بدون خرابکاری بهتره ؟ حدف این پروژه فراهم کردن یک راهنما و ساده کردن مسیر برای تازه کار هاست تا اولین مشارکت رو انجام بدن. یادت باشه: هرچی ریلکس تر باشی. بهتر یاد میگیری. اگه میخوای اولین همکاریت رو انجام بدی فقط راهنمای قدم به قدم ساده زیر رو انجام بده. ما قول میدیم. خوش میگذره :D

<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />
#### *Read this in [other languages](Translations.md).*

اگه روی دستگاهت گیت نداری. نصبش کن 
 https://help.github.com/articles/set-up-git/).

## این ریپوزیتوری رو فورک کن

این ریپوزیتوری رو از طریق کلیک کردن روی دکمه فورک بالای این صفحه فورک کن
این کار یک کپی از ریپوزیتوری تو اکانتت میسازه

## ریپپوزیتوری رو کلون کن

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

حالا ریپ و رو داخل کامپیوترت کلون کن. روی دکمه کلون کلیک کن و بعد روی (کپی در کلیپبورد) کلیک کن

ترمینال رو باز کن و دستورات زیر رو وارد کن

```
git clone "لینکی که کپی کردی"
```
جایی که (لینکی که کپی کردی) هست درواقع آدرس ریپوزیتوری هست که تو قدم پیش دیدی

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

برای مثال   
```
git clone https://github.com/this-is-you/first-contributions.git
```
داخل لینک بجای
`this-is-you`
نام کاربری گیتهاب خودت رو قرار بده
تو این مرحله داری محتویات ریپوزیتوری رو از گیتهاب کپی میکنی تو کامپیوتر خودت

## برنچ (شاخه) بساز

اگه هنوز داخل پوشه ریپوزیتوری نیستی. برو داخلش

```
cd first-contributions
```
حالا با استفاده از دستور
`git checkout`
یک برنچ جدید بساز
```
git checkout -b <add-your-name>
```

برای مثال
```
git checkout -b add-alonzo-church
```
لازم نیست کلمه
`add`
رو اول اسم برنچ بنویسی اما از اونجا که حدف از ساخت این برنچ اضافه کردن اسمت به لیست هست کار منطقی ای هست

## تغیرات ضروری رو انجام بده و کامیت کن

حالا فایل
`Contributors.md` 
رو داخل تکست ایدتور باز کن و اسمت رو به آخر فایل اضافه ک. بعد فابل رو ذخیره کن. اگه حالا وارد پوشه پروژه بشی و دستور
`git status`
رو اجرا کنی. میبینی که تغیرات اونجاست. حالا اون تغیرات رو به برنچی که ساختی اضافه کن با استفاده از دستور
`git add`
```
git add Contributors.md
```
حالا اون تغیرات با استفاده از دستور زیر کامیت کن
`git commit`
```
git commit -m "Add <your-name> to Contributors list"
```
جای
`<your-name>`
رو با اسم خودت عوض کن

## تغیرات رو به گیتهاب پوش کن

با استفاده از دستور زیر تغیراتت رو به گیتهاب پوش کن
`git push`
```
git push origin <add-your-name>
```
اسم
`<add-your-name>`
رو با اسم برنچی که ساخته بودی عوض کن

## تغیراتت رو برای برسی ثبت کن

اگه بری داخل ریپوزیتوریت تو گیتهاب. میبینی که دکمه
`Compare & pull request`
وجود داره . روش کلیک کن

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

حالا دستور پل رو ثبت کن

<img style="float: right;" src="assets/submit-pull.png" alt="submit pull request" />

بزودی من تمام تغیرات تو رو به شاخه اصلی این پروژه اضافه میکنم
زمانی که تغیرات ثبت شد یک ایمیل دریافت میکنی


## از اینجا کجا برم ؟

مشارکتت جشن بگیر و با دوستات و دنبال کننده هات به اشتراک بزار
[web app](https://roshanjossey.github.io/first-contributions/#social-share).

در صورتی که سوالی داشتی یا کمک خواستی میتونی به گروه اسلک ما ملحق بشی
[Join slack team](https://firstcontributions.herokuapp.com).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Additional material](additional-material/additional-material.md)


## Tutorials Using Other Tools

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/vslogo.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|

## Self-Promotion

If you liked this project, star it on [GitHub](https://github.com/Roshanjossey/first-contributions).
If you're feeling especially charitable, follow [Roshan](https://roshanjossey.github.io/) on
[Twitter](https://twitter.com/sudo__bangbang) and
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
