# Cherry-picking a commit

Sometimes you want to apply a specific commit from one branch to another — without merging the entire branch. Git's `cherry-pick` command lets you do exactly that.

## When would you use this?

- You made a bug fix on `main` and need it on a release branch too.
- A colleague's feature branch has one useful commit you want, but the rest isn't ready.
- You accidentally committed to the wrong branch and want to move just that commit.

## Steps

### 1. Find the commit hash you want to copy

Switch to the branch that has the commit you want:

```
git log --oneline
```

Copy the short hash (the 7-character code at the start of the line) of the commit you want.

### 2. Switch to the branch where you want to apply it

```
git switch main
```

### 3. Cherry-pick the commit

```
git cherry-pick <commit-hash>
```

Replace `<commit-hash>` with the hash you copied. Git will apply that commit on top of your current branch.

## Example

```
$ git log --oneline feature/my-branch
a3f8c12 Fix typo in README
9d1e034 Add new feature
...

$ git switch main
$ git cherry-pick a3f8c12
[main 7bc4d91] Fix typo in README
 1 file changed, 1 insertion(+), 1 deletion(-)
```

## Cherry-picking multiple commits

To cherry-pick a range of commits (from oldest to newest):

```
git cherry-pick <oldest-hash>^..<newest-hash>
```

## Handling conflicts

If cherry-pick causes a conflict, Git will pause and let you resolve it:

1. Fix the conflicting files.
2. Stage the resolved files: `git add <file>`
3. Continue: `git cherry-pick --continue`

To cancel and go back to where you started:

```
git cherry-pick --abort
```

## Key things to know

- Cherry-pick creates a **new commit** with a new hash — it does not move the original.
- The original commit stays on its branch unchanged.
- Use cherry-pick sparingly; if you frequently need to share code between branches, consider restructuring your branching strategy.