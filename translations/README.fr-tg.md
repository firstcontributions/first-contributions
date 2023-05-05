[![L'amour du logiciel libre](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Premières Contributions

Salut de là où vous me lisez aujourd'hui, recevez mes salutations 🤗!
C'est un peu étonnant hein, moi qui suis entrain de faire ma prémière contribution pour la deuxième pour être dans le bain, je suis entrain de vous écrire ceci, c'est-à-dire les étape pour un apprenti/débutant à faire une contribution sur GitHub. Ce n'est toujours pas évident de faire une chose la prémière fois (de vous à moi, soyons honnête 😂), et dire que c'est avec GitHub et ces commandes, de plus sur une collaboration avec une équipe (non mais c'est la cata quoi), on a peur qu'un push pourrait écraser le fichier de l'autre et tout, en faisant un pull, peur des conflits, dois-je faire rebase ou merge, 😔 ahhh 😭 tellement on a peur.

Alors, san panique, le monde du logiciel libre est la clé du succès, c'est là où on apprend, on grandi ensemble, on apporte des idées et on collabore pour la pousser plus loin ; ici nous allons apprendre comment contribuer sur un projet pour la première fois, tout commence toujours quelque part. L'objectif de ce projet est de simplifier et guider la manière dont les débutants apportent leur première contribution. Si vous souhaitez apporter votre première contribution, suivez les étapes ci-dessous et ayez le fun en le faisant 🚀.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="embrancher ce repertoire" />

Si vous n'avez pas git sur votre ordinateur, [installez-le]( https://help.github.com/articles/set-up-git/ ).

## Faire une copie de ce répertoire (Faire un fork du dépôt sous son username)

Forker ce répertoire en cliquant sur le bouton de fork en haut de la page.
Cela va créer une copie du répertoire sur votre compte.

## Clonez ce répertoire

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonez ce répertoire" />

Maintenant, clonez ce répertoire sur votre ordinateur. Cliquez sur le bouton clone puis cliquez sur l'icone *copier dans le presse-papier*.

Ouvrez un invite de commande et exécutez les commandes git suivantes :

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
Maintenant créez une branche avec le commande `git checkout` :
```

git checkout -b <add-votre-nom>
```

Par exemple :
```
git checkout -b add-geoffreylgv
```
(Ici c'est un exemple de commande, l'objectif est de créer une branche avec votre nom utilisateur, ceci dit, vous n'êtes pas obligé de mettre le *add* préfixant le nom utilisateur)

## Apporter les modifications nécessaires et les valider

Ouvrez maintenant le fichier `Contributors.md` dans un éditeur de texte et ajoutez-y votre nom. Ne l'ajoutez pas au début ou à la fin du fichier. Mettez-le n'importe où entre les deux. Enregistrez le fichier.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Si vous allez dans le répertoire du projet et que vous exécutez la commande `git status`, vous verrez qu'il y a des changements.

Ajoutez ces changements à la branche que vous venez de créer en utilisant la commande `git add` :

```
git add Contributors.md
```

Validez ensuite ces modifications à l'aide de la commande `git commit`:
```
git commit -m "Add <votre-nom> to Contributors list"
```

en remplaçant `<votre-nom>` par votre nom.

## Transférez vos modifications vers GitHub

Transférez vos modifications à l'aide de la commande `git push` :

```
git push origin <add-votre-nom>
```

en remplaçant `<add-votre-nom>` avec le nom de la branche précédemment créée.

## Soumettre vos modifications pour révision (revue de code)

Si vous allez sur votre dépôt sur Github, vous verrez un bouton  `Compare & pull request`.  Cliquez sur ce bouton.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Maintenant soumettez la demande de tirage (pull request).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Sous peu, je fusionnerai tous vos changements dans la branche principale de ce projet. Vous recevrez un email de notification une fois que les changements auront été fusionnés.

ℹ️ NB : Il est toujours possible de mettre à jours votre dépôt avec ce dépôt principal, pour celà, il faut faire un pull de ce dépôt

## Rester à jour avec votre dépôt et ce dépôt GitHub

Sur GitHub, naviguez jusqu'à la page principale du dépôt forké que vous souhaitez synchroniser(en occurence, votre dépôt) avec ce dépôt. Sélectionnez la liste déroulante Fetch upstream, cliquez sur le bouton 'Fetch and merge' ou bien 'Sync fork' puis c'est bon 😉.

## Tutoriels en utilisant d'autres outils


| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |

## Où aller ensuite ?

Vous pouvez aussi rejoindre notre équipe sur Slack au cas où vous auriez besoin d'aide ou auriez des questions.  [Rejoindre l'équipe sur  Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)

