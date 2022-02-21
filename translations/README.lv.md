[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# पहिले योगदान
प्रथमच काहीतरी करणे नेहमीच कठीण असते. याव्यतिरिक्त, चुका करणे, विशेषतः इतरांशी संवाद साधताना, आनंददायी नाही. आम्ही नवीन मुक्त स्रोत सह-लेखक शिकण्याचा आणि प्रथमच त्यांचे इनपुट जोडण्याचा मार्ग सुलभ करू इच्छितो.

लेख वाचणे आणि ट्यूटोरियल पाहणे मदत करू शकते, परंतु वास्तविक शिक्षण वातावरणापेक्षा चांगले काहीही नाही. या प्रकल्पाचे उद्दिष्ट मार्गदर्शन प्रदान करणे आणि नवशिक्यांनी त्यांचे प्रथम योगदान जोडण्याचे मार्ग सुलभ करणे हे आहे. तुम्हाला सहभागी व्हायचे असल्यास, खालील चरणांचे अनुसरण करा.

#### *जर तुम्हाला कमांड लाइनसह सोयीस्कर वाटत नसेल, तर 


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

तुमच्या संगणकावर गिट नसल्यास, [ते स्थापित करा] (https://help.github.com/articles/set-up-git/).

## भांडार शाखा तयार करते

या पृष्ठाच्या शीर्षस्थानी * फोर्क * बटणावर क्लिक करून तुमची स्वतःची भांडार शाखा तयार करा.
हे तुमच्या प्रोफाइलमध्ये या भांडाराची एक प्रत तयार करेल.

## रेपॉजिटरी क्लोन करा

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

आता तुमच्या संगणकावरील कॉपी केलेल्या भांडाराचे क्लोन करा. तुमच्या GitHub प्रोफाइलवर जा, कॉपी केलेले भांडार उघडा, * क्लोन * बटण दाबा आणि नंतर * क्लिपबोर्डवर कॉपी करा * चिन्हावर क्लिक करा.

टर्मिनल उघडा आणि ही git कमांड चालवा:

``
git क्लोन "फक्त कॉपी केलेली लिंक"
``
जिथे "फक्त कॉपी केलेली लिंक" (कोट्सशिवाय) ही या भांडाराची url आहे (तुमची प्रकल्प शाखा). url कसे मिळवायचे यासाठी मागील चरण पहा.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

उदाहरणार्थ:
```
git clone https://github.com/tavs-vārds/first-contributions.git
```
जिथे `your-name` हे तुमचे GitHub वापरकर्तानाव आहे. अशा प्रकारे तुम्ही GitHub रेपॉजिटरी * प्रथम-योगदान* मधील सामग्री तुमच्या संगणकावर कॉपी करता.
## शाखा तयार करतो
तुमच्या कॉम्प्युटरवरील रेपॉजिटरी डिरेक्टरी बदला (जर तुम्ही त्यात आधीपासून नसल्यास):

``
cd प्रथम-योगदान
``
आता 'git checkout' कमांडसह एक शाखा तयार करा:
``
git checkout -b <put-new-branch-name>
``

उदाहरणार्थ:
``
git checkout -b add-alonzo-church
``
(शाखेच्या नावात *add* हा शब्द असण्याची गरज नाही, पण ते समाविष्ट करणे उपयुक्त ठरेल, कारण या शाखेचा उद्देश तुमचे नाव यादीत समाविष्ट करणे आहे.)

## आवश्यक बदल करा आणि सबमिट करा

आता 'Contributors.md' फाईल टेक्स्ट एडिटरमध्ये उघडा आणि त्यात तुमचे नाव जोडा. फाईलच्या सुरवातीला किंवा शेवटी जोडू नका, तर मध्यभागी कुठेतरी ठेवा. नंतर फाईल सेव्ह करा.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

तुम्ही प्रोजेक्ट डिरेक्टरीमध्ये जाऊन `git status` कमांड कार्यान्वित केल्यास, तुम्हाला त्यात बदल झाल्याचे दिसेल.


तुम्ही 'git add' कमांडने नुकतेच तयार केलेल्या शाखेत खालील बदल जोडा:

``
git add Contributors.md
``

आता हे बदल `git कमिट` कमांडसह सबमिट करा:
``
git कमिट -m "योगदानकर्त्यांच्या यादीत <your-name> जोडा"
``
`<your-name>` च्या जागी तुमच्या स्वतःच्या नावाने.


## GitHub मध्ये बदल जोडते
तुमचे बदल `git push` कमांडसह जोडा:
``
git पुश मूळ <insert-name>
``
`<insert-branch-name>` तुम्ही आधी तयार केलेल्या शाखेच्या नावाने बदलत आहे.

## पुनरावलोकनासाठी बदल सबमिट करा
तुम्ही तुमच्या GitHub रेपॉजिटरीमध्ये गेल्यास, तुम्हाला `तुलना आणि विनंती पुल` बटण दिसेल. ते दाबा.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

आता जोडलेले बदल सबमिट करा.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

या प्रकल्पाच्या मुख्य शाखेत मी तुमचे सर्व बदल लवकरच जोडेन. बदल जोडल्याबरोबर तुम्हाला एक ईमेल सूचना प्राप्त होईल.

## आणि आता काय?

अभिनंदन! तुम्ही नुकतेच मानक _fork -> क्लोन -> संपादन -> PR_ वर्कफ्लो पूर्ण केले आहे ज्याचा तुम्हाला भविष्यात सह-लेखक म्हणून सामना करावा लागेल.
तुमच्या मित्रांना आणि अनुयायांना [आमच्या साइट] (https://firstcontributions.github.io/#social-share) बद्दल सांगा.

तुम्हाला मदत हवी असल्यास किंवा काही प्रश्न असल्यास तुम्ही आमच्या स्लॅक टीममध्ये देखील सामील होऊ शकता. [स्लॅकमध्ये सामील व्हा] (https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYQ

आता तुम्ही इतर प्रकल्पांमध्ये सहभागी होऊ शकता. आम्ही अशा प्रकल्पांची सूची संकलित केली आहे ज्यात तुम्हाला प्रारंभ करण्यासाठी सोप्या समस्या आहेत. एक्सप्लोर करा [आमच्या साइटवरील प्रकल्पांची सूची] (https://firstcontributions.github.io/#project-list).

Tumacyā mitrānnā āṇi anuyāyānnā [āmacyā sā'iṭa] (https://Firstcontributions.Github.Io/#social-share) baddala sāṅgā.

Tumhālā madata havī asalyāsa kinvā kāhī praśna asalyāsa tumhī āmacyā slĕka ṭīmamadhyē dēkhīla sāmīla hō'ū śakatā. [Slĕkamadhyē sāmīla vhā] (https://Join.Slack.Com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYQ

### [पापिलडू मटेरियाली](../additional-material/git_workflow_scenarios/additional-material.md)

## इतर साधनांसाठी सूचना

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|[Visual Studio Code](../github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](sourcetree-macos-tutorial.md)|
