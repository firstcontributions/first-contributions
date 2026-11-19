# Common Git Errors and How to Fix Them

Git errors are a normal part of working with Git and GitHub. Most errors provide useful information about what went wrong.

This guide covers some of the most common Git errors beginners may encounter and explains how to troubleshoot them.

---

## Before Troubleshooting

When you encounter a Git error, start with these commands:

```bash
git status
git branch --show-current
git remote -v
```

- `git status` — Shows the current state of your repository.
- `git branch --show-current` — Shows the branch you are currently on.
- `git remote -v` — Shows the remote repositories configured for your project.

These commands help you understand what is happening before making any changes.

---

## 1. `non-fast-forward`

### Error

```text
! [rejected] main -> main (non-fast-forward)
error: failed to push some refs
```

### Why does this happen?

The remote branch contains changes that your local branch does not have.

### Fix

First, fetch the latest changes:

```bash
git fetch origin
```

Then update your branch:

```bash
git rebase origin/main
```

Finally, push your changes:

```bash
git push
```

If conflicts occur, resolve them before continuing.

> **Tip:** Avoid `git push --force` unless you understand why it is required. If force-pushing is necessary, prefer `git push --force-with-lease`.

---

## 2. `nothing to commit, working tree clean`

### Message

```text
nothing to commit, working tree clean
```

### Why does this happen?

Git cannot find any new changes to commit.

This usually means:

- You have not changed any files.
- Your changes were already committed.
- You edited a different file.
- Your changes were discarded.
- The file is ignored by Git.

### Check

```bash
git status
```

If you expected changes, make sure the file is saved and that you are working in the correct repository.

You can also check your recent commits:

```bash
git log --oneline -5
```

---

## 3. `not a git repository`

### Error

```text
fatal: not a git repository
```

### Why does this happen?

You are running a Git command outside a Git repository.

### Fix

Navigate to your project:

```bash
cd path/to/your-project
```

Then run:

```bash
git status
```

For example:

```bash
cd ~/Desktop/first-contributions
git status
```

> **Note:** Do not delete the `.git` directory unless you intentionally want to remove Git tracking from the project.

---

## 4. `remote origin already exists`

### Error

```text
error: remote origin already exists.
```

### Why does this happen?

A remote named `origin` is already configured.

### Check the remote

```bash
git remote -v
```

If the URL is correct, you do not need to add it again.

If the URL is incorrect, change it:

```bash
git remote set-url origin <repository-url>
```

Then verify:

```bash
git remote -v
```

---

## 5. `Permission denied (publickey)`

### Error

```text
Permission denied (publickey).
fatal: Could not read from remote repository.
```

### Why does this happen?

GitHub could not authenticate your SSH connection.

### Check your remote

```bash
git remote -v
```

An SSH remote usually looks like:

```text
git@github.com:username/repository.git
```

### Test your SSH connection

```bash
ssh -T git@github.com
```

If authentication fails, make sure your SSH key is configured and that your public key has been added to your GitHub account.

> **Security:** Never share your private SSH key.

---

## 6. Merge Conflicts

### What is a merge conflict?

A merge conflict happens when Git cannot automatically combine changes from different branches.

For example, two branches may modify the same part of a file.

Git may show:

```text
<<<<<<< HEAD
Your changes
=======
Changes from another branch
>>>>>>> main
```

### How to resolve it

1. Open the conflicted file.
2. Decide which changes should remain.
3. Remove the conflict markers.
4. Save the file.

Then stage the resolved file:

```bash
git add <file-name>
```

If you were performing a merge:

```bash
git commit
```

If you were performing a rebase:

```bash
git rebase --continue
```

### Cancel a merge

```bash
git merge --abort
```

### Cancel a rebase

```bash
git rebase --abort
```

> **Tip:** Always run `git status` during a conflict to see which files still need to be resolved.

---

## 7. `git: command not found`

### Error

```text
git: command not found
```

### Why does this happen?

Git is either not installed or your system cannot find the Git executable.

### Check

```bash
git --version
```

If the command is not recognized, install Git for your operating system and try again.

---

## 8. Authentication Failed

### Error

```text
fatal: Authentication failed
```

### Why does this happen?

GitHub does not use your normal GitHub account password for Git operations over HTTPS.

GitHub supports authentication methods such as:

- GitHub CLI
- Personal access tokens
- SSH
- Credential managers

### Using GitHub CLI

```bash
gh auth login
```

Follow the prompts to authenticate your GitHub account.

### Using a Personal Access Token

If you use HTTPS and Git asks for a password, use your personal access token instead.

> **Security:** Treat personal access tokens like passwords. Never commit or share them.

---

## 9. `src refspec ... does not match any`

### Error

```text
error: src refspec main does not match any
```

### Why does this happen?

Git cannot find the branch you are trying to push.

This can happen when:

- The branch name is incorrect.
- The branch does not exist.
- The repository does not have any commits yet.

### Check your branch

```bash
git branch --show-current
```

Then push the correct branch:

```bash
git push -u origin <branch-name>
```

For example:

```bash
git push -u origin docs-common-git-errors
```

---

## 10. `Your branch is ahead of 'origin/main'`

### Message

```text
Your branch is ahead of 'origin/main' by 1 commit.
```

### What does it mean?

Your local branch contains commits that have not been pushed to the remote repository.

### Fix

Push your commits:

```bash
git push
```

After a successful push, your local and remote branches should be synchronized.

---

## 11. `Your branch is behind 'origin/main'`

### Message

```text
Your branch is behind 'origin/main' by several commits.
```

### What does it mean?

The remote branch contains commits that your local branch does not have.

### Fix

Fetch the latest changes:

```bash
git fetch origin
```

Then update your branch:

```bash
git pull --rebase
```

If conflicts occur, resolve them and run:

```bash
git add <resolved-file>
git rebase --continue
```

If you want to cancel the rebase:

```bash
git rebase --abort
```

---

## 12. `Please tell me who you are`

### Error

```text
Author identity unknown

*** Please tell me who you are.
```

### Why does this happen?

Git does not know which name and email address should be associated with your commits.

### Fix

Set your name:

```bash
git config --global user.name "Your Name"
```

Set your email:

```bash
git config --global user.email "your-email@example.com"
```

Check your configuration:

```bash
git config --global --list
```

> **Tip:** Use an email address associated with your GitHub account if you want your commits to be attributed to your GitHub profile.

---

## 13. `Your local changes would be overwritten`

### Error

```text
Your local changes to the following files would be overwritten
```

### Why does this happen?

You have uncommitted changes that would be overwritten by another Git operation.

### First, check your changes

```bash
git status
```

### Option 1: Keep your changes

Commit them:

```bash
git add .
git commit -m "Save local changes"
```

### Option 2: Temporarily save your changes

Use Git stash:

```bash
git stash
```

Perform your Git operation and then restore your changes:

```bash
git stash pop
```

### Option 3: Discard your changes

Only do this if you are certain you do not need them:

```bash
git restore <file-name>
```

> **Warning:** Discarding uncommitted changes can permanently remove your work.

---

# Useful Git Commands and Purpose

`git status` : Check repository status 
`git branch` : List branches 
`git branch --show-current` : Show current branch 
`git remote -v` : Show remote URLs 
`git log --oneline` : View recent commits 
`git diff` : View unstaged changes 
`git diff --staged` : View staged changes 
`git fetch` : Get information about remote changes 
`git pull` : Fetch and integrate remote changes 
`git push` : Upload commits 
`git stash` : Temporarily save uncommitted changes
`git restore` : Restore a file 

---

# Be Careful With Destructive Commands

Some Git commands can permanently remove work.

Be careful with:

```bash
git reset --hard
git clean
git restore
git push --force
```

Before using a destructive command, make sure you understand what it will do.

When force-pushing is genuinely necessary, prefer:

```bash
git push --force-with-lease
```

over:

```bash
git push --force
```

---

# Simple Troubleshooting Workflow

When you encounter a Git error:

```text
              Git Error
                  │
                  ▼
             git status
                  │
                  ▼
       Check current branch
                  │
                  ▼
         Check remote URL
                  │
                  ▼
       Read the full error
                  │
                  ▼
        Identify the cause
                  │
                  ▼
           Apply the fix
                  │
                  ▼
            git status
                  │
                  ▼
          Test the result
```

Start with:

```bash
git status
git branch --show-current
git remote -v
```

These commands provide useful information without modifying your repository.

---

# Final Tip

Git errors are a normal part of learning Git.

Instead of blindly copying commands, try to understand:

1. What is Git telling me?
2. Which branch am I on?
3. What changed locally?
4. What changed remotely?
5. Am I trying to push, pull, merge, rebase, or authenticate?

Understanding the cause of an error will make it much easier to solve similar problems in the future.

---

## Further Reading

- [Git Documentation](https://git-scm.com/docs)
- [GitHub Authentication Documentation](https://docs.github.com/en/authentication)
- [GitHub SSH Documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)