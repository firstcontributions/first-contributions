[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# प्रथम योगदान  

ई परियोजना नवका लोकसभ केँ अपन पहिल योगदान करबाक मार्ग सरल बनाबय आ गाइड करबाक हेतु बनाओल गेल अछि।  
जँ अहाँ अपन पहिल योगदान करऽ चाहैत छी, तँ नीचाँ देल गेल चरणसभकेँ अनुसरण करू।  

_जँ अहाँ कमाण्ड लाइनमे सहज नहि छी, तँ [ई GUI टूल्सक प्रयोग करबाक ट्युटोरियल्स](#tutorials-using-other-tools) देखू।_  

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />  

#### जँ अहाँक मशीनमे git नहि छै, [एतय सँ git install करू](https://docs.github.com/en/get-started/quickstart/set-up-git)।  

## ई repository केँ Fork करू  

पृष्ठक ऊपर देल गेल fork बटन पर क्लिक करू।  
एहि सँ ई repository कऽ एकटा नकल अहाँक GitHub accountमे बनि जायत।  

## Repository केँ Clone करू  

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />  

अब अहाँ अपन forked repository केँ अपन मशीन पर clone करबाक अछि।  
GitHub account पर जाउ, forked repository खोलू, _Code_ बटन पर क्लिक करू, SSH टैब चुनू, आ _copy url_ आइकन पर क्लिक करू।  

Terminal खोलू आ ई git आदेश चलाउ:  

```bash
git clone "url you just copied"
```  

जहाँ `"url you just copied"` (बिना उद्धरण चिन्ह) अहाँक forked repository कऽ url थिक।  

उदाहरण:  

```bash
git clone git@github.com:this-is-you/first-contributions.git
```  

जहाँ `this-is-you` अहाँक GitHub username थिक।  

## Branch बनाउ  

Repository directory मे जाउ:  

```bash
cd first-contributions
```  

अब एकटा branch बनाउ:  

```bash
git switch -c your-new-branch-name
```  

उदाहरण:  

```bash
git switch -c add-alonzo-church
```  

(जँ git switch नहि चलैत अछि तँ `git checkout -b your-new-branch-name` प्रयुक्त करू।)  

## बदलाव करू आ commit करू  

`Contributors.md` फाइल खोलू, अपन नाम उसमें जोड़ू (शुरू अथवा अंत मे नहि, बीचमे कहीं जोड़ू)।  
फाइल save करू।  

बदलाव add करू:  

```bash
git add Contributors.md
```  

Commit करू:  

```bash
git commit -m "Add your-name to Contributors list"
```  

`your-name` केँ अपन नाम सँ बदलि दियौ।  

## GitHub पर push करू  

```bash
git push -u origin your-branch-name
```  

जहाँ `your-branch-name` अहाँ बनाओल गेल branch कऽ नाम थिक।  

(जँ authentication error भेटत तँ personal access token अथवा SSH key प्रयोग करू।)  

## Pull Request बनाउ  

GitHub repository पर `Compare & pull request` बटन पर क्लिक करू।  
Pull request submit करू।  

थोड़ेक समयक बाद अहाँक बदलाव main branch मे merge भऽ जायत आ अहाँक ईमेल पर notification भेटत।  

## एतय सँ आगाँ की?  

बधाई! अहाँ _fork → clone → edit → pull request_ workflow सफलतापूर्वक पूरा कऽ लेलहुँ। 🎉  

अहाँ अपन योगदान केँ [web app](https://firstcontributions.github.io/#social-share) पर share कऽ सकैत छी।  

जँ अहाँ आरो अभ्यास करऽ चाहैत छी, तँ [code contributions](https://github.com/roshanjossey/code-contributions) देखू।  
ओहिठाम beginner-friendly project सभक सूची सेहो भेटत।  

---

## अन्य टूल्स सँ ट्युटोरियल्स  

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |  
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)  | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md) |  

---
