[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _Bul hújjetti [basqa tillerde](translations/Translations.md) oqıń._
<kbd>[<img title="Shqip" alt="Shqip" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/al.svg" width="22">](README.al.md)</kbd>
<kbd>[<img title="Armenian" alt="Armenian" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/am.svg" width="22">](README.arm.md)</kbd>
<kbd>[<img title="Uzbek" alt="Uzbek language" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/uz.svg" width="22">](README.uz.md)</kbd>
<kbd>[<img title="Qaraqalpaq" alt="Qaraqalpaq tili" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/uz.svg" width="22">](README.kaa.md)</kbd>

# Birinshi Úles

Bul joба tásinshilerdіń birinshi úlesin qosıwın jеńilletiw hám baqlawǵa baǵıshlanghan. Eger siz birinshi úlesingizdi qosıwdi maqset etseńiz, tómendegishine ámel eting.

_Eger kommanda qatarı menen islewge qolaylı bolmasańız, [GUI qurallarin paydalanıwdıń oqulıqlari bul jerde.](#basqa-qurallar-arqali-oquliqlar)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="repozitoriyani fork qiling" />

#### Eger mashinańızda git bolmasa, [ornating](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Bul repozitoriyani fork eting

Bet jоqarısındaǵı fork túymesin basıw arqalı bul repozitoriyani fork eting.
Bul sizin esabıńızda bul repozitoriyaning kóshirmesin jaratadı.

## Repozitoriyani klonlaw

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="repozitoriyani klonlaw" />

Endi fork qilinghan repozitoriyani mashinańızǵa klonlań. GitHub esabıńızǵa kiriń, fork qilinghan repozitoriyani ashıń, kod túymesin, soń SSH bólimine basing hám _url'di almastiríw buferіne kóshiriw_ belgisine basıń.

Terminal ashıp, tómendegi git buyrıǵın orındań:

```bash
git clone "az ǵana kóshirgen url'ińiz"
```

Munda "az ǵana kóshirgen url'ińiz" (tirnoqshalar menen emes) — bul repozitoriyaǵa URL (bul jobaning sizin fork'ıńız). URL'di alıw ushın aldıńǵı qadamlardı qarań.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL'di almastiríw buferíne kóshiriw" />

Máselen:

```bash
git clone git@github.com:bul-siz-siz/first-contributions.git
```

Munda `bul-siz-siz` — sizin GitHub paydalanıwshı atıńız. Bul jerde siz GitHub'daǵı first-contributions repozitoriyasining mazmunın kompyuteríńizge kóshiresiz.

## Tarmaqlama jaratıń

Kompyuteríńizdegi repozitoriya katalogına ótiń (eger hali ol jerde bolmasańız):

```bash
cd first-contributions
```

Endi `git switch` buyrıǵı arqalı tarmaqlama jaratiń:

```bash
git switch -c sizin-jańa-tarmaqlama-atińız
```

Máselen:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>Eger git switch isletiwde qateler payda bolsa, bul jerni basing:</strong> </summary>

Eger "Git: `switch` is not a git command. See `git –help`" qate xabari payda bolsa, siz git'tiń eskirgen versiyasın isletiip atırǵan bolıwıńız múmkin.

Bul jaǵdayda, orınına `git checkout` isletiw de boladi:

```bash
git checkout -b sizin-jańa-tarmaqlama-atińız
```

</details>

## Kerekli ózgerislerdi kirgiziń hám bul ózgerislerdi tasdiqlań

`Contributors.md` faylın tekst redaktorında ashıń, oǵan atıńızdı qosıń. Faylding basına yamasa aqırına qoymańız. Ortadaǵı islegen jerde qoyıń. Fayldi saqlaň.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Eger joба katalogına barsańız hám `git status` buyrıǵın orındасańız, ózgerisler bolǵanın kóresiz.

Bul ózgerislerdi `git add` buyrıǵı arqalı az ǵana jaratqan tarmaqlamamızǵa qosıń:

```bash
git add Contributors.md
```

Endi bul ózgerislerdi `git commit` buyrıǵı arqalı tasdiqlań:

```bash
git commit -m "Add sizin-atińız Contributors dizimіne"
```

`sizin-atińız` ornına óz atıńızdı jazıń.

## Ózgerislerdi GitHub'qa júklew

Ózgerislerinizdi `git push` buyrıǵı arqalı júkleń:

```bash
git push -u origin sizin-tarmaqlama-atińız
```

`sizin-tarmaqlama-atiníz` ornına az ǵana jaratqan tarmaqlamamızdiń atın jazıń.

<details>
<summary> <strong>Eger júklewde qateler payda bolsa, bul jerni basing:</strong> </summary>

- ### Autentifikaciya Qatesi
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre>
  SSH key'in esabıńızǵa generaciyalaw hám konfiguraciyalaw boyınsha [GitHub oqulıǵına](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) qarań.

</details>

## Ózgerislerinizdi kóriw ushın taqdim eting

Eger GitHub'daǵı repozitoriyańızǵa barsańız, `Compare & pull request` túymesin kóresiz. Bul túymeni basıń.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="salıstırıw hám pull request jaratıw" />

Endi pull request'ti taqdim eting.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="pull request'ti taqdim eting" />

Kóp uzamasdan men sizin barlıq ózgerislerinizdi bul jobaning tiykarǵı tarmaqlamamasına birlestiremen. Ózgerisler birlestiriliwi menen sizge xabar elektron pochta arqalı júberiledi.

## Bunnan keyin qayda barıw kerek?

Qutlıqlańız! Siz úles beriwshi sıpatında kóp ushırasatıǵın standart _fork → klon → redaktirlew → pull request_ jumıs processın tamamladıńız!

Úlesingizdi atap ótıń hám [web ilovasına](https://firstcontributions.github.io/#social-share) kirıw arqalı dostlarıńız hám izbesileriníz menen bólisin.

Eger kóbirek mashq qilǵańız kelse, [kod úleslerine](https://github.com/roshanjossey/code-contributions) qarań.

Endi baslıw ushın basqa jobalárǵa úles qosıwdı dawam ettiriń. Siz baslawıńızǵa bolatıǵın ańsat máselelerı bar jobalardıń dizimін túzip chiqdık. [Web ilova'daǵı jobalardıń dizimіne](https://firstcontributions.github.io/#project-list) qarań.

### [Qosımsha material](additional-material/git_workflow_scenarios/additional-material.md)

## Basqa Qurallar Arqalı Oquliqlar

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
