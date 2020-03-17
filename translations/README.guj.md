[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)
# પ્રથમ યોગદાન

પ્રથમ વખત કંઈક કરવું મુશ્કેલ છે. ખાસ કરીને જ્યારે તમે મળીને કામ કરી રહ્યા હોવ ત્યારે ભૂલો કરવી સારી વાત નથી. પરંતુ એકબીજા સાથે મળીને અને એક જ જોડે કામ કરવું એ જ તો ઓપેન સોર્સ છે. અમે તમારો પ્રથમ ઓપન સોર્સ કોન્ટ્રિબ્યુશન / યોગદાન સરળ બનાવાનો પ્રયત્ન કરીશુ.

આર્ટિકલ્સ વાંચન અને ઑનલાઇન ટ્યુટોરિયલ્સ મદદ કરી શકે છે, પરંતુ પોતે તે કામ કરવાથી સારું શું હોઇ શકે? આ પ્રોજેક્ટ તમે તમારી પ્રથમ કોન્ટ્રિબ્યુશન માટે દિશા નિર્દેશ આપશે. જો તમે તમારી પ્રથમ કોન્ટ્રીબ્યુશન કરવા માંગો છો તો આગળ આપેલી સ્ટેપ્સને અનુસરો.

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

જો તમારા કમ્પ્યુટર પર ગિટ નથી, [ તો install કરો](https://help.github.com/articles/set-up-git/)


## રિપોઝીટરીને ફોર્ક

કાંટા (ફોર્ક) બટન પર ક્લિક કરવાથી આ રિપોઝીટરી ફૉર્ક થાય છે, આ તમારા GitHub એકાઉન્ટમાં આ રિપોઝીટરીની એક નકલ (કૉપિ) બનાવશે.


## રિપોઝીટરી ક્લોન

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />


હવે તમે આ રેપો તમારા કમ્પ્યુટરમાં ક્લોન કરો (અર્થ ડાઉનલોડ કરો). તમારા ગિટહબ એકાઉન્ટ પર જાવ, ક્લોન બટન પર ક્લિક કરો અને પછી કૉપિ ટુ ક્લિપબોર્ડ આઇકોન પર ક્લિક કરો.


તમારા કમ્પ્યુટર પર એક ટર્મિનલ / કમાંડ પ્રોમ્પ્ટ ખોલો અને નીચેનું git આદેશ ચલાવો:

```
git clone "યુઆરએલ જે તમે હમણાં જ નકલ(ક્લોન) કરી"
```


જ્યાં "યુઆરએલ જે તમે હમણાં જ કૉપિ કર્યું છે" (સિવાય અવતરણ ચિહ્નો) આ સંગ્રહ માટે URL છે. (આ પ્રોજેક્ટનો તમારો ફૉર્ક) URL ને મેળવવા માટે પાછલા પગલાં જુઓ.

ઉદાહરણ તરીકે:

```
git clone https://github.com/આ-તમે-છો/first-contributions.git
```

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />


'આ-તમે-છો' તમારા ગીટબબ એકાઉન્ટનું નામ છે. અહીં તમે તમારા કમ્પ્યુટરમાં GitHub થી પ્રથમ-કંટ્રિબ્યુશન્સ રિપોને કૉપિ કરી રહ્યા છો અથવા તેના એક સ્થાનિક / લોકલ કૉપિ બનાવી રહ્યા છે.

## એક બ્રાંચ બનાવો

તમારા કમ્પ્યુટર પર બનાવેલ રિપોઝીટરીની કૉપિનાં ફોલ્ડર / ડિરેક્ટરીમાં જાવ (જો હજુ સુધી ન હોય તો નીચે આપેલ આદેશ ચલાવો)


```
cd first-contributions
```


હવે 'git checkout' આદેશનો ઉપયોગ કરીને એક નવી શાખા બનાવો. નવી શાખા બનાવવા માટે -b વિકલ્પનો ઉપયોગ થાય છે.

```
git checkout -b <તમારી-શાખા-નામ-ઉમેરો>
```

ઉદાહરણ તરીકે:

```
git checkout -b add-alonzo-church
```


(શાખાના નામમાં 'add' ઉમેરવાની જરૂર નથી, પરંતુ તેમાં શામેલ કરવું યોગ્ય છે કારણ કે આ શાખાનો હેતુ એક નામ છે, જે નામ ઉમેરવાનું છે.)

## આવશ્યક ફેરફારો કરો અને તે ફેરફારોને કમીટ કરો-


હવે 'Contributors.md` ફાઇલને એક ટેક્સ્ટ એડિટરમાં ખોલો અને તેના નામ લખો. ફાઇલની શરૂઆત અથવા અંતે તેમાં ઉમેરો. તેને મધ્યમાં ગમે ત્યાં રાખો.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />


જો તમે `git status` નિર્દેશ ચલાવશો, તો તમે કરેલા પરિવર્તન જોઈ શક્શો. તે પરિવર્તન બનાવવામાં આવેલ શાખામાં ઉમેરવા માટે 'git add` કમાન્ડ વાપરો.


```
git add Contributors.md
```


હવે તમારા પોતાના ફેરફારોને કમીટ કરો 'git commit કરો' આદેશનો ઉપયોગ કરી.

```
git commit -m "Add <તમારુ-નામ> to Contributors list"
```

<તમારુ નામ> ની જગ્યાએ તમારું નામ દાખલ કરો


## 
તમારા ફેરફારો ને Github માં પુશ કરો

`git push` ઉપયોગ કરીને તમારા પરિવર્તન ને પુશ કરો

```
git push origin <તમારી-શાખા-નામ-ઉમેરો>
```

`<તમારી-શાખા-નામ-ઉમેરો>` ની જગ્યાએ તમારી શાખાનુ નામ ઉમેરો.

## તમારા ફેરફારોના રીવ્યુ માટે સબમિટ કરો


જો તમે તમારા github એકાઉન્ટ પર તમારી રિપો માં જાવ તો Compare & pull request નો ઓપ્શન હશે. તેને દબાવો.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

હવે તમારી pull request સબમિટ કરો.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />
ટૂંક સમયમાં હું તમારા ફેરફારો માટે આ પ્રોજેક્ટની માસ્ટર શાખામાં મર્જ ક્રી દઇશ. તમને એક મેલ આવશે જ્યારે તમારા ફેરફારો મર્જ થશે.


## અહીંથી ક્યાં જાઓ ?

અભિનંદન! તમે હમણાં જ પૂર્ણ કર્યું છે _ફૉર્ક -> ક્લોન -> edit -> PR_ વર્કફ્લો જે તમે વારંવાર સહયોગકર્તા (contributor) તરીકે સામનો કરશો!


તમારા પ્રથમ યોગદાનની ઉજવણીમાં ઉજવણી કરો અને તમારા મિત્રો સાથે શેર કરો [વેબ એપ્લિકેશન](https://roshanjossey.github.io/first-contributions/#social-share) પર જઈને | 


તમે અમારી સ્લેક ટીમને જોડો છો જો તમને કોઈ મદદની જરૂર હોય અથવા તમારી કોઈ સમસ્યા હોય તો [સ્લેક પે join કરો](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

હવે તમે અને પ્રોજેક્ટ્સમાં કંટ્ર્રીબ્યુટ કરવાનું શરૂ કરો. અમે તમારા માટે એક યાદી બનાવી છે જેમા ખૂબ સરળ મુદ્દાઓ છે [પ્રોજેક્ટ્સ ની સૂચિ]
(https://roshanjossey.github.io/first-contributions/#project-list)

## અન્ય સાધનોનો ઉપયોગ કરીને ટ્યુટોરીયલ

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|
