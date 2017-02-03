# प्रथम योगदान

<img align="right" width="300" src="assets/fork.png" alt="fork this repository" />

अन्य भाषाओं में इस पढ़ें: [अंग्रेजी](README.md), [स्पेन](README.es.md), [डच](README.nl.md), [हिंदी](README.hi.md) 

आप अपने मशीन पर Git नहीं है तो, [इसे स्थापित करें] (https://help.github.com/articles/set-up-git/)

## कांट इस भंडार 

कांटा बटन पर क्लिक करके इस रेपो कांटा

## रिपोजिटरी क्लोन

<img align="right" width="300" src="assets/clone.png" alt="clone this repository" />

अब आप अपने मशीन को यह रेपो क्लोन। क्लोन बटन पर क्लिक करें और फिर कॉपी आइकन क्लिपबोर्ड

एक टर्मिनल खोलें और निम्न git आदेश चलाएँ:

```
git clone "यूआरएल का नकल "
```

कहाँ "यूआरएल का नकल" (उद्धरण चिह्नों के बिना) इस भंडार के लिए यूआरएल  है। यूआरएल प्राप्त करने के लिए पिछले चरण देखें।

उदाहरण के लिए:

```
git clone https://github.com/यह तुम हो/first-contributions.git
```

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

' यह तुम हो 'अपने GitHub उपयोगकर्ता नाम है। यहाँ आप अपने कंप्यूटर के लिए GitHub में पहली योगदान भंडार की सामग्री नकल कर रहे हैं

## एक शाखा बनाएं

आपके कंप्यूटर पर रिपोजिटरी निर्देशिका के लिए परिवर्तित करें अगर आप पहले से ही वहाँ नहीं कर रहे हैं।

```
cd first-contributions
```

अब एक शाखा  बना  `git checkout command` उपयोग करके

```
git checkout -b <अपना नाम जोड़>
```

उदाहरण के लिए:

```
git checkout -b add-alonzo-church
```

## आवश्यक परिवर्तन करें और उन परिवर्तनों के लिए प्रतिबद्ध

अब खुले `Contributors.md` फ़ाइल एक पाठ संपादक में और इसे आपके नाम जोड़, और फ़ाइल सहेजें। आप अगर इस परियोजना निर्देशिका कर और `git status` करते हैं, तो आप परिवर्तन देखेंगे। उन परिवर्तनों को नीचे `git add` commad का उपयोग कर जोड़ें।

```
git add Contributors.md 
```

अब नीचे `git commit` आदेश का उपयोग उन परिवर्तनों को प्रतिबद्ध है।

```
git commit -m "Add <आपका-नाम> to Contributors list"
```

आपके नाम के साथ `<आपका-नाम>` की जगह

## GitHub में परिवर्तन पुश

`git push` का उपयोग कर अपने परिवर्तन धक्का

```
git push origin <अपना नाम जोड़>
```

बदलें `<अपना नाम जोड़>` शाखा आपने पहले बनाया के नाम के साथ

## समीक्षा के लिए अपने परिवर्तनों को जमा करें

आप GitHub पर अपने भंडार के लिए जाना है, तो आप देख `Compare & pull request` बटन खींच लेंगे। उस बटन पर क्लिक करें।

<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

अब पुल अनुरोध सबमिट करें।

<img style="float: right;" src="assets/submit-pull.png" alt="submit pull request" />

## अपने कांटा इस भंडार के साथ समन्वयित रखते हुए

अब मैं इस परियोजना के मास्टर शाखा में अपने सभी परिवर्तन विलय हो जाएगा। अपने कांटा उन परिवर्तनों की जरूरत नहीं होगी। आदेश में अपने कांटा खान के साथ समन्वयित रखने के लिए, `upstream remote url` के रूप में मेरे रेपो के यूआरएल जोड़ें।

```
git remote add upstream https://github.com/multunus/first-contributions
```

यह git को इस परियोजना के दूसरे संस्करण निर्दिष्ट यूआरएल में मौजूद बताने का एक तरीका है और हम इसे मास्टर बुला रहे हैं। एक बार परिवर्तन विलय कर रहे हैं, मेरे रिपॉजिटरी के नए संस्करण लाने।

```
git fetch upstream
```

यहाँ हम अपने कांटा (अपस्ट्रीम दूरदराज) में सभी परिवर्तन ला रहे हैं। अब, आप अपने गुरु शाखा में अपने भंडार के नए संशोधन विलय करने की जरूरत है। 

```
git rebase upstream/master
```

यहाँ आप सभी परिवर्तनों को आप गुरु शाखा को दिलवाया आवेदन कर रहे हैं। तुम अब मास्टर शाखा धक्का, अपने कांटा भी परिवर्तन होगा

```
git push origin master
```

यहां सूचना आप दूरदराज के नाम पर रखा मूल करने के लिए जोर दे रहे हैं।

## यहाँ से कहाँ जाएं ?

आप : [Contributor.ninja](https://contributor.ninja) पर कई शुरुआत के अनुकूल मुद्दों मिलेगा।

यहाँ लोकप्रिय रेपो कि आप को हल कर सकते हैं में कुछ शुरुआत के स्तर के मुद्दों है। आगे बढ़ो और अधिक जानने के लिए उन रेपो करने के लिए जाना

|[![exercism](https://avatars2.githubusercontent.com/u/5624255?v=3&s=100)](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[![fun-retro](https://avatars3.githubusercontent.com/u/15913975?v=3&s=100)](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[<img width="100" src="https://cdn.worldvectorlogo.com/logos/react.svg">](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[![habitat](https://avatars1.githubusercontent.com/u/18171698?v=3&s=100)](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![scikit-learn](https://avatars0.githubusercontent.com/u/365630?v=3&s=100)](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[<img width="100" src="https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067">](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[<img width="100" src="https://images.plot.ly/plotly-documentation/thumbnail/numpy-logo.jpg">](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[![elasticsearch](https://avatars2.githubusercontent.com/u/6764390?v=3&s=100)](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|---|---|---|---|---|---|---|---|
|[exercism](https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22)|[Fun Retros](https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly)|[react](https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22)|[habitat](https://github.com/habitat-sh/habitat/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[scikit-learn](https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[Leiningen](https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie)|[numpy](https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22)|[elasticsearch](https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22)|
|[![homebrew](https://avatars2.githubusercontent.com/u/1503512?v=3&s=100)](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[![rust](https://avatars1.githubusercontent.com/u/5430905?v=3&s=100)](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[![vuejs](https://avatars1.githubusercontent.com/u/6128107?v=3&s=100)](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[![Suave](https://avatars2.githubusercontent.com/u/5822862?v=3&s=100)](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[![OpenRA](https://avatars3.githubusercontent.com/u/409046?v=3&s=100)](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[![PowerShell](https://avatars0.githubusercontent.com/u/11524380?v=3&s=100)](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[![coala](https://avatars2.githubusercontent.com/u/10620750?v=3&s=100)](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[![moment](https://avatars2.githubusercontent.com/u/4129662?v=3&s=100)](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[homebrew](https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)|[Rust](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)|[vuejs](https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)|[Suave](https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy)|[OpenRA](https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy)|[PowerShell](https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs)|[coala](https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer)|[moment](https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs)|
|[![ava](https://avatars0.githubusercontent.com/u/8527916?v=3&s=100)](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[![freeCodeCamp](https://avatars0.githubusercontent.com/u/9892522?v=3&s=100)](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![webpack](https://avatars3.githubusercontent.com/u/2105791?v=3&s=100)](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[![hoodie](https://avatars1.githubusercontent.com/u/1888826?v=3&s=100)](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[![pouchdb](https://avatars3.githubusercontent.com/u/3406112?v=3&s=100)](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[![neovim](https://avatars0.githubusercontent.com/u/6471485?v=3&s=100)](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[![babel](https://avatars2.githubusercontent.com/u/9637642?v=3&s=100)](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[<img width="100" src="https://github.com/adobe/brackets/blob/gh-pages/images/brackets_128.png?raw=true">](https://github.com/adobe/brackets/labels/Starter%20bug)|
|[ava](https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22)|[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[webpack](https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22)|[hoodie](https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only)|[pouchdb](https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22)|[neovim](https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level)|[babel](https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly) |[brackets](https://github.com/adobe/brackets/labels/Starter%20bug)|
