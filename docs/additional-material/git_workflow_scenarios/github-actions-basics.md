# GitHub Actions Basics

## What are GitHub Actions?

GitHub Actions is a CI/CD platform that automates your build, test, and deployment pipeline.

## Basic workflow structure

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: echo "Running tests"
```

## Common triggers

```yaml
# Push to specific branches
on:
  push:
    branches: [main, develop]

# Pull requests
on:
  pull_request:
    branches: [main]

# Multiple events
on: [push, pull_request]

# Scheduled (cron)
on:
  schedule:
    - cron: '0 2 * * *'

# Manual trigger
on:
  workflow_dispatch:
```

## Node.js workflow example

```yaml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - run: npm ci
      - run: npm test
      - run: npm run build
```

## Using secrets

```yaml
steps:
  - name: Deploy
    run: ./deploy.sh
    env:
      API_KEY: ${{ secrets.API_KEY }}
```

Add secrets in: Settings → Secrets and variables → Actions

## Popular actions

```yaml
- uses: actions/checkout@v4           # Checkout code
- uses: actions/setup-node@v4         # Setup Node.js
- uses: actions/setup-python@v5       # Setup Python
- uses: actions/cache@v3              # Cache dependencies
- uses: actions/upload-artifact@v3    # Upload artifacts
```

## Best practices

- Use specific action versions (@v4 not @main)
- Cache dependencies for faster builds
- Use secrets for sensitive data
- Keep workflows simple and focused
- Test workflows on feature branches first

