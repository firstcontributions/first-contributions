[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# पहिलो योगदान
यस प्रोजेक्टले शुरुवातकर्ताहरूले आफ्नो पहिलो योगदान गर्ने तरिकालाई सरल बनाउने र मार्गदर्शन गर्ने लक्ष्य राखेको छ। यदि तपाईं आफ्नो पहिलो योगदान गर्न खोज्दै हुनुहुन्छ भने, तलका चरणहरू पालना गर्नुहोस्।

यदि तपाईं कमाण्ड कमांड लाइन (command line) सँग सहज हुनुहुन्न भने, [यहाँ GUI तूल्सहरू प्रयोग गरेर सेकैएको ट्यूटोरियलहरू छन्।](#ट्यूटोरियलहरू-अन्य-उपकरणहरू-प्रयोग-गर्दै)

यो अन्य [भाषाहरूमा](Translations.md) पढ्नुहोस्।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="यो भण्डार फोर्क गर्नुहोस।" />

यदि तपाईंसँग तपाइँको कम्प्यूटरमा Git छैन, [यसलाई इन्स्टल गर्नुहोस्।]( https://help.github.com/articles/set-up-git/)

## यो रिपो फोर्क गर्नुहोस
यस पृष्ठको शीर्षमा फोर्क बटनमा क्लिक गरेर यो रिपो फोर्क गर्नुहोस। यसले तपाईंको GitHub खातामा यस रिपोको प्रतिलिपि सिर्जना गर्नेछ।

## रिपो क्लोन गर्नुहोस्

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="यो भण्डारलाई क्लोन गर्नुहोस्" />

अब तपाइँको कम्प्यूटरमा फोर्क गरिएको रिपो क्लोन गर्नुहोस। तपाईंको GitHub खातामा जानुहोस्, फोर्क गरिएको रिपो खोल्नुहोस्, क्लोन बटनमा क्लिक गर्नुहोस् र त्यसपछि *copy to clipboard* आइकनमा क्लिक गर्नुहोस्।

टर्मिनल खोल्नुहोस् र निम्न Git कमाण्ड चलाउनुहोस्:

```
git clone "तपाईंले भर्खरै प्रतिलिपि गर्नुभएको URL"
```
जहाँ "तपाईंले भर्खरै प्रतिलिपि गर्नुभएको URL" (" चिन्हहरू बिना) छ, त्यो यस रिपोको url हो (यस प्रोजेक्टको लागी तपाईंको फोर्क)। Url प्राप्त गर्न अघिल्लो चरण हेर्नुहोस्।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL लाई क्लिपबोर्डमा प्रतिलिपि बनाउनुहोस्" />

उदाहरणका लागि:
```
git clone https://github.com/this-is-you/first-contributions.git
```
जहाँ `this-is-you` छ, त्यहाँ तपाईंको GitHub प्रयोगकर्ता नाम (GitHub username) लेख्नुहोस् । यहाँ तपाइँले GitHub बाट तपाईंको कम्प्युटरमा first-contributions रिपोको सामग्री प्रतिलिपि गर्दै हुनुहुन्छ।

## एउटा ब्रांच बनाउनुहोस्

तपाईंको कम्प्यूटरमा रिपोको डाइरेक्टरी खोल्नुहोस् (यदि तपाईं पहिले नै हुनुहुन्न भने):

```
cd first-contributions
```
अब `git checkout` कमाण्ड प्रयोग गरेर एउटा ब्रन्च सिर्जना गर्नुहोस्:
```
git checkout -b <ब्रन्चको-नाम>
```
उदाहरणको लागि:
```
git checkout -b add-alonzo-church
```
(ब्रन्च को नाममा *add* शब्द को आवश्यकता छैन, तर यसमा add समावेश गर्न उचित छ किनभने यस ब्रन्चको उद्देश्य तपाईंको नामलाई सूचीमा थप्ने हो।)

## आवश्यक परिवर्तनहरू गर्नुहोस् र ती परिवर्तनहरू कोम्मित गर्नुहोस्

अब टेक्स्ट एडिटओरमा (text editor) `Contributors.md` फाइल खोल्नुहोस्, यसमा तपाईंको नाम थप्नुहोस्। फाइलको सुरुवात वा अन्त्यमा तपाईंको नाम नथप्नुहोस्। तपाईंको नामलाई बीचमा राख्नुहोस्। अब फाईल save गर्नुहोस्।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


यदि तपाईं प्रोजेक्ट डाइरेक्टरीमा जानुभयो र `git status` कमाण्डलाई रन (run) गर्नुभयो भने,तपाइँले त्यहाँ परिवर्तन भएका फाइलहरुको सुची देख्नुहुनेछ।

तपाईँले भर्खरै बनाउनु भएको ब्रन्चमा `git add` कमाण्ड प्रयोग गरी ती परिवर्तनहरू थप्नुहोस्:

```
git add Contributors.md
```

अब `git commit` कमाण्ड प्रयोग गरेर ती परिवर्तनहरू कोम्मित (commit) गर्नुहोस्:
```
git commit -m "योगदान सूचीमा <तपाइको-नाम> थप गर्नुहोस्"
```

`<तपाईंको-नाम>` को साटोमा तपाईंको आफ्नो नाम लेख्नुहोस्।

## GitHub मा परिवर्तन पुश गर्नुहोस

`git push` कमाण्डको प्रयोग गरेर आफ्नो परिवर्तन पुश (push) गर्नुहोस्:
```
git push origin <ब्रांचको-नाम>
```
`<ब्रांचको-नाम>` को साटोमा तपाईले पहिले सिर्जना गर्नुभएको ब्रांचको नामको लेख्नुहोस्।

## रिभ्युको लागि तपाईंको परिवर्तनहरू पेश गर्नुहोस्

यदि तपाईं GitHub मा तपाईंको रेपोसितोरीमा (repository) जानुहुन्छ भने, तपाइँले `compare & pull request` बटन देख्नुहुनेछ। त्यस बटनमा क्लिक गर्नुहोस्।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="एउटा पुल अनुरोध सिर्जना गर्नुहोस्" />

अब pull request सब्मित गर्नुहोस्।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

चाँडै म यस प्रोजेक्टको मास्टर ब्रन्चमा तपाईका सबै परिवर्तनहरू मर्ज गर्नेछु। परिवर्तनहरू मर्ज भएपछि एक अधिसूचना (notification) इमेल प्राप्त गर्नुहुनेछ।

## यहाँबाट कहाँ जाने?

बधाई छ! तपाईले फोर्क -> क्लोन -> एडिट -> पुल्ल रिक्वेस्ट कार्यनोयन पूरा गर्नुभयो, जुन तपाई प्राय: एक योगदानकर्ताको रूपमा गर्नुहुनेछ!

तपाईंले योगदान दिनु भएकोमा खुशी मनाउनुहोस् र आफ्नो साथी र फोल्लोवेरहरू माझ शेयर गर्नुहोस्। [वेब अनुप्रयोग](https://roshanjossey.github.io/first-contributions/#social-share)

तपाइँलाई कुनै पनि मद्दत चाहिन्छ वा कुनै प्रश्न छ भने तपाइँ हाम्रो स्लाक टीममा (slack team) सामेल हुन सक्नुहुनेछ। [स्लाक टोलीमा सामेल हुनुहोस्](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

अब तपाईले अन्य प्रोजेक्टहरूमा योगदान दिन सुरु गर्नुहोस्। हामीले तपाईंले गर्न सक्नुहुने सजिलो समस्याहरूको साथमा प्रोजेक्टहरूको सूची संकलन गरेका छौ। हेर्नुहोस् [वेब अनुप्रयोगमा परियोजनाहरूको सूची](https://roshanjossey.github.io/first-contributions/#project-list)।

### [थप सामग्री](../additional-material/git_workflow_scenarios/additional-material.md)

## ट्यूटोरियलहरू अन्य उपकरणहरू प्रयोग गर्दै

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

