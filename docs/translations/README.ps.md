<div dir="rtl" lang="ps">

<a href="https://github.com/ellerbrock/open-source-badges/">
  <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" alt="Open Source Love" />
</a>
<a href="https://opensource.org/licenses/MIT">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License" />
</a>
<a href="https://www.codetriage.com/roshanjossey/first-contributions">
  <img src="https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg" alt="Open Source Helpers" />
</a>

---

## لومړی ګډون

**د دې پروژې هدف دا دی چې نویو ګډونوالو ته په خلاصو سرچینو پروژو (Open Source Projects) کې د ګډون اسانه طریقه وښيي.**  
که غواړئ خپله لومړنۍ مرسته وکړئ، لاندې ګامونه تعقیب کړئ.

**که د کمانډ لاین (CLI) سره راحت نه یاست،**  
[کولی شئ تصویري لارښود دلته وګورئ](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)

**که مو Git انسټال نه وي،**  
[له دې ځایه یې ښکته او نصب کړئ](https://help.github.com/articles/set-up-git/).

## دا ذخیره (repository) فورک کړئ

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

- د دې پاڼې په سر کې د Fork تڼۍ کلیک کړئ.
- فورک کول به د دې ذخیرې یوه کاپي ستاسو د GitHub اکاونټ ته انتقال کړي.

<br clear="all"/>

## دا ذخیره (repository) کلون کړئ

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

- خپل اکاونټ ته لاړ شئ او د فورک شوې ذخیرې لینک د **Code** تڼۍ څخه کاپي کړئ.

<br clear="all"/>

- ترمینل یا CMD خلاص کړئ او دا کمانډ اجرا کړئ:

```bash
git clone https://github.com/YourUsername/first-contributions.git
```

**یادونه:** دلته `YourUsername` باید ستاسو د GitHub اکاونټ نوم وي.

## نوې څانګه (branch) جوړ کړئ

- د first-contribution پروژه په خپل کوډ ایډیټر کې خلاصه کړئ.
- ترمینل کې دا کمانډ اجرا کړئ ترڅو نوې څانګه جوړه کړئ. ددې لپاره چې زمونږ د بدلونونو لپاره خپله څانګه وي او له نورو سره شریکه نشي. دې څانګې کې به مونږ ایډیټ کوو او بیا به یې له عمومي څانګې سره یوځای کوو.

```bash
git switch -c your-branch-name
```

your-branch-name ستاسو د څانګې نوم دی. کولای شئ چې هر نوم تاسې ټاکلی شئ.

## اړین بدلونونه راوړئ او commit کړئ

- د `Contributors.md` فایل خلاص کړئ او خپل نوم پکې اضافه کړئ کې).
- فایل ذخیره کړئ.

<img align="left" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

- ترمینل ته لاړ شئ او دا کمانډ اجرا کړئ ترڅو وګورئ کوم فایلونه مو بدل کړي دي:

```bash
git status
```

- بدلونونه ذخیره کړئ:

```bash
git add Contributors.md
```

- اوس مو بدلونونه کمټ Commit کړئ:

```bash
git commit -m "message"
```

د مسیج پر ځای تاسې هر څه لیکلی شئ. بهتره دا ده چې تاسې په دې ځای کې ولیکئ چې کوم بدلونونه مو پروژې کې راوستل.

## بدلونونه GitHub ته push کړئ

- خپل بدلونونه کیټ هب ته پورته کړئ:

```bash
git push origin -u your-branch-name
```

د your-branch-name پر ځای باید تاسې په دقیق ډول سره د خپلې څانګې نوم ورکړئ. هغه نوم چې لږ مخکې مو انتخاب کړی وه.

<details align="right" dir="rtl">
<summary><strong>که چېرې په دې لړ کې د کومې ستونزې سره مخ شوئ دا ځای کېکاږئ</strong></summary>

که چېرته ستاسې ستونزه داسي وي.

<div dir="ltr">
<pre>
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/
</pre>
<div>

[نو بیا دلته زده کړئ چې دا ستونزه څنګه حل کړئ](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

</details>

## خپل بدلونونه د بیاکتنې لپاره وسپارئ

- خپل GitHub اکاونټ کې دې ریپوزیټوري ته لاړ شئ.
- د **Compare & pull request** تڼۍ به ووینئ. پر هغې کلیک وکړئ.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

- اوس د pull request غوښتنه وسپارئ.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

- له دې وروسته به ستاسو بدلونه د اصلي یا main څانګې سره یوځای شي او ستاسو نوم به د ګډون کوونکو لیست ته اضافه کړل شي.

## له دې وروسته څه وکړئ؟

تاسو په بریالیتوب سره د فورک، کلون، ایډیټ، او pull request مرحلې بشپړې کړې. تاسې له دې نه وروسته کولی شئ چې په خلاص-سرچېنه پروژو کې په همدې طریقه برخه واخلئ.

- خپل لومړئ ګډون ولمانځئ او له خپلو ملګرو سره یې [شریک کړئ](https://firstcontributions.github.io/#social-share).
- که کومه ستونزه یا پوښتنه لرئ، کولای شئ زموږ د Slack ټیم سره یوځای شئ.
- اوس کولای شئ په نورو پروژو کې هم ګډون وکړئ. [دلته د پروژو لیست وګورئ](https://firstcontributions.github.io/#project-list).

## <a href="additional-material/git_workflow_scenarios/additional-material.md">اضافي مواد</a>

## د نورو وسیلو په کارولو سره درسونه

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

</div>