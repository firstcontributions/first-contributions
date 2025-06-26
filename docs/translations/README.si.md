[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# පළමු දායකත්වය (First Contribution)

මේ project එකේ අරමුණ, open-source වලට අලුත් අයට, ඒ අයගේ පළමු දායකත්වය (contribution) ලබාදෙන එක සරල කරලා, ඒකට මග පෙන්වීමක් ලබා දෙන එකයි. ඔයත් ඔයාගේ පළමු contribution එක කරන්න බලාගෙන ඉන්නවා නම්, මේ පියවර අනුගමනය කරන්න.

#### *Command line (terminal) එක භාවිතා කරලා මේ දේවල් කරන එක අමාරුයි වගේ නම්, [GUI මෙවලම් පාවිච්චි කරන මේ tutorials බලන්න.](#වෙනත්-මෙවලම්-සඳහා-වන-මාර්ගෝපදේශ)*

**සටහන:** ඔයාගේ computer එකේ git install කරලා නැත්නම්, මුලින්ම [මේ link එකෙන් ගිහින් install කරගන්න](https://docs.github.com/en/get-started/quickstart/set-up-git).

## 1. මේ Repository එක Fork කරගන්න

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="මෙම repository එක fork කරන්න" />

මේ පිටුවේ උඩ දකුණු පැත්තේ තියෙන 'Fork' button එක click කරන්න. එතකොට මේ repository එකේ copy එකක් ඔයාගේ GitHub ගිණුමේ හැදෙයි.
## 2. Fork කරගත්තු Repository එක Clone කරගන්න

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="මෙම repository එක clone කරන්න" />

දැන් ඔයා fork කරගත්ත repository එක ඔයාගේ computer එකට clone කරගන්න ඕන. ඒකට, ඔයාගේ GitHub ගිණුමට යන්න. Fork කරගත්ත repository එක open කරලා, 'Code' button එක click කරලා, එන URL එක copy කරගන්න.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL එක clipboard එකට copy කරගන්න" />

දැන් ඔයාගේ computer එකේ terminal (command prompt) එක open කරලා, මේ git command එක run කරන්න:

```bash
git clone "ඔයා දැන් copy කරගත්තු url එක"
```

"ඔයා දැන් copy කරගත්තු url එක" කියන තැනට (කමාන්ඩ් එකේදී උඩු කොමා දාන්නේ නැතුව) ඔයාගේ forked repository එකේ URL එක දාන්න.

උදාහරණයක් විදියට:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

`this-is-you` කියන තැනට ඔයාගේ GitHub username එක එන්න ඕන. මේ command එකෙන් කරන්නේ, *first-contributions repository* එකේ අන්තර්ගතය ඔයාගේ computer එකට copy කරන එකයි.

## 3. අලුත් Branch එකක් හදන්න

Terminal එකේ ඉඳන් ඔයා දැන් clone කරගත්ත repository එකේ folder එකට යන්න (ඔයා දැනටමත් ඒක ඇතුලේ නෙවෙයි නම්):

```bash
cd first-contributions
```

දැන්, ඔයාගේ වෙනස්කම් ටික කරන්න අලුත් branch එකක් හදන්න `git switch` command එක run කරන්න:

```bash
git switch -c ඔයාගේ-අලුත්-branch-එකේ-නම
```

උදාහරණයක් විදියට:

```bash
git switch -c add-kasun-perera
```

<details>
<summary> <strong>git switch භාවිතා කරන විට error එකක් ආවොත්, මෙතන click කරන්න:</strong> </summary>

"Git: `switch` is not a git command. See `git –help`" වගේ error පණිවිඩයක් ආවොත්, ඒකට හේතුව වෙන්න පුළුවන් ඔයා git වල පරණ version එකක් use කරන එක.

ඒ වගේ වෙලාවක, `git switch` වෙනුවට `git checkout` command එක use කරලා බලන්න:

```bash
git checkout -b your-new-branch-name
```

</details>


*(Branch එකේ නමට `add-` වගේ කෑල්ලක් එකතු කරන එක අනිවාර්ය නැහැ. ඒත්, අපි මේ branch එකෙන් කරන්නේ නමක් එකතු කරන එක නිසා, ඒ වගේ නමක් දාන එක හොඳ පුරුද්දක්.)*

## 4. අවශ්‍ය වෙනස්කම් කරලා Commit කරන්න

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

දැන් `Contributors.md` file එක ඔයා කැමති text editor එකකින් (උදා: VS Code, Notepad) open කරලා, ඔයාගේ නම ඒකට එකතු කරන්න. File එකේ මුලටම හරි අගටම හරි නම දාන්න එපා. මැද හරියට කොතනට හරි දාන්න. දැන් file එක save කරන්න.

ඔයා project folder එකේ terminal එකට ගිහින් `git status` කියලා type කලොත්, ඔයා කරපු වෙනස්කම් ටික පෙන්නයි.

ඒ වෙනස්කම් ටික ඔයා හදපු අලුත් branch එකට add කරන්න `git add` command එක run කරන්න:

```bash
git add Contributors.md
```

දැන්, `git commit` command එකෙන් මේ වෙනස්කම් ටික commit කරන්න:

```bash
git commit -m "Add your-name to Contributors list"
```

your-name` කියන තැනට ඔයාගේ නම දාන්න.

## 5. වෙනස්කම් ටික GitHub වලට Push කරන්න

ඔයා කරපු වෙනස්කම් ටික GitHub එකට push (upload) කරන්න `git push` command එක run කරන්න:

```bash
git push -u origin ඔයාගේ-branch-එකේ-නම
```

ඔයාගේ-branch-එකේ-නම` කියන තැනට ඔයා කලින් හදපු branch එකේ නම දාන්න.

## 6. ඔයාගේ වෙනස්කම් Pull Request එකක් ලෙස යවන්න

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="pull request එකක් හදන්න" />

ඔයාගේ GitHub ගිණුමේ තියෙන repository එකට ගියාම, ඔයාට `'Compare & pull request'` කියලා button එකක් පෙනෙයි. ඒක click කරන්න.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="pull request එක submit කරන්න" />

දැන් ඔයාගේ pull request එක submit කරන්න.

ඉක්මනින්ම මම ඔයාගේ වෙනස්කම් ටික මේ project එකේ ප්‍රධාන (main) branch එකට merge කරන්නම්. ඒක merge කරාට පස්සේ ඔයාට notification email එකක් එයි.

## මෙතැන් සිට කොහේ යන්නද?

සුභ පැතුම්! Open-source contributor කෙනෙක් විදියට ඔයා නිතරම භාවිතා කරන **fork -> clone -> edit -> pull request**  කියන සම්පූර්ණ ක්‍රියාවලියම ඔයා දැන් සාර්ථකව අවසන් කරලා තියෙන්නේ!

ඔයාගේ මේ පළමු දායකත්වය සමරන්න, ඒ වගේම යාළුවොත් එක්ක share කරගන්න [web app](https://firstcontributions.github.io/#social-share) එකට යන්න.

තවත් පුහුණුවක් ලබන්න කැමති නම්, [code contributions](https://github.com/roshanjossey/code-contributions) බලන්න.

දැන් ඔයාට වෙනත් projects වලටත් contribute කරන්න පටන්ගන්න උදව් කරමු. අපි ඔයාට පටන් ගන්නම ලේසි issues (ගැටළු) තියෙන projects ලැයිස්තුවක් හදලා තියෙනවා. [Web app එකෙන් ඒ projects ලැයිස්තුව බලන්න](https://firstcontributions.github.io/#project-list).

### [අතිරේක සම්පත්](../additional-material/git_workflow_scenarios/additional-material.md)

## වෙනත් මෙවලම් සඳහා වන මාර්ගෝපදේශ

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
