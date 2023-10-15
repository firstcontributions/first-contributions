# Check commit log

In order to check commits log for a branch, or, a file, following command can be used:

`git log [options] [path]`

The output of this command is given in reverse chronological order by default.

## Command variations and options 
- In order to prform the commits reachable from a particular commit ids: <i>(In this case, `foo` and `bar`)</i><br>
    `git log foo bar ` 
- It is also possible to remove the commits reachable from a given commit id by adding a `^` in front of commit id: <i>(In this case, `baz`)</i><br>
    `git log foo bar ^baz`
- Commit log for a particular file <br> 
    `git log --all <filename>`
- Limit number of commits in log <i>(In this case, `5`)</i><br> 
    `git log -n 5`

## Refer
- [Official documentation](https://git-scm.com/docs/git-log)
