Here’s the README file translated into the Kathiyawadi language for your GitHub project:

---

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# પેહલુ યોગદાન

પેહલી વાર કઈક કરવુ થોડુ ઓખુ છે, ખાસ કરી ને જારે તમારે ભેગા કામ કરવુ છે. પણ ભુલ करवામા कोई હરજ નથી. જમણु Open Source यही छे. आम्हे तमारे પેહला યોગદાન सरल करवानी कोशिश करिशु.

આર્ટિકલ અને ઓનলাইন ટ્યુટોરીયલ मददगार होई शके छे, पण आपणे हस्वे जो काम करिशु इतलु वधारे शिखवा मले. आ प्रोजेक्ट तमने तमारा पेला યोगदान माटे दिशा बतावशे. जो तमारे तमारु पेलु યोगदान आपवु छे, तो आ स्टेप्स ने फोलो करो.

जो तमे Command Line थी अरामदायक न हो, तो अही [GUI Tools न ट्यूटोरियल्स](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools) मली शके छे.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

जो तमारा कंप्युटर पर Git नथी, [तो Git Install करो](https://help.github.com/articles/set-up-git/)

## રિપોઝીટરી ને Fork करो

Fork બટન दबा ने आ रेपोसिटोरी ने Fork करो, जे तमारा GitHub अकाउंट माटे आ रेपोसिटोरी नी Copy बणशे.

## રિપોઝીટરી ને Clone करो

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

हवे तमे आ रेपो ने तमारा कंप्युटर म Clone करो (अर्थात Download करो). तमारा GitHub अकाउंट पर जाव, Clone बटन दबाओ और 'Copy to Clipboard' Icon दबाओ.

तमारा कंप्युटर मा Terminal / Command Prompt खोलो अने नीचे दाखवेलो Git Command चलाओ:

```
git clone "URL जे तमे अभी-अभी Copy करी"
```

"URL जे तमे अभी-अभी Copy करी" (बिना Quotes) आ रेपो नी URL है. अनी URL ने माटे पिछले Step ने फोलो करो.

Example:

```
git clone https://github.com/आ-तमे-छो/first-contributions.git
```

'आ-तमे-छो' तमारा GitHub अकाउंट नु Username छे. अही तमे तमारा कंप्युटर मा GitHub थी first-contributions रेपो ने Copy करि रहा छो अथवा अनी Local Copy बनावि रहा छो.

## એક Branch बनावो

तमारा कंप्युटर मा बनवेलो रेपो ना Folder / Directory मा जावो (जो तमारा हो न हो तो नीचे नी Command चलाओ):

```
cd first-contributions
```

हवे 'git checkout' Command नो उपयोग करो अने एक नवी Branch बनावो. नवी Branch बनाव माटे -b विकल्प नु उपयोग थाए छे.

```
git checkout -b <तमारी-शाखा-नाम-उमेरो>
```

Example:

```
git checkout -b add-alonzo-church
```

(Branch नाम मा 'add' उमेरवानी जरूर नथी, पण ए उमेरवी ठीक छे कारण Branch नो हड्तु एक नाम छे, जे नाम उमेरवु छे.)

## जरूरी फेरफार करो अने ते फेरफार ने Commit करो

हवे 'Contributors.md` File ने एक Text Editor मा खोलो अने तमा तमारु नाम उमेरो. File नी शुरुआत अथवा अंत मा उमेरता नहीं, तमे जेथे चाहे तमे नाम उमेरो. हवे, File ने Save करो.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

जो तमे प्रोजेक्ट नी Directory मा जशो अने `git status` Command चलावशो, तो तमे तमे जे फेरफार कऱ्या तेम जोई शको. ते फेरफार ने बनवेली Branch मा उमेरवा माटे 'git add' Command वापरो.

```
git add Contributors.md
```

हवे तमारा फेरफार ने 'git commit' Command नो उपयोग करी Commit करो:

```
git commit -m "Add <तमारु-नाम> to Contributors list"
```

<तमारु-नाम> नी जगे तमारु नाम उमेरो.

## तमारा फेरफार ने GitHub मा Push करो

'git push' उपयोग करी तमारा परिवर्तन ने Push करो:

```
git push origin <तमारी-शाखा-नाम-उमेरो>
```

' <તમારી-શાખા-નામ-ઉમેરો>' ની જगे તमारु શાખા(Branch) નु નામ ઉમેરો.

## તારા ફેરફારો ના રીવ્યુ માટે સબમિટ કરો

જો તमे तमारा GitHub अकाउंट पर तमारी रेपो मा जाव तो Compare & pull request नो विकल्प होशे. ते दबाओ.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

હવે તमारૂ pull request સબમિટ કરો.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

ટૂંક સમયમાં હું તારા ફેરફારો માટે આ પ્રોજેક્ટ ની master branch મા merge કરી દઈશ. તને mail આવશે જયારે તારા ફેરફારો merge થશે.

## હવે, અહિથી શું કરવું?

અભિનંદન! 🎉 તું હવે જમરા જ 'fork -> clone -> edit -> pull request' Workflow પૂરો કરયો છે. જેનો તને વારંવાર Contributor તરીકે સામનો કરવો પડશે!

તમારા પેલા યોગદાન नी ઉજવણી करो और [वेब एप](https://firstcontributions.github.io/#social-share) पर जाव और तमारा मित्रो साथे शेर करो.

जो तमने कोई मदद नी जरूर हो अथवा तमारी कोई समस्या हो तो तमारे slack टीम मा शामिल थई शको. [slack टीम ने join करो.](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

ચાલો, હવે તમે ને અન્ય પ્રોજેક્ટ માં Contribution करवामा મદદ કરु. અમે तमारा माटे एक सूची बनावी छे जै मा सरल Issues छे. [વેબ એપમા Project ની सूची જુઓ.](https://firstcontributions.github.io/#project-list)

## અન્ય સાધનો નો ઉપયોગ કરીને ટ્યુટોરીયલ

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-t
