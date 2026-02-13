# first

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# पहला योगदान

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

यह हमारे लिए एक गाइड है, टर्मिनल नर्ड, जो टर्मिनल में सब कुछ करना चाहते हैं, और इसके लिए धन्यवाद [Github-CLI](https://cli.github.com/) उनके कारण इसे प्राप्त कर सकते हैं, आपका पहला योगदान याद रखना मजेदार, पुरस्कृत और आगे बढ़ने के लिए प्रेरक होना चाहिए!

यह मार्गदर्शिका थोड़ी अधिक चुनौतीपूर्ण है क्योंकि हम किसी भी चित्रात्मक इंटरफ़ेस का उपयोग नहीं कर रहे हैं, लेकिन यह अभी भी सचमुच में मज़ेदार है और आप निश्चित रूप से इसका अनुसरण कर सकते हैं!

पहली आवश्यकता है:

- Git installed ([Git](https://git-scm.com/downloads) कैसे स्थापित करें)
- Github खाता

अब हमें आधिकारिक दस्तावेज़ीकरण का पालन करके अपने सिस्टम में `github-cli` टूल इंस्टॉल करना होगा

उसके बाद, हमें CLI में लॉगिन करने की आवश्यकता है, इसलिए यह आदेश दर्ज करें:

```bash
gh auth login
```

निर्देशों का पालन करें और हम तैयार हैं!

# Fork this repository

इस आदेश को चलाना उतना ही आसान है:

```bash
gh repo fork firstcontributions/first-contributions
```

**महत्वपूर्ण: यह आपको संकेत देगा कि यदि आप इसे भी क्लोन करना चाहते हैं, तो "yes" चुनें**

# अपनी शाखा बनाएँ

हम इस कदम को `git` के साथ करेंगे, इसलिए इस आदेश को अपने नाम के साथ नाम बदलकर दर्ज करें, उदाहरण के लिए:

```bash
git switch -c add-जॉन-डूई
```

# आवश्यक बदलना करें और उन बदलना को करें `commit`

अब आप टेक्स्ट एडिटर में `Contributors.md` फ़ाइल खोल सकते हैं और उसमें अपना नाम जोड़ सकते हैं। शुरुआत और अंत के बीच अपना नाम कहीं भी रखें, फिर फाइल को सेव करें।

प्रोजेक्ट डायरेक्टरी में `git status` निष्पादित करें और आप परिवर्तन देखेंगे।
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

उन परिवर्तनों को उस शाखा में जोड़ें जिसे आपने अभी `git add` कमांड का उपयोग करके बनाया है:
`git add Contributors.md`

अब `git commit` कमांड का उपयोग करके उन परिवर्तनों को करें: `git commit -m "Add your-name to Contributors list` अपने नाम के साथ `your-name` बदलें।

# Github में परिवर्तन पुश करें

`git push` कमांड का उपयोग करके अपने परिवर्तन पुश करें:

    git push origin -u your-branch-name

`your-branch-name` आपके द्वारा पहले बनाई गई शाखा के नाम से बदलकर।

<details><summary> <strong>यदि आपको पुश करते समय कोई त्रुटि मिलती है, तो यहां क्लिक करें:</strong></summary></details>

- ### प्रमाणीकरण त्रुटि
       रिमोट: 13 अगस्त, 2021 को पासवर्ड प्रमाणीकरण के लिए समर्थन हटा दिया गया था। कृपया इसके बजाय एक व्यक्तिगत एक्सेस टोकन का उपयोग करें। दूरस्थ: अधिक जानकारी के लिए कृपया https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ देखें। घातक: 'https://github.com/' के लिए प्रमाणीकरण विफल /प्रथम-योगदान.गिट/'
  अपने खाते में SSH कुंजी बनाने और कॉन्फ़िगर करने के लिए [GitHub के ट्यूटोरियल](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) पर जाएं।

# समीक्षा के लिए अपने परिवर्तन सबमिट करें

अब इस आदेश को हमारे रेपो की निर्देशिका में चलाने से हम समीक्षा के लिए एक पुल अनुरोध बना सकेंगे:

```bash
gh pr create --repo firstcontributions/first-contributions
```

इसके बाद पुल रिक्वेस्ट सबमिट करें।

अपने उल्लेखित पुल अनुरोध को क्रियाशील देखने के लिए आप `gh status` कमांड का उपयोग कर सकते हैं।

## यहाँ से कहाँ जाएं?

बधाई हो! आपने अभी-अभी मानक _कांटा पूरा किया है -> क्लोन -> संपादित करें -> पुल अनुरोध_ वर्कफ़्लो जिसे आप अक्सर एक योगदानकर्ता के रूप में सामना करेंगे!

अपने योगदान का जश्न मनाएं और इसे [वेब ऐप](https://firstcontributions.github.io/#social-share) पर जाकर अपने दोस्तों और फॉलोअर्स के साथ साझा करें।

अगर आपको कोई मदद चाहिए या कोई सवाल है तो आप हमारी सुस्त टीम में शामिल हो सकते हैं। [सुस्त टीम में शामिल हों](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA) ।

आइए अब आपको अन्य परियोजनाओं में योगदान के साथ आरंभ करते हैं। हमने उन आसान मुद्दों के साथ परियोजनाओं की एक सूची तैयार की है जिन पर आप शुरुआत कर सकते हैं। [वेब ऐप में परियोजनाओं की सूची](https://firstcontributions.github.io/#project-list) देखें।

### [अतिरिक्त सामग्री](additional-material/git_workflow_scenarios/additional-material.md)

## ट्यूटोरियल अन्य उपकरणों का उपयोग करना

[मुख्य पृष्ठ पर वापस](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
