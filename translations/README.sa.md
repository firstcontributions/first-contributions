[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# प्रथम योगदान

अस्याः परियोजनायाः उद्देश्यं भवति यत् आरम्भकानां प्रथमं योगदानं यथा भवति तस्य सरलीकरणं मार्गदर्शनं च। यदि भवान् प्रथमं योगदानं दातुं इच्छति तर्हि अधोलिखितानि पदानि अनुसृत्य ।

_यदि भवान् आदेशपङ्क्तौ सहजः नास्ति तर्हि [अत्र GUI साधनानां उपयोगेन पाठ्यक्रमाः सन्ति ।](#अन्येषां-साधनानां-उपयोगेन-पाठ्यक्रमाः)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### यदि भवतः यन्त्रे git नास्ति तर्हि [तत् संस्थापयन्तु ।](https://docs.github.com/en/get-started/quickstart/set-up-git).

## एतत् भण्डारं फोर्कं कुर्वन्तु

अस्य पृष्ठस्य उपरि fork बटन् नुत्वा एतत् भण्डारं फोर्कं कुर्वन्तु ।
एतेन भवतः खाते अस्य भण्डारस्य प्रतिलिपिः निर्मीयते ।

## भण्डारस्य क्लोनीकरणं कुर्वन्तु

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

अधुना फोर्कयुक्तः भण्डारः इत्येतत् स्वस्य यन्त्रे क्लोन कुर्वन्तु । स्वस्य GitHub खाते गत्वा, फोर्कयुक्तः भण्डारः उद्घाट्य, code बटन् नुदन्तु ततः _copy to clipboard_ चिह्नं नुदन्तु ।

एकं टर्मिनल् उद्घाट्य निम्नलिखितम् git आदेशं चालयन्तु:

```bash
git clone "url भवता अधुना एव प्रतिलिपितः"
```

यत्र "url भवता अधुना एव प्रतिलिपितः" (उद्धरणचिह्नानि विना) अस्य भण्डारस्य (अस्य परियोजनायाः भवतः काङ्कस्य) url अस्ति । url प्राप्तुं पूर्वपदानि पश्यन्तु ।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

उदाहरणतया:

```bash
git clone git@github.com:एषः-त्वम्/first-contributions.git
```

यत्र `एषः-त्वम्` भवतः GitHub उपयोक्तृनाम अस्ति । अत्र भवान् GitHub इत्यत्र first-contributions भण्डारस्य सामग्रीं स्वसङ्गणके प्रतिलिखति ।

## शाखां रचयतु

सङ्गणके भण्डारनिर्देशिकायां परिवर्तनं कुर्वन्तु (यदि भवान् पूर्वमेव तत्र नास्ति):

```bash
cd first-contributions
```

अधुना `git switch` इति आदेशस्य उपयोगेन शाखा रचयन्तु :

```bash
git switch -c <भवतः-नूतनं-शाखानाम>
```

उदाहरणतया:

```bash
git switch -c add-alonzo-church
```

## आवश्यकं परिवर्तनं कृत्वा तान् परिवर्तनान् प्रतिबद्धं कुर्वन्तु

अधुना एकस्मिन् पाठसम्पादके `Contributors.md` सञ्चिकां उद्घाटयन्तु, तस्मिन् स्वनाम योजयन्तु । सञ्चिकायाः ​​आरम्भे अन्ते वा न योजयन्तु । मध्ये कुत्रापि स्थापयतु। अधुना, सञ्चिकां रक्षन्तु ।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

यदि भवान् परियोजनानिर्देशिकायां गत्वा `git status` इति आदेशं निष्पादयति तर्हि परिवर्तनं भवति इति पश्यति ।

`git add` आदेशस्य उपयोगेन भवता अधुना निर्मितायाः शाखायां तानि परिवर्तनानि योजयन्तु:

```bash
git add Contributors.md
```

अधुना `git commit` आदेशस्य उपयोगेन तानि परिवर्तनानि प्रतिबद्धं कुर्वन्तु:

```bash
git commit -m "Add <भवतः-नाम> to Contributors list"
```

`<भवतः-नाम>` इत्यस्य स्थाने भवतः नाम ।

## GitHub इत्यत्र परिवर्तनं धक्कायन्तु

`git push` इति आदेशस्य उपयोगेन स्वपरिवर्तनानि धक्कायन्तु:

```bash
git push -u origin <भवतः-शाखा-नाम>
```

`<भवतः-शाखा-नाम>` इत्यस्य स्थाने पूर्वं भवता निर्मितायाः शाखायाः नाम स्थापयित्वा ।

<details>
<summary> <strong>यदि भवन्तः धक्कायन्ते किमपि दोषं प्राप्नुवन्ति तर्हि अत्र क्लिक् कुर्वन्तु:</strong> </summary>

- ### प्रमाणीकरणदोषः
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  स्वस्य खाते SSH कुञ्जी उत्पन्नं विन्यस्तं च इति विषये [GitHub इत्यस्य पाठ्यक्रमं](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) 
  गच्छन्तु ।

</details>

## समीक्षायै स्वपरिवर्तनानि प्रस्तूयताम्


यदि भवान् GitHub इत्यत्र स्वस्य भण्डारं गच्छति तर्हि `Compare & pull request` इति बटनं पश्यति । तस्मिन् बटन् नुदन्तु ।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

अधुना पुल-अनुरोधं प्रस्तूयताम् ।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />


शीघ्रमेव अहं भवतः सर्वान् परिवर्तनान् अस्य परियोजनायाः मुख्यशाखायां विलीनं करिष्यामि। परिवर्तनं विलीनं जातं चेत् भवन्तः सूचना-ईमेलं प्राप्नुवन्ति ।

## इतः कुत्र गन्तव्यम् ?

अभिनन्दनम्! भवान् अधुना एव मानकं _fork -> clone -> edit -> pull request_ कार्यप्रवाहं सम्पन्नवान् यस्य भवन्तः प्रायः योगदातृरूपेण सम्मुखीभवन्ति!

स्वस्य योगदानस्य उत्सवं कुर्वन्तु तथा च [web app] इत्यत्र गत्वा स्वमित्रैः अनुयायिभिः सह साझां कुर्वन्तु (https://firstcontributions.github.io/#social-share).

यदि भवतः किमपि साहाय्यस्य आवश्यकता अस्ति वा किमपि प्रश्नं अस्ति तर्हि भवान् अस्माकं slack दलं सम्मिलितुं शक्नोति। [slack दलेन सह सम्मिलितं कुर्वन्तु]। (https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w).

अधुना अन्येषु परियोजनासु योगदानं दातुं भवन्तं आरभामः। वयं परियोजनानां सूचीं संकलितवन्तः येषु सुलभाः विषयाः सन्ति येषु भवान् आरभुं शक्नोति। [web app परियोजनानां सूची] पश्यन्तु । (https://firstcontributions.github.io/#project-list).

### [अतिरिक्त सामग्री](additional-material/git_workflow_scenarios/additional-material.md)

## अन्येषां साधनानां उपयोगेन पाठ्यक्रमाः

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>एषा परियोजना समर्थिता अस्ति :</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
