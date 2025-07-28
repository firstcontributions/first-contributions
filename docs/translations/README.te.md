[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# ఓపెన్‌సోర్స్‌కు మీ మొదటి సహకారం

వ్యాసాలు చదవడం మరియు ట్యుటోరియల్స్ చూసే ప్రతిదీ సహాయపడుతాయి, కానీ వాస్తవ ఆచరణలో నేర్చుకోవడం మించి మెరుగైనది ఏమిటి?

ఈ ప్రాజెక్ట్ ముఖ్య ఉద్దేశ్యం: ప్రారంభకులకు ఓపెన్ సోర్స్ ప్రాజెక్టులలో మొదటి సహకారం అందించే పద్ధతులను సులభతరం చేసి, మార్గదర్శకత్వం ఇవ్వడం.

మీరు మొదటి సారి ఓపెన్ సోర్స్ లో సహకరించాలని భావిస్తున్నట్లయితే, దిగువ సూచనలను అనుసరించండి.

#### *మీకు కమాండ్ లైన్ సౌకర్యం లేకపోతే,  [ఇక్కడ GUI సాధనాలను ఉపయోగించి ట్యుటోరియల్స్ ఉన్నాయి.](#ఇతర-సాధనాలను-ఉపయోగించి-ట్యుటోరియల్స్)*
---

మీరు `గిట్ (git)` వర్షన్ కంట్రోల్ సిస్టమ్‌తో సౌకర్యవంతంగా లేకపోతే, ట్యుటోరియల్స్ కోసం పై లింక్‌ను చూడండి.

---

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

మీ కంప్యూటర్లో Git లేనట్లయితే, [ఇక్కడ Git ఇన్‌స్టాల్ చేయండి](https://help.github.com/articles/set-up-git/).

---

## ఈ రిపోజిటరీని  ఫోర్క్ చెయ్యండి

ఈ పేజీపై ఎగువ భాగంలో ఉన్న **Fork** బటనుపై క్లిక్ చేయండి.  
ఇది మీ ఖాతాలో ఈ రిపోజిటరీ కాపీని (Fork) సృష్టిస్తుంది.

---

## ఈ రిపోజిటరీని క్లోన్ చేయండి

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />
మీ GitHub ఖాతాలో Fork చేసిన ప్రాజెక్ట్‌కి వెళ్లి, **Code** బటన్ పై క్లిక్ చేసి URL కాపీ చేయండి.  
కంప్యూటర్లో టెర్మినల్ తెరవండి మరియు క్రింది ఆదేశం ఇవ్వండి:

git clone <మీరు కాపీ చేసిన URL>

ఉదాహరణ:

git clone https://github.com/your-username/first-contributions.git

---

## కొత్త బ్రాంచ్‌ను సృష్టించండి

మీ ప్రాజెక్ట్ ఫోల్డర్‌లోకి వెళ్లండి:

cd first-contributions

కొత్త బ్రాంచ్ సృష్టించి ఆ బ్రాంచ్‌లోకి మార్చండి:

git checkout -b add-your-name

బ్రాంచ్ పేరును మీకు అనుకూలంగా ఎంచుకోవచ్చు.

---

## అవసరమైన మార్పులు చేయండి

`Contributors.md` ఫైల్‌ను ఎడిట్ చేసి, మీ పేరును ఫైల్ మధ్యలో ఎక్కడైనా జోడించండి.  
ఫైల్ సేవ్ చేయడం మర్చిపోకండి.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

---

## మార్పులను Git లో Stage చేసి Commit చేయండి

git add Contributors.md
git commit -m "Add <your-name> to Contributors list"

`<your-name>` స్థానంలో మీ పేరు జతచేయండి.

---

## GitHubకి మార్చిన మార్పులను Push చేయండి

git push origin <your-branch-name>

`<your-branch-name>` స్థానంలో మీరు సృష్టించిన బ్రాంచ్ పేరు ఇవ్వండి.

<details>
<summary><strong>GitHubకి Push చేసే సమయంలో లోపాలు వచ్చినప్పుడల్లా ఇక్కడ క్లిక్ చేయండి:</strong></summary>

### ప్రమాణీకరణ లోపం (Authentication Error)

remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
fatal: Authentication failed for `https://github.com/<your-username>/first-contributions.git/`

దయచేసి [GitHub Personal Access Token](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/) ను ఉపయోగించండి లేదా  
[SSH కీ ఎలా సృష్టించాలో మరియు GitHubకి ఎలా జతచేయాలో](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) తెలియుకోండి.

</details>

---

## Pull Request (PR) సృష్టించండి

మీ GitHub అకౌంట్‌లో Fork చేసిన రిపోజిటరీ పేజీకి వెళ్లండి.  
మీ తాజా బ్రాంచ్ పట్ల **Compare & pull request** బటన్ కనిపిస్తుంది. దానిపై క్లిక్ చేయండి.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

తదుపరి పేజీలో అన్ని వివరాలు సరిచూసి **Create pull request** పై క్లిక్ చేయండి.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

---

## మార్పులు విలీనం (Merge) అయినపుడు

మీ పుల్ అభ్యర్థన (PR) యజమాని సమీక్షించి, సరి అయినా అనుకుంటే ప్రధాన బ్రాంచ్‌కు విలీనం చేస్తారు.  
మార్పులు విలీనం అయినప్పుడు మీకు నోటిఫికేషన్ ఇమెయిల్ వస్తుంది.

---

## శుభాకాంక్షలు!

మీరు ఫోర్క్ → క్లోన్ → ఎడిట్ → పుల్ రిక్వెస్ట్ వర్క్‌ఫ్లోను విజయవంతంగా పూర్తిచేశారు.

మీ సహకారాన్ని ఈ [వెబ్ యాప్ ద్వారా](https://firstcontributions.github.io/#social-share) షేర్ చేయండి.  
ఏవైనా ప్రశ్నలు లేదా సహాయం కావాలంటే, దయచేస్తూ మా స్లాక్ జట్టులో చేరండి:  
[స్లాక్ జట్టులో చేరండి](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

ఇప్పుడు మీరు ఇతర సులభమైన సమస్యలపై సహకరిస్తూ ప్రారంభించవచ్చు:  
[ప్రాజెక్టుల జాబితా](https://firstcontributions.github.io/#project-list)

---

### [అదనపు విషయం](../additional-material/git_workflow_scenarios/additional-material.md)

## ఇతర సాధనాలను ఉపయోగించి ట్యుటోరియల్స్

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
