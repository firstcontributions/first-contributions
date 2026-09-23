# Undo local commits

## Undo the latest local commit while keeping your changes

If you have not pushed your latest commit and want to redo it, run:

```sh
git reset --soft HEAD~1
```

This moves the current branch back one commit and keeps your changes staged, ready to edit or commit again. `HEAD~1` means the parent of the current commit, so this command requires at least two commits on the branch.

If you also want to unstage the changes, use `git reset --mixed HEAD~1` instead. Your files on disk remain unchanged with either option.

If you have already pushed the commit to a shared branch, see [Reverting a commit](reverting-a-commit.md) to undo it with a new commit without rewriting shared history.

## Unstage changes without undoing a commit

To unstage all staged changes, run:

```sh
git reset
```

This resets your staging area to your most recent commit without moving the branch or changing your files on disk. It does not undo a commit.

To unstage only one file, run the following command, replacing `<file>` with its path:

```sh
git reset -- <file>
```

This unstages changes to the specified file while keeping those changes on disk. It does not remove the file from an existing commit.

Example of ```git reset``` usage
```
# Make changes in index.php and tutorial.php
# Add files into the staging area
$ git add .
# Remembered both files need to be committed separately
# Unstage tutorial.php
$ git reset tutorial.php
# Commit index.php first
$ git commit -m "Changed index.php"
# Commit tutorial.php now
$ git add tutorial.php
$ git commit -m "Changed tutorial.php"
```

## Discard uncommitted changes to tracked files

Let's say if you have messed up your local repository and you just want to reset it to your last commit.
Then, you can run the command below.
```
git reset --hard
```
The command will not only reset your staging area, but also revert all your changes on the files to your last commit.
The mode ```--hard``` tells Git to undo all the changes in the working directory too.
You should only run this when you are really sure of throwing your whole local development out.

Example of ```git reset --hard``` usage
```
# Decided to start a crazy experiment
# Create a new file 'crazy.php' and add some code to it
# Commit crazy.php
$ git add crazy.php
$ git commit -m "Started a crazy dev"
# Edit crazy.php file again and changed a lot of other files
# Commit all tracked files
$ git add .
$ git commit -m "Continued dev"
# Tested and things went out of hand
# Decided to remove the whole things
$ git reset --hard HEAD~2
```
The ```git reset --hard HEAD~2``` moves the current branch backward by 2 commit points at the same time reverting all changes you have made and remove the 2 snapshots we have just created from project history.

P.s. Never perform ```git reset --hard``` if you've already pushed your commits to a shared repository as it will cause problems to everyone on that repository.
