## Revert a commit 

To revert a commit simply means to create a brand new commit that undoes all 
the changes made in a previous one. It is like doing a ```CTRL + Z ``` on git.

Reversion is made easier in git because every commit you push to your remote repository has a unique alphanumeric key known as SHA(Source Hash Algorithm) tied to it it. 
So this means you can revert any commit as long as you have the SHA but you have to be careful to reverse orderly so as not to mess your repository up.


To pick out the SHA of the specific commit we want to undo, a log of all the commits we have made so far would come in handy.
To get this, we would run the command:
```git log --oneline ```
Running the ```git log``` command alone would also give us the SHAs (in long form) however using the ```--oneline ```
flag tells git that we want it displayed in a concise (oneline) manner for easy read.
So with this, we get a list of all the commits made on the repository together with the first 7 characters of its SHA.

* Copy the SHA of the commit you are interested in reversing.
* Now, run the command ```git revert <SHA>```

This would pop open your text editor and prompt you to edit the commit message.
You can decide to leave the commit as the default message which starts with the word `Revert`
or you can also decide to customize the message to your liking.

* Next, save and close your text editor. 
* Go back to your command line.
* Run ```git push origin <branch-name>``` to push the reverted changes to Github.
 
