[![KAY3BEK T3AWN OPEN SOURCE](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# أول مساهمة

ملي كتكون باغي تبدا شي حاجة جديدة، مرات كيبان كلشي معقد فالأول. داك الخوف ديال لا تغلط كيقدر يضغط عليك، خصوصاً إلا كنتي خدام مع ناس آخرين. ولكن الفكرة ديال الأوبن سورس هي أنك كتخدم مع الناس فواحد الفريق. وحنا بغينا نسهلوها عليكم باش تتعلمو كيفاش تساهمو فشي مشروع ديال الأوبن سورس بحال هادا لأول مرة.

راه بطبيعة الحال تقدر تبقى تقرا كيفاش تدير ولا تشوف طوطوريالات، ولكن واش ماشي حسن نوريك كيفاش تدير بلا ما تغلط؟ هاد البروجي الهدف ديالو هو يعطيك نصائح ويخليك عاقل: كلما كنت مهدّن، غتتعلم حسن. إلا كنتي عوال تدير أول مساهمة، تبع هاد الخطوات وراه غاتصدق لك. كنواعدك، غايعجبك الحال.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="اربط هاد الريپو" />

إلا ماكانش عندك **Git** فالحاسوب ديالك، [حمّلو](https://help.github.com/articles/set-up-git/) من هاد الموقع.

## جبّد هاد الريپو لعندك (كتسمّيوها هنا Fork)

برّك على داك الزر ديال **FORK** كيفما كيبان ليك فالصّورة باش تولّي عندك واحد النسخة بحال ديال الريپو فالكومب ديالك.

## تيليشارجي الريپو عندك (كيسمّيوها clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="كلون ديال الريپو" />

دابا، دير كلون للريپو ديالك فالحاسوب ديالك. برّك على زر Clone و نسخ داك اللينك (HTTPS هو الساهل). راه كاين حتى زر حدّا اللينك كينسخو ليك مباشرة.

حل دابا الـcmd إلا كنت فـWindows، ولا الـterminal إلا كنت فـMac ولا خدام بـLinux، ونسخ هاد الأوامر اللي غنوريك:

```bash
git clone "dik lien li 3ad copieti"
```
خاصك تخليها هكاك ههه داك اللينك اللي عاد كوپيتي بلا دوك علامات الاقتباس، كتب تماك داك اللينك اللي كوپيتي، فهمتيني؟

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="نسخ الـيو آر إل فالكليپبورْد" />

غتكون بحال هاد الشكل:
```bash
git clone https://github.com/smytk_dyal_github/first-contributions.git
```
راه `smytk_dyal_github` هي السمية اللي نتا داير فـGitHub.
دابا نتا فهاد الخطوة غاتTélécharger كامل هاد الريپو عندك فالحاسوب باش تبدا تبدّل فيها.

## صوّب البرانش الجديدة ديالك

دابا فـ cmd ولا فالترمينال، دخل لداك الملف اللي عاد تيليشارجيتي (كتب هاد الأمر إلا ماعرفتيش تدخل ليه يدويًا):

## صوّب البرانش الجديدة ديالك

```bash
cd first-contributions
```
دابا هاه كيفاش غاتصوّب البرانش ديالك باستعمال `git checkout`:
```bash
git checkout -b "smya_dlbranch"
```

مثلاً:
```bash
git checkout -b add-brahim
```
ماشي ضروري تدير فالسميّة *add*، غير باش نفهمو علاش زدّيتيها.

## بدّل فالملف ديال Contributors

دابا دخل لملف `Contributors.md` بشي إيديتور، وزيد السمية ديالك وشي لينك إلا بغيتي (راك تقدر تدير أي حاجة بلاش تخاف).
إلا كتبتي دابا فداك الـ cmd/terminal هادشي: `git status` غايبانولك الحوايج اللي بدّلتي.
دابا زيدهم فالـبرانش ديالك **add-brahim** بهاد الأمر ديال `git add`:
```bash
git add Contributors.md
```

وسايفطه بالتسجيل باستعمال `git commit`:
```bash
git commit -m "Add <smytk> to Contributors list"
```

ودر فبلاصة `<smytk>` السمية ديالك بصح (مثلاً: brahim).

## بوشي

دابا غاتبوشي هاد التعديلات اللي درتي لْگيتهاب بـ `git push`:
```bash
git push origin <smya_dlbranch>
```

أنا كنت مسمّيها add-brahim، نتا بدّلها حسب السمية اللي داير.

## حطّ التعديلات باش يتشافو

إلا رجعتي لْگيتهاب غاتلقى داك الزر ديال `Compare & pull request`، برّك عليه أخاي.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="دير بول ريكويست" />

غير برّك عليها باش توصل للناس المسؤولين على هاد الشي.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="قدّم بول ريكويست" />

شوية من بعد ما يتجمعو داك التعديلات اللي درتي، غايصلك إيميل كيقولك باللي راه كلشي ديالك ناضي.

البرانش ديال main عندك ما غايتبدّل فيها والو دابا. إلا بغيتي حتى الـmain ديالك يكون متزامن، تبع هاد الخطوات.

## خَلّي الـmain ديالك متزامن مع contributors

أول حاجة رجع لِـmain وما تبقاش فـ add-brahim:

```bash
git checkout main
```

زيد لينك ديال الريپو كـ `upstream remote url`:
```bash
git remote add upstream https://github.com/smytk_d_github/first-contributions
```

باش يْدارو غير داك التغييرات، خاصك من بعد تجبد آخر نسخة من الريپو:
```bash
git fetch upstream
```

هنا كنقلّبو على جميع التغييرات اللي كاينين فالفورك ديالهم (upstream).
دابا خاصك تجمع هاد التغييرات الجداد مع الريپو ديالك (main):
```bash
git rebase upstream/main
```

ودابا راه جميع التغييرات ولاو فـmain ديالك. إلا بوشيتيهم غايدخلو حتى فالفورك ديالك:
```bash
git push origin main
```

ودابا راه جمعنا البرانش ديال `<add-brahim>` مع الـmain ديالنا، وجمعنا حتى الـmain ديالنا مع الـmain ديالهم (ياربي تكون فهمتيني ههه).
ودابا داك الشي اللي درتي فالأول فـ `<add-votre-nom>` مبقاتش عندها الفايدة. إلا بغيتي تحيدها:
```bash
git branch -d <add-brahim>
```

وحتى من الفورك اللي فالگيتهاب تقدر تحيدها:
```bash
git push origin --delete <add-votre-nom>
```

ماشي ضروري تحيد البرانش، ولكن راه سالات الخدمة ديالها وما بقاتش محتاجة تبقى تما.

## طوطوريالات مع شوية نصائح خرين


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="گيتهاب ديسكتوب" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="فيجوال ستوديو 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="گيت كراكن" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="في إس كود" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="تطبيق سورس تري" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="إنتيليجاي آيديا" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

## فين نمشي دابا؟

يمكن ليكم تجيو لـSlack فين كاينة الفرقة ديال هاد الشي كامل، ونقدرو نعاونكم ونجاوبو على أي أسئلة.
[Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

