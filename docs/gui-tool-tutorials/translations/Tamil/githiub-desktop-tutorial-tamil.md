[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# முதல் பங்களிப்புகள்

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Git Bash பதிப்பு |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |

புதியதாக எதையாவது செய்யும்போது அது கடினமாக இருக்கும். குறிப்பாக ஒத்துழைவாக வேலை செய்யும்போது, பிழைகள் செய்யப்படுவது அவசியம். ஆனால் ஓப்பன்-சோர்ஸ் என்பது ஒரே குழுவாக சூழ்நிலையாக்கி இணைந்து வேலை செய்வதே ஆகும். புதிய ஓப்பன்-சோர்ஸ் பங்களிப்பாளர்கள் முதல் முறையாக எவ்வாறு கற்றுக்கொள்கிறார்கள் மற்றும் பங்களிக்கிறார்கள் என்பது எளிமையாக நடக்க வேண்டும் தன்னெருவாகும் — இதற்காக இந்தத் திட்டம் வழிகாட்டுதல்களையும், புதியவர்களுக்கு முதல் பங்களிப்பை எளிதாக்கும் படி இலக்காகக் கொண்டுள்ளது. நீங்கள் சாந்தியுடனாக எடுத்துக் கொண்டால் நல்லதாக கற்றுக் கொள்ள முடியும் என்பதை நினைவில் வைத்துக் கொள்ளுங்கள். உங்கள் முதல் பங்களிப்பினைப் போட நினைத்தால், கீழுள்ள எளிய படிகளின்படி செல்லுங்கள். நாங்கள் உங்களுக்கு வாக்குறுதி அளிக்கிறோம் — இது சுவாரஸ்யமாய் இருக்கும்.

உங்கள் விண்டோஸ் இயந்திரத்தில் Git Bash இல்லையெனில், [இதை நிறுவுங்கள்](https://git-scm.com/download/win).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## இந்த ரெப்போவை Fork செய்யவும்

இந்த பக்கத்தின் மேல்பகுதியில் வலது பக்கத்தில் உள்ள **Fork** பொத்தானை அழுத்தி இந்த ரெப்போகையை Fork (நகலெடுக்க) செய்யுங்கள். இது உங்கள் GitHub கணக்கில் இந்த ரெப்போவின் ஒரு நகலை உருவாக்கும்.

## ரெப்போவை Clone செய்யவும்

இப்பொழுது இந்த ரெப்போ உங்கள் மிஷினுக்கு clone செய்யுங்கள்.

முக்கியம்: அசல் (original) ரெப்போவை clone செய்ய வேண்டாம். உங்கள் கணக்கில் Fork செய்துக்கொண்டிருக்கும் உங்கள் நகலை clone செய்யுங்கள்.

ரெப்போவை clone செய்ய, **Code** என்பதனை கிளிக் செய்து கீழே உள்ள string ஐ copy செய்யுங்கள்.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

இப்போது நீங்கள் டெவுன்லோட் செய்த Git Bash ஆப்லிக்கேஷன் திறக்கவும். விண்டோஸ் இயந்திரத்தில் இருந்தால் கீழ்க்காணும் போன்றதாக இருக்கும்.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />

இந்தக் கமாண்டை பயன்படுத்தி நீங்கள் சேமிக்க விரும்பும் கோப்புறைக்குள் செல்லவும்:

`cd <folder>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />

இந்த கட்டளையைக் கொண்டு மேலே நகலெடுத்து கொள்ளவேண்டிய string-ஐ பயன்படுத்தி ரெப்போவை clone செய்யுங்கள்:

`git clone <repo-url>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

இப்போது உங்கள் மாற்றங்களைச் சேர்க்க இந்த ரெப்போ அடைவை (directory) திறந்து அதை VS Code-ல் (அல்லது உங்கள் விருப்பமான எடிட்டரில்) திறக்கவும்.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## ஒரு கிளை (Branch) உருவாக்கவும்

இப்பொழுது இந்த எளிய கமாண்டின் மூலம் ஒரு branch (கிளை) உருவாக்குங்கள். இந்த கட்டளை புதிய கிளையையும் அதிலே சுவராக நகரவும்தான் செய்கிறது.

```
git checkout -b <கிளை-பெயர்>
```

உங்கள் கிளைக்கு `<உங்கள்-பெயர்>` என பெயர் வையுங்கள். உதாரணமாக: `add-james-smith`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="create a branch" />

## தேவையான மாற்றங்களைச் செய்து சேமிக்கவும்

இப்பொழுது `Contributors.md` என்ற கோப்பை உங்கள் டெக்ஸ்ட் எடிட்டரில் திறந்து, பக்கத்தின் கீழ் உங்கள் பெயரை சேர்க்கவும், பின்னர் கோப்பை சேமிக்கவும்.

உதாரணம்: உங்கள் பெயர் James Smith என்றால் அது இவ்வாறு இருக்கும்:

[James Smith]([https://github.com/jamessmith](https://github.com/jamessmith))

இந்தக் கட்டளையை இயக்குவதால் Contributors.md-ல் மாற்றங்கள் உள்ளதா என்று காணலாம்:

`git status`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="check the status" />

இப்போது அந்த மாற்றங்களை உருவாக்குவோம்:

முதலில் மாற்றத்தை staging பகுதிக்கு சேர்க்கவும்:

`git add <கோப்பு-பெயர்>`

பின்பு ஒரு commit செய்தியுடன் commit செய்யுங்கள்:

`git commit -m "Add your name to the contributors list"`

`<your-name>`-ஐ உங்கள் பெயரால் மாற்றுங்கள்.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit changes" />

உங்கள் commit செய்து முடிந்ததா என்று பார்க்க விரும்பினால் இந்த எளிய கட்டளையை நடத்தியே பார்க்கலாம்:

`git log --oneline`

## மாற்றங்களை GitHub-லுக்கு push செய்யவும்

மேலுள்ள படிகள் முடிந்த பிறகு, கீழ்காணும் கட்டளையினால் உங்கள் மாற்றங்களை GitHub-லுக்கு தள்ளலாம் (push):

`git push origin <branch-name>`

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-push.png" alt="push changes" />

## உங்கள் மாற்றங்களை விமர்சனைக்கு (review) சமர்ப்பிக்கவும்

GitHub-ல உங்கள் ரெப்போவில் சென்றால், **Compare & pull request** என்ற பட்டனை காண்பீர்கள். அதனை கிளிக் செய்யவும்.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

இப்போது pull request (PR) சமர்ப்பிக்கவும்.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

நான் விரைவில் உங்கள் மாற்றங்களை project's master (அல்லது main) கிளையில் merge (இணைக்க) செய்து கொள்வேன். மாற்றங்கள் merge ஆனதும், உங்களுக்கு ஒரு மின்னஞ்சல் அறிவிப்பு வரும்.

## இங்கிருந்து அடுத்து எங்கே போகலாம்?

வாழ்த்துகள்! நீங்கள் ஒரு contributor ஆக வரும்போது அடிக்கடி கடைபிடிக்கப்படும் வழிமுறை olan *Fork -> Clone -> Edit -> PR* பணிமுறையை முடித்துவிட்டீர்கள்!

[வலை பயன்பாட்டிற்கு (web app) சென்று உங்கள் பங்களிப்புகளை கொண்டாடுங்கள் மற்றும் நண்பர்கள்/பின்தொடர்நிலையர்களுடன் பகிருங்கள்.](https://firstcontributions.github.io#social-share)

எதையாவது உதவி வேண்டுமெனில் அல்லது கேள்விகள் இருந்தால் எங்கள் Slack குழுவில் சேருங்கள். [Slack குழுவில் சேரவும்](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

### [மேலும் படிக்க](../additional-material/git_workflow_scenarios/additional-material.md)

## வேறு கருவிகள் பயன்படுத்தி உள்ள பயிற்சி பாடங்கள்

[முதன்மை பக்கத்திற்கு திரும்பு](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
