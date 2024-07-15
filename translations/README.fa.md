[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

<p align="right">

# اولین مشارکت

این پروژه قصد دارد تا مسیر مشارکت در پروژه‌های متن‌باز را برای تازه‌کارها آسان نماید. اگر شما نیز به دنبال راهی برای ثبت اولین مشارکت خود هستید، این اقدامات را دنبال کنید.

_اگر با محیط کامندی (CLI) احساس راحتی نمی‌کنید، [راهنمای استفاده از ابزارهای گرافیکی (GUI) را مشاهده کنید](#آموزش-انجام-مشارکت-در-دیگر-ابزارها)._

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### اگر نرم‌افزار git را آماده ندارید، [از اینجا نصب کنید](https://help.github.com/articles/set-up-git/).

## مخزن را فورک کنید

با کلیک کردن بر روی دکمه Fork، از مخزن مورد نظر یک انشعاب بگیرید. این عملیات یک نسخه کپی از مخزن را بر روی حساب کاربری شما ایجاد می‌کند.

## مخزن را کلون (شبیه) کنید

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

حال، از مخزن فورک شده، یک کلون روی سیستم کاربری خود ایجاد کنید. وارد حساب کاربری خود شده و مخزن فورک شده را باز کنید. دکمه Code را فشرده و نماد copy to clipboard را انتخاب کنید.

سپس یک ترمینال باز کنید و دستور گیت زیر را اجرا نمایید:

```bash
git clone "url you just copied"
```

بطوری که در قسمت "url you just copied"، آدرس مخزن فورک شده بدون علامت‌های کوتیشن (نقل قول) قرار گیرد.

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

بعنوان مثال:

```bash
git clone https://github.com/this-is-you/first-contributions.git
```

به طوری که عبارت `this-is-you` برابر با نام حساب کاربری گیت‌هاب شما باشد. با این اقدام، تمام محتوای مورد نیاز جهت مشارکت را بر روی سیستم خود آماده می‌سازید.

### یک شاخه ایجاد کنید

اگر در مسیر مخزن کلون شده قرار ندارید، با دستور زیر وارد مسیر مخزن شوید:

```bash
cd first-contributions
```

با استفاده از دستور `git checkout` یک شاخه جدید ایجاد کنید:

```bash
git checkout -b your-new-branch-name
```

بعنوان مثال:

```bash
git checkout -b add-alonzo-church
```

(هیچ لزومی نیست که در نام شاخه از کلمه `add` استفاده کنید. چنانچه قرار است بعنوان مشارکت، نام خود را به یک لیست اضافه کنیم، استفاده از این کلمه بعنوان نام شاخه، امری عاقلانه می‌باشد.)

### تغییرات اساسی ایجاد کرده و کامیت کنید

در این قدم، ابتدا فایل `Contributors.md` را در یک محیط ویرایش متن باز کنید. نام خود را به این فایل اضافه کنید. توجه کنید که نام نه در ابتدا و نه در انتها قرار گیرد. نام را بین اسامی قرار دهید. فایل را ذخیره کنید.

<img align="left" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

چنانچه وارد مسیر مخزن شوید و دستور `git status` را اجرا نمایید، مشاهده خواهید کرد که تغییراتی بر روی مخزن اعمال شده.

با استفاده از دستور `git add`، تغییرات را به برنچ از پیش ساخته‌شده اضافه کنید:

```bash
git add Contributors.md
```

حال، تغییرات را با دستور `git commit` کامیت و ثبت نمایید:

```bash
git commit -m "Add <your-name> to Contributors list"
```

توجه داشته باشید که نام خود را با عبارت `<your-name>` جایگزین کنید.

## تغییرات را ارسال (پوش) کنید

با استفاده از دستور `git push` تغییرات ثبت شده را ارسال کنید:

```bash
git push origin <add-your-branch-name>
```

نام برنچی که در مراحل قبل ایجاد کردید را با عبارت `<add-your-branch-name>` جایگزین کنید.

## تغییرات خود را برای بررسی، ثبت کنید

چنانچه وارد مخزن فورک شده در حساب کاربری خود شوید، گزینه‌ای تحت عنوان `Compare & pull request` مشاهده خواهید کرد. آن گزینه را انتخاب کنید.

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

در این مرحله، درخواست (Pull request) خود را ثبت کنید.

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

نهایتا، من تغییرات شما را به برنچ master پروژه اضافه (merge) خواهم کرد. بلافاصله پس از مرج شدن درخواست شما، یک ایمیل مبنی بر همین موضوع برای شما ارسال خواهد شد.

## اقدامات بعدی

تبریک! شما مراحل فورک کردن، کلون کردن، ایجاد تغییرات و پول رکوئست را به خوبی پشت سر گذاشتید.

مشارکت خود روی این پروژه را [از اینجا](https://firstcontributions.github.io/#social-share) با دیگر دوستان و دنبال‌کنندگان خود جشن بگیرید.

همچنین شما می‌توانید [از اینجا](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)، وارد تیم Slack ما شوید و سوالات خود را مطرح نمایید.

حال، شما می‌توانید مشارکت خود را روی دیگر پروژه‌ها آغاز نمایید. ما یک لیست از پروژه‌ها با مشکلات ساده ایجاد کردیم که گزینه خوبی برای شروع می‌باشد. لیست پروژه‌ها را [از این اینجا](https://firstcontributions.github.io/#project-list) دنبال کنید.

### [اطلاعات بیشتر](additional-material/git_workflow_scenarios/additional-material.md)

## آموزش انجام مشارکت در دیگر ابزارها

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

</p>
