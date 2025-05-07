# Common Git Errors and How to Fix Them

This guide lists frequent Git errors beginners encounter and how to fix them.

---

### ❌ Error: `fatal: not a git repository (or any of the parent directories): .git`

**What it means:**  
You're trying to use Git in a folder that isn't initialized as a Git repository.

**How to fix:**
1. Make sure you're in the correct project folder.
2. Run `git init` to initialize a Git repository, or navigate to a folder that already has one.

```bash
cd your-project-folder
git init
