[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# प्रथम योगदान

सुरुवातीला कुठलीही गोष्ट करणे कठीण असते. विशेषत: आपण एकत्र काम करत असताना चुका होणे स्वाभाविक आहे. परंतु एकमेकांसोबत भेटणे आणि एकत्र कार्य करणे हेच तर मुक्त स्त्रोत (Open Source) चे गमक आहे. आम्ही आपले प्रथम मुक्त स्त्रोत योगदान (Contribution) सुलभ करण्यास मदत करू.

लेख वाचणे आणि ट्यूटोरियल पाहण्याने आपणास मदत होऊ शकते परंतु प्रत्यक्षात सराव करण्यापेक्षा काय चांगले आहे? या प्रकल्पाचा हेतू नवशिक्यांना आपले प्रथम योगदान देण्यासंदर्भात सोप्या स्वरुपात मार्गदर्शन प्रदान करण्याचा आहे. आपण आपले प्रथम योगदान देत असल्यास, खालील पायऱ्यांचे अनुसरण करा.

#### *जर आपल्याला कमांड लाईन (CLI) सोयीस्कर वाटत नसेल तर [GUI टूल्स वापरण्यासंदर्भात ट्यूटोरियल येथे आहेत.](#इतर-साधने-वापरण्याबाबतीत-ट्युटोरियल)*


[<img src="https://firstcontributions.github.io/assets/Readme/pirate.png" width="22">](translations/README.en-pirate.md)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

आपण आपल्या मशीनवर Git नसेल तर, [येथुन इन्स्टॉल करा](https://help.github.com/articles/set-up-git/).

## रिपॉझिटरी (Repository) ला फोर्क (Fork) करणे

फोर्क बटण क्लिक करून या रिपोला फोर्क करा.
हे आपल्या खात्यात या रिपॉझिटरीची प्रत (कॉपी) तयार करेल.

## रिपॉझिटरी (Repository) ला क्लोन (Clone) करणे

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

आता फोर्क केलेला रिपो आपल्या संगणकावर क्लोन (Clone) करा. यासाठी आपण आपल्या गिटहब (GitHub) खात्यावर जा. जो रिपो आपण फोर्क केलेला आहे, त्याला उघडा. उघडलेल्या रिपोत उजव्या बाजुला वर `Clone or download` बटण दिसेल, त्यावर क्लिक करा. नंतर तेथील `Copy to clipboard` या आयकॉनवर क्लिक करा. याद्वारे प्रस्तुत रिपोची लिंक (URL) कॉपी झालेली असेल.

आता आपले टर्मिनल (Terminal) उघडा व त्यात खालील git आदेश (Command) चालवा.

```
git clone <कॉपी-केलेली-लिंक>
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

येथे `<कॉपी-केलेली-लिंक>` (त्रिकोणी कंस वगळता) यास आपण आताच कॉपी केलेली URL लिंक असे ग्राह्य धरण्यात यावे. ही URL लिंक मिळवण्याकरता याआधीच्या पायरीचे अवलोकन करावे.

उदाहरणार्थ:

```
git clone https://github.com/तुमचे-युझर-नाव/first-contributions.git
```

येथे `तुमचे-युझर-नाव` याचा अर्थ आहे, आपल्या गिटहब खात्याचे नाव (Username).

आता एंटर (Enter/Return) बटण दाबा. याद्वारे प्रस्तुत रिपो `first-contributions` आपल्या संगणकावर कॉपी होईल.

## ब्रांच (Branch) बनवणे.

आपल्या टर्मिनल वरुन आपली रिपो फोल्डर/डायरेक्टरी (Folder/Directory) बदला (जर आपण अद्याप बदलले नसेल तर).

```
cd first-contributions
```

आता `git checkout` ही कमांड वापरुन नवीन ब्रांच तयार करा.

```
git checkout -b <आपल्या-ब्रांचचे-नाव-येथे-टाका>
```

उदा:

```
git checkout -b add-rahul-thakare
```

(प्रत्येक ब्रांचच्या नावात `add` हा शब्द असणे आवश्यक नाही, परंतु वरील उदाहरणात त्याचा समावेश असणे ही एक वाजवी गोष्ट आहे कारण ईथे आपले नाव सूचीमध्ये जोडणे हा या शाखेचा उद्देश आहे.)

## आवश्यक बदल करणे आणि ते बदल कमिट (Commit) करणे.

आता मजकूर संपादक मध्ये `Contributors.md` फाइल उघडा, व त्यात आपले नाव जोडा. फाइलच्या सुरवातीस किंवा समाप्तीमध्ये जोडू नका. त्यामध्ये कुठेही ठेवा. आता फाईल सेव्ह (Save) करा.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />
आता तुम्ही पुन्हा टर्मिनल कडे जाल आणि `git status` ही कमांड चालवाल तर तुम्हाला त्यात काही बदल झालेले दिसतील.

`git add` कमांड वापरुन आपण तयार केलेल्या शाखेत ते बदल जोडा

```
git add Contributors.md
```

आता `git commit` ही कमांड वापरुन आपले बदल कमिट/सुरक्षित करा.

```
git commit -m "Add <तुमचे-नाव> to Contributors list"
```

`<तुमचे-नाव>` च्याऐवजी आपले नाव टाका.

## गिटहब मध्ये आपले बदल पुश करणे.

`git push` वापरून आपले बदल पुश करा

```
git push origin <आपल्या-शाखेचे-नाव>
```

`<आपल्या-शाखेचे-नाव>` च्या जागी आपल्या ब्रांचचे नाव टाका.

## पुनरावलोकनासाठी आपले बदल सबमिट करणे.

आपण आपल्या गिटहब प्रोफाइलवर आपल्या रिपो वर गेल्यास, आपल्याला `Compare & pull request` पाठविण्याचा पर्याय दिसेल, ते दाबा.
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

आता आपल्या `Pull request` सबमिट करा.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

लवकरच मी आपले बदल या प्रकल्पाच्या मुख्य शाखेत विलीन करेन. जेव्हा आपले बदल विलीन होतील तेव्हा आपल्याला ई-मेल मिळेल.

## आता पुढे काय?

अभिनंदन! आपण नुकतीच _fork -> clone -> edit -> PR_ ही कार्यपद्धती पूर्ण केली आहे ज्यास आपणास एक योगदानकर्ता (Contributor) म्हणून सदैवच तोंड द्यावे लागते!

आपले योगदान साजरे करा आणि [येथे](https://firstcontributions.github.io/#social-share) जाऊन आपल्या मित्र आणि अनुयायांसह शेअर/सामायिक करा.

आपल्याला कोणत्याही मदतीची आवश्यकता असल्यास किंवा काही प्रश्न असल्यास आपण आमच्या स्लॅक टीममध्ये सामील होऊ शकता. [स्लॅक टीममध्ये सामील व्हा](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

आता आपण इतर प्रकल्पांमध्येही आपले योगदान देऊ शकता. आपण प्रारंभ करू शकाल अशा सुलभ समस्यांसह (Issues) आम्ही काही प्रोजेक्टची सूची संकलित केली आहे. [येथे वेब अॅप मधील प्रकल्पांची यादी पहा.](https://firstcontributions.github.io/#project-list)

## इतर साधने वापरण्याबाबतीत ट्युटोरियल

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
