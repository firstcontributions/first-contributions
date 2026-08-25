# Git Reflog

`git reflog` ("reference log") shows a history of where `HEAD` and branch tips have pointed in your local repository — including commits that are no longer reachable from any branch. It's Git's built-in safety net for recovering "lost" work.

## Why Use It

- Recover commits after an accidental `git reset --hard`
- Restore a branch that was accidentally deleted
- Undo a bad rebase or merge
- Find a commit you "lost" after checking out a different branch or detached HEAD
- Trace exactly what you did in a session, in order

## How It Works

Every time `HEAD` moves — commits, checkouts, resets, rebases, merges, cherry-picks, amends — Git records an entry in the reflog. This log is **local only** (not pushed, not cloned, not shared with remotes) and each entry has an expiry (default 90 days for reachable entries, 30 days for unreachable ones), after which `git gc` may prune it.

Because the reflog tracks *ref movement*, not just commit history, it can find commits that are no longer part of any branch — as long as they haven't been garbage collected.

## Basic Commands

### View the reflog
```bash
git reflog
```
Output looks like:
```
a1b2c3d HEAD@{0}: commit: fix login bug
e4f5g6h HEAD@{1}: reset: moving to HEAD~1
i7j8k9l HEAD@{2}: commit: add login form
m0n1o2p HEAD@{3}: checkout: moving from main to feature-login
```

Equivalent to:
```bash
git log -g
```

### View reflog for a specific branch
```bash
git reflog show <branch-name>
```

### View reflog with dates
```bash
git reflog --date=iso
```

## Recovering Lost Work

### Restore after an accidental `reset --hard`
```bash
git reflog                       # find the entry before the reset
git reset --hard HEAD@{1}        # or the specific commit hash
```

### Recover a deleted branch
```bash
git reflog                       # find the last commit the branch pointed to
git branch recovered-branch <commit-hash>
```

### Recover after a bad rebase
```bash
git reflog                       # find the entry from before "rebase (start)"
git reset --hard HEAD@{5}        # or whatever entry represents pre-rebase state
```

### Recover a commit lost after `checkout` to another branch
```bash
git reflog
git checkout <commit-hash>       # inspect it
git branch recovered <commit-hash>   # save it to a branch
```

### Undo an amend
```bash
git reflog                       # find entry before "commit (amend)"
git reset --soft HEAD@{1}
```

## Reflog Reference Syntax

| Syntax | Meaning |
|---|---|
| `HEAD@{0}` | Where HEAD is right now |
| `HEAD@{1}` | Where HEAD was one move ago |
| `HEAD@{5}` | Where HEAD was five moves ago |
| `HEAD@{yesterday}` | Where HEAD was as of yesterday |
| `HEAD@{2.days.ago}` | Where HEAD was 2 days ago |
| `master@{1}` | Where the `master` branch pointer was one move ago |

These can be used anywhere a commit reference is accepted:
```bash
git diff HEAD@{2} HEAD@{0}
git show HEAD@{3}
git checkout HEAD@{1}
```

## Inspecting Before Acting

Before resetting/restoring based on a reflog entry, inspect it first:
```bash
git show HEAD@{2}
git log -1 HEAD@{2}
git diff HEAD@{2} HEAD
```

## Pruning and Expiry

### Manually expire old reflog entries
```bash
git reflog expire --expire=now --all
```
Removes entries immediately (use with caution — this is what makes commits actually eligible for garbage collection).

### Change expiry settings
```bash
git config gc.reflogExpire 90.days.ago         # default for reachable entries
git config gc.reflogExpireUnreachable 30.days.ago  # default for unreachable entries
```

### Delete a single reflog entry
```bash
git reflog delete HEAD@{3}
```

## Common Workflow Example

```bash
# Oops — accidentally hard reset and lost 3 commits
git reset --hard HEAD~3

# Check the reflog to find where you were before
git reflog
# a1b2c3d HEAD@{0}: reset: moving to HEAD~3
# e4f5g6h HEAD@{1}: commit: fix edge case
# ...

# Restore back to before the reset
git reset --hard HEAD@{1}
```

## Notes & Gotchas

- The reflog is **per-repository and local** — it is never pushed, fetched, or cloned. A teammate cannot use your reflog to recover your local mistakes, and cloning a repo gives you none of the original's reflog.
- Reflog entries expire and get garbage collected eventually (default 90 days for reachable, 30 for unreachable) — it's a safety net, not permanent storage.
- Every branch has its own reflog in addition to `HEAD`'s reflog (`git reflog show <branch>`), which can help when tracing a specific branch's history separately from what HEAD was doing.
- `git reflog` won't help recover changes that were never committed — it only tracks where refs (HEAD, branches) pointed, not uncommitted working directory or staging changes.
- If in doubt after a scary operation, run `git reflog` *before* doing anything else — the more operations you perform afterward, the further back you may need to look, and the closer entries get to expiry/pruning.
- `git gc` (garbage collection) is what actually deletes unreachable objects once their reflog entries expire — running `git gc --aggressive` right after losing work is risky since it may prune your recovery point.

## Quick Reference

| Command | Description |
|---|---|
| `git reflog` | Show HEAD's reflog |
| `git reflog show <branch>` | Show a specific branch's reflog |
| `git reset --hard HEAD@{n}` | Restore to a specific reflog state |
| `git branch <name> <hash>` | Recreate a branch from a reflog commit |
| `git show HEAD@{n}` | Inspect a reflog entry before acting |
| `git reflog expire --expire=now --all` | Force-expire all reflog entries |
| `git reflog delete HEAD@{n}` | Delete a single reflog entry |