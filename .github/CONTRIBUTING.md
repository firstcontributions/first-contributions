# Contribution guide

We appreciate your interest in contributing to open source! :heart:

As this repository is often the first stepping stone for people looking to contribute to open source projects in general, we include both general open source advice and guidelines specific to this project below.

---

## Contributing to open source (general advice)

- **Focus on what maintainers need**: It is best to think less in terms of what you can do to contribute and more in terms of what the project maintainers actually want. Look for issues labeled as [`help wanted`](https://github.com/firstcontributions/first-contributions/labels/help%20wanted) or [`good first issue`](https://github.com/firstcontributions/first-contributions/labels/good%20first%20issue). These labels indicate that maintainers have reviewed the problem and would like someone to address it.
- **Read the contribution guidelines**: Go through the contribution guidelines in the repository (usually `CONTRIBUTING.md`). Pay close attention to the details, requirements, and workflows described there.
- **Communicate before building**: For non-trivial changes, comment on the relevant issue or open a discussion before writing code so that everyone is aligned on the approach.

### On LLMs, coding agents and everything marketed as AI

It's best to use them as a tool for learning and not to do your work for you.

- **Write comments yourself**: If you're copy-pasting what an LLM generated, maintainers are communicating with LLMs rather than you.
- **Test and verify details yourself**: LLMs make mistakes all the time. You don't have to parrot those mistakes.
- **Push changes you understand**: You should be able to explain why you made a specific design choice or code change.

---

## Specific to contributing to first-contributions

### 1. Following the tutorial vs. Improving this project

Please pay attention to the difference between these two files:
- **`Contributors.md`**: If you are following the tutorial to make your first pull request, **this is the only file you should edit**. Add your name here as described in [README.md](../README.md).
- **`CONTRIBUTING.md`** (this file): This file contains guidelines for people who want to improve the codebase, tooling, or documentation of the `first-contributions` project itself. **Do not add your name to this file.**

### 2. Don't make unrequested changes in `README.md`

`README.md` is the core tutorial that has been translated into over 50 languages and carefully refined over years.
- Do not make pull requests for minor wording changes, capitalization changes in headers, or cosmetic formatting tweaks in `README.md`.
- Unsolicited pull requests with minor changes to `README.md` will be closed.
- If you notice a broken link, a broken command, or have a substantial improvement to propose, **open an issue first** and wait for maintainer confirmation before opening a pull request.

### 3. Submitting an issue

If you are opening an issue to propose a change:
- **Explain the value**: Clearly describe the problem and how your proposal improves the learning experience for beginners.
- **Avoid changes just for the sake of change**: Arbitrary edits, subjective stylistic preferences, or "hello world" additions do not add value and create noise for maintainers.
- **Check existing issues**: Search open and closed issues first to avoid duplicate discussions.

### 4. Working on issues

- **Check for the `help wanted` label**: Look for issues labeled [`help wanted`](https://github.com/firstcontributions/first-contributions/labels/help%20wanted) before starting work.
- **Confirm before starting**: Comment on the issue to confirm with maintainers before spending time working on a pull request. This prevents multiple contributors from working on the same thing at once.
- **Review design decisions**: Take a look at our [design decisions](https://github.com/firstcontributions/first-contributions/issues/35892) before suggesting changes to repository structure or workflow.

### 5. Helpful vs. Discouraged contributions

| ✅ Encouraged contributions | ❌ Discouraged contributions |
| :--- | :--- |
| Adding your name to `Contributors.md` to practice git | Making cosmetic edits to `README.md` to practice git |
| Addressing issues labeled `help wanted` or `good first issue` | Submitting pull requests without prior issue discussion |
| Reporting or fixing broken links, typos causing errors, or outdated commands | Submitting subjective rewording or heading capitalization changes |
| Adding complete translations in new languages (after opening an issue) | Adding arbitrary files (e.g., "Hello World" files, sample scripts) |
| Keeping pull requests small, focused, and well-explained | Opening automated or unverified AI-generated PRs and comments |

### 6. Git and PR best practices

- **Create a new branch**: Always check out the `main` branch and create a new feature branch for each change (`git switch -c your-branch-name`). Never work directly on your fork's `main` branch.
- **Keep pull requests small**: A pull request that changes one file is way easier to review than one changing 20 files. Keep each PR focused on a single concern.
