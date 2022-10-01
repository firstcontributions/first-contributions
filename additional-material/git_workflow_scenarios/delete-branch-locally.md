# Deleting a locally created Branch

This will be handy when you accidently misspelled a branch name.

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

-D stands for --delete --force which will delete the branch even it's not merged (force delete), but you can also use -d which stands for --delete which throw an error respective of the branch merge status...