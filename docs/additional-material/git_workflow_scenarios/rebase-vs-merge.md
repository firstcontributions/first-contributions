# Rebase vs Merge

When contributing to open-source projects, it’s important to understand how to integrate your changes cleanly.  
Two common ways to bring updates from one branch into another are **merge** and **rebase**.


## What Is Rebase?

**Rebasing** replays your commits from one branch on top of another — effectively moving your work to start from the tip of another branch.  
This creates a **linear and clean commit history** without merge commits.

### Example

```bash
# Switch to your feature branch
git switch feature_branch

# Rebase your feature branch on top of main
git rebase main
```

Alternatively, 
```bash
git checkout <your-branch> 
git rebase <branch-you-want-to-copy-changes-from>
```
> `git switch <branch>` and `git checkout <branch>` both switch branches, but `switch` is newer and more user-friendly.

---
Both merge and rebase are used to integrate changes from one branch into another. 

**Merging** combines the histories of two branches by creating a new **merge commit**. It **preserves the true sequence of events**, showing exactly how and when branches diverged and rejoined. 

```bash
*   b576e33 (HEAD -> main) Merge branch 'feature' into main
|\
| * 22c5476 C4
| * b1a9c33 C3
* | f2a4d33 C2 (branch - 'feature')
|/
* c9f0a10 C1 (main)
```

**Rebasing**, on the other hand, **reapplies your commits** on top of another branch’s latest state. This effectively **keeps the commit history linear and clean**, as if all your work happened sequentially after the commits on the target branch. 

```bash
* e4d2b3c (HEAD -> feature) C4
* 3f68a71 C3 (branch - 'feature')
* f2a4d33 C2
* c9f0a10 C1 (main)
```

``` bash
# This command will display an ASCII-style commit graph directly in your terminal.
# It shows commit history in a tree-like structure.
git log --graph --oneline --all
```

## Merge vs Rebase

| **Feature**     | **Merge**                                      | **Rebase**                                  |
|------------------|------------------------------------------------|---------------------------------------------|
| **History**      | Preserves the true chronological history       | Creates a linear history                    |
| **Extra Commits**| Adds an extra merge commit                     | No extra commits                            |
| **Readability**  | Can become cluttered with merge commits        | Easier to read and follow                   |
| **Use Case**     | Ideal for public branches (e.g., `main`)       | Ideal for personal or feature branches      |


## Important Rule
**Never rebase a public/shared branch (like main).**
Rebasing rewrites commit history, which can cause problems for collaborators who have already based work on those commits.
Always rebase your personal or feature branch **onto main**, not the other way around.

> If the branch is shared — use merge.
> If the branch is personal — use rebase.


## Git Configuration Options
You can tell Git whether to merge or rebase when pulling updates:

```bash
# Always merge (default behavior)
git config pull.rebase false

# Always rebase by default (recommended for linear history)
git config --global pull.rebase true
```

**NOTE: Setting the global option ensures your local branches stay clean and linear without unnecessary merge commits.**

