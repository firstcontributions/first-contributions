[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions with Google's Antigravity

| <img alt="Antigravity" src="https://www.gstatic.com/devrel-devsite/prod/v45f61267e619b2a75909a28b00b9d19b79ee3cbc8bc00e8b5ba4f3f1dff52f39/cloud/images/cloud-logo.svg" width="200"> | Google Antigravity AI Edition |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |

It can feel daunting to make your first open source contribution, especially when staring at an unfamiliar codebase. That's where **Google's Antigravity** AI coding assistant steps in — it pairs you with an intelligent agent that understands your project, helps you navigate code, and guides you through contributions confidently.

This tutorial walks you through forking, cloning, editing, and submitting a pull request to this project, all while using Antigravity as your pair-programming copilot.

If you don't have git on your machine, [install it](https://docs.github.com/en/get-started/quickstart/set-up-git).

---

## What is Google's Antigravity?

**Antigravity** is Google DeepMind's agentic AI coding assistant. It lives inside your editor, understands your entire codebase in context, and can:

*   Clone and set up repositories on your behalf
*   Read, navigate, and explain unfamiliar code
*   Create branches, make changes, and commit — all through natural language prompts
*   Verify changes by running commands and reading terminal output
*   Help you write clear commit messages and pull request descriptions

Think of it as a senior developer sitting right next to you, available at all times.

---

## Prerequisites

Before starting, make sure you have:

*   A [GitHub](https://github.com/) account
*   [Git](https://git-scm.com/downloads) installed on your machine
*   [Visual Studio Code](https://code.visualstudio.com/) (recommended editor with Antigravity support)
*   Access to **Google's Antigravity** — sign in via your Google account in your editor's Antigravity panel

---

## Step 1 — Fork this Repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork the repository" />

Fork this repository by clicking the **Fork** button at the top-right of this page. This creates a personal copy of the repository in your GitHub account.

> **Why fork?** Forking gives you your own remote copy to freely experiment with, without affecting the original project.

---

## Step 2 — Clone the Repository Using Antigravity

### Option A: Let Antigravity Clone For You (Recommended)

Once you have Antigravity open in your editor, simply type a natural language prompt like:

```
Clone my fork of first-contributions from GitHub and open it
```

Antigravity will:
1. Identify your fork URL from your GitHub account
2. Run `git clone` in your workspace directory
3. Open the cloned project for you automatically

### Option B: Clone Manually via Terminal

Go to your forked repository on GitHub, click the **Code** button, select the **SSH** tab, and copy the URL.

Open a terminal and run:

```bash
git clone "url you just copied"
```

For example:

```bash
git clone git@github.com:your-username/first-contributions.git
```

Then navigate into the project directory:

```bash
cd first-contributions
```

<details>
<summary><strong>Having trouble cloning? Click here for help:</strong></summary>

If you see a `Permission denied (publickey)` error, your SSH key may not be configured. Follow [GitHub's SSH setup guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to fix this.

Alternatively, switch to the **HTTPS** tab when copying the clone URL and use that URL instead. You may be prompted for your GitHub username and personal access token.

</details>

---

## Step 3 — Open the Project in Your Editor with Antigravity

Open the cloned folder in Visual Studio Code:

```bash
code first-contributions
```

In VS Code, open the **Antigravity** panel (usually accessible from the sidebar or via the command palette with `Cmd+Shift+P` → `Open Antigravity`).

You can now ask Antigravity questions about the project, such as:

```
What does this repository do, and where should I add my name?
```

Antigravity will read the `README.md` and `Contributors.md` files and give you a clear, contextual answer.

---

## Step 4 — Create a Branch

### Using Antigravity

Simply ask:

```
Create a new git branch called add-your-name
```

Replace `your-name` with your actual name (e.g., `add-jane-doe`). Antigravity will run the appropriate git command for you.

### Using the Terminal

```bash
git switch -c add-your-name
```

For example:

```bash
git switch -c add-jane-doe
```

<details>
<summary><strong>If you get an error with `git switch`, click here:</strong></summary>

If your git version is older, use `git checkout` instead:

```bash
git checkout -b add-your-name
```

</details>

---

## Step 5 — Make Changes with Antigravity's Help

Open `Contributors.md` in your editor. Ask Antigravity to help you:

```
Add my name "Jane Doe" with my GitHub profile link to the Contributors.md file
```

Antigravity will:
1. Open the `Contributors.md` file
2. Find an appropriate location (not the beginning or end)
3. Insert your entry in the correct format:

```markdown
[Jane Doe](https://github.com/janedoe)
```

4. Save the file automatically

You can always verify the change by reviewing the file diff in your editor's Source Control panel.

---

## Step 6 — Commit Your Changes

### Using Antigravity

Ask Antigravity to commit with a descriptive message:

```
Commit my changes with the message "Add Jane Doe to Contributors list"
```

Antigravity will run:

```bash
git add Contributors.md
git commit -m "Add Jane Doe to Contributors list"
```

### Using the Terminal Manually

```bash
git add Contributors.md
git commit -m "Add your-name to Contributors list"
```

Replace `your-name` with your actual name.

---

## Step 7 — Push Changes to GitHub

### Using Antigravity

```
Push my branch to GitHub
```

Antigravity will push the branch to your remote fork automatically.

### Using the Terminal

```bash
git push -u origin add-your-name
```

Replace `add-your-name` with the name of your branch.

<details>
<summary><strong>If you get a push authentication error, click here:</strong></summary>

If you see:
```
remote: Support for password authentication was removed on August 13, 2021.
```

You need to configure SSH or use a personal access token. Follow [GitHub's guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to set up SSH authentication.

</details>

---

## Step 8 — Submit a Pull Request

Go to your forked repository on GitHub. You should see a **Compare & pull request** banner — click it.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="compare and create pull request" />

Fill in a clear title and description, then click **Create pull request**.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

> **Tip:** Ask Antigravity to help you write a good PR description:
> ```
> Write a concise pull request description for adding my name to Contributors.md
> ```

A maintainer will review and merge your changes. You'll receive a GitHub notification once it's done!

---

## Tips for Using Antigravity Effectively

| Tip | Example Prompt |
| --- | -------------- |
| **Understand code** | `"Explain what the Contributors.md file format expects"` |
| **Navigate the codebase** | `"Show me all markdown files in the docs folder"` |
| **Fix mistakes** | `"Undo my last change to Contributors.md"` |
| **Verify your work** | `"Run git status and show me what files I changed"` |
| **Write commit messages** | `"Suggest a good commit message for my changes"` |

---

## Where to Go from Here?

Congrats! You've completed your first contribution using the _fork → clone → edit → pull request_ workflow, powered by Antigravity! 🎉

Celebrate your contribution and share it with your friends by visiting the [web app](https://firstcontributions.github.io/#social-share).

*   Want more practice? Check out [code contributions](https://github.com/roshanjossey/code-contributions).
*   Browse beginner-friendly open source issues on [GitHub Explore](https://github.com/explore).
*   Learn more about Antigravity's capabilities at [Google DeepMind](https://deepmind.google/).

### [Additional material](../additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Using Other Tools

[Back to main page](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
