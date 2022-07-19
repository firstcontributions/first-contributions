# Undo local commits 

To undo local commits we can use git's ```reset``` and ```revert``` commands.

## Reset vs Revert
At first glance, resetting might seem coincidentally close to reverting, but they are actually quite different. Reverting creates a new commit that reverts or undos a previous commit. Resetting, on the other hand, erases commits!

## What Is A Revert?
When you tell Git to revert a specific commit, Git takes the changes that were made in commit and does the exact opposite of them. Let's break that down a bit. If a character is added in commit A, if Git reverts commit A, then Git will make a new commit where that character is deleted. It also works the other way where if a character/line is removed, then reverting that commit will add that content back!

## The ```git revert``` Command

Now that I've made a commit with some changes, I can revert it with the ```git revert``` command

```git revert <SHA-of-commit-to-revert>```

where ```<SHA>``` is the commit code like the one given below => ```db7e87a```.
  
**Example:** ```git revert db7e87a``` will undo the changes made in the commit ```db7e87a```.

## The ```git reset``` command

⚠️ Resetting Is Dangerous ⚠️

> You've got to be careful with Git's resetting capabilities. This is one of the few commands that lets you erase commits from the repository. If a commit is no longer in the    > repository, then its content is gone.

> To alleviate the stress a bit, Git does keep track of everything for about 30 days before it completely erases anything. To access this content, you'll need to use the 
> ```git reflog``` command. Check out these links for more info:

> * [git-reflog](https://git-scm.com/docs/git-reflog)
> * [Rewriting History](https://www.atlassian.com/git/tutorials/rewriting-history)
> * [reflog, your safety net](http://gitready.com/intermediate/2009/02/09/reflog-your-safety-net.html)

The ```git reset``` command is used to reset (erase) commits:

```git reset <reference-to-commit>```

It can be used to:
* move the HEAD and current branch pointer to the referenced commit
* erase commits
* move committed changes to the staging index
* unstage committed changes

## Git Reset's Flags
The way that Git determines if it erases, stages previously committed changes, or unstages previously committed changes is by the flag that's used. The flags are:

* ```--mixed```
* ```--soft```
* ```--hard```

It's easier to understand how they work with a little animation.

**Click on this [link](https://youtu.be/UN7ki2G2yKc) to view the animation.**

## Reset's ```--mixed``` Flag
Let's look at each one of these flags.

>  9ec05ca (HEAD -> master) Revert "Set page heading to "Quests & Crusades""

>  db7e87a Set page heading to "Quests & Crusades"

>  796ddb0 Merge branch 'heading-update'

Using the sample repo above with ```HEAD``` pointing to ```master``` on commit ```9ec05ca```, running ```git reset --mixed HEAD^``` will take the changes made in commit ```9ec05ca``` and move them to the working directory.

## Reset's ```--soft``` Flag
Let's use the same few commits and look at how the  ```--soft``` flag works:

> 9ec05ca (HEAD -> master) Revert "Set page heading to "Quests & Crusades""

> db7e87a Set page heading to "Quests & Crusades"

> 796ddb0 Merge branch 'heading-update'

Running ```git reset --soft HEAD^``` will take the changes made in commit ```9ec05ca``` and move them directly to the Staging Index.

## Reset's ```--hard``` Flag
Last but not least, let's look at the ```--hard``` flag:

> 9ec05ca (HEAD -> master) Revert "Set page heading to "Quests & Crusades""

> db7e87a Set page heading to "Quests & Crusades"

> 796ddb0 Merge branch 'heading-update'

Running ```git reset --hard HEAD^``` will take the changes made in commit ```9ec05ca``` and erases them.
You should only run this when you are really sure of throwing the changes.
