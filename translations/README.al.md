[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Kontributet e Para


Është gjithmonë e vështirë hera e parë kur bën diçka. Sidomos kur bashkëpunon, të bësh gabime nuk është një ndjenjë e mirë. Ne duam ta thjeshtësojmë mënyrën se si kontribuesit e open-source mësojnë dhe kontribuojnë për herë të parë.
Leximi i artikujve dhe shikimi i tutorialve ndihmojnë, por ç'është më mirë se sa ta bësh këtë gjë në një vend praktik? Prandaj ky projekt synon të udhëzojë dhe të thjeshtësojë mënyrën se si fillestarët e bëjnë kontributin e tyre të parë. Nëse dëshironi të bëni kontributin tuaj të parë, ndiqni hapat më poshtë!

#### *Nëse ende nuk ndiheni rehat me command line, [këtu ke tutoriale që përdorin veglat e GUI]( #tutorials-using-other-tools )*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Nëse nuk e keni Git të instaluar në paisjen tuaj, [instalojeni]( https://help.github.com/articles/set-up-git/).

## Bëni fork këtë repozitor

Për të bërë fork këtë repozitor kliko butonin fork në krye të kësaj faqe. Kjo do të krijojë një kopje të këtij repozitori në llogarinë tuaj.

## Klononi këtë repozitor

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Tani klononi në paisjen tuaj repozitorin që e keni bërë fork paraprakisht. Shkoni tek llogaria juaj e GitHub, hapni repozitorin që e keni bërë fork paraprakisht, klikoni butonin "code" dhe pastaj klikoni ikonën *copy to clipboard*.

Hapni terminalin dhe bëni run git komandën në vazhdim:

```
git clone "url-në që sapo e keni kopjuar"
```
ku "url-në që sapo e keni kopjuar" (pa thonjëzat) është url-ja e këtij repozitori (repozitori që e keni bërë fork). Shiko hapat paraprak për të marrë url-në.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Për shembull:
```
git clone https://github.com/ky-je-ti/first-contributions.git
```
ku `ky-je-ti` është emri juaj në GitHub. Ju këtu i kopjoni përmbajtjet e repozitorit first-contributions në GitHub te kompjuteri juaj.

## Krijoni një degë (branch)

Ndryshoni lokacionin përndryshe direktorinë te repozitori në kompjuterin tuaj (nëse nuk jeni ende në lokacionin e duhur):

```
cd first-contributions
```
Tani krijoni një degë (branch) duke përdorur komandën `git checkout`:
```
git checkout -b <emri-i-degës-tënde>
```

Për shembull:
```
git checkout -b add-filan-fisteku
```
(Emri i degës nuk ka nevojë të ketë fjalën *add* në të, por është një gjë e arsyeshme të përfshihet sepse qëllimi i kësaj dege është të shtojë emrin tuaj në një listë.)

## Bëni ndryshimet e nevojshme dhe bëni commit ato ndryshime

Tani hap fajllin `Contributors.md` në një program për editim të tekstit dhe shtoni emrin tuaj. Mos e shtoni atë në fillim ose në fund të fajllit. Shtojeni ku të doni në mes. Tani, ruani fajllin.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Nëse shkoni te lokacioni i projektit dhe e ekzekutoni komandën `git status`, do shihni se ka ndryshime.


Shtoni këto ndryshime te dega që sapo e krijuat duke përdorur komandën `git add`:

```
git add Contributors.md
```

Tani bëni commit këto ndryshime duke përdorur komandën `git commit`:
```
git commit -m "Add <emri-juaj> to Contributors list"
```
zëvendëso `<emri-juaj>` me emrin tuaj.

## Bëni push (shtyji) ndryshimet në GitHub

Bëni push ndryshimet duke përdorur komandën `git push`: 
```
git push origin <emri-i-degës-tuaj>
```
duke e zëvendësuar `<emri-i-degës-tuaj>` me emrin e degës që krijuat më herët.

## Bëni ndryshimet submit për shqyrtim

Nëse shkoni te repozitori juaj në GitHub, do të shihni një buton `Compare & pull request`. Klikoni në atë buton.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Tani bëni submit këtë pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Së shpejti do t'i bashkoj (bëj merge) të gjitha ndryshimet tuaja te dega master e këtij projekti. Ju do të njoftoheni me e-mail në momentin kur të bëhen ndryshimet.

## Ku të shkoni nga këtu?

Urime!  Ju sapo keni kompletuar rrjedhën standarde  _fork -> clone -> edit -> pull request_ që do ta hasni shpesh si kontribues!

Festoni kontributin tuaj dhe ndajeni me shokët dhe ndjekësit duke shkuar tek  [web aplikacioni](https://firstcontributions.github.io/#social-share).

Ju mund t'i bashkoheni ekipin tonë në slack nëse ju duhet ndihmë ose nëse keni ndonjë pyetje. [Bashkohu ekipit në slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

Tani të të ndihmojmë që të kontribuosh në projekte tjera. Ne kemi krijuar një listë projektesh me probleme të lehta tek të cilat mund të fillosh. Shiko [listën e projekteve në web apliacion](https://firstcontributions.github.io/#project-list).

### [Materiale shtesë](additional-material/git_workflow_scenarios/additional-material.md)


## Tutoriale duke përdorur vegla tjera

| <a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a>| <a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |<a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                 | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)      | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                           | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)     | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)         | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)         |

