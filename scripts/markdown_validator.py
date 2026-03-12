#!/usr/bin/env python3
"""Validate common Markdown formatting issues in this repository."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_TARGETS = ("README.md", "docs", "examples")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+")
MARKDOWN_IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<target>[^)]*)\)")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[(?P<text>[^\]]*)\]\((?P<target>[^)]*)\)")
HTML_IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
HTML_ALT_RE = re.compile(r"""\balt\s*=\s*(['"])(?P<value>.*?)\1""", re.IGNORECASE)
FENCE_RE = re.compile(r"^[ \t]*(```|~~~)")


@dataclass(frozen=True)
class Warning:
    path: Path
    line: int
    check: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate Markdown files for skipped heading levels, trailing "
            "whitespace, missing image alt text, and empty links."
        )
    )
    parser.add_argument(
        "targets",
        nargs="*",
        help=(
            "Files or directories to scan. Defaults to README.md, docs/, and "
            "examples/ when they exist."
        ),
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Exit with status 1 when warnings are found.",
    )
    return parser.parse_args()


def iter_markdown_files(targets: Iterable[str]) -> list[Path]:
    resolved_targets = list(targets) if targets else list(DEFAULT_TARGETS)
    files: set[Path] = set()

    for raw_target in resolved_targets:
        path = Path(raw_target)
        if not path.exists():
            continue
        if path.is_file() and path.suffix.lower() == ".md":
            files.add(path)
            continue
        if path.is_dir():
            files.update(candidate for candidate in path.rglob("*.md") if candidate.is_file())

    return sorted(files)


def validate_file(path: Path) -> list[Warning]:
    warnings: list[Warning] = []
    in_fence = False
    previous_heading_level: int | None = None

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()

    for line_number, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue

        if line.rstrip(" \t") != line:
            warnings.append(
                Warning(path, line_number, "trailing-whitespace", "Line has trailing whitespace.")
            )

        if in_fence:
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            if previous_heading_level is not None and previous_heading_level >= 2:
                if level > previous_heading_level + 1:
                    warnings.append(
                        Warning(
                            path,
                            line_number,
                            "heading-level",
                            (
                                "Heading level jumps from "
                                f"H{previous_heading_level} to H{level}."
                            ),
                        )
                    )
            previous_heading_level = level

        for match in MARKDOWN_IMAGE_RE.finditer(line):
            if not match.group("alt").strip():
                warnings.append(
                    Warning(
                        path,
                        line_number,
                        "image-alt",
                        "Markdown image is missing alt text.",
                    )
                )

        for html_image in HTML_IMG_RE.finditer(line):
            alt_match = HTML_ALT_RE.search(html_image.group(0))
            if alt_match is None or not alt_match.group("value").strip():
                warnings.append(
                    Warning(
                        path,
                        line_number,
                        "image-alt",
                        "HTML image is missing alt text.",
                    )
                )

        for match in MARKDOWN_LINK_RE.finditer(line):
            if not match.group("target").strip():
                warnings.append(
                    Warning(
                        path,
                        line_number,
                        "empty-link",
                        "Markdown link target is empty.",
                    )
                )

    return warnings


def main() -> int:
    args = parse_args()
    files = iter_markdown_files(args.targets)

    if not files:
        print("No Markdown files found.")
        return 0

    warnings = [warning for path in files for warning in validate_file(path)]

    for warning in warnings:
        print(f"{warning.path}:{warning.line}: {warning.check}: {warning.message}")

    print(f"Scanned {len(files)} Markdown file(s). Found {len(warnings)} warning(s).")

    if warnings and args.fail_on_warning:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
