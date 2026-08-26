# Git Submodules

`git submodule` lets you embed one Git repository inside another as a subdirectory, keeping the embedded repo's history separate while pinning it to a specific commit within the parent (superproject) repo.

## Why Use It

- Include a shared library/dependency as source, tracked at a specific version
- Keep a vendored dependency's own history intact and independently updatable
- Split a large project into smaller repos while still being able to check them out together
- Reference internal tooling or shared configs across multiple projects

## How It Works

A submodule is a reference (commit SHA) stored in the parent repo, pointing to a specific commit in another repository. The parent repo doesn't store the submodule's files or history directly — just a pointer. A `.gitmodules` file in the parent repo records the submodule's path and URL.

```
parent-repo/
├── .gitmodules          <- records path + URL of each submodule
├── src/
└── libs/
    └── shared-lib/      <- submodule: a full separate git repo, pinned to a commit
```

## Basic Commands

### Add a submodule
```bash
git submodule add <repository-url> <path>
```
Example:
```bash
git submodule add https://github.com/example/shared-lib.git libs/shared-lib
```
This clones the repo into `libs/shared-lib`, records it in `.gitmodules`, and stages the submodule reference (a specific commit) for commit in the parent repo.

### Commit the addition
```bash
git commit -m "Add shared-lib as a submodule"
```

## Cloning a Repo That Has Submodules

### Clone and initialize submodules in one step
```bash
git clone --recurse-submodules <repository-url>
```

### If already cloned without submodules
```bash
git submodule init
git submodule update
```
Or combined:
```bash
git submodule update --init
```

### Recursively (submodules within submodules)
```bash
git submodule update --init --recursive
```

## Updating Submodules

### Pull the latest changes for a submodule (per `.gitmodules` tracked branch, if set)
```bash
git submodule update --remote
```

### Update a specific submodule
```bash
git submodule update --remote libs/shared-lib
```

### Update and merge/rebase local changes in the submodule
```bash
git submodule update --remote --merge
git submodule update --remote --rebase
```

### After updating, commit the new pointer in the parent repo
```bash
git add libs/shared-lib
git commit -m "Bump shared-lib to latest"
```
Remember: the parent repo only stores a commit reference — updating the submodule's files means the *pointer* changed, and that change itself must be committed in the parent.

## Working Inside a Submodule

A submodule is a fully functional Git repo — `cd` into it and use normal Git commands:
```bash
cd libs/shared-lib
git checkout -b my-fix
# make changes
git add .
git commit -m "Fix bug in shared-lib"
git push origin my-fix
```

Then, back in the parent repo, commit the updated pointer:
```bash
cd ../..
git add libs/shared-lib
git commit -m "Point to shared-lib fix commit"
```

## Checking Status

### See submodule status (commit + whether it's dirty/out of sync)
```bash
git submodule status
```
Output:
```
 a1b2c3d libs/shared-lib (heads/main)
+e4f5g6h libs/other-lib (v2.0-3-ge4f5g6h)
```
- No prefix: submodule matches the recorded commit
- `+`: submodule's checked-out commit differs from what's recorded
- `-`: submodule not initialized
- `U`: merge conflicts in the submodule

### Run a command across all submodules
```bash
git submodule foreach 'git status'
git submodule foreach 'git checkout main && git pull'
```

## Removing a Submodule

Git has no single command for this — it's a multi-step process:
```bash
git submodule deinit -f libs/shared-lib
rm -rf .git/modules/libs/shared-lib
git rm -f libs/shared-lib
git commit -m "Remove shared-lib submodule"
```

## Common Workflows

**Set up a project with submodules from scratch:**
```bash
git clone --recurse-submodules <url>
cd project
```

**Someone else added a submodule; you pulled the parent repo:**
```bash
git pull
git submodule update --init --recursive
```

**Bump a submodule to latest and share the update:**
```bash
git submodule update --remote libs/shared-lib
git add libs/shared-lib
git commit -m "Bump shared-lib"
git push
```

**Always keep submodules current on pull (config option):**
```bash
git config submodule.recurse true
```
Once set, `git pull` will also update submodules automatically (Git 2.14+).

## Notes & Gotchas

- **Submodules point to a specific commit, not a branch.** Even if `.gitmodules` records a branch name, the actual checked-out state is a fixed commit until you explicitly run `update --remote`.
- Forgetting to commit the updated submodule pointer after making changes inside it is the most common submodule mistake — the parent repo won't reflect the update until that commit is made.
- Cloning without `--recurse-submodules` leaves submodule directories **empty** until you run `git submodule update --init`.
- Detached HEAD is the default state when a submodule is checked out via `update` — if you want to make commits inside it, check out a branch first.
- `.gitmodules` records the URL and path; the actual pinned commit is stored as a special "gitlink" entry in the parent repo's tree, not in `.gitmodules`.
- Submodules are widely considered to have a rough UX — many teams prefer alternatives like a package manager, `git subtree`, or a monorepo, depending on the use case.
- CI pipelines need explicit configuration to fetch submodules (they don't come for free) — check your CI provider's submodule/recursive-clone settings.

## Submodules vs. Alternatives

| Approach | History | Complexity | Use case |
|---|---|---|---|
| Submodule | Separate repo, own history | High | Need the dependency's own git history, independent versioning |
| `git subtree` | Merged into parent history | Medium | Want dependency code inline without extra clone/init steps |
| Package manager (npm, pip, etc.) | N/A (versioned artifact) | Low | Dependency has a proper package registry |
| Monorepo | Single shared history | Low (for this problem) | Want everything in one place, one history |

## Quick Reference

| Command | Description |
|---|---|
| `git submodule add <url> <path>` | Add a new submodule |
| `git clone --recurse-submodules <url>` | Clone parent repo + all submodules |
| `git submodule update --init --recursive` | Init and fetch submodules after a normal clone |
| `git submodule update --remote` | Pull latest commit for tracked branch of each submodule |
| `git submodule status` | Show current commit/state of each submodule |
| `git submodule foreach '<cmd>'` | Run a command in every submodule |
| `git submodule deinit -f <path>` | Deinitialize (unregister) a submodule |
| `git config submodule.recurse true` | Auto-update submodules on pull |