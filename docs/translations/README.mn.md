[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

Нээлттэй эх код баазад өөрийн хувь нэмрээ оруулах хүсэл програмч болгонд байдаг байх. Харин яг хаанаас эхлэхээ мэдэхгүй үе тохиолдох нь элбэг. Иймд, бид хэд шиг будилсан хөгжүүлэгч нарт ядаж хийх үйлдлийн зохих дарааллыг нь таниулчих зорилгоор энэхүү төсөл нь эхэлжээ. Та ч бас нээлттэй эх код баазад өөрийн нэмрээ оруулмаар байгаа бол доорх алхмуудыг дагаад хийгээрэй.

_Терминалтай ажиллах дургүй бол [GUI ашигласан хичээл рүү ороорой.](#өөр-програмууд-ашигласан-хичээлүүд)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Компьютер дээрээ git суулгаагүй бол [энд дарж суулгана уу.](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Энэ рэпог форклох

Та энэ хуудасны дээд хэсэгт орших fork товчийг дарснаар энэ рэпоны хуулбар таны хаягт үүсэх юм.

## Энэ рэпог хувилах

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Форк хийчихсэн рэпогоо компьютер дээрээ суулгахын тулд эхлээд Гитхаб хаяг дээрээ очоод, форклосон рэпогоо олоод, code гэсэн товч дээр дараад, SSH хэсэгт дарж _copy_ товчийг дарна.

Терминалдаа:

```bash
git clone "саяны хуулсан линк"
```

Жишээ:

```bash
git clone git@github.com:таны-гитхаб-хаяг/first-contributions.git
```

## Шинэ бранч үүсгэх

```bash
cd first-contributions
```

```bash
git switch -c шинэ-бранчийн-нэр
```

Жишээ:

```bash
git switch -c add-alonzo-church
```

<details>
<summary><strong>git switch ажиллахгүй бол:</strong></summary>

```bash
git checkout -b шинэ-бранчийн-нэр
```

</details>

## Код баазад өөрчлөлт хийгээд коммит хийх

`Contributors.md` файлд нэрээ нэмнэ.

```bash
git add Contributors.md
git commit -m "Add your-name to Contributors list"
```

## Гитхаб руу пуш хийх

```bash
git push -u origin your-branch-name
```

<details>
<summary><strong>Пуш хийхэд алдаа гарвал:</strong></summary>

SSH authentication алдаа гарвал шинэ SSH key үүсгэнэ:  
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

</details>

## Pull Request илгээх

Гитхаб дээр:

**Compare & Pull Request → Create Pull Request**

## Одоо яах вэ?

Та одоо нээлттэй эх кодод хувь нэмэр оруулах үндсэн шат дамжлагыг мэддэг боллоо:

**fork → clone → edit → pull request**

### [Нэмэлт материал](../additional-material/git_workflow_scenarios/additional-material.md)

## Өөр програмууд ашигласан хичээлүүд

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width="100"></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width="100"></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

<p>Энэ төслийг дэмжсэн:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
