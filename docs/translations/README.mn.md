

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Эхний Хандивууд

Анх удаа шинэ зүйл хийх хэцүү. Ялангуяа хамтран ажиллаж, алдаа гаргах нь тухтай биш байдаг. Бид эхлэгчид нээлттэй эхийн төсөлд анхны хувь нэмрээ оруулах үйл явцыг хялбар болгохыг хүссэн юм.

Түүх унших, заавар бичлэг үзэх нь тус болох ч бодитоор хийж үзэхээс илүү сайн зүйл гэж үгүй. Энэ төсөл нь анхны хувь нэмрээ оруулах эхлэгчдэд зориулсан гарын авлага, дадлага хийх орчин юм. Хэрэв та өөрийн **анхны хувь нэмрээ** оруулах гэж байгаа бол доорх алхмуудыг дагаарай.

#### *Хэрэв та командын мөр ашиглахад тухгүй байвал [энд байгаа график хэрэгслүүдийн зааврыг үзээрэй.](#Tutorials-Usin'-Other-Tools)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="энэ repository-г fork хийх" />

Хэрэв та компьютертээ Git суулгаагүй бол [эндээс суулгана уу](https://help.github.com/articles/set-up-git/).

## Энэ Repository-г Fork хийх

Энэ хуудсын дээд талд байгаа **Fork** товч дээр дарна. Ингэснээр таны GitHub аккаунт дээр тус repository-н хувилбар үүснэ.

## Repository-г Clone хийх

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="repository-г clone хийх" />

Одоо өөрийн GitHub аккаунт дээр очоод **Clone** товчийг дараад дараах *Copy to clipboard* дүрс дээр дарж URL-г хуулна.

Тэгээд терминал дээр дараах командыг ажиллуулна:

```
git clone "та хуулсан url"
```

Жишээ нь:

```
git clone https://github.com/taninii-neree-oruulna/first-contributions.git
```

Энд `taninii-neree-oruulna` нь таны GitHub хэрэглэгчийн нэр юм. Энэ команд таны компьютерт `first-contributions` repository-г хуулна.

## Салбар (Branch) Үүсгэх

Repository-ийн хавтас руу шилжинэ:

```
cd first-contributions
```

Дараа нь шинэ branch үүсгэнэ:

```
git checkout -b <shine-branch-neree-oruulna>
```

Жишээ нь:

```
git checkout -b add-luke-oliff
```

(*Branch-ийн нэрийг заавал “add” гэж эхлүүлэх шаардлагагүй, гэхдээ ихэвчлэн шинэ хувь нэмэр нэмэхдээ ийм нэр өгдөг.*)

## Өөрчлөлт Хийгээд Commit Хийх

Одоо `Contributors.md` файлыг нээгээд нэрээ нэмнэ. Эхлэл болон төгсгөлд биш, голд нь хаа нэгтээ байрлуулна. Файлаа хадгална.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

`git status` командыг ажиллуулбал таны хийсэн өөрчлөлтүүд харагдана.

Өөрчлөлтөө stage хийх:

```
git add Contributors.md
```

Commit хийх:

```
git commit -m "Add <tanii-neree-oruulna> to Contributors list"
```

## GitHub руу Push хийх

Өөрчлөлтөө GitHub руу илгээх:

```
git push origin <branch-neree-oruulna>
```

## Pull Request Илгээх

GitHub дээрх өөрийн repository-д очиход `Compare & pull request` товч харагдана. Түүнийг дар.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="pull request үүсгэх" />

Тэгээд pull request-ээ илгээнэ.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="pull request илгээх" />

Удалгүй таны өөрчлөлтийг энэ төслийн **master** салбарт нэгтгэх болно. Нэгтгэгдсэний дараа танд имэйл ирнэ.

## Дараа нь Яах вэ?

Баяр хүргэе! Та анхны **fork → clone → edit → pull request** үйл явцаа амжилттай хийлээ. 🎉

Өөрийн оруулсан хувь нэмрээ найз нөхөддөө хуваалцахыг хүсвэл [энэ вэб апп-аар](https://firstcontributions.github.io/#social-share) дамжуулан түгээгээрэй.

Одоо та илүү олон нээлттэй эхийн төсөлд хувь нэмрээ оруулж эхлэхэд бэлэн боллоо. Анхлан оролцоход тохиромжтой төслүүдийн жагсаалтыг [энэ вэб апп-аас](https://firstcontributions.github.io/#project-list) үзээрэй.

### [Нэмэлт материал](../additional-material/git_workflow_scenarios/additional-material.md)

## Бусад Хэрэгсэл Ашиглан Сурах Заавар

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

---


