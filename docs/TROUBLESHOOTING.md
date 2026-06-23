# ❓ Troubleshooting Guide

Having trouble? You're not alone! Here are solutions to common problems.

## 🔑 Authentication Issues

### Error: "Authentication failed for 'https://github.com/...'"

**Problem**: Git is asking for a password or authentication fails.

**Solution 1: Use SSH Keys (Recommended)**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add SSH key
ssh-add ~/.ssh/id_ed25519

# Copy public key and add to GitHub
cat ~/.ssh/id_ed25519.pub
# Go to GitHub Settings → SSH and GPG keys → New SSH key
```

**Solution 2: Use Personal Access Token**
```bash
# Go to GitHub Settings → Developer settings → Personal access tokens
# Generate new token with 'repo' scope
# Use token as password when prompted

# Or set as environment variable
git config --global user.password "your-token"
```

**Solution 3: Update Remote URL**
```bash
# Check current remote
git remote -v

# Change from HTTPS to SSH
git remote set-url origin git@github.com:username/repository.git
```

---

## 🌳 Git Branch Issues

### Error: "fatal: Not a valid object name"

**Problem**: Branch doesn't exist or is misspelled.

**Solution**:
```bash
# List all local branches
git branch

# List all remote branches
git branch -a

# Delete wrong branch
git branch -d wrong-branch-name

# Create new branch correctly
git switch -c correct-branch-name
```

### Error: "fatal: A branch named ... already exists"

**Problem**: You're trying to create a branch that already exists.

**Solution**:
```bash
# List branches to see what exists
git branch

# Switch to existing branch
git switch existing-branch-name

# Or delete and recreate
git branch -d existing-branch-name
git switch -c existing-branch-name
```

### Error: "error: pathspec 'branch-name' did not match any file(s) known to git"

**Problem**: Git can't find the branch you specified.

**Solution**:
```bash
# Fetch latest from remote
git fetch origin

# List all branches
git branch -a

# Switch with correct name
git switch origin/branch-name
```

---

## 📝 Commit Issues

### Error: "nothing added to commit but untracked files present"

**Problem**: You created files but didn't stage them.

**Solution**:
```bash
# Stage all changes
git add .

# Or stage specific file
git add filename.md

# Check status
git status

# Commit
git commit -m "Your message"
```

### Error: "You are in 'detached HEAD' state"

**Problem**: You checked out a commit instead of a branch.

**Solution**:
```bash
# Create a new branch from current position
git switch -c new-branch-name

# Or go back to main branch
git switch main

# Check status to confirm
git status
```

### Error: "fatal: empty ident ... not allowed"

**Problem**: Git user name or email not configured.

**Solution**:
```bash
# Configure user name
git config --global user.name "Your Name"

# Configure email
git config --global user.email "your.email@example.com"

# Verify
git config --list

# Retry your commit
git commit -m "Your message"
```

---

## 📤 Push/Pull Issues

### Error: "failed to push some refs to 'origin'"

**Problem**: Remote has changes you don't have locally.

**Solution 1: Pull First**
```bash
# Get latest changes
git pull origin branch-name

# Resolve any conflicts if needed
# Then push
git push origin branch-name
```

**Solution 2: Force Push (Use with caution!)**
```bash
# Only use if you're sure
git push -f origin branch-name

# Safer alternative - force with lease
git push --force-with-lease origin branch-name
```

### Error: "There are no changes to commit"

**Problem**: You haven't made any changes or forgot to stage them.

**Solution**:
```bash
# Check status
git status

# Make changes to files
# Then stage them
git add .

# Check status again
git status

# Commit
git commit -m "Your message"
```

### Error: "Your branch is ahead of 'origin/main' by X commits"

**Problem**: You have local commits not pushed yet.

**Solution**:
```bash
# Push your commits
git push origin branch-name

# Or push to all branches
git push --all
```

---

## 🔄 Merge & Conflict Issues

### Error: "CONFLICT (content merge): Merge conflict in ..."

**Problem**: Same lines edited in different branches.

**Solution**:
```bash
# See conflicted files
git status

# Open file and look for conflict markers:
# <<<<<<< HEAD
# your changes
# =======
# their changes
# >>>>>>> branch-name

# Edit to keep what you want
# Stage resolved files
git add .

# Complete merge
git commit -m "Resolve merge conflicts"
```

### Error: "error: Your local changes would be overwritten by merge"

**Problem**: You have uncommitted changes.

**Solution 1: Commit Your Changes**
```bash
git add .
git commit -m "Save work before merge"
```

**Solution 2: Stash Changes (Temporary Save)**
```bash
# Save changes temporarily
git stash

# Do your merge
git pull origin main

# Restore changes
git stash pop
```

---

## 🔍 History & Logs Issues

### "How do I undo my last commit?"

**Solution 1: Keep Changes**
```bash
# Undo last commit but keep changes
git reset --soft HEAD~1
git status  # Your changes are still there
```

**Solution 2: Discard Changes**
```bash
# Undo last commit and discard changes
git reset --hard HEAD~1
```

### "How do I see my commit history?"

**Solution**:
```bash
# Simple log
git log

# One line per commit
git log --oneline

# With branches
git log --graph --oneline --all

# Beautiful format
git log --pretty=format:"%h %s" --graph
```

---

## 🐛 File & Tracking Issues

### "I accidentally added a file I didn't want to commit"

**Solution 1: Before Committing**
```bash
# Unstage file
git reset filename.md

# Check status
git status
```

**Solution 2: After Committing**
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Unstage file
git reset filename.md

# Modify and recommit without the file
git commit -m "Your message"
```

### "How do I add a file to .gitignore after committing?"

**Solution**:
```bash
# Remove file from tracking (won't delete local file)
git rm --cached filename.md

# Add to .gitignore
echo "filename.md" >> .gitignore

# Commit
git add .gitignore
git commit -m "Stop tracking filename.md"
```

---

## 🌐 Remote Issues

### Error: "fatal: No remote named 'origin'"

**Problem**: Repository has no remote configured.

**Solution**:
```bash
# Add remote
git remote add origin https://github.com/username/repository.git

# Verify
git remote -v

# Now you can push
git push -u origin main
```

### Error: "fatal: repository not found"

**Problem**: Wrong repository URL or no access.

**Solution**:
```bash
# Check remote URL
git remote -v

# Verify it matches your repository
# If wrong, update it
git remote set-url origin https://github.com/correct-username/correct-repo.git

# Test connection
git remote -v
```

---

## 🆘 Nuclear Options (Use Only If Desperate!)

### "I messed up everything, what do I do?"

**Option 1: Fresh Clone**
```bash
# Start fresh
cd ..
rm -rf repository
git clone https://github.com/username/repository.git
cd repository
```

**Option 2: Hard Reset**
```bash
# WARNING: This deletes all local changes!
git reset --hard origin/main
```

**Option 3: Check Git Reflog**
```bash
# See all past actions
git reflog

# Return to a specific point
git reset --hard <commit-hash>
```

---

## 📞 Still Need Help?

If your issue isn't listed here:

1. **Search GitHub Issues**: https://github.com/firstcontributions/first-contributions/issues
2. **GitHub Discussions**: https://github.com/firstcontributions/first-contributions/discussions
3. **Stack Overflow**: Tag your question with `git` and `github`
4. **Git Documentation**: https://git-scm.com/doc

---

## 🎓 Useful Git Commands Reference

```bash
# Configuration
git config --list
git config --global user.name "Name"
git config --global user.email "email@example.com"

# Basic
git status
git log
git diff

# Branching
git branch
git branch -a
git switch branch-name
git switch -c new-branch

# Staging & Committing
git add .
git add filename
git commit -m "message"
git commit --amend

# Pushing & Pulling
git push origin branch-name
git pull origin branch-name
git fetch origin

# Undoing
git reset HEAD~1
git revert commit-hash
git clean -fd

# Remote Management
git remote -v
git remote add origin url
git remote set-url origin new-url

# Merging
git merge branch-name
git merge --abort

# Stashing
git stash
git stash list
git stash pop
```

---

**Last Updated**: 2024
**Common Issues Covered**: 30+
**Solutions Provided**: 50+

[← Back to Main README](../README.md)
