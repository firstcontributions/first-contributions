[![Bolingo ya Logiciel Libre](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Makabo nto contribution ya Liboso

Ezalaka ntango nyonso mpasi mpo na moto kosala eloko moko mpo na mbala ya liboso. Kobanga kosala mabunga nto erreurs ezalaka malamu te, mingimingi ntango ozali kosala mosala elongo na bato mosusu. Kasi mokili ya logiciel libre ezali likambo ya kosala mosala elongo mpe kosala na kati ya etuluku nto groupe. Yango wana, tolingi kopesa nzela ya pete mpo na baye bazali kobanda kopesa makabo nto mpe contribution na logiciel libre na koteya bino ndenge ya kosala contribution mpo na mbala ya liboso.

Kotánga ba articles mpe ba tutoriels ekoki kosalisa, kasi nini eleki malamu koleka komeka na kozanga kobanga kosala mabunga nto mpe erreur? Projet oyo ezali na mokano ya kopesa toli mpe kopesa nzela ya pete mpo na ndenge bayekoli bakoki kopesa contribution na bango ya liboso. Kobosana te: soki ozali na kimya mingi, okoyekola malamu. Soki olingi kopesa makabo nto mpe contribution na yo ya liboso, landa kaka ba étapes oyo ezali awa na nse. Nalaki yo, ekozala esengo.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="Kopela dépôt oyo na compte na yo ya GitHub" />

Soki ozali naino na Git te na machine na yo, [ installe-yango ](https://help.github.com/articles/set-up-git/).

## Kosala fork ya dépôt oyo

Sala fork ya dépôt oyo na kokliké na bouton _fork_ neti elakisami na bilili oyo likoló.
Yango ekosala copie ya dépôt oyo na compte na yo moko ya GitHub.

## Kosala clone ya répertoire oyo

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="Sala clone ya dépôt oyo na ordinateur na yo" />

Sikoyo, sala clone ya répertoire oyo na ordinateur na yo. Kende na compte na yo ya GitHub, fungola dépôt oyo osali fork, kliké na bouton _Code_, na nsima na onglet _SSH_ mpe na nsuka na icône _copier dans le presse-papier_.

Fungola invite de commande (soki ozali na Windows) to terminal (soki ozali na MacOS to Linux) mpe sala commande git oyo elandi:

[Okoki mpe koinstallé Git bash na Windows nayo soki](https://gitforwindows.org/)

```bash
git clone "lien ya repertoire oyo okopié"
```

esika "lien ya repertoire oyo okopié" (longola ba guillemets) ezali url ya dépôt oyo osali fork. Talá lisusu ba étapes ya liboso mpo na kozwa URL ya solo.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="Kopa URL na presse-papiers" />

Na ndakisa:

```bash
git clone https://github.com/kombo-na-yo-ya-utilisateur/first-contributions.git
```

esika `kombo-na-yo-ya-utilisateur` ezali kombo na yo ya utilisateur ya GitHub. Awa ozali kokopié ba contenus ya dépôt `first-contributions` uta na GitHub na ordinateur na yo.

## Kosala branche moko

Kende na répertoire ya projet oyo osili kosala clone (soki ozali naino na kati te):

```bash
cd first-contributions
```

Sikoyo sala branche moko na commande `git checkout`:

```bash
git checkout -b <tia-kombo-na-yo>
```

Na ndakisa:

```bash
git checkout -b add-emmanuel-binen
```

(Kombo ya branche kozala na kozala na liloba _add_ ezali ya mutuya te, kasi ezali malamu koyekola yango mpo tina ya branche oyo ezali mpo na kobakisa kombo na yo na liste.)

<details> <summary> <strong>Soki okutani na libunga na git switch, kliká awa:</strong> </summary>
Soki message "Git: switch is not a git command. See git –help" ebimi, ezali mpo ozali kosalela version ya kala ya Git.

Na likambo yango, meká nde:

```bash
git checkout -b kombo-ya-branche-na-yo-ya-sika
```

</details>

## Sala ba modifications oyo esengeli mpe enregistrer yango

Fungola fichier `Contributors.md` na éditeur ya texte, bakisá kombo na yo kuna, mpe enregistrer yango. Kobakisa yango te na ebandeli to na nsuka ya fichier, kasi esika moko na katikati.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="Résultat ya commande git status" />

Soki ofungoli terminal de commande mpe osali commande `git status`, okomona ete ezali na ba modifications. Bakisá ba modifications yango na branche oyo osili kosala na commande `git add`:

```bash
git add Contributors.md
```

Sikoyo sala commit ya ba modifications yango na commande `git commit`:

```bash
git commit -m "Add <kombo-na-yo> to Contributors list"
```

longola `<kombo-na-yo>` mpe bakisa kombo na yo moko.

## Tinda ba modifications na GitHub

Pusa ba modifications na yo na commande `git push`:

```bash
git push -u origin <kombo-ya-branche-na-yo>
```

longola makomi oyo `<kombo-ya-branche-na-yo>` mpe tia kombo ya branche oyo osili kosala.

<details> <summary> <strong>Soki ozwi ba erreurs ntango ya kopusa ba modifications, kliké awa:</strong> </summary>

- ### Erreur ya authentification
  <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead. remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information. fatal: Authentication failed for 'https://github.com/<kombo-na-yo-ya-utilisateur>/first-contributions.git/'</pre>
  Landa tutoriel ya GitHub mpo na kosala mpe ko configurer clé SSH na compte na yo.

Okoki mpe kosala `git remote -v` mpo na kotala adresse na yo ya mosika.

Soki ezali lokola oyo:

<pre>origin https://github.com/kombo-na-yo-ya-utilisateur/ton_repo.git (fetch) origin https://github.com/kombo-na-yo-ya-utilisateur/ton_repo.git (push)</pre>

Bongisa yango na commande oyo:

```bash
git remote set-url origin git@github.com:kombo-na-yo-ya-utilisateur/ton_repo.git
```

Soki te, okokoba komona kokɔtisa mot de passe na yo mpe na suka okozua erreur ya authentification.

</details>

## Tinda contribution na yo mpo na kotala

Soki okeyi na répertoire na yo na Github, okomona bouton `Compare & pull request`. Kliké na yango.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="Kosala pull request" />

Na nsima, tinda _pull request_.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="Kotinda pull request" />

Nakotia ba modifications na yo na branche principale ya projet kala mingi te.
Sima okozwa e-mail ya confirmation soki yango esalemi.

Branche main ya dépôt na yo oyo osali fork ekobongwana te. Mpo ete dépôt na yo ezala synchronisé na ya ngai, landa ba étapes oyo elandi.

## Tiká fork na yo ezala synchronisé na répertoire oyo

Ya liboso, kende na branche main

```bash
git checkout main
```

Mpe bakisá url ya répertoire na ngai lokola `upstream remote url`:

```bash
git remote add upstream https://github.com/Emmanuelbinen/first-contributions
```

Oyo ezali lolenge moko ya koyebisa git ete version mosusu ya répertoire oyo ezali na adresse oyo epesami mpe tobengi yango `upstream`. Soki ba modifications esili kosangisama, luká version ya sika ya répertoire na ngai:

```bash
git fetch upstream
```

Awa tozali koluka ba modifications nyonso na fork na ngai (upstream remote). Sikoyo, osengeli kosangisa version ya sika ya répertoire na ngai na branche main na yo:

```bash
git rebase upstream/main
```

Awa tozali kosalela ba modifications nyonso oyo ozwi na branche main. Soki opusi branche main sikoyo, fork na yo mpe ekozala na ba modifications:

```bash
git push origin main
```

Keba: Mbala oyo, ozali kopusa ba modifications na répertoire ya mosika oyo babengi origin.

Na ntango oyo nasangisi branche na yo `<add-kombo-na-yo>` na branche na ngai main, mpe osangisi branche na ngai main na branche na yo main. Branche na yo `<add-kombo-na-yo>` ezali lisusu na ntina te, yango wana okoki kolongola yango:

```bash
git branch -d <add-kombo-na-yo>
```

mpe okoki kolongola version na naye uta répertoire ya mosika mpe:

```bash
git push origin --delete <add-kombo-na-yo>
```

Oyo ezali ya ntina te, kasi kombo ya branche emonisi ete mokano nto objectif na yango ezali ya sikisiki nto polelepolele. Bomoi na yango ekoki kozala mokuse.

## Ba tutoriels mpo nakosalelá bisaleli nto baoutils mosusu

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md)                                                                                                                                        | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                                                          |

## Wapi kokende na nsima?

Soki olingi kopesa makabo na code, talá [dépôt na biso ya GitHub ya makabo nto contribution na code](https://github.com/roshanjossey/code-contributions).