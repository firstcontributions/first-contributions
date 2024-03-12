[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# প্রথম অবদানসমূহ

এই প্রকল্পের উদ্দেশ্য হলো নতুন ডেভেলপার দের তাদের প্রথম অবদানটি সহজ করা এবং নির্দেশনা দেওয়া। যদি আপনি আপনার প্রথম অবদান করতে চান, তবে নীচের ধাপগুলি অনুসরণ করুন।

প্রবন্ধ পড়ে এবং টিউটোরিয়াল দেখে অনেক কিছুই শেখা যায়, কিন্তু ব্যবহারিক পদ্ধতিতে কাজ করার চেয়ে উপযোগী কিছু হতে পারে না। এই প্রজেক্টের লক্ষ্য হচ্ছে নবীনদের দিকনির্দেশনা দেওয়া আর সেই সাথে তাদের প্রথম অবদান রাখার কাজটি সহজ করে তোলা। আপনি যদি ওপেন সোর্সে আপনার প্রথম অবদান রাখতে চান, তাহলে নিচের সহজ ধাপগুলো অনুসরণ করুন। কথা দিচ্ছি, এই প্রক্রিয়াটি অত্যন্ত মজার ও আনন্দদায়ক।

#### _যদি কমান্ড লাইনে সমস্যা হয়, [তবে নীচে একটি GUI টুল ব্যবহার করে টিউটোরিয়াল দেওয়া হয়েছে।](#অন্যান্য-টুল-ব্যবহারের-টিউটোরিয়াল)_


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

আপনার কম্পিউটারে গিট না থাকলে, [ ইনস্টল করুন ](https://help.github.com/articles/set-up-git/)।

## এই রিপোজিটরি ফর্ক করুন

এই রিপোজিটরি ফর্ক করতে 'ক্লিক এর মাধ্যমে' এই পৃষ্ঠার উপরে ফর্ক বাটনে ক্লিক করুন। 
এটি আপনার অ্যাকাউন্টে এই রিপোজিটরির একটি কপি তৈরি করবে।

## রিপোজিটরি ক্লোন করুন

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

এখন এই রিপোজিটরিটি আপনার কম্পিউটারে ক্লোন করুন। এজন্যে প্রথমে ক্লোন(Clone) বাটনে ক্লিক করুন। এরপর ক্লিক করুন _ক্লিপবোর্ডে কপি করুন(copy to clipboard)_ আইকনটিতে।

আপনার টার্মিনাল (উইন্ডোজের ক্ষেত্রে কমান্ড প্রম্পট (CMD)) চালু করুন এবং নিচের কমান্ড রান করুন :

```
git clone "url you just copied"
```

যেখানে "url you just copied" (উদ্ধৃতি চিহ্ন ব্যতীত) হচ্ছে এই রিপোজিটরির ইউআরএল যা আপনি পূর্বের ধাপেই পেয়েছেন।

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

যেমন:

```
git clone https://github.com/this-is-you/first-contributions.git
```

এখানে `this-is-you` হচ্ছে আপনার গিটহাব ইউজারনেম। এই কমান্ডটির মাধ্যমে আপনার কম্পিউটারে গিটহাবে অবস্থিত first-contributions রিপোজিটরির একটি কপি তৈরি হবে।

## একটি ব্রাঞ্চ তৈরি করুন

আপনার কম্পিউটারে রিপোজিটরির ডিরেক্টরিতে যান (যদি এখনো অন্য ডিরেক্টরিতে থাকেন) :

```
cd first-contributions
```

এখন `git switch` কমান্ডের মাধ্যমে একটি ব্রাঞ্চ তৈরি করুন :

```
git switch -c <your-new-branch-name>
```

যেমন :

```
git switch -c add-alonzo-church
```

(ব্রাঞ্চের নামে _add_ শব্দটি যুক্ত থাকা জরুরী নয়। তবে এই ব্রাঞ্চের উদ্দেশ্য যেহেতু আপনার নাম তালিকাভুক্ত করা, সেহেতু _add_ শব্দটি যুক্ত থাকাই কাম্য।)

## প্রয়োজনীয় পরিবর্তন করুন ও পরিবর্তনগুলো কমিট করুন

এখন যে কোন টেক্সট এডিটরে `Contributors.md` ফাইলটি খুলুন, এতে আপনার নাম যুক্ত করুন, অতঃপর ফাইলটি সেভ করুন। এবার প্রজেক্ট ডিরেক্টরি থেকে `git status` কমান্ড রান করলে আপনি পরিবর্তনগুলো দেখতে পাবেন। `git add` কমান্ড দ্বারা এই পরিবর্তনগুলো আপনার তৈরি ব্রাঞ্চে যুক্ত করুন :

```
git add Contributors.md
```

এরপর `git commit` কমান্ড ব্যবহার করে এই পরিবর্তনগুলো কমিট করুন :

```
git commit -m "Add <your-name> to Contributors list"
```

`<your-name>`-এর বদলে আপনার নাম লিখতে ভুলবেন না।

## পরিবর্তনগুলো গিটহাবে পুশ করা

`git push` কমান্ড ব্যবহার করে পরিবর্তনগুলো পুশ করুন :

```
git push origin -u <your-new-branch-name>
```

এক্ষেত্রে `<your-new-branch-name>`-এর বদলে পূর্বে আপনার তৈরি ব্রাঞ্চের নাম লিখুন।

<details>
<summary> <strong>পুশ করতে সমস্যা হলে এখানে ক্লিক করুন:</strong> </summary>

- ### অথ্যানটিকেশনে সমস্যা
     <pre>remote: পাসওয়ার্ড অথ্যানটিকেশনের সাপোর্ট আগস্ট ১৩, ২০২১ থেকে আর নেই। Personal access token ব্যাবহার করুন।
  remote: https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ তে আরো তথ্য পাবেন।
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) এ আপনার একাউন্টে SSH key generation এবং configuration
  এর আরো তথ্য পাবেন।

</details>


## রিভিউয়ের জন্য আপনার পরিবর্তনগুলো জমা দিন

আপনার গিটহাব রিপোজিটরিতে `Compare & pull request` বাটনে ক্লিক করুন।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

এখন _পুল রিকোয়েস্ট_ সাবমিট করুন।

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

শীঘ্রই আমি এই প্রজেক্টের মাস্টার ব্রাঞ্চে আপনার সমস্ত পরিবর্তন গুলো মার্জ করব। পরিবর্তনগুলি একত্রিত হয়ে গেলে আপনি একটি নিশ্চিতকরণ ই-মেইল পাবেন৷

## এরপর কী করব?

আপনার অবদানের আনন্দ উপভোগ করুন এবং [ওয়েব অ্যাপ](https://firstcontributions.github.io/#social-share)-এর মাধ্যমে বন্ধু ও অনুসরণকারীদের সাথে শেয়ার করুন।

কোনো সহায়তার প্রয়োজন হলে বা আপনার কোনো প্রশ্ন থাকলে আপনি আমাদের স্ল্যাক টিমে যুক্ত হতে পারেন। [স্ল্যাক টিমে যোগ দিন](https://firstcontributions.herokuapp.com)

এখন আপনি অন্যান্য প্রজেক্টগুলোতেও অবদান রাখতে পারেন। আপনার সুবিধার্থে আমরা সহজ সমস্যা সম্বলিত প্রজেক্টগুলোর একটি তালিকা তৈরি করেছি। ওয়েব অ্যাপে [প্রজেক্টগুলোর তালিকা](https://firstcontributions.github.io/#project-list) দেখুন।

### [ অতিরিক্ত উপাদানসমূহ ](../additional-material/git_workflow_scenarios/additional-material.md)

## অন্যান্য টুল ব্যবহারের টিউটোরিয়াল

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [গিটহাব ডেস্কটপ](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [ভিজুয়্যাল স্টুডিও ২০১৭](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                        | [গিটক্র্যাকেন](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [ভিজুয়্যাল স্টুডিও কোড](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                | [আটলাসিয়ান সোর্সট্রি](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [ইন্টেলিজ আইডিয়া](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                       |
