[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Առաջին ներդրումները(contributions)

Այս նախագիծը նպատակ ունի պարզեցնել և առաջնորդել սկսնակներին իրենց առաջին ներդրման ճանապարհին: Եթե ցանկանում եք կատարել ձեր առաջին ներդրումը, հետևեք ստորև նշված քայլերին:

_Եթե հրամանի պատուհանը (command line) ձեզ հարմար չէ, [ահա ուղեցույցներ գրաֆիկական ինտերֆեյսի (GUI) կիրառմամբ.](#Ուղեցույցներ-այլ-գործիքների-կիրառմամբ)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Եթե դուք չունեք git ձեր մեքենայի վրա, [տեղադրեք այն](https://help.github.com/articles/set-up-git/)

## Ճյուղավորեք (fork) այս պահոցը (repository)

Ստեղծեք ձեր սեփական պատճենը՝ սեղմելով այս էջի վերևում գտնվող `fork` կոճակը:
Դա կստեղծի այս պահոցի պատճենը ձեր պրոֆիլում:

## Կլոնավորեք պահոցը

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Հիմա կլոնավորեք պահոցը ձեր համակարգչում: Հղումը պատճենելու համար սեղմեք `clone` կոճակը, այնուհետև `copy to clipboard` կոճակը:

Բացեք տերմինալը և գործարկեք հետևյալ git հրամանը.

```
git clone "url you just copied"
```

Որտեղ "url you just copied"-ը (առանց չակերտների) ձեր պահոցի հղումն է (այս նախագծի ձեր ճյուղավորումը). Հետևեք քայլերին, որպեսզի ստանաք հղումը.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Օրինակ՝

```
git clone https://github.com/this-is-you/first-contributions.git
```

Որտեղ `this-is-you`-ն github-ի ձեր մուտքանունն է. Այսպիսով դուք պատճենում եք first-contributions պահոցը՝ GitHub-ից, ձեր համակարգչի վրա:

## Ստեղծեք ճյուղ

Մուտք գործեք ձեր համակարգչում գտնվող պահոցը, եթե արդեն այնտեղ չեք։

```
cd first-contributions
```

Հիմա ստեղծեք նոր ճյուղ՝ օգտագործելով `git checkout` հրամանը․

```
git checkout -b <add-your-name>
```

Օրինակ՝

```
git checkout -b add-alonzo-church
```

## Կատարեք անհրաժեշտ փոփոխությունները և կատարեք ձեր ներդրումը (commit)

Հիմա բացեք `Contributors.md` ֆայլը ձեր տեքստային խմբագրիչում, գրեք ձեր անունը և պահպանեք ֆայլը։ Մի ավելացրեք այն ֆայլի սկզբում կամ վերջում: Տեղադրեք այն որևէ տեղ մեջտեղում: Այժմ պահպանեք ֆայլը:

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Եթե գնաք նախագծի պանակ և կատարեք `git status` հրամանը, կտեսնեք, որ փոփոխություններ կան:

Ավելացրեք այդ փոփոխությունները այն ճյուղին, որը հենց նոր ստեղծեցիք՝ օգտագործելով `git add` հրամանը.

```
git add Contributors.md
```

Այժմ գործադրեք այս փոփոխությունները `git commit` հրամանով.

```
git commit -m "Add <your-name> to Contributors list"
```

Փոփոքեք `<your-name>`-ը ձեր անունով

## Push արեք փոփոխությունները github

Push արեք ձեր փոփոխությունները `git push` հրամանով․

```
git push origin <add-your-name>
```

Փոփոխոք `<add-your-name>`-ը ավելի վաղ ստեղծած ճյուղի անունով:

<details>
<summary> <strong>Եթե push անելիս առաջանում են սխալներ, սեղմեք այստեղ՝</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

</details>

## Հաստատեք փոփոխությունները վերանայման համար

Եթե այցելեք ձեր GitHub պահոցը, կտեսնեք `Compare & pull request` կոճակը։ Սեղմեք այդ կոճակը։

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Ապա հաստատեք pull հարցումը:

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Շուտով ես կմիավորեմ ձեր բոլոր փոփոխությունները այս նախագծի գլխավոր մասնաճյուղի մեջ: Փոփոխությունները միաձուլվելուց հետո դուք կստանաք ծանուցող նամակ:

## Ու՞ր գնալ այստեղից

Շնորհավորանքնե՛րս, դուք հենց նոր ավարտեցիք ստանդարտ _fork -> clone -> edit -> pull request_ աշխատակարգը, որը հաճախ կհանդիպեք որպես ներդրող:

Նշեք ձեր ներդրումը և կիսվեք այն ձեր ընկերների և հետևորդների հետ՝ այցելելով [web app](https://firstcontributions.github.io/#social-share).

Դուք կարող եք միանալ մեր Slack թիմին, եթե որևէ հարց կամ օգնության կարիք ունեք։ [Միանալ slack թիմին](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Հիմա կարող եք ձեր ներդրումն ունենալ այլ նախագծերում։ Մենք կազմել ենք հեշտ խնդիրներ ունեցող նախագծերի ցանկ, որոնցից կարող եք սկսել: Համեցեք [վեբ հավելվածի նախագծերի ցանկը](https://firstcontributions.github.io/#project-list).

### [Լրացուցիչ նյութեր](additional-material/git_workflow_scenarios/additional-material.md)

## Ուղեցույցներ այլ գործիքների կիրառմամբ

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
