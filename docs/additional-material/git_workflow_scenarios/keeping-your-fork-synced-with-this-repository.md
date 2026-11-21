# Keeping your fork synced with this repository

When contributing to open source, other contributors will continue merging their changes into the original project. Over time, your fork on GitHub and your local repository will fall behind.

To keep your fork up to date with the original project, you need to sync your repositories. In open source development, this setup involves three places and is known as a **triangle workflow**:

1. **The original repository on GitHub** (referred to as `upstream`): `https://github.com/firstcontributions/first-contributions.git`
2. **Your local clone on your computer**: where you write code and make commits.
3. **Your fork on GitHub** (referred to as `origin`): `https://github.com/<your-username>/first-contributions.git`

<img src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

To sync changes, the flow is:
1. Pull the latest commits from the original repository (`upstream`) into your local `main` branch.
2. Push those updated commits from your local machine to your GitHub fork (`origin`).

---

## Step-by-Step Guide

### Step 1: Switch to your `main` branch

Always switch to your `main` branch before syncing:

```bash
git checkout main
```

> **Tip:** If you are using a newer version of Git, you can also use `git switch main`.

You can verify which branch you are on with:

```bash
git status
```

---

### Step 2: Check your configured remotes

Run the following command to see the remotes currently configured in your local repository:

```bash
git remote -v
```

You should see your fork listed as `origin`:

```text
origin  https://github.com/<your-username>/first-contributions.git (fetch)
origin  https://github.com/<your-username>/first-contributions.git (push)
```

---

### Step 3: Add the original repository as `upstream` (one-time setup)

If you haven't added the original repository yet, configure it as a remote named `upstream`:

```bash
git remote add upstream https://github.com/firstcontributions/first-contributions.git
```

> **Note:** You only need to run this command once per repository clone. You can run `git remote -v` again to confirm both `origin` and `upstream` are listed.

---

### Step 4: Fetch and merge the latest changes from `upstream`

Now retrieve the latest commits from the original repository's `main` branch and merge them into your local `main` branch:

```bash
git pull upstream main
```

This command fetches updates from `upstream` and merges them into your current local branch (`main`).

<details>
<summary><strong>Alternative: Fetch and merge/rebase in separate steps</strong></summary>

If you prefer to inspect updates before integrating them, you can fetch first and then merge:

1. Fetch updates from upstream:
   ```bash
   git fetch upstream
   ```
2. Merge the fetched changes into your current branch:
   ```bash
   git merge upstream/main
   ```
   *(Or `git rebase upstream/main` if your project prefers a linear commit history.)*

</details>

---

### Step 5: Push the updated `main` branch to your GitHub fork

Your local `main` branch is now up to date. To update your fork on GitHub as well, push the commits to `origin`:

```bash
git push origin main
```

---

## Summary of Commands

Once `upstream` is configured, keeping your fork synchronized in the future requires just three quick commands:

```bash
git checkout main
git pull upstream main
git push origin main
```

Well done! Your local repository and your GitHub fork are now fully synchronized with the original repository.

