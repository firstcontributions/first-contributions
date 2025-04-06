# Remove a branch from your repository

If you have followed the tutorial up-to-now, our `<branch-name>` branch has finished its purpose, it is time to delete it from your local machine's repo. This isn't necessary, but the name of this branch shows its rather special purpose. Its life can be made correspondingly short.

First, let's merge your `<branch-name>` to your master, so to go to your master branch:
```
git checkout master (if this command fails, replace 'master' with 'main')
```

Merge `<branch-name>` to master:
```
git merge <branch-name> master (#if this command fails, replace 'master' with 'main')
```

Remove `<branch-name>` on your local machine's repo:
```
git branch -d <branch-name>
```

You have now deleted your local machine's `<branch-name>` branch and everything looks neat and tidy.
Though, at this point, you should still have the `<branch-name>` branch in your GitHub fork. However, before you delete this, remember that you have sent a "Pull request" to my repo from this remote branch. So unless I've already merged it, don't delete this branch.

However, if I have merged your branch and you want to delete the remote branch, use:
```
git push origin --delete <branch-name>
```

Now, you know how to tidy your branches.
With time, many commits will be added to my public repo. And the master branches of your local machine and of your GitHub fork won't be up-to-date. So in order to keep your repositories synchronized with mine, follow the steps below.

#### [Keeping your fork synced with the repository](keeping-your-fork-synced-with-this-repository.md)
