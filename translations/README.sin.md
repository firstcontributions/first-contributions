[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-mog68oas-dFnCPhZzJMd9A9dboJhi2g)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# පළමු දායකත්වය

ආරම්භකයින්ට ඔවුන්ගේ පළමු දායකත්වය ලබා දෙන ආකාරය සරල කිරීම සහ මඟ පෙන්වීම මෙම ව්‍යාපෘතියේ අරමුණයි. ඔබ ඔබේ පළමු දායකත්වය ලබා දීමට බලාපොරොත්තු වන්නේ නම්, පහත පියවර අනුගමනය කරන්න.


ඔබට විධාන රේඛාව (command line) සමඟ පහසු නොවේ නම්,[මෙන්න GUI මෙවලම් භාවිතා කරන නිබන්ධන.](#tutorials-using-other-tools)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="මෙම reposotory එක fork කරගන්න" />

#### ඔබගේ මැෂින් එකේ git නැත්නම් [බාගත කරගන්න](https://help.github.com/articles/set-up-git/).


### මෙම reposotory එක fork කරගන්න

මෙම පිටුවේ ඉහලින් ඇති fork බොත්තම ක්ලික් කිරීමෙන් මෙම reposotory එක fork කරගන්න.
මෙය ඔබගේ ගිණුමේ මෙම reposotory එකේ පිටපතක් සාදනු ඇත.

## මෙම reposotory එක clone කරගන්න

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="මෙම reposotory එක clone කරගන්න" />

දැන් ඔබේ යන්ත්‍රයට reposotory එක clone කරගන්න. ඔබගේ GitHub account එක වෙත ගොස්, reposotory එක විවෘත කර, කේත බොත්තම මත ක්ලික් කර _copy to clipboard_ අයිකනය ක්ලික් කරගන්න.

terminal එක විවෘත කර පහත git විධානය ක්‍රියාත්මක කරගන්න:


```
git clone "ඉහත copy කරගත් url එක"
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL එක clipboard එකට copy කරගන්න" />


උදාහරණයක් ලෙස:

```
git clone https://github.com/මෙය-ඔබගේ/පළමු-දායකත්වයයි.git
```

මෙහි `මෙය-ඔබ-ඔබ` ඔබගේ GitHub පරිශීලක නාමය වේ. මෙන්න ඔබ GitHub හි පළමු-දායකත්ව ගබඩාවේ අන්තර්ගතය ඔබේ පරිගණකයට පිටපත් කරයි.

## ශාඛාවක් සාදන්න

ඔබේ පරිගණකයේ ගබඩා නාමාවලියට වෙනස් කරන්න (ඔබ දැනටමත් එහි නොමැති නම්):

```
cd first-contributions
```


දැන් `git checkout` විධානය භාවිතයෙන් ශාඛාවක් සාදන්න:

```
git checkout -b <add-your-new-branch-name>
```

උදාහරණයක් ලෙස:

```
git checkout -b add-දනිරු-ආයුක
```

(ශාඛාවේ නමේ _add_ යන වචනය තිබීම අවශ්‍ය නොවේ, නමුත් මෙම ශාඛාවේ අරමුණ ඔබේ නම ලැයිස්තුවකට එකතු කිරීම නිසා එය ඇතුළත් කිරීම සාධාරණ දෙයකි.)

## අවශ්‍ය වෙනස්කම් සිදු කර එම commit එක සිදු කරන්න

දැන් පාඨ සංස්කාරකයක `Contributors.md` ගොනුව විවෘත කරන්න, එයට ඔබේ නම එක් කරන්න. ගොනුවේ ආරම්භයේ හෝ අවසානයේ එය එකතු නොකරන්න. එය අතර ඕනෑම තැනක තබන්න. දැන්, ගොනුව සුරකින්න.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ඔබ ව්‍යාපෘති නාමාවලිය වෙත ගොස් `git status` විධානය ක්‍රියාත්මක කළහොත්, වෙනස්කම් ඇති බව ඔබට පෙනෙනු ඇත.


`git add` විධානය භාවිතයෙන් ඔබ දැන් නිර්මාණය කළ ශාඛාවට එම වෙනස්කම් එක් කරන්න:

```
git add Contributors.md
```

දැන් එම වෙනස්කම් `git commit` විධානය භාවිතයෙන් සිදු කරන්න:


```
git commit -m "Add <ඔබගේ-නාමය> to Contributors list"
```

මෙහි `<ඔබගේ-නාමය>` ඔබේ නමය සමග වෙනස් කරන්න

## වෙනස්කම් Github එකට push කරන්න

`git push` විධානය භාවිතයෙන් ඔබගේ වෙනස්කම් තල්ලු කරන්න:

```
git push origin <add-your-branch-name>
```

ඔබ කලින් නිර්මාණය කළ ශාඛාවේ නම සමඟ `<add-your-branch-name>` වෙනුවට.

## සමාලෝචනය සඳහා ඔබේ වෙනස්කම් ඉදිරිපත් කරන්න

ඔබ GitHub හි ඔබේ ගබඩාවට ගියහොත්, ඔබට `Compare & pull request` බොත්තමක් පෙනෙනු ඇත. එම බොත්තම මත ක්ලික් කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

දැන් pull request ඉදිරිපත් කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

ළඟදීම මම ඔබේ සියලු වෙනස්කම් මෙම ව්‍යාපෘතියේ ප්‍රධාන ශාඛාවට ඒකාබද්ධ කරමි. වෙනස්කම් ඒකාබද්ධ කළ පසු ඔබට දැනුම්දීමේ විද්‍යුත් තැපෑලක් ලැබෙනු ඇත.

## මෙතැන් සිට කොහේ යන්නද?

සුභ පැතුම්! ඔබ දායකයෙකු ලෙස නිතර හමුවන සම්මත _fork -> clone -> edit -> pull request_ කාර්ය ප්‍රවාහය ඔබ සම්පුර්ණ කර ඇත!


[web app](https://firstcontributions.github.io/#social-share)වෙත යාමෙන් ඔබේ දායකත්වය සමරන්න සහ එය ඔබේ මිතුරන් සහ අනුගාමිකයින් සමඟ බෙදා ගන්න

ඔබට කිසියම් උදව්වක් අවශ්‍ය නම් හෝ කිසියම් ප්‍රශ්නයක් ඇත්නම් ඔබට අපගේ ස්ලැක් කණ්ඩායමට සම්බන්ධ විය හැකිය. [Join our slack crew](https://join.slack.com/t/firstcontributors/shared_invite/zt-kpbyrmkk-JDkRtchcvRvQ0qK4iPmyvA)..

දැන් අපි ඔබට වෙනත් ව්‍යාපෘති සඳහා දායක වීම ආරම්භ කරමු. ඔබට ආරම්භ කළ හැකි පහසු ගැටළු සහිත ව්‍යාපෘති ලැයිස්තුවක් අපි සම්පාදනය කර ඇත්තෙමු. පරීක්ෂාකාරී වන්න[the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [අතිරේක ද්‍රව්‍ය](../additional-material/git_workflow_scenarios/additional-material.md)

## වෙනත් මෙවලම් භාවිතා කරන නිබන්ධන

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
