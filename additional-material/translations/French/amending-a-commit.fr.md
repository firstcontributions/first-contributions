# Modifier un commit

Imaginons que vous avez effectué un commit sur votre répertoire distant et que vous vous rendez compte plus tard qu'il
y a une coquille dans le message de commit ou que vous avez oublié d'ajouter une ligne dans votre tout dernier commit.
Comment faire pour rectifier cette erreur ? C'est le sujet de ce tutoriel.

## Changer un message de commit récent après l'avoir poussé sur Github
Pour se faire sans même ouvrir un fichier :
*   Taper la commande ```git commit --amend -m "suivi de votre nouveau message de commit"```
*   Lancer la commande ```git push origin <nom-de-la-branche>``` pour effectuer un commit vers le répertoire.

NB : Si vous tapez uniquement ```git commit --amend```, l'éditeur de texte s'ouvre et vous demande de modifier le
message de commit. Ajoutez l'option ``-m`` pour éviter de passer par l'éditeur de texte.

## Modifier un commit précis

Donc, qu'est-ce qu'il se passe si vous oubliez de faire un changement mineur sur un fichier, comme changer un mot et
que vous avez déjà poussé ce commit vers notre répertoire distant ?

Pour illustrer ce propos, voici un log de mes commits ;
```
g56123f création d'un fichier bot
a2235d mise à jour de contributeur.md
a5da0d modification du fichier bot
```
Imaginons que j'ai oublié d'ajouter un mot dans le fichier bot.

Il y a deux façons de régler ce problème. Le premier est de faire un nouveau commit qui contient le changement comme ceci :
```
g56123f création d'un fichier bot
a2235d mise à jour de contributeur.md
a5da0d modification du fichier bot
b0ca8f ajout d'un mot dans le fichier bot
```
La seconde façon est de modifier le commit a5da0d et d'ajouter ce nouveau mot puis le pousser sur Github le tout dans un seul commit.
Cette deuxième option semble plus adaptée, étant donné qu'il s'agit d'un changement mineur.

Pour se faire, il faut suivre les étapes suivantes :
*   Modifier le fichier. Dans notre cas, on modifie le fichier bot pour y inclure le mot oublié.
*   Ensuite, ajouter le fichier dans la zone de transit avec la commande ```git add <nom-du-fichier>```

D'habitude, après avoir ajouté des fichiers dans la zone de transit, l'étape suivante est d'exécuter la commande 
git commit -m "notre message de commit", n'est-ce pas ? Mais comme ce qu'on veut ici c'est modifier le commit
précédent, on va plutôt lancer les commandes :

* ```git commit --amend```
 Cela va faire apparaître l'éditeur de texte qui vous demande de modifier le message. Vous pouvez décider de laisser le
 message tel quel ou bien le changer.
* Quitter l'éditeur
* Pousser vos changements avec la commande ```git push origin <nom-de-la-branche>```

De cette façon, les deux changements se trouvent dans un même commit.
