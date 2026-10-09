# Git Commands for Beginners

A simple cheat sheet of the most important Git commands, with plain-English descriptions.
Commands are ordered the way you will actually use them: **setup → start → save → branch → undo → share**.

> **Notation:** `<something>` means "replace this with your own value". Don't type the `< >` brackets.

---

## Table of Contents

1. [First-Time Setup](#1-first-time-setup)
2. [Getting Help](#2-getting-help)
3. [Starting a Repository](#3-starting-a-repository)
4. [Saving Your Work (Daily Workflow)](#4-saving-your-work-daily-workflow)
5. [Looking at What Happened](#5-looking-at-what-happened)
6. [Branches](#6-branches)
7. [Undoing Things](#7-undoing-things)
8. [Working with Remotes (GitHub, GitLab, etc.)](#8-working-with-remotes-github-gitlab-etc)
9. [Stash: Temporarily Hide Changes](#9-stash-temporarily-hide-changes)
10. [Detached HEAD State Explained](#10-detached-head-state-explained)
11. [Typical Workflow at a Glance](#11-typical-workflow-at-a-glance)
12. [Quick Tips](#12-quick-tips)

---

## 1. First-Time Setup

Do this once after installing Git. Git uses this info to label your commits.

| Command | What it does |
|---|---|
| `git config --global user.name "Your Name"` | Sets the name shown on your commits |
| `git config --global user.email "you@example.com"` | Sets the email shown on your commits |
| `git config --list` | Shows all your current Git settings |
| `git config user.name` | Shows the value of one specific setting |

---

## 2. Getting Help

| Command | What it does |
|---|---|
| `git help <command>` | Opens the manual for a command (e.g. `git help commit`) |
| `git help config` | Opens the manual for `git config` |
| `git <command> -h` | Shows a short summary of the command's options |

---

## 3. Starting a Repository

A **repository (repo)** is a project folder that Git is tracking. It contains a hidden `.git` folder where Git stores history.

| Command | What it does |
|---|---|
| `git init` | Turns the current folder into a Git repo (creates the `.git` folder). The default branch name is usually `master` unless you've configured otherwise |
| `git init --initial-branch=main` | Same as above, but names the first branch `main` |
| `git clone <url>` | Downloads a copy of an existing repo from the internet to your computer |

---

## 4. Saving Your Work (Daily Workflow)

Saving in Git is a **two-step process**:

1. **Stage** the changes you want to save (`git add`)
2. **Commit** them with a message (`git commit`)

```
Working folder  --git add-->  Staging area  --git commit-->  Repository (history)
```

| Command | What it does |
|---|---|
| `git status` | Shows which files are changed, staged, or untracked. **Use this all the time!** |
| `git add <filename>` | Stages one specific file |
| `git add .` | Stages **all** changes in the current folder |
| `git commit -m "message"` | Saves the staged changes as a snapshot with a short message describing what you did |
| `git commit --amend -m "new message"` | Fixes the message of your **last** commit (only do this before pushing) |

**Tip:** Write commit messages that say *what* and *why*, e.g. `"Fix login button not responding"` instead of `"changes"`.

---

## 5. Looking at What Happened

| Command | What it does |
|---|---|
| `git log` | Shows the full commit history |
| `git log --oneline` | Shows history in a short, one-line-per-commit format |
| `git diff` | Shows changes you've made but **not yet staged** |
| `git diff --staged` | Shows changes that are staged and ready to commit |
| `git show <commit-id>` | Shows the details and changes of a single commit |

---

## 6. Branches

A **branch** is a separate line of work. You can experiment on a branch without affecting the main code.

| Command | What it does |
|---|---|
| `git branch` | Lists all local branches (the current one has a `*`) |
| `git branch <name>` | Creates a new branch (but does not switch to it) |
| `git switch <name>` | Switches to an existing branch (modern way) |
| `git checkout <name>` | Switches to an existing branch (older way, same result) |
| `git switch -c <name>` | Creates a new branch **and** switches to it |
| `git checkout -b <name>` | Older way to create and switch in one step |
| `git branch -M <new-name>` | Renames the **current** branch (e.g. `git branch -M main`) |
| `git branch -d <name>` | Deletes a branch that has already been merged |
| `git branch -D <name>` | Force-deletes a branch, even if it is not merged |
| `git merge <name>` | Merges the named branch **into the branch you are currently on** |

---

## 7. Undoing Things

Mistakes happen. Here's how to fix them, from safest to most dangerous.

### Undo changes to files

| Command | What it does |
|---|---|
| `git restore <filename>` | Discards your unsaved changes in a file (puts it back to the last commit). **Cannot be undone!** |
| `git checkout -- <filename>` | Older way to do the same thing as above |
| `git restore --staged <filename>` | Un-stages a file (keeps your changes, just removes it from the staging area) |
| `git restore --source=<commit-id> <filename>` | Brings back a file as it looked in an older commit |

### Undo commits

| Command | What it does |
|---|---|
| `git revert <commit-id>` | Creates a **new** commit that cancels out an old one. **Safest**, and good for shared branches |
| `git reset --soft HEAD~1` | Removes the last commit but **keeps your changes staged** |
| `git reset --mixed HEAD~1` | Removes the last commit and keeps your changes, but **un-staged** (this is the default) |
| `git reset --hard HEAD~1` | Removes the last commit **and deletes your changes**. Dangerous! |

> **What is `HEAD~1`?** `HEAD` means "the commit you're on right now". `HEAD~1` means "one commit before that". `HEAD~2` means two commits back.

> **Warning:** Avoid `git reset` on commits you've already pushed. It rewrites history and can cause trouble for others. Use `git revert` instead.

### Removing and moving files

| Command | What it does |
|---|---|
| `git rm <filename>` | Deletes a file and stages the deletion |
| `git mv <old> <new>` | Renames or moves a file and stages the change |

---

## 8. Working with Remotes (GitHub, GitLab, etc.)

A **remote** is a copy of your repo hosted online. By convention, the main remote is called `origin`.

| Command | What it does |
|---|---|
| `git remote` | Lists the names of your remotes |
| `git remote -v` | Lists remotes with their URLs |
| `git remote add origin <url>` | Connects your local repo to a remote and names it `origin` |
| `git push origin <branch>` | Uploads your commits on that branch to the remote |
| `git push -u origin <branch>` | Same as above, but also remembers the link so next time you can just type `git push` |
| `git pull origin <branch>` | Downloads new commits from the remote **and** merges them into your current branch |
| `git fetch` | Downloads new commits from the remote **without** merging (lets you look first) |

**Pull vs Fetch:** `git pull` = `git fetch` + `git merge`. Fetch is the "look but don't touch" version.

---

## 9. Stash: Temporarily Hide Changes

Useful when you're in the middle of something but need to switch branches quickly.

| Command | What it does |
|---|---|
| `git stash` | Hides your uncommitted changes and gives you a clean folder |
| `git stash list` | Shows all your stashes |
| `git stash pop` | Brings back the most recent stash and removes it from the list |

---

## 10. Detached HEAD State Explained

Normally, `HEAD` points to a **branch** (like `main`), and the branch points to your latest commit.

A **detached HEAD** happens when `HEAD` points directly to a **specific commit** instead of a branch. You'll see it if you run something like:

```bash
git checkout <commit-id>
```

**Why it matters:** Any commits you make in this state don't belong to any branch, so they can be lost when you switch away.

**Just looking around?** That's fine. When you're done, go back with:

```bash
git switch main
```

**Made changes you want to keep?** Create a branch right where you are:

```bash
git switch -c my-new-branch
```

---

## 11. Typical Workflow at a Glance

### Starting a brand new project

```bash
git init --initial-branch=main      # 1. Start a repo
git add .                           # 2. Stage your files
git commit -m "Initial commit"      # 3. Save the first snapshot
git remote add origin <url>         # 4. Connect to GitHub
git push -u origin main             # 5. Upload it
```

### Contributing to an open-source project

```bash
git clone <url>                     # 1. Download the project
git switch -c my-feature            # 2. Make your own branch
# ... edit files ...
git status                          # 3. See what changed
git add .                           # 4. Stage changes
git commit -m "Add my feature"      # 5. Save changes
git push -u origin my-feature       # 6. Upload your branch, then open a Pull Request
```

---

## 12. Quick Tips

- Run **`git status`** often. It tells you what's going on and usually suggests the next command.
- **Commit small and often.** Small commits are easier to understand and undo.
- **Never** run `git reset --hard` or `git restore` unless you are sure. They permanently discard work.
- Create a **`.gitignore`** file to tell Git which files to skip (e.g. `node_modules/`, `.env`, `*.log`).
- Stuck? Run `git help <command>` or search the error message online. Everyone has been there.

---

*Found a mistake or want to add a command? Contributions are welcome!*
