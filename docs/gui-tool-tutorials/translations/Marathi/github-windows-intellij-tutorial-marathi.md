[![मुक्त स्रोत प्रेम](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![परवाना: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![ओपन सोर्स हेल्पर्स](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# प्रथम योगदान

| <img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" width="40"> | IntelliJ IDEA |
| --- | --- |

पहिल्यांदा काहीतरी करणे अवघड असते. विशेषतः इतरांसोबत काम करताना चुका करणे सहज वाटत नाही. पण ओपन सोर्स म्हणजे सहकार्याने एकत्र काम करणे. नवीन ओपन-सोर्स योगदानकर्त्यांना पहिल्यांदा शिकणे आणि योगदान देणे सोपे व्हावे, हा आमचा उद्देश आहे.

लेख वाचणे आणि ट्युटोरियल पाहणे उपयुक्त ठरू शकते; पण काही बिघडवण्याची चिंता न करता स्वतः करून पाहण्यापेक्षा चांगले काय? या प्रकल्पाचे उद्दिष्ट मार्गदर्शन देणे आणि नव्या व्यक्तींना त्यांचे पहिले योगदान देण्याचा मार्ग सोपा करणे आहे. लक्षात ठेवा: तुम्ही जितके निवांत असाल तितके चांगले शिकाल. तुम्हाला तुमचे पहिले योगदान द्यायचे असल्यास, खालील सोप्या पायऱ्या अनुसरा. हे मजेदार असेल, याची आम्ही खात्री देतो.

तुमच्या संगणकावर IntelliJ IDEA नसल्यास, ते [स्थापित करा](https://www.jetbrains.com/idea/download/#section=windows).

**टीप:** हे ट्युटोरियल Windows 10 संगणकावर IntelliJ IDEA (आवृत्ती 2019.3.2) वापरून तयार केले आहे. पुढे काही कीबोर्ड शॉर्टकट वापरले आहेत. ते इतर ऑपरेटिंग सिस्टीमवर (macOS/Linux) वेगळे असू शकतात.

## हे रेपॉजिटरी फोर्क करा

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="हे रेपॉजिटरी फोर्क करा" />

या पानाच्या वरच्या उजव्या बाजूला असलेल्या `Fork` बटणावर क्लिक करून हे रेपॉजिटरी फोर्क करा. यामुळे तुमच्या GitHub खात्यात या रेपॉजिटरीची एक प्रत तयार होईल.

GitHub तुमच्या रेपॉजिटरीचा आणि ज्यावरून तुम्ही फोर्क केले त्या रेपॉजिटरीचा संबंध जपून ठेवते. तुमच्या रेपॉजिटरीकडे तुम्ही कामाची प्रत म्हणून पाहू शकता.

बहुतेक उच्च-स्तरीय GitHub रेपॉजिटरींमध्ये (म्हणजे दुसऱ्या रेपॉजिटरीतून फोर्क न केलेल्या) काही मोजके लोक थेट बदल कमिट करू शकतात. इतर योगदानकर्त्यांनी रेपॉजिटरी फोर्क करून त्यात बदल करायचे आणि मग ते बदल मूळ रेपॉजिटरीत विलीन करण्याची विनंती करण्यासाठी Pull Request तयार करायची असते. वरच्या रेपॉजिटरीचा प्रशासक बदल मंजूर केल्यास ते विलीन केले जातील आणि तुम्हाला लगेच प्रसिद्धी व यश मिळेल! हे कसे करायचे ते पुढे पाहू.

## तुमची रेपॉजिटरी क्लोन करा

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="ही रेपॉजिटरी क्लोन करा" />

पुढची पायरी म्हणजे बदल सुरू करण्यासाठी तुमची रेपॉजिटरी तुमच्या संगणकावर क्लोन करणे. IntelliJ IDEA ला तुमच्या रेपॉजिटरीचा URL लागतो; म्हणून `Clone` बटणावर आणि नंतर `Copy to clipboard` चिन्हावर क्लिक करा.

**काळजीपूर्वक:** नवीन योगदानकर्ते अनेकदा तुमची स्वतःची रेपॉजिटरी क्लोन करण्याऐवजी ज्या रेपॉजिटरीवरून फोर्क केले ती क्लोन करतात. ब्राउझरच्या address bar मध्ये तपासा की तुम्ही तुमचीच रेपॉजिटरी क्लोन करत आहात.

आता IntelliJ IDEA उघडा.

IntelliJ IDEA मध्ये आधीपासून असलेली रेपॉजिटरी checkout (Git मध्ये clone) करता येते आणि डाउनलोड केलेल्या डेटावर आधारित नवीन प्रकल्प तयार करता येतो.

मुख्य मेनूमध्ये `VCS | Get from Version Control` निवडा. कोणताही प्रकल्प उघडला नसेल, तर Welcome स्क्रीनवरील `Get from Version Control` वर क्लिक करा.

`Get from Version Control` संवादपेटीत तुम्हाला क्लोन करायच्या दूरस्थ रेपॉजिटरीचा URL द्या. दूरस्थ रेपॉजिटरीशी जोडणी होऊ शकते का हे तपासण्यासाठी `Test` वर क्लिक करू शकता. किंवा डावीकडील VCS hosting service निवडा. निवडलेल्या सेवेत तुम्ही आधीच लॉग इन असाल, तर उपलब्ध रेपॉजिटरींची यादी सुचवली जाईल.

`Clone` वर क्लिक करा. क्लोन केलेल्या स्रोतांवर आधारित IntelliJ IDEA प्रकल्प तयार करायचा असल्यास, पुष्टीकरण संवादपेटीत `Yes` क्लिक करा. Git root mapping प्रकल्पाच्या root वर आपोआप सेट होईल.

तुमच्या प्रकल्पात submodules असतील तर ते देखील क्लोन होऊन प्रकल्प root म्हणून आपोआप नोंदवले जातील.

**महत्त्वाचे:** मूळ रेपॉजिटरी नव्हे, तर फोर्क केलेली रेपॉजिटरी निवडली आहे याची खात्री करा; अन्यथा हे काम करणार नाही.

## ब्रँच तयार करा

Git मध्ये branching ही प्रभावी यंत्रणा आहे. उदाहरणार्थ, नवीन feature वर काम करायचे असल्यास किंवा रिलीजसाठी codebase ची ठराविक स्थिती गोठवायची असल्यास, मुख्य development line पासून वेगळे काम करता येते.

IntelliJ IDEA मध्ये ब्रँचशी संबंधित सर्व क्रिया `Git Branches` popup मधून केल्या जातात. तो उघडण्यासाठी Status bar मधील Git widget वर क्लिक करा किंवा `Ctrl+Shift+\`` दाबा.

सध्या checkout केलेल्या ब्रँचचे नाव Status bar मधील Git widget मध्ये दिसते.

ब्रँचच्या popup मध्ये `New Branch` निवडा.

उघडणाऱ्या संवादपेटीत ब्रँचचे नाव द्या. त्या ब्रँचवर जायचे असल्यास `Checkout branch` पर्याय निवडलेला आहे याची खात्री करा.

नवीन ब्रँच सध्याच्या `HEAD` पासून सुरू होईल. सध्याच्या ब्रँचच्या `HEAD` ऐवजी आधीच्या commit पासून ब्रँच सुरू करायची असल्यास, Version Control tool window मधील `Log` tab मध्ये (`Alt+9`) तो commit निवडा आणि context menu मधून `New Branch` निवडा.

## आवश्यक बदल करा

`Contributors.md` उघडा आणि फाइलमध्ये कुठेही तुमचे नाव जोडा. या फाइलमध्ये GFM (GitHub Flavored Markdown) आहे, जो `markdown` syntax चा एक प्रकार आहे.

syntax योग्य ठेवण्यासाठी इतर योगदानकर्त्यांपैकी एका ओळीची प्रत करा आणि त्यात तुमचे नाव बदला—ती थोडी काटेकोर असू शकते.

## बदल GitHub वर Commit आणि Push करा

Version Control tool window मधील `Local Changes` tab मध्ये तुम्हाला commit करायच्या फाइल्स किंवा संपूर्ण changelist निवडा; नंतर `Ctrl+K` दाबा किंवा toolbar वरील `Commit` बटणावर क्लिक करा.

उघडणारी `Commit Changes` संवादपेटी मागील commit नंतर बदललेल्या सर्व फाइल्स आणि नव्याने जोडलेल्या, version control मध्ये नसलेल्या फाइल्स दाखवते.

अर्थपूर्ण commit message लिहा.

अलीकडील commit messages च्या यादीतून निवडण्यासाठी `Commit Message history` वर क्लिक करा किंवा `Ctrl+M` दाबा.

commit push करण्यापूर्वी तुम्ही नंतरही commit message संपादित करू शकता.

`Ctrl+Shift+K` दाबा किंवा मुख्य मेनूमधून `VCS | Git | Push` निवडा. `Push Commits` संवादपेटी उघडेल. त्यात सर्व Git repositories (अनेक repositories असलेल्या प्रकल्पांसाठी) आणि शेवटच्या push नंतर सध्याच्या ब्रँचमध्ये झालेल्या commits दिसतील.

## तुमचे बदल पुनरावलोकनासाठी पाठवा

या टप्प्यावर तुमचा बदल पूर्ण झाला आहे, पण तो अजून फक्त तुमच्या रेपॉजिटरीत आहे. हा टप्पा तुमचा बदल मूळ रेपॉजिटरीत विलीन करण्याची विनंती प्रशासकाकडे कशी पाठवायची ते दाखवतो.

GitHub वरील तुमच्या रेपॉजिटरीत नवीन ब्रँचच्या सूचनेजवळ `Compare & pull request` बटण दिसेल. त्या बटणावर क्लिक करा.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="pull request तयार करा" />

आता Pull Request submit करा.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="pull request submit करा" />

लवकरच तुमचे बदल या प्रकल्पाच्या मुख्य ब्रँचमध्ये विलीन केले जातील. बदल विलीन झाल्यावर तुम्हाला email notification मिळेल.

## पुढे काय?

अभिनंदन! योगदानकर्ता म्हणून तुम्हाला वारंवार भेटणारी नेहमीची _fork -> clone -> edit -> PR_ प्रक्रिया तुम्ही पूर्ण केली आहे!

[web app](https://firstcontributions.github.io#social-share) वर जाऊन तुमचे योगदान साजरे करा आणि मित्र व followers सोबत शेअर करा.

### [अतिरिक्त सामग्री](../additional-material/git_workflow_scenarios/additional-material.md)

## इतर साधनांसाठी ट्युटोरियल

[मुख्य पानावर परत जा](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
