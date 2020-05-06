# Undo local commits 

To undo a local commit, all you need to do is
```
git reset
```
This command will reset your staging area to your most recent commit, but the changes you made to your working directory will not change. So, you can still re-commit again what you've changed.
Or, if you only want to remove one file from your previous commit. Then, you can do the command below
```
git reset <file>
```
The command will remove only the specified file from the staging area, but changes made on the file will still remain.

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
# Edit crazy.php file again and changed a lot other files
# Commit all tracked files
$ git add .
$ git commit -m "Continued dev"
# Tested and things went out of hand
# Decided to remove the whole things
$ git reset --hard HEAD~2
```
The ```git reset --hard HEAD~2``` moves the current branch backward by 2 commit points in the same time reverting all changes you have made and remove the 2 snapshot we have just created from project history.

P.s. Never perform ```git reset --hard``` if you've already pushed your commits to a shared repository as it will cause problems to everyone on that repository.
