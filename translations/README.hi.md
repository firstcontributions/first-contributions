[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# प्रथम योगदान

पहली बार कुछ करना कठिन होता है| ख़ास तौर पर जब आप मिलकर काम कर रहे हों, तब गलतियां करना अच्छी बात नहीं है | मगर आपस में मिलकर एक जुट होकर काम करना ही तोह 'ओपन सोर्स' केहलाता है | हम आपका ये पहला 'ओपन सोर्स कॉन्ट्रिब्यूशन'/योगदान आसान बनाने में आपकी मदद करेंगे |

लेखों को पढ़ना और ऑनलाइन ट्यूटोरियलज़ देखना मदद कर सकते हैं मगर बिना किसी गलती के, खुद वो काम करने से अच्छा क्या कुछ हो सकता है? यह परियोजना आपको आपके पहले 'कॉन्ट्रिब्यूशन' के लिए मार्गदर्शन करवाएगा| याद रखिऐ - जितने तनाव मुक्त होकर आप सीखेंगे, उतना ही बेहतर सीख पाएंगे | अगर आप अपनी पहली योगदान  करना चाहते हैं, तो निम्नलिखित निर्देशों का अनुसरण कीजिये|

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

अगर आपके कंप्यूटर पर Git नहीं है तो, [इसे स्थापित करें](https://help.github.com/articles/set-up-git/)

## रिपॉज़िटरी को फॉर्क करना

कांटा (फॉर्क) बटन दबाकर, आप इस रिपॉज़िटरी को फॉर्क कर सकते हैं| यह आपके GitHub खाते में इस रिपॉज़िटरी की एक प्रति (कॉपी) बना देगा।

## रिपोजिटरी क्लोन

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

अब आप यह रेपो अपने कंप्यूटर में क्लोन(अर्थात डाउनलोड) करें | अपने गिटहब खाते पर जाएं, क्लोन बटन दबाकर 'कॉपी टू क्लिपबोर्ड' आइकॉन दबाएँ  |

अपने कंप्यूटर पर एक टर्मिनल/कमांड प्रांप्ट खोलें और निम्न git आदेश चलाएँ:

```
git clone "यूआरएल जिसे आपने अभी कॉपी किया"
```

जहाँ "यूआरएल जिसे आपने अभी कॉपी किया" (उद्धरण चिह्नों के बिना) इस भंडार का यूआरएल है । (इस परियोजना का आपका फॉर्क) यूआरएल प्राप्त करने के लिए पिछले चरण देखें ।

उदाहरण के लिए:

```
git clone https://github.com/यह-तुम-हो/first-contributions.git
```

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

`यह-तुम-हो` आपके GitHub खाते का नाम है। यहाँ आप अपने कंप्यूटर में GitHub से फर्स्ट-कंट्रिब्यूशंज़ रेपो को कॉपी कर रहे हैं अथवा उसकी एक लोकल/स्थानीय प्रति बना रहे हैं |

## एक ब्राँच बनाएं

अपने कंप्यूटर पर बनाई गई रिपॉजिटरी की कॉपी के फोल्डर/डायरेक्टरी में जाएँ (अगर अभी तक नहीं की है तो निम्न आदेश चलाएँ)

```
cd first-contributions
```

अब `git checkout` कमांड का उपयोग करके एक नई शाखा बनाएं |
नई शाखा बनाने के लिए -b ऑप्शन का उपयोग होता है ।  

```
git checkout -b <अपनी-शाखा-का-नाम-जोड़ें>
```

उदाहरण के लिए:

```
git checkout -b add-alonzo-church
```

( शाखा के नाम में `add` जोड़ने की आवश्यकता नहीं है, लेकिन इसमें शामिल होना उचित बात है क्योंकि इस शाखा का उद्देश्य एक सूची में अपना नाम जोड़ना है। )

## आवश्यक परिवर्तन करें और उन परिवर्तनों को कमिट करें-

अब `Contributors.md` फ़ाइल को एक टेक्स्ट एडिटर में खोलकर इसमें अपना नाम लिखें। फ़ाइल की शुरुआत या अंत में इसे न जोड़ें। इसे बीच में कहीं भी रखें | 

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />


अगर आप `git status` निर्देश चलाएंगे, तो आप किये हुए परिवर्तन देखेंगे।

उन परिवर्तनों को बनाई गई शाखा में जोड़ने के लिए `git add` का उपयोग करें |

```
git add Contributors.md
```

अब अपने किये गए बदलावों को `git commit` आदेश का उपयोग करके कमिट करें  |

```
git commit -m "Add <आपका-नाम> to Contributors list"
```

<आपका-नाम> की जगह अपना नाम डालें|

## अपने बदलावों को Github में पुश करें|

`git push` का उपयोग कर अपने परिवर्तन को पुश करें |

```
git push origin <अपनी-शाखा-का-नाम-जोड़ें>
```

`<अपनी-शाखा-का-नाम-जोड़ें>` की जगह अपनी शाखा का नाम डालें |

## अपने बदलावों को रिव्यु के लिए सबमिट करें |

अगर आप अपने GitHub प्रोफाइल पर अपनी रेपो में जायेंगे तो आपको 'Compare & pull request' का ऑप्शन दिखेगा| उसे दबाएं |
<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

अब अपनी pull request सबमिट करें |

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />
जल्द ही मैं आपके बदलावों को इस प्रोजेक्ट की 'मास्टर' शाखा में मर्ज कर दूंगा| जब आपके बदलाव मर्ज होंगे, आपको मेल द्वारा सूचित किया जाएगा | 

## यहाँ से कहाँ जाएं ?

बधाई! आपने अभी पूरा कर लिया है _fork -> clone -> edit -> PR_ वर्कफ़्लो जो आप अक्सर योगदानकर्ता के रूप में सामना करेंगे!

अपने पहले योगदान की खुशी में जश्न मनाएं और अपने दोस्तों के साथ शेयर करें [वेब एप्प](https://roshanjossey.github.io/first-contributions/#social-share) पे जाके | 

अगर आपको कोई मदद चाहिए या आपके कोई परेशानी हों, तो आप हमारी स्लैक टीम से जुड़ सकते हैं | [स्लैक पे ज्वाइन करें](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

अब आप अनेक योजनाओं में अपना योगदान देना शुरू कर सकते हैं | हमने आपके लिए एक लिस्ट बनायीं है, जो बहुत आसान विषयों पर हैं | [प्रोजेक्ट्स कि लिस्ट](https://roshanjossey.github.io/first-contributions/#project-list)

## अन्य टूल का उपयोग करके ट्यूटोरियल

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## आत्म पदोन्नति

अगर आपको यह परियोजना पसंद आया, तो इसे [GitHub](https://github.com/Roshanjossey/first-contributions) पर स्टार करें | 
यदि आप विशेष रूप से धर्मार्थ महसूस कर रहे हैं, तो follow [Roshan](https://roshanjossey.github.io/) twitter और
[GitHub](https://github.com/roshanjossey) पर |

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
