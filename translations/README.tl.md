[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Mga unang ambag

Ang layon ng proyekto na ito ay gawing simple ang paraan ng paggawa ng unang ambag at patnubayan ang mga nagsisimula sa paggawa nito. Kung ninanais mong makagawa ng iyong unang ambag, sundin ang mga hakbang sa ibaba.

#### *Kung hindi ka komportable na gumamit ng *command line*, [narito ang mga tutorial na ginagamit ang mga *GUI* na kagamitan.](#Mga-tutorials-gamit-ang-ibang-tools)*


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Kung hindi naka-*install* ang *git* sa iyong kompyuter, [i-install mo ito](https://help.github.com/articles/set-up-git/).

## I-fork ang imbakan

I-fork ang imbakan sa pamamagitan ng pag-click ng *fork* *button* na matatagpuan sa bandang itaas na kanan ng *webpage* na ito.
Gagawa ito ng isang kopya ng imbakan na ito sa iyong *account*.

## I-clone ang imbakan

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Ngayon, i-clone ang nai-fork na imbakan sa iyong kompyuter. Pumunta lang sa iyong GitHub account, buksan ang nai-fork na imbakan, i-click ang clone button pagkatapos i-click ang *copy to clipboard* icon.

Buksan ang terminal at i-enter ang sumusunod na utos:

```
git clone "kawing na nakopya mo"
```
kung saan ang "kawing na nakopya mo" (wala ang mga panipi) ay ang kawing ng imbakan (ang iyong fork ng proyekto na ito). Tingnan ang mga nakaraang hakbang upang makuha ang kawing.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Halimbawa:
```
git clone https://github.com/iyong-username/first-contributions.git
```
kung saan ang `iyong-username` ang iyong username sa GitHub. Dito, kinokopya mo ang mga nilalaman ng imbakan na        `first-contributions` mula Github sa iyong kompyuter.

## Gumawa ng isang sangay

Pumunta sa directory ng iyong imbakan sa iyong kompyuter (kung hindi ka pa nakapunta):

```
cd first-contributions
```
Ngayon, gumawa ng isang sangay gamit ang `git switch` na utos:
```
git switch -c <dagdag-pangalan-ng-sangay>
```

Halimbawa:
```
git switch -c dagdag-juan-dela-cruz
```

## Gumawa ng kinakailangan na pagbabago at i-commit ang mga ito

Ngayon, buksan ang `Contributors.md` na dokumento sa isang *text editor*, at idagdag ang iyong pangalan. Huwag mong idagdag sa simula o sa hulihan ng dokumento. Ilagay sa kalagitnaan nito. Pagkatapos, i-save ang dokumento.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Kapag pumunta ka sa directory ng iyong proyekto at i-execute ang command na `git status`, may makikita mo na mayroong mga pagbabago.


Idagdag ang mga pagbabagong iyon sa iyong sangay na ginawa mo kanina gamit ang `git add` na utos:

```
git add Contributors.md
```

Ngayon, i-commit ang mga pagbabago na iyon gamit ang `git commit` na utos:
```
git commit -m "Add <iyong-pangalan> to Contributors list"
```
kung saan ang `<iyong-pangalan>` ay ang iyong pangalan.

## I-push ang mga changes sa GitHub

I-push ang mga pagbabago mo gamit ang utos na `git push`:
```
git push -u origin <dagdag-pangalan-ng-sangay>
```
kung saan ang `<dagdag-pangalan-ng-sangay>` ay ang pangalan ng sangay na naidagdag mo kanina.

## Ipasa ang mga pagbabago para sa pagsusuri

Kapag pumunta ka sa iyong imbakan sa GitHub, may makikita kang  `Compare & pull request` button. I-click mo ang *button* na iyon.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Ipasa ang pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Maya-maya, pagsasamahin ko ang iyong mga pagbabago sa pangunahing sangay ng proyekto na ito. Makakakuha ka ng isang abisong sulatroniko (*email*) nang pinagsama ang mga pagbabago.

## Saan na mula rito?

Congrats!  Nakumpleto mo ang standard _fork -> clone -> edit -> pull request_ na daloy ng trabaho na madalas mong makakasalamuha bilang isang umaambag!

Ipagdiwang mo ang iyong ambag at ibahagi ito sa mga kaibigan at tagasunod mo sa pamamagitan ng pagpunta sa [web app](https://firstcontributions.github.io/#social-share).

Puwede ka rin sumama sa aming Slack team kung kailangan mo ng karagdagang tulong o mayroon kang mga tanong. [Sumama sa Slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Ngayon, simulan na natin ikaw sa pag-ambag sa ibang proyekto. Nagtipon kami ng isang listahan ng mga proyekto na may mga madaling isyu na puwede mong masimulan. Tingnan lamang [ang listahan ng mga proyekto sa web app](https://firstcontributions.github.io/#project-list).

### [Mga karagdagang materyal](../additional-material/git_workflow_scenarios/additional-material.md)


## Mga tutorials gamit ang ibang mga kagamitan

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

