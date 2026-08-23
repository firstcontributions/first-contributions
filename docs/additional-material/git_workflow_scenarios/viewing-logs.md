# Viewing Logs with the Git CLI

A reference for inspecting commit history using `git log` and related commands.

## Basic Usage

```bash
git log
```
Shows commit history for the current branch: hash, author, date, and message, newest first.

## Common Flags

| Flag | Description |
|---|---|
| `-p` or `--patch` | Show the diff introduced by each commit |
| `--stat` | Show a summary of files changed and line counts |
| `-n <number>` | Limit output to the last N commits (e.g. `git log -n 5`) |
| `--oneline` | Condense each commit to a single line (short hash + message) |
| `--graph` | Draw an ASCII graph of branch/merge history |
| `--all` | Show history for all branches, not just the current one |
| `--reverse` | Show commits oldest-first |
| `--abbrev-commit` | Show shortened commit hashes |

A popular combo:
```bash
git log --oneline --graph --all --decorate
```

## Filtering Commits

**By author:**
```bash
git log --author="Ayush"
```

**By date range:**
```bash
git log --since="2 weeks ago" --until="yesterday"
git log --after="2026-01-01" --before="2026-06-01"
```

**By commit message content:**
```bash
git log --grep="fix bug"
```

**By file or path:**
```bash
git log -- path/to/file.py
```
Shows only commits that touched that file/path.

**By content change (search for a string added/removed):**
```bash
git log -S"functionName"
```

**By number of parents (merge commits only):**
```bash
git log --merges
git log --no-merges
```

## Formatting Output

Customize what's displayed with `--pretty` or `--format`:
```bash
git log --pretty=format:"%h - %an, %ar : %s"
```

Common placeholders:
| Placeholder | Meaning |
|---|---|
| `%H` | Full commit hash |
| `%h` | Abbreviated commit hash |
| `%an` | Author name |
| `%ae` | Author email |
| `%ad` | Author date |
| `%ar` | Author date, relative (e.g. "2 days ago") |
| `%s` | Subject (commit message first line) |
| `%b` | Body of commit message |

## Viewing a Specific Commit

```bash
git show <commit-hash>
```
Displays the metadata and diff for a single commit.

## Log for a Specific Branch or Range

```bash
git log branch-name
git log main..feature-branch     # commits in feature-branch not in main
git log commit1..commit2         # commits between two commits
```

## Viewing File-Level History (Line-by-Line)

```bash
git blame path/to/file.py
```
Shows who last modified each line of a file and in which commit.

## Searching Reflogs (Local History of HEAD)

```bash
git reflog
```
Useful for recovering commits after a reset or rebase — shows a log of where `HEAD` has pointed.

## Useful One-Liners

**Compact history with graph:**
```bash
git log --oneline --graph --decorate --all
```

**Commits by a file, showing diffs:**
```bash
git log -p -- path/to/file.py
```

**Count commits by author:**
```bash
git shortlog -sn
```

**Show commits between two dates in a compact format:**
```bash
git log --since="2026-01-01" --until="2026-03-01" --oneline
```