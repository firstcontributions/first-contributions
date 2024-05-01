[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Wax ku biirinta kowaad

Mashruucan ujeedadiisu waxey tahay in la fududeyo iyo in la hago kuwa bilawga ah si ay usameyan wax ku biirintooda kowaad "First contribution". Hadii aad raadinayso sida aad usameyn laheyd wax ku biirintaada kowaad, talaabooyinkan soo socda raac.


<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Haddii git uusan kuugu jirrin kombiyuutarkaaga, [Soo dagso](https://docs.github.com/en/get-started/quickstart/set-up-git).

## kala qeybi Kaydkan (Repository)

Kala qeybi kaydkan adigoo gujinayo badhanka kore ee page-ka kuna qoran "Fork".
Tani waxay ciwaankaga kudhax abuuri doontaa koobiga kaydkan

## Koobbi (clone) kaydka

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Hadda ku koobbi kaydkan kombiyuutarkaaga.Tag Akoonkaaga GitHub, Waxaad furtaa kaydki aad Kala qeybisay, Waxaad gujisa badhanka ku qoran "Code" ka dibna taabo koobiga sumadda sabuuradda.

Waxaad furta "Teminal" ka kadib waxad ku qorta amarada git-ka soo socda:

```
git clone "url-ka aad hadda soo koobbiyeysay"
```

Iyadoo "url-ka aad hadda soo koobbiyeysay"  (oo aan lahayn calaamadaha xigashada) uu yahay url-ka ama linkiga kaydkaan. waxaad dib usoo eegtaa talaabooyinkii hore si aad u hesho url-ka

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Tusaale:

```
git clone https://github.com/magaca-isticmalaha/first-contributions.git
```

Halka `magaca-isticmalaha` uu yahay magacaaga aad ku isticmasho Github.Halkan waxa aad kombayutarkaaga ku koobiyaynaysaa waxa ku jira kaydka wax ku biirinta koowaad ee GitHub.

## Abuur laan (branch)

Haddii aadan weli ku jirin galka (folder), u gudub halka uu kaaga yaalo galka kombiyuutarkaaga:

```
cd first-contributions
```

Abuur laan cusub adigoo isticmaalaya amarka `git checkout`:

```
git checkout -b <magacaada-cusub-ee-laanta>
```

Tusaale:

```
git checkout -b kudar-nur-farah-omar
```

Waajib ma ahan inaad ku darto ereyga `kudar` magaca laanta, laakin waxey uyeleysa micno maadama laantaan loo sameeyay in aad magacaada ku darto listiga wax kubiiriyasha.

## Samee isbedelada lagama maarmaanka ah oo gali (commit) Github isbedeladaas

Hadda ku fur faylka `Contributors.md` tafatiraha qoraalka,
Waa inaad aqoon u leedahay "Markdown", oo ah luqad calaamadeyn ah oo fudud. Fiiri [xaashida qishka](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) si aad u barato sida loo isticmaalo.
Ku dar magacaada, Hana ku darin bilowga ama dhamaadka faylka. Kudar meel kasta oo u dhaxaysa.

```
- [Magacaada](https://github.com/magaca-isticmalaha)
```

Tusaale:

```
- [Nur Farah](https://github.com/Nur-farah)
```

Hubi in aysan jirin meelo bannaan oo u dhexeeya `](`. Keydi oo xidh faylka.


<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Haddii aad tagto galka aad fuliso amarka `git status` waxaad arki doonta inay jiraan isbedelo

Ku dar isbeddeladaas laanta aad hadda abuurtay adigoo isticmaalaya ammarka `git add`:

```
git add Contributors.md
```

Hadda gali (commit) isbeddeladaas adigoo isticmaalaya amarka `git commit`:

```
git commit -m "Kudar Magacaada listiga wax biirinta kowaad"
```

Adigoo `Magacaada` ku badalayo magacaada shaqsiga.

(N.B: Waxaad ku qori kartaa fariinta xaqiijinta Ingiriisi maadaama aad la shaqayn doonto dad ka kala yimid meelo kala duwan oo adduunka ah.)

## Ku riix isbedelada GitHub

Riix isbedeladaada adigoo isticmaalaya amarka `git push`:

```
git push -u origin magaca-laantaada
```

Adigoo `magaca-laantaada` ku badalaya magaca laanta aad hore u abuurtay.

<details>
<summary> <strong>Haddii aad wax qalad ah aad aragto markaad riixayso, guji halkan:</strong> </summary>

- ### Cilad Xaqiijin
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Tag [casharrada GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) ee ku saabsan abuuritaanka iyo habaynta furaha SSH ee akoonkaaga

</details>

## Soo gudbi isbeddelladaada si dib loogu eego

Haddii aad tagto kaydkaaga GitHub,waxaad arki doontaa badhanka `Compare & pull request`. Badhankaas guji.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Hadda soo gudbi codsiga jiidista (pull request).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Dhawaan waxaan ku dari doonaa dhammaan isbeddelladaada laanta ugu weyn ee mashruucan (master). Waxaad heli doontaa iimayl ogeysiin ah marka isbeddelada la isku daro.

## Halkee laga aadaa halkan?

Hambalyo! Waxaad hadda dhamaystirtay heerka caadiga ah ee kalaqaybinta(fork) -> koobbi-ga (clone) -> wax kabedelka -> codsiga jiidista habka shaqada oo aad inta badan la kulmi doonto ka qaybqaate ahaan!

U dabaaldeg wax ku biirintaada oo la wadaag asxaabtaada iyo kuwa ku raacsan adiga oo aadaya [abka shabakada](https://firstcontributions.github.io/#social-share).

Waxaad ku biiri kartaa kooxdeena slack ah haddii aad u baahan tahay wax caawimo ah ama aad qabto wax su'aalo ah. [Ku biir kooxda slack ](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Hadda aan kuu bilowno ka qayb qaadashada mashaariicda kale. Waxaan soo diyaarinay liis mashruucyo ah oo leh qaladaad sahlan oo aad ku bilaabi karto. Fiiri [liiska mashaariicda ku jira abka shabakada](https://firstcontributions.github.io/#project-list).

### [Waxyaabo dheeraad ah](additional-material/git_workflow_scenarios/additional-material.md)

## Casharrada Isticmaalka Aalado Kale

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |