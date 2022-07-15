# .gitignore

The .gitignore file is a text file that tells Git which files or folders to ignore from your local repository when pushing it to the remote repository.

A local .gitignore file is usually placed in the root directory of a local project. You can also create a global .gitignore file and any entries in that file will be ignored in all of your Git repositories.

## Why .gitignore
Now you may wonder why would you want git to ignore certain files and folders. Its because you don't want files like build files, cache files, other local configuration files like node modules, compilation files, temporary files IDE's create, etc to be tracked by git. It's usually used to avoid committing transient files from your working (or local) directory that aren't useful to other collaborators.

## Getting started
To create a local .gitignore file, create a text file and name it .gitignore (remember to include the . at the beginning). Then edit this file as needed. Each new line should list an additional file or folder that you want Git to ignore.

The entries in this file can also follow a matching pattern.

```
* is used as a wildcard match
/ is used to ignore pathnames relative to the .gitignore file
# is used to add comments to a .gitignore file

This is an example of what the .gitignore file could look like:

# Ignore Mac system files
.DS_store

# Ignore node_modules folder
node_modules

# Ignore all text files
*.txt

# Ignore files related to API keys
.env

# Ignore SASS config files
.sass-cache

```
To add or change your global .gitignore file, run the following command:

```
git config --global core.excludesfile ~/.gitignore_global

```
This will create the file ~/.gitignore_global. Now you can edit that file the same way as a local .gitignore file. All of your Git repositories will ignore the files and folders listed in the global .gitignore file.

## How to Untrack Files Previously Committed from New Gitignore

To untrack a single file, ie stop tracking the file but not delete it from the system use:

```
git rm --cached filename
```

To untrack every file in .gitignore:

First, commit any outstanding code changes, and then run:

```
git rm -r --cached
```

This removes any changed files from the index(staging area), then run:

```
git add .
```
Commit it:

```
git commit -m ".gitignore is now working"
```

To undo ```git rm --cached filename```, use ```git add filename```
