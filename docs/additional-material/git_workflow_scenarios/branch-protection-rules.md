# Branch Protection Rules

## What are branch protection rules?

Branch protection rules prevent accidental changes to important branches and enforce specific workflows before code can be merged.

## Setting up protection

1. Go to repository **Settings**
2. Click **Branches**
3. Click **Add branch protection rule**
4. Enter branch name pattern (e.g., `main`)
5. Select protection options

## Common protection options

### Require pull request reviews
```
☑️ Require a pull request before merging
  ☑️ Require approvals: 1-2
  ☑️ Dismiss stale pull request approvals when new commits are pushed
```

### Require status checks
```
☑️ Require status checks to pass before merging
  ☑️ Require branches to be up to date before merging
  Status checks: ci/test, ci/lint
```

### Other important options
```
☑️ Require conversation resolution before merging
☑️ Require signed commits
☑️ Require linear history
☑️ Restrict who can push to matching branches
☐ Allow force pushes (keep disabled)
```

## Configuration examples

### Basic (small team)
- Require pull requests
- Require 1 approval
- Require status checks to pass

### Strict (enterprise)
- Require pull requests with 2 approvals
- Require all status checks
- Dismiss stale reviews
- Require signed commits
- Restrict who can push

## Using CODEOWNERS

Create `.github/CODEOWNERS`:

```
# Default owners
* @team-lead

# Specific directories
/docs/ @documentation-team
/src/api/ @backend-team
/src/frontend/ @frontend-team

# Specific files
package.json @senior-dev
```

## Working with protected branches

```bash
# Cannot push directly to protected branch
git push origin main  # ❌ Will fail

# Must use pull requests
git checkout -b feature/my-feature
git push origin feature/my-feature
# Create PR on GitHub
```

## Best practices

- Always protect main/master branch
- Require at least 1 reviewer
- Enforce passing tests
- Use CODEOWNERS for expertise areas
- Start lenient, tighten as needed
- Document bypass procedures for emergencies.

