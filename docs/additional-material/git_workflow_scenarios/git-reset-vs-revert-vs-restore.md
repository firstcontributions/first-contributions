# Git Reset vs. Revert vs. Restore

Three commands that all "undo" things in Git, but operate very differently. Mixing them up is one of the most common sources of Git confusion.

## Quick Summary

| Command | Undoes | Rewrites history? | Scope | Safe on shared branches? |
|---|---|---|---|---|
| `git reset` | Commits (moves branch pointer) | Yes | Commit history, staging area, optionally working dir | No |
| `git revert` | Commits (via new inverse commit) | No (adds new commit) | Commit history | Yes |
| `git restore` | Working directory / staging changes | No | Files only, no commits touched | Yes (doesn't touch history) |

---

## `git reset`

Moves the current branch pointer to a different commit, optionally changing the staging area and working directory too. Used to undo commits locally.

### Modes

```bash
git reset --soft <commit>
```
Moves branch pointer to `<commit>`. Staged changes and working directory are **untouched** — all changes from the "undone" commits are kept staged, ready to recommit.

```bash
git reset --mixed <commit>   # default if no flag given
```
Moves branch pointer to `<commit>`, unstages changes, but **keeps changes in the working directory**. You'd need to `git add` again to restage.

```bash
git reset --hard <commit>
```
Moves branch pointer to `<commit>` and **discards everything** — staged changes and working directory changes from the undone commits are gone. Destructive; uncommitted work is lost.

### Common Usage

```bash
git reset HEAD~1              # undo last commit, keep changes staged (mixed)
git reset --soft HEAD~1       # undo last commit, keep changes staged
git reset --hard HEAD~1       # undo last commit, discard all its changes
git reset HEAD <file>         # unstage a specific file (keep changes in working dir)
git reset --hard origin/main  # reset local branch to match remote exactly
```

### When to Use
- You made a commit (or several) locally that you haven't pushed, and want to undo them
- You want to unstage files you accidentally `git add`ed
- You want to completely discard local commits and/or changes

### Danger
`git reset --hard` **permanently discards** uncommitted changes and detaches commits from any branch (they become unreachable and are eventually garbage collected). Rewrites history — never use on commits already pushed/shared unless you know what you're doing (and are prepared to force-push).

---

## `git revert`

Creates a **new commit** that applies the inverse of a previous commit's changes. History is preserved — nothing is deleted or rewritten, the "undo" is itself a commit.

### Basic Usage

```bash
git revert <commit-hash>
```
Opens an editor to confirm/edit the revert commit message, then creates the new commit.

```bash
git revert --no-edit <commit-hash>
```
Skips the editor, uses a default message.

### Revert without committing immediately
```bash
git revert -n <commit-hash>
# or
git revert --no-commit <commit-hash>
```
Applies the inverse changes to the working directory/index without committing — useful for reverting multiple commits into a single commit.

### Revert a range of commits
```bash
git revert <older-hash>..<newer-hash>
```

### Revert a merge commit
```bash
git revert -m 1 <merge-commit-hash>
```
`-m 1` specifies the parent (mainline) to revert to, same concept as in cherry-pick.

### When to Use
- The commit has already been pushed / is on a shared branch
- You want to undo a change but preserve full history and audit trail
- You need a safe, non-destructive way to undo something in production

### Handling Conflicts
```bash
# resolve conflicts in files
git add <file>
git revert --continue
# or
git revert --abort
```

---

## `git restore`

The newer, more focused command (Git 2.23+) for undoing changes in the **working directory or staging area** — it does not touch commit history at all.

### Restore a file to match the last commit (discard working directory changes)
```bash
git restore <file>
```
Equivalent to the old `git checkout -- <file>`.

### Unstage a file (keep working directory changes)
```bash
git restore --staged <file>
```
Equivalent to the old `git reset HEAD <file>`.

### Restore from a specific commit
```bash
git restore --source=<commit> <file>
```
Replaces the file's working directory content with its version from `<commit>`.

### Restore both staged and working directory versions
```bash
git restore --staged --worktree <file>
```

### Restore everything in the working directory
```bash
git restore .
```

### When to Use
- You edited a file and want to discard the changes, going back to the last commit
- You staged a file (`git add`) and want to unstage it without losing the edits
- You want to pull an old version of a single file from another commit without affecting anything else

### Safety
`git restore` (without `--source`) only ever discards **uncommitted** changes — it never rewrites commit history, and is generally low-risk compared to `reset --hard`. Discarded working-directory changes that were never staged/committed are still gone for good, though — there's no undo for that.

---

## Decision Guide

**"I want to undo a commit that's already pushed / others may have pulled."**
→ `git revert <commit>`

**"I want to undo local commits that haven't been pushed yet, and I don't care about the changes."**
→ `git reset --hard <commit>`

**"I want to undo local commits but keep the changes to redo/recommit them."**
→ `git reset --soft <commit>` (kept staged) or `git reset <commit>` (kept unstaged)

**"I edited a file and want to throw away my uncommitted changes."**
→ `git restore <file>`

**"I staged a file by mistake and want to unstage it (keep the edits)."**
→ `git restore --staged <file>`

**"I want one old file version from history without touching anything else."**
→ `git restore --source=<commit> <file>`

## Side-by-Side Example

Say you have 3 uncommitted edits staged, plus your last commit introduced a bug.

| Goal | Command |
|---|---|
| Unstage the 3 edits, keep them in working dir | `git restore --staged .` |
| Discard the 3 edits completely | `git restore .` |
| Undo the buggy commit but keep its changes staged | `git reset --soft HEAD~1` |
| Undo the buggy commit and discard its changes entirely | `git reset --hard HEAD~1` |
| Buggy commit is already on `main` and pushed — undo safely | `git revert HEAD` |

## Notes & Gotchas

- `git reset` and `git checkout` used to overlap in confusing ways (both handled file restoration and branch switching); `git restore` and `git switch` were introduced in Git 2.23 to split those responsibilities more clearly. `checkout` still works but is considered the "legacy" catch-all.
- `reset --hard` on a branch that others have pulled will cause them major headaches when they next pull/fetch — their local history will diverge.
- `revert` can itself be reverted (revert the revert) if you change your mind — since it's just a normal commit.
- None of these commands recover changes that were never staged or committed — only Git's index/history-tracked states are protected.
- `git reflog` can often rescue commits "lost" via `reset --hard`, as long as they haven't been garbage collected yet — worth knowing as a safety net.

## Quick Reference

| Command | Effect |
|---|---|
| `git reset --soft <c>` | Move branch pointer, keep changes staged |
| `git reset --mixed <c>` | Move branch pointer, keep changes unstaged (default) |
| `git reset --hard <c>` | Move branch pointer, discard all changes |
| `git revert <c>` | New commit that undoes `<c>`, history preserved |
| `git revert -n <c>` | Revert without auto-committing |
| `git restore <file>` | Discard uncommitted working dir changes |
| `git restore --staged <file>` | Unstage a file, keep edits |
| `git restore --source=<c> <file>` | Pull a file's content from another commit |