[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Mga Unang Kontribusyon

Nilalayon ng proyektong ito na gawing simple at gabayan ang paraan ng paggawa ng mga nagsisimula sa kanilang unang kontribusyon. Kung gusto mong gawin ang iyong unang kontribusyon, sundin ang mga hakbang sa ibaba.

_Kung hindi ka komportable sa command line, [narito ang mga tutorial gamit ang GUI tool.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Kung wala kang git sa iyong makina, [i-install ito](https://docs.github.com/en/get-started/quickstart/set-up-git).

## I-fork ang repositoryong ito

I-fork ang repository na ito sa pamamagitan ng pag-click sa fork button sa tuktok ng page na ito.
Gagawa ito ng kopya ng repositoryong ito sa iyong account.

## I-clone ang repositoryo

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Ngayon i-clone ang forked repository sa iyong makina. Pumunta sa iyong GitHub account, buksan ang forked repository, i-click ang code button at pagkatapos ay i-click ang _copy to clipboard_ icon.

Magbukas ng terminal at patakbuhin ang sumusunod na git command:

```
git clone "url na kinopya mo lang"
```

kung saan ang "url na kinopya mo lang" (nang walang mga panipi) ay ang url sa repositoryong ito (ang iyong tinidor ng proyektong ito). Tingnan ang mga nakaraang hakbang para makuha ang url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Halimbawa:

```
git clone https://github.com/this-is-you/first-contributions.git
```

kung saan ang `this-is-you` ay ang iyong GitHub username. Dito mo kinokopya ang mga nilalaman ng repositoryo ng mga unang kontribusyon sa GitHub sa iyong computer.

## Gumawa ng sangay

Baguhin sa direktoryo ng repositoryo sa iyong computer (kung wala ka pa roon):

```
cd first-contributions
```

Ngayon lumikha ng isang sangay gamit ang utos na `git switch`:

```
git switch -c your-new-branch-name
```

Halimbawa:

```
git switch -c add-alonzo-church
```

## Gumawa ng mga kinakailangang pagbabago at gawin ang mga pagbabagong iyon

Ngayon buksan ang `Contributors.md` file sa isang text editor, idagdag ang iyong pangalan dito. Huwag idagdag ito sa simula o dulo ng file. Ilagay ito kahit saan sa pagitan. Ngayon, i-save ang file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Kung pupunta ka sa direktoryo ng proyekto at isagawa ang command na `git status`, makikita mong may mga pagbabago.

Idagdag ang mga pagbabagong iyon sa sangay na nilikha mo lamang gamit ang utos na `git add`:

```
git add Contributors.md
```

Ngayon gawin ang mga pagbabagong iyon gamit ang utos na `git commit`:

```
git commit -m "Add your-name to Contributors list"
```

Ngayon gawin ang mga pagbabagong iyon gamit ang utos na `git commit`:

## I-push ang mga pagbabago sa GitHub

Itulak ang iyong mga pagbabago gamit ang command na `git push`:

```
git push -u origin your-branch-name
```

pinapalitan ang `your-branch-name` ng pangalan ng branch na ginawa mo kanina.

<details>
<summary> <strong>Kung nakakakuha ka ng anumang mga error habang nagtutulak, mag-click dito: </strong> </summary>

- ### Error sa Pagpapatunay
     <pre>remote: Inalis ang suporta para sa pagpapatotoo ng password noong Agosto 13, 2021. Mangyaring gumamit na lang ng personal na access token.
  remote: Pakitingnan ang https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ para sa karagdagang impormasyon.
  nakamamatay: Nabigo ang pagpapatotoo para sa 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Pumunta sa [tutorial ng GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) sa pagbuo at pag-configure ng SSH key sa iyong account.
</details>

## Isumite ang iyong mga pagbabago para sa pagsusuri

Kung pupunta ka sa iyong repository sa GitHub, makakakita ka ng button na `Ihambing at hilahin ang kahilingan. I-click ang button na iyon.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Ngayon isumite ang kahilingan sa paghila.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Sa lalong madaling panahon, pagsasamahin ko ang lahat ng iyong mga pagbabago sa pangunahing sangay ng proyektong ito. Makakatanggap ka ng email ng notification kapag napagsama na ang mga pagbabago.

## Saan pupunta mula dito?

Congrats! Nakumpleto mo lang ang karaniwang _fork -> clone -> edit -> pull request_ workflow na madalas mong makaharap bilang isang contributor!

Ipagdiwang ang iyong kontribusyon at ibahagi ito sa iyong mga kaibigan at tagasubaybay sa pamamagitan ng pagpunta sa [web app](https://firstcontributions.github.io/#social-share).

Maaari kang sumali sa aming slack team kung kailangan mo ng anumang tulong o may anumang mga katanungan. [Sumali sa slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Ngayon simulan na natin ang pag-aambag sa iba pang mga proyekto. Nag-compile kami ng isang listahan ng mga proyekto na may mga madaling isyu na maaari mong simulan. Tingnan ang [listahan ng mga proyekto sa web app](https://firstcontributions.github.io/#project-list).

### [Karagdagang materyal](additional-material/git_workflow_scenarios/additional-material.md)

## Mga Tutorial Gamit ang Iba Pang Mga Tool

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |