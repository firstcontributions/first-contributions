# GitHub CLI Advanced Usage

## What is GitHub CLI?

GitHub CLI (`gh`) is a command-line tool that brings GitHub functionality to your terminal.

## Installation

```bash
# macOS
brew install gh

# Windows
winget install GitHub.cli

# Linux
sudo apt install gh  # Debian/Ubuntu
```

## Authentication

```bash
gh auth login
```

## Pull Request commands

```bash
# Create PR
gh pr create --title "Add feature" --body "Description"

# Create PR interactively
gh pr create

# List PRs
gh pr list

# View PR details
gh pr view 123

# Checkout PR
gh pr checkout 123

# Review PR
gh pr review 123 --approve
gh pr review 123 --request-changes --body "Needs fixes"

# Merge PR
gh pr merge 123 --squash
gh pr merge 123 --merge
gh pr merge 123 --rebase
```

## Issue commands

```bash
# Create issue
gh issue create --title "Bug report" --body "Description"

# List issues
gh issue list

# View issue
gh issue view 123

# Close issue
gh issue close 123

# Reopen issue
gh issue reopen 123
```

## Repository commands

```bash
# Clone repository
gh repo clone owner/repo

# Create repository
gh repo create my-project --public

# View repository
gh repo view owner/repo

# Fork repository
gh repo fork owner/repo
```

## Workflow commands

```bash
# List workflows
gh workflow list

# View workflow runs
gh run list

# View specific run
gh run view 123456

# Re-run workflow
gh run rerun 123456

# Watch workflow run
gh run watch
```

## Advanced examples

```bash
# Create PR with auto-merge
gh pr create --fill
gh pr merge --auto --squash

# Approve and merge in one go
gh pr review 123 --approve && gh pr merge 123 --squash

# List open PRs by author
gh pr list --author @me --state open

# View PR diff
gh pr diff 123

# Create issue from template
gh issue create --template bug_report.md
```

## Best practices

- Use `--fill` for quick PR creation from commits
- Combine commands with `&&` for workflows
- Use aliases for common commands
- Integrate with scripts for automation

