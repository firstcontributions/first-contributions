[![L'amour du logiciel libre](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Premières Contributions

C'est toujours compliqué la première fois que l'on fait quelque chose. La peur de faire des fautes n'est pas du tout confortable, spécialement quand vous collaborez. Mais le monde du logiciel libre est le fait de collaborer et de travailler en groupe. Aussi, nous voulons simplifier l'apprentissage des nouveaux contributeurs au logiciel libre en vous enseignant à contribuer pour la première fois.  

Lire des articles et des tutoriels peut aider, mais qu'y a-t-il de mieux que d'essayer sans pouvoir faire d'erreurs ? Ce projet a pour ambition de fournir des conseils et simplifier la manière dont les apprentis font leur première contribution. Souvenez-vous : plus vous êtes serein, mieux vous apprenez. Si vous aspirez à faire votre première contribution, suivez tout simplement les étapes suivantes. Promis, ce sera amusant.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="embrancher ce repertoire" />

Si vous n'avez pas git sur votre ordinateur, [ installez-le ]( https://help.github.com/articles/set-up-git/ ).

## Embranchez ce répertoire (aussi appelé un Fork)

Embranchez ce répertoire en cliquant sur le bouton de fork en haut de la page.
Cela va créer une copie du répertoire sur votre compte.

## Clonez ce répertoire

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonez ce répertoire" />

Maintenant, clonez ce répertoire sur votre ordinateur. Cliquez sur le bouton clone puis cliquez sur l'icône *copier dans le presse-papier*.

Ouvrez une invite de commande (si vous êtes sous Windows) ou un terminal (si vous êtes sous MacOS ou Linux) et exécutez les commandes git suivantes :

```
git clone "l'url que vous venez de copier"
```
où "l'url que vous venez de copier" (sans les guillemets) est l'url du répertoire. Voir la section précédente afin d'obtenir l'url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copier l'URL dans le presse-papier" />

Par exemple :
```
git clone https://github.com/votre-nom-d-utilisateur/first-contributions.git
```
où `votre-nom-d-utilisateur` est votre nom d'utilisateur GitHub. Ici vous êtes en train de copier le contenu du répertoire `first-contributions` depuis GitHub sur votre ordinateur.

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
(Le nom de la branche n'a pas besoin de contenir le terme *add*, mais c'est raisonnable de l'inclure parce que l'objectif de cette branche est d'ajouter votre nom à une liste.)

## Effectuez les modifications nécessaires et engagez-les

Maintenant, ouvrez le fichier `Contributors.md` dans un éditeur de texte, ajoutez-y votre nom, et enregistrez-le. Si vous ouvrez l'invite de commande et vous exécutez la commande  `git status`, vous verrez qu'il y a des modifications. Ajoutez ces modifications à la branche que vous venez de créer avec la commande  `git add` :
```
git add Contributors.md
```

Maintenant engagez ces modifications avec la commande `git commit`:
```
git commit -m "Add <votre-nom> to Contributors list"
```
en remplaçant `<votre-nom>` par votre nom.

## Poussez les modifications vers GitHub

Poussez vos modifications avec la commande `git push` :
```
git push origin <add-votre-nom>
```
en remplaçant `<add-votre-nom>` avec le nom de la branche précédemment créée.

## Soumettez vos changements pour révision

Si vous visitez votre répertoire sur Github, vous verrez un bouton  `Compare & pull request`.  Cliquez sur ce bouton.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Maintenant soumettez la demande de tirage.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Sous peu j'aurai fusionné toutes vos modifications avec la branche main de ce projet. Vous recevrez un mail de notification dès que la fusion sera effectuée.

La branche main de votre embranchement ne subira pas de modification à cet instant. Pour que votre embranchement soit synchronisé avec le mien, suivez les étapes suivantes.

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
Ici nous appliquons toutes les modifications que vous avez cherché à la branche main. Si vous poussez la branche main maintenant, votre embranchement aussi aura les modifications :
```
git push origin main
```
Avertissement: Cette fois, vous poussez au répertoire distant appelé origin.

A ce niveau j'ai fusionné votre branche  `<add-votre-nom>` avec ma branche main, et vous avez fusionné ma branche main avec votre branche main. Votre branche `<add-votre-nom>` n'est plus utile, donc vous pouvez la supprimer :
```
git branch -d <add-votre-nom>
```
et vous pouvez supprimer sa version dans le répertoire distant aussi :
```
git push origin --delete <add-votre-nom>
```
Ceci n'est pas nécessaire, mais le nom de la branche montre que son objectif est assez spécifique. Sa durée de vie peut être courte.

## Tutoriels en utilisant d'autres outils


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

## Où aller ensuite ?

Vous pouvez aussi rejoindre notre équipe sur Slack au cas où vous auriez besoin d'aide ou auriez des questions.  [Rejoindre l'équipe sur  Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

