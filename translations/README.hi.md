[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# प्रथम योगदान

इस परियोजना का उद्देश्य शुरुआती लोगों द्वारा अपना पहला योगदान करने की प्रक्रिया को सरल और मार्गदर्शित करना है। यदि आप योगदान देना चाहते हैं, तो नीचे दिए गए चरणों का पालन करें।

आर्टिकल्स पढ़ना और ऑनलाइन ट्यूटोरियल्स देखना मददगार साबित हो सकते हैं, लेकिन बिना कुछ गलती करके खुद काम करने से अच्छा हो सकता है। इस प्रोजेक्ट आपको अपने पहले योगदान के लिए दिशा निर्देशित करेगा। याद रखें - जितने तनाव मुक्त होकर आप सीखेंगे, उतना ही बेहतर सीख पाएंगे। नीचे दिए गए निर्देशों का पालन करें।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

यदि आपके कंप्यूटर पर Git नहीं है तो, [इसे स्थापित करें](https://help.github.com/articles/set-up-git/) ।

_यदि आप कमांड लाइन के साथ सहज नहीं हैं, [तो यहाँ ग्राफिकल इंटरफेस (GUI) टूल्स का उपयोग करने वाले ट्यूटोरियल हैं] (#अन्य-टूल-का-उपयोग-करके-ट्यूटोरियल) ।_

## रिपॉज़िटरी को फोर्क करना

काँटा (फोर्क) बटन पर क्लिक करके इस रिपॉज़िटरी को फोर्क कर सकते हैं। यह आपके GitHub खाते (अकाउंट) में इस रिपॉज़िटरी की एक प्रति (कॉपी) बना देगा जो केवल आपके लिए उपलब्ध होगी।

## रिपॉज़िटरी को क्लोन करना

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

अब आप यह रिपॉज़िटरी अपने कंप्यूटर में क्लोन (अर्थात् डाउनलोड) करें । अपने GitHub अकाउंट पर जाएँ, फोर्कड रिपोजिटरी खोलें, Code/कोड बटन पर क्लिक करें और फिर copy to clipboard आइकॉन पर क्लिक करें ।

अपने कंप्यूटर पर एक टर्मिनल/कमांड प्रांप्ट खोलें और निम्न git आदेश (कमांड) चलाएँ:

```
git clone "यूआरएल जिसे आपने अभी कॉपी किया"
```

जहाँ "यूआरएल जिसे आपने अभी कॉपी किया" (उद्धरण चिह्नों के बिना) इस रिपॉज़िटरी के लिए यूआरएल है (इस परियोजना का आपका फोर्क) । यूआरएल प्राप्त करने के लिए पिछले निर्देश देखें ।

उदाहरण के लिए:

```
git clone https://github.com/यह-आप-हैं/first-contributions.git
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

`यह-आप-हैं` आपके GitHub अकाउंट का नाम है। यहाँ आप अपने कंप्यूटर में GitHub से first-contributions रिपॉज़िटरी को कॉपी कर रहे हैं अथवा उसकी एक लोकल/स्थानीय कॉपी बना रहे हैं ।

## एक शाखा (ब्राँच) बनाएँ 

अपने कंप्यूटर पर बनाई गई रिपॉज़िटरी की कॉपी के फोल्डर/डायरेक्टरी में जाएँ (यदि अभी तक नहीं की है तो निम्न आदेश चलाएँ)

```
cd first-contributions
```

अब एक नई शाखा बनाएँ `git switch` कमांड का उपयोग करके ।
नई शाखा बनाने के लिए -c ऑप्शन का उपयोग होता है ।  

```
git switch -c <अपनी-शाखा-का-नाम-जोड़ें>
```

उदाहरण के लिए:

```
git switch -c add-alonzo-church
```

( शाखा के नाम में `add` जोड़ने की आवश्यकता नहीं है, लेकिन इसमें शामिल होना जरूरी है क्योंकि इस शाखा का उद्देश्य एक सूची में अपना नाम जोड़ना है। )

## आवश्यक परिवर्तन करें और उन परिवर्तनों को कमिट करें-

अब `Contributors.md` फ़ाइल को एक टेक्स्ट एडिटर में खोलकर इसमें अपना नाम जोड़ दें। फ़ाइल की शुरुआत या अंत में इसे न जोड़ें। इसे बीच में कहीं भी रखें । 

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


आप यदि `git status` कमांड चलाएंगे , तो आपको अपने  द्वारा किये गए परिवर्तन देखेंगे।

उन परिवर्तनों को बनाई गई शाखा में जोड़ने के लिए `git add` कमांड का उपयोग करें ।

```
git add Contributors.md
```

अब अपने किये गए बदलावों को `git commit` कमांड का उपयोग करके कमिट करें ।

```
git commit -m "Add <आपका-नाम> to Contributors list"
```

<आपका-नाम> की जगह अपना नाम लिखें ।

## अपने बदलावों को Github में पुश करें ।

`git push` का उपयोग कर अपने परिवर्तन को पुश करें ।

```
git push origin <अपनी-शाखा-का-नाम-जोड़ें>
```

`<अपनी-शाखा-का-नाम-जोड़ें>` की जगह अपनी शाखा का नाम लिखें ।

## अपने बदलावों को रिव्यु के लिए सबमिट करें ।

यदि आप अपने Github प्रोफाइल पर अपनी रिपॉज़िटरी में जायेंगे तो आपको Compare & pull request का ऑप्शन दिखेगा। उसे दबाएं ।
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

अब अपनी pull request सबमिट करें ।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
जल्द ही मैं आपके बदलावों को इस प्रोजेक्ट की मुख्य शाखा में सम्मिलित कर दूंगा। आपको एक ईमेल आएगी जब आपके बदलाव सम्मिलित होंगे ।

## यहाँ से कहाँ जाएं?

बधाई! आपने _fork -> clone -> edit -> PR_ वर्कफ्लो की पूर्ति कर ली है, जिसका आप अक्सर एक योगदानकर्ता के रूप में सामना करेंगे! 

अपने पहले योगदान की खुशी में जश्न मनाएं तथा इसे [वेब एप्प](https://firstcontributions.github.io/#social-share) के जरिये अपने मित्रों के साथ शेयर करें। 

आप हमारी स्लैक टीम को ज्वाइन कर सकते हैं यदि आपको कुछ मदद चाहिए या आपके कोई प्रश्न हों । [स्लैक पे ज्वाइन करें](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w)

अब आप अन्य प्रोजेक्ट्स पर योगदान कर सकते हैं, तो चलिए शुरू करते हैं! हमने आपके लिए एक प्रोजेक्ट्स की सूचि तैयार की है जहाँ सरल इश्यूज हैं । आप चाहें तो वहाँ से आरम्भ कर सकते हैं । [प्रोजेक्ट्स कि लिस्ट](https://firstcontributions.github.io/#project-list)

## शिक्षण अन्य साधनो का उपयोग करने के लिए

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)|[Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)|[GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)|[Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)|
