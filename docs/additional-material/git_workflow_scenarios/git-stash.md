# Git Stash

`git stash` temporarily shelves (or stashes) changes you've made to your working directory so you can work on something else, then come back and re-apply them later.

## Why Use It

- Switch branches without committing half-finished work
- Pull updates from remote without conflicts from local changes
- Quickly clean your working directory for testing
- Save experimental changes you're not ready to commit

## Basic Commands

### Stash your changes
```bash
git stash
# or
git stash save "optional message"
```
Stashes tracked, modified files (staged and unstaged). Untracked and ignored files are left alone by default.

### List all stashes
```bash
git stash list
```
Output looks like:
```
stash@{0}: WIP on main: 5002d47 add login form
stash@{1}: On feature-x: fix typo
```

### Apply the most recent stash (keep it in the stash list)
```bash
git stash apply
```

### Apply a specific stash
```bash
git stash apply stash@{2}
```

### Apply and remove the stash in one step
```bash
git stash pop
```

### Remove a specific stash without applying it
```bash
git stash drop stash@{1}
```

### Remove all stashes
```bash
git stash clear
```

### View the contents of a stash
```bash
git stash show
git stash show -p        # full diff
git stash show stash@{1} -p
```

## Advanced Usage

### Stash including untracked files
```bash
git stash -u
# or
git stash --include-untracked
```

### Stash including untracked AND ignored files
```bash
git stash -a
# or
git stash --all
```

### Stash only specific files (interactive)
```bash
git stash -p
# or
git stash --patch
```
Lets you choose hunks interactively, like `git add -p`.

### Stash specific paths
```bash
git stash push -- path/to/file1 path/to/file2
```

### Give a stash a descriptive message
```bash
git stash push -m "WIP: refactor auth middleware"
```
(`git stash push` is the modern, more flexible form of `git stash save`.)

### Create a branch from a stash
```bash
git stash branch new-branch-name stash@{0}
```
Useful when applying the stash would cause conflicts — this creates a new branch from the commit you stashed on, applies the stash, and drops it if successful.

### Keep the staged/index state
```bash
git stash --keep-index
```
Stashes changes but leaves your staged files staged in the working directory too.

### Stash only staged changes
```bash
git stash push --staged
```
(Available in newer Git versions.)

## Common Workflows

**Switch branches quickly:**
```bash
git stash
git checkout other-branch
# do stuff
git checkout original-branch
git stash pop
```

**Pull without conflicts:**
```bash
git stash
git pull
git stash pop
```

**Resolve conflicts on pop:**
If `git stash pop` results in a merge conflict, Git will not drop the stash automatically. Resolve the conflicts, then:
```bash
git add .
git stash drop
```

## Notes & Gotchas

- Stashes are stored as a stack — `stash@{0}` is always the most recent.
- Stashes are local to your repository; they are not pushed to remotes.
- `git stash pop` can fail with conflicts — in that case the stash is *not* automatically dropped, so you don't lose the changes.
- Untracked files are **not** stashed by default — use `-u` if you need them included.
- Stashes can be lost if you run `git stash clear` or `git gc` aggressively drops unreferenced stashes — treat them as short-term, not permanent storage.
- You can stash merge conflict states too, though it's less common and can be tricky to reapply.

## Quick Reference

| Command | Description |
|---|---|
| `git stash` | Stash tracked changes |
| `git stash -u` | Stash tracked + untracked |
| `git stash list` | List all stashes |
| `git stash show -p` | Show diff of latest stash |
| `git stash apply` | Reapply latest stash, keep it stashed |
| `git stash pop` | Reapply latest stash, remove it |
| `git stash drop stash@{n}` | Delete a specific stash |
| `git stash clear` | Delete all stashes |
| `git stash branch <name>` | New branch from a stash |