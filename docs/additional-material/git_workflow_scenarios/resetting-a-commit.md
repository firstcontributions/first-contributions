# Reset a commit

```reset``` is the command which can be used when we want to move the repository back to a previous commit, discarding any changes made after that commit.<br/>
The main difference between resetting and reverting a commit is that git reset ```unstages a file and bring our changes back to the working directory``` 
and git revert ```removes the commits from the remote repository```. <br/>

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
