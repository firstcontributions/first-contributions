# پہل تعاون – First Contributions

[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


## پروجیکٹک مقصد

یہ پروجیکٹ نوآموزن ہند مدد کرن تہ رہنمائی کرن خٲطرہ بنٲون آمُت چھُ، یِتھ سیتھ تِم آسانی سان پنن پہل اوپن سورس تعاون کٔرتھ ہیکن۔

اگر توہیہ پنن پہل تعاون کرُن چھاہیو، تیلے یِم نیبر دِتھ قدم فالو کرِو۔

_اگر توہیہ کمانڈ لائن استعمال کرنس منز آرام دہ نِہ چھو، تیلے GUI ٹولزن سیتھ ٹیوٹوریل دستیاب چھ۔_
<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />




## ر Git انسٹال کرُن

اگر توہند کمپیوٹرنس پیٹھ git انسٹال نِہ چھُ، تیلے اتھ انسٹال کرِو:

https://docs.github.com/en/get-started/quickstart/set-up-git


## قدم 2 – ریپوزیٹری فورک کرُن

یِہ پیجک پیٹھ موجود **Fork** بٹن پیٹھ کلک کرنہ سیتھ یِہ ریپوزیٹری فورک کرِو۔  
یِمن عملہ سیتھ یِہ ریپوزیٹری ہُنٛد نقل توہند GitHub اکاؤنٹس منز بنِہ۔



## قدم 3 – ریپوزیٹری کلون کرُن
<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the repository" />
ونہِ فورک کرمت ریپوزیٹری پننس کمپیوٹرنس پیٹھ کلون کرِو۔

پننس GitHub اکاؤنٹس منز گژھِو، فورک کرمت ریپوزیٹری کھولِو، “Code” بٹن پیٹھ کلک کرِو، SSH ٹیب ژارِو تہ URL کاپی کرِو۔

ٹرمنل کھولِو تہ یِہ کمانڈ چلٲو:

```bash
git clone "url you just copied"
```

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />
مثال:
```bash
git clone git@github.com:this-is-you/first-contributions.git
```

یتھہ this-is-you توہند GitHub یوزرنیم چھُ۔

قدم 4 – نوو برانچ بنٲوُن

ریپوزیٹری ڈائریکٹری منز گژھِو:
```bash
cd first-contributions
```

نوو برانچ بنٲوِو:
```bash
git switch -c your-new-branch-name
```
مثال:
```bash
git switch -c add-alonzo-church
```
<details>  
<summary> <strong>اگر یِمۍ تُہۍ git switch استعمال کران وِز کُنہِ غلطی آیہٕ، یَتھ پٲٹھۍ کلِک کٔرِو:</strong> </summary>  

اگر غلطی پیغام "Git: `switch` is not a git command. See `git –help`" ظاہر گژھِ، تَتھٕ ہُند مطلب یہ چھُ کہ تُہۍ git ہُند پرٛان وٲژن استعمال کران چھُو۔

اَسہِ حالتس منٛز، `git checkout` استعمال کرُن ہُند کوشش کٔرِو:

```bash
git checkout -b your-new-branch-name
```

</details>

## قدم 5 – تبدیلی کرُن تہ Commit کرُن

Contributors.md فایل کھولِو

اتھ منز پنُن ناو شامل کرِو

فائل محفوظ کرِو
<img align="left" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ونہِ یِہ کمانڈ چلٲو:
```bash
git status
```

تبدیلی شامل کرنہ خٲطرہ:
```bash
git add Contributors.md
```

Commit کرنہ خٲطرہ:
```bash
git commit -m "Add your-name to Contributors list"
```

“your-name” بدلہ پنُن ناو لیکھِو۔

 ## قدم 6 – تبدیلی GitHub پیٹھ Push کرُن
```bash
git push -u origin your-branch-name
```

“your-branch-name” بدلہ پنُن برانچک ناو لیکھِو۔
<details>  
<summary> <strong>اگر push کران وِز کُنہِ غلطی آیہٕ، یَتھ پٲٹھۍ کلِک کٔرِو:</strong> </summary>  

* ### Authentication Error

     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.  
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.  
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>  

  SSH key بنٲوُن تہ پننس اکاؤنٹس سۭتۍ configure کرُن خٲطرٕ GitHub ہُند tutorial وُچھِو۔

  اَسہِ علاوہ، remote address چیک کرُن خٲطرٕ یہ کمانڈ چَلاوُن:

  `git remote -v`

  اگر یہ یِمۍ پٲٹھۍ وُچھِ:

  <pre>origin	https://github.com/your-username/your_repo.git (fetch)  
  origin	https://github.com/your-username/your_repo.git (push)</pre>  

  تہ یہ کمانڈ استعمال کٔرِو تام change کرُن خٲطرٕ:

  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```

  نَتہ تُہۍ ہنوز username تہ password خٲطرٕ prompt گژھِو تہ authentication error آیہٕ۔

</details>

## پنٕنۍ تبدیلیاں جائزہ خٲطرٕ جمع کرِو

  پننس GitHub ریپوزیٹری پیٹھ گژھِو، تہ توہیہ Compare & pull request بٹن وُچھِو۔

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />
اتھ پیٹھ کلک کرِو تہ pull request جمع کرِو۔


<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
ژٹہِ وقتس منز توہند تبدیلی مین برانچس سیتھ مرج گژھن۔
توہیہ ای میل نوٹیفکیشن رَٹِو جب تبدیلی منظور گژھِتھ۔

## یِتھہ پتہ کِتھ گژھن؟

مبارک! 🎉
توہیہ کامیابی سان معیاری ورک فلو مکمل کرمُت:

fork → clone → edit → pull request

یُس اوپن سورس دنیاس منز عام طور استعمال گژھان چھُ!

مزيد مشق

اگر توہیہ مزيد مشق چھاہیو، تیلے یِہ چیک کرِو:
https://github.com/roshanjossey/code-contributions

دُسریں آسان پروجیکٹن ہند فہرست:
https://firstcontributions.github.io/#project-list
[**وَڌھ مواد**](/additional-material/git_workflow_scenarios/additional-material.md)



GUI ٹولزن سیتھ ٹیوٹوریل

## توہیہ یِم ٹول تہِ استعمال کٔرتھ ہیکو:



| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |


توہند پہل اوپن سورس تعاونس خٲطرہ بہت بہت مبارک! 🚀
