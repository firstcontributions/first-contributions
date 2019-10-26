# Revert a commit using cherry=pick command

Sometimes it may happen that we may want to remove some commit that has been pushed accidently to the remote repo.

We can run the below command to get the list of recent commits

``` git log --oneline ``` this will give the commit ids of all the commits

Then run the command ``` git cherry-pick <SHA> ``` where SHA is the commit id of the commit which you wan to keep and the commits made after that one you want to discard


For example when i run the command ``` git log --oneline``` on my local machine, the output is something like this

```
8463b9fe5 add name to list
d6cfe3d9e Merge pull request #22767 from huisyy/add-meg-h
936d959ef Add Meg to Contributors list
acad380c5 Merge pull request #22766 from siddharth952/add-siddharth-sen
322c5ce9d Add Siddharth Sen to Contributors list
cc7e42270 Merge pull request #22765 from jarofblueberries/add-jarofblueberries
45a014761 Add to Contributors list
41b083725 Merge pull request #22763 from Hangar205/ugarte
89e28c296 my name

```

So suppose i want to revert to the third last commit i.e, i don't want to keep my last(recent) 2 commits

so i run the command ``` git cherry-pick 936d959ef ``` where ``` 936d959ef ``` is the SHA of 3rd last commit