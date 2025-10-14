[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# पहिला योगदान (First Contributions)

ई प्रोजेक्ट के मकसद बा कि नया लोग अपना पहिला योगदान आसान आ समझदार तरीका से करे। अगर रउआ योगदान देवे के चाहत बानी, त नीचे दिहल स्टेप्स फॉलो करीं।  

लेख पढ़ल आ ऑनलाइन ट्यूटोरियल देखल मदद कर सके ला, बाकि खुद काम क के गलती करे से बेसी सीख मिले ला। ई प्रोजेक्ट रउआ के पहिला योगदान खातिर गाइड करी। याद राखीं - जेतना आराम से सीखब, ओतना जल्दी आ बढ़िया सीखब।  

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

अगर रउआ कंप्यूटर पर Git ना बा, [इंस्टॉल करीं](https://help.github.com/articles/set-up-git/)।  

_अगर रउआ कमांड लाइन से सहज ना बानी, [त GUI टूल इस्तेमाल करे वाला ट्यूटोरियल भी बा](#अन्य-टूल-का-उपयोग-करके-ट्यूटोरियल)।_

## रिपॉजिटरी के फोर्क करीं (Fork this repository)

ऊपर वाला **Fork** बटन दबाके ई रिपॉजिटरी फोर्क करीं। ई रउआ GitHub अकाउंट में एक कॉपी बना दी, जवन सिर्फ रउआ खातिर होई।  

## रिपॉजिटरी के क्लोन करीं (Clone the repository)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

अब ई रिपॉजिटरी के आपन कंप्यूटर पर क्लोन करीं। GitHub अकाउंट में जाएं, फोर्क कइल रिपॉजिटरी खोलें, **Code** बटन दबाईं आ **Copy to Clipboard** आइकन पर क्लिक करीं।  

टर्मिनल/कमांड प्रॉम्प्ट खोल के ई कमांड चलाईं:
git clone "रउआ जे URL अभी कॉपी कइनी"


जहाँ `"रउआ जे URL अभी कॉपी कइनी"` के जगह रउआ के फोर्क के लिंक आई।  

उदाहरण:



git clone https://github.com/Rauwa-username/first-contributions.git


`Rauwa-username` रउआ GitHub यूजरनेम बा। ई कमांड रउआ कंप्यूटर पर रिपॉजिटरी के लोकल कॉपी बना दी।  

## एगो ब्रांच बनाईल जाव (Create a branch)

अब रिपॉजिटरी वाला फोल्डर में जाईं:



cd first-contributions


फिर एगो नया ब्रांच बनाईल जाव:



git switch -c <अपना-ब्रांच-नाम>


उदाहरण:



git switch -c add-bihari-translation


(ब्रांच नाम में `add` रहे जरूरी नइखे, बाकि समझदारी खातिर रखल जा सकेला, काहे कि ई नाम जोड़ला खातिर बा।)  

## जरूरी बदलाव करीं आ कमिट करीं (Make changes & commit)

`Contributors.md` फाइल खोलीं, आ अपना नाम जोड़ दीं। फाइल के शुरू या अंत में मत डालल जाव, बीच में कहीं भी।  

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

अब देखीं का बदलाव बा:



git status


बदलाव जोड़ल जाव:



git add Contributors.md


फिर कमिट करीं:



git commit -m "Add <रउआ-नाम> to Contributors list"


`<रउआ-नाम>` के जगह अपना नाम लिखीं।  

## बदलाव Github पर पुश करीं (Push changes to GitHub)



git push origin <अपना-ब्रांच-नाम>

`<अपना-ब्रांच-नाम>` में अपना ब्रांच के नाम डालल जाव।  

## बदलाव के रिव्यु खातिर सबमिट करीं (Submit pull request)

GitHub अकाउंट में अपने रिपॉजिटरी खोलें, **Compare & pull request** बटन दबाईं।  

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

अब अपना Pull Request सबमिट करीं:

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

जल्द ही रउआ बदलाव मुख्य ब्रांच में मर्ज हो जाई, आ रउआ ईमेल से नोटिफिकेशन पाईब।  

## आगे कहाँ जाईं? (Where to go from here?)

बधाई! रउआ _fork -> clone -> edit -> PR_ वर्कफ़्लो पूरा कइनी।  

अपना पहिला योगदान के जश्न मनाईं आ [वेब एप्प](https://firstcontributions.github.io/#social-share) पर दोस्त लोग के बताईं।  

अब दुसरा प्रोजेक्ट पर योगदान करीं। आसान इश्यू वाला प्रोजेक्ट लिस्ट [एहिजा](https://firstcontributions.github.io/#project-list) देखें।  


`<अपना-ब्रांच-नाम>` में अपना ब्रांच के नाम डालल जाव।  

## बदलाव के रिव्यु खातिर सबमिट करीं (Submit pull request)

GitHub अकाउंट में अपने रिपॉजिटरी खोलें, **Compare & pull request** बटन दबाईं।  

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

अब अपना Pull Request सबमिट करीं:

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

जल्द ही रउआ बदलाव मुख्य ब्रांच में मर्ज हो जाई, आ रउआ ईमेल से नोटिफिकेशन पाईब।  

## आगे कहाँ जाईं? (Where to go from here?)

बधाई! रउआ _fork -> clone -> edit -> PR_ वर्कफ़्लो पूरा कइनी।  

अपना पहिला योगदान के जश्न मनाईं आ [वेब एप्प](https://firstcontributions.github.io/#social-share) पर दोस्त लोग के बताईं।  

अब दुसरा प्रोजेक्ट पर योगदान करीं। आसान इश्यू वाला प्रोजेक्ट लिस्ट [एहिजा](https://firstcontributions.github.io/#project-list) देखें।  

## अन्य टूल्स इस्तेमाल क के ट्यूटोरियल (Tutorials Using Other Tools)

| <a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                          | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                       | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                     | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                               | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                |
