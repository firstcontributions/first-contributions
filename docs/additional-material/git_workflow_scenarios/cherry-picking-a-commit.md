# Cherry-picking a commit

Cherry-picking in Git allows you to choose a specific commit from one branch and apply it onto your current working branch. This is particularly useful when you want to port a bug fix, feature, or specific change without merging the entire source branch.

---

## When to use `git cherry-pick`

* **Porting bug fixes**: You fixed a bug in a development branch and want to apply the fix to a production or release branch immediately.
* **Selectively grabbing features**: A teammate built several commits on a branch, but you only need one specific commit for your work.
* **Recovering lost commits**: You committed changes to the wrong branch and want to bring that specific commit onto the correct branch.

---

## How to Cherry-pick a Commit

### Step 1: Find the Commit Hash

First, locate the commit hash of the change you want to copy. You can view the commit history using `git log`:

```bash
git log --oneline
```

Example output:
```text
e3f1a2b Fix navigation alignment issue
a1b2c3d Add user profile page
9f8e7d6 Update README documentation
```

Copy the commit hash (for example, `e3f1a2b`).

---

### Step 2: Switch to the Target Branch

Switch to the branch where you want to apply the commit:

```bash
git switch target-branch-name
```
*(If using an older version of Git, use `git checkout target-branch-name`)*

---

### Step 3: Run `git cherry-pick`

Apply the commit onto your current branch:

```bash
git cherry-pick e3f1a2b
```

Git will fetch the changes from commit `e3f1a2b` and create a **new commit** on your current branch with the same changes and commit message.

---

## Handling Cherry-pick Conflicts

If the changes in the cherry-picked commit conflict with your current branch, Git will pause the process and report merge conflicts.

1. View the conflicting files:
   ```bash
   git status
   ```

2. Open the conflicting files in your code editor and resolve the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

3. Stage the resolved files:
   ```bash
   git add <file-name>
   ```

4. Continue the cherry-pick:
   ```bash
   git cherry-pick --continue
   ```

If you decide to cancel the cherry-pick operation at any point:
```bash
git cherry-pick --abort
```

---

## Summary of Useful Commands

| Command | Description |
| :--- | :--- |
| `git cherry-pick <commit-hash>` | Applies the specified commit to the current branch. |
| `git cherry-pick <hash1> <hash2>` | Applies multiple specified commits in sequence. |
| `git cherry-pick --continue` | Resumes cherry-picking after resolving merge conflicts. |
| `git cherry-pick --abort` | Cancels the cherry-pick process and restores your working state. |
