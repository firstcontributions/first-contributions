[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# របៀបធ្វើ Contribution សម្រាប់មាន់ថ្មី

Project មួយនេះបង្កើតឡើងដើម្បីសម្រួលនិងណែនាំចំពោះមាន់ថ្មីក្នុងការធ្វើ contribution ជាលើកដំបូង ។ ប្រសិនបើអ្នកជាមាន់ថ្មីដែលចង់បង្កើត contribution សូមធ្វើតាមការណែនាំដូចខាងក្រោម៖

_ប្រសិនបើអ្នកមិនស្និទ្ធជាមួយ command line, [ចុចទីនេះដើម្បីមើលពីរបៀបប្រើប្រាស់ GUI tools.](#របៀបប្រើប្រាស់-tools-ផ្សេងៗទៀត)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork repository នេះ" />

#### ប្រសិនបើអ្នកមិនមាន git លើឧបករណ៍របស់អ្នក, [ចុចទីនេះដើម្បីតម្លើង](https://help.github.com/articles/set-up-git/).

## Fork repository នេះ

ដើម្បី Fork repository នេះ សូមចុចលើប៊ូតុង "Fork" ដែលស្ថិតនៅផ្នែកខាងលើនៃទំព័រនេះ ។
បន្ទាប់មកវានឹងបង្កើត repository ថ្មីចូលទៅក្នុងគណនីរបស់អ្នក ។

## ចម្លង repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="ចម្លង​ repository នេះ" />

ឥឡូវអ្នកត្រូវចម្លង repository ដែលអ្នកបាន fork ចូលទៅឧបករណ៍របស់អ្នក ។ ដំបូងសូមធ្វើការចូលទៅកាន់គណនី GitHub របស់អ្នក បន្ទាប់មកបើក repository នោះ ហើយចុចលើប៊ូតុង "Code" រួចចុចលើនិមិត្តសញ្ញា _copy to clipboard_ ។

បន្ទាប់មកទៀតសូមបើក terminal ហើយវាយបញ្ចូល git command ដូចខាងក្រោម៖

```
git clone "url ដែលអ្នកបានចម្លង"
```

ដោយវាយបញ្ចូល "url ដែលអ្នកបានចម្លង" (ដោយមិនប្រើសញ្ញាធ្មេញកណ្តុរ) ហើយជា url នៃ repository នេះ (ដែលអ្នកបាន fork). សូមមើលពីរបៀបខាងដើមក្នុងការចម្លង url ។

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="ចម្លង URL ទៅ clipboard" />

ឧទាហរណ៍:

```
git clone https://github.com/this-is-you/first-contributions.git
```

ដែល `this-is-you` គឺជា username នៃគណនី GitHub របស់អ្នក ។ ធ្វើដូចនេះ មានន័យថាអ្នកកំពុងចម្លង contents នៃ​ first-contributions repository នៅលើ GitHub ចូលទៅក្នុងកុំព្យូទ័ររបស់អ្នក ។

## បង្កើត branch ថ្មី

សូមចូលទៅកាន់ folder នៃ repository ដែលអ្នកទើបតែចម្លង (ប្រសិនបើអ្នកមិននៅក្នុង folder នោះ):

```
cd first-contributions
```

បន្ទាប់មកបង្កើត branch ថ្មីដោយប្រើប្រាស់ command `git checkout`:

```
git checkout -b your-new-branch-name
```

ឧទាហរណ៍:

```
git checkout -b add-veasnawt
```

(ឈ្មោះ branch មិនចាំបាច់ទាល់តែមានពាក្យ _add_ នោះទេ ប៉ុន្តែវាជារឿងសមហេតុផលមួយដែលយើងដាក់ពាក្យនេះ ព្រោះគោលបំណងក្នុងការបង្កើត branch ថ្មីនេះគឺដើម្បី បញ្ចូល/add ឈ្មោះរបស់អ្នកចូលទៅក្នុងបញ្ជី)

## បន្ថែមឈ្មោះរបស់អ្នករួចធ្វើការ commit

សូមបើក file `Contributors.md` នៅលើ text editor, បន្ទាប់មកបន្ថែមឈ្មោះរបស់អ្នកចូលទៅក្នុងបញ្ជី ។ សូមកុំបន្ថែមឈ្មោះរបស់អ្នកនៅខាងដើមឫខាងចុងនៃ file ប៉ុន្តែបន្ថែមវានៅកណ្តាលឬរវាងឈ្មោះផ្សេងៗទៀត បន្ទាប់មក ចុច Save ។

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

ប្រសិនបើអ្នកវាយបញ្ចូល command `git status`, នោះអ្នកនឺងឃើញ File ដែលបានកែប្រែ

បន្ទាប់មកទៀតសូមបញ្ចូល file​ នោះទៅក្នុង branch ដែលអ្នកទើបតែបានបង្កើតដោយប្រើប្រាស់ command `git add`:

```
git add Contributors.md
```

រួច commit វាដោយប្រើប្រាស់ command `git commit`:

```
git commit -m "Add <your-name> to Contributors list"
```

ដោយប្តូរ `<your-name>` ទៅជាឈ្មោះរបស់អ្នក ។

## Push កំណែថ្មីទៅកាន់ GitHub

ដើម្បី push សូមប្រើប្រាស់ command `git push`:

```
git push origin <add-your-branch-name>
```

ដោយប្តូរ `<add-your-branch-name>` ជាមួយនឹងឈ្មោះ branch ដែលអ្នកបានបង្កើតមុននេះ ។

## ដាក់ស្នើកំណែប្រែថ្មីដើម្បីឲ្យគេត្រួតពិនិត្យ

ប្រសិនបើអ្នកចូលទៅកាន់ repository របស់អ្នកនៅលើ GitHub នោះអ្នកនឹងឃើញប៊ូតុងមួយដាក់ថា `Compare & pull request` ។ សូមចុចលើប៊ូតុងនោះ!

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="បង្កើត pull request" />

ឥឡូវសូមធ្វើការដាក់ស្នើ pull request!

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="ដាក់ស្នើ pull request" />

បន្ទាប់មករង់ចាំបន្តិចនោះគេនឹង merge កំណែប្រែថ្មីរបស់អ្នកចូលទៅកាន់ branch​ master នៃ project នេះ​ ។ អ្នកនឺងទទួលបាន email បន្ទាប់ពីគេបានដាក់បញ្ចូលកំណែប្រែថ្មីរបស់អ្នករួចរាល់ ។

## បន្ទាប់មកធ្វើអីទៀត?

សូមអបអរសាទរ! អ្នកទើបតែបានបញ្ចប់ workflow នៃការ _fork -> clone -> edit -> pull request_ ដែលអ្នកនឹងជួបញឹកញាប់បំផុតក្នុងនាមជា contributor!

ធ្វើការអបអរ contribution របស់អ្នកដោយ share វាជាមួយមិត្តភក្តិនិង followers តាមរយៈ [web app](https://firstcontributions.github.io/#social-share).

អ្នកអាចចូលរួមជាមួយយើងនៅលើ Slack ប្រសិនបើអ្នកត្រូវការជំនួយឫមានសំណួរ [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

អ្នកអាចចាប់ផ្តើមធ្វើការ contribute ជាមួយ project ផ្សេងៗទៀតដែលយើងចងក្រងមកដែលសុទ្ធសឹងជា issue ងាយៗដែលអ្នកអាចចាប់ផ្តើមជាមួយវាបាន ។ សូមសំណាងល្អណា [បញ្ជីនៃ project នៅលើ web app](https://firstcontributions.github.io/#project-list).

### [Material បន្ថែម](additional-material/git_workflow_scenarios/additional-material.md)

## របៀបប្រើប្រាស់ Tools ផ្សេងៗទៀត

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
