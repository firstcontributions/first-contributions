[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Kontributet e Para

Është gjithmonë e vështirë hera e parë kur bën diçka. Sidomos kur bashkëpunon, të bësh gabime nuk është një ndjenjë e mirë. Ne duam ta thjeshtësojmë mënyrën se si kontribuesit e open-source mësojnë dhe kontribuojnë për herë të parë.

Leximi i artikujve & shikimi i tutorialve ndihmojnë, por ç'është më mirë se sa ta bësh këtë gjë në një vend praktike? Ky projekt synon të udhëzojë & të thjeshtësojë mënyrën se si fillestarët bëjnë kontributin e tyre të parë. Nëse dëshiron të bësh kontributin tënd të parë, ndiqi hapat më poshtë.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="forko këtë repozitor" />

#### Nëse nuk e ke git në kompjuterin tënd, [instaloje](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Forko këtë repozitor

Forko këtë repozitor duke klikuar në butonin fork në krye të kësaj faqeje.
Kjo do të krijojë një kopje të këtij repozitori në llogarinë tënde.

## Klono repozitorin

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="klono këtë repozitor" />

Tani klono repozitorin e forkuar në kompjuterin tënd. Shko në llogarinë tënde të GitHub, hap repozitorin e forkuar, kliko butonin code dhe më pas kliko ikonën _kopjo në clipboard_.

Hap një terminal dhe ekzekuto komandën vijuese të git:

```bash
git clone "url që sapo e kopjove"
```

Ku "url që sapo e kopjove" (pa thonjëzat) është url-ja e këtij repozitori (forku yt i këtij projekti). Shiko hapat e mëparshëm për të marrë url-në.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="kopjo URL në clipboard" />

Për shembull:

```bash
git clone git@github.com:ky-je-ti/first-contributions.git
```

Ku `ky-je-ti` është emri i përdoruesit tënd të GitHub. Këtu je duke kopjuar përmbajtjen e repozitorit first-contributions në GitHub në kompjuterin tënd.

## Krijo një degë

Ndrysho direktorinë e repozitorit në kompjuterin tënd (nëse nuk je tashmë atje):

```bash
cd first-contributions
```

Tani krijo një degë duke përdorur komandën `git switch`:

```bash
git switch -c emri-jot-i-deges-se-re
```

Për shembull:

```bash
git switch -c shto-john-doe
```

## Bëj ndryshimet e nevojshme dhe kryej ato ndryshime

Tani hap skedarin `Contributors.md` në një editor teksti, shto emrin tënd tek ai. Mos e shto në fillim ose në fund të skedarit. Vendose diku në mes. Tani, ruaje skedarin.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Nëse shkon në direktorinë e projektit dhe ekzekuton komandën `git status`, do të shohësh se ka ndryshime.

Shto ato ndryshime në degën që sapo e krijove duke përdorur komandën `git add`:

```bash
git add Contributors.md
```

Tani kryej ato ndryshime duke përdorur komandën `git commit`:

```bash
git commit -m "Add emri-yt to Contributors list"
```

Duke zëvendësuar `emri-yt` me emrin tënd.

## Shty ndryshimet në GitHub

Shty ndryshimet e tua duke përdorur komandën `git push`:

```bash
git push -u origin emri-jot-i-deges-se-re
```

Duke zëvendësuar `emri-jot-i-deges-se-re` me emrin e degës që krijove më parë.

<details>
<summary> <strong>Nëse merr ndonjë gabim gjatë shtyrjes, kliko këtu:</strong> </summary>

- ### Gabim i Autentikimit
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Shko te [tutoriali i GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) mbi gjenerimin dhe konfigurimin e një çelësi SSH në llogarinë tënde.

</details>

## Dërgo ndryshimet e tua për rishikim

Nëse shkon në repozitorin tënd në GitHub, do të shohësh një buton `Compare & pull request`. Kliko në atë buton.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="krijo një pull request" />

Tani dërgo pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="dërgo pull request" />

Së shpejti unë do t'i bashkoj të gjitha ndryshimet tuaja në degën kryesore të këtij projekti. Do të marrësh një email njoftimi pasi ndryshimet të jenë bashkuar.

## Ku të shkosh nga këtu?

Urime! Sapo përfundove rrjedhën standarde _fork -> clone -> edit -> pull request_ që do ta hasësh shpesh si kontribues!

Festo kontributin tënd dhe shpërndaje me miqtë e tu dhe ndjekësit duke shkuar te [web app](https://firstcontributions.github.io/#social-share).

Mund të bashkohesh në ekipin tonë slack në rast se ke nevojë për ndonjë ndihmë ose ke ndonjë pyetje. [Bashkohu në ekipin slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-29qhyr9lt-Bi7WLbgGIFqV7aCEG_grvg).

Tani le të fillojmë me kontributin në projekte të tjera. Ne kemi përmbledhur një listë projektesh me probleme të lehta që mund të fillosh. Shiko [listën e projekteve në web app](https://firstcontributions.github.io/#project-list).

### [Materiale shtesë](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriale duke përdorur vegla të tjera

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/512px-Visual_Studio_Code_1.35_icon.svg.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                           | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                                                                      | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                                                                               | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                                                                         | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                                                             | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                                               |
