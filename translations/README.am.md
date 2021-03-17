# Առաջին ներդրումները

Այս նախագծի նպատակն է հեշտացնել և ուղեկցել նորեկենրին կատարելու նրանց առաջին ներդրումը։ Եթե դուք ցանկանում եք կատարել ձեր առաջին ներդրումը, հետևեք այս քայլերին։

_Եթե ձեզ հարմար չէ աշխատել Հրահանգների Վահանակի(CLI) հետ, [այս հղումով դուք կգտնեք ձեռնարկներ որոնք ձեզ կօգնեն աշխատել գրաֆիկական ինտերֆեյսով](https://github.com/MichaelGrigoryan25/first-contributions#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Եթե դուք չունեք Git ծրագրային ապահովվումը, ապա ներբեռնեք այն [այստեղից](https://docs.github.com/en/github/getting-started-with-github/set-up-git)

# Կրկնօրինակեք պահոցը

Կրկնօրինակեք այս պահոցը կտտացնելով Fork կոճակը, էջի վերևի աջ անկյունում։ Դա ձեզ համար կստեղծի այս պահոցի ձեր տարբերակը հենց ձեր հաշվի մեջ։

# Կլոնավորեք պահոցը

Հիմա, կլոնավորեք կրկնօրինակված պահոցը ձեր սարքի վրա․ Գնացեք ձեր GitHub - ի հաշիվ, բացեք կրկնօրինակած պահոցի էջը, սեղմեք code կոճակը, այնուհետև տհեղմեք _copy to clipboard_ կոճակը։

Բացեք հրահանգների վահանակը և աշխատացրեք հետևյալ հրահանգը։

```
git clone "պահոցի հղումը (այլ կերպ link)"
```

որտեղ "պահոցի հղումը (այլ կերպ link)" (առանց չակերտների) դա այն հղումն է որը դուք պատճենահանեցիք։ Նայեք նախորդ քայլերը, որպեսզի գտնեք այդ հղումը։

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Օրինակ։

```
git clone https://github.com/this-is-you/first-contributions.git
```

որտեղ `this-is-you` -ն ձեր GitHub հաշվի անունն է։ Այստեղ դուք կլոնավորում եք այն ամենը ինչ `first-contributions` պահոցը ներառում է իր մեջ դեպի ձեր համակարգիչը։

# Ստեղծեք ճյուղ

Փոխեք ձեր համակարգչի պահեստային գրացուցակին (եթե դուք արդեն այնտեղ չեք).

```
cd first-contributions
```

Այժմ ստեղծեք մասնաճյուղ օգտագործելով ՝git checkout՝ հրամանը.

```
git checkout -b your-new-branch-name
```

(Ճյուղի անունը պետք չէ դրա մեջ ունենալ _ավելացնել_ բառը, բայց խելամիտ բան է ներառել, քանի-որ այս ճյուղի նպատակն է ավելացնել ձեր անունը ցուցակում):

# Անհրաժեշտ փոփոխություններ կատարեք և կատարեք այդ փոփոխությունները

Այժմ տեքստի խմբագրում բացեք `Contributors.md` ֆայլը, դրան ավելացրեք ձեր անունը: Տեղադրեք այն ցանկացած վայրում: Այժմ պահեք ֆայլը:

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Եթե դուք գնում եք ծրագրի գրացուցակ և կատարում `git status` հրամանը, կտեսնեք, որ փոփոխություններ կան:

Այդ փոփոխությունները ավելացրեք ձեր ստեղծած ճյուղում օգտագործելով `git add` հրամանը.

```
git add Contributors.md
```

Այժմ կատարեք այդ փոփոխությունները օգտագործելով ՝git commit՝ հրամանը.

```
git commit -m "Ավելացնում եմ <քո-անունը> ներդրողների ցանկի մեջ"
```

փոխելով `<քո-անունը>` ձեր անվամբ.

## Հրում ենք փոփոխությունները դեպի GitHub

Հրել ձեր փոփոխությունները օգտագործելով ՝git push՝ հրամանը.

```
git push origin <ձեր-ճյուղի-անունը>
```

՝ձեր-ճյուղի-անունը՝ -ը փոխարինեք ավելի վաղ ստեղծված մասնաճյուղի անունով:

## Ներկայացրեք ձեր փոփոխությունները վերանայման համար

Եթե դուք գնում եք ձեր պահոց GitHub- ում, կտեսնեք `Compare & pull request՝ կոճակը: Կտտացրեք այդ կոճակին:

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Այժմ ներկայացրեք pull request -ը:

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Շուտով ձեր բոլոր փոփոխությունները միացնելու եմ այս նախագծի հիմնական մասնաճյուղին: Փոփոխությունները միաձուլվելուց հետո դուք կստանաք նամակ.

## Ու՞ր գնալ այստեղից

Շնորհավո՜ր։ Դուք հենց նոր ավարտեցիք ստանդարտ _fork -> clone -> edit -> pull request_ աշխատանքային հոսք- ը, որին դուք հաճախ հանդիպում եք որպես ներդրող:

Նշեք ձեր ներդրումը և կիսվեք այն ձեր ընկերների և հետևորդների հետ ՝ այցելելով [վեբ հավելվածը](https://firstcontributions.github.io/#social-share):

Կարող եք միանալ մեր Slack թիմին, եթե օգնության կարիք ունեք կամ որևէ հարց ունեք: [Միացեք Slack թիմին](https://join.slack.com/t/firstcontributors/shared_invite/zt-kpbyrmkk-JDkRtchcvRvQ0qK4iPmyvA)

Հիմա եկեք սկսենք այլ նախագծերին մասնակցելու հարցում: Մենք կազմել ենք այն նախագծերի ցուցակը, որտեղ կան հեշտ խնդիրներ, որոնց համար կարող եք սկսել: Ծանորացեկ [նախագծերի ցանկի հետ վեբ հավելվածում](https://firstcontributions.github.io/#project-list)

### [Լրացուցիչ նյութ](additional-material/git_workflow_scenarios/additional-material.md)

## Ձեռնարկներ, որոնք օգտագործում են այլ գործիքներ

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
