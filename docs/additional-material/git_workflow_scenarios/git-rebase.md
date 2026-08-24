# Git Rebase

`git rebase` reapplies commits from one branch on top of another base commit, creating a linear history instead of a merge commit's diverging graph.

## Why Use It

- Keep a clean, linear project history (no unnecessary merge commits)
- Update a feature branch with the latest changes from `main`
- Clean up, reorder, squash, or edit commits before merging/publishing
- Make `git bisect` and `git log` easier to read

## How It Works

Rebase takes the commits unique to your branch, temporarily sets them aside, moves your branch tip to the new base, then reapplies each commit one by one on top of it — generating new commits (new SHAs) in the process.

```
Before:
main:      A---B---C
                \
feature:         D---E

After `git rebase main` (on feature):
main:      A---B---C
                     \
feature:              D'---E'
```

## Basic Commands

### Rebase current branch onto another
```bash
git checkout feature
git rebase main
```
Moves `feature`'s commits to start from the tip of `main`.

### Continue after resolving a conflict
```bash
git add <resolved-file>
git rebase --continue
```

### Skip a commit that's causing conflicts
```bash
git rebase --skip
```

### Abort and return to the pre-rebase state
```bash
git rebase --abort
```

## Interactive Rebase

```bash
git rebase -i HEAD~5
```
Opens an editor listing the last 5 commits, each with a command:

| Command | Effect |
|---|---|
| `pick` | Keep the commit as-is |
| `reword` | Keep content, edit commit message |
| `edit` | Pause here to amend the commit |
| `squash` | Merge into previous commit, combine messages |
| `fixup` | Merge into previous commit, discard this message |
| `drop` | Remove the commit entirely |
| `exec` | Run a shell command at this point |

Reorder lines to reorder commits in history.

### Squash the last N commits into one
```bash
git rebase -i HEAD~3
# mark commits 2 and 3 as "squash" or "fixup"
```

### Edit an old commit
```bash
git rebase -i HEAD~3
# mark the commit as "edit"
git commit --amend
git rebase --continue
```

## Rebase vs. Merge

| | Merge | Rebase |
|---|---|---|
| History | Preserves actual history, adds merge commit | Rewrites history, linear |
| Commit SHAs | Unchanged | New SHAs created |
| Safety on shared branches | Safe | Risky (see below) |
| Conflict resolution | Once, at merge time | Potentially once per commit |
| Traceability | Shows when branches diverged/joined | Looks like work happened sequentially |

## Common Workflows

**Update a feature branch with latest main:**
```bash
git checkout feature
git fetch origin
git rebase origin/main
```

**Clean up commits before opening a PR:**
```bash
git rebase -i origin/main
# squash/reword/reorder as needed
git push --force-with-lease
```

**Rebase onto a different base (`--onto`):**
```bash
git rebase --onto main server client
```
Takes commits in `client` that aren't in `server`, and replays them onto `main`.

## The Golden Rule of Rebasing

**Never rebase commits that have been pushed to a shared/public branch** that others may have based work on. Rebasing rewrites commit history (new SHAs), so anyone who already pulled the old commits will have a diverged, conflicting history. Rebase is safe for:
- Local commits not yet pushed
- Your own feature branches nobody else is using
- Cleaning up before your first push, or before opening a PR

## Force-Pushing After a Rebase

Since rebase rewrites history, you must force-push to update a remote branch:
```bash
git push --force-with-lease
```
Prefer `--force-with-lease` over `--force` — it fails if the remote has commits you haven't seen (e.g., a teammate pushed in the meantime), preventing accidental overwrites.

## Handling Conflicts During Rebase

1. Git stops at the conflicting commit and marks conflict markers in the file(s).
2. Resolve the conflicts manually in each file.
3. Stage the resolved files: `git add <file>`
4. Continue: `git rebase --continue`
5. Repeat for each conflicting commit until the rebase finishes.
6. If it gets too messy: `git rebase --abort` to return to the original state.

## Rebase and Merge Conflicts Caching

```bash
git rebase --continue
git config rerere.enabled true
```
`rerere` ("reuse recorded resolution") remembers how you resolved a conflict and auto-applies the same resolution if it recurs — useful for long-running rebases with repeated conflicts.

## Notes & Gotchas

- Rebasing changes commit hashes — anything referencing the old hashes (tags pointing to them, other branches, PR review comments tied to old SHAs on some platforms) can become disconnected.
- `git pull --rebase` rebases your local commits on top of fetched changes instead of creating a merge commit — a common alternative to `git pull`.
- An interactive rebase can be aborted at any point with `git rebase --abort`, restoring the branch to its pre-rebase state.
- `git rebase -i --autosquash` automatically reorders `fixup!`/`squash!` commits (made with `git commit --fixup <sha>`) next to their targets.
- Rebasing merge commits is complex and can duplicate commits unless you use `git rebase -i --rebase-merges`.

## Quick Reference

| Command | Description |
|---|---|
| `git rebase main` | Rebase current branch onto main |
| `git rebase -i HEAD~n` | Interactive rebase of last n commits |
| `git rebase --continue` | Continue after resolving a conflict |
| `git rebase --skip` | Skip the current commit |
| `git rebase --abort` | Cancel and restore original state |
| `git rebase --onto <newbase> <upstream> <branch>` | Rebase a range onto a new base |
| `git pull --rebase` | Rebase local commits on top of fetched changes |
| `git push --force-with-lease` | Safely force-push after rebase |