# Git & GitHub Quick Reference

## Essential Git Commands

### Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Clone & Create Branch
```bash
git clone <repository-url>
cd <repository-name>
git checkout -b <branch-name>
```

### Commit & Push
```bash
git add .                           # Stage all changes
git add <filename>                  # Stage specific file
git commit -m "Clear message"       # Commit with message
git push origin <branch-name>       # Push to GitHub
```

### Update Your Branch
```bash
git pull origin main                # Fetch latest changes
git fetch upstream                  # Get upstream updates
git rebase upstream/main            # Apply latest changes
```

### View Changes
```bash
git status                          # See what changed
git diff                            # See differences
git log --oneline                   # See commit history
```

## GitHub Workflow

### 1. Fork the Repository
- Click **Fork** button on GitHub (creates your copy)

### 2. Clone to Your Machine
```bash
git clone https://github.com/<YOUR-USERNAME>/<repo>.git
cd <repo>
```

### 3. Add Upstream Remote
```bash
git remote add upstream <original-repo-url>
git remote -v                       # Verify both origin & upstream
```

### 4. Create Feature Branch
```bash
git checkout -b fix/issue-123       # Use descriptive names
```

### 5. Make Changes
- Edit files
- Test your changes locally
- Commit with clear messages

### 6. Push to Your Fork
```bash
git push origin <branch-name>
```

### 7. Open Pull Request
- Go to GitHub → Your fork
- Click **Compare & pull request**
- Add title & description
- Reference issue if applicable: "Closes #123"
- Click **Create pull request**

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Merge conflict | Run `git status` to see conflicts. Edit files, then `git add` and `git commit` |
| Wrong branch | `git branch -a` to see all, `git checkout <branch>` to switch |
| Need to undo commit | `git revert <commit-hash>` or `git reset HEAD~1` |
| Push rejected | Run `git pull origin <branch>` first, then `git push` |
| Lost commits | `git reflog` shows all actions, use `git reset --hard <hash>` |

## Commit Message Tips
✅ **Good**: `fix: resolve navigation bug in mobile menu`  
✅ **Good**: `docs: add setup instructions`  
✅ **Good**: `feat: add dark mode toggle`  
❌ **Bad**: `fixed stuff`  
❌ **Bad**: `update`

## PR Review Checklist
- [ ] Code follows project style guide
- [ ] Changes tested locally
- [ ] Commit messages are clear
- [ ] No unnecessary files committed
- [ ] PR description explains the change
- [ ] Linked to related issues

## Useful Links
- [GitHub Docs](https://docs.github.com)
- [Git Official Docs](https://git-scm.com/doc)
- [Git Workflow Scenarios](./additional-material/git_workflow_scenarios/)
- [Main README](../README.md)

---
**Need help?** Check our [Troubleshooting Guide](./troubleshooting.md) or ask in discussions!
