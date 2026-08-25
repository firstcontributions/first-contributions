# Git Bisect

`git bisect` uses binary search across your commit history to find the exact commit that introduced a bug (or any change in behavior), letting you check a handful of commits instead of scanning through hundreds manually.

## Why Use It

- Pinpoint which commit introduced a regression in a large history
- Find the commit that broke a test, build, or feature
- Works even if you don't know roughly where the bug was introduced
- Automatable — can run a script to test each commit instead of doing it by hand

## How It Works

You tell Git a known **bad** commit (bug present) and a known **good** commit (bug absent). Git checks out a commit halfway between them and asks you to test it and report `good` or `bad`. It repeats this, halving the search space each time, until it isolates the exact commit that introduced the problem — O(log n) steps instead of checking every commit.

```
good ----------------------- bad
     ^binary search narrows down^
                 ↓
        first bad commit found
```

## Basic Manual Workflow

### 1. Start a bisect session
```bash
git bisect start
```

### 2. Mark the current (or a specific) commit as bad
```bash
git bisect bad                # current HEAD is bad
git bisect bad <commit-hash>  # or a specific commit
```

### 3. Mark a known good commit
```bash
git bisect good <commit-hash>
```

Git will now check out a commit roughly halfway between good and bad.

### 4. Test that commit, then tell Git the result
```bash
git bisect good   # bug is absent here
# or
git bisect bad    # bug is present here
```

Repeat step 4 — Git checks out a new midpoint commit each time — until Git reports:
```
<hash> is the first bad commit
```

### 5. End the bisect session
```bash
git bisect reset
```
Returns you to the branch/commit you were on before starting the bisect. **Always run this** when done, or you'll be left in a detached HEAD state.

## Skipping a Commit

If the checked-out commit can't be tested (e.g., doesn't build, unrelated breakage):
```bash
git bisect skip
```
Git will pick a nearby commit instead and continue.

You can also skip a specific range up front:
```bash
git bisect skip <hash1> <hash2>..<hash3>
```

## Automated Bisecting

The real power of bisect: automate testing with a script that exits `0` for good and non-zero (1-127, excluding 125) for bad.

```bash
git bisect start
git bisect bad HEAD
git bisect good v1.0
git bisect run <script-or-command>
```

Example with a test suite:
```bash
git bisect run npm test
```

Example with a custom script:
```bash
git bisect run ./check-bug.sh
```

Example `check-bug.sh`:
```bash
#!/bin/bash
make || exit 125   # 125 = "can't test this commit, skip it" (e.g., build failure)
./run-tests --filter=regression-test
exit $?
```

Git will automatically run the script/command against each candidate commit, interpret the exit code, and narrow down to the first bad commit — no manual `good`/`bad` typing needed.

### Exit Code Meaning for `bisect run`
| Exit code | Meaning |
|---|---|
| `0` | Good |
| `1`–`127` (except 125) | Bad |
| `125` | Can't test this commit — skip it |
| `128`+ | Aborts the bisect entirely |

## Visualizing Progress

```bash
git bisect log
```
Shows the full sequence of good/bad markings so far — useful for saving/replaying a session.

```bash
git bisect log > bisect-log.txt
```
Save the log to replay later:
```bash
git bisect replay bisect-log.txt
```

```bash
git bisect visualize
# or
git bisect view
```
Opens a visual log (gitk or configured tool) of remaining candidate commits.

## Narrowing the Search Path

### Limit bisect to specific files/directories
```bash
git bisect start -- path/to/file.js path/to/dir/
```
Only considers commits that touched those paths.

### Bisect terms other than good/bad
```bash
git bisect start --term-old=fast --term-new=slow
git bisect fast <commit>
git bisect slow <commit>
```
Useful for bisecting things other than binary bugs, e.g., a performance regression (old="fast", new="slow").

## Common Workflow Example

```bash
git bisect start
git bisect bad                     # current commit has the bug
git bisect good v2.1.0             # this tagged release was fine
# Git checks out a midpoint commit
npm test                           # manually test
git bisect bad                     # test failed, mark as bad
# Git checks out another midpoint
npm test
git bisect good                    # test passed, mark as good
# ... repeat until Git identifies the first bad commit ...
git bisect reset                   # clean up, return to original branch
```

Or fully automated:
```bash
git bisect start HEAD v2.1.0
git bisect run npm test
git bisect reset
```

## Notes & Gotchas

- Bisect puts you in a **detached HEAD** state while running — don't make new commits during a session unless you know what you're doing.
- Always run `git bisect reset` when finished, even if you found the answer, to return to your original branch cleanly.
- If bisect ends inconclusively (e.g., too many skips clustered together), Git will tell you it can't narrow further.
- Works best with a reliable, deterministic test — flaky tests will give bisect false signals and lead to wrong conclusions.
- `git bisect run` fails fast if your test script itself has bugs (e.g., wrong exit codes) — verify the script manually on a known-good and known-bad commit first.
- You can also bisect on merge commits, though the "first bad commit" found might be a merge commit itself rather than a specific code change, if the bug came from combining two branches.
- Bisect state is stored in `.git/BISECT_LOG` and related files — `git bisect reset` cleans these up.

## Quick Reference

| Command | Description |
|---|---|
| `git bisect start` | Begin a bisect session |
| `git bisect bad [<commit>]` | Mark a commit (default: HEAD) as bad |
| `git bisect good <commit>` | Mark a commit as good |
| `git bisect skip` | Skip current commit (untestable) |
| `git bisect run <cmd>` | Automate testing with a script/command |
| `git bisect log` | Show bisect session history |
| `git bisect replay <file>` | Replay a saved bisect log |
| `git bisect visualize` | Visualize remaining candidates |
| `git bisect reset` | End session, return to original HEAD |