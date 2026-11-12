[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="GitHub CLI" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/600px-Octicons-mark-github.svg.png" width="40"> | GitHub CLI (`gh`) Edition |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |

It's hard. It's always hard the first time you do something. Especially when you are collaborating, making mistakes isn't a comfortable thing. But open source is all about collaboration & working together. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

This project aims at providing guidance & simplifying the way rookies make their first contribution. If you prefer working in the terminal and want a streamlined, modern CLI experience specifically designed for GitHub, you can use the official [GitHub CLI (`gh`)](https://cli.github.com/).

## Prerequisites

If you don't have GitHub CLI installed on your machine, [install it](https://cli.github.com/).

Once installed, authenticate GitHub CLI with your GitHub account:

```bash
gh auth login
```

Follow the on-screen prompts to log in (select `GitHub.com`, `HTTPS`, and authenticate via your web browser or personal access token).

## Fork and clone this repository

With GitHub CLI, you can fork and clone this repository in a single command directly from your terminal:

```bash
gh repo fork firstcontributions/first-contributions --clone
```

When prompted:
- `Would you like to clone the fork?` -> Select **Yes** (or press `Enter`).
- `What should the new repository be called?` -> Press `Enter` to keep `first-contributions`.

Now navigate into the cloned directory:

```bash
cd first-contributions
```

## Create a branch

Now create and switch to a new branch for your changes:

```bash
git switch -c your-new-branch-name
```
*(Replace `your-new-branch-name` with your actual branch name, for example `add-alonzo-church`)*

> If you are using an older version of Git where `git switch` is not available, you can use:
> ```bash
> git checkout -b your-new-branch-name
> ```

## Make necessary changes and commit

1. Open `Contributors.md` in your favorite text editor.
2. Add your name anywhere in between the existing contributors (avoid adding at the very beginning or the very end to prevent merge conflicts).
   ```markdown
   - [Your Name](https://github.com/your-username)
   ```
3. Save the file.

Now stage and commit your changes:

```bash
git add Contributors.md
git commit -m "Add your-name to Contributors list"
```

## Push your branch to GitHub

Push your new branch to your forked repository:

```bash
git push -u origin your-new-branch-name
```
*(Make sure to replace `your-new-branch-name` with the branch name you created).*

## Submit your pull request

Create a pull request right from your terminal using `gh pr create`:

```bash
gh pr create --title "Add your-name to Contributors list" --body "My first contribution!"
```

Follow the interactive prompts if prompted to choose the base repository (`firstcontributions/first-contributions`) and submit.

Once submitted, GitHub CLI will print the URL to your new pull request so you can view it on GitHub.

## Celebrate

Congrats! You just completed the contribution workflow using the GitHub CLI! 🎉
