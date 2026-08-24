# Git Cherry-Pick

`git cherry-pick` applies the changes introduced by an existing commit (or commits) from one branch onto another, creating a new commit with the same changes but a different SHA.

## Why Use It

- Apply a specific bug fix from one branch to another without merging everything
- Backport a fix to a release/maintenance branch
- Move a commit that was accidentally made on the wrong branch
- Selectively bring in one or two commits from a feature branch without the rest

## How It Works

Cherry-pick takes the diff introduced by a target commit and replays it as a new commit on your current branch. The original commit is untouched; a new commit (new SHA, same author/message by default) is created.

```
Before:
main:      A---B---C
                     \
feature:              D---E---F

`git cherry-pick E` while on main:

main:      A---B---C---E'
                     \
feature:              D---E---F
```

## Basic Commands

### Cherry-pick a single commit
```bash
git cherry-pick <commit-hash>
```

### Cherry-pick multiple specific commits
```bash
git cherry-pick <hash1> <hash2> <hash3>
```
Applied in the order listed, each as a separate commit.

### Cherry-pick a range of commits
```bash
git cherry-pick <start-hash>..<end-hash>
```
Applies commits after `start-hash` up to and including `end-hash` (start is **excluded**).

```bash
git cherry-pick <start-hash>^..<end-hash>
```
Use `^` after the start hash to **include** it in the range.

### Cherry-pick without committing immediately
```bash
git cherry-pick -n <commit-hash>
# or
git cherry-pick --no-commit <commit-hash>
```
Applies changes to the working directory/index but doesn't create a commit — useful for combining multiple cherry-picks into one commit, or reviewing/editing before committing.

## Handling Conflicts

If the cherry-picked changes conflict with your current branch:

1. Git pauses and marks the conflicting files.
2. Resolve conflicts manually.
3. Stage the resolved files: `git add <file>`
4. Continue: `git cherry-pick --continue`

### Abort a cherry-pick in progress
```bash
git cherry-pick --abort
```
Restores everything to the pre-cherry-pick state.

### Skip the current commit (in a multi-commit cherry-pick)
```bash
git cherry-pick --skip
```

## Useful Flags

| Flag | Description |
|---|---|
| `-n`, `--no-commit` | Apply changes without committing |
| `-e`, `--edit` | Open editor to modify commit message before committing |
| `-x` | Append a line noting the original commit hash it was cherry-picked from (good for public/shared branches, so origin is traceable) |
| `-s`, `--signoff` | Add a `Signed-off-by` line |
| `-m <parent-number>` | Required when cherry-picking a **merge commit** — specifies which parent to treat as the mainline |
| `--strategy=<strategy>` | Use a specific merge strategy (e.g. `recursive`, `ours`) |
| `--strategy-option=<option>` | Pass an option to the merge strategy (e.g. `theirs`) |

### Cherry-pick a merge commit
```bash
git cherry-pick -m 1 <merge-commit-hash>
```
`-m 1` tells Git to diff against the merge commit's first parent (typically the branch it was merged into) to determine what changes to apply.

### Keep a traceability reference to the original commit
```bash
git cherry-pick -x <commit-hash>
```
Adds `(cherry picked from commit <hash>)` to the commit message — useful when backporting to release branches so the origin is clear.

## Common Workflows

**Backport a fix to a release branch:**
```bash
git checkout release-1.0
git cherry-pick -x <fix-commit-hash>
git push origin release-1.0
```

**Move a commit from the wrong branch:**
```bash
git checkout correct-branch
git cherry-pick <commit-hash>
git checkout wrong-branch
git reset --hard HEAD~1   # remove it from the wrong branch
```

**Combine several commits into one:**
```bash
git cherry-pick -n <hash1> <hash2> <hash3>
git commit -m "Combined fix from three commits"
```

**Cherry-pick a range while skipping merge commits:**
```bash
git cherry-pick --no-merges <start>..<end>
```

## Notes & Gotchas

- Cherry-picking creates a **new commit with a new SHA** — Git treats it as a distinct commit from the original, even though the content/diff is the same.
- If you later merge or rebase the branches together, Git usually recognizes identical changes and won't duplicate them, but this isn't always guaranteed — conflicts can occur if the histories have diverged significantly.
- Cherry-picking a commit that depends on earlier commits (e.g., it modifies code introduced in a prior commit not yet on your branch) will likely cause conflicts or errors.
- Overusing cherry-pick instead of merge/rebase can lead to a messy, hard-to-follow history with duplicate-looking commits across branches.
- Cherry-picking merge commits is rarely a good idea unless you know exactly why (use `-m` carefully).
- Empty cherry-picks (where the change is already present) will normally error out; use `--allow-empty` or `--keep-redundant-commits` to force them if needed.

## Quick Reference

| Command | Description |
|---|---|
| `git cherry-pick <hash>` | Apply a single commit |
| `git cherry-pick <h1> <h2>` | Apply multiple commits |
| `git cherry-pick A..B` | Apply a range (A excluded) |
| `git cherry-pick A^..B` | Apply a range (A included) |
| `git cherry-pick -n <hash>` | Apply without committing |
| `git cherry-pick -x <hash>` | Apply and note original commit source |
| `git cherry-pick -m 1 <hash>` | Cherry-pick a merge commit |
| `git cherry-pick --continue` | Continue after resolving conflicts |
| `git cherry-pick --skip` | Skip current commit |
| `git cherry-pick --abort` | Cancel and restore original state |