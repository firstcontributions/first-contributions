[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# પ્રથમ યોગદાન

પ્રથમ વખત કંઈક કરવું થોડું મુશ્કેલ છે. ખાસ કરીને જ્યારે તમે જુથ સાથે મળીને કામ કરી રહ્યા હોવ, ત્યારે ભૂલો કરવી એ સારી વાત નથી. પરંતુ એકબીજા સાથે મળીને અને એક જ સાથે કામ કરવું એ જ તો ઓપેન સોર્સ છે. અમે તમારું પ્રથમ ઓપન સોર્સ કોન્ટ્રિબ્યુશન / યોગદાન સરળ બનાવાનો પ્રયત્ન કરીશુ.

ઓનલાઇન આર્ટિકલ્સ વાંચન અને ઓનલાઇન ટ્યુટોરિયલ્સ મદદ કરી શકે છે, પરંતુ પોતે જ તે કામ કરવાથી સારું શું હોઇ શકે? આ પ્રોજેક્ટ તમને તમારી પ્રથમ કોન્ટ્રિબ્યુશન માટે દિશા નિર્દેશ આપશે. જો તમે તમારું પ્રથમ કોન્ટ્રીબ્યુશન કરવા માંગો છો તો આગળ આપેલા પગલાઓ અનુસરો.

જો તમે કમાન્ડ લાઇન સાથે આરામદાયક ન હોવ, તો અહીં [ GUI ટૂલ્સનો ઉપયોગ કરવાના ટ્યુટોરિયલ્સ ](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools) આપેલ છે.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

જો તમારા કમ્પ્યુટર પર Git ઇન્સ્ટોલ નથી, [ તો Git ઈન્સ્ટોલ કરો](https://help.github.com/articles/set-up-git/)


## રિપોઝીટરીને ફોર્ક કરો

ફોર્ક(કાંટા) બટન પર ક્લિક કરવાથી આ રિપોઝીટરી ફોર્ક થાય છે, આ તમારા GitHub એકાઉન્ટમાં આ રિપોઝીટરીની એક નકલ (કોપી) બનાવશે.


## રિપોઝીટરી ક્લોન કરો

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />


હવે તમે આ રેપો તમારા કમ્પ્યુટરમાં ક્લોન કરો (અર્થાત ડાઉનલોડ કરો). તમારા GitHub એકાઉન્ટ પર જાવ, ક્લોન બટન પર ક્લિક કરો અને પછી `copy to clipboard` આઇકોન પર ક્લિક કરો. આનાથી એ રેપોજીટરીનો યુઆરએલ કોપી થશે.


તમારા કમ્પ્યુટર પર એક ટર્મિનલ / કમાંડ પ્રોમ્પ્ટ ખોલો અને નીચે દર્શાવ્યા મુજબ git આદેશ ચલાવો:

```
git clone "યુઆરએલ જે તમે હમણાં જ નકલ(ક્લોન) કરી"
```


જ્યાં "યુઆરએલ જે તમે હમણાં જ કોપી કર્યું છે" (અવતરણ ચિહ્નો સિવાય) એ આ રિપોઝીટરી(આ પ્રોજેક્ટનો તમારો ફૉર્ક) ની URL ના સંગ્રહ માટે છે. તેની URL ને મેળવવા માટે પાછલા પગલાં જુઓ. તેમને કોપી કરેલ યુઆરએલ સાથે બદલી કાઢો.

ઉદાહરણ તરીકે:

```
git clone https://github.com/આ-તમે-છો/first-contributions.git
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />


'આ-તમે-છો' તમારા GitHub એકાઉન્ટનું `username` છે. અહીં તમે તમારા કમ્પ્યુટરમાં GitHub થી first-contributions રિપોને કોપી કરી રહ્યા છો અથવા તેના એક સ્થાનિક / લોકલ કોપી બનાવી રહ્યા છે.

## એક બ્રાંચ બનાવો

તમારા કમ્પ્યુટર પર બનાવેલ રિપોઝીટરીની કોપીનાં ફોલ્ડર / ડિરેક્ટરીમાં જાવ (જો હજુ સુધી તમે ત્યાં ન હોવ તો નીચે આપેલ Command(આદેશ) ચલાવો)


```
cd first-contributions
```


હવે 'git checkout' command(આદેશ) નો ઉપયોગ કરીને એક નવી શાખા(Branch) બનાવો. નવી શાખા(Branch) બનાવવા માટે -b વિકલ્પનો ઉપયોગ થાય છે.

```
git checkout -b <તમારી-શાખા-નામ-ઉમેરો>
```

ઉદાહરણ તરીકે:

```
git checkout -b add-alonzo-church
```


(શાખા(Branch)ના નામમાં 'add' ઉમેરવાની જરૂર નથી, પરંતુ તેમાં શામેલ કરવું યોગ્ય છે કારણ કે શાખા(Branch)નો હેતુ એક નામ છે, જે નામ ઉમેરવાનું છે.)

## આવશ્યક ફેરફારો કરો અને તે ફેરફારોને કમીટ કરો-


હવે 'Contributors.md` ફાઇલને એક ટેક્સ્ટ એડિટરમાં ખોલો અને તેમા તમારુ નામ લખો. ફાઇલની શરૂઆત અથવા અંતે ઉમેરવાને બદલે, તેને મધ્યમાં ગમે ત્યાં રાખો. હવે, ફાઇલને સેવ કરો.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


જો તમે પ્રોજેક્ટની ડાઈરેક્ટરીમા જશો અને કમાન્ડ પ્રોમ્પ્ટમાં `git status` નિર્દેશ ચલાવશો, તો તમે કરેલા પરિવર્તન જોઈ શક્શો. તે પરિવર્તન બનાવવામાં આવેલ શાખા(Branch)માં ઉમેરવા માટે 'git add` કમાન્ડ વાપરો.


```
git add Contributors.md
```


હવે તમારા પોતાના ફેરફારોને 'git commit' આદેશનો ઉપયોગ કરી કમીટ કરો.

```
git commit -m "Add <તમારુ-નામ> to Contributors list"
```

<તમારુ નામ> ની જગ્યાએ તમારું નામ દાખલ કરો


## 
તમારા ફેરફારો ને Github માં પુશ કરો (ધકેલો).

`git push` ઉપયોગ કરીને તમારા પરિવર્તન ને પુશ કરો

```
git push origin <તમારી-શાખા-નામ-ઉમેરો>
```

`<તમારી-શાખા-નામ-ઉમેરો>` ની જગ્યાએ તમારી શાખા(Branch)નુ નામ ઉમેરો.

## તમારા ફેરફારોના રીવ્યુ માટે સબમિટ કરો


જો તમે તમારા github એકાઉન્ટ પર તમારી રિપો માં જાવ તો Compare & pull request નો ઓપ્શન હશે. તેને દબાવો.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

હવે તમારી pull request સબમિટ કરો.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
ટૂંક સમયમાં હું તમારા ફેરફારો માટે આ પ્રોજેક્ટની માસ્ટર શાખામાં મર્જ ક્રી દઇશ. તમને એક મેલ આવશે જ્યારે તમારા ફેરફારો મર્જ થશે.


## હવે, અહીંથી ક્યાં જવું ?

અભિનંદન!:tada: તમે હમણાં જ સ્ટાન્ડર્ડ `fork -> clone -> edit -> pull request` વર્કફ્લો પૂર્ણ કર્યો છે. જેનો તમે વારંવાર સહયોગકર્તા (contributor) તરીકે સામનો કરશો!


તમારા પ્રથમ યોગદાનની ઉજવણી કરો અને [વેબ એપ્લિકેશન](https://firstcontributions.github.io/#social-share) પર જઈને તમારા મિત્રો અને ફોલોઅર્સ સાથે શેર કરો.



જો તમને કોઈ મદદની જરૂર હોય અથવા તમારી કોઈ સમસ્યા હોય તો તમે અમારી સ્લેક ટીમમા જોડાઈ શકો છો. [સ્લેક ટીમ જોઈન કરો.](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)


ચાલો, હવે તમને અન્ય પ્રોજેક્ટ્સમાં કંટ્ર્રીબ્યુટ કરવામા મદદ કરુ. અમે તમારા માટે એક યાદી બનાવી છે જેમા ખૂબ સરળ issues(મુદ્દાઓ) છે વેબ એપમા પ્રોજેક્ટ્સ ની સૂચિ જુઓ.](https://firstcontributions.github.io/#project-list)

## અન્ય સાધનોનો ઉપયોગ કરીને ટ્યુટોરીયલ્સ

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
