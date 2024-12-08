
<!-- This section includes badges related to open source, license, and community engagement. -->


[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# පළමු දායකත්වය

| <img alt="GitHub ඩෙස්ක්ටොප්" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|

මෙය ටර්මිනලයේ සෑම දෙයක්ම කිරීමට අවශ්‍ය terminal nerds වන අපට මඟ පෙන්වීමක් වන අතර [Github-CLI](https://cli.github.com/) ට ස්තූතිවන්ත වන අතර, ඔබේ පළමු දායකත්වය සිහිපත් කරමින් අපට එය සාක්ෂාත් කර ගත හැකිය. එය විනෝදජනක, ප්‍රතිලාභදායක සහ ඉදිරියට යාමට පෙළඹවීමක් විය යුතුය!

අපි කිසිදු විටෙක අතුරුමුහුණතක් භාවිතා නොකරන බැවින් මෙම මාර්ගෝපදේශය තරමක් අභියෝගාත්මකය, නමුත් එය තවමත් ඇත්තෙන්ම විනෝදජනක වන අතර ඔබට අනිවාර්යයෙන්ම එය අනුගමනය කළ හැකිය!

පළමු අවශ්‍යතාවය වන්නේ:
- Git ස්ථාපනය කර ඇත ([git](https://git-scm.com/downloads) ස්ථාපනය කරන්නේ කෙසේද)
- Github ගිණුම


දැන් අපට [නිල ලේඛන](https://github.com/cli/cli#installation) අනුගමනය කිරීමෙන් අපගේ පද්ධතිය තුළ `github-cli` මෙවලම ස්ථාපනය කිරීමට අවශ්‍ය වේ.

ඊට පසු, අපි CLI වෙත පිවිසිය යුතුය, එබැවින් මෙම විධානය ඇතුළත් කරන්න:
```bash 
gh auth login
```

උපදෙස් අනුගමනය කරන්න, අපි සූදානම්!

# මෙම ගබඩාව fork කිරීම

මෙම විධානය ක්‍රියාත්මක කිරීම තරම්ම පහසුය:

```bash
gh repo fork firstcontributions/first-contributions
```

**වැදගත්: ඔබට එය clone කිරීමට අවශ්‍ය නම් එය ඔබෙන් විමසනු ඇත, "ඔව්" විකල්පය තෝරන්න**

# ශාඛාවක් නිර්මාණය කිරීම

අපි මෙම පියවර git සමඟ කරන්නෙමු, එබැවින් නම ඔබේ නම සමඟ ප්‍රතිස්ථාපනය කරමින් මෙම විධානය ඇතුළත් කරන්න, උදාහරණයක් ලෙස:

```bash 
git switch -c add-john-doe
```
# අවශ්‍ය වෙනස්කම් සිදු කර commit කරන්න
දැන් ඔබට පාඨ සංස්කාරකයක `Contributors.md` ගොනුව විවෘත කර එයට ඔබේ නම එක් කළ හැක. ඔබේ නම ආරම්භය සහ අවසානය අතර ඕනෑම තැනක තබන්න, ඉන්පසු ගොනුව සුරකින්න.

ව්‍යාපෘති නාමාවලියෙහි `git status` ක්‍රියාත්මක කරන්න, එවිට ඔබට වෙනස්කම් පෙනෙනු ඇත.
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/6873747072637F6F06F1000000000000000000000000 69627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

`git add` විධානය භාවිතයෙන් ඔබ දැන් නිර්මාණය කළ ශාඛාවට එම වෙනස්කම් එක් කරන්න:
`git add Contributors.md`

දැන් එම වෙනස්කම් `git commit` විධානය භාවිතයෙන් සිදු කරන්න:
`git commit -m "Add your-name to Contributors list`
ඔබේ නම සමඟ `your-name` වෙනුවට.


# වෙනස්කම් github වෙත තල්ලු කරන්න
`git push` විධානය භාවිතයෙන් ඔබගේ වෙනස්කම් තල්ලු කරන්න:

```
git push origin -u your-branch-name
```
ඔබ කලින් නිර්මාණය කළ ශාඛාවේ නම සමඟ `your-branch-name` වෙනුවට.

<details><summary><strong>ඔබට තල්ලු කිරීමේදී කිසියම් දෝෂයක් ඇත්නම්, මෙහි ක්ලික් කරන්න:</strong></summary>

- ### Authentication Error
     <pre>දුරස්ථ: මුරපද සත්‍යාපනය සඳහා වන සහාය 2021 අගෝස්තු 13 දින ඉවත් කරන ලදී. කරුණාකර ඒ වෙනුවට පුද්ගලික ප්‍රවේශ ටෝකනයක් භාවිතා කරන්න.
  දුරස්ථ: කරුණාකර වැඩි විස්තර සඳහා https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ බලන්න.
  මාරක: 'https://github.com/<your-username>/first-contributions.git/'</pre> සඳහා සත්‍යාපනය අසාර්ථක විය
  [GitHub හි නිබන්ධනය](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) වෙත යන්න ඔබගේ ගිණුමට SSH යතුරක් උත්පාදනය කිරීම සහ වින්‍යාස කිරීම.
  
</details>     


# ඔබගේ වෙනස්කම් සමාලෝචනය සඳහා ඉදිරිපත් කරන්න
දැන් අපගේ repo හි නාමාවලියෙහි මෙම විධානය ක්‍රියාත්මක කිරීමෙන් සමාලෝචනය සඳහා ඇදීමේ ඉල්ලීමක් සෑදීමට අපට ඉඩ සලසයි:

```bash 
gh pr create --repo firstcontributions/first-contributions
```

ඊට පස්සේ pull request එක ඉදිරිපත් කරන්න

ඔබගේ සඳහන් ඇදීමේ ඉල්ලීම ක්‍රියාත්මක වන ආකාරය බැලීමට ඔබට `gh status` විධානය භාවිතා කළ හැක.

## මෙතනින් කොහෙට යන්නද?

සුභ පැතුම්! ඔබ දායකයෙකු ලෙස නිතර හමුවන සම්මත _fork -> clone -> edit -> pull request_ කාර්ය ප්‍රවාහය සම්පූර්ණ කර ඇත!

[web යෙදුම](https://firstcontributions.github.io/#social-share) වෙත යාමෙන් ඔබේ දායකත්වය සමරන්න සහ එය ඔබේ මිතුරන් සහ අනුගාමිකයින් සමඟ සමරන්න.

ඔබට කිසියම් උදව්වක් අවශ්‍ය නම් හෝ කිසියම් ප්‍රශ්නයක් ඇත්නම් ඔබට අපගේ Slack කණ්ඩායමට සම්බන්ධ විය හැකිය. [Slack කණ්ඩායමට එකතු වන්න](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

දැන් අපි ඔබට වෙනත් ව්‍යාපෘති සඳහා දායක වීම ආරම්භ කරමු. ඔබට ආරම්භ කළ හැකි පහසු ගැටළු සහිත ව්‍යාපෘති ලැයිස්තුවක් අපි සම්පාදනය කර ඇත්තෙමු. [වෙබ් යෙදුමේ ව්‍යාපෘති ලැයිස්තුව](https://firstcontributions.github.io/#project-list) පරීක්ෂා කරන්න.

### [අතිරේක මූලාශ්‍ර](අතිරේක-ද්‍රව්‍ය/git_workflow_scenarios/additional-material.md)

## වෙනත් මෙවලම් භාවිතා කරන නිබන්ධන

[ආපසු ප්‍රධාන පිටුවට](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)