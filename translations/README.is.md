# Fyrsta Framlag

Þetta project er til að einfalda og leiðbeina byrjendum við að búa til þeirra fyrsta framlag. Ef þetta er eitthvað sem þig langar að læra, endilega fylgdu eftir skrefunum hér fyrir neðan.

_Ef þú kannt ekki við þig í skel og vilt frekar nota grafískt viðmót. [leiðbeiningar til að nota grafísk viðmót.](#tutorials-using-other-tools)_


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Ef þú ert ekki með git uppsett á tölvunni þinni [skoðaðu þessar leiðbeiningar](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Afrita þetta gagnasafn (fork)

Afritaður þetta gagnasafn með því að smella á "Fork" takkann hér efst á síðunni.
Þá verður til afrit af þessu gagnasafni inni á þinni síðu.

## Afrita gagnasafnið til vinnslu (clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Næst er að afrita gagnasafnið þitt inn á vélina þína til vinnslu. Farðu inn á GitHub aðgang þinn, opnaðu gagnasafnið þitt sem þú varst að búa til, veldu "Code" takkann og síðan "Copy to clipboard".

Opnaðu skel og skrifaðu eftirfarandi skipun:

```
git clone "slóðin sem þú varst að afrita"
```

Þar sem "Slóðin sem þú varst að afrita" (án gæsalappa) er slóðin inn á gagnasafn (gagnasafn þitt sem þú varst að afrita á þinni síðu). Sjá fyrri skref til að finna þá slóð.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Til dæmis:

```
git clone https://github.com/this-is-you/first-contributions.git
```

þar sem `this-is-you` er GitHub notendanafn þitt. Með þessu ertu að afrita innihald gagnasafnsins sem þú varst að setja upp á þinni síðu inn á tölvuna þína.

## Stofnun á grein (branch)

Færðu þig inn á gagnasafns möppuna á þinni tölvu (ef þú ert ekki þar þegar):

```
cd first-contributions
```

Næst stofnar þú nýja grein (branch) með því að nota `git switch` skipunina:

```
git switch -c your-new-branch-name
```

Til dæmis:

```
git switch -c add-alonzo-church
```

## Búa til nauðsynlegar breytingar og vista (commit)

Opnaðu `Contributors.md` skrána í skráarvinnslu forriti, bættu þínu nafni í skrána. Ekki bæta því við alveg í byrjun eða enda skráar. Getur sett það hvar sem er annarstaðar inn á milli. Vistaðu síðan skrána.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ef þú ferð næst í project skrána og keyrir skipunina `git status`, þá kemur frama að það hafa verið gerðar breytingar.

Bættu þeim breytingum við greinina sem þú skapaðir áður og ert þegar í með `git add` skipuninni.

```
git add Contributors.md
```
Næst vistaru þær breytingar með commit skipuninni `git commit`:

```
git commit -m "Add your-name to Contributors list"
```

Skiptir út `your-name` og setur þitt nafn í staðinn.

## Ýta/senda (push) nýjust breytingum til GitHub

Sendu nýjustu breytingar með `git push` skipuninni:

```
git push -u origin your-branch-name
```

skiptu `your-branch-name` út fyrir nafnið á greininni sem þú stofnaðir áður.

<details>
<summary> <strong>Ef upp koma villur þegar þú sendir, smelltu hér:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

</details>

## Senda þínar breytingar inn til yfirferðar

Inni á gagnasafns síðunni á GitHub síðu þinni getur þú séð `Compare & pull request` takka. Smelltu á þann takka.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Sendu inn pull óskina með því að ýta á `Create pull request`.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Fljótlega verður síðan pull ósk þín yfirfarin og samþykkt af upphaflega höfundi/umsjónamanni verkefnisins og sameinuð inn í það. Þú færð tilkynningu í tölvupósti þegar það gerist.

## Hvað geri ég svo næst?

Congrats! You just completed the standard _fork -> clone -> edit -> pull request_ workflow that you'll often encounter as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io/#social-share).

You could join our slack team if you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Viðbótar kennsluefni](additional-material/git_workflow_scenarios/additional-material.md)

## Kennsluefni fyrir önnur tól

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
