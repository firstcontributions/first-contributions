# Pull Request Templates

## What are PR templates?

Pull request templates are pre-filled forms that appear when creating a pull request, ensuring contributors provide necessary information.

## Creating a basic template

Create `.github/pull_request_template.md`:

```markdown
## Description

Summary of changes and which issue is fixed.

Fixes # (issue)

## Type of change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

How was this tested?

## Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Tests added
- [ ] Documentation updated
- [ ] All tests pass
```

## Creating the template

```bash
# Create directory
mkdir -p .github

# Create template
cat > .github/pull_request_template.md << 'EOF'
## Description

Fixes # (issue)

## Type of change

- [ ] Bug fix
- [ ] New feature

## Checklist

- [ ] Code reviewed
- [ ] Tests added
- [ ] Tests pass
EOF

# Commit
git add .github/pull_request_template.md
git commit -m "Add PR template"
git push
```

## Multiple templates

For different PR types, create `.github/PULL_REQUEST_TEMPLATE/`:

### Feature template (`feature.md`)
```markdown
## New Feature

### Description
What feature does this add?

### Related Issues
Closes # (issue)

### Checklist
- [ ] Tests added
- [ ] Documentation updated
```

### Bug fix template (`bug_fix.md`)
```markdown
## Bug Fix

### Bug Description
What bug does this fix?

### Solution
How does this fix it?

### Testing
How was this tested?

### Related Issues
Fixes # (issue)
```

## Using templates

Templates appear automatically when creating PRs.

For specific template:
```
https://github.com/user/repo/compare/main...branch?template=feature.md
```

## Best practices

- Keep templates concise (50-80 lines)
- Use checkboxes for easy tracking
- Include issue linking ("Fixes #123")
- Provide clear sections
- Don't make templates too long
- Update based on team feedback

