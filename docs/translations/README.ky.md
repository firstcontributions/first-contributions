[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Алгачкы салымдар (first contributions)

Бул долбоор жаңы баштагандарга алгачкы салымын кошуу жолун жеңилдетип, багыт берүүнү максат кылат. Эгер сиз алгачкы салымыңызды кошууну кааласаңыз, төмөнкү кадамдарды аткарыңыз.
Эгер сиз командалык сап (command line) менен иштөөдө ыңгайсыз болсоңуз, бул жерде GUI куралдарын колдонгон окуу материалдары бар.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Эгер компьютериңизде git жок болсо, [аны орнотуңуз](https://docs.github.com/en/get-started/quickstart/set-up-git).


## Репозиторийди "fork" кылыңыз

Бул баракчанын жогору жагындагы fork баскычын басып, бул репозиторийди fork кылыңыз. Бул сиздин аккаунтуңузда бул репозиторийдин көчүрмөсүн түзөт.

## Репозиторийди клондоңуз (clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />
Эми fork кылынган репозиторийди компьютериңизге клондоңуз. GitHub аккаунтуңузга кирип, fork кылынган репозиторийди ачыңыз, андан кийин code баскычын, анан SSH кошумча барагын (tab) басып, url-ди алмашуу буферине көчүрүү (copy url to clipboard) сөлөкөтүн басыңыз.
Терминалды ачып, төмөнкү git командасын аткарыңыз:
```
git clone "сиз жаңы эле көчүргөн url"
```
мында "сиз жаңы эле көчүргөн url" (тырмакчасыз) бул репозиторийдин url-и болуп саналат (бул долбоордун сиздин fork'уңуз). Url-ди алуу үчүн мурунку кадамдарды караңыз.
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />
Мисалы:
```
git clone git@github.com:this-is-you/first-contributions.git
```
мында `this-is-you` сиздин GitHub колдонуучу атыңыз. Бул жерде сиз GitHub-дагы first-contributions репозиторийинин мазмунун компьютериңизге көчүрүп жатасыз.

## Тармак (branch) түзүңүз

Компьютериңиздеги репозиторий каталогуна өтүңүз (эгер ал жерде болбосоңуз):
```
cd first-contributions
```
Эми `git switch` командасын колдонуп, тармак (branch) түзүңүз:
```
git switch -c your-new-branch-name
```
Мисалы:
```
git switch -c add-tigilchi-balanchaev
```
<details> <summary> <strong>Эгер git switch командасын колдонууда кандайдыр бир каталар кетсе, бул жерди басыңыз:</strong> </summary>
Эгер "Git: switch is not a git command. See git –help" деген ката билдирүүсү чыкса, анда сиз git-тин эски версиясын колдонуп жаткан болушуңуз мүмкүн.
Бул учурда, анын ордуна git checkout колдонуп көрүңүз:
```
git checkout -b add-tigilchi-balanchaev
```
</details>

## Керектүү өзгөртүүлөрдү киригизип, аларды "commit" кылыңыз

Эми `Contributors.md` файлын текст редакторунан ачып, ага өз атыңызды кошуңуз. Аны файлдын башына же аягына кошпоңуз. Ортосуна бир жерге коюңуз. Эми, файлды сактаңыз.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />
Эгер сиз долбоор каталогуна барып, `git status` командасын аткарсаңыз, өзгөртүүлөр бар экенин көрөсүз.
Жаңы эле түзгөн тармакка (branch) ал өзгөртүүлөрдү `git add` командасын колдонуп кошуңуз:

```
git add Contributors.md
```

Эми ал өзгөртүүлөрдү `git commit` командасын колдонуп, commit кылыңыз:

```
git commit -m "Add your-name to Contributors list"
```

мында `your-name` дегенди өз атыңыз менен алмаштырыңыз.

## Өзгөртүүлөрдү github-га "push" кылыңыз

Өзгөртүүлөрүңүздү `git push` командасын колдонуп push кылыңыз:
```
git push -u origin your-branch-name
```
мында `your-branch-name` дегенди мурда түзгөн тармагыңыздын аты менен алмаштырыңыз.
<details> <summary> <strong>Эгер push кылууда кандайдыр бир каталар кетсе, бул жерди басыңыз:</strong> </summary>

- ### Аутентификация катасы (authentication error)

     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.   remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.   fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>   [GitHub'дын окуу материалына](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) өтүп, аккаунтуңузга SSH ачкычын түзүү жана конфигурациялоо боюнча окуңуз.
  Ошондой эле, алыскы дарегиңизди текшерүү үчүн 'git remote -v' командасын аткаргыңыз келиши мүмкүн.      Эгер ал ушундай көрүнсө:   <pre>origin https://github.com/your-username/your_repo.git (fetch)   origin https://github.com/your-username/your_repo.git (push)</pre>      Аны төмөнкү команда менен өзгөртүңүз:   ```bash   git remote set-url origin git@github.com:your-username/your_repo.git   ```   Антпесе, сизге дагы деле колдонуучу аты жана сырсөз суралып, аутентификация катасы келе берет.
</details>

## Өзгөртүүлөрүңүздү карап чыгуу үчүн жөнөтүңүз

Эгер GitHub'дагы репозиторийиңизге барсаңыз, `Compare & pull request` баскычын көрөсүз. Ошол баскычты басыңыз.
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />
Эми pull request жөнөтүңүз.
<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit the pull request" />
Жакында мен сиздин бардык өзгөртүүлөрүңүздү бул долбоордун негизги тармагына бириктирем (merge). Өзгөртүүлөр бириктирилгенде сизге электрондук почта аркылуу билдирүү келет.

## Эми каякка баруу керек?

Куттуктайбыз! Сиз салым кошуучу катары көп кездешүүчү стандарттуу _fork -> clone -> edit -> pull request_ иш процессин аяктадыңыз!
Салымыңызды белгилеп, [веб-тиркемеге](https://firstcontributions.github.io/#social-share) кирип, досторуңуз жана жолдоочуларыңыз менен бөлүшүңүз.
Эгер көбүрөөк тажрыйба алгыңыз келсе, [биздин Slack командасына кошулуңуз](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA) карап көрүңүз.
Эми башка долбоорлорго салым кошууну баштайлы. Биз сиз баштасаңыз боло турган жеңил маселелери бар долбоорлордун тизмесин түздүк. [веб-тиркемедеги долбоорлордун тизмесин](https://firstcontributions.github.io/#project-list) карап чыгыңыз.

---

## Башка куралдарды колдонгон окуу материалдары

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
