Here’s the Hindi translation of your Git commit log guide in the same format:

---

# कमिट लॉग देखें

किसी ब्रांच या फ़ाइल के कमिट लॉग की जाँच करने के लिए, निम्नलिखित कमांड का उपयोग किया जा सकता है:

```bash
git log [options] [path]
```

इस कमांड का आउटपुट डिफ़ॉल्ट रूप से उल्टे कालानुक्रमिक क्रम (reverse chronological order) में दिया जाता है।

---

## कमांड आउटपुट उदाहरण

```bash
$ git log
commit e3fabb30ab536bd5876461d8a749301a321e714f (HEAD -> check-commit-log-ko, upstream/main, origin/main, origin/HEAD, main)
Author: Dan Yunheum Seol <yunheum.seol@mail.mcgill.ca>
Date:   Tue Jun 4 01:07:25 2024 -0400

    Add dan-seol to Contributors list (#84962)

commit 4af4ec8a56e057ce8768af77eda528453974d0bc
Author: Edgar Humberto Tijerina Tamez <168693312+EdgarHTT@users.noreply.github.com>
Date:   Mon Jun 3 23:06:05 2024 -0600

    Add Edgar Tijerina to Contributors list (#84961)
```

---

## कमांड वेरिएशन्स और ऑप्शन्स

### किसी विशेष कमिट आईडी से पहुँचे हुए कमिट्स देखने के लिए:

(इस उदाहरण में `foo` और `bar`)

```bash
git log foo bar
```

### किसी कमिट आईडी से पहुँचे हुए कमिट्स को हटाना:

`^` चिह्न कमिट आईडी के आगे लगाकर किया जा सकता है। (इस उदाहरण में `baz`)

```bash
git log foo bar ^baz
```

### किसी विशेष फ़ाइल के लिए कमिट लॉग:

```bash
git log --all <filename>
```

### लॉग में कमिट्स की संख्या सीमित करना:

(इस उदाहरण में 5)

```bash
git log -n 5
```

---

## संदर्भ

[Git आधिकारिक डॉक्यूमेंटेशन](https://git-scm.com/docs/git-log)

---


