# Git Partial Clone

Partial clone lets you clone a repository **without downloading every object** (blobs and/or trees) up front. Git fetches the missing objects on demand, later, as you actually need them (checkout, diff, log -p, etc.). Aimed at very large repositories where a full clone is slow or wastes bandwidth/disk.

## Why Use It

- Clone huge repositories (large monorepos, repos with big binary history) much faster
- Save disk space by not storing blobs you'll never touch
- Combine with sparse-checkout to only ever fetch what you actually check out
- Useful for CI runners that only need certain paths/depths, or for quick one-off inspections of a large repo

## How It Works

A normal `git clone` downloads the full history: every commit, tree, and blob (file content) ever created. Partial clone instead downloads the commit and tree structure (so you have full history/metadata) but **omits blob contents** (or other objects) according to a filter you specify. Git marks the repo as a "promisor" remote — when an omitted object is actually needed (e.g., you check out a file, or `git log -p` needs a diff), Git transparently fetches it from the origin on demand.

```
Full clone:     [commits] + [trees] + [ALL blobs]         <- everything downloaded
Partial clone:  [commits] + [trees] + [blobs as needed]    <- blobs fetched lazily
```

## Basic Commands

### Clone without any file contents (blobless clone)
```bash
git clone --filter=blob:none <url>
```
Downloads all commits and trees (so `git log`, `git blame` metadata, and history browsing work fully) but no file contents until you check out a specific commit/branch — then only the blobs needed for that checkout are fetched.

### Clone with a blob size limit
```bash
git clone --filter=blob:limit=1m <url>
```
Downloads blobs smaller than 1 MB up front; larger blobs (e.g., binaries, large assets) are fetched on demand only when needed.

### Clone with no tree objects at all except at the checked-out commit (treeless clone)
```bash
git clone --filter=tree:0 <url>
```
More aggressive — even tree objects for history you're not actively browsing are fetched lazily. Operations like `git log -p` on old commits will trigger more network fetches than `blob:none`.

## Common Filter Specs

| Filter | Effect |
|---|---|
| `blob:none` | Omit all blobs; fetch on demand |
| `blob:limit=<size>` | Omit blobs larger than `<size>` (e.g., `1k`, `1m`, `500k`) |
| `tree:0` | Omit all trees and blobs except those needed for the initial checkout |
| `sparse:oid=<blob-ish>` | Use a sparse-checkout spec (from a blob) to determine what to include — advanced/less common |

## Combining with Sparse-Checkout

This is the most common and powerful pairing — partial clone reduces what's *downloaded*, sparse-checkout reduces what's *checked out*, and together they minimize both:

```bash
git clone --filter=blob:none --no-checkout <url>
cd repo
git sparse-checkout init --cone
git sparse-checkout set services/payments
git checkout main
```

With this setup, Git only ever fetches blobs for files inside `services/payments/` (plus root-level files) — the rest of a massive monorepo is never downloaded.

## Converting an Existing Full Clone

You can't directly "shrink" an existing full clone into a partial one, but you can add a filter for future fetches:
```bash
git remote set-url origin --add <url>
git config remote.origin.promisor true
git config remote.origin.partialCloneFilter blob:none
```
This is a less common workflow — it's usually simpler to do a fresh partial clone if you need the space/bandwidth savings retroactively.

## Checking Status

### See if a repo is a partial clone
```bash
git rev-parse --is-shallow-repository   # for shallow clones, not partial — see below
cat .git/config | grep -A2 '\[remote "origin"\]'
```
Look for `promisor = true` and `partialCloneFilter = ...` under the remote's config section.

### See how many objects are missing/lazily fetched
```bash
git count-objects -v
```

## Fetching Missing Objects Manually (Prefetch)

If you know you'll need a broader set of objects soon (e.g., before going offline), you can prefetch:
```bash
git fetch --filter=blob:none
```
Or explicitly backfill everything:
```bash
git fetch origin --filter=blob:none --unshallow  # if also shallow
```

To fully "unfilter" and download everything you were missing:
```bash
git config remote.origin.promisor false
git fetch --refetch
```
(Behavior/flags for fully converting back to a full clone can vary by Git version — check `git fetch --help` for your version's options.)

## Partial Clone vs. Shallow Clone

These solve different problems and are often confused:

| | Partial Clone | Shallow Clone |
|---|---|---|
| Limits | Object **content** (blobs/trees) | Commit **history depth** |
| History | Full history metadata available | Truncated — history beyond depth doesn't exist locally |
| `git log` on old commits | Works (may fetch blobs on demand) | Fails/limited beyond the shallow boundary |
| Can push from it | Yes, generally | Complicated — pushing from shallow clones has restrictions |
| Typical flag | `--filter=blob:none`, `--filter=tree:0` | `--depth=<n>` |
| Good for | Huge repos with big files, need full history | Huge repos with long history you don't need, CI checkouts |

They can be combined:
```bash
git clone --filter=blob:none --depth=1 <url>
```

## Common Workflows

**Fast clone of a huge monorepo for a small piece of work:**
```bash
git clone --filter=blob:none --no-checkout <url>
cd repo
git sparse-checkout init --cone
git sparse-checkout set my/team/directory
git checkout main
```

**CI job that only needs recent history and no huge assets:**
```bash
git clone --filter=blob:limit=1m --depth=50 <url>
```

**Inspect a huge repo's structure/history without downloading everything:**
```bash
git clone --filter=tree:0 --no-checkout <url>
cd repo
git log --oneline           # works, walks commit graph
git show <old-commit>:<path>  # triggers on-demand fetch for that specific blob
```

## Notes & Gotchas

- Requires server-side support for partial clone (most modern Git hosts — GitHub, GitLab, Bitbucket — support it; older/self-hosted servers may not).
- On-demand fetches happen transparently but require network access — working fully offline with a partial clone means anything not already fetched will fail until you're back online.
- Partial clone adds latency to operations that touch not-yet-fetched objects (e.g., `git blame` across history, `git log -p` on old files) since each miss triggers a network round-trip — mitigate by prefetching or narrowing scope with sparse-checkout.
- `git gc` and repacking behave slightly differently in promisor remotes — avoid aggressive local pruning that might remove objects the server still promises to serve, unless you know what you're doing.
- Partial clone is a good complement to, but distinct from, Git LFS — LFS replaces large files with pointers permanently (even after "full" checkout), whereas partial clone just delays fetching a normal blob until needed.

## Quick Reference

| Command | Description |
|---|---|
| `git clone --filter=blob:none <url>` | Clone with no blob contents, fetched on demand |
| `git clone --filter=blob:limit=1m <url>` | Clone omitting blobs over 1 MB |
| `git clone --filter=tree:0 <url>` | Most aggressive — trees also fetched on demand |
| `git clone --filter=blob:none --no-checkout <url>` | Partial clone prep before sparse-checkout |
| `git fetch --filter=blob:none` | Apply/refresh a filter on fetch |
| `git count-objects -v` | Check local object counts (see what's been fetched) |
| `git clone --filter=blob:none --depth=1 <url>` | Combine partial + shallow clone |