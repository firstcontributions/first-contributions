[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# మొదటి కాంట్రిబ్యూషన్ 

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

మొదటి సరి ఏదైనా చేస్తే అది కొంచం కష్టాంగానే ఉంటుంది. మీరు వేరే వాళ్ళతో కలిసి పనిచేస్తున్నప్పుడు తప్పులు చెయ్యడం అంత సౌకర్యంగా ఉండదు . మేము ఓపెన్ సోర్స్ కి కొత్తగా కాంట్రిబ్యూటె చేసే వాళ్లకు మార్గం సుగమం చేసేందుకు సహాయం చేస్తాం .

ఆర్టికల్స్ చదవడం మరియు ఆన్లైన్ ట్యుటోరియల్స్ చూడడం ఉపయోగకారమే కానీ ఆచరించడం కంటే ఏది ఉపయోగకరం ? ఈ ప్రాజెక్ట్ మీకు మీ మొదటి కాంట్రిబ్యూషన్ / సహకారం చేయడం కోసం సహాయం చేస్తుంది . మీరు ఓపెన్ సోర్స్  సంఘానికి కాంట్రిబ్యూట్ చెయ్యాలి అనుకుంటే , ఈ కింది సూచనలను ఆచరించండి.

మీ కంప్యూటర్ లో git లేకపోతె, [ఈ లింక్ కి వెళ్ళండి](https://help.github.com/articles/set-up-git/)

## రేపోసిటోరీ ని ఫోర్క్ చేయుట

ఫోర్క్ బటన్ పై క్లిక్ చేసి ఈ రేపోసిటోరీ ని ఫోర్క్ చేసుకోవచ్చు . ఈ పధ్ధతి  మీ Github ఖాతా లో  ఈ రేపోసిటోరీ ని ఒక కాపీ చేస్తుంది .

## రేపోసిటోరీ ని క్లోన్ చేయుట 

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

ఇప్పుడు మీరు ఈ రేపోసిటోరీ మీ కంప్యూటర్ లో క్లోన్ చెయ్యాలి (అంటే డౌన్లోడ్ చేయుట) .ఈ రేపోసిటోరీ ని క్లోన్ చేయుటకు మీ github ఖాతా కి వెళ్లి క్లోన్ బటన్ పై క్లిక్ చేస్తే అక్కడ ఉన్న క్లిప్బోర్డు ఐకాన్ పై క్లిక్ చెయ్యండి, ఇప్పుడు మీరు రేపో యుఆర్ఎల్ ని కాపీ చేశారు .
మీ కంప్యూటర్ లో ఒక టెర్మినల్/ కమాండ్ ప్రాంప్ట్ ని తెరిచి ఈ క్రింది  git ఆదేశాన్ని రన్ చెయ్యండి
```
git clone "మీరు కాపీ చేసిన యుఆర్ఎల్"
```

ఇక్కడ "మీరు కాపీ చేసిన యుఆర్ఎల్ " (కొటేషన్ మార్కులు లేకుండా ) ఏ ఈ రేపోసిటోరీ యొక్క యుఆర్ఎల్. యుఆర్ఎల్ పొందుట కొరకు మునుపటి ూచనను చుడండి.

ఉదాహరణకు :

```
git clone https://github.com/మీ-పేరు/first-contributions.git
```

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

మీ-పేరు మీ github అకౌంట్ యొక్క పేరు. దీనిని మీరు మీ కంప్యూటర్ లో github నుంచి ఫస్ట్-కాంట్రిబ్యూషన్స్ రెపో ని కాపీ చేస్తున్నారు అంటే మీరు ఆ రెపో ని మీ కంప్యూటర్ లో ఒక లోకల్ కాపీ చేస్తున్నారు.

## ఒక బ్రాంచ్ సృష్టించుట 

మీ కంప్యూటర్ లో కాపీ అయిన రెపో  యొక్క ఫోల్డర్ కి వెళ్ళాలి (ఇప్పటి వరకు వెళ్లకపోతే )

```
cd first-contributions
```

ఇప్పడు `git checkout ` ఆదేశాన్ని ఉపయోగించి ఒక బ్రాంచ్ సృష్టించండి. -b కొత్త బ్రాంచ్ ని సూచిస్తుంది.

```
git checkout -b <మీ-బ్రాంచ్-పేరు>
```

ఉదాహరణకు:

```
git checkout -b add-alonzo-church 
```

( బ్రాంచ్ పేరు లో add లేకపోయినా పర్వాలేదు కానీ ఉండడం వలన మీ యొక్క ఉద్దేశాన్ని సూచిస్తుంది. )

## అవసరమైన మార్పులు చేయుట మరియు కమిట్ చేయుట

ఇప్పుడు `Contributors.md ` ఫైల్ ని టెక్స్ట్ ఎడిటర్ లో ఓపెన్ చెయ్యండి, దాని లో మీరు పేరు ని చేర్చండి. మీ పేరుని ప్రారంభం లో గాని చివరి లో గాని చేర్చొద్దు.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />


మీరు ఇప్పుడు `git status` ఆదేశాన్ని రన్ చెయ్యండి.  ఇప్పడు మీరు చేసిన మార్పుల్ని చూడగలరు.

ఆ మార్పుల్ని మీరు సృష్టించిన బ్రాంచ్ కి జోడించడానికి git add కమాండ్ ని ఉపయోగించగలరు .
```
git add Contributors.md
```

ఇప్పుడు మీరు చేసిన మార్పులను కమిట్ చేయుటకు `git commit ` కమాండ్ ని ఉపయోగించగలరు.

```
git commit -m "Add <మీ-పేరు> to Contributors list"
```

<మీ-పేరు> చోట మీ పేరుని చేర్చండి.

## మీ మార్పులను github లో పుష్ చేయుట

`git push ` కమాండ్ ని ఉపయోగించి మీ మార్పుల్ని github లోకి పుష్ చేయగలరు.
```
git push origin <మీ-బ్రాంచ్-యొక్క-పేరు>
```

`<మీ-బ్రాంచ్-యొక్క-పేరు>` బదులు గా మీ బ్రాంచ్ పేరు ని చేర్చగలరు. |

## మీ మార్పులను రివ్యూ చేసి సబ్మిట్ చేయుట

ఒకవేళ మీరు మీ github ప్రొఫైల్ లో మీ రెపో కి వెళ్ళినట్లైతే మీకు Compare & pull request ఆప్షన్ ని చూడగలరు. ఆ బటన్ ని ప్రెస్ చెయ్యండి .
<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

ఇప్పుడు మీ pull request ని సబ్మిట్ చెయ్యగలరు.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />
వెంటనే నేను మీ మార్పుల్ని నేను master బ్రాంచ్ ని మెర్జ్ చేస్తాను. నేను మెర్జ్ చేసిన వెంటనే మీకు మెర్జ్ అయ్యినట్లు ఒక నోటిఫికేషన్ వస్తుంది.

## తరువాత ఏంటి ?

అభినందనలు! మీరు కంట్రిబ్యూటర్ గా తరచూ ఎదురుకునే ప్రామాణికమైన fork -> clone -> edit -> PR వర్క్ ఫ్ల్లో ను పూర్తి చేసారు.

మీ మొదటి కాంట్రిబ్యూషన్ ను పూర్తి చేసిన సంతోషాన్ని మీ స్నేహితులతో పంచుకోండి [వెబ్ అప్](https://roshanjossey.github.io/first-contributions/#social-share)  లోకి వెళ్లి . 

మా [slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)లోకి జాయిన్ అయ్యి మీ సందేహాలను లేదా మీ ప్రశ్నల ను మాకు తెలపండి.

ఇప్పుడు మీరు మరిన్ని ప్రాజెక్ట్స్ లో కాంట్రిబ్యూట్ చెయ్యడం మొదలు పెట్టవచ్చు. మేము మీ కోసం సులువైన సమస్యలు వున్న ఒక జాబితాను రూపొందించాము. [ప్రోజెక్టుల యొక్క జాబితా](https://roshanjossey.github.io/first-contributions/#project-list)

## ఇతర టూల్స్ వాడుటకు ట్యుటోరియల్స్

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## స్వీయ ప్రమోషన్ 

మీకు ఈ ప్రాజెక్ట్ నచ్చితే, దీనిని [GitHub](https://github.com/Roshanjossey/first-contributions) లో స్టార్ చెయ్యండి. 
మీకు ఇంకా ఏమైనా సహాయం చెయ్యాలి అనుకుంటే [రోషన్](https://roshanjossey.github.io/) twitter మరియు
[GitHub](https://github.com/roshanjossey) లో ఫాలో అవ్వండి.

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>