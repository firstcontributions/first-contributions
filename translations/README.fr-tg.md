[![L'amour du logiciel libre](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Premières Contributions

Salut de là où vous me lisez aujourd'hui recevez mes salutations 🤗!
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
