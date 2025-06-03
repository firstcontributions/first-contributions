[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

## የመጀመሪያ አስተዋፅኦዎች

ይህ ፕሮጀክት ጀማሪዎች የመጀመሪያ አስተዋጾ የሚያደርጉበትን መንገድ ለማቅለል እና ለመምራት ያለመ ነው። የመጀመሪያዎን አስተዋፅዖ ለማድረግ ከፈለጉ ከታች ያሉትን ደረጃዎች ይከተሉ።

_በትእዛዝ መስመር ካልተመቸዎት፣ [የግዩ(GUI) መሳሪያዎችን በመጠቀም አጋዥ ስልጠናዎች እዚህ አሉ።](#ሌሎች መሳሪያዎችን በመጠቀም አጋዥ ስልጠናዎች)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### በማሽንዎ ላይ ጊት ከሌለዎት ፤ [ይጫኑት።](https://docs.github.com/en/get-started/quickstart/set-up-git).

## ይህንን ማከማቻ ሹካ ያድርጉ

በዚህ ገጽ ላይኛው ክፍል ላይ ያለውን የሹካ ቁልፍን ጠቅ በማድረግ ይህንን ማከማቻ ሹካ ያድርጉት።
ይህ በአንተ መለያ ውስጥ የዚህን ማከማቻ ቅጂ ይፈጥራል።

## የማከማቻውን ተመሳሳይ ፍጠር

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

አሁን ሹካውን ተመሳሳይ ማከማቻ በማሽንዎ ይፍጥሩ። ወደ GitHub መለያዎ ይሂዱ፤ ሹካ የትደረገውን ማከማቻ ይክፈቱ፤ የኮድ ቁልፍን ጠቅ ያድርጉ እና  ከዚያ _ወደ ቅንጥብ ሰሌዳ ቅዳ_ የሚለውን ጠቅ ያድርጉ::

ተርሚናል ይክፈቱ እና የሚከተለውን የgit ትዕዛዝ run 

```bash
git clone "የቀዱትን url "
```

"አሁን የገለበጡት url" (ያለ ጥቅስ ምልክቶች) የማከማቻ (የዚህ ፕሮጀክት ሹካ) url ነው። urlን ለማግኘት የቀደመውን ደረጃዎች ይመልከቱ።

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

ለምሳሌ:-

```bash
git clone git@github.com:ይህ-አንተ-ነህ/first-contributions.git
```

'ይህ-አንተ-ነህ' የእርሶ GitHub ተጠቃሚ username ነው።እዚህ በ GitHub ላይ ያለውን የመጀመሪያ አስተዋፅዖ(first-contributions) ማከማቻ ይዘቶችን ወደ ኮምፒውተርዎ እየገለበጡ ነው።

## ቅርንጫፍ ይፍጠሩ

በኮምፒተርዎ ላይ ወዳለው የማከማቻ ማውጫ ይቀይሩ (እዚያው ከሌሉ ማለት ነው!)፡

```bash
cd first-contributions
```

አሁን የ‹git switch› ትዕዛዝን በመጠቀም ቅርንጫፍ ይፍጠሩ፡

```bash
git switch -c የእርስዎ-አዲሱ-ቅርንጫፍ-ስም
```

ለምሳሌ:-

```bash
git switch -c ይሁን-አለማየሁ
```

## አስፈላጊ ለውጦችን ያድርጉ እና ለውጦችን ይፈጥሙ(commit)

አሁን የ‹Contributors.md› ፋይልን በጽሑፍ አርታኢ ውስጥ ይክፈቱ ፤ ስምዎትን ጨምርበት። በፋይሉ መጀመሪያ ወይም መጨረሻ ላይ አይጨምሩት። በመካከል የትኛውም ቦታ ላይ ያስቀምጡት. አሁን, ፋይሉን ያስቀምጡ(save).

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ወደ የፕሮጀክት ማውጫው ሄደው ትዕዛዙን `git status' ከፈጸሙ፣ ለውጦች እንዳሉ ያያሉ።

የ‹git add› ትዕዛዙን በመጠቀም እነዚያን ለውጦች ወደ ፈጠሩት ቅርንጫፍ ያክሉ።

```bash
git add Contributors.md
```

አሁን የ‹git commit› ትዕዛዙን በመጠቀም እነዚህን ለውጦች ያድርጉ፡:

```bash
git commit -m "የአስተዋጽዖ አበርካቾች ዝርዝር ውስጥ የእርስዎን-ስም ያክሉ"
```

'የእርስዎን-ስም'ን በስምዎ ይተኩ፡፡

ለውጦችን ወደ GitHub ይግፉ

‹git push› የሚለውን ትዕዛዝ በመጠቀም ለውጦችዎን ይግፉ፡፡

```bash
git push -u origin የእርስዎ-ቅርንጫፍ-ስም
```

ቀደም ብለህ በፈጠርከው የቅርንጫፍ ስም 'የአንተ-ቅርንጫፍ-ስም'ን ይትኩ።

<details>
<summary> <strong>በመግፋት ላይ ማንኛውም ስህተት ካጋጠመህ ፤ እዚህ ጠቅ አድርግ:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

</details>

## ለውጦችዎን ለግምገማ ያስገቡ

በ GitHub ላይ ወደ ማከማቻዎ ከሄዱ፣ 'አወዳድር እና ጥያቄን ጎትት' የሚለውን ቁልፍ ያያሉ። በዚያ ቁልፍ ላይ ጠቅ ያድርጉ።

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

አሁን የመሳብ ጥያቄውን ያስገቡ።

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

በቅርቡ ሁሉንም ለውጦችዎን ወደ የዚህ ፕሮጀክት ዋና ቅርንጫፍ አዋህዳለሁ። ለውጦቹ ከተዋሃዱ በኋላ የማሳወቂያ ኢሜይል ይደርስዎታል።

## ከዚህስ ወዴት ልሂድ?

እንኳን ደስ ያለህ! ልክ እንደ አስተዋጽዖ አበርካች የሚያጋጥሙትን መደበኛ _fork -> clone -> አርትዕ -> የመሳብ ጥያቄ_ የስራ ፍሰትን አጠናቀዋል!

አስተዋጾዎን ያክብሩ እና ወደ ድር በመሄድ ለጓደኞችዎ እና ተከታዮችዎ ያካፍሉ።(https://firstcontributions.github.io/#social-share).

ማንኛውም እርዳታ ከፈለጉ ወይም ማንኛውም ጥያቄ ካለዎት የእኛን 'slack' ቡድን መቀላቀል ይችላሉ::(https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w).

አሁን ለሌሎች ፕሮጀክቶች በማበርከት እንጀምር። እርስዎ ሊጀምሩባቸው የሚችሉ ቀላል ጉዳዮች ያላቸውን የፕሮጀክቶች ዝርዝር አዘጋጅተናል።በድር መተግበሪያ ውስጥ ያሉትን የፕሮጀክቶች ዝርዝር ይመልከቱ(https://firstcontributions.github.io/#project-list).

## [ተጨማሪ ቁሳቁስ](additional-material/git_workflow_scenarios/additional-material.md)

## ሌሎች መሳሪያዎችን በመጠቀም አጋዥ ስልጠናዎች

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>ይህ ፕሮጀክት የሚደገፈው በ:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>





