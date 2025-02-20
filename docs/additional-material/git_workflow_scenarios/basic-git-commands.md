# 📚 Basic Git Commands for Beginners

## 🔄 1. Setup & Configuration
```bash
# Set your username
git config --global user.name "Your Name"

# Set your email
git config --global user.email "youremail@example.com"

# Check configuration settings
git config --list
```

## 📁 2. Repository Management
```bash
# Initialize a new Git repository
git init

# Clone an existing repository
git clone <repository-url>

# Check repository status
git status
```

## 💾 3. Working with Files
```bash
# Add specific file(s) to staging
git add <filename>

# Add all changes to staging
git add .

# Remove a file from staging
git reset <filename>

# Commit changes with a message
git commit -m "Your commit message"
```

## 🌐 4. Remote Repositories
```bash
# Add a remote repository
git remote add origin <repository-url>

# View all remote repositories
git remote -v

# Push changes to remote repository
git push origin <branch-name>

# Pull changes from remote repository
git pull origin <branch-name>
```

## 🌿 5. Branching & Merging
```bash
# Create a new branch
git branch <branch-name>

# Switch to a branch
git checkout <branch-name>

# Create and switch to a new branch
git checkout -b <branch-name>

# Merge a branch into the current branch
git merge <branch-name>

# Delete a branch
git branch -d <branch-name>
```

## 🐛 6. Troubleshooting
```bash
# View commit history
git log

# Undo the last commit (keep changes)
git reset --soft HEAD~1

# Discard local changes
git checkout -- <filename>

# See differences between commits
git diff
```

## 💡 Pro Tip
Use `git status` often to check the state of your working directory and staging area.

