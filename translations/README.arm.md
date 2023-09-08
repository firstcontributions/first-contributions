[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Առաջին ներդրումը նախագծում:

Դա բարդ է. Դժվար է առաջին անգամ ինչ-որ բան անելիս, հատկապես երբ համագործակցում ես ուրիշների հետ, քանի որ սխալվելն ամենևին էլ հաճելի չէ։ Մեր նպատակն է պարզեցնել, թե ինչպես են նոր _open source_ ներդրողները սովորում և առաջին անգամ ներդրում կատարում:

Հոդվածներ կարդալը և ձեռնարկներ դիտելը կարող են օգնել, բայց ի՞նչն է ավելի լավ, քան գործնական միջավայրում բաներ անելը: Այս նախագիծը կենտրոնանում է ուղեցույց լինելու վրա և պարզեցնելու այն ձևը, որով սկսնակները կատարում են իրենց առաջին ներդրումը: Եթե ​​ցանկանում եք կատարել ձեր առաջին ներդրումը, հետևեք ստորև նշված քայլերին:

#### *Եթե դուք ծանոթ չեք հրամանի տողին, [այստեղ կան ձեռնարկներ՝ օգտագործելով GUI գործիքներ](#Ձեռնարկներ-այլ-գործիքների-հետ)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork այս պահոցից" />

Եթե ​​դուք չունեք git ձեր համակարգչում, կարող եք գտնել այն տեղադրելու հրահանգները [այս հղումով]( https://docs.github.com/es/get-started/quickstart/set-up-git ).

## Ստեղծեք  (*Fork*)  այս պահոցը

Պատառաքաղեք այս պահոցը՝ սեղմելով «*Fork*» կոճակը այս էջի վերևի աջ մասում:
Սա կստեղծի այս պահոցի պատճենը ձեր Github-ի հաշվում:

## Կլոնավորել (*Clone*) պատառաքաղված պահոցը

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="կլոնավորել այս պահոցը" />

Այժմ կլոնավորեք այս պահոցը ձեր համակարգչում: Գնացեք ձեր GitHub հաշիվ, սեղմեք «*clone or download*» կոճակը և այնուհետև սեղմեք *copy to clipboard* պատկերակը:

Բացեք ձեր վահանակը կամ տերմինալը և գործարկեք հետևյալ git հրամանը.

``` 
git clone "URL-ը, որը դուք հենց նոր պատճենեցիք"
```

Այնտեղ, որտեղ գրված է «url you just copy» (առանց կրկնակի չակերտների) այս պահոցի *url* է (ձեր * պատառաքաղը* այս նախագծին): Տեսեք նախորդ քայլերը՝ *url* ստանալու համար:

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="պատճենել url-ը clipboard-ում" />

Օրինակ:
```
git clone https://github.com/este-eres-tu/first-contributions.git
```
Մենք փոխարինում ենք «այս դու ես» մասը ձեր GitHub օգտատիրոջով: Այստեղ դուք պատճենում եք GitHub-ի *first-contributions* պահոցի բովանդակությունը ձեր համակարգչում:

## Ստեղծել մեկը ռամա (*Branch*)

Փոխեք ձեր համակարգչի պահեստի գրացուցակը (եթե արդեն այնտեղ չեք):

```
cd first-contributions
```

Այժմ ստեղծեք ռամա (*Branch*)՝ օգտագործելով հրամանը  `git checkout`:
```
git checkout -b <añade tu nombre>
```

Օրինակ:
```
git checkout -b add-vmartir-dev
```
(Ճյուղի անվանումը պարտադիր չէ, որ պարունակի *add* բառը, բայց խելամիտ է, որ դա պարունակի, քանի որ այս մասնաճյուղի նպատակը ձեր անունը ցուցակին ավելացնելն է:)

## Կատարեք անհրաժեշտ փոփոխությունները և հաստատեք(*Commit*)  այդ փոփոխությունները

Բացեք ֆայլը `Contributors.md`տեքստային խմբագրիչում և ավելացրեք ձեր անունը: Մի ավելացրեք այն ֆայլի սկզբում կամ վերջում, դա արեք այլ տեղ: Պահպանեք ֆայլը:

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Եթե ​​դուք գնում եք ծրագրի գրացուցակ և գործարկեք հրամանը  `git status`, դուք կտեսնեք, որ փոփոխություններ կան։

Ավելացնել այդ փոփոխությունները ռամա (*branch*) որը դուք ստեղծել եք ավելի վաղ՝ օգտագործելով հրամանը `git add`:

```
git add Contributors.md
```

Հիմա դա արեք *commit* այս փոփոխությունների մասին՝ գործարկելով հրամանը `git commit`:
```
git commit -m "Add <քո անունը> to Contributors list"
```
Փոփոխվող `<քո անունը>` քո անունով.

## Ուղարկել (*Push*) ձեր փոփոխությունները դեպի GitHub

Արեք *push* ձեր փոփոխությունները, օգտագործելով հրամանը `git push`:
```
git push origin <ավելացնել-ճյուղ-անուն>
```
Փոխարինում է `<ավելացնել-ճյուղ-անուն>` նախկինում ստեղծած մասնաճյուղի անունով.

## Ուղարկել (*Submit*) ձեր փոփոխությունները պետք է վերանայվեն

Եթե ​​ գնաք ձեր պահոցը GitHub-ում, կտեսնեք կոճակ `Compare & pull request`. Սեղմեք այս կոճակը:

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="ստեղծել pull request" />

Այժմ ուղարկեք *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="ուղարկել pull request" />

Ես շուտով կմիավորեմ ձեր փոփոխությունները (միաձուլում կատարելով որ   կոչվում է *merge*) այս նախագծի գլխավոր *main* ռամա հետ: Փոփոխությունների միաձուլման ժամանակ դուք էլփոստով ծանուցում կստանաք:

## Որո՞նք են հաջորդ քայլերը:

Շնորհավորում եմ!! Դուք ավարտել եք հոսքըtrabajo *_fork -> clone -> edit -> PR_* որը սովորաբար կգտնեք որպես ներդրող:

Նշեք ձեր ներդրումը և կիսվեք այն ձեր ընկերների և հետևորդների հետ՝ գնալով [web app](https://firstcontributions.github.io/#social-share).

Դուք կարող եք նաև միանալ մեր Slack *թիմին, եթե օգնության կարիք ունեք կամ որևէ հարց ունեք:
 [Միացե՛ք մեր Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Այժմ սկսեք նպաստել այլ նախագծերի: Մենք կազմել ենք նախագծերի ցանկը *issues* sհեշտ է սկսել: Նայեք [նախագծերի ցանկը վեբ հավելվածում](https://firstcontributions.github.io/#project-list).

### [Լրացուցիչ նյութ](../additional-material/git_workflow_scenarios/additional-material.md)


## Ձեռնարկներ այլ գործիքներով

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
