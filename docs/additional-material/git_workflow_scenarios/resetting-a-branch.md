# Reset a branch

```reset``` is the command which can be used when we want to reset the repository with respect to a commit or a branch. A reset, as the name suggests, discards everything on the base(current) branch and makes it exactly same as the branch with which we chose to reset the base branch (calling it as origin branch). This essentially means, that we will have a copy of the origin branch with the name of base branch.<br/>
However, the question is, why don't we just delete the base branch and checkout a new branch with the name of base branch from origin branch. Technically, it will have the same effect as resetting but in some industrial situations we do not have the access to delete a branch, or we can not delete a branch as it will hamper/disrupt a CI/CD pipeline or maybe an ongoing workflow. Hence, to avoid such situations which can lead to downtimes, we suggest using `git reset` whenever we want to reset a particular branch.

## The Command

`git reset` always acts on the branch that is currently checked out (HEAD), so you cannot pass two branch names to it. To reset a branch with respect to another one, first switch to the branch you want to reset (the base branch), then reset it to the target branch (calling it the origin branch):
```
git switch <base_branch>
git reset --hard <origin_branch>
```

An example could be:
```
git switch stage
git reset --hard master
```
The above commands will reset the `stage` branch to `master` and therefore make `stage` exactly same as `master`.
You must be wondering about why `--hard` flag is used? This is to ignore all the changes which are or will be staged before/after the reset.
