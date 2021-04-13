[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Kontributet e Para

Ky projekt synon t'i udhëzojë fillestarët në lidhje me kontributin e tyre të parë. Nëse jeni të interesuar, ndihni hapat më poshtë.

#### *Nëse ende nuk ndjehesh rehat me linjën e komandave, [më poshtë ke tutoriale në lidhje me veglat e GUI-t]( #tutoriale-duke-përdorur-vegla-të-tjera)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Nëse nuk ke Git të instaluar në pajisjen tënde, [hidhi një sy kësaj]( https://help.github.com/articles/set-up-git/).

## Bëje fork (degëzoje) këtë repozitor

Për të bërë fork këtë repozitor kliko butonin 'fork' në majë të kësaj faqeje. Kjo do të krijojë një kopje të ketij repozitori në llogarinë tënde.

## Klonoje këtë repozitor

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Tani klono në pajisjen tënde repozitorin që ke bërë degëzimin. Shko te llogaria e GitHub-it, hap 'forked repository', kliko butonin 'Code' dhe pastaj kliko ikonën *'copy to clipboard'*.

Hap terminalin dhe bëje run git komandën në vazhdim:

```
git clone <url që sapo ke kopjuar>
```
ku `<url që sapo ke kopjuar>` (pa kllapat këndore) është URL-ja e këtij repozitori (repozitori që bëre fork). Shiko hapat e mëparshëm për të marrë URL-në.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Për shembull:
```
git clone https://github.com/ky-je-ti/first-contributions.git
```
në të cilën `ky-je-ti` është emri yt në GitHub. Këtu ti e kopjon përmbajtjen e repozitorit 'first-contributions' në GitHub te kompjuteri yt.

## Krijo një degë (branch)

Ndrysho vendndodhjen e repozitorit në kompjuterin tënd (nëse nuk je në vendin e duhur):

```
cd first-contributions
```
Tani krijo një degë duke përdorur komandën `git checkout`:
```
git checkout -b <emri-i-degës-tënde>
```

Për shembull:
```
git checkout -b add-filan-fisteku
```
(Emri i degës nuk është i nevojshme të ketë fjalën 'add' në të, por është e arsyeshme të përfshihet pasi që qëllimi i kësaj dege është të shtojë emrin tënd në një listë.)

## Bëj ndryshimet e nevojshme dhe bëju commit

Tani hap file-in `Contributors.md` në një program për editim të tekstit dhe shto emrin tënd. Mos e shto në fillim ose në fund. Shtoje diku në mes. Tani, ruaj skedarin.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Nëse shkon te vendndodhja e projektit dhe ekzekuton komandën `git status`, do shohësh se ka ndryshime.


Shtoji këto ndryshime te dega që sapo krijove duke përdorur komandën `git add`:

```
git add Contributors.md
```

Tani bëji commit këto ndryshime duke përdorur komandën `git commit`:
```
git commit -m "Add <emri-yt> to Contributors list"
```
zëvendëso `<emri-yt>` me emrin tënd.

## Bëji push (shtyji) ndryshimet në GitHub

Bëji push ndryshimet duke përdorur komandën `git push`: 
```
git push origin <emri-i-degës-tënde>
```
zëvendëso `<emri-i-degës-tënde>` me emrin e degës që krijove më herët.

## Dorëzo ndryshimet për shqyrtim

Nëse shkon te repozitori yt në GitHub, do të shohësh një buton `Compare & pull request`. Klikoje.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Tani bëje 'submit' këtë 'pull request'.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Së shpejti do të bashkojë (merge) të gjitha ndryshimet e degës master të këtij projekti. Ti do të njoftohesh me email kur ndryshimet të zbatohen.

## Po tani?

Urime!  Ti sapo ke përfunduar procesin `fork -> clone -> edit -> PR` që do ta hasësh shpesh si kontributor!

Festo kontributin tënd dhe nda me shokët dhe ndjekësit duke shkuar te [linku](https://firstcontributions.github.io/#social-share).

Ti mund të bashkohesh në ekipin tonë në Slack nëse të duhet ndihmë ose nëse ke ndonjë pyetje. [Bashkoju ekipit në Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

Tani të të ndihmojmë që të kontribuosh në projekte tjera. Ne kemi krijuar një listë projektesh me probleme të lehta tek të cilat mund të fillosh. Shiko [listën e projekteve](https://firstcontributions.github.io/#project-list).


## Tutoriale duke përdorur vegla të tjera

| <a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gitkraken-tutorial.md"><img alt="GitKraken" src="./assets/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                 | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)      | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                           | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)     | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)         | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)         |

