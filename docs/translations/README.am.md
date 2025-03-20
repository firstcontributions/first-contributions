[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# የመጀመሪያ አስተዋጽዖዎች

ይህ ፕሮጀክት ጀማሪዎች የመጀመሪያ አስተዋጾ የሚያደርጉበትን መንገድ ለማቅለል እና ለመምራት ያለመ ነው። የመጀመሪያዎን አስተዋፅዖ ለማድረግ ከፈለጉ ከታች ያሉትን ደረጃዎች ይከተሉ


#### command line ካልተመቸህ, [GUI መሳሪያዎችን በመጠቀም አጋዥ ስልጠናዎች አሉ።.](#Tutorials-Usin'-Other-Tools)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

በማሽንዎ ላይ git ከሌለዎት, [ይጫኑት](https://help.github.com/articles/set-up-git/).

## Fork this repository

በዚህ ገጽ ላይኛው ክፍል ላይ ያለውን fork ቁልፍን ጠቅ በማድረግ ይህንን ይጫኑት። 
ይህ በአንተ መለያ ውስጥ የዚህን repository ቅጂ ይፈጥራል።

## Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

አሁን Fork ይህን repository ወደ ማሽንዎ. ወደ GitHub መለያዎ ይሂዱ, የእርሶን repository ይክፈቱ. የኮድ ምልክቱን ጠቅ ያድርጉ እና ከዚያ ቅጂውን ምልክቱን ጠቅ ያድርጉ ለመቅዳት.

```
git clone "የቀዱትን url' ያስገቡ"
```
"የቀዱትን url' ያስገቡ" (ያለ ጥቅስ ምልክቶች) ይህ የዚህ repository url ነው(የእርሶ ቅጂ ፕሮጀክት). url ለማግኘት የቀደመውን ደረጃዎች ይመልከቱ.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

ለምሳሌ:

```
git clone https://github.com/this-is-you/first-contributions.git
```

where `this-is-you` የእርስዎ GitHub መለያ ስም ነው።. እዚህ በ GitHub ላይ ያለውን የመጀመሪያ አስተዋፅዖ repository ይዘቶችን ወደ ኮምፒውተርዎ እየገለበጡ ነው።

## Create a branch(ቅርንጫፍ ይፍጠሩ)

በኮምፒተርዎ ላይ ያለውን repository ማውጫ ይቀይሩ (እዚያ ከሌለዎት):

```
cd first-contributions
```

አሁን የ `git checkout` ትዕዛዝን በመጠቀም ቅርንጫፍ ይፍጠሩ:

```
git checkout -b <add-your-new-branch-name>
```

ለምሳሌ:

```
git checkout -b github-ethiopia
```

## አስፈላጊ ለውጦችን ያድርጉ እና ለውጦችን commit ያድርጉ

አሁን የ Contributors.md ፋይልን በጽሑፍ አርታኢ(editor) ውስጥ ይክፈቱ፣ ስምዎን በእሱ ላይ ያክሉ። በፋይሉ መጀመሪያ ወይም መጨረሻ ላይ አይጨምሩት። በመካከል የትኛውም ቦታ ላይ ያስቀምጡት. አሁን, ፋይሉን ያስቀምጡ(save).

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ወደ የፕሮጀክት ማውጫው ሄደው የ git status ከፈጸሙ ለውጦች እንዳሉ ያያሉ።

የ `git add` ትእዛዝን በመጠቀም እነዚያን ለውጦች አሁን በፈጠሩት ቅርንጫፍ ላይ አክል፡

```
git add Contributors.md
```

አሁን የ `git commit` ትዕዛዝ በመጠቀም እነዚህን ለውጦች ያድርጉ፡

```
git commit -m "Add <የእርስዎ-ስም> to Contributors list"
```

<የእርስዎ-ስም> ፋንታ የራስዎትን ስም ይጻፉ.

## ለውጦችን ወደ GitHub ይጫኑ

`git push` የሚለውን ትዕዛዝ በመጠቀም ለውጦችዎን ይጫኑ

```
git push origin <የእርስዎ-branch-name>
```

`<የእርስዎ-branch-name>` ፋንታ የራስዎትን branch ስም ያስገቡ

## ለውጦችዎን ለግምገማ ያስገቡ

በ GitHub ላይ ወደ repository ከሄዱ፣ `Compare & pull request` ጥያቄን ያያሉ። በዚያ ቁልፍ ላይ ጠቅ ያድርጉ።

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

አሁን pull request ጥያቄውን ያስገቡ

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

በቅርቡ ሁሉንም ለውጦችዎን ወደ የዚህ ፕሮጀክት ዋና ቅርንጫፍ አዋህዳለሁ. ለውጦቹ ከተዋሃዱ በኋላ የማሳወቂያ ኢሜይል ይደርስዎታል።

## ከዚህ ወዴት መሄድ አለብዎት ?

እንኳን ደስ ያለህ! አሁን መደበኛ fork -> clone -> edit -> pull request ሂደትን ጨርሰዋል. እንደ አስተዋጽዖ አበርካች ብዙ ጊዜ ይህ ሂደት ያጋትሞታል

አስተዋጾዎን ያክብሩ እና ለጓደኞችዎ እና ተከታዮችዎ ያካፍሉ ወደ [ዲህረ ገጾ በመሄድ](https://firstcontributions.github.io/#social-share).

ማንኛውም እርዳታ ከፈለጉ ወይም ማንኛውም ጥያቄ ካለዎት የእኛን [Slack ቡድን](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY) መቀላቀል ይችላሉ.

አሁን ለሌሎች ፕሮጀክቶች በማበርከት እንጀምር. እርስዎ ሊጀምሩባቸው የሚችሉ ቀላል ጉዳዮች ያላቸውን የፕሮጀክቶች ዝርዝር አዘጋጅተናል።. [እኚህን ማስፈተሪያ ይከተሉ](https://firstcontributions.github.io/#project-list).

### [ተጨማሪ ቁሳቁስ](../additional-material/git_workflow_scenarios/additional-material.md)

## ሌሎች መሳሪያዎችን በመጠቀም አጋዥ ስልጠናዎች

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)| 
