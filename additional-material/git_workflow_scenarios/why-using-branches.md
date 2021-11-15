# WHY USING BRANCHES DURING CONTRIBUTING

## What are branches.

Branches are simply pointers to a commit.

When you branch out, git is essentially making a new state of your current code, upon which you can work, without affecting the important main state of the code (which is in master branch).

When you are happy with your experiments, and want to merge you experiments in main code, you run git merge
<branch name> master.
This will tell git, to add in all changes from your experiment branch into master.

This way, while working in an open source project with a number of contributors, it becomes easy to merge the best suited code without altering the main code or master branch.

## How it works?

A branch represents an independent line of development. Branches serve as an abstraction for the edit/stage/commit process. You can think of them as a way to request a brand new working directory, staging area, and project history. New commits are recorded in the history for the current branch, which results in a fork in the history of the project.

The git branch command lets you create, list, rename, and delete branches. It doesn’t let you switch between branches or put a forked history back together again. For this reason, git branch is tightly integrated with the git checkout and git merge commands.

## Why to use branches?

If the question "Why do we use branching in version control like git?" still persists in your mind, here's a quick explanation:

Let's take a simple example to understand the branching strategy. A production car needs a paint job before its launch. Prior to its official sale, it was decided that the car would come in 'olive green' color as default. But some of the members in the manufacturing team decided to showcase the car in 'red' color. Hence an ambiguous situation arises and to avoid this problem branching was introduced.The red color paint job is like a branch to the master repository 'Car'. Pushing this branch will suggest the red color. If merged with the master repository the car will get the red color otherwise it will continue with olive green. Merging a contributors branch to the master repo of the organization depends on the project head.

## Example

Alice is working on Feature A and Bob is working on Feature B. Alice is halfway done with Feature A and has made a few commits in alice. However, Feature A is quite hard to implement so Alice decides that she should rather work on Feature C and makes a few commits onto alice. Bob finished Feature B and decides that he would like to tackle Feature A and so pulls aliceinto bob.

After Bob finishes Feature A he would like to merge bob into master. However, bob now contains Feature A, Feature B and parts of Feature C, but Feature C is not ready to be merged! It's easy to see that a workflow like this can lead to many confusing merge conflicts.

The trick is that instead of having personal branches one should have feature branches. Alice should have a branch for Feature A and Feature C and Bob should have a branch for Feature B and Feature A. That way they both can work on different features without tramping on each other's toes.

## How to create branches?

#### Create a branch

```
git branch AnyBranchName
```

A new branch will be created named AnyBranchName and all the file changes in this branch will not be affected in the main branch.
For detailed explanation refer [How to create branch](https://www.atlassian.com/git/tutorials/using-branches)

#### Delete the branch

```
git branch -d AnyBranchName
```

Branch name AnyBranchName will be deleted from the git repository.
Refer to [Removing branch from your repository](https://github.com/jashnimje/first-contributions/blob/7dcae72208e4b42fcf834b4f189fa8ee78238077/additional-material/git_workflow_scenarios/removing-branch-from-your-repository.md)
