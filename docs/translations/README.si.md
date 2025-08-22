[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# පළමු දායකත්වය

ආරම්භකයින්ගේ පළමු දායකත්වය ලබා දෙන ආකාරය සරල කිරීම සහ මඟ පෙන්වීම මෙම ව්‍යාපෘතියේ අරමුණයි. ඔබ ඔබේ පළමු දායකත්වය ලබා දීමට බලාපොරොත්තු වන්නේ නම්, පහත පියවර අනුගමනය කරන්න.

#### *ඔබ විධාන රේඛාව (command line) සමඟ අපහසු නම්, [GUI මෙවලම් භාවිතා කරන නිබන්ධන මෙන්න.](#tutorials-using-other-tools)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="මෙම ගබඩාව fork කරන්න" />

ඔබේ පරිගණකයේ git නොමැති නම්, [ස්ථාපනය කරන්න](https://help.github.com/articles/set-up-git/).

## මෙම ගබඩාව fork කිරීම

පිටුවේ ඉහළින් ඇති fork බොත්තම ක්ලික් කිරීමෙන් මෙය කළ හැකිය. මෙය ඔබගේ ගිණුමේ
පිටපතක් සාදනු ඇත.

## මෙම ගබඩාව clone කරන්න

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="මෙම ගබඩාව clone කරන්න" />

දැන් ඔබේ පරිගණකට fork කරපු repository ය ක්ලෝන කරන්න. ඔබට ඔබගේ GitHub ගිණුමට ගොස් fork කරපු repository විවෘත කර clone බොත්තම ක්ලික් කර එය පසුරු පුවරුවට (clipboard) පිටපත් කිරීමෙන් මෙය කළ හැක.

*terminal* හෝ *command prompt* විවෘත කර පහත git විධානය ක්‍රියාත්මක කරන්න:

```
git clone "ඔබ පිටපත් කළ url එක"
```

මෙහි "ඔබ පිටපත් කළ url එක" (උපුටා දැක්වීම් ලකුණු නොමැතිව) මෙම ගබඩාවේ url එක වේ (මෙම ව්යාපෘතියේ ඔබේ දෙබල (fork) ). url එක ලබා ගැනීමට පෙර පියවර බලන්න.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />


උදාහරණ වශයෙන්:

```
git clone https://github.com/මෙය-ඔබයි/first-contributions.git
```

මෙහි `මෙය ඔබයි` යනු GitHub පරිශීලක නාමයයි. මෙය ඔබගේ GitHub ගිණුමේ first-contributions repository පිටපතක් සෑදීමට ඔබට ඉඩ සලසයි.

## ශාඛාවක් නිර්මාණය කිරීම

ඔබේ පරිගණකයේ ගබඩා නාමාවලියට වෙනස් කරන්න (ඔබ දැනටමත් එහි නොමැති නම්):

```
cd first-contributions
```


දැන් `git checkout` විධානය භාවිතා කරමින් ශාඛාවක් සාදන්න:

```
git checkout -b <ඔබගේ-නව-ශාඛාවේ-නම>
```

උදාහරණ වශයෙන්:

```
git checkout -b add-luke-oliff
```

(ශාඛාවේ නමට *add* එකතු කිරීම අවශ්‍ය නොවේ, නමුත් එය සාධාරණ දෙයකි, මන්ද මෙම ශාඛාවේ අරමුණ ඔබේ නම ලැයිස්තුවකට එකතු කිරීමයි.)

## අවශ්‍ය වෙනස්කම් සිදු කර commit කරන්න

දැන් Contributors.md ගොනුව පෙළ සංස්කාරකයක විවෘත කරන්න, එයට ඔබේ නම එක් කරන්න. ගොනුවේ ආරම්භයේ හෝ අවසානයේ එය එකතු නොකරන්න. එය අතර මැද ඕනෑම තැනකට එකතු කරන්න. දැන්, ගොනුව save කරන්න.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ඔබ ව්‍යාපෘති නාමාවලිය වෙත ගොස් git status විධානය ක්‍රියාත්මක කළහොත්, වෙනස්කම් ඇති බව ඔබට පෙනෙනු ඇත.

`git add` විධානය භාවිතයෙන් ඔබ දැන් නිර්මාණය කළ ශාඛාවට එම වෙනස්කම් එක් කරන්න:

```
git add Contributors.md
```

දැන් `git commit` විධානය භාවිතා කර එම වෙනස්කම් සිදු කරන්න:

```
git commit -m "Add <ඔයාගේ_නම> to Contributors list"
```

`<ඔබේ_නම>` වෙනුවට ඔබේ නම ඇතුල් කරන්න.

## GitHub වෙත වෙනස්කම් තල්ලු කරන්න

`git push` විධානය භාවිතයෙන් ඔබගේ වෙනස්කම් තල්ලු කරන්න:
```
git push origin -u <ඔබගේ-නව-ශාඛාවේ-නම>
```

`<ඔබගේ-නව-ශාඛාවේ-නම>` ඔබ කලින් නිර්මාණය කළ නම සමඟ ශාඛාව ප්රතිස්ථාපනය කරන්න.

## සමාලෝචනය සඳහා ඔබේ වෙනස්කම් ඉදිරිපත් කරන්න


ඔබ GitHub හි ඔබගේ ගබඩාවට ගියහොත්, ඔබට `Compare & pull request` බොත්තමක් පෙනෙනු ඇත. එම බොත්තම මත ක්ලික් කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

දැන් pull request ඉදිරිපත් කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

මම ළඟදීම ඔබේ සියලු වෙනස්කම් මෙම ව්‍යාපෘතියේ ප්‍රධාන ශාඛාවට ඒකාබද්ධ කරමි. වෙනස්කම් ඒකාබද්ධ කළ පසු ඔබට දැනුම්දීමේ Email පණිවිඩයක් ලැබෙනු ඇත.

## මෙතැන් සිට කොහේ යන්නද?

සුභ පැතුම්! ඔබ දායකයෙකු ලෙස සම්මත 'fork -> clone -> edit -> pull request' කාර්ය ප්‍රවාහය ඔබ සම්පුර්ණ කර ඇත!

ඔබේ දායකත්වය සහ ඔබේ මිතුරන් සහ අනුගාමිකයින් සමඟ සමරන්න [web app](https://firstcontributions.github.io/#social-share) ගිහින් share කරන්න.

ඔබට කිසියම් උදව්වක් අවශ්‍ය නම් හෝ කිසියම් ප්‍රශ්නයක් ඇත්නම් ඔබට අපගේ slack කණ්ඩායමට සම්බන්ධ විය හැකිය. [අපගේ slack කණ්ඩායමට එක්වන්න](https://join.slack.com/t/firstcontributors/shared_invite/zt-kpbyrmkk-JDkRtchcvRvQ0qK4iPmyvA)..

දැන් අපි ඔබට වෙනත් ව්‍යාපෘති සඳහා දායක වීම ආරම්භ කරමු. ඔබට ආරම්භ කළ හැකි පහසු ගැටළු සහිත ව්‍යාපෘති ලැයිස්තුවක් අපි සම්පාදනය කර ඇත්තෙමු. පරීක්ෂා කරන්න [web app ව්‍යාපෘති ලැයිස්තුව](https://firstcontributions.github.io/#project-list).

### [අතිරේක සම්පත්](../additional-material/git_workflow_scenarios/additional-material.md)

## වෙනත් මෙවලම් භාවිතා කරන නිබන්ධන

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
