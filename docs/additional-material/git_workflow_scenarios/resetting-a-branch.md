# Reset a branch

```reset``` is the command which can be used when we want to reset the repository with respect to a commit or a branch. A reset, as the name suggests, discards everything on the base(current) branch and makes it exactly same as the branch with which we chose to reset the base branch (calling it as origin branch). This essentially means, that we will have a copy of the origin branch with the name of base branch.<br/>
However, the question is, why don't we just delete the base branch and checkout a new branch with the name of base branch from origin branch. Technically, it will have the same effect as resetting but in some industrial situations we do not have the access to delete a branch, or we can not delete a branch as it will hamper/disrupt a CI/CD pipeline or maybe an ongoing workflow. Hence, to avoid such situations which can lead to downtimes, we suggest using `git reset` whenever we want to reset a particular branch.

## The Command

First, switch to the branch that you want to reset. Then reset it to the target branch:
```
git switch <base_branch>
git reset --hard <origin_branch>
```

An example could be:
```
git switch stage
git reset --hard master
```
The above commands switch to the `stage` branch and reset it to `master`, making `stage` exactly the same as `master`.
The `--hard` flag makes the working tree and staging area match the target branch. Any uncommitted changes will be discarded, so make sure you do not need them before running the command.
