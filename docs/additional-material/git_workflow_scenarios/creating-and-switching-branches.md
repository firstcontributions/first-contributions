# Creating and Switching Branches

## What is a branch?

A branch in Git is an independent line of development. It allows you to work on features or fixes without affecting the main codebase.

## Creating a new branch

### Traditional method
```bash
git branch feature-branch-name
git checkout feature-branch-name
```

### Quick method (recommended)
```bash
git checkout -b feature-branch-name
```

### Modern method (Git 2.23+)
```bash
git switch -c feature-branch-name
```

## Branch naming conventions

```bash
# Feature branches
git checkout -b feature/add-login

# Bug fixes
git checkout -b fix/header-bug

# Hotfixes
git checkout -b hotfix/security-patch
```

## Viewing branches

```bash
git branch              # List local branches
git branch -a           # List all branches (local and remote)
git branch -r           # List remote branches only
```

## Switching branches

```bash
git checkout branch-name    # Old method
git switch branch-name      # New method (Git 2.23+)
git switch -                # Switch to previous branch
```

## Creating branch on GitHub

### Via web interface
1. Go to your repository
2. Click branch dropdown (shows "main")
3. Type new branch name
4. Click "Create branch"

### Pushing local branch to GitHub
```bash
git push -u origin feature-branch-name
```

## Common workflow

```bash
# 1. Start from main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/new-feature

# 3. Make changes and commit
git add .
git commit -m "Add new feature"

# 4. Push to GitHub
git push -u origin feature/new-feature

# 5. Create pull request on GitHub

# 6. After merge, clean up
git checkout main
git pull origin main
git branch -d feature/new-feature
```

## Best practices

- Keep branches focused on single features or fixes
- Use descriptive names
- Always work on a branch, never directly on main
- Delete branches after merging
- Keep branches updated with main regularly

