To see which remote servers you have configured, you can run the 
```
 git remote 

 ```

 You can also specify -v, which shows you the URLs that Git has stored for the shortname to be used when reading and writing to that remote

 ```
 git remote -v 

 ```

 ** Adding Remote Repositories
 git remote add <shortname> <repo-url>
 to fetch all the information :
 git fetch <shortname>
**Pushing to Your Remotes
```
git push <shortname> <branch>

```
exemple
git push origin main

** remove remote
```
git remote remove
```
exemple 
git remove origin

