## Moving a Commit to a different Branch 

What if you commit a change, and then realize that you commited to a different branch?
How can you change that? This is what this tutorial covers.

### Moving the lastest commits to an existing Branch 
To do this, type:  
```git checkout existingbranch```  
```git merge master```  
```git checkout master```  
```git reset --hard HEAD~#``` - Move master back by # commits. Remember, this commits will be gone from master
```git checkout existingbranch```

### Moving the lastest commits to a new Branch 
To do this, type:  
```git branch newbranch``` -  Creates a new Branch. Saving all the Commits.  
```git reset --hard HEAD~#``` - Move master back by # commits. Remember, this commits will be gone from master  
```git checkout newbranch``` - Goes to the branch you created. It will have all the commits.  

Remember: Any changes not commited will be LOST.
