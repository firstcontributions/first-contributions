[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Анхны хувь нэмэр оруулах

Энэхүү төсөл нь анхлан суралцлагчдад  хувь нэмэр оруулах арга замыг хялбарчлах, чиглүүлэх зорилготой юм. Хэрэв та анхны хувь нэмрээ оруулах гэж байгаа бол доорх алхмуудыг дагана уу.

_Хэрэв та командын мөрөнд арай дасаагүй бол, [GUI хэрэгслийг ашиглах зааварчилгааг эндээс үзнэ үү..](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="энэ төслийг салаалж авах" />

#### git байхгүй бол, [эндээс суулгана уу](https://help.github.com/articles/set-up-git/).

## Энэ төслийг салаалж авна уу

Энэ хуудасны дээд талд байрлах fork товчлуур дээр дарж энэ төслийг салаалж авснаар таны төслүүд дээр нэмэгдэх болно.

## Төсөл хуулбарлаж авах

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Төсөл хуулбарлах" />

Одоо салаалж авасан төслийг өөрийн машиндаа хуулбарлаж хийнэ үү. GitHub бүртгэл рүүгээ орж, салаа хадгалах газрыг нээгээд, кодын товчлуур дээр дарж, дараа нь _хуулбарлах самбар руу хуулах_ дүрс дээр дарна уу.

Терминал нээж, дараах git командыг ажиллуулна уу:

```
git clone "дөнгөж сая хуулбарласан URL"
```

"дөнгөж сая хуулбарласан URL" (хашилтгүй) нь энэ агуулахын url (таны энэ төслийн салаа) юм. URL авахын тулд өмнөх алхмуудыг харна уу.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL хаягийг санах ой руу хуулах" />

Жишээ нь:

```
git clone https://github.com/энэ-бол-чи/first-contributions.git
```

"энэ бол чи" нь таны GitHub хэрэглэгчийн нэр юм. Энд та GitHub дээрх анхны хувь нэмэрийн төслийг компьютер дээрээ хуулж байна.

## Мөчир үүсгэх

Компьютер дээрх репозиторын лавлах руу шилжинэ үү (хэрэв та тэнд байхгүй бол):

```
cd ./first-contributions
```

Одоо `git switch` командыг ашиглан мөчир үүсгэнэ үү:

```
git switch -c шинэ-мөчрийн-нэр
```

Жишээ нь:

```
git switch -c шинэ-мөчрийн-нэр
```

## Шаардлагатай өөрчлөлтүүдийг хийж, эдгээр өөрчлөлтүүдийг хий

Одоо `Contributors.md` файлыг текст засварлагч дээр нээгээд түүнд нэрээ нэмнэ үү. Үүнийг файлын эхэнд эсвэл төгсгөлд бүү нэм. Үүнийг хооронд нь хаана ч тавь. Одоо файлаа хадгал.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Хэрэв та төслийн лавлах руу очоод `git status` командыг ажиллуулбал өөрчлөлтүүд байгааг харах болно.

`git add` командыг ашиглан шинээр үүсгэсэн салбар дээрээ эдгээр өөрчлөлтүүдийг нэмнэ үү:

```
git add Contributors.md
```

Одоо `git commit` командыг ашиглан эдгээр өөрчлөлтүүдийг хийнэ үү:

```
git commit -m "<таны нэр>-г хувь нэмэр оруулагчдын жагсаалтад нэмэх"
```

`<таны нэр>`-г өөрийн нэрээр солино.

## GitHub руу өөрчлөлт оруулах

`git push` командыг ашиглан өөрчлөлтөө дарна уу:

```
git push origin -u <мөчрийн-нэр>
```

`<мөчрийн-нэр>`-г өмнө нь үүсгэсэн салбарынхаа нэрээр солино.

<details>
<summary> <strong>Хэрэв та түлхэх явцад алдаа гарвал энд дарна уу:</strong> </summary>

* ### Authentication Error
     <pre>алсын зайнаас: 2021 оны 8-р сарын 13-нд нууц үг баталгаажуулалтын дэмжлэгийг устгасан. Оронд нь хувийн хандалтын токен ашиглана уу.
   алсын зайнаас: Дэлгэрэнгүй мэдээллийг https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/-с үзнэ үү.
   аюултай: 'https://github.com/<your-username>/first-contributions.git/-ийн баталгаажуулалт амжилтгүй боллоо</pre>
   [GitHub-н заавар](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) руу очно уу. өөрийн бүртгэлд SSH түлхүүр үүсгэж, тохируулах.

</details>

## Өөрчлөлтүүдээ хянуулахаар илгээнэ үү

Хэрэв та GitHub дээрх репозитор руугаа очвол `Харьцуулах & татах хүсэлт` товчийг харах болно. Тэр товчлуур дээр дарна уу.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Харьцуулах & татах хүсэлт" />

Одоо татах хүсэлтийг илгээнэ үү.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="татах хүсэлт гаргах" />

Удахгүй би таны бүх өөрчлөлтийг энэ төслийн мастер салбар болгон нэгтгэх болно. Өөрчлөлтүүдийг нэгтгэсний дараа танд мэдэгдлийн имэйл ирэх болно.

## Эндээс хаашаа явах вэ?

Баяр хүргэе! Та хувь нэмэр оруулагчийн хувьд байнга тулгардаг стандарт _салаа -> клон -> засварлах -> татах хүсэлт_ ажлын урсгалыг дөнгөж сая дуусгалаа!

Өөрийн оруулсан хувь нэмрийг тэмдэглэж, [вэб апп](https://firstcontributions.github.io/#social-share) руу орж найзууд болон дагалдагч нартайгаа хуваалцаарай.

Танд тусламж хэрэгтэй эсвэл асуух зүйл байвал манай сул багт нэгдэж болно. [Сул багт нэгдээрэй](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

Одоо бусад төслүүдэд хувь нэмрээ оруулах ажлыг эхлүүлье. Бид таны эхлүүлж болох хялбар асуудлууд бүхий төслүүдийн жагсаалтыг гаргалаа. [Вэб апп дахь төслүүдийн жагсаалтыг] (https://firstcontributions.github.io/#project-list) шалгана уу.

### [Нэмэлт материал](additional-material/git_workflow_scenarios/additional-material.md)

## Бусад хэрэгслийг ашиглах заавар

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

