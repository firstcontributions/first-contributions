[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/)


# 🇸🇾 أول مساهمة إلك بهالمشروع

👋 أهلاً وسهلاً بكل المساهمين!

نحن كتير مبسوطين بانضمامك لهالمشروع المفتوح المصدر! مساهمتك رح تساعدنا نكبر ونطوّر أكتر، وكل تعديل منك إلو قيمة كبيرة. إذا عندك أي سؤال أو فكرة، لا تتردد تشاركنا. سوا فينا نعمل فرق ونبني مجتمع قوي ومفيد للجميع. 💪


هالمشروع هدفه يسهّل الطريق للمبتدئين ليعملوا أول مساهمة إلهم بالمشاريع مفتوحة المصدر. إذا بدك تبلّش وتعمل أول مساهمة، اتبع الخطوات الجاية:

 إذا ما بتعرف تشتغل عالـ Command Line  
فيك تشوف [هالدروس باستخدام أدوات واجهة رسومية](#دروس-باستخدام-أدوات-تانية).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />


#### إذا ماعندك ´git´ على جهازك, فينك تنزلها من الرابط [حمل git](https://docs.github.com/en/get-started/quickstart/set-up-git).


##  أول خطوة: اعمل Fork للمستودع  

اضغط على زر **Fork** فوق بهالصفحة. هيك بتصير عندك نسخة من المستودع بحسابك.



##  ثاني خطوة: اعمل Clone للمستودع  
افتح حسابك عالـ GitHub، فوت عالنسخة يلي عملتلها Fork، واضغط على زر **Code**، بعدين اختار تبويب **SSH** واضغط على أيقونة **Copy URL to clipboard**.

افتح التيرمنال واكتب الأمر التالي:

```bash
git clone "الرابط يلي نسختو"
```

وين "الرابط يلي نسختو هلأ" (بدون الإشارات) هو الرابط لهالمستودع (النسخة يلي عملتها من هالمشروع). شوف الخطوات السابقة لتجيب الرابط.


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />


مثال:
```bash
git clone git@github.com:this-is-you/first-contributions.git
```


وين `this-is-you` هو اسم المستخدم تبعك على GitHub. هون عم تنسخ محتويات مستودع first-contributions من GitHub لجهازك.


##  ثالث خطوة: أنشئ فرع جديد  

غيّر للمجلد تبع المستودع على جهازك (إذا ما كنت فيه أساسًا):
```bash
cd first-contributions
```

وبعدين أنشئ فرع جديد:
```bash
git switch -c اسم-الفرع-الجديد
```

مثلا:
```bash
git checkout -c اضافة-لغة-جديدة
```


<details>
<summary><strong>إذا طلع معك أي خطأ وقت تستخدم git switch، كبس هون:</strong></summary>

إذا ظهرت رسالة الخطأ "Git: `switch` مو أمر git. شوف `git --help`"، غالبًا السبب إنك عم تستخدم نسخة قديمة من git.

بهالحالة، جرب تستخدم `git checkout` بدلها:

```bash
git checkout -b اسم-الفرع-الجديد-تبعك
```

</details>



##  عدّل وأضف اسمك  

هلق افتح ملف `Contributors.md` بأي محرر نصوص، وضيف اسمك عليه. لا تحطّه بأول الملف ولا بآخره، حطّه بنصّ الملف. بعدين احفظ التغييرات.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

إذا بتروح على مجلد المشروع وبتنفّذ الأمر `git status`، رح تشوف إنو صار في تغييرات.
ضيف هالتغييرات على الفرع يلي أنشأته باستخدام أمر `git add`:

```bash
git add Contributors.md
```

هلق ثبت التغييرات باستخدام أمر `git commit`:
```bash
git commit -m "ضيف اسمك على قائمة المساهمين"
```

## ادفع التغييرات على GitHub

ادفع التغييرات باستخدام الأمر `git push`:

```bash
git push -u origin اسم-الفرع-تبعك
```

بدّل `اسم-الفرع-تبعك` باسم الفرع يلي أنشأته قبل شوي.


<details>
<summary><strong>إذا طلع معك أي خطأ وقت الدفع، كبس هون:</strong></summary>

*   ### مشكلة التوثيق (Authentication Error)

        remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
        remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
        fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'

    روح لهون شرح 
    [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
     لتوليد وضبط مفتاح SSH على حسابك.

    كمان فيك تشغّل الأمر:

    ```bash
    git remote -v
    ```

    لتتأكد من عنوان الريموت.

    إذا شكله هيك:

        origin  https://github.com/your-username/your_repo.git (fetch)
        origin  https://github.com/your-username/your_repo.git (push)

    غيّره بهالأمر:

    ```bash
    git remote set-url origin git@github.com:your-username/your_repo.git
    ```

    غير هيك رح يضل يطلب منك اسم المستخدم والباسوورد ويعطيك خطأ بالتوثيق.

</details>






تمام، رح أترجم لك هالجزء كمان باللهجة السورية وبصيغة **Markdown**:

***

## قدّم تغييراتك للمراجعة

إذا بتروح على المستودع تبعك على GitHub، رح تشوف زر اسمه `Compare & pull request`. كبس عليه.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

هلق قدّم طلب السحب (Pull Request).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

قريباً رح أدمج كل تغييراتك مع الفرع الرئيسي للمشروع. رح توصلك إيميل إشعار وقت يخلص الدمج.



## وين تروح من هون؟

مبروك! خلصت هلأ الخطوات الأساسية يلي غالباً رح تواجهها كمساهم:  
*فورك → كلون → تعديل → طلب سحب (Pull Request)* 🎉

احتفل بمساهمتك وشاركها مع رفقاتك والمتابعين من خلال التطبيق عالويب [web app](https://firstcontributions.github.io/#social-share).

إذا بدك تتمرّن أكتر، شوف مساهمات الكود [code contributions](https://github.com/roshanjossey/code-contributions).

وهلق خلينا نبلّش نساعدك تساهم بمشاريع تانية. جمعنا لك قائمة مشاريع فيها مشاكل سهلة لتبلّش فيها. شوف قائمة المشاريع بالتطبيق عالويب [the list of projects in the web app](https://firstcontributions.github.io/#project-list).


### [Additional material](docs/additional-material/git_workflow_scenarios/additional-material.md)

---

## 📚 دروس باستخدام أدوات تانية  
| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
