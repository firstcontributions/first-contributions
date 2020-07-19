[![L'amour du logiciel libre](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Premières Contributions

C'est toujours compliqué la première fois que l'on fait quelque chose. La peur de faire des fautes n'est pas du tout confortable, spécialement quand vous collaborez. Mais le monde du logiciel libre est fait de collaboration et de travail de groupe. Aussi, nous voulons simplifier l'apprentissage des nouveaux contributeurs au logiciel libre en vous enseignant à contribuer pour la première fois.

Lire des articles et des tutoriels peut aider, mais qu'y a-t-il de mieux que d'essayer sans pouvoir faire d'erreurs ? Ce projet a pour ambition de fournir des conseils et simplifier la manière dont les apprentis font leur première contribution. Souvenez-vous : plus vous êtes serein, mieux vous apprenez. Si vous aspirez à faire votre première contribution, suivez tout simplement les étapes suivantes. Promis, ce sera amusant.

**Si vous n'êtes pas à l'aide avec la ligne de commande, [voici des tutoriels avec une interface graphique.](#tutoriels-en-utilisant-dautres-outils)**

<img align="right" width="300" src="../assets/fork.png" alt="embrancher ce repertoire" />

Si vous n'avez pas git sur votre ordinateur, [installez-le](https://help.github.com/articles/set-up-git/).

## Embranchez ce répertoire (aussi appelé un Fork)

Embranchez ce répertoire en cliquant sur le bouton de fork en haut de la page.
Cela va créer une copie du répertoire sur votre compte.

## Clonez ce répertoire

<img align="right" width="300" src="../assets/clone.png" alt="clonez ce répertoire" />

Maintenant, clonez ce répertoire sur votre ordinateur. Cliquez sur le bouton clone puis cliquez sur l'icone *copier dans le presse-papier*.

Ouvrez un invite de commande et exécutez les commandes git suivantes :

```sh
git clone "l'url que vous venez de copier"
```

où "l'url que vous venez de copier" (sans les guillemets) est l'url du répertoire. Voir la section précédente afin d'obtenir l'url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copier l'URL dans le presse-papier" />

Par exemple :

```sh
git clone https://github.com/votre-nom-d-utilisateur/first-contributions.git
```

où `votre-nom-d-utilisateur` est votre nom d'utilisateur GitHub. Ici vous êtes en train de copier le contenu du répertoire `first-contributions` depuis GitHub sur votre ordinateur.

## Créez une branche

Déplacez-vous dans le répertoire du projet nouvellement cloné (si vous n'y êtes pas encore) :

```sh
cd first-contributions
```

Maintenant créez une branche avec la commande `git checkout` :

```sh
git checkout -b <add-votre-nom>
```

Par exemple :

```sh
git checkout -b add-koffi-sani
```

(Le nom de la branche n'a pas besoin de contenir le terme *add*, mais c'est raisonnable de l'inclure parce que l'objectif de cette branche est d'ajouter votre nom à une liste.)

## Effectuez les modifications nécessaires et engagez-les

Maintenant, ouvrez le fichier [`Contributors.md`](../Contributors.md) dans un éditeur de texte, ajoutez-y votre nom. Ne l'ajoutez pas au début du fichier, ni à la fin. Mettez-le n'importe où au milieu. Maintenant enregistrez le fichier.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Si vous ouvrez l'invite de commande et vous exécutez la commande `git status`, vous verrez qu'il y a des modifications.

Ajoutez ces modifications à la branche que vous venez de créer avec la commande `git add` :

```sh
git add Contributors.md
```

Maintenant engagez ces modifications avec la commande `git commit`:

```sh
git commit -m "Add <votre-nom> to Contributors list"
```

en remplaçant `<votre-nom>` par votre nom.

## Poussez les modifications vers GitHub

Poussez vos modifications avec la commande `git push` :

```sh
git push origin <add-votre-nom>
```

en remplaçant `<add-votre-nom>` avec le nom de la branche précédemment créée.

## Soumettez vos changements pour révision

Si vous visitez votre répertoire sur Github, vous verrez un bouton `Compare & pull request`. Cliquez sur ce bouton.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Maintenant soumettez la demande de tirage.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Sous peu j'aurai fusionné toutes vos modifications avec la branche master de ce projet. Vous recevrez un mail de notification dès que la fusion sera effectuée.

La branche master de votre embranchement ne subira pas de modification à cet instant. Pour que votre embranchement soit synchronisé avec le mien, suivez les étapes suivantes.

## Gardez votre embranchement synchronisé avec ce répertoire

D'abord, basculez sur la branche master

```sh
git checkout master
```

Et ajoutez l'url de mon répertoire comme `upstream remote url` :

```sh
git remote add upstream https://github.com/Roshanjossey/first-contributions
```

Ceci est une manière de dire à git qu'une autre version de ce répertoire existe à l'adresse spécifiée et que nous l'appelons `upstream`. Une fois les modifications fusionnées, cherchez la nouvelle version de mon répertoire :

```sh
git fetch upstream
```

Ici nous cherchons toutes les modification dans mon embranchement (upstream remote). Maintenant, vous devez fusionner la nouvelle révision de mon répertoire avec votre branche master :

```sh
git rebase upstream/master
```

Ici nous appliquons toutes les modifications que vous avez cherché à la branche master. Si vous poussez la branche master maintenant, votre embranchement aussi aura les modifications :

```sh
git push origin master
```

Avertissement: Cette fois, vous poussez au répertoire distant appelé origin.

À ce niveau j'ai fusionné votre branche `<add-votre-nom>` avec ma branche master, et vous avez fusionné ma branche master avec votre branche master. Votre branche `<add-votre-nom>` n'est plus utile, donc vous pouvez la supprimer :

```sh
git branch -d <add-votre-nom>
```

et vous pouvez supprimer sa version dans le répertoire distant aussi :

```sh
git push origin --delete <add-votre-nom>
```

Ceci n'est pas nécessaire, mais le nom de la branche montre que son objectif est assez spécifique. Sa durée de vie peut être courte.

## Où aller ensuite ?

Félicitations ! Vous venez de suivre le flux de travail standard _embrancher -> cloner -> modifier -> soumettre_ que vous rencontrerez souvent en tant que contributeur-trice !

Célébrez votre contribution et partagez-la avec vos amis et vos followers en allant sur [notre site](https://firstcontributions.github.io/#social-share).

Vous pouvez aussi rejoindre notre équipe sur Slack au cas où vous auriez besoin d'aide ou auriez des questions. [Rejoindre l'équipe sur Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

À présent vous êtes prêt-e-s à contribuer à d'autres projets. Nous avons réuni des projets avec quelques issues simples auxquelles vous pourriez vous attaquer. Retrouvez [la liste des projets sur notre site](https://firstcontributions.github.io/#project-list).

## Tutoriels en utilisant d'autres outils

| <a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../github-desktop-tutorial.md)                                                                                          | [Visual Studio 2017](../github-windows-vs2017-tutorial.md)                                                                                                                       | [GitKraken](../gitkraken-tutorial.md)                                                             | [Visual Studio Code](../github-windows-vs-code-tutorial.md)                                                                                                               | [Atlassian Sourcetree](../sourcetree-macos-tutorial.md)                                                                                                                                   | [IntelliJ IDEA](../github-windows-intellij-tutorial.md)                                                                                                                |
