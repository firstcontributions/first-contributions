
Configure the author name and email address to be used with your commits.
Note that Git strips some characters (for example trailing periods) from user.name.
```
git config --global user.name "Sam Smith"

git config --global user.email sam@example.com
```
Create a new local repository
```
git init
```

Create a working copy of a local repository
```
git clone /path/to/repository
```
For a remote server, use:
```
git clone username@host:/path/to/repository
```
