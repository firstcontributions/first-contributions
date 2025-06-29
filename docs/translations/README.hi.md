[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# प्रथम योगदान

## विषय सूची

- [आवश्यकताएं](#आवश्यकताएं)
- [रिपॉज़िटरी को फोर्क करना](#रिपॉज़िटरी-को-फोर्क-करना)
- [रिपॉज़िटरी को क्लोन करना](#रिपॉज़िटरी-को-क्लोन-करना)
- [एक शाखा बनाएं](#एक-शाखा-ब्राँच-बनाएँ)
- [आवश्यक परिवर्तन करें और उन्हें कमिट करें](#आवश्यक-परिवर्तन-करें-और-उन-परिवर्तनों-को-कमिट-करें)
- [अपने बदलावों को GitHub में पुश करें](#अपने-बदलावों-को-github-में-पुश-करें)
- [अपने बदलावों को रिव्यू के लिए सबमिट करें](#अपने-बदलावों-को-रिव्यू-के-लिए-सबमिट-करें)
- [समस्या निवारण](#समस्या-निवारण)
- [यहाँ से कहाँ जाएं](#यहाँ-से-कहाँ-जाएं)
- [अन्य टूल्स का उपयोग करके ट्यूटोरियल](#अन्य-टूल्स-का-उपयोग-करके-ट्यूटोरियल)

## परिचय

इस परियोजना का उद्देश्य शुरुआती लोगों द्वारा अपना पहला योगदान करने की प्रक्रिया को सरल और मार्गदर्शित करना है। यदि आप अपना पहला ओपन सोर्स योगदान देना चाहते हैं, तो नीचे दिए गए चरणों का पालन करें।

आर्टिकल्स पढ़ना और ऑनलाइन ट्यूटोरियल्स देखना मददगार साबित हो सकते हैं, लेकिन वास्तव में काम करके सीखना सबसे अच्छा होता है। यह प्रोजेक्ट आपको अपने पहले योगदान के लिए दिशा निर्देशित करेगा। याद रखें - जितने तनाव मुक्त होकर आप सीखेंगे, उतना ही बेहतर सीख पाएंगे।

## आवश्यकताएं

### Git की स्थापना और सत्यापन

यदि आपके कंप्यूटर पर Git नहीं है तो, [इसे स्थापित करें](https://help.github.com/articles/set-up-git/)।

Git सही तरीके से स्थापित है या नहीं, इसकी जांच करने के लिए टर्मिनल/कमांड प्रॉम्प्ट खोलें और निम्न कमांड चलाएं:

```bash
git --version
```

यदि Git सही तरीके से स्थापित है, तो आपको इस प्रकार का आउटपुट दिखेगा:
```
git version 2.x.x
```

### GitHub खाता

सुनिश्चित करें कि आपका [GitHub खाता](https://github.com) है।

_यदि आप कमांड लाइन के साथ सहज नहीं हैं, तो [अन्य टूल्स का उपयोग करके ट्यूटोरियल](#अन्य-टूल्स-का-उपयोग-करके-ट्यूटोरियल) देखें।_

## रिपॉज़िटरी को फोर्क करना

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

इस पेज के ऊपरी दाएं कोने में स्थित 'Fork' बटन पर क्लिक करके इस रिपॉज़िटरी को फोर्क करें। यह आपके GitHub खाते में इस रिपॉज़िटरी की एक प्रति बना देगा जो केवल आपके लिए उपलब्ध होगी।

## रिपॉज़िटरी को क्लोन करना

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

अब इस रिपॉज़िटरी को अपने कंप्यूटर पर क्लोन (यानी डाउनलोड) करें। अपने GitHub अकाउंट पर जाएं, फोर्क की गई रिपॉज़िटरी खोलें, 'Code' बटन पर क्लिक करें, और फिर 'Copy to clipboard' आइकॉन पर क्लिक करें।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

अपने कंप्यूटर पर एक टर्मिनल/कमांड प्रॉम्प्ट खोलें और निम्न git कमांड चलाएं:

```bash
git clone "यूआरएल जिसे आपने अभी कॉपी किया"
```

जहाँ "यूआरएल जिसे आपने अभी कॉपी किया" (उद्धरण चिह्नों के बिना) इस रिपॉज़िटरी के लिए यूआरएल है। यूआरएल प्राप्त करने के लिए पिछले चरण देखें।

उदाहरण के लिए:
```bash
git clone https://github.com/यह-आप-हैं/first-contributions.git
```

यहाँ `यह-आप-हैं` आपके GitHub अकाउंट का नाम है। यहाँ आप अपने कंप्यूटर में GitHub से first-contributions रिपॉज़िटरी को कॉपी कर रहे हैं।

## एक शाखा (ब्राँच) बनाएँ

अपने कंप्यूटर पर बनाई गई रिपॉज़िटरी की डायरेक्टरी में जाएँ:

```bash
cd first-contributions
```

अब एक नई शाखा बनाएं `git switch` कमांड का उपयोग करके:

```bash
git switch -c add-आपका-नाम
```

वैकल्पिक रूप से, आप पुराने Git संस्करण के लिए इस कमांड का भी उपयोग कर सकते हैं:

```bash
git checkout -b add-आपका-नाम
```

उदाहरण के लिए:
```bash
git switch -c add-alonzo-church
```

## आवश्यक परिवर्तन करें और उन परिवर्तनों को कमिट करें

अब `Contributors.md` फ़ाइल को एक टेक्स्ट एडिटर में खोलें और इसमें अपना नाम जोड़ें। फ़ाइल की शुरुआत या अंत में इसे न जोड़ें। इसे बीच में कहीं भी रखें। अब फ़ाइल को सेव करें।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

यदि आप प्रोजेक्ट डायरेक्टरी में जाकर `git status` कमांड चलाएंगे, तो आपको अपने द्वारा किए गए परिवर्तन दिखेंगे।

उन परिवर्तनों को बनाई गई शाखा में जोड़ने के लिए `git add` कमांड का उपयोग करें:

```bash
git add Contributors.md
```

अब अपने किए गए बदलावों को `git commit` कमांड का उपयोग करके कमिट करें:

```bash
git commit -m "Add आपका-नाम to Contributors list"
```

`आपका-नाम` की जगह अपना नाम लिखें।

## अपने बदलावों को GitHub में पुश करें

`git push` का उपयोग कर अपने परिवर्तन को पुश करें:

```bash
git push origin add-आपका-नाम
```

`add-आपका-नाम` की जगह अपनी शाखा का नाम लिखें।

## अपने बदलावों को रिव्यू के लिए सबमिट करें

यदि आप अपने GitHub प्रोफ़ाइल पर अपनी रिपॉज़िटरी खोलते हैं, तो आपको `Compare & pull request` का बटन दिखाई देगा। उस पर क्लिक करें।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

अब अपनी pull request सबमिट करें।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

जल्द ही मैं आपके बदलावों को इस प्रोजेक्ट की मुख्य शाखा में सम्मिलित कर दूंगा। आपको एक ईमेल आएगी जब आपके बदलाव सम्मिलित होंगे।

## समस्या निवारण

### सामान्य Git त्रुटियां और उनके समाधान

#### 1. "git: command not found"
**समस्या**: Git स्थापित नहीं है।  
**समाधान**: 
```bash
# Ubuntu/Debian पर
sudo apt-get install git

# macOS पर (Homebrew के साथ)
brew install git

# Windows पर git-scm.com से डाउनलोड करें
```

#### 2. "Permission denied (publickey)"
**समस्या**: SSH key सेटअप नहीं है।  
**समाधान**: HTTPS URL का उपयोग करें या SSH key सेटअप करें।
```bash
# HTTPS का उपयोग करें
git clone https://github.com/username/first-contributions.git
```

#### 3. "fatal: not a git repository"
**समस्या**: आप सही डायरेक्टरी में नहीं हैं।  
**समाधान**: 
```bash
cd first-contributions
```

#### 4. "error: pathspec 'branch-name' did not match any file(s)"
**समस्या**: गलत ब्राँच नाम।  
**समाधान**: मौजूदा branches देखें:
```bash
git branch -a
```

#### 5. "Updates were rejected because the remote contains work"
**समस्या**: Remote repository में नए changes हैं।  
**समाधान**: 
```bash
git pull origin main
git push origin your-branch-name
```

#### 6. "Your branch is ahead of 'origin/main' by X commits"
**समाधान**: 
```bash
git push origin your-branch-name
```

### मदद प्राप्त करना

यदि आपको अभी भी समस्या आ रही है:

1. **GitHub Issues**: परियोजना के Issues section में प्रश्न पूछें
2. **Slack Community**: [हमारी Slack टीम](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w) में शामिल हों
3. **Documentation**: [Git Documentation](https://git-scm.com/doc) पढ़ें

## यहाँ से कहाँ जाएं?

🎉 बधाई! आपने सफलतापूर्वक _fork → clone → edit → PR_ वर्कफ़्लो पूरा कर लिया है, जिसका आप अक्सर एक योगदानकर्ता के रूप में सामना करेंगे!

### अपनी सफलता का जश्न मनाएं
अपने पहले योगदान की खुशी में जश्न मनाएं और इसे [वेब एप्प](https://firstcontributions.github.io/#social-share) के जरिए अपने मित्रों के साथ शेयर करें।

### समुदाय से जुड़ें
आप हमारी [Slack टीम](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w) को ज्वाइन कर सकते हैं यदि आपको कुछ मदद चाहिए या आपके कोई प्रश्न हों।

### अगले कदम
अब आप अन्य प्रोजेक्ट्स पर योगदान करने के लिए तैयार हैं! हमने आपके लिए [शुरुआती अनुकूल प्रोजेक्ट्स की सूची](https://firstcontributions.github.io/#project-list) तैयार की है जहाँ सरल इश्यूज़ हैं।

## अन्य टूल्स का उपयोग करके ट्यूटोरियल

यदि आप कमांड लाइन के बजाय ग्राफिकल टूल्स का उपयोग करना पसंद करते हैं, तो निम्नलिखित ट्यूटोरियल देखें:

### डेस्कटॉप एप्लिकेशन्स

| टूल | ट्यूटोरियल लिंक | विवरण |
|------|-----------------|--------|
| <img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="50"> **GitHub Desktop** | [ट्यूटोरियल](../gui-tool-tutorials/github-desktop-tutorial.md) | GitHub का आधिकारिक डेस्कटॉप एप्प |
| <img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="50"> **GitKraken** | [ट्यूटोरियल](../gui-tool-tutorials/gitkraken-tutorial.md) | शक्तिशाली Git GUI क्लाइंट |
| <img alt="Sourcetree" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width="50"> **Sourcetree** | [ट्यूटोरियल](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | Atlassian का मुफ़्त Git GUI |

### कोड एडिटर्स और IDEs

| टूल | ट्यूटोरियल लिंक | विवरण |
|------|-----------------|--------|
| <img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="50"> **Visual Studio Code** | [ट्यूटोरियल](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | लोकप्रिय कोड एडिटर |
| <img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="50"> **Visual Studio 2017** | [ट्यूटोरियल](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | Microsoft का IDE |

### किसी भी टूल को चुनने से पहले विचार करें:
- **शुरुआती लोगों के लिए**: GitHub Desktop सबसे आसान है
- **उन्नत सुविधाओं के लिए**: GitKraken या Sourcetree
- **कोडिंग के साथ-साथ**: VS Code या Visual Studio

---

*यह प्रोजेक्ट [First Contributions](https://github.com/firstcontributions/first-contributions) का हिंदी अनुवाद है।*