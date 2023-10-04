# Removing a file from Git

Sometimes, you may want to remove a file from Git but not delete it from your computer. You can achieve this by using the following command:

``git rm <file> --cached``

## So what happened?

Git will no longer keep track of changes in the removed file. As far as Git knows, it's as if you had deleted the file. If you were to locate the file in your file system, you will notice that it's still there.

Notice that in the example above, the flag `--cached` is used. If we didn't add this flag, Git will remove the file from not just the repo, but from your file system too.

If you commit the change with `git commit -m "Remove file1.js"` and pushed it to the remote repository using `git push origin master`, the remote repository will remove the file.

## Additional features

-   If you want to remove more than one file, you can include them all in the same command:

    `git rm file1.js file2.js file3.js --cached`

-   You can use a wildcard (*) to remove similar files. For example, if you would like to remove all .txt files from your local repository:

    `git rm *.txt --cached`
