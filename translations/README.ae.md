[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1n4y7xnk0-DnLVTaN6U9xLU79H5Hi62w)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)



# Unua Kontribuoj

Tiu ĉi projekto celas simpligi kaj gvidi la vojon per kiu komencantoj faras sian unuan kontribuon. Se vi celas fari vian unuan kontribuon, sekvu la paŝojn sube.

_Se vi ne sentas vin komforta per la komandlinio, [jen instruiloj uzante GUI-ilojn.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Se vi ne havas giton sur via maŝino, [instalu ĝin](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Forku tiun ĉi deponejon

Forku tiun ĉi deponejon klakante sur la forkknupon en la supra parto de tiu ĉi paĝo.
Tio kreos kopion de tiu ĉi deponejo en via konto.

## Klonu la deponejon

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Nun klonu la forkitan deponejon al via komputilo. Iru al via GitHub-konto, malfermu la forkitan deponejon, klaku sur la butono "kodo" kaj poste klaku sur la ikono _kopi al klembordo_.

Malfermu terminalon kaj rulu la jenan gitan komandon:

```bash
git clone "URL-n vi ĵus kopiis"
```

kie "URL-n vi ĵus kopiis" (sen la citiloj) estas la URL al ĉi tiu deponejo (via forko de ĉi tiu projekto). Vidu la antaŭajn paŝojn por akiri la URL-on.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Ekzemple:

```bash
git clone git@github.com:tiu-estas-vi/first-contributions.git
```

kie `tiu-estas-vi` estas via GitHub-uzantnomo. Ĉi tie vi kopias la enhavon de la first-contributions-deponejo en GitHub al via komputilo.

## Kreu branĉon

Ŝanĝu al la dosierujo de la deponejo sur via komputilo (se vi jam ne estas tie):

```bash
cd first-contributions
```

Nun kredu branĉon uzante la `git switch`-komandon:

```bash
git switch -c via-nova-branĉo-nomo
```

Ekzemple:

```bash
git switch -c add-alonzo-church
```

## Faru necesajn ŝanĝojn kaj registru tiujn ŝanĝojn

Nun malfermu la dosieron `Contributors.md` en teksta redaktilo, aldonu vian nomon al ĝi. Ne aldonu ĝin je la komenco aŭ fino de la dosiero. Metu ĝin ie interne. Nun, konservu la dosieron.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Se vi iras al la projekta dosierujo kaj plenumas la komandon `git status`, vi vidos ke estas ŝanĝoj.

Aldonu tiujn ŝanĝojn al la branĉo, kiun vi ĵus kreis, uzante la `git add`-komandon:

```bash
git add Contributors.md
```

Nun registru tiujn ŝanĝojn uzante la `git commit`-komandon:

```bash
git commit -m "Add your-name to Contributors list"
```

anstataŭigante `your-name` per via nomo.

## Push changes to GitHub

Alpuŝu viajn ŝanĝojn uzante la komandon `git push`:

```bash
git push -u origin your-branch-name
```

anstataŭigante `your-branch-name` per la nomo de la branĉo, kiun vi kreis antaŭe.

<details>
<summary> <strong>Se vi ricevas ajnan eraron dum alpuŝado, klaku ĉi tie:</strong> </summary>

- ### Aŭtentikiga Eraro
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Iru al [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) pri generado kaj agordo de SSH-ŝlosilon al via konto.

</details>

## Submetu viajn ŝanĝojn por revizio

Se vi iras al via deponejo en GitHub, vi vidos butonon `Compare & pull request`. Klaku sur tiu butono.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Nun sendu la peton pri aldoni.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Baldaŭ mi kunfandos ĉiujn viajn ŝanĝojn en la ĉefan branĉon de ĉi tiu projekto. Vi ricevos retpoŝtan avizon, kiam la ŝanĝoj estos kunfanditaj.

## Kien iri de ĉi tie?

Gratulojn! Vi ĵus finis la standardan _forku -> klonu -> redaktu -> petu aldonon_ fluon kiun vi ofte renkontos kiel kontribuanto!

Festu vian kontribuon kaj dividi ĝin kun viaj amikoj kaj sekvantoj irante al [retejo](https://firstcontributions.github.io/#social-share).

Vi povus aliĝi al nia slack-teamo se vi bezonas ian helpon aŭ havas iajn demandojn. [Aliĝu al slack-teamo](https://firstcontributors.slack.com/join/shared_invite/zt-29qhyr9lt-Bi7WLbgGIFqV7aCEG_grvg#/shared-invite/email).

Nun ni ekintigu vin pri kontribuado al aliaj projektoj. Ni kunmetis liston de projektoj kun facilaj problemoj, pri kiuj vi povus ekfari. Rigardu [la liston de projektoj en la retejo](https://firstcontributions.github.io/#project-list).

### [Plia materialo](additional-material/git_workflow_scenarios/additional-material.md)

## Instruoj Uzante Aliajn Ilarojn

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

<p>Ĉi tiu projekto estas subtenata de:</p>
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
