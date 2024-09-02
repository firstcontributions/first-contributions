# Vérifier l'historique des commits

Pour vérifier l'historique des commits d'une branche ou d'un fichier, la commande suivante peut être utilisée :

git log [options] [path]

Par défaut, la sortie de cette commande est affichée dans l'ordre chronologique inverse.

## Variations et options de la commande
- Pour effectuer les commits accessibles à partir de certains identifiants de commit : <i>(Dans ce cas,`foo` et `bar`)</i><br>
    `git log foo bar` 
- Il est également possible de supprimer les commits accessibles à partir d'un identifiant de commit donné en ajoutant un `^` devant l'identifiant de commit: <i>(Dans ce cas, `baz`)</i><br>
    `git log foo bar ^baz`
- Historique des commits pour un fichier spécifique <br>
    `git log --all <nom_du_fichier>`
- Limiter le nombre de commits affichés dans l'historique : <i>(Dans ce cas, `5`)</i><br>
    `git log -n 5`

## Référence
- [Documentation officielle](https://git-scm.com/docs/git/fr)