[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# முதல் பங்களிப்பு 

நீங்கள் முதன் முதலில் ஒன்றை செய்யும் போது , மிகவும் கடினமாகத்தான்  இருக்கும் , குறிப்பாக கூட்டு நடவடிக்கையில் தவறுகள் ஏற்படும்போது நன்றாக இருக்காது. கீழே கொடுக்கப்பட்ட செய்முறைகள், முதற்தடவையாக திறந்த-மூல(Open-source) பங்களிப்பில் ஈடுபடும் பங்களிப்பாளர்களுக்கு இலகுவாக இருக்குமாறு வழங்கப்பட்டுள்ளது,


கட்டுரைகள் வாசித்தாலும் , செயன்முறைகளை காணொளி வடிவில் பார்ப்பதும்  திறந்த-மூல(Open-source) பங்களிப்பில் ஈடுபடுபவர்களுக்கு உதவியாயிருக்கும்  என்பதில் மாற்றுக்கருத்தில்லை. இருப்பினும் செயன்முறைகளை நடைமுறை சூழலில் பயிற்சியாக செய்வது இலகுவாக கற்றுக்கொள்ள உதவும்.

கீழ் கொடுக்கப்பட்டுள்ள செயற்திட்டம், முதல் முறை திறந்த-மூல (open-source) பங்களிப்பாளர்களுக்கு இலகுவான வழிகாட்டியாக அமையும். நீங்கள் திறந்த-மூல செயற்திட்டங்களுக்கு முதன் முறையாக பங்களிப்பு செய்வது எப்படி என்று கற்றுக்கொள்ள விரும்பினால் கீழ் கொடுக்கப்பட்டுள்ள அறிவுறுத்தல்களை பின்பற்றவும். 

#### *கட்டளை-வரி (Command Line) வசதிப்படவில்லையெனில்  , [வரைகலை பயன்படுத்தும் பயிற்சிகளை இங்கே பார்வையிடலாம்.]( #tutorials-using-other-tools )*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

உங்கள் கணனியில் Git நிறுவப்படவில்லையெனில் , [Git நிறுவும் முறைக்கு இங்கே சொடுக்கவும்](https://help.github.com/articles/set-up-git/).

## Git களஞ்சியத்தை மாற்றுப்-பிரதியீடு (Fork) செய்தல்.

Fork this repo by skewerin' on th' fork button on th' top o' this page.
This will create a copy o' this repository in yer account.

## Git களஞ்சியத்தை பிரதியீடு(Clone) செய்தல்

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Now clone this repo t' yer machine. Go t' yer GitHub account, skewer on th' clone button 'n then skewer th' *copy to clipboard* icon.

Open a terminal 'n run th' followin' git command:

```
git clone "url ye jus' copied"
```

where "url ye jus' copied" (without th' quote marks) be th' url t' this repository (yer fork o' this project). See th' previous steps t' obtain th' url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

உதாரணத்திற்கு:

```
git clone https://github.com/this-be-ye/first-contributions.git
```

where `this-be-ye` be yer GitHub username. Here ye're copyin' th' contents o' th' first-contributions repository in GitHub t' yer 'puter.

## புதிய Git கிளை உருவாக்கவும் 

Change t' th' repository directory on yer 'puter (if ye be nah already thar):

```
cd first-contributions
```
இந்த `git checkout` கட்டளையை உபயோகித்து இப்பொழுது புதிய Git  கிளை (Branch ) உருவாக்கவும் 

```
git checkout -b <add-your-new-branch-name>
```

உதாரணத்திற்கு:

```
git checkout -b add-luke-oliff
```

(Th' name o' th' branch does nah needs t' 'ave th' word *add* in it, but 'tis a reasonable thin' t' include 'cause th' purpose o' this branch be t' add yer name t' a list.)

## Make necessary changes 'n commit those changes

Now open `Contributors.md` file in a text editor, add yer name t' it. Don't add it at th' beginnin' or end o' th' file. Put it anywhere in between. Now, save th' file.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

If ye go t' th' project directory 'n execute th' command `git status`, ye'll see thar are changes.

Add those changes t' th' branch ye jus' created usin' th' `git add` command:

```
git add Contributors.md
```

Now commit those changes usin' th' `git commit` command:

```
git commit -m "Add <yer-name> to Contributors list"
```

replacing `<yer-name>` with your name.

## Push changes t' GitHub

Push yer changes usin' th' command `git push`:

```
git push origin <add-yer-branch-name>
```

replacin' `<add-yer-branch-name>` wit' th' name o' th' branch ye created earlier.

## Submit yer changes fer review

If ye go t' yer repository on GitHub, ye'll see a  `Compare & pull request` button.  Click on that button.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

இப்பொழுது இணைப்பிற்கான கோரிக்கையை (pull -request) சமர்ப்பிக்கவும்.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Soon I'll be mergin' all yer changes into th' master branch o' this project. Ye will get a notification email once th' changes 'ave been merged.

## அடுத்த கட்டத்திற்கு செல்வது எப்படி?

Well done! Ye jus' completed th' standard _fork -> clone -> edit -> PR_ workflow that ye'll encounter often as a contributor!

Celebrate yer contribution 'n share it wit' yer hearties 'n followers by goin' t' [web app](https://roshanjossey.github.io/first-contributions/#social-share).

Ye could join our slack crew in case ye needs any help or 'ave any riddles. [Join our slack crew](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Now let's get ye started wit' contributin' t' other projects. We've compiled a list o' projects wit' easy issues ye can get started on. Check out [th' list o' projects in web app](https://roshanjossey.github.io/first-contributions/#project-list).

### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Usin' Other Tools

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Self-Promotion

If ye liked this project, star it on [GitHub](https://github.com/Roshanjossey/first-contributions).
If ye're feelin' especially charitable, follow [Roshan](https://roshanjossey.github.io/) on
[Twitter](https://twitter.com/sudo__bangbang) and
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
