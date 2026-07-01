[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# प्रथम योगदान

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Git Bash Edition |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |

यह कठीण आहे. जेव्हा तुम्ही पहिल्यांदा काहीतरी करता तेव्हा ते नेहमीच कठीण असते. खासकरून जेव्हा तुम्ही सहकार्य करत असता, तेव्हा चुका करणे ही काही सोपी गोष्ट नाही. पण ओपन सोर्सचा अर्थच सहकार्य आणि एकत्र काम करणे हा आहे. नवीन ओपन-सोर्स योगदानकर्त्यांच्या शिकण्याची आणि पहिल्यांदा योगदान देण्याची पद्धत आम्हाला सोपी करायची होती.

लेख वाचणे आणि ट्यूटोरियल पाहणे उपयुक्त ठरू शकते, पण काहीही न बिघडवता प्रत्यक्षात काम करण्यापेक्षा उत्तम काय असू शकते. या प्रकल्पाचा उद्देश मार्गदर्शन प्रदान करणे आणि नवशिक्यांसाठी आपले पहिले योगदान देण्याची पद्धत सोपी करणे हा आहे. लक्षात ठेवा की तुम्ही जितके जास्त सहज असाल, तितकेच तुम्ही चांगले शिकाल. जर तुम्हाला तुमचे पहिले योगदान द्यायचे असेल तर फक्त खाली दिलेल्या सोप्या चरणांचे पालन करा. आम्ही तुम्हाला वचन देतो, हे मजेदार असेल.

जर तुमच्याकडे विंडोज मशीनवर Git Bash नसेल, [तर ते इंस्टॉल करा](https://git-scm.com/download/win)।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## या रिपोजिटरीला फोर्क करा

या पेजच्या वरच्या उजव्या बाजूला दिलेल्या फोर्क बटणावर क्लिक करून या रिपोला फोर्क करा.
यामुळे तुमच्या खात्यात या रिपोची एक कॉपी तयार होईल.

## रिपोजिटरी क्लोन करा

आता हा रेपो तुमच्या मशीनवर क्लोन करा.

महत्त्वाचे: मूळ रेपो क्लोन करू नका. तुमच्या फोर्कवर जा आणि तो क्लोन करा.

रेपो क्लोन करण्यासाठी, "कोड" वर क्लिक करा आणि नंतर खालील स्ट्रिंग कॉपी करा.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

तुम्ही आत्ताच जे git bash ॲप्लिकेशन डाउनलोड केले आहे ते उघडा. जर ते विंडोज मशीनवर असेल तर ते खालील प्रतिमेसारखे दिसेल.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />

या कमांडचा वापर करून त्या फोल्डरवर जा जिथे तुम्हाला हा प्रोजेक्ट सेव्ह करायचा आहे

`cd <folder>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />

या कमांडचा वापर करून रिपॉजिटरी क्लोन करण्यासाठी वरील चरणात तुम्ही कॉपी केलेल्या स्ट्रिंगचा वापर करा

`git clone <repo-url>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

त्या निर्देशिकेवर (directory) जा जिथे रेपो आहे आणि तुमचे बदल करण्यासाठी ते व्हीएस कोड (VS Code) वर उघडा.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## एक शाखा (branch) तयार करा

आता या सोप्या कमांडचा वापर करून एक शाखा तयार करा. ही कमांड केवळ तुमच्यासाठी एक शाखा तयार करत नाही तर तुम्हाला त्या शाखेवर स्विच करण्याची सुविधाही देते.
