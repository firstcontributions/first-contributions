[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# أول مساهمة ليك

المشروع ده هدفه يبسّط ويوضح إزاي المبتدئين يعملوا أول contribution ليهم. لو بتدور تعمل أول contribution، اتبع الخطوات دي.

_لو مش مرتاح مع الـ command line، [اتفرج على التيوتوريالز دي اللي بتستخدم GUI tools.](#tutorials-using-other-tools)_

> 💡 **نصيحة:** الـ open source مش بس للمحترفين، حتى لو بتضيف اسمك بس، ده contribution حقيقي وبيفرق!

#### لو مش عندك git على جهازك، [ثبّته من هنا](https://docs.github.com/en/get-started/quickstart/set-up-git).

---

## 📖 مسرد المصطلحات، اعرف معنى كل كلمة قبل ما تبدأ
 
| المصطلح | معناه |
|---|---|
| **Repository (repo)** | المشروع بالكامل، كل الـ files والـ history بتاعته محفوظين فيه |
| **Fork** | نسخة من الـ repo بتتعمل في أكونتك على GitHub عشان تشتغل عليها براحتك |
| **Clone** | تحميل الـ repo من GitHub على جهازك المحلي عشان تشتغل عليه offline |
| **Branch** | نسخة موازية من الـ code بتشتغل عليها من غير ما تأثر على الـ main |
| **Commit** | حفظ التغييرات اللي عملتها مع رسالة بتوصف إيه اللي اتغير |
| **Push** | رفع الـ commits من جهازك على GitHub |
| **Pull** | جيب آخر التغييرات من GitHub على جهازك |
| **Pull Request (PR)** | طلب بتبعته لصاحب الـ repo الأصلي عشان يراجع تغييراتك ويضيفها |
| **Merge** | دمج تغييرات branch في branch تاني (غالباً في الـ main) |
| **Merge Conflict** | لما نفس السطر اتغير في مكانين مختلفين وـ Git محتاج منك تقرر تاخد إيه |
| **Staging Area** | منطقة مؤقتة بتحط فيها التغييرات اللي عايز تحفظها في الـ commit الجاي |
| **upstream** | الـ repo الأصلي اللي عملت منه fork (مش نسختك إنت) |
| **origin** | الـ repo بتاعك على GitHub (نسختك الـ forked) |
| **main** | الـ branch الرئيسي في المشروع، ده اللي الـ code الشغال بيتحفظ فيه |
 
---

## ⚠️ قبل ما تبدأ، حاجات مهمة اعرفها

- **متعملش push على الـ `main` branch أبداً**، دايماً اشتغل على branch جديد منفصل.
- **الـ fork هو نسختك الشخصية**، أي حاجة بتعملها فيه مش بتأثر على الـ repo الأصلي.
- **الـ commit message لازم يكون واضح**، اكتب إيه اللي عملته بالظبط، مش "update" أو "fix".
- **لو حصل غلط متخافش**، Git بيخليك ترجع لأي نقطة قديمة في أي وقت.

---

## الخطوة 1، عمل Fork للـ repository

اعمل fork للـ repository بالضغط على زرار الـ **fork** في أعلى الصفحة. ده هيعمل نسخة من الـ repo دي في أكونتك على GitHub.

> 📌 **إيه الفرق بين Fork و Clone؟**
> - الـ **fork** = نسخة من الـ repo على GitHub في أكونتك.
> - الـ **clone** = نسخة من الـ repo على جهازك المحلي.
> - الاتنين مع بعض = تقدر تشتغل محلياً وترفع التغييرات على أكونتك.

![عمل Fork للـ repository](https://camo.githubusercontent.com/42b18e612219cae827d8c4ee97bf15ec971f271fe60789e73a8aaeeeb42eb73f/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f666f726b2e706e67)

---

## الخطوة 2، الـ Clone بتاع الـ repository

![clone the repository](https://camo.githubusercontent.com/d4bafe4b6b8db07be80cb5d74070c2fb8ec18559711ad85ab3ae2bc576e1e9bc/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636c6f6e652e706e67)

روح على الـ forked repository في أكونتك، اضغط زرار **Code**، اختار تاب **SSH**، وانسخ الـ URL.

![copy URL to clipboard](https://camo.githubusercontent.com/fe81d0584418cc04c31a477538ec11825bceb285d865f5c34dff84180fb5adeb/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f70792d746f2d636c6970626f6172642e706e67)

افتح الـ terminal وشغّل:

```bash
git clone "الـ URL اللي نسخته"
```

> ⚡ **بيعمل إيه؟** بيجيب كل الـ files والـ history بتاع الـ project على جهازك في مجلد جديد.

---

## الخطوة 3، إنشاء branch

انتقل لمجلد الـ project:

```bash
cd first-contributions
```

> 📌 `cd` = "change directory"، بتنقلك جوه المجلد.

أنشئ branch جديد:

```bash
git switch -c اسم-الـ-branch-الجديد
```

> ⚡ **بيعمل إيه؟** بيعمل branch جديد وبيبدّل عليه في نفس الوقت. الـ `-c` = "create".
> الـ branch زي نسخة موازية من الـ code، بتشتغل عليها لوحدك من غير ما تأثر على الباقي.

مثال:

```bash
git switch -c add-mahmoud-elgohary
```

> 💡 **نصيحة:** سمّي الـ branch باسمك أو بوصف التغيير، ده بيسهّل على الفريق يفهم إيه اللي بيحصل.

<details>
<summary><strong>⚠️ لو طلعت errors مع git switch، اضغط هنا</strong></summary>

لو ظهرت رسالة `"Git: switch is not a git command"`، على الأغلب بتستخدم نسخة قديمة من git. جرّب:

```bash
git checkout -b اسم-الـ-branch-الجديد
```

</details>

---

## الخطوة 4، عمل التعديلات والـ commit

افتح ملف `Contributors.md` في أي text editor، وأضف اسمك في النص (مش في الأول ولا في الآخر). بعدين save الملف.

تأكد إن التغييرات اتحفظت:

```bash
git status
```

> ⚡ **بيعمل إيه؟** بيوريك الـ files اللي اتغيرت، باللون الأحمر (مش متضافة لسه) أو الأخضر (جاهزة للـ commit).

أضف الملف للـ staging area:

```bash
git add Contributors.md
```

> ⚡ **بيعمل إيه؟** بيقول لـ Git "الملف ده هو اللي عايز أحفظه في الـ commit الجاي".
> لو عايز تضيف كل التغييرات دفعة واحدة: `git add .`

عمل commit:

```bash
git commit -m "Add your-name to Contributors list"
```

> ⚡ **بيعمل إيه؟** بيحفظ snapshot من التغييرات مع رسالة بتوصفها.

> ⚠️ **الـ commit message مهم جداً:**
> - ✅ `"Add Mahmoud Elgohary to Contributors list"`
> - ❌ `"update"` أو `"fix"` أو `"done"`

---

## الخطوة 5، رفع التغييرات على GitHub

```bash
git push -u origin اسم-الـ-branch-بتاعك
```

> ⚡ **بيعمل إيه؟** بيرفع الـ branch من جهازك على GitHub. الـ `-u origin` بتربط الـ local branch بالـ remote عشان المرة الجاية تكتب `git push` بس.

<details>
<summary><strong>⚠️ لو طلعت errors وانت بتعمل push، اضغط هنا</strong></summary>

### Authentication Error

لو ظهرت رسالة إن الـ password authentication اتشالت، اعمل SSH key وربطه بأكونتك عن طريق [التيوتوريال ده](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

شيّك على الـ remote address بتاعك:

```bash
git remote -v
```

لو شايف `https://` مش `git@github.com` غيّره بالأمر ده:

```bash
git remote set-url origin git@github.com:username-بتاعك/your_repo.git
```

</details>

---

## الخطوة 6، تقديم الـ pull request للمراجعة

روح على الـ repo بتاعك على GitHub، هتلاقي زرار **Compare & pull request**. اضغط عليه.

![compare and pull request](https://camo.githubusercontent.com/af350925874cc9d92469b7800b819295f2b8da906486a169b54a874a30d75ded/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f6d706172652d616e642d70756c6c2e706e67)

بعدين اضغط **Submit pull request**.

![submit pull request](https://camo.githubusercontent.com/87bc1d6af5a0c15e6ed798ff80fe57efe8a145c47e98ba16245350ebdfd13007/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f7375626d69742d70756c6c2d726571756573742e706e67)

> 📌 **الـ pull request بيعمل إيه؟** بيقول لصاحب الـ repo الأصلي "عندي تغييرات، ممكن تراجعها وتضيفها؟"
>
> 💡 **نصيحة:** في خانة الـ description، اكتب بإيجاز إيه اللي عملته وليه، ده بيساعد الـ maintainer يراجع أسرع.

قريباً هيتعمل merge لتغييراتك في الـ main branch وهتوصلك notification بالإيميل.

---

## 🛠️ أوامر Git مهمة تعرفها

| الأمر | بيعمل إيه |
|---|---|
| `git status` | بيوريك الـ files اللي اتغيرت وحالتها |
| `git log --oneline` | بيوريك تاريخ الـ commits بشكل مختصر |
| `git diff` | بيوريك الفرق التفصيلي في الـ code قبل الـ add |
| `git stash` | بيخفي تغييراتك مؤقتاً من غير ما تعمل commit |
| `git stash pop` | بيرجّع التغييرات اللي خبيتها |
| `git pull` | بيجيب آخر تحديثات من الـ remote |
| `git branch` | بيوريك كل الـ branches اللي عندك |
| `git branch -d اسم-الـ-branch` | بيمسح branch بعد ما تخلص منه |

---

## 🆘 حلول لأشهر المشاكل

<details>
<summary><strong>عملت commit بالغلط، عايز أتراجع</strong></summary>

تراجع عن آخر commit من غير ما تمسح التغييرات:

```bash
git reset --soft HEAD~1
```

تراجع ومسح التغييرات خالص **(خطر، مش هترجع)**:

```bash
git reset --hard HEAD~1
```

</details>

<details>
<summary><strong>الـ branch بتاعي بقى متأخر عن الـ main الأصلي</strong></summary>

```bash
git switch main
git pull upstream main
git switch اسم-الـ-branch-بتاعك
git rebase main
```

</details>

<details>
<summary><strong>طلع merge conflict، إيه اللي أعمله؟</strong></summary>

الـ merge conflict بيحصل لما نفس السطر اتغير في مكانين مختلفين. Git بيحطلك علامات في الملف كده:

```
<<<<<<< HEAD
التغيير بتاعك
=======
التغيير التاني
>>>>>>> branch-name
```

افتح الملف، اختار التغيير الصح أو ادمج الاتنين، امسح العلامات، وبعدين:

```bash
git add الملف-اللي-عدّلته
git commit
```

</details>

---

## تعمل إيه بعد كده؟

مبروك! 🎉 إنت خلّصت الـ workflow الأساسي:

**fork → clone → branch → edit → commit → push → pull request**

ده اللي هتشتغل بيه في أي open source project من دلوقتي.

لو عايز تتدرب أكتر، اتفرج على [code contributions](https://github.com/roshanjossey/code-contributions).

ودلوقتي خد نظرة على [قائمة الـ projects](https://firstcontributions.github.io/#project-list) اللي فيها issues سهلة تبدأ بيها.

---

## Tutorials باستخدام Tools تانية

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
