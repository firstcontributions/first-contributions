
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# پہچھِ پہلی حصہ داری۔

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|

یہ وُہ ہِک گائِڈ چھُ، جو ٹرمِنَل کے ماہر ہیں، ژہ ٹرمِنَل کے وچ سَربٲ کَرُن چاہن۔ اور شکریہ [Github-CLI](https://cli.github.com/), توہہِاں پہچھِ پہلی حصہ داری کے یاد رکھہ کرن، آسَن حاصل چھُ۔
مزہ، فائدہ مند اور جاری رکھن تِہِ ہِک محرک بنو!

یہ گائِڈ تھوڑا زیادہ مشکل چھُ، چوں ژہ کسے وی گرافیکل انٹرفیس نہ استعمال پٲٹُھ، پر یہ ابھی بھی وُہ بہت مزہ دی چھُ، اور تس توہہِاں بخوبی اس کی پیروی کر سکتے ہو!

پہلی شرط ہے کہ
- گٹ انسٹال چھُ۔ [git](انسٹال کرنے کا طریقہ)(https://git-scm.com/downloads)
- گیتھب اکاؤنٹ

ہن ہمیں انسٹال کرن ضروری چھُ `github-cli` ہمارا سسٹم تے ٹول دَڑھ تھِس اَے [official documentation](https://github.com/cli/cli#installation)

اس کے بعد ہمیں CLI تے لاگ ان کرن ضروری چھُ، لہٰذا یہ کمانڈ درج کر:
```bash 
gh auth login
```

ہدایات تے عمل کر اور ہم تیار ہیں!

# اس ذخیرے کو فورک کرن۔
یہ اتنا ہی آسان چھُ جتھ کمانڈ چلائیو:
```bash
gh repo fork firstcontributions/first-contributions
```
**اہم: یہ آپ کو اشارہ کرے گا کہ اگر آپ اسے بھی کلون کرنا چاہتے ہیں تو "ہاں" کا اختیار منتخب کریں۔**

# اپنی برانچ بناؤ
ہم یہ مرحلہ گٹ کے ساتھ کریں گے، اس لیے اس کمانڈ کو اپنے نام سے بدلتے ہوئے درج کریں، مثال کے طور پر:
```bash 
git switch -c add-john-doe
```

# ضروری تبدیلیاں کرن اور ان تبدیلیوں کا ارتکاب کرن۔ 
اب آپ کھول سکتے ہیں `Contributors.md` فائل کو ٹیکسٹ ایڈیٹر میں اور اس میں اپنا نام شامل کریں۔ اپنا نام شروع اور اختتام کے درمیان کہیں بھی رکھو، پھر فائل کو محفوظ کریں۔

پروجیکٹ ڈائرکٹری میں عملدرآمد کرو۔ `git status` اور آپ تبدیلیاں دیکھو گے。
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

ان تبدیلیوں کو اس برانچ میں شامل کرن، جے کرن جو تسی نے پہلے استعمال کر کے بنائی چھُ۔ `git add` کمانڈ:
`git add Contributors.md`

اب ان تبدیلیوں کا ارتکاب کرن `git commit` کمانڈ:
`git commit -m "Add your-name to Contributors list"`
تبدیل کرن `your-name` آپ کے نام سے

# تبدیلیوں کو گیتھب میں دبائیں۔ 
کمانڈ استعمال کر کے اپنی تبدیلیوں کو آگے بڑھاؤ۔ `git push`:

```
git push origin -u your-branch-name
```

تبدیل کرن `your-branch-name` اس برانچ کے نام کے ساتھ جو آپ نے پہلے بنائی تھی۔

<details>
<summary> <strong>اگر آپ کو دھکیلتے وقت کوئی غلطی ہو جاتی ہے تو، یہاں کلک کریں:</strong> </summary>

- ### تصدیق کی غلطی
     <pre>ریموٹ: پاس ورڈ کی توثیق کے لیے سپورٹ 13 اگست 2021 کو ہٹا دیا گیا تھا۔ براہ کرم اس کے بجائے ذاتی رسائی کا ٹوکن استعمال کریں。
 remote: براہ کرم دیکھیں https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ مزید معلومات کے لیے.
  fatal: کے لیے توثیق ناکام ہو گئی۔ 'https://github.com/<your-username>/first-contributions.git/'</pre>
  کے پاس جاؤ [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) اپنے اکاؤنٹ میں SSH کلید بنانے اور ترتیب دینے پر۔

</details>

# جائزہ کے لیے اپنی تبدیلیاں جمع کرواؤ۔
اب اس کمانڈ کو ہماری ریپو کی ڈائرکٹری میں چلانے سے ہمیں نظرثانی کے لیے پل کی درخواست بنانے کی اجازت ملے گی۔

```bash 
gh pr create --repo firstcontributions/first-contributions
```

اس کے بعد پل کی درخواست جمع کرواؤ۔

آپ کمانڈ استعمال کر سکتے ہیں۔ `gh status` آپ کی ذکر کردہ پل کی درخواست کو عمل میں دیکھنے کے لیے۔

## یہاں سے کہاں جانا ہے؟

مبارک ہو! آپ نے ابھی معیاری _fork -> کلون -> ترمیم -> pull request_ ورک فلو مکمل کیا ہے جس کا آپ کو اکثر شراکت دار کے طور پر سامنا ہوگا!

اپنی شراکت کا جشن مناؤ اور اپنے دوستوں اور پیروکاروں کے ساتھ اس کا اشتراک کرو۔[web app](https://firstcontributions.github.io/#social-share).

اگر آپ کو کوئی مدد درکار ہو یا کوئی سوال ہو تو آپ ہماری سلیک ٹیم میں شامل ہو سکتے ہیں۔ [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

اب آئیے آپ کو دوسرے پروجیکٹس میں حصہ ڈالنا شروع کرتے ہیں۔ ہم نے آسان مسائل کے ساتھ پروجیکٹس کی ایک فہرست مرتب کی ہے جس پر آپ شروع کر سکتے ہیں۔ اس کو دیکھو [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [اضافی مواد](additional-material/git_workflow_scenarios/additional-material.md)

## دوسرے ٹولز کا استعمال کرتے ہوئے سبق

[مرکزی صفحہ پر واپس جائیں۔](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
