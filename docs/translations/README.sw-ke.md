[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

#### _Soma toleo hili katika [lugha nyingine](../translations/Translations.md)._

# Mchango Wako wa Kwanza (First Contributions)

Mradi huu una lengo la kurahisisha na kuwaongoza wanaoanza jinsi ya kufanya mchango wao wa kwanza katika mradi wa programu huria (open source). Ikiwa unatafuta jinsi ya kufanya mchango wako wa kwanza, fuata hatua zilizoainishwa hapa chini.

_Iwapo hujazoea kutumia amri za kompyuta (command line), [hapa kuna mafunzo yanayotumia zana za GUI.](#mafunzo-kwa-kutumia-zana-nyingine)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />

#### Iwapo huna git kwenye kompyuta yako, [iweke kwanza (install)](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Fanya "fork" kwa hifadhi hii (repository)

Fanya "fork" kwa hifadhi hii kwa kubofya kitufe cha fork kilicho juu ya ukurasa huu.
Hatua hii itaunda nakala ya hifadhi hii kwenye akaunti yako.

## Fanya "clone" kwa hifadhi hii

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone the repository" />

Sasa fanya "clone" kwa hifadhi uliyoifanyia fork kuja kwenye kompyuta yako. Nenda kwenye akaunti yako ya GitHub, fungua hifadhi uliyoifanyia fork, bofya kitufe cha "Code", kisha kichupo cha SSH, kisha bofya aikoni ya _nakili kiungo (URL) kwenye clipboard_.

Fungua terminal na endesha amri ifuatayo ya git:

```bash
git clone "kiungo ulichonakili hivi punde"
```

ambapo "kiungo ulichonakili hivi punde" (bila alama za nukuu) ni kiungo (URL) cha hifadhi hii (fork yako ya mradi huu). Angalia hatua zilizotangulia kupata kiungo hicho.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Kwa mfano:

```bash
git clone git@github.com:huyu-ndiwe/first-contributions.git
```

ambapo `huyu-ndiwe` ni jina lako la mtumiaji (username) la GitHub. Hapa unanakili maudhui ya hifadhi ya first-contributions iliyoko GitHub kuja kwenye kompyuta yako.

## Unda tawi (branch)

Nenda kwenye saraka (directory) ya hifadhi hii kwenye kompyuta yako (ikiwa haupo huko tayari):

```bash
cd first-contributions
```

Sasa unda tawi kwa kutumia amri ya `git switch`:

```bash
git switch -c jina-la-tawi-lako-jipya
```

Kwa mfano:

```bash
git switch -c ongeza-alonzo-church
```

<details>
<summary> <strong>Ikiwa utapata hitilafu (error) yoyote unapotumia git switch, bofya hapa:</strong> </summary>

Ikiwa ujumbe wa hitilafu "Git: `switch` is not a git command. See `git –help`" utaonekana, huenda ni kwa sababu unatumia toleo la zamani la git.

Katika hali hii, jaribu kutumia `git checkout` badala yake:

```bash
git checkout -b jina-la-tawi-lako-jipya
```

</details>

## Fanya mabadiliko yanayohitajika na uwasilishe (commit) mabadiliko hayo

Sasa fungua faili la `Contributors.md` kwa kutumia kihariri cha maandishi (text editor), ongeza jina lako humo. Usiliweke mwanzoni au mwishoni mwa faili. Liweke mahali popote katikati. Sasa hifadhi (save) faili hilo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Ukienda kwenye saraka ya mradi na kuendesha amri `git status`, utaona kuna mabadiliko.

Ongeza mabadiliko hayo kwenye tawi ulilounda hivi punde kwa kutumia amri ya `git add`:

```bash
git add Contributors.md
```

Sasa wasilisha (commit) mabadiliko hayo kwa kutumia amri ya `git commit`:

```bash
git commit -m "Ongeza jina-lako kwenye orodha ya Contributors"
```

ukibadilisha `jina-lako` na jina lako halisi.

## Sukuma (push) mabadiliko kwenda GitHub

Sukuma mabadiliko yako kwa kutumia amri `git push`:

```bash
git push -u origin jina-la-tawi-lako
```

ukibadilisha `jina-la-tawi-lako` na jina la tawi ulilolliunda hapo awali.

<details>
<summary> <strong>Ikiwa utapata hitilafu yoyote wakati wa kusukuma (push), bofya hapa:</strong> </summary>

- ### Hitilafu ya Uthibitishaji (Authentication Error)
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/&lt;jina-lako-la-mtumiaji&gt;/first-contributions.git/'</pre>
  Nenda kwenye [mafunzo ya GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) kuhusu jinsi ya kuunda na kusanidi ufunguo wa SSH kwenye akaunti yako.

  Pia, huenda ukahitaji kuendesha amri 'git remote -v' kuangalia anwani ya remote yako.

  Ikiwa itaonekana kama ifuatavyo:
  <pre>origin	https://github.com/jina-lako-la-mtumiaji/mradi-wako.git (fetch)
  origin	https://github.com/jina-lako-la-mtumiaji/mradi-wako.git (push)</pre>

  ibadilishe kwa kutumia amri hii:
  ```bash
  git remote set-url origin git@github.com:jina-lako-la-mtumiaji/mradi-wako.git
  ```
  La sivyo, bado utaulizwa jina la mtumiaji na nywila (password) na kupata hitilafu ya uthibitishaji.
</details>

## Wasilisha mabadiliko yako kwa ukaguzi (review)

Ukienda kwenye hifadhi yako kwenye GitHub, utaona kitufe cha `Compare & pull request`. Bofya kitufe hicho.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

Sasa wasilisha ombi la kuunganisha (pull request).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Hivi karibuni, nitaunganisha mabadiliko yako yote kwenye tawi kuu (main branch) la mradi huu. Utapokea barua pepe ya arifa mara mabadiliko yatakapokamilika kuunganishwa.

## Hatua inayofuata ni ipi?

Hongera! Umekamilisha mtiririko wa kawaida wa _fork -> clone -> edit -> pull request_ ambao utaukumbana nao mara kwa mara ukiwa mchangiaji wa miradi mingine!

Sherehekea mchango wako na uushiriki na marafiki na wafuasi wako kwa kwenda kwenye [programu ya wavuti (web app)](https://firstcontributions.github.io/#social-share).

Ikiwa ungependa mazoezi zaidi, angalia [michango ya msimbo (code contributions)](https://github.com/roshanjossey/code-contributions).

Sasa hebu tukusaidie kuanza kuchangia kwenye miradi mingine. Tumekusanya orodha ya miradi yenye masuala (issues) rahisi unayoweza kuanzia. Angalia [orodha ya miradi kwenye programu ya wavuti](https://firstcontributions.github.io/#project-list).

### [Maudhui ya ziada](../additional-material/git_workflow_scenarios/additional-material.md)

## Mafunzo kwa Kutumia Zana Nyingine

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/960px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |
