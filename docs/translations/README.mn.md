
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Эхний Хувь Нэмэр

Анх удаа ямар нэг зүйл хийхэд үргэлж хэцүү байдаг. Ялангуяа хамтран ажиллаж, алдаа гаргах үед тухгүй санагддаг. Бид шинэ нээлттэй эхийн хувь нэмэр оруулагчид хэрхэн суралцаж, анхны хувь нэмрээ хийх процессыг хялбар болгохыг хүссэн.

Өгүүллэг уншиж, бичлэг үзэх нь тус дөхөмтэй байж болох ч бодитоор нь хийж үзэхээс дээр зүйл үгүй. Энэхүү төсөл нь анхлан суралцагчдад анхны хувь нэмрээ оруулах замыг зааж өгөх, хялбарчлах зорилготой. Хэрэв та анхны хувь нэмрээ хийхийг хүсвэл доорх алхмуудыг дагаарай.  

#### *Хэрэв та командын мөр ашиглахад тухгүй байвал [энд бусад хэрэгсэл ашиглах зааврууд бий.](#Бусад-Хэрэгсэл-Ашигласан-Заавар)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="энэ репог салаалж авах" />

Хэрэв таны машин дээр git байхгүй бол [суулгана уу](https://help.github.com/articles/set-up-git/).

## Репог салаалж авах (Fork)

Энэ репогийн хуудасны дээд талд байрлах **Fork** товчийг дарна уу.  
Ингэснээр таны GitHub бүртгэл дээр тус репогийн хуулбар үүснэ.  

## Репог клон хийх (Clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="энэ репог клон хийх" />

Одоо энэ репог өөрийн компьютер дээрээ клон хийж авна. GitHub бүртгэл рүүгээ орж, **Clone** товчийг дараад дараа нь *copy to clipboard* тэмдгийг дарна.  

Терминал нээгээд дараах командыг ажиллуулна:  

```bash
git clone "та хуулсан url"
```

Энд `"та хуулсан url"` гэдэг нь энэ төслийн таны салаалсан хувилбарын URL юм.  

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL хуулах" />

Жишээ нь:  

```bash
git clone [https://github.com/taniin-ner/first-contributions.git](https://github.com/taniin-ner/first-contributions.git)
```

Энд `taniin-ner` гэдэг нь таны GitHub-н хэрэглэгчийн нэр.  

## Салбар (Branch) үүсгэх

Компьютер дээрээ тухайн репо руу орно:  

```bash
cd first-contributions
```

Шинэ салбар үүсгэнэ:  

```bash
git checkout -b <shine-salbar-ner>
```

Жишээ нь:  

```bash
git checkout -b add-luke-oliff
```

(*Салбарын нэр заавал `add` гэж эхлэх албагүй, гэхдээ өөрийн нэрээ нэмэх зорилготой тул ингэж нэрлэх нь ойлгомжтой.*)

## Өөрчлөлт хийх ба commit хийх

`Contributors.md` файлыг текст засварлагчаар нээгээд өөрийн нэрээ нэмнэ. Эхлэл эсвэл төгсгөлд бүү нэмээрэй, хаа нэгтээ дунд хэсэгт нь хийнэ. Дараа нь файлаа хадгална.  

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Дараа нь терминалдаа `git status` ажиллуулбал өөрчлөлт гарсныг харуулна.  

Өөрчлөлтөө салбартаа нэмнэ:  

```bash
git add Contributors.md
```

Commit хийж хадгална:  

```bash
git commit -m "Add <tanii-ner> to Contributors list"
```

## Өөрчлөлтөө GitHub руу push хийх

Дараах командаар өөрчлөлтөө push хийнэ:  

```bash
git push origin <salbar-ner>
```

`<salbar-ner>` хэсэгт та өмнө үүсгэсэн салбарын нэрээ оруулна.  

## Pull Request илгээх

GitHub дээр өөрийн репод ормогцоо **Compare & pull request** товчийг дарна.  

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="pull request үүсгэх" />

Дараа нь pull request-ээ илгээнэ.  

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="pull request илгээх" />

Тун удалгүй таны өөрчлөлтүүд гол (master) салбарт нэгтгэгдэх бөгөөд танд мэдэгдэл ирнэ.  

## Цааш хаашаа явах вэ?

Баяр хүргэе! Та _fork -> clone -> edit -> PR_ гэсэн стандарт ажлын урсгалыг амжилттай хийж дуусгалаа.  

Хувь нэмрээ хийсэндээ баярлаад найзууд, дагагчидтайгаа [энэ вэб апп](https://firstcontributions.github.io/#social-share)-аар дамжуулан хуваалцаарай.  

Мөн бид анхлан суралцагчдад зориулсан хялбар асуудлуудтай төслүүдийн жагсаалтыг цуглуулсан байгаа. [Энэ вэб апп доторх төслийн жагсаалтыг](https://firstcontributions.github.io/#project-list) шалгаарай.  

### [Нэмэлт материал](../additional-material/git_workflow_scenarios/additional-material.md)

## Бусад Хэрэгсэл Ашигласан Заавар

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |



