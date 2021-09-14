# Moving a commit to a different branch
What if you commit a change, and then realize that you committed to a different branch?
How can you change that? This is what this tutorial covers.

## Moving the latest commits to an existing branch
To do this, type:

```git reset HEAD~ --soft``` - Undoes the last commit, but leave the changes available.  
```git stash``` - Records the state of the directory.  

```git checkout name-of-the-correct-branch``` - Switches to another branch.
```git stash pop``` - Removes latest stashed state.  
```git add .``` - Or try adding individual files.  
```git commit -m "your message here"``` - Saves and Commits the changes.  

Now your changes are on the correct branch


### Moving the latest commits to a new Branch
To do this, type:  
```git branch newbranch``` -  Creates a new Branch. Saving all the Commits.  
```git reset --hard HEAD~#``` - Move master back by # commits. Remember, these commits will be gone from master  
```git checkout newbranch``` - Goes to the branch you created. It will have all the commits.  

Remember: Any changes not committed will be LOST.
