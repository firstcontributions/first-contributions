# Deleting a locally created Branch

Deleting a locally created branch comes in handy when you have made an unchangeable mistake in that branch.

Deleting a local branch can be performed in **3** ways:

- ```bash
    git branch -D <branch_name>
  ```


- ```
    git branch --delete --force <branch_name>  # Same as -D
  ```


- ```
    git branch --delete  <branch_name>         # Error on unmerge
  ```

### Note
 The `-D` stands for `--delete --force` which will delete the branch even it's not merged (force delete).
 However, you can also use `-d` which stands for `--delete` which throws an error respective of the branch merge status.

 Happy Coding!!