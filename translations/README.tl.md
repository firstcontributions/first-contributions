[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Mga unang kontribusyon

Mahirap. Laging mahirap sa unang beses ng anumang gawain. Lalo na sa isang kolaborasyon, kung saan hindi komportableng tignan at usapan ang mga pagkakamali. Gusto naming simplehan at linawin ang modernong pamamaraan kung papaanong matuto at tumulong ang mga bagong *open-source contributors*.

Maaaring makatulong ang pagbabasa ng mga artikulo at panonood ng mga *tutorials*, pero ano pa bang mas epektibong pamamaraan kaysa sa aktual na aplikasyon sa isang pagsasanay? Ang pangunahing pakay ng proyektong ito ay gabayin ang mga baguhan na gawin ang kanilang unang *contribution*. Kung ikaw ay isa sa mga taong iyon, sundin lang ang ibabang instruksyon.

#### *Kung hindi ka komportable na gumamit ng *command line*, [ito ay mga tutorials gamit ang mga *GUI* tools.]( #tutorials-using-other-tools )*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Kung hindi naka-*install* ang *git* sa iyong kompyuter, [i-install mo](https://help.github.com/articles/set-up-git/).

## I-fork ang repository

I-fork ang repository sa pamamagitan ng pag-click ng *fork* button na matatagpuan sa bandang itaas ng webpage na ito.
Magkakaroon na ng kopya ng repository na ito sa iyong account.

## I-clone ang repository

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Ngayon, i-clone ang ngayong na-forked na repository sa iyong kompyuter. Pumunta lang sa iyong GitHub account, buksan ang nai-forked na repository, i-click ang clone button pagkatapos i-click ang *copy to clipboard* icon.

Buksan ang terminal at i-enter ang sumusunod na git command:

```
git clone "url na nakopya mo"
```
kung saan ang "url na nakopya mo" (wala ang mga quotation marks) ay ang url ng repository (iyong fork ng proyekto). Pakitingin  nang mabuti ang mga nakaraan na hakbang upang makuha ang url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Halimbawa:
```
git clone https://github.com/iyong-username/first-contributions.git
```
kung saan ang `iyong-username` ang iyong username sa GitHub. Mula sa command na ito, dito nagsisimula ng paggawa ng kopya ng nilalaman ng first-contributions repository mula sa GitHub papunta sa iyong kompyuter.

## Gumawa ng isang branch

Pumunta sa directory ng iyong repository sa iyong kompyuter (kung hindi ka pa nakapunta):

```
cd first-contributions
```
Ngayon, gumawa na ng isang branch gamit ang `git checkout` command:
```
git checkout -b <dagdag-branch-name>
```

For example:
```
git checkout -b dagdag-juan-dela-cruz
```
(Hindi kailangan ng salitang *"dagdag"* sa pangalan ng nadagdag na branch pero makatwiran pa rin na gawin dahil layunin ng branch ang pagdagdag ng iyong pangalan sa isang listahan.)

## Gumawa ng kinakailangan na pagbabago at i-commit ang mga natukoy na pagbabago

Ngayon, buksan ang `Contributors.md` file sa isang text editor, idagdag ang iyong pangalan. Huwag mo idagdag sa simula o sa hulian ng tinutukoy na file. Ilagay sa kalagitnaan ng file. At i-save and file.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />


Kung pumunta ka sa directory ng iyong proyekto at i-enter ang command na `git status`, may makikita kang mga pagbabago.


Idagdag ang mga pagbabagong naganap papunta sa iyong branch gamit ang `git add` command:

```
git add Contributors.md
```

Ngayon, i-commit ang mga nabagong files gamit ang `git commit` command:
```
git commit -m "Add <your-name> to Contributors list"
```
kung saan ang `<your-name>` ay ang iyong pangalan.

## I-push ang mga changes sa GitHub

I-push ang mga nabago mong files gamit ang command na `git push`:
```
git push origin <dagdag-branch-name>
```
kung saan ang `<dagdag-branch-name>` ay ang pangalan ng branch na naidagdag mo kani-kanila lang.

## I-submit ang changes para sa review

Pumunta sa iyong repository sa GitHub at may makikita kang  `Compare & pull request` button, i-click mo ang tumutukoy na button.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

I-submit ang pull request.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Mga oras na nakalipas at sasamahin ko ang mga pagbabago na nagawa mo papunta sa master branch ng proyekto na ito. May makukuha kang notification email kapag ang mga pagbabago ay na-isama sa proyekto.

## Saan na mula rito?

Congrats!  Nakumpleto mo ang standard _fork -> clone -> edit -> PR_ na workflow na laging mong makakasalamuha bilang isang kontribyutor!

I-celebrate ang iyong kontribusyon at i-share mo sa mga kaibigan at followers mo sa pagpunta sa [web app](https://firstcontributions.github.io/#social-share).

Puwede ka rin sumama sa aming Slack team kung kailangan mo ng karagdagan tulong o gustong magtanong. [Sumama sa aming Slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Ngayon, magsimula ka na mag-contribute sa ibang proyekto. Nagtipon kami ng listahan ng mga proyekto na may madaling issues na puwedeng-puwede kang makisabay. Paki-visit lang [ang listahan mula sa web app](https://firstcontributions.github.io/#project-list).

### [Mga karagdagan na materyal](additional-material/git_workflow_scenarios/additional-material.md)


## Mga tutorials gamit ang ibang tools

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Visual_Studio_2017_Logo.svg/800px-Visual_Studio_2017_Logo.svg.png" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

