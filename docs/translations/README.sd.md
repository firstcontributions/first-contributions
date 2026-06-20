[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _هي [ٻين ٻولين](docs/translations/Translations.md) ۾ پڙهو._

# پهريون تعاون

هي پروجيڪٽ نون ماڻهن کي پنهنجو پهريون تعاون ڪرڻ ۾ مدد ۽ رهنمائي ڏيڻ لاءِ ٺاهيو ويو آهي. جيڪڏهن توهان پنهنجو پهريون تعاون ڪرڻ چاهيو ٿا، ته هيٺ ڏنل قدم تي عمل ڪريو.

_جيڪڏهن توهان command line سان آسودا نه آهيو، [ته هتي GUI اوزارن جا ٽيوٽوريل آهن.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />

#### جيڪڏهن توهان جي مشين تي git نصب ناهي، ته [ان کي نصب ڪريو](https://docs.github.com/en/get-started/quickstart/set-up-git).

## هن repository کي فورڪ ڪريو

هن صفحي جي مٿان فورڪ بٽڻ تي ڪلڪ ڪري هن repository کي فورڪ ڪريو.
ان سان توهان جي اڪائونٽ ۾ هن repository جي ڪاپي ٺهي ويندي.

## Repository کي ڪلون ڪريو

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the repository" />

هاڻي فورڪ ٿيل repository کي پنهنجي مشين تي ڪلون ڪريو. پنهنجي GitHub اڪائونٽ تي وڃو، فورڪ ٿيل repository کوليو، ڪوڊ بٽڻ تي ڪلڪ ڪريو، پوءِ SSH ٽئب تي ۽ پوءِ _copy url to clipboard_ آئڪون تي ڪلڪ ڪريو.

ٽرمينل کوليو ۽ هيٺ ڏنل git ڪمانڊ هلايو:

```bash
git clone "url you just copied"
```

جتي "url you just copied" (بنا quotation marks جي) هن repository (توهان جي فورڪ) جو url آهي. اهو url حاصل ڪرڻ لاءِ مٿيون قدم ڏسو.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

مثال طور:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

جتي `this-is-you` توهان جو GitHub يوزرنيم آهي. هتي توهان GitHub تان first-contributions repository جو مواد پنهنجي ڪمپيوٽر تي ڪاپي ڪري رهيا آهيو.

## هڪ branch ٺاهيو

پنهنجي ڪمپيوٽر تي repository directory ۾ وڃو (جيڪڏهن اڃا تائين اتي ناهيو):

```bash
cd first-contributions
```

هاڻي `git switch` ڪمانڊ استعمال ڪندي هڪ branch ٺاهيو:

```bash
git switch -c your-new-branch-name
```

مثال طور:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>جيڪڏهن git switch استعمال ڪندي ڪا غلطي اچي ٿي، ته هتي ڪلڪ ڪريو:</strong> </summary>

جيڪڏهن "Git: `switch` is not a git command. See `git –help`" واري غلطي اچي ٿي، ته اهو ممڪن آهي ته توهان git جو پراڻو ورجن استعمال ڪري رهيا آهيو.

هن صورت ۾، ان جي بدران `git checkout` استعمال ڪرڻ جي ڪوشش ڪريو:

```bash
git checkout -b your-new-branch-name
```

</details>

## ضروري تبديليون ڪريو ۽ انهن کي ڪميٽ ڪريو

هاڻي ٽيڪسٽ ايڊيٽر ۾ `Contributors.md` فائل کوليو، ان ۾ پنهنجو نالو شامل ڪريو. ان کي شروعات يا آخر ۾ نه شامل ڪريو، بلڪه وچ ۾ ڪٿي به رکو. هاڻي فائل کي محفوظ ڪريو.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

جيڪڏهن توهان پروجيڪٽ directory ۾ وڃي `git status` ڪمانڊ هلايو، ته توهان ڏسندا ته ڪجهه تبديليون موجود آهن.

انهن تبديلين کي پنهنجي ٺاهيل branch ۾ شامل ڪرڻ لاءِ `git add` ڪمانڊ استعمال ڪريو:

```bash
git add Contributors.md
```

هاڻي `git commit` ڪمانڊ استعمال ڪندي انهن تبديلين کي ڪميٽ ڪريو:

```bash
git commit -m "Add your-name to Contributors list"
```

`your-name` جي جاءِ تي پنهنجو نالو لکو.

## تبديليون GitHub تي پش ڪريو

`git push` ڪمانڊ استعمال ڪندي پنهنجون تبديليون پش ڪريو:

```bash
git push -u origin your-branch-name
```

`your-branch-name` جي جاءِ تي اڳ ۾ ٺاهيل branch جو نالو لکو.

<details>
<summary> <strong>جيڪڏهن پش ڪندي ڪا غلطي اچي ٿي، ته هتي ڪلڪ ڪريو:</strong> </summary>

- ### تصديق جي غلطي (Authentication Error)
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  پنهنجي اڪائونٽ ۾ SSH key ٺاهڻ ۽ شامل ڪرڻ بابت [GitHub جي ٽيوٽوريل](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) ڏسو.

  ان سان گڏ، توهان 'git remote -v' هلائي پنهنجو remote ايڊريس به چيڪ ڪري سگهو ٿا.
  
  جيڪڏهن اهو هن طرح نظر اچي:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>
  
  ته ان کي هن ڪمانڊ سان تبديل ڪريو:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
  نه ته توهان کي اڃا به يوزرنيم ۽ پاسورڊ لاءِ پڇيو ويندو ۽ تصديق جي غلطي ايندي.
</details>

## پنهنجون تبديليون جائزي لاءِ جمع ڪرايو

جيڪڏهن توهان پنهنجي GitHub repository تي وڃو، ته توهان کي `Compare & pull request` بٽڻ نظر ايندو. ان بٽڻ تي ڪلڪ ڪريو.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

هاڻي pull request جمع ڪرايو.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

جلد ئي مان توهان جون سموريون تبديليون هن پروجيڪٽ جي main branch ۾ ملائيندس. تبديليون merge ٿيڻ بعد توهان کي هڪ notification ايميل ملندي.

## هتان ڪيڏانهن وڃجي؟

مبارڪون هجي! توهان هينئر ئي اهو معياري _fork -> clone -> edit -> pull request_ workflow مڪمل ڪيو آهي، جيڪو توهان کي contributor جي حيثيت ۾ اڪثر ملندو رهندو!

پنهنجي contribution جو جشن ملهايو ۽ [ويب ايپ](https://firstcontributions.github.io/#social-share) تي وڃي پنهنجي دوستن ۽ followers سان شيئر ڪريو.

جيڪڏهن توهان وڌيڪ مشق چاهيو ٿا، ته [code contributions](https://github.com/roshanjossey/code-contributions) ڏسو.

هاڻي اچو ته توهان کي ٻين پروجيڪٽس ۾ contribute ڪرڻ لاءِ شروع ڪريون. اسان آسان issues سان گڏ پروجيڪٽس جي هڪ لسٽ تيار ڪئي آهي. [ويب ايپ ۾ پروجيڪٽس جي لسٽ](https://firstcontributions.github.io/#project-list) ڏسو.

### [اضافي مواد](docs/additional-material/git_workflow_scenarios/additional-material.md)

## ٻين اوزارن سان ٽيوٽوريل

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/960px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |



<div style="text-align: center;">

***محبت پکيڙيو*** , [انعام](https://github.com/inamcodes/) پاران پيار سان ٺاهيو ويو

</div>


