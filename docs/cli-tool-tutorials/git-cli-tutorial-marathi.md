[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# प्रथम योगदान

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Git Bash आवृत्ती |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |

सुरुवात करणे नेहमीच कठीण असते, विशेषतः जेव्हा आपण एखाद्या प्रकल्पात योगदान देत असता. चुका होणे नैसर्गिक आहे. पण ओपन सोर्स म्हणजे सहकार्य, शिकणे आणि एकत्र काम करणे.  
या प्रकल्पाचा उद्देश नवशिक्यांना मार्गदर्शन देणे आणि त्यांचे पहिले योगदान सुलभ करणे हा आहे.

वाचणे आणि ट्यूटोरियल पाहणे उपयुक्त ठरते, पण प्रत्यक्ष काम करून शिकणे अधिक फायदेशीर आहे. खालील सोप्या टप्प्यांचे पालन करा आणि तुमचे पहिले योगदान मजेदार ठरेल!

जर तुमच्याकडे विंडोजवर Git Bash नसेल, [तर ते इथे डाउनलोड करा](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## या रेपोचे Fork करा

वरील उजव्या बाजूस असलेला **Fork** बटण दाबा.  
यामुळे ह्या रेपोची कॉपी तुमच्या GitHub अकाउंटमध्ये तयार होईल.

## रेपो Clone करा

आता या रेपोची कॉपी तुमच्या संगणकावर क्लोन करा.

**महत्वाचे:** मूळ रेपो क्लोन करू नका. तुमच्या Fork वर जा आणि ते क्लोन करा.

**Clone करण्यासाठी:**
1. "Code" वर क्लिक करा आणि URL कॉपी करा.
2. Git Bash उघडा.
3. ज्या फोल्डरमध्ये प्रोजेक्ट सेव्ह करायचे आहे त्या फोल्डरमध्ये जा:

```bash
cd <folder-path>
```

4. रेपो क्लोन करा:

```bash
git clone <repo-url>
```

5. रेपोच्या डायरेक्टरीमध्ये जा आणि VS Code मध्ये उघडा:

```bash
cd <repo-folder>
code .
```

## नवीन Branch तयार करा

खालील कमांड वापरून नवीन branch तयार करा आणि त्यावर जा:

```bash
git checkout -b <branch-name>
```

उदाहरणार्थ:  
```bash
git checkout -b add-your-name
```

## आवश्यक बदल करा आणि Commit करा

`Contributors.md` फाइल उघडा, पेजच्या खाली स्क्रोल करा आणि तुमचे नाव जोडा.  
उदाहरण:

```markdown
[तुमचे नाव](https://github.com/तुमचा-गिटहब-यूजरनेम)
```

बदल तपासण्यासाठी:

```bash
git status
```

बदल Stage करा:

```bash
git add Contributors.md
```

Commit करा:

```bash
git commit -m "Add your-name to Contributors list"
```

Commit झाले का हे पाहण्यासाठी:

```bash
git log --oneline
```

## GitHub वर Push करा

```bash
git push origin <branch-name>
```

## Pull Request तयार करा

GitHub वर आपल्या Fork मध्ये जा, **Compare & pull request** बटण क्लिक करा आणि PR सबमिट करा.  

तुमचे बदल Merge झाल्यानंतर तुम्हाला ईमेल नोटिफिकेशन मिळेल.

## पुढे काय करावे?

अभिनंदन! तुम्ही `fork -> clone -> edit -> PR` वर्कफ्लो पूर्ण केला आहे.  
आता तुम्ही तुमच्या योगदानाचा आनंद घ्या आणि [वेब अ‍ॅपवर](https://firstcontributions.github.io#social-share) शेअर करा.

अधिक मदतीसाठी किंवा प्रश्नांसाठी [Slack टीममध्ये सहभागी व्हा](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

### [अधिक माहिती](../additional-material/git_workflow_scenarios/additional-material.md)

[मुख्य पृष्ठावर परत जा](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
