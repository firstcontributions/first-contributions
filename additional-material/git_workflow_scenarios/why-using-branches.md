
# WHY USING BRANCHES DURING CONTRIBUTING

Branches are simply pointers to a commit.

When you branch out, git is essentially making a new state of your current code, upon which you can work, without affecting the important main state of the code (which is in master branch).

When you're happy with your experiments, and want to merge your experiments in the main code, you run:

`git merge <branch name> master`

This will tell git, to add in all changes from your experiment branch into master.

 This way, while working on an open source project with a number of contributors, it becomes easy to merge the best suited code without altering the main code or master branch.
 
