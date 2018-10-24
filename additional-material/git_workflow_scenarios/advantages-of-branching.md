# Branching in workflow.
Normally we pull the code from the git repo ( called the origin ) to the local system and then we make a branch and start working on it. Once you are done and you have commited your work in that branch, we should checkout the master and then do a pull on it. This syncs the work done in the repo since the last time you pulled the code. Now you will need to 'merge' the newer code into your worked-on branch and hence bring the newer code to your work. Now when you push the code into the origin.

Remember, you have synced a local branch into the repository. Now assuming this code is forked from another repository, you will put in a pull request. It becomes very easy for the maintainer to merge your code if there are little or no conflicts.
The branching helps in 2 ways when you have a git workflow.
1. topic based branches: This is when you have a specific task which will just be branched from the master branch and then once the code has been verified by the user, will be merged into master.
2. multi level branches: This could be very specifically dependent on the needs of the organisation, but this means that your code would be merged on a lower branch and then moved up the branches to the master depending on its stability and completeness. 

To conclude, branching keeps everyone sane and productive.

Sources and References:
1. (Branching workflows)[https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows] 
