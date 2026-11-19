[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# پٔہلہ اوپن سورس شراکت

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

یہِ گائیڈ چھُ تِمَن لوٗکن خٲطرٕ یِم ٹرمِنل استعمال کرنہٕ پسند کران چھِ تہٕ پنُن سٲری کام ٹرمِنل منٛز کرُن چاہان۔ **GitHub CLI** ہُند استعمال کرِتھ تُہۍ آسانی سان پنُن پٔہلہ اوپن سورس تعاون کٔرِتھ۔ یاد تھٲو کہ پٔہلہ تعاون چھُ مزٕدار، حوصلہ افزا تہٕ سیکھنہٕ خٲطرٕ ایک اہم قدم۔

یہِ گائیڈ چھُ ذرا مشکل، کیازِ اَسہِ کُنہِ تہِ گرافیکل انٹرفیسُک استعمال نہٕ کران، مگر اگر تُہۍ نیچے دِیِتھ ہدایتَن پیروٕی کرِو، تہٕ یہِ آسانی سان مکمل کرِتھ۔

## ضروریات

شروع کرنہٕ پؠٹھ تُہندٕ پاس یہِ چیزٕ ہونہٕ چھِ ضروری:

- Git انسٹال آسن (Git انسٹال کرنہٕ خٲطرٕ: https://git-scm.com/downloads)
- GitHub اکاؤنٹ

اَمہِ پتہٕ `github-cli` ٹول پننس سسٹم منٛز انسٹال کٔرِو۔ یِم سرکاری ہدایات دِیِتھ عمل کٔرِو:

https://github.com/cli/cli#installation

انسٹالیشن پتہٕ CLI منٛز لاگ اِن کرنہٕ خٲطرٕ یہِ کمانڈ چلٲو:

```bash
gh auth login
```

ہدایتَن پؠٹھ عمل کٔرِو تہٕ تُہۍ تیار چھِ!

# یہِ Repository فورک کٔرِو

صرف یہِ کمانڈ چلٲون:

```bash
gh repo fork firstcontributions/first-contributions
```

**اہم نوٹ:** اگر تُہۍ پُژھنہٕ آیہِ کہ Repository کلون کرُن چھا چاہان، تہٕ **"Yes"** منتخب کٔرِو۔

# پنُن Branch بنٲو

اَسہِ یہِ قدم Git استعمال کرِتھ پورا کران۔

مثال خٲطرٕ:

```bash
git switch -c add-john-doe
```

`john-doe` ہٕنٛد جاے پنُن ناو استعمال کٔرِو۔

# ضروری تبدیلیاں کٔرِو تہٕ Commit کٔرِو

اب `Contributors.md` فائل کانٛہہ تہِ Text Editor منٛز کٔھولِو تہٕ پنُن ناو تَمہِ منٛز شامل کٔرِو۔

پنُن ناو فائل ہنٛد شروع یا آخرس منٛز نہٕ بلکہ درمیان منٛز کَتھٕنہِ تہِ جگہِ پؠٹھ لیکھِو۔

فائل محفوظ (Save) کرنہٕ پتہٕ Project Directory منٛز یہِ کمانڈ چلٲو:

```bash
git status
```

یہِ تُہۍ تبدیلیاں دِکھاوِ۔

اب تبدیلیاں Stage کرنہٕ خٲطرٕ:

```bash
git add Contributors.md
```

اَمہِ پتہٕ تبدیلیاں Commit کٔرِو:

```bash
git commit -m "Add your-name to Contributors list"
```

`your-name` ہٕنٛد جاے پنُن ناو استعمال کٔرِو۔

# تبدیلیاں GitHub پؠٹھ Push کٔرِو

```bash
git push origin -u your-branch-name
```

`your-branch-name` ہٕنٛد جاے پننس Branch ہُند ناو لیکھِو۔

<details>
<summary><strong>اگر Push کران وِزِ غلطی آیہِ، تہٕ یہِ حصہٕ کٔھولِو:</strong></summary>

### Authentication Error

```text
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'
```

GitHub اکاؤنٹ سان SSH Key جوڑنہٕ خٲطرٕ یہِ گائیڈ وٕچھِو:

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

</details>

# پنُن Pull Request جمع کٔرِو

Repository Directory منٛز یہِ کمانڈ چلٲو:

```bash
gh pr create --repo firstcontributions/first-contributions
```

اَمہِ پتہٕ Pull Request جمع (Submit) کٔرِو۔

پنُن Pull Request ہنٛد حالت وٕچھنہٕ خٲطرٕ:

```bash
gh status
```

## اَمہِ پتہٕ کیاہ؟

مبارک ہو!

تُہۍ کامیابی سان اوپن سورس ہُند بنیادی Workflow مکمل کٔرِو:

**Fork → Clone → Edit → Pull Request**

یہِ عمل تقریباً ہر اوپن سورس پروجیکٹ منٛز استعمال گژھان۔

پنُن تعاون منانٕہ خٲطرٕ Web App استعمال کٔرِو تہٕ پننہِ دوستن سان شیئر کٔرِو۔

اگر تُہۍ مزید مشق کرُن چاہان، تہٕ **Code Contributions** وٕچھِو۔

اب تُہۍ آسانی سان باقی اوپن سورس پروجیکٹس منٛز تہِ تعاون شروع کرِتھ۔

### اضافی مواد

https://github.com/firstcontributions/first-contributions/blob/main/docs/additional-material/git_workflow_scenarios/additional-material.md

### مرکزی صفحہ پؠٹھ واپس گٔژھِو

https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools