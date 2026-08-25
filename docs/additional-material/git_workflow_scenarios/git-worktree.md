# Git Worktree

`git worktree` lets you check out multiple branches from the same repository into separate directories simultaneously, each with its own working directory and index, all sharing the same underlying `.git` history/object database.

## Why Use It

- Work on a hotfix branch without stashing or committing WIP on your feature branch
- Run tests/builds on one branch while editing code on another, in parallel
- Compare two branches side by side in separate editor windows
- Avoid the overhead of cloning the repo again just to check out a second branch
- Keep a long-running branch (e.g., a release branch) checked out permanently in its own folder

## The Problem It Solves

Normally, a Git repository has exactly one working directory — checking out a different branch changes the files in place, and you can't have two branches checked out at once. Historically, the workaround was to clone the repo again into a second folder, but that duplicates the whole object database and requires separate fetches to stay in sync.

`git worktree` instead lets multiple working directories share **one** `.git` object database — no duplication, and all worktrees see the same remotes, tags, and history.

## Basic Commands

### Add a new worktree for an existing branch
```bash
git worktree add ../hotfix-branch hotfix-branch
```
Creates a new directory `../hotfix-branch` checked out to the `hotfix-branch` branch.

### Add a new worktree with a new branch
```bash
git worktree add -b new-feature ../new-feature main
```
Creates branch `new-feature` off `main`, checked out in `../new-feature`.

### Add a worktree in detached HEAD state (e.g., to inspect a specific commit)
```bash
git worktree add --detach ../inspect-commit <commit-hash>
```

### List all worktrees
```bash
git worktree list
```
Output:
```
/path/to/main-repo        a1b2c3d [main]
/path/to/hotfix-branch     e4f5g6h [hotfix-branch]
/path/to/new-feature       i7j8k9l [new-feature]
```

### Remove a worktree
```bash
git worktree remove ../hotfix-branch
```
Removes the worktree's directory and its administrative files (only works if the worktree is clean — no uncommitted changes).

```bash
git worktree remove --force ../hotfix-branch
```
Force-remove even with uncommitted changes (they will be lost).

### Move a worktree
```bash
git worktree move ../old-location ../new-location
```

### Prune stale worktree metadata
```bash
git worktree prune
```
If a worktree directory was deleted manually (e.g., `rm -rf` instead of `git worktree remove`), its metadata lingers in `.git/worktrees/` — this cleans it up.

## Common Workflows

**Quick hotfix without disturbing current work:**
```bash
# You're mid-feature on `feature-x`, uncommitted changes present
git worktree add ../hotfix -b hotfix/urgent-bug main
cd ../hotfix
# fix the bug, commit, push, open PR
cd ../original-repo
# feature-x working directory untouched the whole time
```

**Run tests on main while developing a feature:**
```bash
git worktree add ../main-tests main
cd ../main-tests && npm test
# meanwhile, keep coding in the original feature worktree
```

**Review a PR/branch without disturbing your current branch:**
```bash
git worktree add ../review-pr-42 origin/pr-42-branch
cd ../review-pr-42
# inspect, test, etc.
git worktree remove ../review-pr-42   # clean up when done
```

**Compare two branches side by side:**
```bash
git worktree add ../branch-a branch-a
git worktree add ../branch-b branch-b
# open both directories in separate editor windows
```

## Constraints & Rules

- **A branch can only be checked out in one worktree at a time.** Trying to `git worktree add` a branch already checked out elsewhere will fail:
  ```
  fatal: 'branch-name' is already checked out at '/path/to/other/worktree'
  ```
  Use `--detach` or check out a different branch/commit if you just want to look, or use `git worktree add ../dir branch --force` cautiously (advanced/edge-case use).
- Each worktree has its own index (staging area) and `HEAD`, but shares refs, objects, and config with the main repository.
- Deleting a worktree's directory manually (without `git worktree remove`) leaves stale metadata — run `git worktree prune` afterward.
- The original repository directory is itself considered the "main" worktree and can't be removed with `git worktree remove`.
- Submodules have historically had rough edges with worktrees — verify behavior if your repo uses them.

## Useful Flags

| Flag | Description |
|---|---|
| `-b <name>` | Create a new branch for the worktree |
| `-B <name>` | Create or reset a branch (force) for the worktree |
| `--detach` | Check out in detached HEAD state, no branch |
| `--force` | Bypass safety checks (e.g., same branch checked out elsewhere) |
| `--lock` | Lock the worktree to prevent `prune`/`remove` (e.g., for worktrees on removable media) |
| `--track` / `--no-track` | Control upstream tracking when creating a branch from a remote |

### Lock a worktree
```bash
git worktree lock ../hotfix --reason "on external drive"
git worktree unlock ../hotfix
```

## Notes & Gotchas

- All worktrees share the same `.git` object database, so disk usage is much lower than separate clones — only the working files are duplicated, not the full history.
- Fetching/pulling in one worktree updates the shared remotes/refs — visible to all worktrees, though each worktree's checked-out branch stays where it is until you switch or merge.
- `git worktree list --porcelain` gives machine-readable output, handy for scripting.
- Worktrees are stored under `.git/worktrees/<name>/` in the main repo — don't hand-edit these.
- If you delete the **main** worktree's directory, all linked worktrees become unusable — the main worktree can't itself be `git worktree remove`d, only manually deleted with caution (and it breaks the others).
- Combine with CI: some teams use a dedicated worktree per long-lived branch (e.g., `main`, `staging`, `release`) that CI or a bot keeps updated without ever needing to `checkout` and disturb a developer's active worktree.

## Quick Reference

| Command | Description |
|---|---|
| `git worktree add <path> <branch>` | Check out an existing branch into a new worktree |
| `git worktree add -b <new-branch> <path> <start-point>` | Create a new branch in a new worktree |
| `git worktree add --detach <path> <commit>` | Detached-HEAD worktree at a commit |
| `git worktree list` | List all worktrees |
| `git worktree remove <path>` | Remove a worktree (must be clean) |
| `git worktree remove --force <path>` | Force-remove, discarding changes |
| `git worktree move <old> <new>` | Move a worktree's location |
| `git worktree lock <path>` | Prevent a worktree from being pruned/removed |
| `git worktree unlock <path>` | Unlock a worktree |
| `git worktree prune` | Clean up metadata for manually deleted worktrees |