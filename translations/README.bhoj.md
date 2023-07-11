[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# पहिल योगदान

ई परियोजना के उद्देश्य लोगन के द्वारा आपना पहिला योगदान देने के प्रक्रिया के सरल और मार्गदर्शित करना होखे। जेर आप योगदान देन के चाहत बा, त निचे दियेल चरणों के पालन करीं।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

अगर रउरा कंप्यूटर पर गिट नइखे, [इसे स्थापित करें](https://help.github.com/articles/set-up-git/) ।

_अगर रउरा कमांड लाइन से सहज नइखीं त [त इहाँ ग्राफिकल इंटरफेस टूल के इस्तेमाल के ट्यूटोरियल दिहल बा।](#अन्य-टूल-का-उपयोग-करके-ट्यूटोरियल) ।_

## फॉर्क करइल एगो रिपॉज़िटरी

रउआँ एह रिपॉजिटरी के कांटा बटन पर क्लिक क के फॉर्क कर सकत बानी। ई तोहार गिटहब खाता में एगो कॉपी बनाईं जवन खाली रउरा खातिर उपलब्ध होखे.

## रिपॉज़िटरी के क्लोन कर

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

अब एह रिपोजिटरी के अपना कंप्यूटर पर क्लोन करीं (अर्थात डाउनलोड करीं)। अपना गिटहब खाता में जा के फोर्क वाला रिपोजिटरी खोलीं, कोड बटन पर क्लिक करीं, आ ओकरा बाद कॉपी टू क्लिपबोर्ड आइकन पर क्लिक करीं.

अपना कंप्यूटर पर एगो टर्मिनल/कमांड प्रॉम्प्ट खोलीं आ निम्नलिखित git कमांड (कमांड) चलाईं:

```
git clone "जवन यूआरएल रउरा अभी कॉपी कइले बानी"
```

जहाँ "जवन यूआरएल रउआँ अभी कॉपी कइले बानी" (बिना उद्धरण के) एह रिपोजिटरी खातिर यूआरएल हवे (एह प्रोजेक्ट के राउर फॉर्क)। यूआरएल पावे खातिर पिछला स्टेप देखीं।

उदाहरण खातिर:

```
git clone https://github.com/यह-आप-हैं/first-contributions.git
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

`यह-आप-हैं` राउर गिटहब खाता के नाम ह। इहाँ रउआँ गिटहब से first-contributions रिपोजिटरी के अपना कंप्यूटर पर कॉपी कर रहल बानी या एकर स्थानीय कॉपी बना रहल बानी।

## एगो शाखा बनावे के बा

अपना कंप्यूटर पर जवन रिपोजिटरी बनवले बानी ओकर कॉपी के फोल्डर/डायरेक्टरी में जाईं (अगर पहिले से नइखीं चलावत त निम्नलिखित कमांड चलाईं)

```
cd first-contributions
```

अब `git switch` कमांड के उपयोग करके एगो नया शाखा बनाईं।
-c विकल्प के इस्तेमाल नया शाखा बनावे खातिर कइल जाला।

```
git switch -c <अपनी-शाखा-का-नाम-जोड़ें>
```

उदाहरण खातिर:

```
git switch -c add-alonzo-church
```

( शाखा के नाम में `add` के जरूरत नइखे, बाकिर एकरा के शामिल कइल जरूरी बा काहे कि एह शाखा के मकसद एकर नाम सूची में जोड़ल होला. )

## जरूरी बदलाव करीं आ ऊ बदलाव कमिट करीं-

अब कवनो टेक्स्ट एडिटर में `Contributors.md` फाइल खोलीं आ ओकरा में आपन नाम लिखीं| फाइल के शुरुआत भा अंत में एकरा के मत जोड़ल जाव| बीच में कहीं रखे के बा।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


अगर रउआ `git status` कमांड चलावत बानी त रउआ बदलाव देखाई दिही।

ओह बदलावन के बनावल शाखा में जोड़े खातिर `git add` कमांड के इस्तेमाल करीं.

```
git add Contributors.md
```

अब `git commit` कमांड के इस्तेमाल से आपन बदलाव कमिट करीं।

```
git commit -m "Add <आपका-नाम> to Contributors list"
```

<आपका-नाम> के जगह आपन नाम लिखीं|

## आपन बदलाव के Github पर पुश करीं।

`git push` के उपयोग करके आपन बदलाव के पुश करीं।
```
git push origin <अपनी-शाखा-का-नाम-जोड़ें>
```

`<अपनी-शाखा-का-नाम-जोड़ें>` के जगह आपन शाखा के नाम लिखीं।

## समीक्षा (रिव्यु) खातिर आपन बदलाव जमा करीं|

अगर रउआ अपना Github प्रोफाइल पर अपना रिपोजिटरी में जाईं त रउआ के Compare & pull request विकल्प देखाई दिही। एकरा के दबा दिही।
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

अब आपन pull request जमा करीं।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
जल्दिये हम राउर बदलाव के एह प्रोजेक्ट के मास्टर शाखा में मर्ज करब| जब राउर बदलाव मर्ज हो जाई त रउरा के ईमेल मिल जाई|

## इहाँ से कहाँ जाए के बा ?

बधाई! रउआ _fork -> clone -> edit -> PR_ वर्कफ़्लो पूरा कर लेले बानी जवना के रउआ अक्सर योगदानकर्ता के रूप में सामना करे के पड़ी!

आपन पहिला योगदान के जश्न मनाईं आ [वेब एप्प](https://firstcontributions.github.io/#social-share) के माध्यम से अपना दोस्तन के साझा करीं।

अगर रउरा कुछ मदद के जरूरत बा भा कवनो सवाल बा त रउरा हमनी के स्लैक टीम से जुड़ सकेनी| [स्लैक पे ज्वाइन करें](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

अब रउरा अउरी प्रोजेक्ट में योगदान दे सकेनी, त आईं शुरुआत कइल जाव! हमनी के रउरा खातिर एगो अइसन प्रोजेक्ट के लिस्ट बनवले बानी जा जहाँ साधारण मुद्दा बा| अगर रउरा चाहब त ओहिजा से शुरुआत कर सकीलें| [प्रोजेक्ट्स कि लिस्ट](https://firstcontributions.github.io/#project-list)

## दोसरा संसाधन के इस्तेमाल करे के सिखावल

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)|[Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)|[GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)|[Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)|
