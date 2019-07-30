#### Importance of Branching

Branches are extremely important when working on an open source project. Master is deployable, meaning that any adverse additions or deletions from master will impact the users of the software.

A good practice is to create your own branch, commit changes, merge master in to the development branch, and then, if there are any, resolve any merge conflicts. You don't want merge conflicts occurring when trying to merge the development branch in to master. This can hamper the working of the product the contributor is working on and also affect the users of the product.

So, it is very important that the contributor first locally tests all the commits he or she has made on a separate branch of their local fork of the original repo and then only merge the changes in the master of their upsteam repository.



