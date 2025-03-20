# ওপেন সোর্স অবদানের জন্য Git অনুমতি ত্রুটি সমাধান

## সমস্যা

আমি "first-contributions" রিপোজিটরিতে অবদান রাখার চেষ্টা করার সময় একটি অনুমতি ত্রুটি পেয়েছিলাম। আমি নতুন ব্রাঞ্চ তৈরি করে এবং পরিবর্তনগুলি পুশ করার চেষ্টা করার পর:

```bash
$ git checkout -b fahimar_oss_YYYY
Switched to a new branch 'fahimar_oss_YYYY'

$ git push origin fahimar_oss_YYYY
remote: Permission to firstcontributions/first-contributions.git denied to fahimar.
fatal: unable to access 'https://github.com/firstcontributions/first-contributions.git/': The requested URL returned error: 403
```

সমস্যাটি ছিল যে, আমি মূল রিপোজিটরিটি সরাসরি ক্লোন করেছিলাম এবং সেখানে পুশ করার চেষ্টা করেছিলাম। একজন বাইরের অবদানকারী হিসেবে, আমার মূল রিপোজিটরিতে লেখার অনুমতি নেই।

## সমাধান

আমি নিম্নলিখিত উপায়ে এই সমস্যাটি সমাধান করেছি:

1. আমার রিমোট URL পরিবর্তন করে এটিকে আমার ব্যক্তিগত ফর্কে পয়েন্ট করানো:

   ```bash
   $ git remote set-url origin https://github.com/yourname/first-contributions.git
   ```

2. রিমোট ঠিকভাবে আপডেট হয়েছে কিনা তা যাচাই করা:

   ```bash
   $ git remote -v
   origin  https://github.com/yourname/first-contributions.git (fetch)
   origin  https://github.com/yourname/first-contributions.git (push)
   ```

3. সফলভাবে আমার ফর্কে পুশ করা:

   ```bash
   $ git push origin fahimar_oss_YYYY
   ```

4. GitHub আমাকে একটি লিঙ্ক দিয়েছিল যাতে আমি আমার ব্রাঞ্চ থেকে পুল রিকোয়েস্ট তৈরি করতে পারি:
   ```
   remote: Create a pull request for 'fahimar_oss_YYYY' on GitHub by visiting:
   remote: https://github.com/fahimar/first-contributions/pull/new/fahimar_oss_YYYY
   ```

## প্রধান শিক্ষা

ওপেন সোর্স অবদানের জন্য সঠিক কাজের ধারাবাহিকতা হল:

1. মূল রিপোজিটরিটি আপনার GitHub অ্যাকাউন্টে ফর্ক করুন
2. আপনার ফর্কটি স্থানীয়ভাবে ক্লোন করুন
3. একটি নতুন ব্রাঞ্চে পরিবর্তন করুন
4. আপনার ফর্কে পুশ করুন
5. আপনার ফর্ক থেকে মূল রিপোজিটরিতে পুল রিকোয়েস্ট তৈরি করুন

যদি আপনি আগে মূল রিপোজিটরি ক্লোন করে থাকেন এবং আপনার ফর্ক না করে থাকেন, তবে উপরে দেখানো মতো রিমোট URL আপডেট করে এটি ঠিক করতে পারেন।
