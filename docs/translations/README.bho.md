# पहिल योगदान

ई प्रोजेक्ट के मकसद बा कि शुरुआती लोगन खातिर ओपन सोर्स में योगदान कइल आसान बनावल जा सके। अगर रउआ आपन पहिल योगदान देवे के सोच रहल बानी, त नीचे दिहल गइल स्टेप्स के फॉलो करीं।

_अगर रउआ कमांड लाइन (command line) के साथ सहज नइखीं, त [इहाँ जीयूआई (GUI) टूल्स के उपयोग करत ट्यूटोरियल्स बा।](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />

#### अगर रउआ मशीन पर git नइखे, त [एकरा के इंस्टॉल करीं](https://docs.github.com/en/get-started/quickstart/set-up-git)।

## ई रिपॉजिटरी के फोर्क (Fork) करीं

ई पेज के ऊपर दाहिने ओर "Fork" बटन पर क्लिक क के ई रिपॉजिटरी के फोर्क करीं।
एह से रउआ खाता में ई रिपॉजिटरी के एगो कॉपी बन जाई।

## रिपॉजिटरी के क्लोन (Clone) करीं

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the repository" />

अब अपने फोर्क कइल गइल रिपॉजिटरी के अपने मशीन पर क्लोन करीं। अपने गिटहब (GitHub) अकाउंट पर जाईं, फोर्क कइल रिपॉजिटरी खोलें, "Code" बटन पर क्लिक करीं, फिर "SSH" टैब पर क्लिक करीं आ "copy url to clipboard" आइकन पर क्लिक करीं।

अब टर्मिनल (terminal) खोलीं आ नीचे दिहल गइल git कमांड चलाविं:

```bash
git clone "url you just copied"
```

जहाँ "url you just copied" (बिना उद्धरण " " के) ई रिपॉजिटरी के यूआरएल (URL) ह (रउआ फोर्क)। यूआरएल प्राप्त करे खातिर पिछला स्टेप्स देखीं।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

उदाहरण खातिर:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

जहाँ `this-is-you` रउआ गिटहब यूजरनेम (username) ह। इहाँ रउआ गिटहब से `first-contributions` रिपॉजिटरी के कंटेंट अपने कंप्यूटर पर कॉपी कर रहल बानी।

## एगो ब्रांच (Branch) बनाविं

अपने कंप्यूटर पर रिपॉजिटरी डायरेक्टरी में जाईं (अगर रउआ पहिले से ओहिजा नइखीं):

```bash
cd first-contributions
```

अब `git switch` कमांड के उपयोग क के एगो नया ब्रांच बनाविं:

```bash
git switch -c your-new-branch-name
```

उदाहरण खातिर:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>अगर git switch के उपयोग करत समय कौनो गलती मिले, त इहाँ क्लिक करीं:</strong> </summary>

अगर "Git: `switch` is not a git command. See `git –help`" जइसन एरर मैसेज आवे, त एकर मतलब बा कि रउआ git के पुराना वर्जन यूज कर रहल बानी।

एह स्थिति में, `git checkout` के उपयोग करे के कोशिश करीं:

```bash
git checkout -b your-new-branch-name
```

</details>

## जरूरी बदलाव करीं आ ओकरा के कमिट (Commit) करीं

अब `Contributors.md` फाइल के कवनो टेक्स्ट एडिटर में खोलीं आ अपना नाम ओमें जोड़ीं। एकरा के फाइल के शुरू या अंत में मत जोड़ीं। बीच में कहीं भी डाल दीं। अब फाइल के सेव करीं।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

अगर रउआ प्रोजेक्ट डायरेक्टरी में जाईं आ `git status` कमांड चलाविं, त रउआ देखब कि कुछ बदलाव भइल बा।

अब `git add` कमांड के उपयोग क के ऊ बदलाव के ओ ब्रांच में जोड़ीं जवन रउआ अभी बनवले बानी:

```bash
git add Contributors.md
```

अब `git commit` कमांड के उपयोग क के ऊ बदलाव के कमिट करीं:

```bash
git commit -m "Add your-name to Contributors list"
```

`your-name` के जगह पर अपना नाम लिखीं।

## गिटहब (GitHub) पर बदलाव पुश (Push) करीं

`git push` कमांड के उपयोग क के अपना बदलाव के पुश करीं:

```bash
git push -u origin your-branch-name
```

`your-branch-name` के जगह पर ओ ब्रांच के नाम लिखीं जवन रउआ पहिले बनवले रहनी।

<details>
<summary> <strong>अगर पुश करत समय कौनो गलती मिले, त इहाँ क्लिक करीं:</strong> </summary>

- ### ऑथेंटिकेशन (Authentication) एरर
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  अपने अकाउंट के साथ SSH की (key) जनरेट आ कॉन्फिगर करे खातिर [गिटहब के ट्यूटोरियल](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) देखीं।

  साथ ही, रउआ 'git remote -v' चला के अपना रिमोट एड्रेस चेक कर सकत बानी।

  अगर ई कुछ अइसन देखाई देता:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>

  त एकरा के नीचे दिहल कमांड से बदल दीं:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  ना त रउआ से बार-बार यूजरनेम आ पासवर्ड पूछल जाई आ ऑथेंटिकेशन एरर मिली।
</details>

## अपना बदलाव के रिव्यु (Review) खातिर सबमिट करीं

अगर रउआ गिटहब पर अपना रिपॉजिटरी पर जाइब, त रउआ `Compare & pull request` बटन देखाई दी। ओ बटन पर क्लिक करीं।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

अब पुल रिक्वेस्ट (pull request) सबमिट करीं।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

जल्दिये हम रउआ सभे बदलाव के ई प्रोजेक्ट के मुख्य ब्रांच में मर्ज (merge) कर देब। जेना ही बदलाव मर्ज हो जाई, रउआ के ईमेल पर नोटिफिकेशन मिल जाई।

## अब आगे का?

बधाई हो! रउआ अभी स्टैंडर्ड _fork -> clone -> edit -> pull request_ वर्कफ़्लो पूरा कइली जवन रउआ अक्सर एगो योगदानकर्ता (contributor) के रूप में देखब!

अपना योगदान के जश्न मनावें आ अपने दोस्तन आ फॉलोअर्स के साथ शेयर करस [web app](https://firstcontributions.github.io/#social-share) पर जा के।

अगर रउआ अउरी प्रैक्टिस चाहत बानी, त [code contributions](https://github.com/roshanjossey/code-contributions) चेक करीं।

अब रउआ के दूसर प्रोजेक्ट्स में योगदान देवे खातिर शुरू कइल जाव। हमनी आसान इश्यूज (issues) वाला प्रोजेक्ट्स के लिस्ट तैयार कइले बानी। [प्रोजेक्ट्स के लिस्ट वेब ऐप में](https://firstcontributions.github.io/#project-list) चेक करीं।

### [अतिरिक्त सामग्री](docs/additional-material/git_workflow_scenarios/additional-material.md)

## अन्य टूल्स के उपयोग करत ट्यूटोरियल्स

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
