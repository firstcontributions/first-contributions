# Git Sparse-Checkout

`git sparse-checkout` lets you check out only a subset of a repository's files/directories into your working directory, while the full history is still fetched (unless combined with a partial clone). Useful for very large repositories where you only need part of the tree.

## Why Use It

- Work in a monorepo but only need one project/service's directory
- Avoid checking out huge unrelated directories (assets, unrelated services) you don't touch
- Speed up working-directory operations (status, checkout, IDE indexing) on large repos
- Combine with partial clone to also reduce what's downloaded, not just what's checked out

## How It Works

Sparse-checkout restricts which paths appear in your working directory. The full commit history and (by default) all blobs are still present in the local `.git` object database — sparse-checkout only affects what's materialized as files on disk. For also limiting what's *fetched*, pair it with `git clone --filter` (partial clone).

## Basic Commands (Cone Mode — Recommended)

Git 2.25+ introduced "cone mode," a simpler, faster pattern format recommended over the legacy full pattern-matching mode.

### Enable sparse-checkout (cone mode) and set initial directories
```bash
git sparse-checkout init --cone
git sparse-checkout set dir1 dir2/subdir
```
This checks out only `dir1/`, `dir2/subdir/`, and files at the repo root — everything else disappears from the working directory (but stays in the object database).

### Add more directories
```bash
git sparse-checkout add dir3
```

### List currently included paths
```bash
git sparse-checkout list
```

### Disable sparse-checkout (restore full working directory)
```bash
git sparse-checkout disable
```

## Cloning Directly Into Sparse Mode

```bash
git clone --no-checkout <url>
cd repo
git sparse-checkout init --cone
git sparse-checkout set dir1 dir2
git checkout main
```

Or, in one flow with a filtered (partial) clone for maximum efficiency on huge repos:
```bash
git clone --filter=blob:none --no-checkout <url>
cd repo
git sparse-checkout init --cone
git sparse-checkout set dir1 dir2
git checkout main
```
`--filter=blob:none` avoids downloading file contents you haven't checked out yet — Git fetches blobs on demand as you touch paths within your sparse-checkout set.

## Legacy Mode (Full Pattern Matching)

Before cone mode, sparse-checkout used `.gitignore`-style patterns directly, offering finer control but with steeper performance costs on large repos.

```bash
git sparse-checkout init
```
Then edit `.git/info/sparse-checkout` manually:
```
/dir1/
/dir2/subdir/
*.md
!/dir1/excluded-file.txt
```
Apply changes:
```bash
git sparse-checkout reapply
```

Cone mode is preferred for performance; legacy mode remains available for cases needing individual file patterns rather than whole directories.

## Common Workflows

**Work on just one service in a large monorepo:**
```bash
git clone --filter=blob:none --no-checkout <monorepo-url>
cd monorepo
git sparse-checkout init --cone
git sparse-checkout set services/payments
git checkout main
```

**Add a second directory you now also need:**
```bash
git sparse-checkout add services/shared-lib
```

**Check what's currently sparse-checked-out:**
```bash
git sparse-checkout list
```

**Temporarily see the full tree, then go back:**
```bash
git sparse-checkout disable      # full working directory restored
# ...
git sparse-checkout init --cone
git sparse-checkout set services/payments   # back to sparse
```

## Checking Status

```bash
git sparse-checkout list
```
Shows the currently configured cone-mode directories (or, in legacy mode, prints the raw pattern file).

```bash
git status
```
Still works normally within the sparse-checked-out subset.

## Notes & Gotchas

- Sparse-checkout only affects the **working directory** — the full commit history remains fetchable/present locally unless you also use a partial clone (`--filter`).
- Cone mode restricts inclusion to whole directories (plus files at the root); it can't cherry-pick individual files deep in an excluded directory the way legacy pattern mode can.
- If you `cd` into an excluded directory, it simply won't exist on disk — Git won't error, the path just isn't materialized.
- Combining sparse-checkout with **partial clone** (`--filter=blob:none` or `--filter=blob:limit=<size>`) is what actually reduces network/disk usage; sparse-checkout alone with a full clone still downloads everything, just doesn't check it all out.
- Switching sparse-checkout sets is fast — it doesn't require re-cloning, just re-materializing the working directory for the new path set.
- Some Git operations (e.g., certain merge/rebase conflict scenarios touching excluded paths) can behave unexpectedly; cone mode's directory-based restriction is generally more robust here than legacy pattern mode.
- Sparse-checkout state is local — it's not something you push or that affects other clones/checkouts of the repo.
- `git sparse-checkout list` in cone mode shows directories; running `cat .git/info/sparse-checkout` shows the underlying raw patterns either way.

## Sparse-Checkout vs. Related Features

| Feature | What it limits | Combine with sparse-checkout? |
|---|---|---|
| Sparse-checkout | What's in the working directory | — |
| Partial clone (`--filter`) | What's downloaded from the remote | Yes, commonly paired together |
| Shallow clone (`--depth`) | How much history is fetched | Yes, can combine all three |
| Submodules | Separate embedded repositories | Different problem — use for genuinely separate repos, not just subdirectories |

## Quick Reference

| Command | Description |
|---|---|
| `git sparse-checkout init --cone` | Enable sparse-checkout in cone mode |
| `git sparse-checkout set <dir1> <dir2>` | Set the included directories (replaces previous set) |
| `git sparse-checkout add <dir>` | Add a directory to the current set |
| `git sparse-checkout list` | Show currently included paths |
| `git sparse-checkout disable` | Restore full working directory |
| `git sparse-checkout reapply` | Reapply patterns after manual edits (legacy mode) |
| `git clone --filter=blob:none --no-checkout <url>` | Partial clone paired with sparse-checkout setup |