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

Форк хийчихсэн рэпогоо компьютер дээрээ суулгахын тулд хлээд Гитхаб хаяг дээрээ очоод, форклосон рэпогоо олоод, code гэсэн товчин даар дараад, SSH хэсэг дээр дарж, _хуулах_ товчлуур дээр дарах хэрэгтэй.

Дараа нь, терминалаа нээгээд доорх үйлдлийг хийнэ:

```bash
git clone "саяны хуулсан линк"
```

"саяны хуулсан линк" хэсгийн оронд эхний алхам дээр хуулсан линкээ наана.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Жишээ нь:

```bash
git clone git@github.com:таны-гитхаб-хаяг/first-contributions.git
```

`таны-гитхаб-хаяг` гэсний оронд Гитхабын хэрэглэгчийн нэрээ бичнэ. Ингэснээр та өөрийн хаяг дээрээ үүсгэсэн энэхүү рэпоны хуулбарыг өөрийн компьютер дээрээ хувилан авч чадлаа.

## Шинэ бранч үүсгэх

Дараа нь, хувилсан рэпоныхоо фолдер луу шилжинэ:

```bash
cd first-contributions
```

`git switch` үйлдлийг ашиглан шинэ бранч үүсгэнэ:

```bash
git switch -c шинэ-бранчийн-нэр
```

Жишээ нь:

```bash
git switch -c add-alonzo-church
```

<details>
<summary><strong>git switch үйлдлийг хийхэд ямар нэгэн алдаа гарсан бол энд дар:</strong></summary>

Дараах алдаа гарсан бол Git хувилбар хоцрогдсон байна:  
"Git: `switch` is not a git command."

Ийм үед:

```bash
git checkout -b шинэ-бранчийн-нэр
```

гэсэн команд ашиглана.
</details>

## Код баазад өөрчлөлт хийгээд өөрчлөлтөө коммит хийх

`Contributors.md` файлыг дурын текст эдитор дээр нээгээд өөрийн нэрээ нэмээрэй.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

`git status` хийвэл таны өөрчилсөн файлууд харагдана.

```bash
git add Contributors.md
```

```bash
git commit -m "Add your-name to Contributors list"
```

## Гитхаб руу пушлэх

```bash
git push -u origin your-branch-name
```

<details>
<summary><strong>Пуш хийх үед алдаа гарвал энд дар:</strong></summary>

SSH нэвтрэх алдаа гарвал:

```text
remote: Support for password authentication was removed...
fatal: Authentication failed
```

Шинэ SSH түлхүүр үүсгэж GitHub-тэй холбох шаардлагатай:

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
</details>

## Нэгтгэх хүсэлт илгээх

Гитхаб дээр `Compare & pull request` товч дээр дарна.

<img align="right" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Дараа нь:

<img align="right" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Pull request илгээнэ.

## Одоо яг яах вэ?

Та нээлттэй эхийн төслүүдэд хувь нэмэр оруулах үндсэн зарчмуудыг сурлаа:  
**fork → clone → edit → pull request**

Цааш үргэлжлүүлэхийг хүсвэл:

- https://firstcontributions.github.io/#project-list  
- https://github.com/roshanjossey/code-contributions

### [Нэмэлт материал](../additional-material/git_workflow_scenarios/additional-material.md)

## Өөр програмууд ашигласан хичээлүүд

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width="100"></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

<p>Энэ төслийг дэмжсэн:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
