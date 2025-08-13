# GitHub Windows VS Code Tutorial

This guide will help you use GitHub with Visual Studio Code (VS Code) on Windows, covering setup, cloning, committing, pushing, and creating pull requests. It is designed for beginners and those new to open source.

---

## Prerequisites
- **VS Code**: Download and install from [code.visualstudio.com](https://code.visualstudio.com/)
- **Git**: Download and install from [git-scm.com](https://git-scm.com/)
- **GitHub Account**: Sign up at [github.com](https://github.com/)

---

## 1. Install the GitHub Pull Requests and Issues Extension
- Open VS Code
- Go to Extensions (Ctrl+Shift+X)
- Search for `GitHub Pull Requests and Issues` and install it

---

## 2. Clone a Repository from GitHub
1. Copy the repository URL from GitHub (HTTPS or SSH)
2. In VS Code, press `Ctrl+Shift+P` and type `Git: Clone`
3. Paste the URL and select a folder to save the project
4. Open the cloned folder in VS Code

---

## 3. Make Changes and Commit
- Edit files as needed
- The Source Control icon (left sidebar) shows changed files
- Stage changes: Click the `+` next to files or `Stage All Changes`
- Enter a commit message and click the checkmark (✔) to commit

---

## 4. Push Changes to GitHub
- Click the `...` menu in Source Control and select `Push`
- Or use the blue bar at the bottom if prompted
- If this is your first push, VS Code may ask you to sign in to GitHub

---

## 5. Create a New Branch (Recommended for Contributions)
- Click the branch name in the bottom left
- Select `Create new branch`
- Name your branch (e.g., `add-your-name`)
- Make your changes, commit, and push as above

---

## 6. Create a Pull Request
- After pushing your branch, VS Code will show a prompt to create a pull request
- Or, go to the repository on GitHub.com and click `Compare & pull request`
- Add a description and submit the pull request

---

## 7. Syncing and Pulling Updates
- To get the latest changes from the main repository, click `...` in Source Control and select `Pull`
- If you forked the repo, add the original as an `upstream` remote and pull from it:
  - Open Terminal in VS Code
  - `git remote add upstream https://github.com/original-owner/repo.git`
  - `git fetch upstream`
  - `git merge upstream/main`

---

## 8. Resolving Merge Conflicts
- VS Code highlights conflicts in files
- Use the inline options to accept current, incoming, or both changes
- After resolving, stage and commit the changes

---

## 9. Useful VS Code Git Shortcuts
- `Ctrl+Shift+G`: Open Source Control
- `Ctrl+Shift+P`: Command Palette (for all Git commands)
- `F1`: Command Palette (alternative)

---

## 10. Tips
- Always pull the latest changes before starting new work
- Use branches for each feature or fix
- Write clear commit messages
- Use the Issues tab in VS Code to track and discuss issues

---

## Resources
- [VS Code Docs: Version Control](https://code.visualstudio.com/docs/editor/versioncontrol)
- [GitHub Docs: Using GitHub with Visual Studio Code](https://docs.github.com/en/get-started/getting-started-with-git/using-git-in-visual-studio-code)
- [First Contributions Guide](https://github.com/firstcontributions/first-contributions)

---

If you follow these steps, you'll be able to contribute to any GitHub project using VS Code on Windows like a pro!
