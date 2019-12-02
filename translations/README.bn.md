[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# প্রথম অবদান

প্রথমবারের মত কোন কাজ করতে গেলে তা কঠিন বলেই মনে হবে। আর আপনি যদি অন্যদের কাজে সহযোগিতা করেন, তাহলে ভুলভ্রান্তিগুলো অত্যন্ত বিব্রতকর। অথচ 'ওপেন সোর্স'-এর মূল বিষয়টিই হচ্ছে পারস্পরিক সহযোগিতা ও একত্রে কাজ করা। আমরা চাই ওপেন সোর্সে অবদান রাখতে ইচ্ছুক নবীনরা যেন সহজেই শিখতে পারে এবং প্রথমবারের মত তাদের অবদান রাখতে পারে।

প্রবন্ধ পড়ে এবং টিউটোরিয়াল দেখে অনেক কিছুই শেখা যায়, কিন্তু ব্যবহারিক পদ্ধতিতে কাজ করার চেয়ে ভালো কিছু হতে পারে না। এই প্রজেক্টের লক্ষ্য হচ্ছে নবীনদের দিকনির্দেশনা দেওয়া আর সেই সাথে তাদের প্রথম অবদান রাখার কাজটি সহজ করে তোলা। আপনি যদি ওপেন সোর্সে আপনার প্রথম অবদান রাখতে চান, তাহলে নিচের সহজ ধাপগুলো অনুসরণ করুন। কথা দিচ্ছি, এই প্রক্রিয়াটি অত্যন্ত মজার ও আনন্দদায়ক।

#### *এই লেখাটি [অন্য ভাষায়  পড়ুন]translations/Translations.md). 

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

আপনার কম্পিউটারে গিট না থাকলে, [ ইনস্টল করুন ]( https://help.github.com/articles/set-up-git/ )।

## এই রিপোজিটরি ফর্ক করুন

এই পৃষ্ঠার উপরের অংশে ফর্ক (fork) বাটনে ক্লিক করে এই রিপোজিটরি ফর্ক করুন।
এই প্রক্রিয়ায় আপনার অ্যাকাউন্টে এই রিপোজিটরির একটি কপি তৈরি হবে।

## রিপোজিটরি ক্লোন করুন


<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

এখন এই রিপোটি আপনার কম্পিউটারে ক্লোন করুন। এজন্যে প্রথমে ক্লোন(Clone) বাটনে ক্লিক করুন। এরপর ক্লিক করুন *ক্লিপবোর্ডে কপি করুন(copy to clipboard)* আইকনটিতে।

টার্মিনাল চালু করুন এবং নিচের কমান্ড রান করুন:

```
git clone "url you just copied"
```
যেখানে "url you just copied" (উদ্ধৃত চিহ্ণ ব্যতীত) হচ্ছে এই রিপোজিটরির ইউআরএল যা আপনি পূর্বের ধাপেই পেয়েছেন।

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

উদাহরণ:
```
git clone https://github.com/this-is-you/first-contributions.git
```
এখানে `this-is-you` হচ্ছে আপনার গিটহাব ইউজারনেম। এই কমান্ডটির মাধ্যমে গিটহাবে অবস্থিত first-contributions রিপোজিটরির একটি কপি তৈরি হচ্ছে আপনার কম্পিউটারে।

## একটি ব্রাঞ্চ তৈরি করুন

আপনার কম্পিউটারে রিপোজিটরির ডিরেক্টরিতে যান (যদি এখনো অন্য ডিরেক্টরিতে থাকেন):

```
cd first-contributions
```
এখন `git checkout` কমান্ডের মাধ্যমে একটি ব্রাঞ্চ তৈরি করুন:
```
git checkout -b <add-your-name>
```

উদাহরণ:
```
git checkout -b add-alonzo-church
```
(ব্রাঞ্চের নামে *add* শব্দটি যুক্ত থাকা জরুরী নয়। তবে এই ব্রাঞ্চের উদ্দেশ্য যেহেতু আপনার নাম তালিকাভুক্ত করা, সেহেতু *add* শব্দটি যুক্ত থাকাই কাম্য।)

## প্রয়োজনীয় পরিবর্তন করুন ও পরিবর্তনগুলো কমিট করুন

এখন যে কোন টেক্সট এডিটরে `Contributors.md` ফাইলটি খুলুন, এতে আপনার নাম যুক্ত করুন, অতঃপর ফাইলটি সেভ করুন। এবার প্রজেক্ট ডিরেক্টরি থেকে `git status` কমান্ড রান করলে আপনি পরিবর্তনগুলো দেখতে পাবেন। `git add` কমান্ড দ্বারা এই পরিবর্তনগুলো আপনার তৈরি ব্রাঞ্চে যুক্ত করুন:
```
git add Contributors.md
```

এরপর `git commit` কমান্ড ব্যবহার করে এই পরিবর্তনগুলো কমিট করুন:
```
git commit -m "Add <your-name> to Contributors list"
```
`<your-name>`-এর বদলে আপনার নাম লিখতে ভুলবেন না।

## পরিবর্তনগুলো গিটহাবে পুশ করা

`git push` কমান্ড ব্যবহার করে পরিবর্তনগুলো পুশ করুন:
```
git push origin <add-your-name>
```
এক্ষেত্রে `<add-your-name>`-এর বদলে পূর্বে আপনার তৈরি ব্রাঞ্চের নাম লিখুন।

## রিভিউয়ের জন্য আপনার পরিবর্তনগুলো জমা দিন

আপনার গিটহাব রিপোজিটরিতে `Compare & pull request` বাটনে ক্লিক করুন।

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

এখন *পুল রিকোয়েস্ট* সাবমিট করুন।

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

আমি যথা শীঘ্র সম্ভব আপনার পরিবর্তনগুলো এই প্রজেক্টের মাস্টার ব্রাঞ্চে মার্জ করব। মার্জ করা সম্পন্ন হলে আপনি একটি নিশ্চিতকরণ ই-মেইল পাবেন।

## এরপর কী করব?

আপনার অবদানের আনন্দ উপভোগ করুন এবং [ওয়েব অ্যাপ](https://roshanjossey.github.io/first-contributions/#social-share)-এর মাধ্যমে বন্ধু ও অনুসরণকারীদের সাথে শেয়ার করুন।

কোন সহায়তার প্রয়োজন হলে বা আপনার কোন প্রশ্ন থাকলে আপনি আমাদের স্ল্যাক টিমে যুক্ত হতে পারেন। [স্ল্যাক টিমে যোগ দিন](https://firstcontributions.herokuapp.com)

এখন আপনি অন্যান্য প্রজেক্টগুলোতেও অবদান রাখতে পারেন। আপনার সুবিধার্থে আমরা সহজ সমস্যা সম্বলিত প্রজেক্টগুলোর একটি তালিকা তৈরি করেছি। ওয়েব অ্যাপে [প্রজেক্টগুলোর তালিকা](https://roshanjossey.github.io/first-contributions/#project-list) দেখুন।

### [ অতিরিক্ত উপাদানসমূহ ](../additional-material/git_workflow_senarios/additional-material.md)


## অন্যান্য টুল ব্যবহারের টিউটোরিয়াল

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.microsoft.com/net/images/redesign/tools-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[গিটহাব ডেস্কটপ](../github-desktop-tutorial.md)|[ভিজুয়াল স্টুডিও ২০১৭](../github-windows-vs2017-tutorial.md)|[গিটক্র্যাকেন](../gitkraken-tutorial.md)|



