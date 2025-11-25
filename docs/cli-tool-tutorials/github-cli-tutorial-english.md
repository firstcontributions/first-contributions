---
title: "GitHub CLI tutorial (English)"
---

# GitHub CLI — Quick Tutorial (Windows / PowerShell)

This short guide shows how to use the GitHub CLI (`gh`) together with `git` to make a simple contribution: fork (optional), clone, create a branch, make a change, commit, push and open a pull request.

Prerequisites
- `git` installed and configured (`git --version`).
- `gh` (GitHub CLI) optionally installed for launching PRs from the terminal: https://cli.github.com/

If you prefer the web UI you can still follow the same steps — use the GitHub website to fork and open PRs.

1) Fork the repository (optional but recommended if you don't have write access)

PowerShell (web method):
```
# Open the repo in your browser and click Fork
start https://github.com/shreyaajahan/first-contributions
```

Or with `gh` (creates a fork under your account):
```
gh repo fork shreyaajahan/first-contributions --clone=false
```

2) Clone the repository (use your fork URL if you forked)

PowerShell:
```
Set-Location -Path F:\path\to\projects
git clone https://github.com/<your-username>/first-contributions.git
Set-Location -Path .\first-contributions
```

If you didn't fork, clone the original repo URL instead.

3) Create and switch to a feature branch

Use a descriptive branch name, for example `docs/add-github-cli-tutorial`:
```
git checkout -b docs/add-github-cli-tutorial
```

4) Make your changes

- Add or edit files under `docs/cli-tool-tutorials/`.
- Example: create `docs/cli-tool-tutorials/github-cli-tutorial-english.md` with this content.

5) Stage and commit

```
git add docs/cli-tool-tutorials/github-cli-tutorial-english.md
git commit -m "docs: add GitHub CLI tutorial (English)"
```

6) Push your branch to your fork (or `origin` if you have write access)

```
git push -u origin docs/add-github-cli-tutorial
```

7) Open a Pull Request

- Web: go to your fork on GitHub, you'll see a banner to create a PR from your branch — click it and fill the template.
- `gh` CLI:
```
gh pr create --title "docs: add GitHub CLI tutorial (English)" --body "This adds a short GitHub CLI tutorial for Windows/PowerShell." --base main
```

Tips for your PR description
- Explain what you added and why (one or two sentences).
- Include a short checklist: `- [x] I signed the CLA (if needed)` or `- [x] Docs added`.

That's it — once maintainers review they may ask for small changes. Respond to feedback by pushing commits to the same branch.

If you want, I can prepare this file locally, create a branch and commit it for you (I won't push without your go-ahead). Tell me if you'd like me to push the branch and open the PR (you may need to authenticate or have a fork).

---

## Expanded examples and screenshots

Below are a few practical examples you can copy-paste in PowerShell and explanations of what they do.

- Clone (example using your fork):
```powershell
git clone https://github.com/<your-username>/first-contributions.git
cd .\first-contributions
```

- Create a branch and add your name to `Contributors.md`:
```powershell
git checkout -b docs/add-your-name
Add-Content -Path .\Contributors.md -Value "`n- [Your Name](https://github.com/your-github-username)"
git add Contributors.md
git commit -m "docs: add <Your Name> to Contributors.md"
```

- Push and create PR using `gh` (after `gh auth login`):
```powershell
git push -u origin docs/add-your-name
gh pr create --title "docs: add <Your Name> to Contributors" --body "Adds my name to Contributors.md" --base main
```

Screenshot examples (hosted images):

![Clone screenshot](https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png)

If you want me to include local image files in the repo (e.g. `docs/assets/gh-cli-windows-1.png`), I can add them and update the tutorial to use relative paths.

If you'd prefer a worked example that edits `docs/how-to-contribute-to-open-source-projects.md` instead, I can make that change here on the branch so you can see a real PR-ready sample.
