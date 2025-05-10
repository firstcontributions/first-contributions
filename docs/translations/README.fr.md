[![L'amour du logiciel libre](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Premières Contributions

C'est toujours compliqué la première fois que l'on fait quelque chose. La peur de faire des fautes n'est pas du tout confortable, spécialement quand vous collaborez. Mais le monde du logiciel libre est le fait de collaborer et de travailler en groupe. Aussi, nous voulons simplifier l'apprentissage des nouveaux contributeurs au logiciel libre en vous enseignant à contribuer pour la première fois.

Lire des articles et des tutoriels peut aider, mais qu'y a-t-il de mieux que d'essayer sans pouvoir faire d'erreurs ? Ce projet a pour ambition de fournir des conseils et simplifier la manière dont les apprentis font leur première contribution. Souvenez-vous : plus vous êtes serein, mieux vous apprenez. Si vous aspirez à faire votre première contribution, suivez tout simplement les étapes suivantes. Promis, ce sera amusant.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="forker ce repertoire" />

Si vous n'avez pas encore Git installé sur votre machine, [ installez-le ]( https://help.github.com/articles/set-up-git/ ).

## Faire un fork de ce dépôt

Forkez ce dépôt en cliquant sur le bouton *fork* en haut de cette page.
Cela créera une copie de ce dépôt dans votre propre compte GitHub

## Clonez ce répertoire

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonez ce répertoire" />

Maintenant, clonez ce répertoire sur votre ordinateur. Allez sur votre compte GitHub, ouvrez le dépôt forké, cliquez sur le bouton *Code*, puis sur l’onglet *SSH* et enfin sur l’icône *copier dans le presse-papiers*.

Ouvrez une invite de commande (si vous êtes sous Windows) ou un terminal (si vous êtes sous MacOS ou Linux) et exécutez la commande git suivante :

```
git clone "l'url que vous venez de copier"
```
où "l'url que vous venez de copier" (sans les guillemets) est l'url du dépôt forké. Revoir les étapes précédentes pour obtenir l’URL exacte.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copier l'URL dans le presse-papier" />

Par exemple :
```
git clone https://github.com/votre-nom-d-utilisateur/first-contributions.git
```
où `votre-nom-d-utilisateur` est votre nom d'utilisateur GitHub. Ici vous êtes en train de copier le contenu du dépôt `first-contributions` depuis GitHub sur votre ordinateur.

## Créez une branche

Déplacez-vous dans le répertoire du projet nouvellement cloné (si vous n'y êtes pas encore) :

```
cd first-contributions
```
Maintenant créez une branche avec la commande `git checkout` :
```
git checkout -b <add-votre-nom>
```

Par exemple :
```
git checkout -b add-koffi-sani
```
(Le nom de la branche n'a pas besoin de contenir le terme *add*, mais il est mieux de l'inclure car l'objectif de cette branche est d'ajouter votre nom à une liste.)

<details> <summary> <strong>Si vous rencontrez une erreur avec git switch, cliquez ici :</strong> </summary>
Si le message "Git: switch is not a git command. See git –help" s’affiche, c’est probablement parce que vous utilisez une ancienne version de Git.

Dans ce cas, essayez plutôt :

```
git checkout -b nom-de-ta-nouvelle-branche
```
</details>

## Effectuez les modifications nécessaires et enregistrez-les

Ouvrez le fichier `Contributors.md` dans un éditeur de texte, ajoutez-y votre nom, et enregistrez-le. Ne l’ajoutez pas au début ou à la fin du fichier, mais quelque part au milieu.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Si vous ouvrez l'invite de commande et que vous exécutez la commande  `git status`, vous verrez qu'il y a des modifications. Ajoutez ces modifications à la branche que vous venez de créer avec la commande  `git add` :
```
git add Contributors.md
```

Maintenant faites un commit de ces modifications avec la commande `git commit`:
```
git commit -m "Add <votre-nom> to Contributors list"
```
en remplaçant `<votre-nom>` par votre nom.

## Envoyez les modifications vers GitHub

Poussez vos modifications avec la commande `git push` :
```
git push -u origin <nom-de-votre-branche>
```
en remplaçant `<nom-de-votre-branche>` avec le nom de la branche précédemment créée.

<details> <summary> <strong>Si tu obtiens une erreur au moment de pousser, clique ici :</strong> </summary>

- ### Erreur d’authentification
<pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead. remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information. fatal: Authentication failed for 'https://github.com/<ton-nom-utilisateur>/first-contributions.git/'</pre>
Suivez le tutoriel GitHub pour générer et configurer une clé SSH sur votre compte.

Vous pouvez également exécuter git remote -v pour vérifier votre adresse distante.

Si elle ressemble à ceci :

<pre>origin https://github.com/ton-nom-utilisateur/ton_repo.git (fetch) origin https://github.com/ton-nom-utilisateur/ton_repo.git (push)</pre>
Modifiez-la avec cette commande :

```
git remote set-url origin git@github.com:ton-nom-utilisateur/ton_repo.git
```
Sinon, vous continuerez de devoir entrer votre mot de passe et vous obtiendrez une erreur d’authentification.

</details>

## Soumettez votre contribution pour révision

Si vous vous rendez sur votre répertoire sur Github, vous verrez un bouton  `Compare & pull request`.  Cliquez dessus.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="créer une pull request" />

Soumettez ensuite la *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="soumettre une pull request" />

Je fusionnerai bientôt vos modifications dans la branche principale du projet.
Vous recevrez un e-mail de confirmation une fois que ce sera fait.

La branche main de votre dépôt forké ne subira pas de modification. Pour que votre dépôt soit synchronisé avec le mien, suivez les étapes suivantes.

## Gardez votre embranchement synchronisé avec ce répertoire

 D'abord, basculez sur la branche main
 ```
 git checkout main
 ```

 Et ajouter l'url de mon répertoire comme  `upstream remote url` :
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Ceci est une manière de dire à git qu'une autre version de ce répertoire existe à l'adresse spécifiée et que nous l'appelons  `upstream`. Une fois les modifications fusionnées, cherchez la nouvelle version de mon répertoire :
```
git fetch upstream
```

Ici nous cherchons toutes les modifications dans mon embranchement (upstream remote). Maintenant, vous devez fusionner la nouvelle révision de mon répertoire avec votre branche main :
```
git rebase upstream/main
```
Ici nous appliquons toutes les modifications que vous avez récupéré à la branche main. Si vous poussez la branche main maintenant, votre embranchement aussi aura les modifications :
```
git push origin main
```
Avertissement: Cette fois, vous poussez les modifications au répertoire distant appelé origin.

A cet instant j'ai fusionné votre branche  `<add-votre-nom>` avec ma branche main, et vous avez fusionné ma branche main avec votre branche main. Votre branche `<add-votre-nom>` n'est plus utile, donc vous pouvez la supprimer :
```
git branch -d <add-votre-nom>
```
et vous pouvez supprimer sa version dans le répertoire distant aussi :
```
git push origin --delete <add-votre-nom>
```
Ceci n'est pas nécessaire, mais le nom de la branche montre que son objectif est assez spécifique. Sa durée de vie peut être courte.

## Tutoriels en utilisant d'autres outils


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

## Où aller ensuite ?

Vous pouvez aussi rejoindre notre équipe sur Slack au cas où vous auriez besoin d'aide ou auriez des questions.  [Rejoindre l'équipe sur  Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
