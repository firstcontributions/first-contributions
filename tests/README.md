# Tests

This directory contains unit tests for the first-contributions project.

## Running Tests

To run all tests:

```bash
python -m unittest discover tests -v
```

To run a specific test file:

```bash
python -m unittest tests.test_validator -v
```

## Test Coverage

### `test_validator.py`

Tests for the Contributors.md validation script (`../.github/scripts/validate_contributors.py`).

**Test Coverage:**
- Valid file format validation
- Missing header detection
- Markdown syntax errors (unmatched brackets, parentheses)
- Space between `]` and `(` detection
- Placeholder username detection
- Domain typo detection
- Missing GitHub link warnings
- Duplicate username warnings
- Missing HTTPS protocol warnings
- Unicode character support
- Special characters in usernames
- Trailing slashes in URLs
- Multiple sections in the file
- Entries with additional comments

## Contributing Tests

When adding new validation rules to the validator script, please add corresponding unit tests to ensure the functionality works correctly.
