[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# प्रथम योगदान

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Git Bash Edition |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |

यह कठिन है। जब आप पहली बार कुछ करते हैं तो यह हमेशा कठिन होता है। खासकर जब आप सहयोग कर रहे हों, तो गलतियाँ करना कोई सहज बात नहीं है। लेकिन ओपन सोर्स का मतलब सहयोग और साथ मिलकर काम करना है। हम नए ओपन-सोर्स योगदानकर्ताओं के सीखने और पहली बार योगदान करने के तरीके को सरल बनाना चाहते थे।

लेख पढ़ना और ट्यूटोरियल देखना मददगार हो सकता है, लेकिन बिना कुछ गड़बड़ किए वास्तव में काम करने से बेहतर क्या हो सकता है। इस परियोजना का उद्देश्य मार्गदर्शन प्रदान करना और नौसिखियों द्वारा अपना पहला योगदान करने के तरीके को सरल बनाना है। याद रखें कि आप जितने अधिक सहज होंगे, आप उतना ही बेहतर सीखेंगे। यदि आप अपना पहला योगदान करना चाहते हैं तो बस नीचे दिए गए सरल चरणों का पालन करें। हम आपसे वादा करते हैं, यह मजेदार होगा।

यदि आपके पास विंडोज़ मशीन पर Git Bash नहीं है, [तो इसे इंस्टॉल करें](https://git-scm.com/download/win)।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## इस रिपोजिटरी को फोर्क करें

इस पेज के ऊपर दाईं ओर दिए गए फोर्क बटन पर क्लिक करके इस रिपो को फोर्क करें।
इससे आपके खाते में इस रिपो की एक कॉपी बन जाएगी।

## रिपोजिटरी को क्लोन करें

अब इस रेपो को अपनी मशीन पर क्लोन करें।

महत्वपूर्ण: मूल रेपो को क्लोन न करें। अपने फोर्क पर जाएं और इसे क्लोन करें।

रेपो को क्लोन करने के लिए, "कोड" पर क्लिक करें और फिर नीचे स्ट्रिंग को कॉपी करें।

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

आपने अभी जो git bash एप्लीकेशन डाउनलोड किया है उसे खोलें। अगर यह विंडोज़ मशीन पर है तो यह नीचे दी गई छवि की तरह दिखाई देगा।

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />

इस कमांड का उपयोग करके उस फ़ोल्डर पर जाएँ जहाँ आप इस प्रोजेक्ट को सहेजना चाहते हैं

`cd <folder>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />

इस कमांड का उपयोग करके रिपॉजिटरी को क्लोन करने के लिए ऊपर दिए गए चरण में आपके द्वारा कॉपी की गई स्ट्रिंग का उपयोग करें

`git clone <repo-url>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

उस निर्देशिका पर जाएं जहां रेपो है और अपने परिवर्तन करने के लिए इसे वीएस कोड पर खोलें।

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## एक शाखा बनाएं

अब इस सरल कमांड का उपयोग करके एक शाखा बनाएँ। यह कमांड न केवल आपके लिए एक शाखा बनाता है बल्कि आपको उस शाखा पर स्विच करने की सुविधा भी देता है।

```
git checkout -b <branch-name>
```

अपनी शाखा का नाम `<add-your-name>` रखें। उदाहरण के लिए, "add-james-smith"

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="create a branch" />

## आवश्यक परिवर्तन करें और उन परिवर्तनों को लागू करें

अब `Contributors.md` फ़ाइल को टेक्स्ट एडिटर में खोलें, पेज के नीचे स्क्रॉल करें और उसमें अपना नाम जोड़ें, फिर फ़ाइल को सेव करें।

उदाहरण: यदि आपका नाम James Smith है, तो यह इस तरह दिखना चाहिए।

[James Smith](https://github.com/jamessmith)

आप केवल यह आदेश चलाकर देख सकते हैं कि Contributors.md में परिवर्तन हुए हैं

`git status`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="check the status" />

अब उन परिवर्तनों को प्रतिबद्ध करें:

सबसे पहले आपके द्वारा किए गए परिवर्तन को स्टेजिंग क्षेत्र में जोड़ें

`git add file-name`

फिर इस कमांड को गाकर एक कमिट संदेश लिखें

`git commit -m "Add your-name to Contributors list"`

`<your-name>` को अपने नाम से बदलें।

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit changes" />

यह देखने के लिए कि क्या आपका कमिट हो गया है, आप एक सरल `git log --oneline` कमांड चला सकते हैं।

## परिवर्तनों को github पर भेजें

एक बार जब आप उपरोक्त चरणों को पूरा कर लें तो आप इस कमांड का उपयोग करके अपने परिवर्तनों को पुश कर सकते हैं

`git push origin <branch-name>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-push.png" alt="push changes" />

## अपने परिवर्तन समीक्षा के लिए सबमिट करें

यदि आप गिटहब पर अपने रिपॉजिटरी में जाते हैं, तो आपको `Compare & pull request` बटन दिखाई देगा। उस बटन पर क्लिक करें।

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

अब पुल अनुरोध सबमिट करें.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

जल्द ही मैं आपके सभी बदलावों को इस प्रोजेक्ट की मास्टर ब्रांच में मर्ज कर दूँगा। बदलावों के मर्ज हो जाने पर आपको एक सूचना ईमेल मिलेगी।

## यहाँ से कहाँ जाएं?

बधाई हो! आपने अभी-अभी मानक _fork -> clone -> edit -> PR_ वर्कफ़्लो पूरा किया है, जिसका सामना आप एक योगदानकर्ता के रूप में अक्सर करेंगे!

अपने योगदान का जश्न मनाएँ और [वेब ऐप](https://firstcontributions.github.io#social-share) पर जाकर इसे अपने दोस्तों और फ़ॉलोअर्स के साथ शेयर करें।

यदि आपको किसी सहायता की आवश्यकता हो या कोई प्रश्न हो तो आप हमारी स्लैक टीम में शामिल हो सकते हैं। [स्लैक टीम में शामिल हों](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)।

### [अतिरिक्त सामग्री](../additional-material/git_workflow_scenarios/additional-material.md)

## अन्य टूल का उपयोग करके ट्यूटोरियल

[मुख्य पृष्ठ पर वापस जाएँ](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)