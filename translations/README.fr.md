[![L'amour du logiciel libre](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![Licence: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Contributeurs Open Source](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Premières Contributions

C'est toujours compliqué la première fois que l'on fait quelque chose. La peur de faire des fautes n'est pas du tout confortable, particulièrement quand vous collaborez. Mais le monde du logiciel libre est fait de collaborations et de travaux de groupe. Aussi, nous voulons simplifier l'apprentissage des nouveaux contributeurs et nouvelles contributrices au logiciel libre en vous enseignant à contribuer pour la première fois.  

Lire des articles et des tutoriels peut aider, mais qu'y a-t-il de mieux que d'essayer sans pouvoir faire d'erreurs ? Ce projet a pour ambition de fournir des conseils et simplifier la manière dont les apprentis font leur première contribution. Souvenez-vous : plus vous êtes serein·e, mieux vous apprenez. Si vous aspirez à faire votre première contribution, suivez tout simplement les étapes suivantes. Promis, ce sera amusant.

<img align="right" width="300" src="../assets/fork.png" alt="embrancher ce repertoire" />

Si vous n'avez pas git sur votre ordinateur, [ installez-le ]( https://help.github.com/articles/set-up-git/ ).

## Embranchez ce répertoire (aussi appelé un Fork)

Embranchez ce répertoire en cliquant sur le bouton de fork en haut de la page.
Cela va créer une copie du répertoire sur votre compte.

## Clonez ce répertoire

<img align="right" width="300" src="../assets/clone.png" alt="clonez ce répertoire" />

Maintenant, clonez ce répertoire sur votre ordinateur. Cliquez sur le bouton clone puis cliquez sur l'icone *copier dans le presse-papier*.

Ouvrez un invite de commande et exécutez la commande git suivante :

```
git clone "l'url que vous venez de copier"
```
où "l'url que vous venez de copier" (sans les guillemets) est l'url du répertoire. Voir la section précédente afin d'obtenir l'url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copier l'URL dans le presse-papier" />

Par exemple :
```
git clone https://github.com/votre-pseudo/first-contributions.git
```
où `votre-pseudo` est votre nom d'utilisateur ou utilisatrice GitHub. Ici vous êtes en train de copier le contenu du répertoire `first-contributions` depuis GitHub sur votre ordinateur.

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
(Le nom de la branche n'a pas besoin de contenir le terme *add* ("*ajouter*" en anglais), mais c'est raisonnable de l'inclure parce que l'objectif de cette branche est d'ajouter votre nom à une liste.)

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
en remplaçant `<add-votre-nom>` par le nom de la branche précédemment créée.

## Soumettez vos changements pour révision

Si vous visitez votre répertoire sur GitHub, vous verrez un bouton  `Compare & pull request`.  Cliquez sur ce bouton.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="créez une nouvelle demande de triage" />

Maintenant soumettez la demande de tirage.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="soumettez la demande de triage" />

Sous peu, j'aurai fusionné toutes vos modifications avec la branche master de ce projet. Vous recevrez un mail de notification dès que la fusion sera effectuée.

La branche master de votre embranchement ne subira pas de modification à cet instant. Pour que votre embranchement soit synchronisé avec le mien, suivez les étapes suivantes.

## Tutoriels en utilisant d'autres outils


|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|

## Et maintenant ?

Félicitaions ! Vous venez de terminer le flux classique *embranchement -> clone -> modifications -> triage* que vous rencontrerez souvent en tant que contributeur ou contributrice !

Célébrez votre contribution et partagez-la avec vos amis et votre réseau sur [l'application web](https://roshanjossey.github.io/first-contributions/#social-share).

Vous pouvez aussi rejoindre notre équipe sur Slack au cas où vous auriez besoin d'aide ou auriez des questions.  [Rejoindre l'équipe sur  Slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)

Pour vous aider à vous lancez dans vos premières contributions, nous avons établi une liste de projets avec des problématiques faciles qur lesquelles vous pouvez vous lancer. Consultez la liste dans [l'application web](https://roshanjossey.github.io/first-contributions/#project-list).


### [Informations complémentaires](additional-material/git_workflow_scenarios/additional-material.md)


## Didacticiels utilisant d'autres outils

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

## Auto-Promotion

Si vous avez apprécié ce projet, ajoutez-lui une étoile sur [GitHub](https://github.com/Roshanjossey/first-contributions).
Si vous vous sentez particulièrement généreu·x·se, suivez [Roshan](https://roshanjossey.github.io/) sur
[Twitter](https://twitter.com/sudo__bangbang) et
[GitHub](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="https://app.saasgrids.com" src="assets/saasgrids-banner.png" width="500"></a>
