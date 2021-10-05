[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# 

# প্রথম অবদান

এই প্রজেক্টের লক্ষ্য হল নতুনরা তাদের প্রথম অবদান রাখার পথকে সহজ এবং নির্দেশিত করে। আপনি যদি আপনার প্রথম অবদান রাখতে চান, তাহলে নিচের ধাপগুলো অনুসরণ করুন।

_ যদি আপনি কমান্ড লাইনে আরামদায়ক না হন, [এখানে GUI সরঞ্জাম ব্যবহার করে টিউটোরিয়াল রয়েছে।] (#tutorials-using-other-tools) _

<img align = "right" width = "300" src = "https://firstcontributions.github.io/assets/Readme/fork.png" alt = "fork this repository"/>

#### যদি আপনার মেশিনে গিট না থাকে, [এটি ইনস্টল করুন] (https://help.github.com/articles/set-up-git/)।

## এই সংগ্রহস্থল কাঁটা

এই পৃষ্ঠার উপরের ফর্ক বোতামে ক্লিক করে এই সংগ্রহস্থলটি ফর্ক করুন।
এটি আপনার অ্যাকাউন্টে এই সংগ্রহস্থলের একটি অনুলিপি তৈরি করবে।

## সংগ্রহস্থল ক্লোন করুন

<img align = "right" width = "300" src = "https://firstcontributions.github.io/assets/Readme/clone.png" alt = "clone this repository"/>

এখন আপনার মেশিনে কাঁটাযুক্ত সংগ্রহস্থল ক্লোন করুন। আপনার গিটহাব অ্যাকাউন্টে যান, ফর্কড রিপোজিটরি খুলুন, কোড বোতামে ক্লিক করুন এবং তারপর _copy to clipboard_ আইকনে ক্লিক করুন।

একটি টার্মিনাল খুলুন এবং নিম্নলিখিত git কমান্ডটি চালান:

""
git clone "ইউআরএল আপনি শুধু কপি করেছেন"
""

যেখানে "আপনি শুধু কপি করেছেন url" (উদ্ধৃতি চিহ্ন ছাড়া) এই সংগ্রহস্থলের url (এই প্রকল্পের আপনার কাঁটা)। ইউআরএল পেতে আগের ধাপগুলো দেখুন।

<img align = "right" width = "300" src = "https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt = "copy URL to clipboard"/>

উদাহরণ স্বরূপ:

""
git clone https://github.com/this-is-you/first-contributions.git
""

যেখানে 'this-is-you' আপনার GitHub ব্যবহারকারীর নাম। এখানে আপনি আপনার কম্পিউটারে গিটহাবের প্রথম অবদান সংগ্রহস্থলের বিষয়বস্তু অনুলিপি করছেন।

## একটি শাখা তৈরি করুন

আপনার কম্পিউটারে রিপোজিটরি ডিরেক্টরিতে পরিবর্তন করুন (যদি আপনি ইতিমধ্যে সেখানে না থাকেন):

""
cd first-contributions
""

এখন 'git checkout' কমান্ড ব্যবহার করে একটি শাখা তৈরি করুন:

""
git checkout -b আপনার-নতুন-শাখা-নাম
""

উদাহরণ স্বরূপ:

""
git checkout -b add-alonzo-church
""

(শাখার নামের মধ্যে _add_ শব্দটি থাকা আবশ্যক নয়, কিন্তু এটি যুক্ত করা একটি যুক্তিসঙ্গত বিষয় কারণ এই শাখার উদ্দেশ্য একটি তালিকাতে আপনার নাম যোগ করা।)

## প্রয়োজনীয় পরিবর্তন করুন এবং সেই পরিবর্তনগুলি করুন

এখন একটি টেক্সট এডিটরে `Contributors.md` ফাইলটি খুলুন, এতে আপনার নাম যোগ করুন। ফাইলের শুরুতে বা শেষে যোগ করবেন না। এর মাঝে যে কোন জায়গায় রাখুন। এখন, ফাইলটি সংরক্ষণ করুন।

<img align = "right" width = "450" ​​src = "https://firstcontributions.github.io/assets/Readme/git-status.png" alt = "git status"/>

আপনি যদি প্রকল্প ডিরেক্টরিতে যান এবং `git status` কমান্ডটি চালান, তাহলে আপনি পরিবর্তনগুলি দেখতে পাবেন।

আপনি যে শাখাটি 'git add' কমান্ড ব্যবহার করে তৈরি করেছেন তাতে সেই পরিবর্তনগুলি যুক্ত করুন:

""
git add Contributors.md
""

এখন `git commit` কমান্ড ব্যবহার করে সেই পরিবর্তনগুলি করুন:

""
git commit -m "Add <your-name> to Contributors list"
""

আপনার নামের সাথে '<your-name>' প্রতিস্থাপন করা হচ্ছে।

## গিটহাবের পরিবর্তনগুলি চাপুন

কমান্ড 'git push' ব্যবহার করে আপনার পরিবর্তনগুলি পুশ করুন:

""
git push origin <add-your-branch-name>
""

আপনার পূর্বে তৈরি করা শাখার নামের সাথে '<add-your-branch-name>' প্রতিস্থাপন করা হচ্ছে।

## পর্যালোচনার জন্য আপনার পরিবর্তন জমা দিন

আপনি যদি গিটহাব -এ আপনার সংগ্রহস্থলে যান, আপনি একটি 'তুলনা করুন এবং অনুরোধ করুন' বোতামটি দেখতে পাবেন। সেই বোতামে ক্লিক করুন।

<img style = "float: right;" src = "https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt = "create a pull request"/>

এখন পুল অনুরোধ জমা দিন।

<img style = "float: right;" src = "https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt = "submit pull request"/>

শীঘ্রই আমি এই প্রকল্পের মাস্টার শাখায় আপনার সমস্ত পরিবর্তন একত্রিত করব। পরিবর্তনগুলি একত্রিত হয়ে গেলে আপনি একটি বিজ্ঞপ্তি ইমেল পাবেন।

## এখান থেকে কোথায় যাবেন?

অভিনন্দন! আপনি কেবলমাত্র _fork -> clone -> edit -> pull request_ workflow সম্পন্ন করেছেন যা আপনি প্রায়ই একজন অবদানকারী হিসাবে সম্মুখীন হবেন!

আপনার অবদান উদযাপন করুন এবং [ওয়েব অ্যাপ] (https://firstcontributions.github.io/#social-share) এ গিয়ে আপনার বন্ধু এবং অনুগামীদের সাথে ভাগ করুন।

যদি আপনার কোন সাহায্যের প্রয়োজন হয় বা কোন প্রশ্ন থাকে তাহলে আপনি আমাদের স্ল্যাক টিমে যোগ দিতে পারেন। [স্ল্যাক দলে যোগ দিন] (https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)।

এখন আসুন আপনাকে অন্যান্য প্রকল্পে অবদান দিয়ে শুরু করি। আমরা শুরু করতে পারি এমন সহজ সমস্যাগুলির সাথে প্রকল্পগুলির একটি তালিকা সংকলন করেছি। [ওয়েব অ্যাপে প্রকল্পগুলির তালিকা] (https://firstcontributions.github.io/#project-list) দেখুন।

### [অতিরিক্ত উপাদান] (additional-material/git_workflow_scenarios/additional-material.md)

## অন্যান্য সরঞ্জাম ব্যবহার করে টিউটোরিয়াল