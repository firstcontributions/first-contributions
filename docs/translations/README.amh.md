## የመጀመሪያ አስተዋፅኦዎች

ይህ ፕሮጀክት ጀማሪዎች የመጀመሪያ አስተዋጾ የሚያደርጉበትን መንገድ ለማቅለል እና ለመምራት ያለመ ነው። የመጀመሪያዎን አስተዋፅዖ ለማድረግ ከፈለጉ ከታች ያሉትን ደረጃዎች ይከተሉ።

***በcommand line(ተርሚናል) ካልተመቸዎት፣ [የGUI መሳሪያዎችን ለመጠቀም አጋዥ ስልጠናዎች እዚህ ያገኛሉ።](#tutorials-using-other-tools)***

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

### በማሽንዎ ላይ ጊት(git) ከሌለዎት ፤ [ይጫኑት](https://docs.github.com/en/get-started/quickstart/set-up-git) ።

## ይህንን ማከማቻ **fork** ያድርጉ

በዚህ ገጽ ላይኛው ክፍል ላይ ያለውን የfork button ጠቅ በማድረግ ይህንን ማከማቻ fork ያድርጉት።
ይህ በአንተ account ውስጥ የዚህን repository ቅጂ ይፈጥራል።

## የማከማቻውን ተመሳሳይ ይፍጠሩ

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

አሁን fork የተደረገውን ማከማቻ (repository) ቅጂ በማሽንዎ(በኮምፒውተርዎ) ይፍጥሩ። ወደ GitHub (account)መለያዎ ይሂዱ፤ fork የተደረገውን ማከማቻ ይክፈቱ፤ ኮድ የሚለውን button ጠቅ ያድርጉ እና  ከዚያ *ወደ clipboard ቅዳ* የሚለውን ጠቅ ያድርጉ::

ተርሚናል ይክፈቱ እና የሚከተለውን የgit ትዕዛዝ run

```bash
git clone "የቀዱትን url"

```

"አሁን የገለበጡት url" (ያለ ጥቅስ ምልክቶቹ) የማከማቻው (የዚህ ፕሮጀክት fork) url ነው። urlን ለማግኘት የቀደመውን ደረጃዎች ይመልከቱ።

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

ለምሳሌ:-

```bash
git clone git@github.com:ይህ-አንተ-ነህ/first-contributions.git

```

'ይህ-አንተ-ነህ' የእርሶ GitHub ተጠቃሚ username ነው። አሁን በ GitHub ላይ ያለውን የመጀመሪያ አስተዋፅዖ(first-contributions) ማከማቻ ይዘቶችን ወደ ኮምፒውተርዎ እየገለበጡ ነው።

## ቅርንጫፍ ይፍጠሩ

በኮምፒተርዎ ላይ ወዳለው የማከማቻ ማህደር ይግቡ (እዚያው ከሌሉ ማለት ነው!)፡

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

አሁን የ‹[Contributors.md](http://contributors.md/)› ፋይልን በጽሑፍ አርታኢ ውስጥ ይክፈቱ እና ስምዎትን ይጨምሩበት። በፋይሉ መጀመሪያ ወይም መጨረሻ ላይ አይጨምሩት። በመካከል የትኛውም ቦታ ላይ ያስቀምጡት። አሁን, ፋይሉን save ያድርጉ።

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ወደ የፕሮጀክት ማህደሩ ሄደው ይህን ትዕዛዝ (`git status`) ከፈጸሙ፣ ለውጦች እንዳሉ ያያሉ።

የ‹git add› ትዕዛዙን በመጠቀም እነዚያን ለውጦች ወደ ፈጠሩት ቅርንጫፍ ያክሉ።

```bash
git add Contributors.md

```

አሁን የ‹git commit› ትዕዛዙን በመጠቀም እነዚህን ለውጦች ያድርጉ፡:

```bash
git commit -m "የአስተዋጽዖ አበርካቾች ዝርዝር ውስጥ የእርስዎን-ስም ያክሉ"

```

'የእርስዎን-ስም' የሚለውን በስምዎ ይተኩ፡፡

ለውጦችን ወደ GitHub ይግፉ

‹git push› የሚለውን ትዕዛዝ በመጠቀም ለውጦችዎን ይግፉ፡፡

```bash
git push -u origin የእርስዎ-ቅርንጫፍ-ስም

```

ቀደም ብለዉ በፈጠሩት የቅርንጫፍ ስም 'የእርስዎን-ቅርንጫፍ-ስም'ን ይትኩ።

<details>
<summary> <strong>በመግፋት ላይ ማንኛውም ስህተት ካጋጠሞት ፤ እዚህ ጠቅ ያድርግ:</strong> </summary>

- Authentication Error
<pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

</details>

## ለውጦችዎን ለግምገማ ያስገቡ

በ GitHub ላይ ወደ ማከማቻዎ ከሄዱ፣ ‘compare & pull request' የሚለውን ቁልፍ ያያሉ። በዚያ ቁልፍ ላይ ጠቅ ያድርጉ።

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

አሁን pull request ያስገቡ።

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

በቅርቡ ሁሉንም ለውጦችዎን ወደ የዚህ ፕሮጀክት ዋና ቅርንጫፍ አዋህዳቸዋለሁ። ለውጦቹ ከተዋሃዱ በኋላ የማሳወቂያ ኢሜይል ይደርስዎታል።

## ከዚህስ ወዴት ልሂድ?

እንኳን ደስ ያሎዎት! ልክ እንደ አስተዋጽዖ አበርካች የሚያጋጥሙትን መደበኛ _fork -> clone -> አርትዕ -> የመሳብ ጥያቄ_ የስራ ፍሰትን አጠናቀዋል!

አስተዋጾዎን  ያጣጣጥሙ እና ወደ ድር በመሄድ ለጓደኞችዎ እና ተከታዮችዎ ያካፍሉ።(https://firstcontributions.github.io/#social-share).

ማንኛውም እርዳታ ከፈለጉ ወይም ማንኛውም ጥያቄ ካለዎት የእኛን 'slack' ቡድን መቀላቀል ይችላሉ::(https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w).

አሁን ለሌሎች ፕሮጀክቶች በማበርከት እንጀምር። እርስዎ ሊጀምሩባቸው የሚችሉ ቀላል ጉዳዮች ያላቸውን የፕሮጀክቶች ዝርዝር አዘጋጅተናል። በድር መተግበሪያ ውስጥ ያሉትን የፕሮጀክቶች ዝርዝር ይመልከቱ(https://firstcontributions.github.io/#project-list).

## [ተጨማሪ ቁሳቁስ](https://www.notion.so/additional-material/git_workflow_scenarios/additional-material.md)

## የሌሎች መሳሪያዎች አጠቃቀም አጋዥ ስልጠናዎች

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>ይህ ፕሮጀክት የሚደገፈው በ:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
