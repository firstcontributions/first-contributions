# Amending a Commit

What if you commit a change to your remote repository only to realize later that you have a typo in the commit message or you forgot to add a line in your most recent commit.
How do you edit that? This is what this tutorial covers.

## Changing a recent commit message after you have pushed to Github.
To do this without opening a file:
*   Type in the ```git commit --amend -m "followed by your new commit message"```
*   Run ```git push origin <branch-name>``` to commit the changes to the repository.

Note: If you type in just ```git commit --amend```, your text editor would open up prompting you to edit the commit message.
Adding the ``-m`` flags prevents it.

## Modifying on a single commit

So, what if we forgot to make a minor change to a file like changing a single word and we have already pushed the commit to our remote repository?

To illustrate here is a log of my commits:
```
g56123f create file bot file
a2235d updated contributor.md
a5da0d modified bot file
```
Let's say I forgot to add a single word to the bot file

There are 2 ways to go about this. The first is to have an entirely new commit that contains the change like so:
```
g56123f create file botfile
a2235d updated contributor.md
a5da0d modified botfile
b0ca8f added single word to botfile
```
The second way is to amend the a5da0d commit, add this new word and  push it to Github as one commit.
The second sounds better since it is just a minor change.

To achieve this, we would do the following:
*   Modify the file. In this case, I will modify the botfile to include the word I omitted previously.
*   Next, add the file to the staging area with ```git add <filename>```

Usually after adding files to the staging area, the next thing we do is git commit -m "our commit message" right?
But since what we want to achieve here is to amend the previous commit, we would instead run:

* ```git commit --amend```
 This would then bring up the text editor and prompt you to edit the message. You can decide to leave the message as it was before or change it.
* Exit the editor
* Push your changes with ```git push origin <branch-name>```

That way, both changes would be in one single commit.

## Modifying commits on remote

If the commit that you like to amend has been already pushed to the remote, amending this commit will lead to your local history being diverged from the remote (since you basically create a new commit and replace the amended one). Since you want to change the commit on the remote, you need to overwrite the remotes history on your branch. To achieve that, follow the same procedure as described above, but use force push when pushing your commit to the remote.

> **Warning**  
> Force pushing to the remote will overwrite (and discard) changes on the remote and only keep your pushed commits. Changes on the remote, that other team members did in the meantime, will be overwritten as well.

This is how you modify the last recent commit on the remote:

```bash
git add <your changed files>
git commit --amend -m "followed by your new commit message"
git push --force
```

> Using `--force-with-lease` is a safer option instead of `--force` which avoids overwriting other people's changes on the remote branch (if you do not intend to do so).
