[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# पहिलो योगदान
यो कठिन छ। पहिलो पल्ट केहि गर्दा सधै कठिन हुन्छ। बिशेष गरि जब तपाई योगदान गर्दै हुनुहुन्छ,गल्ति हुनु सहज कुरा हैन। हामी नया खुला स्रोत योगदानकर्ताले सिक्ने र योगदान गर्ने तरिका लाई सहज बनाउन चहन्थियेउम।

लेखहरू पढ्न र ट्यूटोरियलहरू हेर्न मद्दत गर्न सक्दछ, तर वास्तवमा एक अभ्यास वातावरणमा गरेर हेर्दा भन्दा के असल होला र। यो परियोजनाले निर्देशन प्रदान गर्न र शुरुआती शुरुवातहरूलाई उनीहरूको पहिलो योगदान प्रदान गर्ने तरिका सरल बनाउँदछ। यदि तपाईं आफ्नो पहिलो योगदान बनाउन खोज्दै हुनुहुन्छ भने तलको चरणहरू पालना गर्नुहोस्।

#### *यदि तपाईं कमांड रेखासँग सहज हुनुहुन्न भने, [यहाँ GUI उपकरणहरू प्रयोग गरेर ट्यूटोरियलहरू छन्।]( #tutorials-using-other-tools )*

#### *यो अन्य [भाषाहरूमा](Translations.md) पढ्नुहोस्।*

<img align="right" width="300" src="../assets/fork.png" alt="यो भण्डार फोर्क गर्नुहोस।" />

यदि तपाईंसँग तपाइँको मेशिनमा Git छैन, [यसलाई इन्स्टल गर्नुहोस्]( https://help.github.com/articles/set-up-git/).

## यो भण्डार फोर्क गर्नुहोस
यस पृष्ठको शीर्षमा फोर्क बटनमा क्लिक गरेर यो रिपो फोर्क गर्नुहोस। यसले तपाईंको खातामा यस भण्डारको प्रतिलिपि सिर्जना गर्नेछ।

## भण्डार क्लोन गर्नुहोस्

<img align="right" width="300" src="../assets/clone.png" alt="यो भण्डारलाई क्लोन गर्नुहोस्" />

अब तपाइँको मेसिनमा फोर्क गरिएको रिपो क्लोन गर्नुहोस। तपाईंको GitHub खातामा जानुहोस्, फोर्क गरिएको रिपो खोल्नुहोस्, क्लोन बटनमा क्लिक गर्नुहोस् र त्यसपछि *copy to clipboard* आइकनमा क्लिक गर्नुहोस्।

टर्मिनल खोल्नुहोस् र निम्न Git आदेश चलाउनुहोस्:

```
git clone "url तपाईंले भर्खरै प्रतिलिपि गर्नुभएको"
```
जहाँ "युआरएल तपाईंले भर्खरै प्रतिलिपि गर्नुभयो" (" चिन्हहरू बिना) यस भण्डारको url हो (यस परियोजनाको तपाईंको फोर्क)। Url प्राप्त गर्न अघिल्लो चरण हेर्नुहोस्।

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="URL लाई क्लिपबोर्डमा प्रतिलिपि बनाउनुहोस्" />

उदाहरणका लागि:
```
git clone https://github.com/this-is-you/first-contributions.git
```
जहाँ `this-is-you` तपाईंको GitHub प्रयोगकर्ता नाम हो। यहाँ तपाइँ GitHub मा तपाईंको कम्प्युटरमा पहिलो-योगदान भण्डारको सामग्री प्रतिलिपि गर्दै हुनुहुन्छ।

## एक शाखा बनाउनुहोस्

तपाईंको कम्प्यूटरमा भण्डार गरिएको डाइरेक्टरीमा परिवर्तन गर्नुहोस् (यदि तपाईं पहिले नै हुनुहुन्न भने):

```
cd first-contributions
```
अब `git checkout` आदेश प्रयोग गरेर एउटा शाखा सिर्जना गर्नुहोस्:
```
git checkout -b <शाखाको-नाम>
```
उदाहरणका लागि:
```
git checkout -b add-milap-neupane
```
(शाखा को नाममा *add* शब्द को आवश्यकता छैन, तर यसमा एक उचित कुरा समावेश छ किनभने यस शाखाको उद्देश्य तपाईंको नामलाई सूचीमा थप्न हो।)

## आवश्यक परिवर्तनहरू गर्नुहोस् र ती परिवर्तनहरू प्रतिबद्ध गर्नुहोस्

अब पाठ सम्पादकमा `Contributors.md` फाइल खोल्नुहोस्, यसलाई तपाईंको नाम थप्नुहोस्। फाइलको सुरुवात वा अन्त्यमा यसलाई जोड नगर्नुहोस्। यसलाई बीचमा राख्नुहोस्। अब, फाईल save गर्नुहोस्।

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />


यदि तपाईं प्रोजेक्ट डाइरेक्टरीमा जानुहोस् र आदेश `git status` लाई कार्यान्वयन गर्नुहुन्छ भने,तपाइँ त्यहाँ परिवर्तनहरू देख्नुहुनेछ।

तपाईँले भर्खरै बनाएको शाखामा `git add` कमांड प्रयोग गरी ती परिवर्तनहरू थप्नुहोस्:

```
git add Contributors.md
```

अब `git commit` आदेश प्रयोग गरेर ती परिवर्तनहरू प्रतिबद्ध गर्नुहोस्:
```
git commit -m "योगदान सूचीमा <तपाइको-नाम> थप गर्नुहोस्"
```

तपाईंको नामको साथ `<तपाईंको-नाम>` को स्थानान्तरण गर्नुहोस्।

## GitHub मा परिवर्तन पुश गर्नुहोस

आदेश `git push` को प्रयोग गरेर आफ्नो परिवर्तन पुश गर्नुहोस्:
```
git push origin <शाखाको-नाम>
```
तपाईले पहिले सिर्जना गर्नुभएको शाखाको नामको साथ `<शाखाको-नाम>` को प्रतिस्थापन गर्नुहोस्।

## समीक्षाको लागि तपाईंको परिवर्तनहरू पेश गर्नुहोस्

यदि तपाईं GitHub मा तपाईंको भण्डारमा जानुहुन्छ भने, तपाइँ एक `compare र pull request` बटन देख्नुहुनेछ। त्यस बटनमा क्लिक गर्नुहोस्।

<img style="float: right;" src="../assets/compare-and-pull.png" alt="एउटा पुल अनुरोध सिर्जना गर्नुहोस्" />

अब pull request पेश गर्नुहोस्।

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

चाँडै म यस परियोजनाको मास्टर शाखामा तपाईका सबै परिवर्तनहरू मर्ज गर्नेछु। परिवर्तनहरू विलय भएपछि एक अधिसूचना इमेल प्राप्त गर्नुहुनेछ।

## यहाँबाट कहाँ जानुहुन्छ?

बधाई छ! तपाईले _फर्क -> क्लोन -> सम्पादन -> PR_कार्यप्रवाह पूरा गर्नुभयो जुन तपाई प्राय: एक योगदानकर्ताको रूपमा सामना गर्नुहुनेछ!

तपाईंको योगदान मनाउनुहोस् र आफ्नो साथी र अनुयायीहरूसँग [वेब अनुप्रयोग](https://roshanjossey.github.io/first-contributions/#social-share) मा जानुहोस्।

तपाइँलाई कुनै पनि मद्दत चाहिन्छ वा कुनै प्रश्न छ भने तपाइँ हाम्रो स्लाक टोलीमा सामेल हुन सक्नुहुनेछ। [स्लाक टोलीमा सामेल हुनुहोस्](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

अब तपाईले अन्य परियोजनाहरूमा योगदान दिन सुरु गरौं। हामीले सुरू गर्न सक्नुहुने सजिलो समस्याहरूको साथमा परियोजनाहरूको सूची संकलन गरेको छ। जाँच गर्नुहोस् [वेब अनुप्रयोगमा परियोजनाहरूको सूची](https://roshanjossey.github.io/first-contributions/#project-list)।

### [थप सामग्री](additional-material/git_workflow_scenarios/additional-material.md)

## ट्यूटोरियलहरू अन्य उपकरणहरू प्रयोग गर्दै

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

