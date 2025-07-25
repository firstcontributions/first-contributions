[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Mga unang kontribusyon

Mahirap. Palaging mahirap sa unang pagkakataon ng anumang gawain. Lalo na sa isang kolaborasyon, kung saan hindi komportableng paglaanan ng tuon ang mga pagkakamali. Gusto naming simplehan at linawin ang modernong pamamaraan kung papaanong matuto at tumulong ang mga bagong *open-source contributors*.

Maaaring makatulong ang pagbabasa ng mga artikulo at panonood ng mga *tutorials*, pero ano pa bang mas epektibong pamamaraan kaysa sa aktual na aplikasyon ng isang pagsasanay? Ang pangunahing pakay ng proyektong ito ay gabayan ang mga baguhan na gawin ang kanilang unang *contribution*. Kung ikaw ay isa sa mga taong iyon, sundin lang ang mga sumusunod na tagubilin.

Kung hindi comfortable sa paggamit ng *command line*, [may mga tutorials din gamit ang mga *GUI* tools.](#Mga-tutorials-gamit-ang-ibang-tools)*



<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Kung wala pang *git* sa iyong computer, [i-install ito](https://help.github.com/articles/set-up-git/).


## I-fork ang repository

I-fork ang *repository* sa pamamagitan ng pag-click sa *fork* *button* na matatagpuan sa bandang itaas na kanan ng *webpage* na ito.
Magkakaroon na ng kopya ng *repository* na ito sa iyong account.

## I-clone ang repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Ngayon, i-clone ang repository na iyong na-fork sa iyong computer.
Pumunta lang sa iyong GitHub account, buksan ang nai-fork na repository, i-click ang clone button pagkatapos i-click ang *copy to clipboard* icon.

Buksan ang terminal at i-enter ang sumusunod na git command:

```bash
git clone "url na nakopya mo"
```
kung saan ang "url na nakopya mo" (wala ang mga panipi) ay ang URL ng repository (ang fork ng iyong proyekto). Pakitingnan nang mabuti ang mga nakaraang hakbang upang makuha ang url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Halimbawa:
```bash
git clone https://github.com/iyong-username/first-contributions.git
```
kung saan ang `iyong-username` ang iyong username sa GitHub. Mula sa command na ito, dito nagsisimula ng paggawa ng kopya ng nilalaman ng first-contributions repository mula sa GitHub papunta sa iyong kompyuter.

## Gumawa ng isang branch

Pumunta sa kompyuter directory ng iyong repository (kung hindi ka pa nakapunta):

```bash
cd first-contributions
```
Ngayon, gumawa na ng isang branch gamit ang `git checkout` command:
```bash
git checkout -b <dagdag-branch-name>
```

Halimbawa:
```bash
git checkout -b dagdag-juan-dela-cruz
```
(Hindi kailangan ng salitang *"dagdag"* sa pangalan ng i-dadagdag na branch pero makatwiran pa rin na gawin dahil layunin ng branch ang pagdagdag ng iyong pangalan sa isang listahan.)

## Gumawa ng kinakailangan na pagbabago at i-commit ang mga nagawang pagbabago

Ngayon, buksan ang `Contributors.md` file sa isang text editor, idagdag ang iyong pangalan. Huwag mong idagdag sa simula o sa hulian ng tinutukoy na file. Ilagay sa kalagitnaan ng file. At i-save and file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


Kapag pumunta ka sa directory ng iyong proyekto at i-enter ang command na `git status`, may makikita kang mga pagbabago.


Idagdag ang mga pagbabagong naganap papunta sa iyong branch gamit ang `git add` command:

```bash
git add Contributors.md
```

Ngayon, i-commit ang mga nabagong files gamit ang `git commit` command:
```bash
git commit -m "Add <your-name> to Contributors list"
```
kung saan ang `<your-name>` ay ang iyong pangalan.

## I-push ang mga changes sa GitHub

I-push ang mga nabago mong files gamit ang command na `git push`:
```bash
git push origin <dagdag-branch-name>
```
kung saan ang `<dagdag-branch-name>` ay ang pangalan ng branch na naidagdag mo kani-kanila lang.

## I-submit ang changes para sa review

Pumunta sa iyong repository sa GitHub at may makikita kang  `Compare & pull request` button, i-click mo ang tumutukoy na button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

I-submit ang pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Pagkalipas ng ilang oras ay isasama ko ang mga pagbabago na nagawa mo papunta sa master branch ng proyekto na ito. May makukuha kang notification email kapag ang mga pagbabago ay na-isama sa proyekto.

## Ano ang susunod na hakbang?


Congrats!  Nakumpleto mo ang standard _fork -> clone -> edit -> PR_ na workflow na lagi mong magagamit bilang isang kontribyutor!

I-celebrate ang iyong kontribusyon at i-share mo sa mga kaibigan at followers mo sa pagpunta sa [web app](https://firstcontributions.github.io/#social-share).

Puwede ka rin sumama sa aming Slack team kung kailangan mo ng karagdagan tulong o gustong magtanong. [Sumama sa aming Slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Ngayon, magsimula ka na mag-contribute sa ibang proyekto. Nagtipon kami ng listahan ng mga proyekto na may madaling issues na puwedeng-puwede kang makisabay. Paki-visit lang [ang listahan mula sa web app](https://firstcontributions.github.io/#project-list).

### [Mga karagdagan na materyal](../additional-material/git_workflow_scenarios/additional-material.md)


## Mga tutorials gamit ang ibang tools

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
