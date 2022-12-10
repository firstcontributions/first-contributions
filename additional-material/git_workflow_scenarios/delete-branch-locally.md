# Deleting a locally created Branch

<<<<<<< HEAD
This will be handy when you accidentally misspelled a branch name.
=======
This will be handy when you accidently misspelled a branch name.
>>>>>>> deffbe2881f842fe35d5a167069d46f956b6aab5

This can be done in *3* ways

```
git branch -D <branch_name>
```

```
git branch --delete --force <branch_name>  # Same as -D
```

```
git branch --delete  <branch_name>         # Error on unmerge
```

<<<<<<< HEAD
-D stands for --delete --force which will delete the branch even it's not merged (force delete), but you can also use -d which stands for --delete which throws an error respective of the branch merge status...
=======
-D stands for --delete --force which will delete the branch even it's not merged (force delete), but you can also use -d which stands for --delete which throw an error respective of the branch merge status...
>>>>>>> deffbe2881f842fe35d5a167069d46f956b6aab5
