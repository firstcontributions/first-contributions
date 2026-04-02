[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _Gba kpam hemen sha [asol sha mbatsav](docs/translations/Translations.md)._

# Ikyôrun U Ken Ken

Tar sha iyol a faan sha mba u gba ikyôrun sha ken ken, ngu i de ka mba u gba ikyôrun sha ken ken kpaa hemen. Ka i yô u gba ikyôrun sha ken ken, kpe iyol sha i kpe je.

_Ka i bua u sha command line, [kpe iyol sha je u sha GUI tools.](#tutorials-using-other-tools)_

#### Ka git a gba sha machine sha ër, [nom er](https://docs.github.com/en/get-started/quickstart/set-up-git).

---

## Fork Repository A

Fork repository a sha u gbe button sha fork sha ier sha page a. Ngu i mba u ter copy sha repository sha sha account sha ër.

---

## Clone Repository A

Ngu clone repository sha u fork sha er sha machine sha ër. Kpe sha GitHub account sha ër, yev repository sha u fork sha, gbe sha code button, hemen sha SSH tab, hemen gbe sha icon sha _copy url to clipboard_.

Yev terminal, nom u sha git command sha je:

```bash
git clone "url u u copy sha"
```

sha "url u u copy sha" (ka kpaa quotation marks) i yô url sha repository a (fork sha project sha je sha ër). Kpe iyol sha i kpe sha je u ngu url.

Ka sha instance:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

sha `this-is-you` i yô GitHub username sha ër. Sha hemen, u kpe contents sha repository sha first-contributions sha GitHub sha computer sha ër.

---

## Ter Branch

Faan sha directory sha repository sha computer sha ër (ka a gba sha sha ër):

```bash
cd first-contributions
```

Ngu ter branch sha u sha command sha `git switch`:

```bash
git switch -c zwa-branch-sha-ken-ken
```

Ka sha instance:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>Ka u ngu mba sha git switch, gbe sha hemen:</strong> </summary>

Ka error sha "Git: `switch` is not a git command. See `git –help`" a yev, i yô sha sha u yô u sha version sha git sha gben. Sha hemen, ngu u sha `git checkout` sha:

```bash
git checkout -b zwa-branch-sha-ken-ken
```

</details>

---

## Nom Sha U Faan U Nom Sha Commit

Ngu yev `Contributors.md` file sha sha text editor, nom iyol sha ër sha sha er. Ngu nom sha sha asen sha sha iyol. Nom sha sha bande. Ngu, save file a.

Ka u kpe sha project directory u nom command sha `git status`, u mba u yev sha sha nom sha sha.

Nom sha sha branch sha u ter sha u sha command sha `git add`:

```bash
git add Contributors.md
```

Ngu commit sha sha sha u sha command sha `git commit`:

```bash
git commit -m "Add iyol-sha-ër sha Contributors list"
```

u faan `iyol-sha-ër` sha iyol sha ër.

---

## Push Sha U Nom Sha GitHub

Push sha sha u nom sha u sha command sha `git push`:

```bash
git push -u origin zwa-branch-sha-ër
```

u faan `zwa-branch-sha-ër` sha iyol sha branch sha u ter sha sha je.

<details>
<summary> <strong>Ka u ngu mba sha u push, gbe sha hemen:</strong> </summary>

- ### Authentication Error
  Ka error sha authentication a yev, kpe sha [GitHub tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) u nom u SSH key sha account sha ër.

</details>

---

## Nom Sha U Nom Sha U Kpaa Review

Ka u kpe sha repository sha ër sha GitHub, u mba u yev button sha `Compare & pull request`. Gbe sha button sha je.

Ngu nom pull request sha.

Sha hemen, i mba u merge sha sha sha nom sha sha sha main branch sha project a. U mba u ngu notification email sha u merge sha sha sha nom sha sha.

---

## Sha Iyol Sha U Kpe Sha?

Congrats! U nom sha ikyôrun sha ken ken sha _fork -> clone -> edit -> pull request_ sha u mba sha sha contributor!

Celebrate sha ikyôrun sha ër u share sha sha mbatsav sha ër sha u kpe sha [web app](https://firstcontributions.github.io/#social-share).

Ka u yô u nom practice, kpe sha [code contributions](https://github.com/roshanjossey/code-contributions).

Ngu kpe sha [list sha projects sha web app](https://firstcontributions.github.io/#project-list).

### [Iyol sha gben](docs/additional-material/git_workflow_scenarios/additional-material.md)

---

## Tutorials U Sha Tools Sha Gben

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md) |