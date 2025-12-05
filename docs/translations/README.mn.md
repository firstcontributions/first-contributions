[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

Нээлттэй эх код баазад өөрийн хувь нэмрээ оруулах хүсэл програмч болгонд байдаг байх. Харин яг хаанаас эхлэхээ мэдэхгүй үе тохиолдох нь элбэг. Иймд, бид хэд шиг будилсан хөгжүүлэгч нарт ядаж хийх үйлдлийн зохих дарааллыг нь таниулчих зорилгоор энэхүү төсөл нь эхэлжээ. Та ч бас нээлттэй эх код баазад өөрийн нэмрээ оруулмаар байгаа бол доорх алхмуудыг дагаад хийгээрэй.


_Терминалтай ажиллах дургүй бол [GUI ашигласан хичээл рүү ороорой.](#tutorials-using-other-tools)_

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
<summary> <strong>git switch үйлдлийг хийхэд ямар нэгэн алдаа гарсан бол энд дар:</strong> </summary>

Дараах алдаа гарсан бол Гит програмын чинь хувилбар нийцэхгүй байна гэсэн үг: "Git: `switch` is not a git command. See `git –help`" 

Дээрх тохиолдолд `git checkout` үйлдлийг хэрэглээд үзээрэй:

```bash
git checkout -b шинэ-бранчийн-нэр
```

</details>

## Код баазад өөрчлөлт хийгээд өөрчлөлтөө коммит хийх

`Contributors.md` файлыг дурын текст эдитор дээр нээгээд өөрийн нэрээ нэмээрэй. Файлын эхэнд болон сүүлд нэмэхгүй л байхад болно.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Дараа нь, үндсэн фолдер луу шилжээд `git status` үйдлийг хийвэл танд таны өөрчилсөн файлууд харагдана.

Харагдаж буй өөрчлөлтүүдээ эхлээд бранчдаа `git add` үйлдлийг ашиглан нэмнэ:

```bash
git add Contributors.md
```

Дараа нь `git commit` үйлдлийг ашиглан коммит хийнэ (`your-name` гэснийг нэмсэн нэрээрээ солихоо мартуузай):

```bash
git commit -m "Add your-name to Contributors list"
```

## Гитхаб руу пушлэх

Дараа нь, `git push` үйлдлийг ашиглан саяны коммитоо пушлэнэ (`your-branch-name` гэснийг үүсгэсэн бранчийнхаа нэрээр солихоо мартуузай):

```bash
git push -u origin your-branch-name
```

<details>
<summary> <strong>Пушлэх үйлдэл дээр ямар нэгэн алдаа заавал энд дарж харах:</strong> </summary>

- ### Нэвтрэх эрхийн алдаа
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Хэрэв дээрх янзаар алдаа зааж байвал шинэ SSH түлхүүр үүсгэн хаягтайгаа холбох хэрэгтэй гэсэн үг бөгөөд хэрхэн холбохыг [энд дарж харна уу](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

  Мөн, аль рэпотой холбогдсон байгаагаа 'git remote -v' үйлдлээр шалгачихад гэмгүй.
  
  Хэрэв дээрх үйлдлийн хариу доорх маягаар байвал:
  <pre>origin	https://github.com/таны-хэрэглэгчийн-нэр/таны-рэпо-нэр.git (fetch)
  origin	https://github.com/таны-хэрэглэгчийн-нэр/таны-рэпо-нэр.git (push)</pre>
  
  дараах үйлдлээр өөрчлөх хэрэгтэй:
  ```bash
  git remote set-url origin git@github.com:таны-хэрэглэгчийн-нэр/таны-рэпо-нэр.git
  ```
  Ингэснээр та нууц үгээр биш хаягтай чинь холбогдсон SSH түлхүүрээр нэвтэрч эхэлнэ.
</details>

## Нэгтгэх хүсэлт илгээх

Гитхаб дээрх рэпо руу очмогц `Compare & pull request` товчлуур харагдах болно. Уг товчлуур дээр дарснаар шинэ нэгтгэх хүсэлт (pull request) үүсгэх хуудас гарч ирнэ.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Дараа нь нэгтгэх хүсэлтээ илгээнэ.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Таны хүсэлтийг бид хүлээн аваад автоматаар код бааздаа нэгтгэсэн байх болно. Энэ талаар бүртгэлтэй и-мейл хаяг дээр чинь мэдэгдэл ирнэ.

## Одоо яг яах билээ?

Нээлттэй эх код баазад өөрийн нэмрээ оруулахын тулд ерөнхийд нь мөрдөх ёстой  _fork -> clone -> edit -> pull request_ гэсэн дарааллыг та одоо мэддэг боллоо.

Нээлттэй эхэд нэмэр оруулж эхлэх анхны алхамаа хийсэн талаараа [энд дарж](https://firstcontributions.github.io/#social-share) нөхөдтэйгөө хуваалцана уу.

Өшөө дасгал ажиллахын тулд [энд дар](https://github.com/roshanjossey/code-contributions).

Нээлттэй эх код баазтай янз бүрийн төслүүдийн жагсаалтыг [энд дарж харна уу](https://firstcontributions.github.io/#project-list).

### [Нэмэлт материал](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Өөр програмууд ашигласан хичээлүүд

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Энэ төслийг дэмжсэн:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
