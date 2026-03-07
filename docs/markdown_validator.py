#!/usr/bin/env python3
"""
Markdown Validator Script

This script scans Markdown files in the repository and reports
common formatting issues such as:

- Skipped heading levels
- Trailing whitespace
- Images without alt text
- Empty Markdown links

Usage:
    python scripts/markdown_validator.py
    python scripts/markdown_validator.py --dir docs
"""

import os
import re
import argparse
from pathlib import Path

# Regex patterns
HEADING_PATTERN = re.compile(r'^(#{1,6})\s+')
IMAGE_PATTERN = re.compile(r'!\[(.*?)\]\((.*?)\)')
LINK_PATTERN = re.compile(r'\[(.*?)\]\((.*?)\)')


def check_heading_order(lines, filepath):
    """Check if heading hierarchy is correct."""
    last_level = 0
    issues = []

    for i, line in enumerate(lines, start=1):
        match = HEADING_PATTERN.match(line)

        if match:
            level = len(match.group(1))

            if last_level and level > last_level + 1:
                issues.append(
                    f"{filepath}:{i} - Skipped heading level (H{last_level} -> H{level})"
                )

            last_level = level

    return issues


def check_trailing_whitespace(lines, filepath):
    """Detect trailing whitespace."""
    issues = []

    for i, line in enumerate(lines, start=1):
        if line.rstrip("\n").endswith(" "):
            issues.append(f"{filepath}:{i} - Trailing whitespace")

    return issues


def check_images(lines, filepath):
    """Check for images missing alt text."""
    issues = []

    for i, line in enumerate(lines, start=1):
        for alt, src in IMAGE_PATTERN.findall(line):
            if not alt.strip():
                issues.append(
                    f"{filepath}:{i} - Image missing alt text ({src})"
                )

    return issues


def check_empty_links(lines, filepath):
    """Check for empty Markdown links."""
    issues = []

    for i, line in enumerate(lines, start=1):
        for text, url in LINK_PATTERN.findall(line):
            if not url.strip():
                issues.append(
                    f"{filepath}:{i} - Empty link detected"
                )

    return issues


def validate_markdown_file(filepath):
    """Run all validation checks on a file."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    issues = []
    issues.extend(check_heading_order(lines, filepath))
    issues.extend(check_trailing_whitespace(lines, filepath))
    issues.extend(check_images(lines, filepath))
    issues.extend(check_empty_links(lines, filepath))

    return issues


def scan_directory(directory):
    """Scan directory recursively for Markdown files."""
    all_issues = []

    for path in Path(directory).rglob("*.md"):
        issues = validate_markdown_file(path)
        all_issues.extend(issues)

    return all_issues


def main():
    parser = argparse.ArgumentParser(description="Validate Markdown formatting")
    parser.add_argument(
        "--dir",
        default=".",
        help="Directory to scan for Markdown files (default: current directory)"
    )

    args = parser.parse_args()

    print("Running Markdown validation...\n")

    issues = scan_directory(args.dir)

    if not issues:
        print("No formatting issues found.")
        return

    print("Formatting issues detected:\n")

    for issue in issues:
        print(issue)

    print(f"\nTotal issues: {len(issues)}")


if __name__ == "__main__":
    main()