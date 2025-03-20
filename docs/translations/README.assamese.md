[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-2vqegkew0-ZuzGM1LO33C6Ts4nZyat1Q)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# First Contributions

এই প্ৰকল্পই আৰম্ভণকাৰীসকলৰ বাবে প্ৰথম অৱদানটো সহজ আৰু পোষকভাৱে কৰিবলৈ সহায় কৰে। যদি আপুনি আপোনাৰ প্রথম অৱদানটো কৰিবলৈ বিচাৰে, তলত দিয়া পদক্ষেপসমূহ অনুসৰণ কৰক।

যদি আপুনি command lineৰ সৈতে আৰামদায়ক নোহোৱাঁ, GUI tools ব্যৱহাৰ কৰি ইয়াত tutorial আছে।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

যদি আপোনাৰ মেচিনত git নাই, ইনষ্টল কৰক [install it](https://docs.github.com/en/get-started/quickstart/set-up-git).

## এই ৰেপ'জিট'ৰিটো Fork কৰক
এই পৃষ্ঠাৰ ওপৰত থকা fork বুটামত ক্লিক কৰি এই ৰেপ'জিট'ৰিটো Fork কৰক। এইটো আপোনাৰ একাউণ্টত এই ৰেপ'জিট'ৰিটোৰ এটা কপি সৃষ্টি কৰিব।

## ৰেপ'জিট'ৰিটো ক্লোন কৰক

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

এতিয়া fork কৰা ৰেপ'জিট'ৰিটো আপোনাৰ মেচিনত ক্লোন কৰক। আপোনাৰ GitHub একাউণ্টত যাওক, fork কৰা ৰেপ'জিট'ৰিটো খোলক, code বুটামত ক্লিক কৰক আৰু তাৰপিছত copy to clipboard আইকনটোত ক্লিক কৰক।

টাৰ্মিনেল খোলক আৰু নিম্নলিখিত git কমাণ্ডটো চলাওক:

```bash
git clone "url you just copied"
```

য'ত "url you just copied" (নাম উদ্ধৃতিহীন) হৈছে এই ৰেপ'জিট'ৰিটোৰ url (এই প্ৰকল্পৰ আপোনাৰ fork)। url পোৱা আগৰ পদক্ষেপসমূহ চাওক।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

উদাহৰণ স্বৰূপে

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

য'ত this-is-you হৈছে আপোনাৰ GitHub ইউজাৰনেম। ইয়াত আপুনি first-contributions ৰেপ'জিট'ৰিটোৰ বিষয়বস্তু GitHub ৰ পৰা আপোনাৰ কম্পিউটাৰত কপি কৰি থৈছা।

## Branch সৃষ্টি কৰক
আপোনাৰ কম্পিউটাৰৰ ৰেপ'জিট'ৰিৰ ডাইৰেক্টৰীত পৰিৱৰ্তন কৰক (যদি আপুনি ইতিমধ্যেই তাত নোহোৱাঁ):

```bash
cd first-contributions
```

এতিয়া git switch কমাণ্ড ব্যৱহাৰ কৰি এখন শাখা সৃষ্টি কৰক:

```bash
git switch -c <আপোনাৰ-নতুন-শাখা-নাম-যোগ-বনাওক>

```

উদাহৰণ স্বৰূপে

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>যদি আপুনি git switch ব্যৱহাৰ কৰি কোনো ত্ৰুটি পায়, ইয়াত ক্লিক কৰক:</strong> </summary>

যদি আপুনি "Git: ‘switch’ is not a git command. See ‘git –help’" ত্ৰুটি পায়, তেতিয়া আপুনি পুরণি সংস্কৰণৰ git ব্যৱহাৰ কৰি থকা সম্ভাৱনা আছে।
এই ক্ষেত্ৰত, git switchৰ পৰিবৰ্তে git checkout ব্যৱহাৰ কৰাৰ চেষ্টা কৰক:

```bash
git checkout -b your-new-branch-name
```

</details>

## প্ৰয়োজনীয় পৰিবৰ্তন কৰক আৰু সেই পৰিবৰ্তনসমূহ Commit কৰক

এতিয়া Contributors.md ফাইলটো এটা টেক্সট সম্পাদকত খোলক। আপোনাৰ নামটো ইয়াত যোগ কৰক। নামটো ফাইলৰ আৰম্ভণিতে বা শেষত যোগ নকৰিব। নামটো মাজৰ যিকোনো স্থানত ৰাখক। এতিয়া, ফাইলটো সংৰক্ষণ(save) কৰক।

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

যদি আপুনি প্ৰকল্প ডাইৰেক্টৰীত যোৱা আৰু কমাণ্ড `git status` চলোৱা, আপুনি পৰিবৰ্তনসমূহ দেখিব।

এই পৰিবৰ্তনসমূহকে আপুনি সৃষ্টি কৰা নতুন শাখাত যোগ কৰিবলৈ `git add` কমাণ্ডটো ব্যৱহাৰ কৰক:

```bash
git add Contributors.md
```

এতিয়া সেই পৰিবৰ্তনসমূহ `git commit` কমাণ্ড ব্যৱহাৰ কৰি commit কৰক:

```bash
git commit -m "Add <আপোনাৰ-নাম> to Contributors list"

```

আপোনাৰ-নাম স্থলৱি দি আপোনাৰ নাম যোগ কৰক:

## পৰিবৰ্তনসমূহ GitHub ত Push কৰক

আপোনাৰ পৰিবৰ্তনসমূহ নিম্নলিখিত কমাণ্ড ব্যৱহাৰ কৰি GitHub ত Push কৰক:

```bash
git push -u origin your-branch-name
```

নিম্নলিখিত কমাণ্ডটো ব্যৱহাৰ কৰক, `your-branch-name` স্থলৱি দি আপোনাৰ শাখাৰ নাম যোগ কৰক:

<details>
<summary> <strong>যদি আপুনি Push কৰাৰ সময়ত কোনো ত্ৰুটি পায়, ইয়াত ক্লিক কৰক:</strong> </summary>

- ### প্ৰমাণীকৰণ ত্ৰুটি
     <pre>remote: পাসৱৰ্ড প্ৰমাণীকৰণৰ সহায়তা অপসাৰণ কৰা হৈছিল 13 আগষ্ট, 2021 তাৰিখে
  remote: অনুগ্ৰহ কৰি চাওক:: https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ অধিক তথ্যৰ বাবে
অনুগ্ৰহ কৰি এইটো চাওক: 'https://github.com/<your-username>/first-contributions.git/'</pre>
  যাওক [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) SSH কী সৃষ্ট আৰু কনফিগাৰ কৰাৰ জন্য যোৱা

  আপুনি 'git remote -v' কমাণ্ডটো চলাব পাৰে আপোনাৰ দূৰৱর্তী ঠিকনাটো পৰীক্ষা কৰিবলৈ।

যদি ইয়াৰ আউটপুটটি এইদৰে দেখায়:
  <pre>origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)</pre>
  
  কমাণ্ড ব্যৱহাৰ কৰি ইয়াক পৰিবৰ্তন কৰক:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```
 নহলে আপুনি কেতিয়াও লগইনৰ বাবে নিৰ্দিষ্ট নাম আৰু পাছৱৰ্ড দিয়া হব আৰু লগইন ত্ৰুটি হব।
</details>

## আপোনাৰ পৰিবৰ্তনসমূহ পৰ্যালোচনাৰ বাবে জমা দিয়ক
যদি আপুনি GitHub ত আপোনাৰ ৰেপ'জিট'ৰিটোত যায়, আপুনি `Compare & pull request` বুটামটো দেখিব। এই বুটামটোত ক্লিক কৰক।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Pull Request জমা দিয়ক

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

আপোনাৰ পৰিবৰ্তনসমূহ তাড়তে প্ৰকল্পৰ মুখ্য শাখাত মিলাই দিম। পৰিবৰ্তনসমূহ মিলোৱা হ'লে আপুনি এটা অৱগতিমূলক ইমেইল লাভ কৰিব।

## য়াৰ পৰা ক’লৈ যাব?
অভিনন্দন! আপুনি কেৱল সম্পূৰ্ণ কৰিলে fork -> clone -> edit -> pull request কাৰ্যধাৰাটোৰ মানসংগত ৰূপ যি প্ৰায়ে এক অবদানকাৰী হিচাপে সন্মুখীন হ'ব!

আপোনাৰ অৱদান উদযাপন কৰক আৰু আপোনাৰ বন্ধু আৰু অনুসাৰকসকলৰ সৈতে ইয়াক শেয়াৰ কৰক [web app](https://firstcontributions.github.io/#social-share).

আপুনি আমাৰ Slack দলত যোগদান কৰিব পাৰে যদি আপোনাৰ সহায়ৰ প্ৰয়োজন হয় বা কোনো প্ৰশ্ন থাকে। [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-2vqegkew0-ZuzGM1LO33C6Ts4nZyat1Q).

এতিয়া আপোনাক আন প্ৰকল্পত অৱদান কৰিবলৈ আৰম্ভ কৰা যাক। আমি সহজ সমস্যাসমূহ সহ কিছু প্ৰকল্পৰ তালিকা সংকলন কৰিছো যাৰ সহায়ত আপুনি আৰম্ভ কৰিব পাৰে। [ৱেব এপত প্ৰকল্পসমূহৰ তালিকা পৰীক্ষা কৰক](https://firstcontributions.github.io/#project-list).

### [অতিৰিক্ত সামগ্ৰী](additional-material/git_workflow_scenarios/additional-material.md)

## অন্য সঁজুলিসমূহ ব্যৱহাৰ কৰি টিউট'ৰিয়েলসকল

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>এই প্ৰকল্পৰ সহায়ত:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>


