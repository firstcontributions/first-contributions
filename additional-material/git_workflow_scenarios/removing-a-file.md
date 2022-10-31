# Removing a file from Git

Sometimes, you may want to remove a file from Git, but not delete it from your computer. For that, use the following command:
``Git rm <file> --cached``

## So what happened?

Git will no longer record any changes in the deleted file. As far as Git knows, that's like deleting the file. If you had to find the file in your filesystem, you will notice it is still there.

Notice that in the example above, the flag `--cached` is used. If we haven't added this flag, Git will remove the file not only from the repo, but also from your file system.

If you commit the change to `git commit -m "Remove file1. j's"` and pushed it to the remote repository using `git push origin master`, the remote repository will remove the file.

## Additional features

- If you want to remove more than one file, you can include them all in a single command:
    `Git rm file1. J's file2. J's file3. J's --cached`

-   You can use a wildcard (*) to remove similar files. For example, if you would like to remove all .txt files from your local repository:

    `git rm *.txt --cached`