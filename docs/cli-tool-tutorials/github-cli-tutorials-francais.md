

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Premières Contributions

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | Interface en Ligne de Commande GitHub (CLI) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|

Ceci est un guide pour nous, les adeptes du terminal, qui veulent tout faire en ligne de commande. Grâce à [Github-CLI](https://cli.github.com/), nous pouvons y parvenir. Votre première contribution devrait être amusante, gratifiante et motivante pour continuer à progresser !

Ce guide est un peu plus complexe, car nous n'utilisons aucune interface graphique, mais c'est toujours très amusant et vous pouvez suivre les instructions !

Le premier prérequis est d'avoir :
- Git installé (comment installer [git](https://git-scm.com/downloads))
- Un compte GitHub

Ensuite, nous devons installer l'outil `github-cli` sur notre système en suivant la [documentation officielle](https://github.com/cli/cli#installation).

Après cela, nous devons nous connecter à la CLI en entrant cette commande : 
```bash 
gh auth login
```

Suivez les instructions et vous êtes prêt(e) !

# Fork de ce dépôt
C'est aussi simple que d'exécuter cette commande :

```bash
gh repo fork firstcontributions/first-contributions
```
**Important : Il vous demandera si vous souhaitez également le cloner, sélectionnez l'option "yes"**

# Créer votre branche
Nous allons effectuer cette étape avec Git, alors entrez cette commande en remplaçant le nom par votre nom, par exemple :
```bash 
git switch -c add-john-doe
```

# Effectuer les changements nécessaires et commitez ces modifications 
Vous pouvez maintenant ouvrir le fichier `Contributors.md` dans un éditeur de texte et y ajouter votre nom. Placez votre nom n'importe où entre le début et la fin du fichier, puis enregistrez-le.

Dans le répertoire du projet, exécutez `git status` et vous verrez les modifications.
![image-git](https://camo.githubusercontent.com/a35c4722d7aab337eefc655d1488f7b4dc038508e6adaf5e88e2e052a976f010/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

Ajoutez ces changements à la branche que vous venez de créer en utilisant la commande `git add` :
`git add Contributors.md`

Commitez maintenant ces changements en utilisant la commande `git commit` :
`git commit -m "Ajouter votre-nom à la liste des contributeurs"`
en remplaçant `votre-nom` par votre nom.

# Envoyez les modifications sur GitHub 
Envoyez vos modifications en utilisant la commande `git push` :

```
git push origin -u votre-nom-de-branche
```

en remplaçant `votre-nom-de-branche` par le nom de la branche que vous avez créée précédemment.

<details>
<summary> <strong>Si vous obtenez des erreurs lors de la soumission, cliquez ici :</strong> </summary>

- ### Erreur d'authentification
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<votre-nom-d'utilisateur>/first-contributions.git/'</pre>
  Suivez le [tutoriel GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) sur la génération et la configuration d'une clé SSH pour votre compte.

</details>

# Soumettez vos modifications pour examen
Maintenant, en exécutant cette commande dans le répertoire de notre dépôt, vous pourrez créer une pull request pour examen :

```bash 
gh pr create --repo firstcontributions/first-contributions
```

Ensuite, soumettez la pull request.

Vous pouvez utiliser la commande `gh status` pour voir votre pull request mentionnée en action.

## Où aller à partir de maintenant ?

Félicitations ! Vous venez de terminer le flux de travail standard _fork -> clone -> édition -> pull request_ que vous rencontrerez souvent en tant que contributeur !

Célébrez votre contribution et partagez-la avec vos amis et abonnés en allant sur [l'application web](https://firstcontributions.github.io/#social-share).

Vous pouvez rejoindre notre équipe Slack si vous avez besoin d'aide ou si vous avez des questions. [Rejoignez l'équipe Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-vchl8cde-S0KstI_jyCcGEEj7rSTQiA).

Maintenant, passons à la contribution à d'autres projets. Nous avons dressé une liste de projets avec des problèmes faciles pour vous permettre de commencer. Consultez [la liste des projets sur l'application web](https://firstcontributions.github.io/#project-list).

### [Matériel supplémentaire](additional-material/git_workflow_scenarios/additional-material.md)

## Tutoriels Utilisant d'Autres Outils

[Retour à la page d'accueil](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)