[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Mga Unang Kontribusyon

Makakatulong ang proyektong ito na gawing mas simple at magsilbing gabay sa paggawa ng mga gustong magbigay ng kanilang unang kontribusyon. Kung gusto magkaroon ng unang kontribusyon, sundin ang mga hakbang sa ibaba.

_Kung hindi ka komportable sa paggamit ng command line, [narito ang mga tutorial gamit ang GUI tool.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="i-fork ang repository na ito" />

#### Kung wala kang Git sa iyong computer, [i-install ito](https://docs.github.com/en/get-started/quickstart/set-up-git).

## I-fork ang repository ito

I-fork ang repository na ito sa pamamagitan ng pag-click sa _fork button_ sa kanang itaas ng page na ito.
Gagawa ito ng kopya ng _repository_ sa iyong _account_.

## I-clone ang _repository_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="i-clone ang repository na ito" />

Ngayon, i-clone ang _forked repository_ sa iyong _computer_. Pumunta sa iyong _GitHub account_, buksan ang _forked repository_, i-click ang _code button_ at pagkatapos ay i-click ang _copy to clipboard_ icon.

Magbukas ng terminal at patakbuhin ang sumusunod na git command:

```bash
git clone "url na kakakopya mo lang"
```

ang "url na kakakopya mo lang" (tanggalin ang "") ay ang url ng iyong _forked repository_.Tingnan ang mga nakaraang hakbang para makuha ang url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="kopyahin ang URL sa clipboard" />

Halimbawa:

```bash
git clone https://github.com/username/first-contributions.git
```

ang `username` ay ang iyong GitHub username. Dito mo napunta ang mga laman ng kinopya mong _repository_ ng mga unang kontribusyon sa GitHub sa iyong _computer_.

## Gumawa ng _branch_

Pumunta sa _directory_ ng _repository_ sa iyong _computer_ (kung wala ka pa roon, i-type ito sa _terminal_):

```bash
cd first-contributions
```

Ngayon, gumawa ng isang _branch_ gamit ang _command_ na `git switch`:

```bash
git switch -c pangalan-ng-branch
```

Halimbawa:

```bash
git switch -c add-juan-delacruz
```

## Ilagay ang mga gusto mong baguhin sa _repository_

Ngayon, buksan ang `Contributors.md` _file_ sa isang _text editor_ at idagdag ang iyong pangalan (maaari mong gayahin na lang ang gawa ng iba). Iwasang ilagay ito sa pinaka-simula o dulo ng _file_. Ilagay ito kahit saan sa gitna ng _file_. I-save ang _file_ kapag nailagay na.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Kung pupunta ka sa _directory_ ng proyekto at i-type ang _command_ na `git status`, makikita mo yung mga nabago mo sa `Contributors.md`.

Idagdag ang mga _file_ na nabago mo sa _branch_ na ginawa mo kanina gamit ang _command_ na `git add`:

```bash
git add Contributors.md
```

I-commit ang mga _files_ na iyon gamit ang _command_ na `git commit`:

```bash
git commit -m "Add iyong-pangalan to Contributors list"
```

## I-push ang mga _files_ na _nabago_ sa GitHub

I-push ang mga nabago mong _files_ gamit ang command na `git push`:

```bash
git push -u origin pangalan-ng-branch
```

Ang `pangalan-ng-branch` ay pangalan ng branch na ginawa mo kanina.

<details>
<summary> <strong>Kung nagkaroon ng error habang nag-pupush, i-click ito: </strong> </summary>

- ### Error sa Pagpapatunay
    <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
    remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
    fatal: Authentication failed for 'https://github.com//first-contributions.git/'</pre>
  Pumunta sa [tutorial ng GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) sa paggawa at pag-configure ng SSH key sa iyong account.
</details>

## I-submit ang mga binago mo para mareview

Kung pupunta ka sa iyong _forked repository_ sa GitHub, makikita mo yung button na `Compare & pull request`. I-click mo iyon.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="gumawa ng pull request" />

Ngayon, baguhin ang ilang _checkboxes_ sa _description textarea_, at i-submit ang _pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="ipasa ang pull request" />

Ime-merge ko ang lahat ng mga nabago mo sa _main branch_ ng proyektong ito. Makakatanggap ka ng _email notification_ kapag na-merge ko na ito.

## Saan na pagkatapos?

Congrats! Nakumpleto mo lang ang karaniwang _fork -> clone -> edit -> pull request_ workflow na madalas mong gagamitin bilang isang _contributor_!

Ipakita ang iyong kontribusyon sa iyong mga kaibigan at tagasubaybay at magpunta sa [web app](https://firstcontributions.github.io/#social-share).

Ngayon, pwede ka nang gumawa ng kontribusyon sa iba pang mga proyekto! Gumawa kami ng isang listahan ng mga proyekto na may mga madadaling gawing _issues_ na pwede mong gawin. Tingnan ang [listahan ng mga proyekto sa web app](https://firstcontributions.github.io/#project-list).

### [Karagdagang materyal](additional-material/git_workflow_scenarios/additional-material.md)

## Mga Tutorial Gamit ang Iba Pang Mga Tool

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
