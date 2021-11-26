[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# පළමු දායකත්වය

ආරම්භකයින් ඔවුන්ගේ පළමු දායකත්වය ලබා දෙන ආකාරය සරල කිරීම සහ මඟ පෙන්වීම මෙම ව්‍යාපෘතියේ අරමුණයි. ඔබ ඔබේ පළමු දායකත්වය ලබා දීමට බලාපොරොත්තු වන්නේ නම්, පහත පියවර අනුගමනය කරන්න.

ඔබට command line භාවිතය අපහසු වේ නම් , [GUI මෙවලම් භාවිතා කරන අකාරය පිලිබඳ නිබන්ධන මෙතනින් .](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### ඔබගේ පරිගණකයේ git නැත්නම්, [install කරන්න](https://help.github.com/articles/set-up-git/).

## මෙම රිපෝව ෆෝක් කරන්න

මෙම පිටුවේ ඉහලින් ඇති fork බොත්තම ක්ලික් කිරීමෙන් මෙම රිපොව ෆෝක් කරන්න.
මෙය ඔබගේ ගිණුමේ මෙම රිපෝවේ පිටපතක් සාදනු ඇත.

## රිපෝව ක්ලෝන් කරන්න

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

දැන් ඔබේ පරිගණකයට ෆෝක් කල රිපෝව ක්ලෝන කරන්න. ඔබගේ GitHub ගිණුමට ගොස්, ෆෝක් කල රිපෝව විවෘත කර, code බොත්තම මත ක්ලික් කර _copy to clipboard_ අයිකනය ක්ලික් කරන්න.

Terminal එකක් විවෘත කර පහත git විධානය ක්‍රියාත්මක කරන්න:

```
git clone "url you just copied"
```

මෙහි "url you just copied" (උද්ධෘත නොමැතිව) මෙම රිපෝවට url එක වේ. url එක ලබා ගැනීමට පෙර පියවර බලන්න.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

උදාහරණ වශයෙන්:

```
git clone https://github.com/this-is-you/first-contributions.git
```

මෙහි 'this-is-you' ඔබගේ GitHub username එක වේ. මෙතැනදී ඔබ GitHub හි first-contributions රිපෝවේ අන්තර්ගතය ඔබේ පරිගණකයට පිටපත් කරයි.

## ශාඛාවක් සාදන්න

ඔබේ පරිගණකයේ රිපෝව සහිත තැනට යන්න (ඔබ දැනටමත් එතැන නොව් නම්):

```
cd first-contributions
```

දැන් `git Checkout` විධානය භාවිතා කර ශාඛාවක් සාදන්න:

```
git checkout -b your-new-branch-name
```

උදාහරණ වශයෙන්:

```
git checkout -b add-alonzo-church
```

(ශාඛාවේ නමේ _add_ යන වචනය තිබීම අවශ්‍ය නොවේ, නමුත් මෙම ශාඛාවේ අරමුණ ඔබේ නම ලැයිස්තුවකට එකතු කිරීම නිසා එය ඇතුළත් කිරීම සුදුසු දෙයකි.)

## අවශ්‍ය වෙනස්කම් සිදු කර එම වෙනස්කම් කොමිට් කරන්න

දැන් text editor එකක් මගින්  `Contributors.md` ගොනුව විවෘත කරන්න, එයට ඔබේ නම එක් කරන්න. ගොනුවේ ආරම්භයේ හෝ අවසානයේ එය එකතු නොකරන්න. එය අතර ඕනෑම තැනකට එකතු කරන්න. දැන්, file එක save කරන්න.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ඔබ ව්‍යාපෘති නාමාවලිය වෙත ගොස් 'git status' විධානය ක්‍රියාත්මක කළහොත්, ඔබට කල වෙනස්කම් ඇති බව පෙනෙනු ඇත.

`git add` විධානය භාවිතයෙන් ඔබ දැන් නිර්මාණය කළ ශාඛාවට එම වෙනස්කම් එක් කරන්න:

```
git add Contributors.md
```

දැන් එම වෙනස්කම් `git commit` විධානය භාවිතයෙන් කොමිට් කරන්න:

```
git commit -m "Add <your-name> to Contributors list"
```

ඔබේ නම `<your-name>` වෙනුවට යොදන්න.

## GitHub වෙත වෙනස්කම් පුෂ් කරන්න

`git push` විධානය භාවිතයෙන් ඔබගේ වෙනස්කම් පුෂ් කරන්න:


```
git push origin <add-your-branch-name>
```

ඔබ කලින් නිර්මාණය කළ ශාඛාවේ නම, `<add-your-branch-name>` වෙනුවට යොදන්න.

## සමාලෝචනය සඳහා ඔබේ වෙනස්කම් ඉදිරිපත් කරන්න

ඔබ GitHub හි ඔබගේ රිපෝව ගියහොත්, ඔබට `Compare & pull request` බොත්තමක් පෙනෙනු ඇත. එම බොත්තම මත ක්ලික් කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

දැන් pull request එක ඉදිරිපත් කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

ඉක්මනින් මම ඔබේ සියලු වෙනස්කම් මෙම ව්‍යාපෘතියේ main branch එකට merge කරමි. වෙනස්කම් merge කළ පසු ඔබට දැනුම්දීමේ ඊමේල් පණිවුඩයක් ලැබෙනු ඇත.

## මෙතැන් සිට කොහේ යන්නද?

සුභ පැතුම්! ඔබ දායකයෙකු ලෙස නිතර හමුවන සම්මත _fork -> clone -> edit -> pull request_ කාර්යයන් සම්පුර්ණ කර ඇත!

[මෙය](https://firstcontributions.github.io/#social-share) වෙත යාමෙන් ඔබේ දායකත්වය සමරන්න සහ එය ඔබේ මිතුරන් සහ අනුගාමිකයින් සමඟ බෙදා ගන්න.

ඔබට කිසියම් උදව්වක් අවශ්‍ය නම් හෝ කිසියම් ප්‍රශ්නයක් ඇත්නම් ඔබට අපගේ slack team එකට සම්බන්ධ විය හැකිය.[slack team එකට සම්බන්ධවන්න](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

දැන් අපි ඔබව වෙනත් ව්‍යාපෘති සඳහා දායක කරවීමට ආරම්භ කරමු. ඔබට ආරම්භ කළ හැකි පහසු ගැටළු සහිත ව්‍යාපෘති ලැයිස්තුවක් අපි සම්පාදනය කර ඇත්තෙමු. පරීක්ෂාකාරී වන්න[ව්‍යාපෘති ලැයිස්තුව](https://firstcontributions.github.io/#project-list).

### [අතිරේක දේවල්](additional-material/git_workflow_scenarios/additional-material.md)

## වෙනත් tool භාවිතය පිලිබඳ නිබන්ධන

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
添加内容
