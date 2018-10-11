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
