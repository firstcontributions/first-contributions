# How to work cleanly without using branches locally

Someone people get confused between branches, we can work cleaning without using branches locally
What we can do is to work on the master branch locally and push our changes to remote repo in some other branch

#Let me demonstrate by giving an example

Step 1: Fetch changes from remote repo ``` git fetch origin```
Step 2: Set your local repo with the latest master ``` git reset --hard origin/master ```
Step 3: Work locally on master branch and commit your changes ``` git commit -am "some changes" ```
Step 4: Push to some other branch and not the master branch ``` git push origin master:feature ```

# master is the local branch that we want to push and feature is the remote branch that we push the changes into
# the syntax for pushing is <local_branch> : <remote_branch>

Step 5: Now we create a PR and merge our feature branch into the master after completing our feature and pushing the changing into fetaure branch
 