પ્રથમ ફાળો
પ્રથમ વખત કંઇક કરવું મુશ્કેલ છે. ખાસ કરીને જ્યારે તેઓ ભૂલો જ્યારે તમે કામ કરી રહ્યા છે એક સારી બાબત નથી | પરંતુ એકબીજા સાથે મળવું અને મળીને કામ કરવું એ ફક્ત ખુલ્લા સ્રોત છે. અમે તમને તમારા પ્રથમ ઓપન સોર્સ યોગદાન / યોગદાનને વધુ સરળ બનાવવામાં સહાય કરીશું.

લેખો તમને જોવા અને ઓનલાઇન Tutoriyljh વાંચી છે, પરંતુ અહીં કંઈક ખોટું થયું વગર તેઓ સારા કામ કરી શકો છો મદદ કરી શકે? આ પ્રોજેક્ટ તમને તમારા પ્રથમ યોગદાનમાં માર્ગદર્શન આપવામાં મદદ કરશે. યાદ રાખો - તમે જે વધુ તાણ શીખી શકો છો, તેટલી સારી રીતે તમે શીખી શકો છો. જો તમે તમારું પ્રથમ ફાળો આપવા માંગતા હોવ તો આપેલ પગલાઓને અનુસરો.

જો ગીટ તમારા કમ્પ્યુટર પર નથી, તો તેને ઇન્સ્ટોલ કરો

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

જો ગીટ તમારા કમ્પ્યુટર પર નથી, તો [ઇન્સ્ટોલ કરો](https://help.github.com/articles/set-up-git/)

## રિપોઝીટરી ક્લોન
<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

હવે તમારે આને તમારા કમ્પ્યુટરમાં ક્લોન કરવું પડશે. તમારા એકાઉન્ટના એકાઉન્ટ પર જાઓ, ક્લોન બટનને ક્લિક કરો અને પછી ક્લિપબોર્ડ આયકન પર કૉપિ પર ક્લિક કરો.

તમારા કમ્પ્યુટર પર ટર્મિનલ / કમાન્ડ પ્રોમ્પ્ટ ખોલો અને નીચેના git આદેશને ચલાવો:
```
git clone "यूआरएल जिसे आपने अभी कॉपी किया"
```
<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />
'આ-તમે-હો' એ તમારા ગિથહબ એકાઉન્ટનું નામ છે. અહીં તમે તમારા કમ્પ્યુટરમાં ગિથહબ સાથે ફર્સ્ટ-ફાળો રેપો કૉપિ કરી રહ્યાં છો અથવા તેની સ્થાનિક / સ્થાનિક કૉપિ બનાવી રહ્યા છો.

## એક બ્રાન્ચ બનાવો

તમારા કમ્પ્યુટર પર બનાવેલ રિપોઝીટરીની કૉપિની ફોલ્ડર / ડાયરેક્ટરી પર જાઓ (જો હજી સુધી નહીં, તો નીચે આપેલ આદેશ ચલાવો)

```
cd first-contributions
```
હવે 'ગીટ ચેકઆઉટ' આદેશનો ઉપયોગ કરીને નવી શાખા બનાવો.
-B વિકલ્પનો ઉપયોગ નવી શાખા બનાવવા માટે થાય છે.

ઉદાહરણ તરીકે:
```
git checkout -b add-alonzo-church
```
(શાખાના નામ પર 'ઍડ' ઉમેરવાની કોઈ જરૂર નથી, પરંતુ તેને શામેલ કરવાનો સારો વિચાર છે કારણ કે શાખાના હેતુને તેનું નામ સૂચિમાં ઉમેરવાનું છે.)

## આવશ્યક ફેરફારો કરો અને તે ફેરફારો કરો -

હવે ટેક્સ્ટ એડિટરમાં 'contributributors.md` ફાઇલ ખોલો અને તમારું નામ લખો. ફાઇલના પ્રારંભ અથવા અંતમાં તેને ઉમેરશો નહીં. તેને મધ્યમાં ગમે ત્યાં રાખો.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />


જો તમે 'git status' સૂચનાને ચલાવો છો, તો તમે જે ફેરફારો કર્યા છે તે જોશો.

બનાવેલી શાખામાં તે ફેરફારો ઉમેરવા માટે 'ગિટ ઍડ' આદેશનો ઉપયોગ કરો.

```
git add Contributors.md
```

હવે 'git commit' આદેશનો ઉપયોગ કરીને, તમારા ફેરફારો કરો.

```
git commit -m "Add <आपका-नाम> to Contributors list"
```

<તમારું નામ> ને બદલે તમારું નામ દાખલ કરો.

## ગિથબમાં તમારા ફેરફારોને દબાણ કરો.

`Git push` નો ઉપયોગ કરીને તમારા ફેરફારને દબાણ કરો.

```
git push origin <अपनी-शाखा-का-नाम-जोड़ें>
```

`<ઉમેરો-નામ-તમારી-શાખા>` ને બદલે તમારી શાખાનું નામ દાખલ કરો.

## તમારા ફેરફારોને સમીક્ષા માટે સબમિટ કરો.

જો તમે તમારા ગિથબ પ્રોફાઇલ પર તમારા રેપો પર જાઓ છો, તો તમે તુલના અને વિનંતીને ખેંચવાની વિકલ્પ જોશો. તેને દબાવો.
<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

હમણાં તમારા ખેંચવાની વિનંતી સબમિટ કરો.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />
ટૂંક સમયમાં હું ક્રમ આ પ્રોજેક્ટના મુખ્ય શાખા મર્જ થશે તમારા ફેરફારો | જ્યારે તમારા ફેરફારો મર્જ થશે ત્યારે તમને એક મેચ મળશે.

## અહીંથી ક્યાંથી જવું?

અભિનંદન! તમે હમણાં જ _fork પૂર્ણ કરી લીધી -> ક્લોન -> ફેરફાર કરો -> PR_ વર્કફ્લો કે જે તમે વારંવાર ફાળો આપનાર તરીકે ઊભી કરશે!

તમારા પ્રથમ યોગદાનને આનંદ ઉજવણી અને તમારા મિત્રો [વેબ એપ્લિકેશન] (https://roshanjossey.github.io/first-contributions/#social-share) PE જેકેટ સાથે શેર |

તમે અમારી ટીમ નબળી જોડાઇ શકે જો તમે કોઇ મદદની જરૂર હોય અથવા કોઇ મુશ્કેલી હોય તો | [સ્લેક જોડાઓ PE] (https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

હવે તમે વધુ પ્રોજેક્ટ્સમાં ફાળો આપવાનું શરૂ કરી શકો છો. અમે તમારા માટે એક સૂચિ બનાવી છે જે ખૂબ જ સરળ સમસ્યાઓ છે. [પ્રોજેક્ટો યાદી] (https://roshanjossey.github.io/first-contributions/#project-list)

## અન્ય સાધનોનો ઉપયોગ કરીને ટ્યુટોરીયલ

|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## સ્વયં પ્રમોશન

જો તમને આ પ્રોજેક્ટ ગમે છે, તો તેને [ગિથબબ] સ્ટાર કરો (https://github.com/Roshanjossey/First-contributions).
જો તમે ખાસ કરીને ચેરિટેબલ અનુભવો છો, તો [રોશન] (https://roshanjossey.github.io/) ટ્વિટર અનુસરો અને
[ગિથબબ] (https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>

