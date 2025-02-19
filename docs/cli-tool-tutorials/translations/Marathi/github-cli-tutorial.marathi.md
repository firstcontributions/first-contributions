
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# प्रथम योगदान

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

हे आमच्यासाठी मार्गदर्शक आहे, टर्मिनलच्या अभ्यासकांसाठी, ज्यांना टर्मिनलमध्ये सर्व काही करायचे आहे आणि [Github-CLI](https://cli.github.com/) बद्दल धन्यवाद, त्यांना ते मिळू शकते, तुमचे पहिले योगदान लक्षात ठेवा मजेशीर, फायद्याचे आणि पुढे जाण्यासाठी प्रेरक!

हे मार्गदर्शक थोडे अधिक आव्हानात्मक आहे कारण आम्ही कोणताही ग्राफिकल इंटरफेस वापरत नाही, परंतु तरीही ते खरोखर मजेदार आहे आणि आपण निश्चितपणे अनुसरण करू शकता!

पहिली आवश्यकता आहेः

- Git स्थापित ([Git] कसे स्थापित करावे (https://git-scm.com/downloads))
- Github खाते

आता आम्हाला अधिकृत कागदपत्रांचे अनुसरण करून आमच्या सिस्टममध्ये `github-cli` टूल स्थापित करणे आवश्यक आहे

त्यानंतर, आम्हाला CLI वर लॉग इन करणे आवश्यक आहे, म्हणून ही आज्ञा प्रविष्ट करा:

```bash
gh auth login
```

सूचनांचे अनुसरण करा आणि आम्ही तयार आहोत!

# या भांडाराचा फोर्क करा

ही कमांड चालवणे तितकेच सोपे आहे:

```bash
gh repo fork firstcontributions/first-contributions
```

**महत्त्वाचे: तुम्हाला हे देखील क्लोन करायचे असल्यास ते तुम्हाला सूचित करेल, "होय" निवडा**

# तुमची शाखा तयार करा

आम्ही ही पायरी `git` सह करू, म्हणून ही आज्ञा तुमच्या नावाने पुनर्नामित करून प्रविष्ट करा, उदाहरणार्थ:(जॉन-डूई येथे तुमचे नाव टाका

```bash
git switch -c add-जॉन-डूई
```

# आवश्यक बदल करा आणि ते बदल `किट` करा

आता तुम्ही मजकूर संपादकामध्ये `Contributors.md` फाईल उघडू शकता आणि त्यात तुमचे नाव जोडू शकता. तुमचे नाव सुरुवातीपासून शेवटच्या दरम्यान कुठेही ठेवा, नंतर फाइल सेव्ह करा.

प्रोजेक्ट डिरेक्टरीमध्ये `git status` कार्यान्वित करा आणि तुम्हाला बदल दिसतील.


ते बदल तुम्ही 'git add' कमांड वापरून तयार केलेल्या शाखेत जोडा:
`git add contributors.md`

आता ते बदल `git कमिट` कमांड वापरून करा: `git commit -m "Add your-name to Contributors list` तुमच्या नावाने `your-name` बदला.

# Github मध्ये बदल पुश करा

'git push' कमांड वापरून तुमचे बदल पुश करा:

```bash
git push origin -u your-branch-name
```

तुम्ही आधी तयार केलेल्या शाखेच्या नावाने `your-branch-name` बदला.

<details><summary> <strong>पुश करताना तुम्हाला काही त्रुटी आढळल्यास, येथे क्लिक करा:</strong></summary></details>

- ### प्रमाणीकरण त्रुटी
        रिमोट: 13 ऑगस्ट 2021 रोजी पासवर्ड ऑथेंटिकेशनसाठी सपोर्ट काढून टाकण्यात आला. कृपया त्याऐवजी वैयक्तिक प्रवेश टोकन वापरा. रिमोट: अधिक माहितीसाठी कृपया https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ पहा. घातक: 'https://github.com//first-contrib.git/' साठी प्रमाणीकरण अयशस्वी
  [तुमच्या खात्यासाठी एसएसएच की तयार आणि कॉन्फिगर करण्यावर गिटहबचे ट्यूटोरियल](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

# तुमचे बदल पुनरावलोकनासाठी सबमिट करा

आता ही कमांड आमच्या रेपोच्या निर्देशिकेत चालवल्याने आम्हाला पुनरावलोकनासाठी पुल विनंती तयार करण्याची अनुमती मिळेल:

```bash
gh pr create --repo firstcontributions/first-contributions
```

यानंतर पुल विनंती सबमिट करा.

तुमची नमूद पुल विनंती कृतीत पाहण्यासाठी तुम्ही `gh status` कमांड वापरू शकता.

## इथून कुठे जायचं?

अभिनंदन! तुम्ही नुकतेच मानक फोर्क -> क्लोन -> संपादन -> पुल विनंती वर्कफ्लो पूर्ण केले आहे ज्याचा तुम्हाला अनेकदा एक योगदानकर्ता म्हणून सामना करावा लागेल!

तुमचे योगदान साजरे करा आणि [वेब ॲप](https://firstcontributions.github.io/#social-share) ला भेट देऊन ते तुमच्या मित्र आणि अनुयायांसह शेअर करा.

तुम्हाला काही मदत हवी असल्यास किंवा काही प्रश्न असल्यास, तुम्ही आमच्या स्लॅक टीममध्ये सामील होऊ शकता. [स्लॅक टीममध्ये सामील व्हा](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

आता आपण इतर प्रकल्पांमध्ये योगदानासह प्रारंभ करूया. आम्ही सोप्या समस्यांसह प्रकल्पांची सूची संकलित केली आहे ज्यावर तुम्ही सुरुवात करू शकता. [वेब ॲपमधील प्रकल्पांची यादी](https://firstcontributions.github.io/#project-list पहा).

### [अतिरिक्त साहित्य](additional-material/git_workflow_scenarios/additional-material.md)

##इतर साधनांचा वापर करून शिकवण्या

[मुख्य पृष्ठावर परत](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
