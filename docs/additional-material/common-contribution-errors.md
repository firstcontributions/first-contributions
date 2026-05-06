# Common contribution errors (and what to do)

If you’re making your first contribution, you will eventually hit some problems—most of them are predictable. This page collects the most common beginner issues seen across git/GitHub tutorials and offers practical next steps.

> Tip: When asking for help, paste the exact error text and the command you ran.

---

## 1) `git switch` / `git checkout` errors (older Git)

### Symptom
You see something like:

- `Git: 'switch' is not a git command`
- `error: pathspec ...` (when using commands from a newer tutorial)

### What to do
- Check your Git version:
  - `git --version`
- If `switch` isn’t supported, use the compatible command:
  - `git checkout -b <branch-name>`

---

## 2) Authentication error when pushing (HTTPS)

### Symptom
You can’t push and you see an error mentioning authentication / password deprecation / token requirements.

### What to do
- If you use **HTTPS**, GitHub requires a **personal access token (PAT)** instead of a password.
- Alternatively switch your remote to **SSH**:
  - Verify current remotes: `git remote -v`
  - Set SSH URL (example):
    - `git remote set-url origin git@github.com:<your-username>/<repo>.git`

---

## 3) Permission denied / 403 / remote denied

### Symptom
- `remote: Permission to <repo> denied ...`
- `fatal: unable to access ... (403)`

### What to do
- Confirm you’re pushing to your **fork** (not the upstream repo).
- Confirm the remote URL points to your account:
  - `git remote -v`
- Common fix: make sure your `origin` remote is your fork.

---

## 4) Push rejected: non-fast-forward

### Symptom
- `rejected (non-fast-forward)`
- `updates were rejected because the tip of your current branch is behind`

### What to do
- Pull and integrate the upstream changes for your branch:
  - `git fetch`
  - Then choose either merge or rebase (follow the project’s preference).
- If you’re unsure: use **merge** first for simplicity.

---

## 5) “My PR has conflicts”

### Symptom
- GitHub reports merge conflicts when creating a PR.

### What to do
- Update your branch with the latest target branch (often `main`) and resolve conflicts locally.
- After resolving, commit the conflict fixes and push again.

---

## 6) Accidentally committed the wrong thing

### Symptom
You committed but realized:
- you forgot a file
- you misspelled the commit message
- you committed to the wrong branch

### What to do
Pick the simplest option:
- Add missing changes:
  - make changes, then `git add ...`
  - amend commit (if it’s safe): `git commit --amend`
- For commits already pushed, coordinate with your workflow (some projects prefer revert).

---

## 7) Line ending issues (CRLF vs LF)

### Symptom
- PR shows many unrelated changes
- diffs look like every line changed

### What to do
- Ensure your editor and git are configured consistently.
- You can add/change a `.gitattributes` / `.gitconfig` for line endings, then recreate the branch changes.

---

## 8) `gitignore` doesn’t seem to work

### Symptom
- Files you added to `.gitignore` still show up in `git status`.

### What to do
- `.gitignore` doesn’t affect files already tracked by git.
- For tracked files, you need to remove them from the index (without deleting locally) and commit.

---

## 9) Confused about rebase vs merge

### Quick rule
- **Merge**: safer and keeps history of how branches diverged.
- **Rebase**: rewrites commit history to make it look linear.

### What to do as a beginner
If you already shared commits to others, prefer **merge** to avoid history-rewrite surprises.

---

## 10) “I can’t find where my change is”

### Symptom
You committed but can’t see your changes in the PR.

### What to do
- Confirm you committed on the branch you pushed:
  - `git branch --show-current`
  - `git log --oneline --decorate -n 10`
- Ensure you opened the PR from the correct branch.

---

## Appendix: fastest commands to diagnose

- Show current branch: `git branch --show-current`
- Show remotes: `git remote -v`
- See recent commits: `git log --oneline --decorate -n 10`
- See what changed: `git status`


