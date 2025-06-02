# Git Auto Commit and Push Scripts

This document provides scripts for automating the process of committing and pushing changes to a Git repository. Scripts are available for both Windows (PowerShell) and Bash.

---

## Windows (PowerShell)

The following PowerShell function automates the process of adding, committing, and pushing changes to the current branch. It uses a random commit message from a predefined list.

```powershell
function Git-Auto-Commit-Push() {
    $messages=@(
        "Update scripts",
        "Fix bugs",
        "Improve performance",
        "Add new features",
        "Refactor code",
        "Update documentation",
        "Clean up code",
        "Update dependencies",
        "Optimize assets",
        "Enhance security",
        "Improve UI/UX",
        "Update configuration"
    )
    $randomMessage = Get-Random -InputObject $messages
    git add .
    git commit -m "$randomMessage"

    $branchName = git rev-parse --abbrev-ref HEAD
    if (-not (git branch --list "origin/$branchName")) {
        git push --set-upstream origin $branchName
    }
    else {
        git push
    }
}

#!/bin/bash

function git_auto_commit_push() {
    messages=(
        "Update scripts"
        "Fix bugs"
        "Improve performance"
        "Add new features"
        "Refactor code"
        "Update documentation"
        "Clean up code"
        "Update dependencies"
        "Optimize assets"
        "Enhance security"
        "Improve UI/UX"
        "Update configuration"
    )
    random_message=${messages[$RANDOM % ${#messages[@]}]}
    git add .
    git commit -m "$random_message"

    branch_name=$(git rev-parse --abbrev-ref HEAD)
    if ! git ls-remote --exit-code --heads origin "$branch_name" &>/dev/null; then
        git push --set-upstream origin "$branch_name"
    else
        git push
    fi
}

Usage

Save the script to a file, e.g., git-auto-commit-push.sh.
Make the script executable: chmod +x git-auto-commit-push.sh.
Run the script in your Git repository: ./git-auto-commit-push.sh.
Both scripts simplify the process of committing and pushing changes, making it easier to manage your Git workflow. ```