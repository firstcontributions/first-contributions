[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# 

# පළමු දායකත්වය

ආරම්භකයින් ඔවුන්ගේ පළමු දායකත්වය ලබා දෙන ආකාරය සරල කිරීම සහ මඟ පෙන්වීම මෙම ව්‍යාපෘතියේ අරමුණයි. ඔබ ඔබේ පළමු දායකත්වය ලබා දීමට බලාපොරොත්තු වන්නේ නම්, පහත පියවර අනුගමනය කරන්න.

_ඔබ විධාන රේඛාව (command line) සමඟ නුහුරු නම්, [මෙන්න GUI මෙවලම් භාවිතා කරන නිබන්ධන.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### ඔයාගේ මැෂින් එකේ git නැත්නම්, [එය ස්ථාපනය කරන්න](https://help.github.com/articles/set-up-git/).

## මෙම repository එක fork කරගන්න

මෙම පිටුවේ ඉහලින් ඇති fork බොත්තම ක්ලික් කිරීමෙන් මෙම repository එක fork කරගන්න.
මෙය ඔබගේ ගිණුමේ මෙම repository එකේ පිටපතක් සාදනු ඇත.

## මෙම repository එක clone කරගන්න

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

දැන් ඔබේ යන්ත්‍රයට repository එක clone කරගන්න. දැන් ඔබගේ GitHub ගිණුම වෙත ගොස්, fork කරගත් repository එක විවෘත කර, කේත (code) බොත්තම මත ක්ලික් කර පසුව _copy to clipboard_ අයිකනය ක්ලික් කරන්න.

Terminal එකක් විවෘත කර පහත git විධානය ක්‍රියාත්මක කරන්න:

```
git clone "ඔබ දැන් පිටපත් කරගත් url එක"
```

එහිදී "ඔබ දැන් පිටපත් කරගත් url එක" (උපුටා දැක්වීම් ලකුණු නොමැතිව) මෙම repository url එක වේ (මෙම ව්‍යාපෘතියේ ඔබේ fork එක).url ලබා ගන්නා ආකාරය සදහා  පෙර පියවර බලන්න.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

උදාහරණයක් ලෙස:

```
git clone https://github.com/this-is-you/first-contributions.git
```

මෙහි 'this-is-you' ඔබගේ GitHub පරිශීලක නාමය වේ.මෙහිදී ඔබ GitHub හි පළමු-දායකත්ව repository එකෙහි  අන්තර්ගතය ඔබේ පරිගණකයට පිටපත් කරයි.

## ශාඛාවක් (brnach) සාදන්න

ඔබේ පරිගණකයේ repository directory එක වෙනස් කරන්න (ඔබ දැනටමත් එහි නොමැති නම්):

```
cd first-contributions
```
දැන් 'git Checkout' විධානය භාවිතා කර ශාඛාවක් සාදන්න:

```
git checkout -b your-new-branch-name
```

උදාහරණයක් ලෙස:

```
git checkout -b add-alonzo-church
```

(ශාඛාවේ නමේ _add_ යන වචනය තිබීම අවශ්‍ය නොවේ, නමුත් මෙම ශාඛාවේ අරමුණ ඔබේ නම ලැයිස්තුවකට එකතු කිරීම නිසා එය ඇතුළත් කිරීම සාධාරණ දෙයකි.)

## අවශ්‍ය වෙනස්කම් සිදු කර එම වෙනස්කම් commit කරන්න

දැන් `Contributors.md` ගොනුව text editor එකේ විවෘත කරන්න, එයට ඔබේ නම එක් කරන්න. ගොනුවේ ආරම්භයේ හෝ අවසානයේ එය එකතු නොකරන්න. එය අතර ඕනෑම තැනක තබන්න. දැන්, ගොනුව save කරන්න.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ඔබ ව්‍යාපෘති directory ය වෙත ගොස් `git status` විධානය ක්‍රියාත්මක කළහොත්, වෙනස්කම් ඇති බව ඔබට පෙනෙනු ඇත.

'git add' විධානය භාවිතයෙන් ඔබ දැන් නිර්මාණය කළ ශාඛාවට එම වෙනස්කම් එක් කරන්න:

```
git add Contributors.md
```

දැන් එම වෙනස්කම් commit කිරීමට 'git commit' විධානය භාවිතා කරන්න:

```
git commit -m "Add <your-name> to Contributors list"
```

ඔබේ නම `<your-name>` වෙනුවට ආදේශ කරන්න.

## වෙනස්කම් GitHub එකට push කරන්න

`git push` විධානය භාවිතයෙන් ඔබගේ වෙනස්කම් push කරන්න:

```
git push origin <your-new-branch-name>
```

ඔබ කලින් නිර්මාණය කළ ශාඛාවේ නම `<your-new-branch-name>` වෙනුවට ආදේශ කරන්න.

## සමාලෝචනය සඳහා ඔබේ වෙනස්කම් ඉදිරිපත් කරන්න

ඔබ GitHub හි ඔබේ ගබඩාවට ගියහොත්, ඔබට `Compare & pull request` බොත්තමක් පෙනෙනු ඇත. එම බොත්තම මත ක්ලික් කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

දැන් pull request එක ඉදිරිපත් කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

ළඟදීම මම ඔබේ සියලු වෙනස්කම් මෙම ව්‍යාපෘතියේ ප්‍රධාන ශාඛාවට ඒකාබද්ධ කරමි. වෙනස්කම් ඒකාබද්ධ කළ පසු ඔබට දැනුම්දීමේ විද්‍යුත් තැපෑලක් ලැබෙනු ඇත.

## මෙතනින් කොහෙ යන්නද?

සුභ පැතුම්! ඔබ දායකයෙකු ලෙස නිතර හමුවන සම්මත _fork -> clone -> edit -> pull request_ කාර්ය ප්‍රවාහය ඔබ සම්පූර්ණ කර ඇත!

[web app](https://firstcontributions.github.io/#social-share) වෙත යාමෙන් ඔබේ දායකත්වය සමරන්න සහ එය ඔබේ මිතුරන් සහ අනුගාමිකයින් සමඟ බෙදා ගන්න.

ඔබට කිසියම් උදව්වක් අවශ්‍ය නම් හෝ කිසියම් ප්‍රශ්නයක් ඇත්නම් ඔබට අපගේ slack කණ්ඩායමට සම්බන්ධ විය හැකිය. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

දැන් අපි ඔබට වෙනත් ව්‍යාපෘති සඳහා දායක වීම ආරම්භ කරමු. ඔබට ආරම්භ කළ හැකි පහසු ගැටළු සහිත ව්‍යාපෘති ලැයිස්තුවක් අපි සම්පාදනය කර ඇත්තෙමු. පරීක්ෂා කරන්න [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)

## වෙනත් මෙවලම් භාවිතා කරන නිබන්ධන

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
