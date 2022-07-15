[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# प्रथम योगदान

पहली बार कुछ करना कठिन होता है | ख़ास तौर पर जब आप मिलकर काम कर रहे हों तब गलतियां करना अच्छी बात नहीं है | मगर आपस में मिलना और एक जुट होकर काम करना ही तो है ओपन सोर्स | हम आपका ये पहला ओपन सोर्स कॉन्ट्रिब्यूशन/योगदान आसान बनाने में आपकी मदद करेंगे |

आर्टिकल्स पढ़ना और ऑनलाइन ट्यूटोरियलज़ देखना मदद कर सकते हैं मगर बिना कुछ गलत करे खुद वो काम करने से अच्छा क्या हो सकता है? यह प्रोजेक्ट आपको आपके पहले कॉन्ट्रिब्यूशन के लिए दिशा निर्देशन में मदद करेगा | याद रखिये - जितने तनाव मुक्त होकर आप सीखेंगे उतना ही बेहतर सीख पाएंगे | अगर आप अपनी पहली कॉन्ट्रिब्यूशन करना चाहते हैं तो आगे दिए गए निर्देशों का पालन करें |

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

अगर आपके कंप्यूटर पर Git नहीं है तो, [इसे स्थापित करें](https://help.github.com/articles/set-up-git/) |

_यदि आप कमांड लाइन के साथ सहज नहीं हैं, [तो यहाँ ग्राफिकल इंटरफेस (GUI) टूल्स का उपयोग करने वाले ट्यूटोरियल हैं](#अन्य-टूल-का-उपयोग-करके-ट्यूटोरियल) |_

## रिपॉज़िटरी को फॉर्क करना

काँटा (फॉर्क) बटन पर क्लिक करके इस रिपॉज़िटरी को फॉर्क कर सकते हैं| यह आपके GitHub खाते (अकाउंट) में इस रिपॉज़िटरी की एक प्रति (कॉपी) बना देगा जो केवल आपके लिए उपलब्ध होगी।

## रिपॉज़िटरी को क्लोन करना

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

अब आप यह रिपॉज़िटरी अपने कंप्यूटर में क्लोन (अर्थात् डाउनलोड) करें | अपने GitHub अकाउंट पर जाएँ, Code/क्लोन बटन पर क्लिक करें और फिर कॉपी टू क्लिपबोर्ड आइकॉन पर क्लिक करें |

अपने कंप्यूटर पर एक टर्मिनल/कमांड प्रांप्ट खोलें और निम्न git आदेश (कमांड) चलाएँ:

```
git clone "यूआरएल जिसे आपने अभी कॉपी किया"
```

जहाँ "यूआरएल जिसे आपने अभी कॉपी किया" (उद्धरण चिह्नों के बिना) इस रिपॉज़िटरी के लिए यूआरएल है (इस परियोजना का आपका फॉर्क) | यूआरएल प्राप्त करने के लिए पिछले चरण देखें ।

उदाहरण के लिए:

```
git clone https://github.com/यह-तुम-हो/first-contributions.git
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

`यह-तुम-हो` आपके GitHub अकाउंट का नाम है। यहाँ आप अपने कंप्यूटर में GitHub से first-contributions रिपॉज़िटरी को कॉपी कर रहे हैं अथवा उसकी एक लोकल/स्थानीय कॉपी बना रहे हैं |

## एक शाखा (ब्राँच) बनाएँ 

अपने कंप्यूटर पर बनाई गई रिपॉज़िटरी की कॉपी के फोल्डर/डायरेक्टरी में जाएँ (अगर अभी तक नहीं की है तो निम्न आदेश चलाएँ)

```
cd first-contributions
```

अब एक नई शाखा बनाएँ `git checkout` कमांड का उपयोग करके |
नई शाखा बनाने के लिए -b ऑप्शन का उपयोग होता है ।  

```
git checkout -b <अपनी-शाखा-का-नाम-जोड़ें>
```

उदाहरण के लिए:

```
git checkout -b add-alonzo-church
```

( शाखा के नाम में `add` जोड़ने की आवश्यकता नहीं है, लेकिन इसमें शामिल होना जरूरी है क्योंकि इस शाखा का उद्देश्य एक सूची में अपना नाम जोड़ना है। )

## आवश्यक परिवर्तन करें और उन परिवर्तनों को कमिट करें-

अब `Contributors.md` फ़ाइल को एक टेक्स्ट एडिटर में खोलकर इसमें अपना नाम लिखें। फ़ाइल की शुरुआत या अंत में इसे न जोड़ें। इसे बीच में कहीं भी रखें | 

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


आप अगर `git status` कमांड चलाएंगे , तो आप किये गए परिवर्तन देखेंगे।

उन परिवर्तनों को बनाई गई शाखा में जोड़ने के लिए `git add` कमांड का उपयोग करें |

```
git add Contributors.md
```

अब अपने किये गए बदलावों को कमिट करें `git commit` कमांड का उपयोग करके |

```
git commit -m "Add <आपका-नाम> to Contributors list"
```

<आपका-नाम> की जगह अपना नाम लिखें |

## अपने बदलावों को Github में धकेले (पुश करें) |

`git push` का उपयोग कर अपने परिवर्तन को धकेले  |

```
git push origin <अपनी-शाखा-का-नाम-जोड़ें>
```

`<अपनी-शाखा-का-नाम-जोड़ें>` की जगह अपनी शाखा का नाम लिखें |

## अपने बदलावों को रिव्यु के लिए सबमिट करें |

अगर आप अपने Github प्रोफाइल पर अपनी रिपॉज़िटरी में जायेंगे तो आपको Compare & pull request का ऑप्शन दिखेगा| उसे दबाएं |
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

अब अपनी pull request सबमिट करें |

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
जल्द ही मैं आपके बदलावों को इस प्रोजेक्ट की मास्टर शाखा में मर्ज कर दूंगा| आपको एक मेल आएगी जब आपके बदलाव मर्ज होंगे |

## यहाँ से कहाँ जाएं ?

बधाई! आपने अभी पूरा कर लिया है _fork -> clone -> edit -> PR_ वर्कफ़्लो जो आप अक्सर योगदानकर्ता के रूप में सामना करेंगे!

अपने पहले योगदान की खुशी में जश्न मनाएं और अपने दोस्तों के साथ शेयर करें [वेब एप्प](https://roshanjossey.github.io/first-contributions/#social-share) पे जाके | 

आप हमारी स्लैक टीम को ज्वाइन कर सकते हैं अगर आपको कोई मदद चाहिए या आपको कोई परेशानी हों | [स्लैक पे ज्वाइन करें](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

अब आप और प्रोजेक्ट्स में कंट्रीब्यूट करना शुरू कर सकते हैं | हमने आपके लिए एक लिस्ट बनायीं है जो कि बहुत आसान मुद्दे हैं | [प्रोजेक्ट्स कि लिस्ट](https://roshanjossey.github.io/first-contributions/#project-list)

## अन्य टूल का उपयोग करके ट्यूटोरियल

|<a href="/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://camo.githubusercontent.com/3793fd7afab1e383a841a5e39c681c802cdcbbb1ffa01571a06b1a167e086512/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f6775692d746f6f6c2d7475746f7269616c732f6769746b72616b656e2d7475746f7269616c2f676b2d69636f6e2e706e67" width="100"></a>|<a href="/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)|[Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)|[GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)|[Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)|


