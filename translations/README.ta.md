[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# முதல் பங்களிப்புகள்

இது கடினம். நீங்கள் ஏதாவது முதல் தடவை செய்யும் போது அது எப்போதும் கடினம். குறிப்பாக நீங்கள் இங்கு குழுவாக ஒத்துழைக்கும்போது, தவறு செய்வது என்பது சாதாரண விஷயமே. முதல் தடவை பங்களிப்போர் கற்றுக்கொள்ளவும் மேலும் பங்களிப்பு செய்வதை இலகுவாக்குவதே எங்களுக்கு தேவையாக உள்ளது.

கட்டுரைகளைப் படிப்பதும், பயிற்சிகளைப் பார்ப்பதும் உதவக்கூடும், ஆனால் நடைமுறைச் சூழலில் விஷயங்களைச் செய்வதை விட சிறந்தது என்ன? இந்த திட்டம் வழிகாட்டுதல்களை வழங்குவதையும், ஆரம்பநிலை பங்களிப்பாளர்களை அவர்களின் முதல் பங்களிப்பை எளிதாக்குவதையும் நோக்கமாகக் கொண்டுள்ளது. உங்கள் முதல் பங்களிப்பை வழங்க விரும்பினால், கீழே உள்ள வழிமுறைகளை பின்பற்றவும்.

#### *command line உங்களுக்கு வசதியாக இல்லை என்றால், [இங்கே GUI tools ஐ பயன்படுத்தி பயிற்சிகள் உள்ளன.]( #tutorials-using-other-tools )*

<img align="right" width="300" src="../assets/fork.png" alt="இந்த repository ஐ fork செய்யவும்" />

உங்கள் கணினியில் git இல்லை என்றால், [install செய்யவும்](https://help.github.com/articles/set-up-git/).

## இந்த repository ஐ fork செய்தல்


இந்த பக்கத்தின் மேலே உள்ள fork பொத்தானைக் கிளிக் செய்வதன் மூலம் செயட்படுத்தலாம்.
இது உங்கள் account இல் ஒரு copy ஐ உருவாக்கும்.

## இந்த repository ஐ clone செய்தல்

<img align="right" width="300" src="../assets/clone.png" alt="இந்த repository ஐ clone செய்யவும்" />

இப்போது உங்கள் கணினியில் fork செய்யப்பட்ட repository ஐ clone செய்யவும். உங்கள் GitHub கணக்கிற்குச் சென்று, forked செய்யப்பட்ட repository ஐ open செய்து clone பொத்தானைக் கிளிக் செய்து copy to clipboard கிளிக் செய்வதன் மூலம் நிறைவேற்றலாம்.  

terminal ஐ open செய்து  பின்வரும் git கட்டளையை இயக்கவும்:

```
git clone "நீங்கள் copy செய்த url"
```

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />


உதாரணத்திற்கு:

```
git clone https://github.com/இது நீங்கள்/first-contributions.git
```

இங்கு `இது நீங்கள்` என்பது GitHub username என்பதாகும். இதன் மூலம் நீங்கள் first-contributions repository இன் பிரதி ஒன்றை உங்கள் GitHub கணக்கில் செயட்படுத்துகிறீர்கள்.

## கிளையொன்றை  உருவாக்குதல்

repository directory இட்கு செல்லவும்(நீங்கள் ஏற்கனவே இல்லையென்றால்):

```
cd first-contributions
```


இப்போது `git checkout` கட்டளையைப் பயன்படுத்தி ஒரு கிளையை உருவாக்கவும்:

```
git checkout -b <add-your-new-branch-name>
```

உதாரணத்திற்கு:

```
git checkout -b add-luke-oliff
```

(கிளையின் பெயருக்கு அதில் *add* சேர்க்க வேண்டிய அவசியமில்லை, ஆனால் இது ஒரு நியாயமான விஷயம், ஏனெனில் இந்த கிளையின் நோக்கம் உங்கள் பெயரை ஒரு பட்டியலில் சேர்ப்பதுதான்.)

## தேவையான மாற்றங்களைச் செய்து அந்த மாற்றங்களை commit செய்யுங்கள்

இப்போது text editor இல் `Contribitors.md` கோப்பைத் திறந்து, அதில் உங்கள் பெயரைச் சேர்க்கவும். கோப்பின் தொடக்கத்திலோ அல்லது முடிவிலோ இதைச் சேர்க்க வேண்டாம். இடையில் எங்கும் வைக்கவும். இப்போது, ​​கோப்பை சேமிக்கவும்.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

நீங்கள் project directory சென்று `git status` இயக்கினால், மாற்றங்கள் இருப்பதை நீங்கள் காண்பீர்கள்.


`git add` கட்டளையைப் பயன்படுத்தி நீங்கள் உருவாக்கிய கிளையில் அந்த மாற்றங்களைச் சேர்க்கவும்:

```
git add Contributors.md
```

இப்போது `git commit` கட்டளையைப் பயன்படுத்தி அந்த மாற்றங்களைச் செய்யுங்கள்:

```
git commit -m "Add <உங்கள்_பெயர்> to Contributors list"
```

`உங்கள்_பெயர்` என்ற இடத்தில் உங்கள் பெயரை கொடுங்கள்.

## மாற்றங்களை GitHub இட்கு push செய்தல்

`git push` கட்டளையைப் பயன்படுத்தி உங்கள் மாற்றங்களைத் தள்ளுங்கள்:

```
git push origin <add-your-branch-name>
```


`<add-your-branch-name>` ஐ நீங்கள் முன்பு உருவாக்கிய கிளையின் பெயருடன் மாற்றுங்கள்.

## உங்கள் மாற்றங்களை மதிப்பாய்வுக்கு சமர்ப்பிக்கவும்


GitHub இல் உள்ள உங்கள் களஞ்சியத்திற்குச் சென்றால், `Compare & pull request` கோரிக்கை பொத்தானைக் காண்பீர்கள். அந்த பொத்தானைக் கிளிக் செய்க.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

இப்போது இழுக்கும் கோரிக்கையை சமர்ப்பிக்கவும்.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

விரைவில் உங்கள் எல்லா மாற்றங்களையும் இந்த திட்டத்தின் முதன்மை கிளையில் இணைக்கப்படும். மாற்றங்கள் ஒன்றிணைக்கப்பட்டவுடன் உங்களுக்கு அறிவிப்பு மின்னஞ்சல் கிடைக்கும்.

## இங்கிருந்து எங்கு செல்வது?

வாழ்த்துக்கள்! நீங்கள் ஒரு பங்களிப்பாளராக அடிக்கடி சந்திக்கும் _fork -> clone -> edit -> PR_ பணிப்பாய்வு முடித்துவிட்டீர்கள்.


உங்கள் பங்களிப்பைக் கொண்டாடுங்கள் மற்றும் உங்கள் நண்பர்கள் மற்றும் பின்தொடர்பவர்களுடன் [web app](https://roshanjossey.github.io/first-contributions/#social-share) சென்று பகிர்ந்து கொள்ளுங்கள்.

உங்களுக்கு ஏதேனும் உதவி தேவைப்பட்டால் அல்லது ஏதேனும் கேள்விகள் இருந்தால் எங்கள் slack team இல் இணையலாம். [Join our slack crew](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

இப்போது மற்ற திட்டங்களுக்கு பங்களிப்பதன் மூலம் தொடங்குவோம். நீங்கள் தொடங்கக்கூடிய எளிதான சிக்கல்களுடன் திட்டங்களின் பட்டியலை நாங்கள் தொகுத்துள்ளோம். பாருங்கள் [the list of projects in the web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [கூடுதல் வளங்கள்](../additional-material/git_workflow_scenarios/additional-material.md)

## பிற கருவிகளைப் பயன்படுத்தி பயிற்சிகள்

| <a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gitkraken-tutorial.md"><img alt="GitKraken" src="./assets/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [GitHub Desktop](github-desktop-tutorial.md)                 | [Visual Studio 2017](github-windows-vs2017-tutorial.md)      | [GitKraken](gitkraken-tutorial.md)                           | [Visual Studio Code](github-windows-vs-code-tutorial.md)     | [Atlassian Sourcetree](sourcetree-macos-tutorial.md)         | [IntelliJ IDEA](github-windows-intellij-tutorial.md)         |
