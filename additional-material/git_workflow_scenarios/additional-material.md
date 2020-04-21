# Additional information

We assume that you have already finished with the basic tutorial before coming here. This document will give you some additional information about advanced Git techniques.

### [Amending a commit](amending-a-commit.md)
This document provides information about how to amend a commit on the remote repository.
> Use this when you need to adjust a commit you made.

### [Configuring git](configuring-git.md)
This document provides information about how to configure user details and other options in git.
> Use this to better control your git configurations.

### [Keeping your fork synced with the repository](keeping-your-fork-synced-with-this-repository.md)
This document provides information about how to keep your forked repository up-to-date with the base repository. This is important, as hopefully you and many others will contribute to the project.
> Follow these steps if your fork doesn't have any changes in parent repository.

### [Moving a Commit to a different Branch](moving-a-commit-to-a-different-branch.md)
This document provides information about how to move a Commit to another Branch.
> Moving to an existing branch
If you want to move your commits to an existing branch:

git checkout existingbranch
git merge master         # Bring the commits here
git checkout master
git reset --keep HEAD~3  # Move master back by 3 commits.
git checkout existingbranch
The --keep option preserves any uncommitted changes that you might have in unrelated files, or aborts if those changes would have to be overwritten -- similarly to what git checkout does. If it aborts, git stash your changes and retry, or use --hard to lose the changes (even from files that didn't change between the commits!)

Moving to a new branch
This method works by creating a new branch with the first command (git branch newbranch) but not switching to it. Then we roll back the current branch (master) and switch to the new branch to continue working.

git branch newbranch      # Create a new branch, containing all current commits
git reset --keep HEAD~3   # Move master back by 3 commits (Make sure you know how many commits you need to go back)
git checkout newbranch    # Go to the new branch that still has the desired commits

But  make sure how many commits to go back. Alternatively, instead of HEAD~3, you can simply provide the hash of the commit (or the reference like origin/master) you want to revert back to, e.g:

git reset --keep a1b2c3d4 (community wiki) (https://stackoverflow.com/questions/1628563/move-the-most-recent-commits-to-a-new-branch-with-git)

### [Removing a File](removing-a-file.md)
This document provides information about how to remove a file from your local repository.
> Follow these steps to learn how to remove a file prior to a commit

### [Removing a branch from your repository](removing-branch-from-your-repository.md)
This document provides information about how to delete a branch from your repository.
> Only do these steps after your pull request get's merged.

### [Resolving Merge Conflicts](resolving-merge-conflicts.md)
This document provides information about how to resolve merge conflicts.
> Take these steps to resolve the annoying merge conflicts.

### [Reverting a commit](reverting-a-commit.md)
This document provides information about how to revert a commit on the remote repository. It will come in handy in case you need to undo a commit that has already been pushed to Github.
> Take these steps if you want to reverse a commit.

### [Squashing Commits](squashing-commits.md)
This document provides information about how to squash commits with an interactive rebase.
> Use this if you want to open a PR in an open source project and the reviewer asks you to squash every commit into one, with an informative commit message.

### [Undo-ing a local commit](undoing-a-commit.md)
This document provides information about how to undo a commit on your local repository. This is what you need to do when you feel you've messed up your local repository and wish to reset the local repository.
> Take these steps if you want to undo/reset a local commit.

### [Useful Links](Useful-links-for-further-learning.md)
This document is dedicated to all the tips and tricks websites, blog posts, and helpful sites that make our lives easier. They are a great reference to serve all of our needs, be it a beginner or an expert. This page should act as an index of all those useful links that would help everybody who is new in the open-source domain or someone who wants to learn more.
