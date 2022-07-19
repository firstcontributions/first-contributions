# Stashing

What if you are working on a big code and suddenly you need to switch the branch from which you are currently working on to some other branch. Since the code, is not complete, and without any tests, you probably don't want to commit it. But you cannot move to the other branch without committing the changes, Git won't let you break this flow. What do we do then? How do we prevent an unnecessary commit, while being able to jump branches? This is what this tutorial covers.

## Stashing your work

Let's assume you are working on a project's branch where you have changed some files. Now if you run ```git status``` you can see your changes in the files.

```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

Now you want to switch your branch, but don't want to commit the changes yet; so you would stash the changes.
To push a new stash on to your stack, run ```git stash```:

```
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")
```

Now your working directory is clean, use ```git status``` :

```
$ git status
# On branch master
nothing to commit, working directory clean
```

Now you can switch to any branch and do your work; your stashed changes are stored in form of a stack. To see which stashes you have stored in the stack you can use ```git stash list```:

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

In case you want to re-apply the changes you just stashed, you can use the command ```git stash apply```. By using this command you can reapply the most recent stashed file. In order to reapply any other file, you can specify it by naming it like: ```git stash apply <stash-name>```, in place of ```<stash-name>``` write the name of the stash you need to reapply.

```
$ git stash apply
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   index.html
#      modified:   lib/simplegit.rb
#
```

You can see that git re-modifies the file that you uncommitted when you saved the stash. In this case, you had a clean working directory when you tried to apply the stash, and you tried to apply it on the same branch you saved it from; but having a clean working directory and applying it on the same branch aren’t necessary to successfully apply a stash. You can save a stash on one branch, switch to another branch later, and re-apply the changes in the new branch. You can also have modified and uncommitted files in your working directory when you apply a stash, git gives merge conflicts if anything no longer applies cleanly.

The changes made to your files are reapplied, but the file you staged was not restaged. To do so you need to run the command ```git stash apply``` with a ```--index``` to tell the command to reapply the staged changes. If you have run that instead, you would have returned to your original position:

```
$ git stash apply --index
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
```

The apply command only applies the stashed work, but you still have that on your stack. In order to remove it, you can run ```git stash drop``` with the name of the stash to remove.

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
```

You can use ```git stash pop``` to un-stash the last changes drop it from your stash's stack.

## Un-applying a Stash

In some cases you want to apply stashed changes, do some work, but up-apply the changes that originally came from the stash. Git does not provide command like ```git unapply```, but it is possible to achieve this effect by simply retrieving the patch associated with a stash and applying it in reverse:

```$ git stash show -p stash@{0} | git apply -R```

Again if you don't specify a stash, Git assumes the most recent stash:

```$ git stash show -p | git apply -R```

You may want to create an alias and effectively add a ```stash-unapply``` command to your Git. For example:

```
$ git config --global alias.stash-unapply '!git stash show -p | git apply -R'
$ git stash apply
$ #... work work work
$ git stash-unapply
```

## Creating a Branch from Stash

If you stash some work, leave it there for a while, and continue on the branch from which you stashed the work, you may have a problem reapplying the work. If the apply tries to modify a file that you’ve since modified, you’ll get a merge conflict and will have to resolve it. If you want an easier way to test the stashed changes again, you can run ```git stash branch```, which creates a new branch for you, checks out the commit you were on when you stashed your work, reapplies your work there, and then drops the stash if it applies successfully:

```
$ git stash branch testchanges
Switched to a new branch "testchanges"
# On branch testchanges
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
```

This is a nice shortcut to recover stashed work easily and work on it in a new branch.