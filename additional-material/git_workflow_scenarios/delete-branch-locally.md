#Deleting a locally created Branch

This will be handy when you accidentally misspelled a branch name.

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

The -d option will delete the branch only if it has already been pushed and merged with the remote branch. Use -D instead if you want to force the branch to be deleted, even if it hasn't been pushed or merged yet.

If you try to delete a branch that has unmerged changes, you’ll receive the following error message:

```
error: The branch 'branch_name' is not fully merged.
If you are sure you want to delete it, run 'git branch -D branch_name'.
```

# Deleting a branch REMOTELY

Here's the command to delete a branch remotely: 

```
git push <remote> --delete <branch>
```

You can also use this shorter command to delete a branch remotely:

```
 git push <remote> :<branch>
```

If you get the error below, it may mean that someone else has already deleted the branch.


```
error: unable to push to unqualified destination: remoteBranchName The destination refspec neither matches an existing ref on the remote nor begins with refs/, and we are unable to guess a prefix based on the source ref. error: failed to push some refs to 'git@repository_name'

```
