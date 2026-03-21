[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![లైసెన్స్: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![ఓపెన్ సోర్స్ సహాయకులు](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# మొదటి సహకారాలు

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Git Bash వెర్షన్ |
| ------------------------------------------------- ------------------------------------------------- ------------- | ---------------- |

ఇది కష్టం. మీరు మొదటిసారి ఏదైనా చేసినప్పుడు అది ఎప్పుడూ కష్టంగానే ఉంటుంది. ముఖ్యంగా మీరు సహకారంతో పని చేస్తున్నప్పుడు, తప్పులు చేయడం సౌకర్యంగా అనిపించదు. కానీ ఓపెన్ సోర్స్ అంటే సహకారం మరియు కలిసి పని చేయడం. కొత్త ఓపెన్ సోర్స్ సహకారదారులు మొదటిసారి నేర్చుకుని సహకరించే విధానాన్ని సులభతరం చేయాలని మేము కోరుకుంటున్నాము.

వ్యాసాలు చదవడం, ట్యూటోరియల్స్ చూడడం సహాయపడవచ్చు, కానీ ఏదీ గందరగోళం చేయకుండా నిజంగా చేసి చూడడాన్ని మించినది ఏముంటుంది? ఈ ప్రాజెక్ట్ మార్గదర్శకతను అందించడం మరియు కొత్తవారు తమ మొదటి సహకారం చేసే విధానాన్ని సరళీకరించడం లక్ష్యంగా పెట్టుకుంది. మీరు ఎంత రిలాక్స్‌గా ఉంటే, అంత బాగా నేర్చుకుంటారని గుర్తుంచుకోండి. మీ మొదటి సహకారం చేయాలనుకుంటే, కింద ఉన్న సులభమైన దశలను అనుసరించండి. మేము మీకు హామీ ఇస్తున్నాము, ఇది సరదాగా ఉంటుంది.

మీ Windows కంప్యూటరులో Git Bash లేకపోతే, [దాన్ని ఇన్‌స్టాల్ చేయండి](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="ఈ రిపాజిటరీని ఫోర్క్ చేయండి" />

## ఈ రిపాజిటరీని ఫోర్క్ చేయండి

ఈ పేజీ పై కుడి వైపున ఉన్న Fork బటన్‌పై క్లిక్ చేసి ఈ రిపోను ఫోర్క్ చేయండి.
దీంతో మీ ఖాతాలో ఈ రిపాజిటరీకి ఒక ప్రతిని సృష్టిస్తుంది.

## రిపాజిటరీని క్లోన్ చేయండి

ఇప్పుడు ఈ రిపోను మీ కంప్యూటర్‌లో క్లోన్ చేయండి.

ముఖ్యమైనది: అసలు రిపోను క్లోన్ చేయవద్దు. మీ ఫోర్క్‌కు వెళ్లి దాన్నే క్లోన్ చేయండి.

రిపోను క్లోన్ చేయడానికి, "Code" పై క్లిక్ చేసి, క్రింద ఉన్న స్ట్రింగ్‌ను కాపీ చేయండి.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="కాపీ స్ట్రింగ్" />

మీరు డౌన్‌లోడ్ చేసిన git bash అప్లికేషన్‌ను తెరవండి. Windows మెషిన్‌లో ఉంటే అది కింది చిత్రంలా కనిపించాలి.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="Git Bash టెర్మినల్‌ను తెరవండి" />

ఈ ప్రాజెక్ట్‌ను సేవ్ చేయాలనుకుంటున్న ఫోల్డర్‌కు వెళ్లడానికి ఈ కమాండ్‌ను ఉపయోగించండి

```bash
cd <folder>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="ఒక ఫోల్డర్‌లోకి cd చేయండి" />

ఈ కమాండ్‌ను ఉపయోగించి రిపాజిటరీని క్లోన్ చేయడానికి పై దశలో మీరు కాపీ చేసిన స్ట్రింగ్‌ను ఉపయోగించండి

```bash
git clone <repo-url>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="రిపాజిటరీని క్లోన్ చేయండి" />

మీ మార్పులు చేయడానికి రిపో ఉన్న డైరెక్టరీకి వెళ్లి దాన్ని VS Code‌లో తెరవండి.

<img src="[https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png](https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png)" alt="కొత్తగా క్లోన్ చేసిన రిపోలోకి cd చేయండి" / >

## ఒక బ్రాంచ్‌ను సృష్టించండి

ఇప్పుడు ఈ సులభమైన కమాండ్‌ను ఉపయోగించి ఒక బ్రాంచ్‌ను సృష్టించండి. ఈ కమాండ్ మీ కోసం ఒక బ్రాంచ్‌ను సృష్టించడమే కాకుండా ఆ బ్రాంచ్‌కు మిమ్మల్ని మార్చుతుంది కూడా.

```bash
git checkout -b <branch-name>
```

మీ బ్రాంచ్‌కు `<add-your-name>` అని పేరు పెట్టండి. ఉదాహరణకు, "add-james-smith"

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="ఒక బ్రాంచ్‌ను సృష్టించండి" />

## అవసరమైన మార్పులు చేసి వాటిని commit చేయండి

ఇప్పుడు టెక్స్ట్ ఎడిటర్‌లో `Contributors.md` ఫైల్‌ను తెరిచి, పేజీ చివరకు స్క్రోల్ చేసి, అందులో మీ పేరును చేర్చి, ఫైల్‌ను సేవ్ చేయండి.

ఉదాహరణ: మీ పేరు జేమ్స్ స్మిత్ అయితే, అది ఇలా ఉండాలి.

[జేమ్స్ స్మిత్]([https://github.com/jamessmith](https://github.com/jamessmith))

ఈ కమాండ్‌ను నడపడం ద్వారా Contributors.md లో మార్పులు ఉన్నాయో చూడవచ్చు

```bash
git status
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="స్థితిని తనిఖీ చేయండి" />

ఇప్పుడు ఆ మార్పులను commit చేయండి:

మొదట మీరు చేసిన మార్పును staging area లోకి చేర్చడానికి ఈ కమాండ్‌ను ఉపయోగించండి

```bash
git add <filename>
```

ఈ కమాండ్‌ను టైప్ చేయడం ద్వారా ఒక commit message రాయండి

```bash
git commit -m "మీ పేరును contributors జాబితాలో చేర్చండి"
```

`<your-name>` ను మీ పేరుతో భర్తీ చేయండి.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="మార్పులను commit చేయండి" />

మీ commit పూర్తైందో లేదో తెలుసుకోవడానికి, ఒక సులభమైన `git log --oneline` కమాండ్‌ను నడపవచ్చు.

## GitHub కు మార్పులను push చేయండి

పై దశలను మీరు పూర్తి చేసిన తర్వాత

మీకు కావాలంటే, మిగిలిన భాగాన్ని కూడా ఇదే విధంగా తెలుగులో కొనసాగిస్తాను.
