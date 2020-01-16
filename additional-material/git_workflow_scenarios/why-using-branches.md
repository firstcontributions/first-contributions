
# WHY USING BRANCHES DURING CONTRIBUTING

Branches are simply pointers to a commit.

When you branch out, git is essentially making a new state of your current code, upon which you can work, without affecting the important main state of the code (which is in master branch).

When you are happy with your experiments, and want to merge you experiments in main code, you run git merge 
<branch name> master.
 This will tell git, to add in all changes from your experiment branch into master.

 This way, while working in an open source project with a number of contributors, it becomes easy to merge the best suited code without altering the main code or master branch.
 
If the question "Why do we use branching in version control like git?" still persists in your mind, here's a quick explanation:

Let's take a simple example to understand the branching strategy. A production car needs a paint job before its launch. Prior to its official sale, it was decided that the car would come in 'olive green' color as default. But some of the members in the manufacturing team decided to showcase the car in 'red' color. Hence an ambiguous situation arises and to avoid this problem branching was introduced.The red color paint job is like a branch to the master repository 'Car'. Pushing this branch will suggest the red color. If merged with the master repository the car will get the red color otherwise it will continue with olive green. Merging a contributors branch to the master repo of the organization depends on the project head. 
