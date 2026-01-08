[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Ilkinji goşantlar
Bu proýektiň maksady, GitHub-y täze öwrenýänlere ilkinji goşantlaryny (contribution) nädip goşup biljeklerini görkezmekdir.

Kyn bolup biler. Täze bir işi ilkinji sapar etmek hemişe kyn bolýar. Başga kişiler bilen bilelikde işlemeli bolsaň, ýalňyşlyk etmäne çekinýäň we gorkýaň. Ýöne açyk çeşmäniň (open source) düýbünde başga adamlar bilen bilelikde işleşmek ýatýar. Biz açyk çeşme (open source) proýektlerine ilkinji sapar goşant goşjaklara ýol görkezip, olaryň ilkinji goşantlaryny has aňsatlaşdyrmak isleýäris.

Blog postlary okamak ýa-da wideolary görüp öwrenmek kömek edip biler, ýöne bir zady edip öwrenmegiň ýerini tutup biljek zat ýok, şeýle dälmi? Eger ilkinji goşandyňyzy goşmak isleýän bolsaňyz, aşakdaky görkezmeleri yzarlaň.



<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Eger kompýuteriňizde git ýok bolsa, [şu ýerden ýükläň](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Şu repositoryny forklaň

Şu sahypanyň ýokarsynda duran fork düwmesine basyp şu repositoryny forklap bilýaňiz.
Şunlukda, şu repositorynyň kopiýasy siziň hasabyňyzda bolyar. (Şu proýektiň eýesiniň hasabynda-da, siziň hasabyňyzda-da bolýar)

## Şu repositoryny klonlaň(clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Indi, forklan repositoryny öz kompýuteriňize klonlaň(clone). Bu diýmek, ýaňy siziň github hasabyňyza kopiýasy gelen(forklan) şu proýekti oz kompyuteriňizde-de bir kopiýasyna eýe bolup bilýäňiz. Github hasabyňyza gidiň, forklan repositoryny açyň, code düwmesine basyň, soňra _copy to clipboard_ nyşanyna basyň. 

Terminaly açyp aşakdaky git buýruguny işlediň:

```bash
git clone "ýaňy kopiýa eden url-ňyz"
```

"ýaňy kopiýa eden url-ňyz"(goşa dyrnaksyz) şu repositorynyň url-y (şu proýektiň siziň eden forkuňyz).Url-ny almak üçin ýokarda görkezilenleri yzarlaň.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Mysal üçin:

```bash
git clone https://github.com/ulanyjy-ady/first-contributions.git
```

`ulanyjy-ady` diýip duran bölegiň deregine siziň Githubdaky ulanyjy adyňyz. Şu ýerde, Githubdaky first-contributions repositorynyň içindäki ähli zatlary kompýuteriňize kopiýalaýarsyňyz.

## Şaha(branch) döretmek

Repositorynyň duran papkasynda däl bolsaňyz, şol ýere gidiň:

```bash
cd first-contributions
```

Indi, `git switch` buýrugy arkaly täze şaha(branch) dörediň:

```bash
git switch -c siziň-täze-şahaňyzyň-ady
```

Mysal üçin:

```bash
git switch -c goş-ahmet-ahmedow
```

(Şahanyň adynda _goş_ sözüni hökman ýazmasaňyzam bolyar, ýöne bu şahanyň maksady adyňyzy goşant goşanlaryň hasabyna goşmak bolany üçin, _goş_ sözüni ulanmak düşnükli bolar)

## Gerekli üýtgeşmeleri edip, ol üýtgeşmeleri bellige almak (commit etmek).


Indi, tekst redaktorynda(m.ü VSCode) `Contributors.md` faýlyny açyň, içinde iň soňunda adyňyzy giriziň we ýatda saklaň(save)

```bash
- [Adyňyz](https://github.com/ulanyjy-adyňyz)
```

Mysal üçin:
```bash
- [Ahmet Ahmedow](https://github.com/ahmetahmedow)
```
```](``` arasynda boşluk ýokdur

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Terminalda eger proýektiň duran ýerine gidip,```git status``` buýrugyny işletseňiz, şol ýerde bolan üýtgeşmeleri görýaňiz.

```git add ``` buýrugyny ulanyp şol üýtgeşmeleri ýokarda döreden şahamyza(branch) goşýas:


```bash
git add Contributors.md
```

Indi, `git commit` buýrugy arkaly şol üýtgeşmeleri bellige alyp(commit) goýýas:

```bash
git commit -m "<Adyňyz> goşant goşanlaryň hataryna girizildi"
```
`<Adyňyz>` diýen ýere öz adyňyzy ýazyň

(BELLIK: açyk çeşme(open source) dünýäsinde dünýäniň her dürli ýerlerinden her dürli adamlar bilen bilelikde işleşýaniňiz üçin bellige alyş(commit) tekstini iňlis dilinde ýazyp bilýaňiz).

## Üýtgeşmeleri Githuba ibermek(Push)

`git push` buýrugy arkaly üýtgeşmeleriňizi iberiň(push):

```bash
git push -u origin siziň-şahaňyzyň-ady
```

`siziň-şahaňyzyň-ady` bölegini ýokarda doreden şahaňyzyň ady bilen çalşyň.

## Üýtgeşmeleriňizi gözden geçirmek üçin ýollaň
Eger Githubda şu repositoryňyza gitseňiz, `Compare & pull request` düwmesini görýäňiz. Şol düwmä basyň.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Indi, Çekiş haýyşnamasyny(pull request) ýollaň.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Basym, Eden ähli üýtgeşmeleriňizi gözden geçirip, proýektiň esasy şahasy(main branch) bilen birleşdirýäs. Üýtgeşmeler birleşdirilen soň, habarnama alarsyňyz.


## Mundan soň näme edip bilersiňiz?

Gutlaýas! Siz standart goşant goşujy hökmünde kän gabat gelinýän _forklamak(fork) -> Klonlamak(clone) -> Üýtgetmek(edit) -> Çekiş haýyşnamasy(pull request)_ yzygiderliligini tamamladyňyz!

Eden goşandyňyza begeniň we dostlaryňyz bilen paýlaşyň!

[Bu baglanma](https://firstcontributions.github.io/#social-share) arkaly hem birnäçe gyzykly proýektlere öz goşandyňyzy goşup bilýäňiz.




### [Goşmaça maglumat](additional-material/git_workflow_scenarios/additional-material.md)

## Başga gurallar hakynda sapaklar (ýöne iňlis dilinde)

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop gatnaşygynyň programmasy" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt=" Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/ gitkraken-tutorial.md"><img alt=" GitKraken programmasy" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code redaktory" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt=" Sourcetree programmasy" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA programmasy" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |


<p>Bu proýektiň goldaýjysy:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
