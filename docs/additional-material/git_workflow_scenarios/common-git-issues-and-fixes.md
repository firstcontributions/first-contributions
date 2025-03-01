Here’s a "Common Git Issues and Fixes" section you can contribute to First Contributions or any other open-source documentation project.

---

### Common Git Issues and Fixes

Git is a powerful tool, but sometimes things go wrong. Here are some common Git issues and how to fix them.

## 1. Undo Last Commit (But Keep Changes)
# Problem: You committed changes by mistake but want to edit before pushing.

# Fix:
```sh
git reset --soft HEAD~1
```
This moves the last commit back to the staging area, keeping your changes.

---

## 2. Undo Last Commit (And Remove Changes)
# Problem: You want to delete the last commit and discard all changes.

# Fix:
```sh
git reset --hard HEAD~1
```
⚠️ Warning: This deletes changes permanently.

---

## 3. Undo `git add` Before Committing
# Problem: You staged (`git add`) files but don’t want them in the next commit.

# Fix:
```sh
git reset HEAD <file>
```
or to unstage all files:
```sh
git reset
```
This moves files back to "unstaged" without losing changes.

---

## 4. Fix "detached HEAD" State
# Problem: You checked out a commit and now you're in a "detached HEAD" state.

# Fix:
```sh
git checkout main  # or your branch name
```
If you want to save changes, create a new branch:
```sh
git checkout -b new-branch
```

---

## 5. Discard Local Changes in a File
# Problem: You made changes to a file but want to reset it to the last committed version.

# Fix:
```sh
git checkout -- <file>
```
or
```sh
git restore <file>
```
⚠️ Warning: This deletes uncommitted changes.

---

## 6. Delete a Local Branch
# Problem: You want to delete a branch that’s no longer needed.

# Fix:
```sh
git branch -d my-branch
```
If the branch is not merged and you really want to delete it:
```sh
git branch -D my-branch
```

---

## 7. Fix a Merge Conflict
# Problem: Git tells you there’s a merge conflict.

# Fix:
1. Open the conflicting file (`git status` will show which files).
2. Look for `<<<<<<<`, `=======`, and `>>>>>>>` markers.
3. Edit the file to keep only the correct version.
4. Add the resolved file:
   ```sh
   git add <file>
   ```
5. Complete the merge:
   ```sh
   git commit
   ```

---

## 8. Force Pull When Local Changes Conflict
# Problem: You need to discard local changes and sync with the remote branch.

# Fix:
```sh
git fetch --all
git reset --hard origin/main  # Replace 'main' with your branch name
```
⚠️ Warning: This will delete any uncommitted local changes.

---

## 9. Fix "fatal: refusing to merge unrelated histories"
# Problem: You’re trying to merge two unrelated repositories.

# Fix:
```sh
git pull origin main --allow-unrelated-histories
```

---

## 10. Revert a Pushed Commit
# Problem: You pushed a commit but want to undo it.

# Fix:
```sh
git revert HEAD
```
This creates a new commit that undoes the last one without changing history.

---
