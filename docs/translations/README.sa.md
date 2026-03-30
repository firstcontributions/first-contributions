[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _इदं [अन्यभाषासु](docs/translations/Translations.md) पठन्तु।_

# प्रथमयोगदानम् (First Contributions)

अस्य प्रकल्पस्य उद्देश्यं वर्तते यत् आरम्भकाः कथं स्वकीयं प्रथमं योगदानं कुर्युः इति सरलीकर्तुं मार्गदर्शनं च कर्तुम्। यदि भवान्/भवती प्रथमं योगदानं कर्तुमिच्छति तर्हि अधोदत्तान् सोपानान् अनुसरतु।

_यदि भवान्/भवती आज्ञापङ्क्तौ (command line) कुशलो नास्ति, तर्हि [अत्र चित्रमयसाधनैः (GUI tools) पाठानि सन्ति।](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />

#### यदि भवतः/भवत्याः सङ्गणके git नास्ति, तर्हि [तस्य संस्थापनं कुर्वन्तु (install it)](https://docs.github.com/en/get-started/quickstart/set-up-git)।

## इमं कोशं स्वखाते स्थापयन्तु (Fork this repository)

अस्य पृष्ठस्य उपरिभागे विद्यमानं 'fork' इति पिञ्जं नुदन्तः इमं कोशं स्वखाते स्थापयन्तु।
अनेन भवतः/भवत्याः खातमध्ये अस्य कोशस्य प्रतिलिपिः (copy) निर्मास्यते।

## कोशस्य प्रतिलिपिं सङ्गणके आनयन्तु (Clone the repository)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the repository" />

इदानीं तं प्रतिलिपीकृतं कोशं स्वसङ्गणके आनयन्तु। स्वस्य GitHub खाते गत्वा, तं कोशं उद्घाटयन्तु, 'Code' इति पिञ्जं नुदन्तु, ततः 'SSH' इति विभागं गत्वा _copy url to clipboard_ इति चिह्नं नुदन्तु।

कञ्चित् 'terminal' उद्घाट्य अधोलिखितां git आज्ञां चालयन्तु:

```bash
git clone "भवता/भवत्या प्रतिलिपीकृतं URL"
```

## नवीनां शास्त्रां (Branch) सृजन्तु

स्वसङ्गणके कोशस्य निर्देशिकां (directory) प्रति गच्छन्तु:

```bash
cd first-contributions
```

इदानीं `git switch` आज्ञया नवीनां शाखां सृजन्तु:

```bash
git switch -c भवतः_शाखायाः_नाम
```

उदाहरणम्:

```bash
git switch -c add-alonzo-church
```

## परिवर्तनानि कृत्वा तानि प्रतिबध्नन्तु (Commit changes)

इदानीं `Contributors.md` सञ्चिकां (file) कस्मिश्चित् पाठसम्पादके (text editor) उद्घाट्य तत्र स्वनाम योजयन्तु। सञ्चिकायाः आरम्भे अन्ते वा मा योजयन्तु, मध्ये कुत्रापि लिखन्तु। ततः सञ्चिकां सुरक्षितां (save) कुर्वन्तु।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

यदि भवान्/भवती `git status` इति आज्ञां चालयति, तर्हि परिवर्तनानि द्रक्ष्यति।

अधोलिखिताज्ञया तानि परिवर्तनानि स्वशाखायां योजयन्तु:

```bash
git add Contributors.md
```

इदानीं `git commit` आज्ञया तानि परिवर्तनानि प्रतिबध्नन्तु:

```bash
git commit -m "Contributors सूच्यां भवतः_नाम योजयन्तु"
```

## परिवर्तनानि GitHub प्रति प्रेषयन्तु (Push changes)

`git push` आज्ञया स्वपरिवर्तनानि प्रेषयन्तु:

```bash
git push -u origin भवतः_शाखायाः_नाम
```

## परिवर्तनानां समीक्षां प्रार्थयन्तु (Submit for review)

स्वकोशस्य GitHub पृष्ठे 'Compare & pull request' इति पिञ्जं द्रक्ष्यति। तत्र नुदन्तु।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

इदानीं pull request समर्पयन्तु।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

शीघ्रमेव अहं भवतां परिवर्तनानि मुख्यशाखायां (main branch) योजयिष्यामि। संयोजनानन्तरं भवान्/भवती सूचनापत्रं (notification) प्राप्स्यति।

---
**अभिनन्दनानि!** भवान्/भवती योगदानस्य मानककार्यप्रवाहमं (fork -> clone -> edit -> pull request) सफलीकृतवान्/सफलीकृतवती।
