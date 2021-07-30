[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# पहिलो योगदान
पहिलो पटक नयाँ काम गर्न खोज्दा अवश्य कठिन लाग्नसक्छ  र गर्दैजादाँ भुल्चुक गल्ति पनि हुन सक्छ । हामी नयाँ खुल्ला स्रोत योगदानकर्ताकोलागी योगदान गर्न सिक्ने तरिका सहज र सरल बनाउन चाहनछौं।

लेखहरु पढेर र भिडियोहरु हेरेर सबै कुरा सिकेको जस्तो लागेता पनि, जब सम्म तपाई अभ्यास गर्नु हुदैन तब सम्म तपाईलाई गर्दै जादाँ आउने कठिनाईका बारे थाहा हुदैन।  यो परियोजनाले नयाँ खुल्ला स्रोत कर्ताहरुलाई खुल्ला स्रोत योगदानका लागि शुरुआत गर्न तथा गर्दैजादाँ आउने समस्याको समधान गर्न मदत गर्दछ। तपाई यदि आफ्नो पहिलो योगदान गर्न चाहनुहुन्छ भने निम्न दिएको निर्देशनको पालन गर्नुहोस्।   

#### *यदि तपाइँ COMMAND LINE INTERFACE बाट काम गर्न सहज हुनुहुन्न भने, [यहाँ बैकल्पिक रुपमा GRAPHICAL USER INTERFACE (GUI) को प्रयोग गरि काम गर्ने सकिने निर्देशनहरु पनि राखिएको छ](#tutorials-using-other-tools)।* 

#### *यस निर्देशन अन्य [भाषाहरूमा](Translations.md) पढ्नुहोस्।*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="यो भण्डार फोर्क गर्नुहोस।" />

सर्वप्रथम, आफ्नो कम्प्युटरमा GIT भएको वा नभएको सुनिस्चित गर्नुहोस्। यदि तपाइको कम्पुटरमा पहिला देखिनै GIT छैन भने, [यी निर्देशनको पालना गर्न सक्नुहुनेछ।]( https://help.github.com/articles/set-up-git/)

## यो रेपो फोर्क गर्नुहोस् 
फोर्क गर्नकोलागि यस रेपो `(Repository)` को पहिलो  पृष्ठमा रहेको फोर्क `(Fork)` भन्ने बटनलाई क्लिक गर्नुहोस्। यो बटन क्लिक गरेपछि, तपाईको एकाउनटमा पनि यस रेपोको एक कपी बस्ने छ।

## यस रेपोलाई क्लोन गर्नुहोस् 

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="यो भण्डारलाई क्लोन गर्नुहोस्" />

तपाईले भर्खरै फोर्क गर्नुभएको रेपोलाई आफ्नो कम्प्युटरमा क्लोन गर्नुहोस्। क्लोन गर्नकोलागी, तपाइको एकाउन्टमा फोर्क भएको रेपो खोल्नुहोस र कोड `(Code)` लेखिएको बटनमा क्लिक गर्नुहोस् र कपी टु क्लिपबोर्ड `(Copy to cipboard)` भन्ने आइकोन क्लिक गर्नुहोस्। थप समस्या भएमा साइडमा राखिएको चित्रको मदत लिन सक्नुहुनेछ। 

आफ्नो कम्प्युटरमा टर्मिनल `(Terminal)` खोल्नुहोस र तल दिएको कोडको प्रयोग गर्नुहोस् ,
```
git clone "URL you copied"
```
`URL you copied` भनिएको ठाउँमा अगि कपी गर्नुभएको लिंक पेस्ट गर्नुहोस्।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL लाई क्लिपबोर्डमा प्रतिलिपि बनाउनुहोस्" />

उदाहरणको लागी:
```
git clone https://github.com/this-is-you/first-contributions.git
```
उदाहरणमा `this_is_you` भनेको ठाउँमा तपाईको गिटहबको युजरनेम राख्नुहोस्। यहाँ तपाइँ GitHub मा तपाईंको कम्प्युटरमा पहिलो-योगदान भण्डारको सामग्री प्रतिलिपि गर्दै हुनुहुन्छ।

## नयाँ शाखा बनाउनुहोस्

यदि तपाई आफ्नो रेपोको डिरेक्टोरीमा हुनुहुन्न भने, सर्व-प्रथम आफ्नो रेपोको डिरेक्टोरीमा जानुहोस्। त्यसको लागि तल दिएको कोड प्रयोग गर्न सक्नु हुनेछ। 

```
cd first-contributions
```
अब नयाँ शाखा बनाउनुहोस्। त्यसको लागि तल दिएको कोड `git checkout` प्रयोग गर्न सक्नु हुनेछ। 
```
git checkout -b <शाखाको-नाम>
```
उदाहरणका लागि:
```
git checkout -b add-milap-neupane
```
कृपया तपाईले बनाएको शाखाको नाम राख्दा, उचित नामको प्रयोग गर्नुहोस्। 

## आवश्यक परिवर्तनहरू गर्नुहोस् र ती परिवर्तनहरू प्रतिबद्ध गर्नुहोस्

अब पाठ सम्पादकमा `Contributors.md` फाइल खोल्नुहोस् र यसमा तपाईंको नाम थप्नुहोस्। फाइलको सुरुवात वा अन्त्यमा यसलाई जोड नगर्नुहोस्। यसलाई बीचमा राख्नुहोस्। अब, फाईल save गर्नुहोस्।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


यदि तपाई प्रोजेक्ट डिरेक्टोरीमा गएर, यहाँ लेखिएको कोड `git status` प्रयोग गर्नुहुन्छ भने, तपाईले गर्नुभएको परिवर्तनहरु तपाई देख्न सक्नुहुनेछ।

अब तपाईँले भर्खरै बनाएको शाखामा `git add` कमांड प्रयोग गरी ती परिवर्तनहरू थप्नुहोस्:

```
git add Contributors.md
```

अब `git commit` आदेश प्रयोग गरेर ती परिवर्तनहरू प्रतिबद्ध गर्नुहोस्:
```
git commit -m "योगदान सूचीमा <तपाईँको-नाम> थप गर्नुहोस्"
```

`<तपाईंको-नाम>` भएको ठाउँमा आफ्नो नाम राख्नुहोस्। 

## GitHub मा परिवर्तन पुश गर्नुहोस

`git push` कमाण्डको प्रयोग गरेर आफ्नो परिवर्तन पुश गर्नुहोस्:
```
git push origin <शाखाको-नाम>
```
`<शाखाको-नाम>` भएको ठाउँमा तपाईले पहिले सिर्जना गर्नुभएको शाखाको नाम राख्नुहोस् ।

## समीक्षाको लागि तपाईंको परिवर्तनहरू पेश गर्नुहोस्

यदि तपाईं GitHub मा तपाईंको भण्डारमा जानुहुन्छ भने, तपाइँ एक `compare र pull request` बटन देख्नुहुनेछ। त्यस बटनमा क्लिक गर्नुहोस्।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="एउटा पुल अनुरोध सिर्जना गर्नुहोस्" />

अब pull request पेश गर्नुहोस्।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

चाँडै म यस परियोजनाको मास्टर शाखामा तपाईका सबै परिवर्तनहरू मर्ज गर्नेछु। परिवर्तनहरू विलय भएपछि एक अधिसूचना इमेल प्राप्त गर्नुहुनेछ।

## यहाँबाट कहाँ जानुहुन्छ?

बधाई छ! तपाईले _फर्क -> क्लोन -> सम्पादन -> PR_कार्यप्रवाह पूरा गर्नुभयो जुन तपाई प्राय: एक योगदानकर्ताको रूपमा सामना गर्नुहुनेछ!

तपाईंको योगदान मनाउनुहोस् र आफ्नो साथी र अनुयायीहरूसँग [वेब अनुप्रयोग](https://roshanjossey.github.io/first-contributions/#social-share) मा जानुहोस्।

तपाइँलाई कुनै पनि मद्दत चाहिन्छ वा कुनै प्रश्न छ भने तपाइँ हाम्रो स्लाक टोलीमा सामेल हुन सक्नुहुनेछ। [स्लाक टोलीमा सामेल हुनुहोस्](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

अब तपाईले अन्य परियोजनाहरूमा योगदान दिन सुरु गरौं। हामीले सुरू गर्न सक्नुहुने सजिलो समस्याहरूको साथमा परियोजनाहरूको सूची संकलन गरेको छ। जाँच गर्नुहोस् [वेब अनुप्रयोगमा परियोजनाहरूको सूची](https://roshanjossey.github.io/first-contributions/#project-list)।

### [थप सामग्री](../additional-material/git_workflow_scenarios/additional-material.md)

## ट्यूटोरियलहरू अन्य उपकरणहरू प्रयोग गर्दै

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>|<a href="../github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|[Visual Studio Code](../github-windows-vs-code-tutorial.md)|

