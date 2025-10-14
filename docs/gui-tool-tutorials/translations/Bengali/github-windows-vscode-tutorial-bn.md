প্রথম অবদান (First Contributions)
<img alt="Visual Studio Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="40">	Visual Studio Code

প্রথমবার কিছু করা সবসময়ই কঠিন। বিশেষ করে যখন আপনি টিমে কাজ করছেন, তখন ভুল করার ভয় থেকেই যায়। কিন্তু ওপেন সোর্স সহযোগিতা আর একসাথে কাজ করার মাধ্যম। আমরা চাই নতুন অবদানকারীদের জন্য প্রথমবার শেখা ও অবদান রাখার প্রক্রিয়াকে সহজ করে তুলতে।

আর্টিকেল পড়া বা টিউটোরিয়াল দেখা সাহায্য করতে পারে, কিন্তু বাস্তবে নিজের হাতে চেষ্টা করার মতো অভিজ্ঞতা আর কিছুতেই নেই। এই প্রোজেক্টের উদ্দেশ্য হলো একটি স্পষ্ট গাইড তৈরি করা এবং নতুনদের জন্য প্রথম অবদান রাখার পদ্ধতিকে সহজ করা। মনে রাখবেন: যত শান্ত থাকবেন, শেখাও তত সহজ হবে।

👉 যদি আপনার মেশিনে Visual Studio Code না থাকে, তবে এখান থেকে ইন্সটল করুন
।

তথ্য: এই টিউটোরিয়ালটি Windows 10 মেশিনে VS Code (ভার্সন 1.27.2) ব্যবহার করে তৈরি করা হয়েছে। এখানে কিছু কিবোর্ড শর্টকাট ব্যবহার করা হয়েছে, যেগুলো অন্য অপারেটিং সিস্টেম (macOS/Linux) বা কিবোর্ড লেআউট অনুযায়ী আলাদা হতে পারে। আপনি চাইলে VS Code-এর Command Palette-এ "shortcut" লিখে আপনার শর্টকাটগুলোর তালিকা দেখতে পারবেন।

এই রিপোজিটরিকে Fork করুন
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

এই পেজের উপরের ডান দিকে Fork বাটনে ক্লিক করুন।
এটি আপনার GitHub অ্যাকাউন্টে এই রিপোজিটরির একটি কপি তৈরি করবে।

GitHub আপনার রিপোজিটরি এবং মূল রিপোজিটরির মধ্যে সম্পর্ক ট্র্যাক করে রাখে।

আপনার রিপোজিটরি Clone করুন
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

এখন রিপোজিটরিটি আপনার মেশিনে ক্লোন করতে হবে।

⚠️ সতর্কতা: অনেক নতুন অবদানকারী ভুল করে মূল রিপোজিটরি ক্লোন করে বসেন। সবসময় নিশ্চিত করুন যে আপনি নিজের ফর্কড রিপোজিটরি ক্লোন করছেন।

VS Code ওপেন করুন → F1 চাপুন → কমান্ড প্যালেটে Git: Clone লিখুন → Enter চাপুন।

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-clone2.png" alt="Paste Repository URL in" />

রিপোজিটরির URL পেস্ট করুন → Enter চাপুন → ফোল্ডার লোকেশন সিলেক্ট করুন।

একটি Branch তৈরি করুন

আবার F1 চাপুন → branch লিখুন → Create Branch সিলেক্ট করুন।

নতুন ব্রাঞ্চের নাম দিন যেমন:

add-david-krol


Enter চাপুন। নতুন ব্রাঞ্চ তৈরি হবে এবং আপনি সেখানেই কাজ শুরু করতে পারবেন।

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-branch.png" alt="Branches Command Palette" />
প্রয়োজনীয় পরিবর্তন করুন

Contributors.md ফাইল ওপেন করুন এবং নিজের নাম যোগ করুন।

👉 অন্য কোনো কন্ট্রিবিউটরের নাম কপি করে তার জায়গায় নিজের নাম বসিয়ে নিতে পারেন, এতে Markdown সিনট্যাক্স সঠিক থাকবে।

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-changes.png" alt="Add your name" />
GitHub এ পরিবর্তনগুলো Push করুন

১. VS Code-এর বাম পাশ থেকে Source Control (Ctrl+Shift+G) আইকন সিলেক্ট করুন।
২. পরিবর্তিত ফাইলগুলো স্টেজ করুন (+ এ ক্লিক করে)।
৩. কমিট মেসেজ লিখুন এবং ✅ চিহ্নে ক্লিক করুন।
৪. তারপর তিন ডট (...) মেনু থেকে Publish Branch নির্বাচন করুন।

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-windows-vs-code-tutorial/vscode-2018-08-push.png" alt="push changes" />
Pull Request (PR) সাবমিট করুন

এখন GitHub এ গিয়ে নতুন ব্রাঞ্চের পাশে থাকা Compare & pull request বাটনে ক্লিক করুন।

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="একটি Pull Request তৈরি করুন" />

এরপর PR সাবমিট করুন।

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Pull Request সাবমিট করুন" />

শীঘ্রই আপনার পরিবর্তনগুলো মূল প্রোজেক্টে merge হবে এবং আপনাকে ইমেইলে নোটিফিকেশন দেওয়া হবে।

এরপর কী?

অভিনন্দন 🎉 আপনি এখনই পুরো প্রক্রিয়াটি শেষ করেছেন:
fork → clone → edit → PR

👉 আপনার অবদান উদযাপন করুন এবং ওয়েব অ্যাপ
 থেকে বন্ধুদের সাথে শেয়ার করুন।

👉 কোনো প্রশ্ন থাকলে আমাদের Slack টিমে যোগ দিন: Slack টিমে যোগ দিন
।

অতিরিক্ত উপকরণ
অন্যান্য টুল ব্যবহার করে টিউটোরিয়াল

মূল পাতায় ফিরে যান