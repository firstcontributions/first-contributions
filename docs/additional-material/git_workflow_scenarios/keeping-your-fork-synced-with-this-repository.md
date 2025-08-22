# Keeping your fork synced with this repository

First, the flow for a full sync should be understood, which is important. In this schema, there are 3 different repos: my public repo on Github `github.com/firstcontributions/first-contributions.git`, your fork of the repo on GitHub `github.com/Your-Name/first-contributions/` and your local machine's repo from which you are suppose to work. This kind of cooperation is typical for open source projects and called `Triangle Workflows`.

<img style="float;" src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

To keep your two repos up-to-date with my public repo, we first have to fetch and merge the public repo with your local machine's repo.
Our second move will be to push your local repo to your GitHub fork. As you've seen earlier, it's only from your fork that you can ask for a "pull request". So your GitHub fork is the last repo to be updated.

Now, let's see how to do it:

First, you must be on your main branch. To know which branch you are on, check the first line of:
```
git status
```
if you are not already on main:
```
git checkout main
```

Then you should add my public repo to your git with `add upstream remote-url`:
```
git remote add upstream https://github.com/firstcontributions/first-contributions.git
```
This is a way of telling git that another version of this project exists in the specified url and we're calling it `upstream`. Once your git has a name let's fetch the latest version of the public repository:
```
git fetch upstream
```

You've just fetched the latest version of my fork (`upstream` remote). Now, you need to merge the public repository into your main branch.
```
git rebase upstream/main
```
Here you're merging the public repository with your main branch. Your local machine's main branch is now up-to-date. Lastly, if you push your main branch to your fork, your GitHub fork will also have the changes:
```
git push origin main
```
Notice here you're pushing to the remote named `origin`.

If you want to fetch and merge the latest changes of my fork (`upstream` remote) to your local branch at same time then you can directly go for:
```
git pull upstream main
```

So by now or at this point, all your repositories are up-to-date. Well done! You should do this, every time your GitHub repo tells you that you are a few commits behind.
