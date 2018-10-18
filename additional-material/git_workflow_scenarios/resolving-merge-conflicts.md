# What is a merge conflict?

When you try to merge another branch into your current working branch, you are taking changes from another context and combine them with your current working files.
If two people changed the same lines in that same file, or if one person decided to delete it while the other person decided to modify it, Git simply cannot know what is correct. Git will then mark the file as having a conflict - which you'll have to solve before you can continue your work.

# How to resolve a merge conflict?

When faced with a merge conflict, git will mark the problematic area in the file by enclosing it in “<<<<<<<< HEAD” and “>>>>>>>>>>[other branch name]”

The contents after the first marker originate from your current working branch. After the angle brackets, Git tells us where (from which branch) the changes came from. A line with "=======" separates the two conflicting changes.
Our job is now to clean up these lines: when we're done, the file should look exactly as we want it to look. It can be necessary to consult the teammate who wrote the conflicting changes to decide which code is finally correct. Maybe it's yours, maybe it's his - or maybe a mixture between the two.

e.g. :
```
 <<<<<<< HEAD:mergetest
 This is my third line
 =======
 This is a fourth line I am adding
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Indicates the start of the lines that had a merge conflict. The first set of lines are the lines from the file that you were trying to merge the changes into.  
`=======`: Indicates the break point used for comparison. Breaks up changes that user has committed (above) to changes coming from merge (below) to visually see the differences.  
`>>>>>>>`: Indicates the end of the lines that had a merge conflict.  

You resolve a conflict by editing the file to manually merge the parts of the file that git had trouble merging. This may mean discarding either your changes or someone else's or doing a mix of the two. You will also need to delete the '<<<<<<<', '=======', and '>>>>>>>' in the file.


Once you have resolved the conflict do `git add`. Do not forget to run the tests that you have to make sure you have resolved the conflict correctly.

You can also download different plugins depending on the IDE you are using for an easier way to resolve merge conflicts.


# How to undo a merge?
If you want to undo a merge then you can do `git merge —abort`


# Removed file merge conflicts
To resolve a merge conflict caused by competing changes to a file, where a person deletes a file in one branch and another person edits the same file, you must choose whether to delete or keep the removed file in a new commit.

For example, if you edited a file, such as README.md, and another person removed the same file in another branch in the same Git repository, you'll get a merge conflict error when you try to merge these branches. You must resolve this merge conflict with a new commit before you can merge these branches.

Open Terminal.

Navigate into the local Git repository that has the merge conflict.

```
cd REPOSITORY-NAME
```

Generate a list of the files affected by the merge conflict. In this example, the file README.md has a merge conflict.
```
$ git status
# On branch master
# Your branch and 'origin/master' have diverged,
# and have 1 and 2 different commits each, respectively.
#  (use "git pull" to merge the remote branch into yours)
# You have unmerged paths.
#  (fix conflicts and run "git commit")
#
# Unmerged paths:
#  (use "git add/rm ..." as appropriate to mark resolution)
#
#  deleted by us:   README.md
#
# no changes added to commit (use "git add" and/or "git commit -a")
```

Open your favorite text editor, such as Atom, and navigate to the file that has merge conflicts.

Decide if you want keep the removed file. You may want to view the latest changes made to the removed file in your text editor.

To add the removed file back to your repository:
```
$ git add README.md
```

To remove this file from your repository:
```
$ git rm README.md
README.md: needs merge
rm 'README.md'
```

Commit your changes with a comment.
```
$ git commit -m "Resolved merge conflict by keeping README.md file."
[branch-d 6f89e49] Merge branch 'branch-c' into branch-d
```
You can now merge the branches on the command line



