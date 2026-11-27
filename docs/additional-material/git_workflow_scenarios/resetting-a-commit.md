# Reset a commit

```reset``` is the command which can be used when we want to move the current branch back to a previous commit.<br/>
The main difference between resetting and reverting a commit is that ```git reset``` moves the current branch back to an older commit (the discarded commits disappear from the branch history), while ```git revert``` creates a brand new commit that undoes the changes of an older one, so the original commits stay in the history and nothing is removed from the remote repository. <br/>

By default (mixed mode), ```git reset``` keeps the changes made in the discarded commits in your working directory as uncommitted changes, so you can recommit them however you like. If you want to discard those changes completely as well, add the ```--hard``` flag — but be careful, uncommitted work will be lost.

```git reset``` can be achieved using following commands:
- The following command will give summary of all the commits using following two parameters:
   
     - The first seven characters of the commit hash - this is what we need to refer to in our **reset** command.
     - the commit message
  
   ```
   git log --oneline
   ```
 
   
- One can reset repository back to the specific commit using following command: <br />
  ```git reset commithash```
  where commithash being the first 7 characters of the commit hash we found in the log

  To reset and discard all the changes made after that commit at the same time, add the ```--hard``` flag:
  ```
  git reset --hard commithash
  ```
  Avoid ```--hard``` on commits you have already pushed to a shared repository, as rewriting shared history causes problems for everyone else (use ```git revert``` for that instead).
