[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# प्रथम योगदान

पहली बार कुछू  करे बर कठिन होथे| ख़ास तौर पर जब आपमन मिलकर काम करथव तब  गलतियां करना बने बात नहीं आय | मगर आपस म मिलना अउ एक जुट होकर काम करे ल ही त ओपन सोर्स कइथे| हमन आप मन के पहला ओपन सोर्स कॉन्ट्रिब्यूशन/योगदान आसान बनाए बर आपमन  की मदद करबो |

आर्टिकल्स पढ़े अउ ऑनलाइन ट्यूटोरियल देखके  मदद मिल सकत हे  मगर बिना कुछू गलत करे अउ खुद वो काम करे ले बने अउ का हो सकत हे ? यह प्रोजेक्ट आपमन के पहले कॉन्ट्रिब्यूशन बर दिशा निर्देशन करे बर बने मदद करहि  | याद रखौ  - जतका तनाव मुक्त होकर आप मन सिखहु ततका आपमन बने सीख पाबौ | अगर आप मन अपन पहली कॉन्ट्रिब्यूशन करना चाहत हो त आगे दिए तरीका ल बने  फॉलो करौ |

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

आपमन  के कंप्यूटर म  Git नहीं हे  त, [एला स्थापित करौ](https://help.github.com/articles/set-up-git/)

## रिपॉज़िटरी ल फॉर्क करे बर

कांटा (फॉर्क) बटन म क्लिक करके ए रिपॉज़िटरी ल फॉर्क कर सकत हो| ए ह आपमन के  GitHub खाते म  इही रिपॉज़िटरी के एकठन प्रति (कॉपी) बना दिहि।

## रिपोजिटरी क्लोन

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

अब आपमन  ए रेपो ल अपन कंप्यूटर म क्लोन (डाउनलोड) करव| अपन GitHub खाते म जाकर क्लोन बटन म क्लिक करव अउ फिर कॉपी टू क्लिपबोर्ड आइकॉन म क्लिक करव |

अपन कंप्यूटर म एक ठन टर्मिनल/कमांड प्रांप्ट खोलव अउ निम्न git आदेश चलावव:

```
git clone "यूआरएल जैला आपमन कॉपी करे हावव "
```

जेती "यूआरएल जैला आपमन कॉपी करे हावव" (उद्धरण चिह्नों के बिना) ए भंडार बर यूआरएल हे । यूआरएल प्राप्त करे बर पिछला चरण देखव ।

उदाहरण बर:

```
git clone https://github.com/यह-तै-हावस/first-contributions.git
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

यह-तै-हावस आपमन के GitHub अकाउंट के नाम हावै। एती आपमन अपन कंप्यूटर न GitHub ले फर्स्ट-कंट्रिब्यूशंज़ रेपो ल कॉपी करथव अउ ओखर एक लोकल/स्थानीय कॉपी बनावथस|

## एक ब्राँच बनाए बर

अपन कंप्यूटर म बनाये गए रिपॉजिटरी के कॉपी के फोल्डर/डायरेक्टरी म जावव (अगर अब तक नहीं करे हावस त निम्न आदेश चलावव)

```
cd first-contributions
```

अब एक ठी नवा शाखा बनवाव `git checkout` कमांड के उपयोग करके |
नवा शाखा बनाए  बर -b ऑप्शन के उपयोग होथे।

```
git checkout -b <अपन-शाखा-के-नाम-जोड़ें>
```

उदाहरण बर:

```
git checkout -b add-alonzo-church
```

( शाखा के नाम म `add` जोड़ने के आवश्यकता नहीं हावए, लेकिन एमा जोड़ना चल जाहि काबर की ए शाखा के उद्देश्य एक सूची म अपन नाम ल जोड़े बर हे। )

## आवश्यक परिवर्तन करे बर अउ उन परिवर्तनों ल कमिट करे बर-

अब `Contributors.md` फ़ाइल ल एक टेक्स्ट एडिटर म खोलकर एमा अपन नाम लिखव। फ़ाइल के शुरुआत या अंत म एला झन जोड़बे। एला बीच म कही तिरिया देहु आपमन |

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


आपमन अगर `git status` निर्देश चलाहु , त आपमन ल किये गए परिवर्तन दिखहि।

उन परिवर्तनों ल बनाए गए शाखा म जोड़े बर `git add` कमान्ड के उपयोग करव |

```
git add Contributors.md
```

अब अपन करे गए बदलाव ल कमिट करे बर  `git commit` आदेश के उपयोग करव |

```
git commit -m "Add <अपन-नाम> to Contributors list"
```

<अपन-नाम> के जगह अपन नाम डालव|

## अपन करे बदलाव ल Github म पुश करव|

`git push` के उपयोग कर अपन परिवर्तन ल पुश करव|

```
git push origin <अपन-शाखा-के-नाम-जोड़व>
```

`<अपन-शाखा-के-नाम-जोड़व>` के जगह अपन शाखा के नाम डालव|

## अपन बदलाव ल रिव्यु करे बर सबमिट करव|

आपमन अपन github प्रोफाइल म अपन रेपो म जाबा अउ Compare & pull request ल दबवाव|
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

आप मन के pull request सबमिट करव|

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
मैं आपमन के बदलाव ल ए प्रोजेक्ट के मास्टर शाखा म तुरते मर्ज कर दुहु| आप मन ल एक ठन मेल आ जहि जब बदलाव मर्ज होही|

## इहा ले कती जाबो?

बधाई हो मितान! आपमन ने_fork -> clone -> edit -> PR_ वर्कफ़्लो ल पूरा कर डरे हव!

अपन पहली योगदान के ख़ुशी म अपन संगी मन करा शेयर करव [वेब एप्प](https://firstcontributions.github.io/#social-share) पे जाके |

आपमन हमर स्लैक टीम ल ज्वाइन कर सकत हव अगर आपमन ल कोनो सहायता के जरुरत होही त | [म ज्वाइन करव](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

अब आपमन अउ प्रोजेक्ट्स म कंट्रीब्यूट करे बर शुरू कर सकत हव | हमन एक लिस्ट बनाए हन जेन म अड़बड़ सरल मुद्दे हवएं| [प्रोजेक्ट्स के लिस्ट](https://firstcontributions.github.io/#project-list)

## अन्य टूल के उपयोग करके ट्यूटोरियल

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
