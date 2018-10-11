# Revert a commit

To revert a commit simply means to create a brand new commit that undoes all
the changes made in a previous one. It is like doing a ```CTRL + Z ``` on git.

Reversion is made easier in git because every commit you push to your remote repository has a unique alphanumeric key known as SHA(Secure Hash Algorithm) tied to it.
So this means you can revert any commit as long as you have the SHA.
But then, you have to be careful to reverse orderly so as not to mess your repository up.


To pick out the SHA of the specific commit we want to undo, a log of all the commits we have made so far would come in handy.
To get this, we would run the command:
```git log --oneline ```
Running the ```git log``` command alone would also give us the SHAs (in long form)
However using the ```--oneline ``` flag tells git that we want it displayed in a concise (one line) manner for easy read.

The first 7 characters displayed when you run this command is called the abbreviated commit hash.

For example, here is what I get when I run ```git log --oneline ``` on this repository:
```
389004d added spacing in title
c1b9fc1 Merge branch 'master' into tutorials
77eaafd added tutorial for reverting a commit
```

So this shows that with ```git log --oneline```, we can fetch a list of all the commits made on the repository together with the first 7 characters of its SHA.

Now, Let's assume I want to undo my commit of "added spacing in title", here are the steps I would take:

*   Copy the SHA of the commit which, in this case is ```389004d```
*   Then, run the command ```git revert 389004d```

This would pop open my text editor and prompt me to edit the commit message.
You can decide to leave the commit message as the default git message which starts with the word `Revert`
or you can also decide to customize the message to your liking.

*   Next, I will save and close the text editor.
*   Return to the command line.
*   Run ```git push origin <branch-name>``` to push the reverted changes to Github.

And that is it, the change would be undone. In this case,  my repository would be reverted to how it looked like in ```c1b9fc1```
