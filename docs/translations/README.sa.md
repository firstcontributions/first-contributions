[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# प्रथमः योगदानः (First Contributions)

एषः परियोजनः नूतनानां योगदानकर्तṝणां कृते प्रथमं योगदानं सरलतया कर्तुं मार्गदर्शनं च यच्छति। यदि त्वं प्रथमं योगदानं कर्तुं इच्छसि, अधोलिखितान् चरणान् अनुसर।

_यदि त्वं आदेशपङ्क्त्या (command line) सह सुखं न अनुभवसि, तर्हि [GUI उपकरणं उपयुज्य एते मार्गदर्शकाः सन्ति।](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### यदि ते संगणके git अस्ति न चेत्, [तत् स्थापय।](https://docs.github.com/en/get-started/quickstart/set-up-git)

## एतत् भण्डारं (repository) फोर्क् कुरु

पृष्ठस्य उपरिस्थे फोर्क् (fork) बटनं नुद।  
एवं कृत्वा एषः भण्डारः तव GitHub खातायाम् प्रतिलिपिरूपेण रच्यते।

## भण्डारं क्लोनं कुरु

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

GitHub गत्वा, स्वीयं फोर्क्-भण्डारं उद्घाट्य, ‘Code’ बटनं नुद। ततः SSH चयनं कृत्वा ‘copy URL to clipboard’ चिह्नं नुद।

पश्चात् टर्मिनल् उद्घाट्य, एषः आदेशः प्रयोज्यः —

```bash
git clone "url you just copied"
```

yatra "url you just copied" (चिन्हविना) अस्ति, सः एषः भण्डारस्य url (तव fork कृत परियोजनायाः)। पूर्वं निर्दिष्टं चरणं पश्य।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

उदाहरणार्थ —

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

`this-is-you` इत्येतत् तव `GitHub` उपयोगकर्तृनाम (username) अस्ति। अत्र त्वं `GitHub` स्थित `first-contributions` नामकस्य भण्डारस्य सामग्रीं स्वयम् यन्त्रे अनुकलयसि।

## शाखां (branch) रचय

स्वयम् यन्त्रे भण्डारस्य निर्देशिकायाम् प्रवेशं कुरु (यदि तत्र पूर्वमेव न स्थितः)।

```bash
cd first-contributions
```
इदानीं `git switch` आदेशं उपयुज्य शाखां निर्मारय।

```bash
git switch -c your-new-branch-name
```

उदाहरणतः —

```bash
git switch -c add-alonzo-church
```

<details>
<summary><strong>यदि git switch कार्यं न करोति, तर्हि एतत् प्रयोज्यं:</strong></summary>

यदि एषः दोषसन्देशः दृश्यते— "Git: switch git-आदेशः नास्ति। git –help पश्य।", तर्हि सम्भवतः त्वं git-नामकस्य पुरातन-संस्करणं उपयोगसि।

एतादृशे स्थितौ git checkout इत्ययं आदेशः प्रयुज्यताम्।

```bash
git checkout -b your-new-branch-name
```

</details>

## परिवर्तनं कुरु च commit अपि कुरु

इदानीं `Contributors.md` नामकं सञ्चिकां पाठसम्पादके उद्घाटय। तत्र स्वस्य नाम योजय। सञ्चिकायाः आरम्भे वा अन्ते च नाम न योजय। मध्ये कतरेषु अपि योजय। अनन्तरं तां सञ्चिकां संरक्षय।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

यदि त्वं परियोजनायाः निर्देशिकायां गत्वा `git status` आदेशं प्रवर्तयसि, तर्हि परिवर्तनानि दृश्यन्ते।

git add आदेशं उपयुज्य त्वया नूतनया निर्मिता शाखा यत्र, तत्र एतानि परिवर्तनानि योजय।

```bash
git add Contributors.md
```

इदानीं `git commit` आदेशं उपयुज्य एतानि परिवर्तनानि सङ्ग्रहीतुं `commit` कुरु।

```bash
git commit -m "Add your-name to Contributors list"
```

`your-name` इत्येतत् स्वनाम्ना परिवर्तय।

## GitHub इत्यत्र परिवर्तनं प्रेषय

git push आदेशं उपयुज्य स्वीयं परिवर्तनं GitHub इत्यत्र प्रेषय।

```bash
git push -u origin your-branch-name
```

`your-branch-name` इत्येतत् पूर्वं त्वया निर्मितायाः शाखायाः नाम्ना परिवर्तय।

<details>
<summary><strong>यदि push समये दोषः जायते तर्हि:</strong></summary>

- ### प्रमाणीकरण-दोषः (Authentication Error)
     <pre>remote: कूटशब्द-आधारित प्रमाणीकरणस्य समर्थनं 2021 अगस्त् 13 दिनाङ्के निष्कासितम्। कृपया तस्य स्थाने personal access token उपयुज्यताम्।
  remote: अधिकविवरणाय https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ पश्यतु।
  fatal: 'https://github.com/<your-username>/first-contributions.git/' इत्यत्र प्रमाणीकरणं असफलम्।</pre>
  स्वखाते SSH key निर्माणं तथा विन्यासं कर्तुं [GitHub इत्यस्य शिक्षणं](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) पश्य।

  अपि च, त्वं 'git remote -v' इत्येतं आदेशं प्रवर्तयन् स्वस्य remote address ज्ञातुं इच्छेयाः।

  यदि एषः परिणामः दृश्यते—
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>

  तर्हि एतेन आदेशेन तं परिवर्तय:
```bash
git remote set-url origin git@github.com:your-username/your_repo.git
```
  अन्यथा त्वं पुनः username तथा च password प्रवेशयितुं प्रेरितः भविष्यसि, तथा च प्रमाणीकरण-दोषः अपि प्राप्तः भविष्यति।
</details>

## समीक्षायै परिवर्तनं समर्पय

यदि त्वं स्वं GitHub भण्डारं गच्छसि, तर्हि `Compare & pull request` इत्यः बटनः दृष्टव्यः भविष्यति। तं बटनं नुद। 

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

तदनन्तरं pull request समर्पय।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

शीघ्रं अहं तव सर्वाणि परिवर्तनानि अस्य परियोजनायाः मुख्यशाखायां संयोजयिष्यामि। यदा ते परिवर्तनानि संयोजितानि भविष्यन्ति, तदा तव इमेल्-पत्रे एकं सूचना-सन्देशं लप्स्यसे।

## इतः परं कुत्र गन्तव्यम्?

साधु! त्वं सफलतया सामान्यं _fork → clone → edit → pull request_ इत्येतत् कार्यप्रवाहं पूर्णीकृतवान् यं योगदानकर्तृभिः प्रायः अनुभवते।

स्वीयं योगदानं उत्सवेन चिनोतु च स्वमित्रैः अनुयायिभिश्च सह साझां कुरु [web app](https://firstcontributions.github.io/#social-share) इत्यत्र गत्वा।

यदि त्वं अधिकं अभ्यासं कर्तुम् इच्छसि, तर्हि [code contributions](https://github.com/roshanjossey/code-contributions) इत्येतत् पश्य।

अद्य वयं त्वां अन्येषु परियोजनासु योगदानं कर्तुं आरब्धुं सज्जीकरोमः। वयं सरलैः समस्याभिः युक्तानां परियोजनानां सूचीं सङ्कलितवन्तः।  
[web app इत्यस्य परियोजना-सूची](https://firstcontributions.github.io/#project-list) अपि पश्य।


### [अधिकवस्तु](docs/additional-material/git_workflow_scenarios/additional-material.md)

## दृश्योपकरणं उपयोग्य शिक्षणम्

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>एषः परियोजनः एतेन समर्थितः अस्ति:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>