[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# <div dir="rtl"> پہلی شراکت يا کانٹریبیوشن </div>

<div dir="rtl">
اس پروجیکٹ کا مقصد ابتدائی افراد کے اپنا پہلى شركت يا کانٹریبیوشن کرنے کے طریقے کو آسان بنانا اور رہنمائی کرنا ہے۔ اگر آپ اپنا پہلا حصہ ڈالنا چاہتے ہیں تو نیچے دیے گئے مراحل پر عمل کریں۔
</div>
<br />
<div dir="rtl">
اگر آپ کمانڈ لائن سے واقف نہیں ہیں تو، یہاں 
<a href="#tutorials-using-other-tools">جى يو آئ ٹولز استعمال کرنے كا طریقہ</a>
 موجود ہے۔
</div>
<br />
<div dir="rtl">
اگر آپ کی مشین پر گٹ نہیں ہے تو،
<a href="https://help.github.com/articles/set-up-git/">انسٹال کریں</a>
</div>

## <div dir="rtl"> اس ریپوزٹری کو فورک کریں </div>
<div dir="rtl">
اس صفحے کے سب سے اوپر فورک بٹن دبا کر اس ریپوزٹری کا استعمال کریں.

<img style="float: left" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="اس ریپوزٹری کوفورک کریں" />
<br />

یہ آپ کے اکاؤنٹ میں اس کی ایک نقل بنا كے ذخیرہ کرے گا۔.
</div>
<br />

## <div dir="rtl">ریپوزٹری کا کلون کیجیے</div>

<div dir="rtl">
اب آپ اپنے کمپیوٹر مشین پر یہ ریپوزٹری کلون کریں.
</div>

<img style="float: left;" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="ریپوزٹری کا کلون کیجیئے" />

<div dir="rtl">
 کلون بٹن کو دبائیں اور پھر "copy to clipboard" آئیکن کو دبائیں۔
</div>

<img style="float: left;" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="یوآرایل کلپ بورڈ پر کاپی کریں" />

<div dir="rtl">
ایک ٹرمینل کھولیں اور مندرجہ ذیل گٹ کمانڈ چلائیں:
</div>

```bash
git clone "یو آر ایل جو آپ نے ابھی کاپی کیا"
```

<div dir="rtl">
جہاں "یو آر ایل جو آپ نے ابھی کاپی کیا" (اقتباس کے نشانات " " کے بغیر) اس ریپوزٹری کو کلون کرنے کا  یو آر ایل کا اندراج مراد ہے. یو آر ایل حاصل کرنے کیلئے پچھلے مرحلے کو دیکھیں.
</div>

<div dir="rtl">مثال کے طور پر:</div>

```bash
git clone https://github.com/this-is-you/first-contributions.git
```

<div dir="rtl">اس میں 'this-is-you' آپکا GitHub یوزرنیم ہے۔ یہاں آپ first-contributions GitHub ریپوزٹری کے مندرجات کمپیوٹر پر نقل کر رہے ہیں.</div>

## <div dir="rtl"> ایک شاخ (برانچ) بنائیں </div>

<div dir="rtl"> اپنے کمپیوٹر پر ریپوزٹری کی ڈائرکٹری تبدیل کریں (اگرآپ پہلے سے وہاں نہیں ہیں): </div>

```bash
cd first-contributions
```

<div dir="rtl"> اب <code>git checkout</code>  کمانڈ استعمال کرتے ہوئے ایک شاخ/برانچ  تشکیل دیں : </div>

```bash
git checkout -b <add-your-name>
```

<div dir="rtl">مثال کے طور پر:</div>

```bash
git checkout -b add-alonzo-church
```

<div dir="rtl"> شاخ (برانچ) کا نام میں ضروری نہیں <i>add</i> شامل کریں، لیکن یہ مناسب ہے کہ اس میں یہ شامل ہو، کیونکہ اس شاخ کا مقصد آپ کے نام کو فہرست میں شامل کرنا ہے. </div>

## <div dir="rtl"> ضروری تبدیلیاں کریں اور ان تبدیلیوں کو انجام دیں۔ </div>

<div dir="rtl">
اب <code>Contributors.md</code> فائل کو ٹیکسٹ ایڈیٹر پر کھولیں، اپنا نام اس میں شامل کریں، اور پھر فائل کو محفوظ کریں۔ نام فائل کے شروع یا آخر میں شامل نہ کریں۔ اسے درمیان میں کہیں بھی ڈال دیں۔اگر آپ پراجیکٹ ڈائرکٹری میں جاتے ہیں اور کمانڈ <code>git status</code> کو چلاتے ہیں، تو آپ دیکھیں گے کہ تبدیلیاں موجود ہیں. ان تبدیلیوں کو اس شاخ میں <code>git add</code> کمانڈ استعمال کرتے ہوئے شامل کریں، جسے ابھی آپ نے بنایا تھا۔ :
</div>

```bash
git add Contributors.md
```

<div dir="rtl"> اب <code>git commit</code> کمانڈ کا استعمال کرتے ہوئے ان تبدیلیوں کا ارتکاب کریں: </div>

```bash
git commit -m "Add <your-name> to Contributors list"
```

<div dir="rtl"> <code>&lt;your-name&gt;</code> کو اپنے نام کے ساتھ تبدیل کردیں. </div>

## <div dir="rtl"> ان تبدیلیوں کو GitHub پردهکیل دیں۔ </div>

<div dir="rtl"> <code>git push</code> کمانڈ کے ذریعے اپنی تبدیلیوں کو پش کریں: </div>

```bash
git push origin <add-your-name>
```

<div dir="rtl"> <code>&lt;add-your-name&gt;</code> کو شاخ کے نام کے ساتھ بدل دیں، جسے آپ نے پہلے بنایا تھا. </div>

## <div dir="rtl">  اپنی تبدیلیوں کو جائزے کیلئے جمع کروائیں۔ </div>

<div dir="rtl"> اگر آپ GitHub پر اپنی ریپوزٹری پر جاتے ہیں تو، آپ کو <code>Compare & pull request</code> دکھائی دے گا. اس بٹن کو دبائیں. </div>

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="ایک پل درخواست کریں" />

<div dir="rtl"> اب پل درخواست جمع کروائیں. </div>

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="پل درخواست جمع کروائیں" />

<div dir="rtl"> جلد ہی میں آپ کی تمام تبدیلیوں کو اس پروجیکٹ کی ماسٹر شاخ میں ضم کر دونگا. تبدیلیوں کو ضم کرنے کے بعد آپ کو نوٹیفکیشن ای میل مل جائے گی </div>

## <div dir="rtl">آگے کیا کرنا چاہیے؟</div>
<div dir="rtl">
مبارک ہو! آپ نے کامیابی سے 
 فورک -> کلون -> ترمیم -> پل ریکویسٹ ورک فلو 
 مکمل کر لیا ہے جو آپ کو اکثر ایک شراکت دار کے طور پر ملے گا

اپنی شراکت کا جشن منائیں اور اپنے دوستوں اور فالوورز کے ساتھ اسے
<a href="https://firstcontributions.github.io/#social-share"> ویب ایپ</a>
 پر جا کر شیئر کریں۔
</div>
<div dir="rtl">
  آپ کو مدد کی ضرورت ہے یا کوئی سوال ہو تو آپ ہماری سلیک ٹیم میں بھی شامل ہوسکتے ہیں.
<a href="https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA">سلیک ٹیم میں شمولیت اختیار کریں۔</a>
</div>
<br />
<div dir="rtl">
اب ہم آپ کو دوسرے پراجيكٹس میں شراکت کرنے کے لئے دعوت ديتے ہیں۔ 
ادھر آپ چند
<a href="https://firstcontributions.github.io/#project-list"> مقبول ذخیروں</a>
  میں کچھ ابتدائی سطح کے مسائل حل کر سکتے ہیں. آگے بڑھیے اور مزید جاننے کے لئے ان ذخیروں پر جائیے۔
</div>

### <div dir="rtl"> [ اضافی مواد ](../additional-material/git_workflow_scenarios/additional-material.md) </div>

## <div dir="rtl"> دوسرے ٹولز کو استعمال کرتے ہوئے سبق۔   </div>


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

<div dir="rtl">  
اس منصوبے کی حمایت کی ہے
</div>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
