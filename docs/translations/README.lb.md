[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Éischt Bäiträg

Dëst Projet zielt drop of, d'Aart a Weis wéi Ufänger hiren éischte Bäitrag maachen ze vereinfachen an ze guidéieren. Wann Dir Ären éischte Bäitrag maache wëllt, befollegt d'Schrëtt hei ënnendrënner.

_Wann Dir Iech net mat der Kommandozeil vertraut maacht, [hei sinn Tutorials mat GUI-Tools.](#tutorials-using-other-tools)_
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Fork the repository" />

#### Wann Dir kee Git op Ärer Maschinn hutt, [installéiert et](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Fork dëst Repository

Forkéiert dëse Repository andeems Dir op de Fork-Knäppchen uewen op dëser Säit klickt.
Dëst erstellt eng Kopie vun dësem Repository an Ärem Kont.

## Klonéiert de Repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="klonéiert de Repository" />

Klonéiert elo de Fork-Repository op Äre Computer. Gitt op Äre GitHub-Kont, maacht de Fork-Repository op, klickt op de Code-Knäppchen, dann op den SSH-Tab an dann op d'Ikon _copy url to clipboard_.

Maacht en Terminal op a féiert de folgende Git-Kommando aus:

```bash
git clone "url you just copied"
```
wou "URL déi Dir grad kopéiert hutt" (ouni d'Zitatzeechen) d'URL zu dësem Repository ass (Är Fork vun dësem Projet). Kuckt déi viregt Schrëtt fir d'URL ze kréien.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="URL an d'Zwëschespeicher kopéieren" />

Zum Beispill:

```bash
git clone git@github.com:this-is-you/first-contributions.git
```

wou `this-is-you` Äre GitHub Benotzernumm ass. Hei kopéiert Dir den Inhalt vum first-contributions Repository op GitHub op Äre Computer.

## Eng Branche erstellen

Ännert an den Repository Verzeichnis op Ärem Computer (wann Dir nach net do sidd):

```bash
cd first-contributions
```

Erstellt elo eng Branch mat dem `git switch` Kommando:

```bash
git switch -c your-new-branch-name
```

Zum Beispill:

```bash
git switch -c add-alonzo-church
```

<details>
<summary> <strong>Wann Dir Feeler beim Gebrauch vu Git Switch kritt, klickt hei:</strong> </summary>

Wann d'Fehlermeldung "Git: `switch` is not a git command. See `git –help`" erscheint, ass et wahrscheinlech well Dir eng méi al Versioun vu Git benotzt.

An dësem Fall, probéiert amplaz `git checkout` ze benotzen:

```bash
git checkout -b your-new-branch-name
```

</details>

## Maacht déi néideg Ännerungen a confirméiert dës Ännerungen

Maacht elo d'Datei `Contributors.md` an engem Texteditor op a setzt Ären Numm derbäi. Füügt se net um Ufank oder um Enn vun der Datei derbäi. Setzt se iergendwou dertëschent. Späichert elo d'Datei.

<img align="right" width="450" ​​src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Wann Dir an den Projetverzeichnis gitt an de Kommando `git status` ausféiert, gesitt Dir, datt et Ännerungen gëtt.

Füügt dës Ännerungen an de Branch bäi, deen Dir just mam Kommando `git add` erstallt hutt:

```bash
git add Contributors.md
```

Confirméiert elo dës Ännerungen mam Kommando `git commit`:

```bash
git commit -m "Add your-name to Contributors list"
```

Ersatz vun `your-name` duerch Ären Numm.

## Ännerungen op GitHub verschécken

Är Ännerungen mat dem Kommando `git push` verschécken:

```bash
git push -u origin your-branch-name
```

`your-branch-name` duerch den Numm vun der Branch ersat, déi Dir virdru erstallt hutt.

<details>
<summary> <strong>If you get any errors while pushing, click here:</strong> </summary>

- ### Authentifikatiounsfehler
<pre>remote: D'Ënnerstëtzung fir Passwuertauthentifikatioun gouf den 13. August 2021 ewechgeholl. Benotzt w.e.g. amplaz en perséinlechen Zougangstoken.
remote: Kuckt w.e.g. https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ fir méi Informatiounen.
fatal: D'Authentifikatioun fir 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre> ass gescheitert.
Gitt an den [GitHub säin Tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) fir d'Generéierung an d'Konfiguratioun vun engem SSH-Schlëssel fir Äre Kont.
Dir kënnt och 'git remote -v' ausféieren fir Är Remote-Adress ze kontrolléieren.

Wann et sou ausgesäit:
<pre>origin https://github.com/your-username/your_repo.git (fetch)
origin https://github.com/your-username/your_repo.git (push)</pre>

ännert et mat dësem Kommando:
```bash
git remote set-url origin git@github.com:your-username/your_repo.git
```
Soss gitt Dir ëmmer nach no engem Benotzernumm a Passwuert gefrot an Dir kritt en Authentifikatiounsfehler.
</details>

## Gitt Är Ännerungen zur Iwwerpréiwung an
IWann Dir op Äert Repository op GitHub gitt, gesitt Dir e Knäppchen `Compare & Pull Request`. Klickt op dëse Knäppchen.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create Pull Request" />

Elo gitt d'Pull Request of.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit Pull Request" />

Geschwënn wäert ech all Är Ännerungen an den Haaptbranch vun dësem Projet zesummeféieren. Dir kritt eng Notifikatioun per E-Mail soubal d'Ännerunge zesummegefaasst sinn.

## Wou geet et weider?

Gratulatioun! Dir hutt just de Standard _fork -> clone -> edit -> pull request_ Workflow ofgeschloss, op deen Dir als Mataarbechter dacks stéisst!
Feiert Äre Bäitrag a deelt en mat Äre Frënn a Follower andeems Dir op [Web App](https://firstcontributions.github.io/#social-share) gitt.

Wann Dir méi Übung wëllt, kuckt Iech [Codebäiträg](https://github.com/roshanjossey/code-contributions) un.

Loosst eis elo ufänken, un anere Projeten bäizedroen. Mir hunn eng Lëscht vu Projeten mat einfache Froen zesummegestallt, mat deenen Dir ufänke kënnt. Kuckt Iech [d'Lëscht vun de Projeten an der Web App](https://firstcontributions.github.io/#project-list) un.

### [Zousätzlecht Material](docs/additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials mat aneren Tools

| <a href="docs/gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="docs/gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="docs/gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="docs/gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](docs/gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](docs/gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](docs/gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](docs/gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
