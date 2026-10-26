# Execute: Clone and Run a Project on Your Own Machine

This guide takes you from "I found a project on GitHub" to "it's running on my computer."
You can use the same steps for almost any project you contribute to.

## Prerequisites

- A [GitHub account](https://github.com/join)
- [Git](https://git-scm.com/downloads) installed. Check with:
  ```bash
  git --version
  ```
- A code editor, such as [VS Code](https://code.visualstudio.com/)
- A terminal (Terminal on macOS/Linux, Git Bash or PowerShell on Windows)

## Step 1: Fork the repository

A fork is your own copy of the project on GitHub.

1. Open the project's GitHub page.
2. Click **Fork** in the top-right corner.
3. GitHub creates a copy under your account: `github.com/<your-username>/<repo-name>`.

## Step 2: Clone your fork

Cloning downloads your fork to your computer.

```bash
git clone https://github.com/<your-username>/<repo-name>.git
```

Move into the project folder:

```bash
cd <repo-name>
```

> Make sure you clone **your fork**, not the original repository.

## Step 3: Look around

Open the folder in your editor and read the `README.md` first. It usually explains how to run the project.

```bash
code .
```

See `context.md` for an explanation of what each file and folder is for.

## Step 4: Create a branch

Never work directly on `main`. Make a branch for your change:

```bash
git checkout -b add-your-name
```

Use a short, descriptive branch name.

## Step 5: Make your change

Edit the files you need to. For First Contributions, that means adding your name to `Contributors.md`.

Check what changed:

```bash
git status
git diff
```

## Step 6: Commit your change

```bash
git add Contributors.md
git commit -m "Add <your-name> to Contributors list"
```

## Step 7: Push to your fork

```bash
git push origin add-your-name
```

## Step 8: Open a Pull Request

1. Go to your fork on GitHub.
2. Click **Compare & pull request**.
3. Add a clear title and short description.
4. Click **Create pull request**.

The maintainers will review it. Once it's merged, you're an open source contributor.

## Running a project with code

If the project has code (not just docs), also do this after cloning:

| Step | What to do | Example |
|------|-----------|---------|
| Install dependencies | Look for `package.json`, `requirements.txt`, etc. | `npm install` or `pip install -r requirements.txt` |
| Set up environment | Copy the example env file and fill it in | `cp .env.example .env` |
| Start the project | Check the README or the `scripts` section | `npm start` or `python main.py` |

## Keeping your fork up to date

```bash
git remote add upstream https://github.com/<original-owner>/<repo-name>.git
git fetch upstream
git checkout main
git merge upstream/main
```

## Troubleshooting

- **`git: command not found`**: Install Git and restart your terminal.
- **Permission denied when pushing**: Make sure you cloned your own fork and are signed in to GitHub.
- **Merge conflicts**: Open the conflicted files, keep the correct lines, remove the `<<<<<<<` markers, then `git add` and `git commit`.
- **Pushed to the wrong branch**: No worries. Create a new branch from your current one and push that.
- **Stuck?** Ask in the project's Issues or Discussions. Everyone was a beginner once.