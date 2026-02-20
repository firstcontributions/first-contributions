[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

<p align="right">

# نخستین همکاری

این پروژه قصد دارد تا راه همکاری در پروژه‌های متن‌باز را برای تازه‌کارها آسان نماید. اگر شما نیز به دنبال راهی برای ثبت نخستین همکاری خود هستید، این گام ها را دنبال کنید.

_اگر با محیط خط فرمان (CLI) احساس راحتی نمی‌کنید، [راهنمای کاربرد ابزارهای گرافیکی (GUI) را بنگرید](#آموزش-انجام-همکاری-در-دیگر-ابزارها)._

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="فورک کردن این انبار" />

#### اگر نرم‌افزار git را آماده ندارید، [از اینجا نصب کنید](https://help.github.com/articles/set-up-git/).

## انبار را فورک کنید

با کلیک کردن بر روی دکمه Fork، از انبار دلخواه یک شاخه بگیرید. این کار یک نسخه کپی از انبار را بر روی حساب کاربری شما ایجاد می‌کند.

## انبار را کلون (شبیه) کنید

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="کلون کردن این انبار" />

اکنون، از انبار فورک شده، یک کلون روی سیستم کاربری خود ایجاد کنید. وارد حساب کاربری خود شده و انبار فورک شده را باز کنید. دکمه Code را فشرده و نماد copy to clipboard را انتخاب کنید.

سپس یک ترمینال باز کنید و فرمان گیت زیر را اجرا نمایید:

```bash
git clone "url you just copied"
```

بگونه ای که در قسمت "url you just copied"، نشانی انبار فورک شده بدون علامت‌های کوتیشن (نقل قول) قرار گیرد.

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="کپی URL در کلیپ‌بورد" />

نمونه:

```bash
git clone https://github.com/this-is-you/first-contributions.git
```

به گونه ای که عبارت `this-is-you` برابر با نام حساب کاربری گیت‌هاب شما باشد. با این کار، همه محتوای مورد نیاز برای مشارکت را بر روی سیستم خود آماده می‌سازید.

### یک شاخه ایجاد کنید

اگر در مسیر انبار کلون شده نیستید، با فرمان زیر وارد مسیر انبار شوید:

```bash
cd first-contributions
```

با فرمان `git checkout` یک شاخه جدید ایجاد کنید:

```bash
git checkout -b your-new-branch-name
```

نمونه:

```bash
git checkout -b add-alonzo-church
```

(مهم نیست که در نام شاخه از واژه `add` کار بگیرید. چنانچه قرار است برای همکاری، نام خود را به یک فهرست بی افزاید، بکار گیری از این واژه برای نام شاخه، یک کار خرد مندانه می‌باشد.)

### دیگرگونی بنیادی ایجاد کرده و کامیت کنید

در این قدم، نخست فایل `Contributors.md` را در یک محیط ویرایش متن باز کنید. نام خود را به این فایل بی افزایید. آگاه باشید که نام نه در آغاز و نه در پایان نگاشته شود. نام را بین نامهای قرار دهید. فایل را ذخیره کنید.

<img align="left" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="وضعیت گیت" />

چنانچه وارد مسیر انبار شوید و فرمان `git status` را اجرا نمایید، مشاهده خواهید کرد که دیگر گونی بر روی انبار انجام شده.

با فرمان `git add`، دیگرگونی را به شاخه از پیش ساخته‌شده بی افزایید:

```bash
git add Contributors.md
```

اکنون، دیگرگونی ها را با فرمان `git commit` کامیت و ثبت نمایید:

```bash
git commit -m "Add <your-name> to Contributors list"
```

توجه داشته باشید که نام خود را با عبارت `<your-name>` جایگزین کنید.

## ویرایش ها را بفرستید (پوش کنید)

با فرمان `git push` ویرایش ثبت شده را بفرستید:

```bash
git push origin <add-your-branch-name>
```

نام شاخه ای که در گامهای پیش ایجاد کردید را با عبارت `<add-your-branch-name>` جایگزین کنید.

## ویرایش های خود را برای بررسی، ثبت کنید

چنانچه وارد انبار فورک شده در حساب کاربری خود شوید، گزینه‌ای به نام `Compare & pull request`  خواهید دید. آن را بر گزینید.

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="ایجاد یک درخواست کشش" />

در این گام، درخواست (Pull request) خود را ثبت کنید.

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="ثبت درخواست کشش" />

در پایان، من ویرایش های شما را به شاخه master پروژه خواهم افزود (merge) خواهم کرد. بی درنگ پس از مرج شدن درخواست شما، یک ایمیل بر پایه همین زمینه برای شما فرستاده خواهد شد.

## کارهای پسین

تبریک! شما گامهای فورک کردن، کلون کردن، ویرایش کردن و پول رکوئست را به خوبی پشت سر گذاشتید.

همکاری خود روی این پروژه را [از اینجا](https://firstcontributions.github.io/#social-share) با دیگر دوستان و دنبال‌کنندگان خود جشن بگیرید.

کنون، شما می‌توانید همکاری خود را روی دیگر پروژه‌ها آغاز نمایید. ما یک فهرست از پروژه‌ها با چالش های آسان پدید آوردیم که گزینه خوبی برای آغاز می‌باشد. فهرست پروژه‌ها را [از این اینجا](https://firstcontributions.github.io/#project-list) دنبال کنید.

### [آگاهی بیشتر](additional-material/git_workflow_scenarios/additional-material.md)

## آموزش انجام همکاری در دیگر ابزارها

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

</p>
