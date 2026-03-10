# What is a merge conflict?

A merge conflict occurs when changes from different branches clash and Git cannot merge them automatically. Common scenarios include:

- Two contributors editing the same line in a file.
- One contributor deletes a file that another has modified.
- Simultaneous renaming of a file to different names in separate branches.

In such cases, Git will pause the merge process and mark the conflicting files for manual resolution. There are tools that helps users resolve these conflicts but in this guide, we will be focusing on the git command line tool.

## How to resolve a merge conflict?

1. **Identify Conflicted Files**
   After attempting a merge, Git will notify you of conflicts. Use the following command to list them:

```bash
git status
```

Look for files listed under "Unmerged paths."

2. **Open and Examine Conflicted Files**
   Open each conflicted file in your preferred text editor. Git sets boundaries for conflicts using the following markers:

```plaintext
<<<<<<< HEAD
Your changes
=======
Incoming changes
>>>>>>> branch-name
```

- `<<<<<<< HEAD` represents your current branch's changes.

- `=======` separates the conflicting changes.

- `>>>>>>> branch-name` shows the incoming changes from the other branch.

3. **Resolve the Conflicts**

Decide how to integrate the changes:

- Keep your changes.
- Accept the incoming changes.
- Combine both changes in a coherent manner.

After making the necessary edits, remove the conflict markers (<<<<<<<, =======, >>>>>>>)

4. **Mark Conflicts as Resolved**
   Once you've resolved the conflicts in a file:

```bash
git add <filename>
```

**Repeat this for each conflicted file.**

5. **Commit the Merge**
   After staging all resolved files:

```bash
git commit -m "Resolved merge conflicts"
```

🎉This finalizes the merge process.🎉

---

# Additional information

## Tools to Assist in Conflict Resolution

- Git Merge Tool: Launches a visual merge tool to help resolve conflicts.

```bash
git mergetool
```

> Note: Ensure you have a merge tool installed (e.g., Meld, KDiff3, Beyond Compare).

- Abort a Merge: If you wish to cancel the merge process:

```bash
  git merge --abort
```

## Best Practices to Avoid Conflicts

Pull Regularly: Frequently pull changes from the main branch to stay updated.

```bash
git pull origin main
```

Work on Feature Branches: Create separate branches for each feature or fix.

```bash
git checkout -b feature-branch
```

## Additional Resources

- [GitHub: Resolving Merge Conflicts via Command Line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)

- [Atlassian: Git Merge Conflicts Tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)

- [FreeCodeCamp: Practical Guide to Merge Conflicts](https://www.freecodecamp.org/news/resolve-merge-conflicts-in-git-a-practical-guide/)

By following this guide, you'll be well-equipped to handle merge conflicts confidently, ensuring a smoother contribution process to any open source project!
