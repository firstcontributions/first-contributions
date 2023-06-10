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
- Github  खाता

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

**महत्वपूर्ण: यह आपको संकेत देगा कि यदि आप इसे भी क्लोन करना चाहते हैं, तो "yes"  चुनें**

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