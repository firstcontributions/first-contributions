[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

<p align="right">

# لومړنۍ مرستې
د دې پروژې موخه دا ده چې د پیل کونکو لپاره د دوی لومړنۍ مرسته کولو لاره ساده او لارښود کړي. که تاسو د خپلې لومړۍ مرستې په لټه کې یاست، لاندې مرحلې تعقیب کړئ.

_که تاسو د کمانډ لاین (CLI) سره راحته نه یاست ، [دا لارښوونې وکاروئ ترڅو پوه شئ چې د GUI وسیلو کارولو څرنګوالی](#د-نورو-وسیلو-کارولو-لارښوونې)._

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### که تاسو git نصب نلرئ [له دې ځایه نصب کړئ](https://help.github.com/articles/set-up-git/).

## د دې ریپوزیتوری فورک کړئ
د دې پاڼې په سر کې د Fork تڼۍ په کلیک کولو سره دا ذخیره فورک کړئ.
دا به ستاسو په حساب کې د دې ذخیره کاپي رامینځته کړي.

## فورک شوی ریپازیتوری کلون Clone کړئ

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

اوس خپل ماشین ته د فورک شوي ذخیره کلون کړئ. خپل GitHub حساب ته لاړ شئ، د فورک شوي ریپازیتوری خلاص کړئ، د Code تڼۍ باندې کلیک وکړئ او بیا د کلپ بورډ ته د Copy To Clipboard باندې کلیک وکړئ.

بیا یو ټرمینل خلاص کړئ او لاندې کمانډ چل کړئ:
```
git clone "url you just copied"
```
چیرته چې "url you just copied" (پرته د نرخ نښه) د دې ریپازیتوری url دی (ستاسو د دې پروژې فورک). د url ترلاسه کولو لپاره مخکیني ګامونه وګورئ.

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

د مثال په توګه:
```
git clone https://github.com/this-is-you/first-contributions.git
```
چیرته چې 'this-is-you' ستاسو د GitHub کاربری نوم دی. دلته تاسو خپل کمپیوټر ته په GitHub کې د لومړۍ مرستې ذخیره مینځپانګې کاپي کوئ.

### یوه څانګه جوړه کړئ
په خپل کمپیوټر کې د ریپوزیتوری لارښود ته بدل کړئ (که تاسو دمخه نه لرئ):
```
cd first-contributions
```
اوس د `git switch` کمانډ په کارولو سره څانګه جوړه کړئ:
```
git checkout -b your-new-branch-name
```
د مثال په توګه:
```
git checkout -b add-alonzo-church
```

### اړین بدلونونه وکړئ او دا بدلونونه Commit کړئ
اوس د `Contributors.md` فایل په متن ایډیټر کې خلاص کړئ، خپل نوم پکې اضافه کړئ. دا د فایل په پیل یا پای کې مه اضافه کړئ. په منځ کې هر ځای کېږدئ. اوس، فایل ذخیره کړئ.

<img align="left" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

که تاسو د پروژې موقعیت ته لاړ شئ او د `git status` کمانډ اجرا کړئ ، نو تاسو به وګورئ چې بدلونونه شتون لري.

د `git add` کمانډ په کارولو سره دا بدلونونه په هغه څانګه کې اضافه کړئ چې تاسو یې رامینځته کړی:
```
git add Contributors.md
```

اوس دا بدلونونه د `git commit` کمانډ په کارولو سره ترسره کړئ:
```
git commit -m "Add <your-name> to Contributors list"
```
<your-name> د خپل نوم سره بدل کړئ.

## GitHub ته بدلونونه فشار (Push) وکړئ
د 'git push' کمانډ په کارولو سره خپل بدلونونه فشار (Push) وکړئ:
```
git push origin <add-your-branch-name>
```
د `your-branch-name` بدلول د هغه څانګې نوم سره چې تاسو مخکې جوړ کړی:

## خپل بدلونونه د بیاکتنې لپاره وسپارئ
که تاسو په GitHub کې خپل ریپازیتوری ته لاړ شئ، نو تاسو به د `Compare & pull request` تڼۍ وګورئ. په هغه تڼۍ کلیک وکړئ.

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

اوس د پلولو غوښتنه (Pull Request) وسپارئ.

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

ډیر ژر به زه ستاسو ټول بدلونونه د دې پروژې په اصلي څانګه کې یوځای کړم. تاسو به د خبرتیا بریښنالیک ترلاسه کړئ کله چې بدلونونه یوځای شي.

## راتلونکی څه شی دی
مبارک شه! تاسو یوازې د معیاري فورک(Fork)، کلون(Clone)، ایډیټ(Edit)، او پلولو غوښتنې (Pull Request) کاري فلو بشپړ کړی چې تاسو به ډیری وختونه د مرسته کونکي په توګه ورسره مخ شئ!

خپله ونډه ولمانځئ او له خپلو ملګرو او پیروانو سره یې شریک کړئ [دلته](https://firstcontributions.github.io/#social-share) لاړ شئ.

همدارنګه، تاسو کولی شئ زموږ د Slack ټیم سره یوځای شئ که تاسو کومې مرستې ته اړتیا لرئ یا کومه پوښتنه لرئ. [دلته کلیک وکړی](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)

اوس راځئ چې تاسو په نورو پروژو کې د مرستې سره پیل وکړو. موږ د اسانه مسلو سره د پروژو لیست ترتیب کړی چې تاسو یې پیل کولی شئ. [بشپړ ی وګوره](https://firstcontributions.github.io/#project-list)

### [نور معلومات](additional-material/git_workflow_scenarios/additional-material.md)

## د-نورو-وسیلو-کارولو-لارښوونې
| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
|                                                                                                                                                             |                                                                                                                                                                                                     |                                                                                                                                                                                              |                                                                                                                                                                                              |                                                                                                                                                                                                              |                                                                                                                                                                                                                                  |
</p>
