[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Առաջին ներդրումները

Սկսնակների համար պարզ ու վստահ ուղեցույց՝ ձեր առաջին ներդրումն (առաջին Pull Request-ը) open source նախագծում կատարելու համար։

Եթե հրամանի տողը (Terminal) ձեզ հարմար չէ, անցեք [GUI գործիքներով ձեռնարկներին](#gui-tutorials)։

<a id="contents"></a>

## Բովանդակություն

- [Արագ մեկնարկ](#quickstart)
- [Նախապայմաններ](#prerequisites)
- [Քայլ 1․ Fork (պատառաքաղել)](#step-1-fork)
- [Քայլ 2․ Clone (կլոնավորել)](#step-2-clone)
- [Քայլ 3․ Branch (մասնաճյուղ ստեղծել)](#step-3-branch)
- [Քայլ 4․ Փոփոխել և commit անել](#step-4-change-and-commit)
- [Քայլ 5․ Push (մղել) դեպի GitHub](#step-5-push)
- [Քայլ 6․ Pull Request ներկայացնել](#step-6-pr)
- [Հաճախ հանդիպող խնդիրներ](#troubleshooting)
- [Ձեռնարկներ՝ GUI գործիքներով](#gui-tutorials)
- [Որտեղ գնալ այստեղից](#next)

<a id="quickstart"></a>

## Արագ մեկնարկ

1. Fork արեք պահոցը GitHub-ում
2. Clone արեք ձեր fork-ը համակարգչում
3. Ստեղծեք նոր branch
4. Թարմացրեք `Contributors.md`-ը և commit արեք
5. Push արեք branch-ը GitHub
6. Բացեք Pull Request

<a id="prerequisites"></a>

## Նախապայմաններ

- GitHub հաշիվ
- Git (եթե դեռ չունեք՝ [տեղադրեք Git-ը](https://docs.github.com/en/get-started/quickstart/set-up-git))
- Տերմինալ (Windows՝ PowerShell / Terminal, macOS / Linux՝ Terminal)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Fork արեք այս պահոցը" />

<a id="step-1-fork"></a>

## Քայլ 1․ Fork (պատառաքաղեք) այս պահոցը

Սեղմեք էջի վերևում գտնվող **Fork** կոճակը․ արդյունքում այս պահոցի պատճենը կստեղծվի ձեր GitHub հաշվում։

<a id="step-2-clone"></a>

## Քայլ 2․ Clone (կլոնավորեք) ձեր fork-ը

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Կլոնավորեք ձեր պահոցը" />

Գնացեք ձեր GitHub հաշիվ, բացեք ձեր fork արած պահոցը, սեղմեք **Code** կոճակը և պատճենեք հղումը (_Copy to clipboard_)։

Բացեք տերմինալ և գործարկեք՝

```bash
git clone "այստեղ-տեղադրեք-ձեր-պատճենած-url-ը"
```

որտեղ `"այստեղ-տեղադրեք-ձեր-պատճենած-url-ը"` ձեր fork-ի URL-ն է։

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="Պատճենեք URL-ը clipboard-ում" />

Օրինակ:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

որտեղ `this-is-you` ձեր GitHub օգտանունն է։

<a id="step-3-branch"></a>

## Քայլ 3․ Ստեղծեք նոր branch (մասնաճյուղ)

Մուտք գործեք հենց նոր կլոնավորած նախագծի պանակը՝

```bash
cd first-contributions
```

Ստեղծեք նոր branch՝

```bash
git switch -c your-new-branch-name
```

Օրինակ՝

```bash
git switch -c add-your-name
```

<a id="step-4-change-and-commit"></a>

## Քայլ 4․ Կատարեք փոփոխությունը և commit արեք

Բացեք նախագծի արմատում գտնվող [`Contributors.md`](../../Contributors.md) ֆայլը, ավելացրեք ձեր անունը ցուցակում և պահեք փոփոխությունը։

Մի ավելացրեք անունը ֆայլի սկզբում կամ վերջում․ տեղադրեք այն ցանկում ցանկացած տեղ՝ շարադրանքի տրամաբանությունը չխախտելով։

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git-ի վիճակը" />

Ստուգեք, որ փոփոխությունները տեսանելի են՝

```bash
git status
```

Ավելացրեք ֆայլը staging area՝

```bash
git add Contributors.md
```

Commit արեք փոփոխությունը՝

```bash
git commit -m "Add your-name to Contributors list"
```

`your-name`-ը փոխարինեք ձեր անունով։

<a id="step-5-push"></a>

## Քայլ 5․ Push արեք փոփոխությունները GitHub

Ձեր branch-ը մղեք GitHub՝

```bash
git push -u origin your-branch-name
```

`your-branch-name`-ը փոխարինեք ձեր ստեղծած branch-ի անունով։

<a id="troubleshooting"></a>

<details>
<summary><strong>Եթե push անելիս սխալ եք ստանում, բացեք այստեղ</strong></summary>

### Վավերացման (Authentication) խնդիր

Եթե տեսնում եք նման սխալ՝

<pre>
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'
</pre>

Դուք պետք է օգտագործեք՝

- **SSH key** (խորհուրդ է տրվում) կամ
- **Personal Access Token (PAT)**՝ եթե HTTPS եք օգտագործում։

Տե՛ս GitHub-ի ուղեցույցը՝ SSH բանալի ստեղծելու և ավելացնելու համար․  
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
</details>

<a id="step-6-pr"></a>

## Քայլ 6․ Ներկայացրեք Pull Request (PR)

Գնացեք ձեր fork-ի էջը GitHub-ում․ սովորաբար կտեսնեք `Compare & pull request` կոճակը։ Սեղմեք այն։

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Ստեղծեք Pull Request" />

Այժմ լրացրեք վերնագիրը/նկարագրությունը և ուղարկեք Pull Request-ը։

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Ուղարկեք Pull Request" />

Փոփոխությունները հաստատվելուց և միաձուլվելուց հետո դուք կստանաք ծանուցում GitHub-ից։

<a id="next"></a>

## Որտեղ գնալ այստեղից

Շնորհավորում եմ․ դուք ավարտեցիք ստանդարտ `fork → clone → edit → pull request` հոսքը, որը ամենահաճախն է հանդիպում open source ներդրումների ժամանակ։

- Կիսվեք ձեր առաջին ներդրմամբ՝ [վեբ հավելվածում](https://firstcontributions.github.io/#social-share)
- Եթե ցանկանում եք ավելի շատ փորձ հավաքել, դիտեք [code-contributions](https://github.com/roshanjossey/code-contributions)
- Փնտրեք սկսնակների համար հարմար նախագծեր՝ [project list](https://firstcontributions.github.io/#project-list)

### [Լրացուցիչ նյութ](../additional-material/git_workflow_scenarios/additional-material.md)

<a id="gui-tutorials"></a>

## Ձեռնարկներ՝ GUI գործիքներով

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Այս նախագծին աջակցում են:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
