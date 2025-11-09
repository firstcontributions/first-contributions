# Setting Up Dependabot

## What is Dependabot?

Dependabot automatically checks dependencies for security vulnerabilities and outdated packages, creating pull requests to update them.

## Enabling Dependabot

1. Go to repository **Settings**
2. Click **Code security and analysis**
3. Enable **Dependabot alerts** and **Dependabot security updates**

## Setting Up Version Updates

Create `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
```

## Configuration for different ecosystems

### Node.js/npm
```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
    labels:
      - "dependencies"
```

### Python
```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
```

### Docker
```yaml
version: 2
updates:
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
```

### GitHub Actions
```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

## Common options

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    assignees:
      - "username"
    reviewers:
      - "reviewer-name"
    labels:
      - "dependencies"
    commit-message:
      prefix: "chore"
    ignore:
      - dependency-name: "express"
```

## Best practices

- Start with weekly updates
- Limit open PRs to 5-10
- Use labels for organization
- Review and merge PRs regularly
- Set up auto-merge for patch updates

