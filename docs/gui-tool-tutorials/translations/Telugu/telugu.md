[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# మొదటి సహకారాలు

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Git Bash వెర్షన్ |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |

కొత్తగా ఏదైనా ప్రారంభించడం కొంత కష్టంగానే అనిపిస్తుంది. ముఖ్యంగా ఇతరులతో కలిసి పనిచేసేటప్పుడు తప్పులు చేయడం సహజం. కానీ ఓపెన్ సోర్స్ అంటే ఒకరితో ఒకరు కలిసి నేర్చుకుంటూ, సహకరిస్తూ ముందుకు సాగడం. కొత్తగా ఓపెన్ సోర్స్‌లోకి వచ్చే వారు తమ మొదటి సహకారాన్ని సులభంగా చేయడానికి ఈ ప్రాజెక్ట్ రూపొందించబడింది.

ఈ ప్రాజెక్ట్ యొక్క లక్ష్యం మొదటిసారి సహకరించే వారికి దశలవారీగా మార్గనిర్దేశం చేయడం. మీరు ప్రశాంతంగా ఒక్కో దశను అనుసరిస్తే, మీ మొదటి సహకారం చేయడం చాలా సులభమవుతుంది. క్రింది సూచనలను అనుసరించండి — ఇది మీకు ఒక ఆసక్తికరమైన అనుభవంగా ఉంటుంది.

మీ Windows కంప్యూటరులో Git Bash ఇన్‌స్టాల్ చేసి లేకపోతే, [ఇక్కడ నుండి ఇన్‌స్టాల్ చేయండి](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## ఈ రిపోజిటరీని Fork చేయండి

ఈ పేజీ కుడి పైభాగంలో ఉన్న **Fork** బటన్‌పై క్లిక్ చేయండి. దీంతో ఈ రిపోజిటరీకి మీ GitHub ఖాతాలో ఒక కాపీ సృష్టించబడుతుంది.

## రిపోజిటరీని Clone చేయండి

ఇప్పుడు ఈ రిపోజిటరీని మీ కంప్యూటర్‌కు Clone చేయాలి.

**ముఖ్యం:** అసలు (Original) రిపోజిటరీని Clone చేయవద్దు. మీరు Fork చేసిన మీ స్వంత కాపీని మాత్రమే Clone చేయండి.

దీనికోసం **Code** బటన్‌పై క్లిక్ చేసి, కనిపించే URLని కాపీ చేసుకోండి.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

ఇప్పుడు Git Bash ను తెరవండి.

మీరు ఫైళ్లను ఉంచాలనుకునే ఫోల్డర్‌లోకి వెళ్లడానికి ఈ కమాండ్ ఉపయోగించండి:

`cd <folder>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />

ఆ తర్వాత మీరు కాపీ చేసిన URLతో ఈ కమాండ్ అమలు చేయండి:

`git clone <repo-url>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

ఇప్పుడు కొత్తగా Clone అయిన రిపోజిటరీ ఫోల్డర్‌లోకి వెళ్లి, దానిని VS Code లేదా మీకు ఇష్టమైన ఎడిటర్‌లో తెరవండి.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## కొత్త Branch సృష్టించండి

ఈ కమాండ్ ద్వారా కొత్త Branch సృష్టించి, అదే Branch‌కి మారండి.

```bash
git checkout -b <branch-name>
```

ఉదాహరణకు, మీ పేరు XYZ అయితే:

```bash
git checkout -b add-xyz
```

## అవసరమైన మార్పులు చేయండి

`Contributors.md` ఫైల్‌ను తెరిచి, చివరలో మీ పేరును జోడించి సేవ్ చేయండి.

ఉదాహరణ:

```
[Your Name](https://github.com/your-github-username)
```

మార్పులు ఉన్నాయా లేదా చూడటానికి:

```bash
git status
```

మార్పులను Stage చేయడానికి:

```bash
git add <file-name>
```

తర్వాత Commit చేయండి:

```bash
git commit -m "Add your name to the contributors list"
```

Commit సరిగ్గా జరిగిందో లేదో చూడటానికి:

```bash
git log --oneline
```

## GitHub కి Push చేయండి

ఈ కమాండ్ ద్వారా మీ మార్పులను GitHub కి పంపండి:

```bash
git push origin <branch-name>
```

## Pull Request సమర్పించండి

GitHubలో మీ Fork చేసిన రిపోజిటరీని తెరవండి.

**Compare & pull request** బటన్‌పై క్లిక్ చేయండి.

తర్వాత Pull Request (PR) ను సమర్పించండి.

మీ మార్పులను పరిశీలించిన తరువాత, వాటిని ప్రధాన (Main) Branch‌లో విలీనం (Merge) చేస్తారు. Merge పూర్తయ్యాక మీకు GitHub నుండి ఇమెయిల్ ద్వారా సమాచారం అందుతుంది.

## తరువాత ఏమి చేయాలి?

అభినందనలు! 🎉

మీరు ఓపెన్ సోర్స్‌లో సాధారణంగా ఉపయోగించే **Fork → Clone → Edit → Pull Request** విధానాన్ని విజయవంతంగా పూర్తి చేశారు.

మీ మొదటి సహకారాన్ని జరుపుకోండి మరియు మీ స్నేహితులతో పంచుకోండి.

ఏదైనా సహాయం కావాలన్నా లేదా ప్రశ్నలు ఉన్నా, మా Slack కమ్యూనిటీలో చేరండి.

### మరింత తెలుసుకోవడానికి

* Git Workflow గురించి మరింత తెలుసుకోండి.
* ఇతర టూల్స్ ఉపయోగించే ట్యుటోరియల్స్ కూడా చూడండి.
