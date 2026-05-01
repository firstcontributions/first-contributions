#!/usr/bin/env bash
# check_translation_coverage.sh
#
# Cross-validates the translation links in README.md against the actual
# files present in docs/translations/.
#
# Two categories of discrepancy are reported:
#
#   ERROR (exit code 1):
#     A link in README.md points to a file that does not exist on disk.
#     These are broken links that 404 for visitors.
#
#   WARNING (exit code 0):
#     A file exists in docs/translations/ but is not linked from README.md.
#     These are unreferenced translations — flagged as warnings rather than
#     errors because a new translation may arrive in the same PR as the
#     README update, and we don't want to block that PR based on ordering.
#
# Usage:
#   check_translation_coverage.sh <readme_file> <translations_dir>
#
# Arguments:
#   <readme_file>      — path to README.md
#   <translations_dir> — path to the docs/translations/ directory
#
# Exit codes:
#   0 — no broken links (warnings about unreferenced files are non-fatal)
#   1 — one or more links in README.md point to non-existent files

set -euo pipefail

# ---------------------------------------------------------------------------
# Argument validation
# ---------------------------------------------------------------------------

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <readme_file> <translations_dir>" >&2
  exit 1
fi

README_FILE="$1"
TRANSLATIONS_DIR="$2"

if [[ ! -f "$README_FILE" ]]; then
  echo "Error: README file not found: $README_FILE" >&2
  exit 1
fi

if [[ ! -d "$TRANSLATIONS_DIR" ]]; then
  echo "Error: translations directory not found: $TRANSLATIONS_DIR" >&2
  exit 1
fi

# Resolve both paths to absolute to guarantee consistent path prefix stripping.
# Using cd+pwd for portability across macOS (no GNU realpath) and Linux.
REPO_ROOT="$(cd "$(dirname "$README_FILE")" && pwd)"
TRANSLATIONS_DIR_ABS="$(cd "$TRANSLATIONS_DIR" && pwd)"

# ---------------------------------------------------------------------------
# Step 1: Extract all relative paths pointing into docs/translations/
#         from README.md (e.g. docs/translations/README.fr.md)
# ---------------------------------------------------------------------------

# The '|| true' guards against grep returning exit code 1 when no links are
# found (e.g. a fresh README with no translations section yet). Under
# 'set -e' a bare failing grep would abort the script prematurely.
LINKED_FILES="$(
  grep -oE '\(docs/translations/[^)]+\)' "$README_FILE" \
    | tr -d '()' \
    | sort -u \
  || true
)"

# ---------------------------------------------------------------------------
# Step 2: Enumerate all .md files actually present in the translations dir
# ---------------------------------------------------------------------------

EXISTING_FILES="$(
  find "$TRANSLATIONS_DIR_ABS" -maxdepth 1 -name '*.md' -type f \
    | sed "s|$REPO_ROOT/||" \
    | sort -u
)"

# ---------------------------------------------------------------------------
# Step 3: Check for broken links (links in README → missing files)
# ---------------------------------------------------------------------------

broken_links=()

while IFS= read -r linked_path; do
  [[ -z "$linked_path" ]] && continue
  full_path="$REPO_ROOT/$linked_path"
  if [[ ! -f "$full_path" ]]; then
    broken_links+=("$linked_path")
  fi
done <<< "$LINKED_FILES"

# ---------------------------------------------------------------------------
# Step 4: Check for unreferenced files (files on disk → not in README)
# ---------------------------------------------------------------------------

unreferenced_files=()

while IFS= read -r existing_path; do
  [[ -z "$existing_path" ]] && continue
  # Skip the Translations.md index file — it is intentionally a directory
  # listing page rather than a language-specific README
  if [[ "$(basename "$existing_path")" == "Translations.md" ]]; then
    continue
  fi
  if ! echo "$LINKED_FILES" | grep -qF "$existing_path"; then
    unreferenced_files+=("$existing_path")
  fi
done <<< "$EXISTING_FILES"

# ---------------------------------------------------------------------------
# Step 5: Output results
# ---------------------------------------------------------------------------

exit_code=0

if [[ ${#broken_links[@]} -gt 0 ]]; then
  echo "❌ BROKEN LINKS — the following files are linked in README.md but do not exist:" >&2
  for path in "${broken_links[@]}"; do
    echo "  ✗ $path" >&2
  done
  echo "" >&2
  exit_code=1
fi

if [[ ${#unreferenced_files[@]} -gt 0 ]]; then
  echo "⚠️  UNREFERENCED FILES — the following translation files are not linked in README.md:"
  for path in "${unreferenced_files[@]}"; do
    echo "  ○ $path"
  done
  echo ""
  echo "  (These are warnings only — ensure README.md is updated to include these translations.)"
fi

if [[ $exit_code -eq 0 && ${#broken_links[@]} -eq 0 && ${#unreferenced_files[@]} -eq 0 ]]; then
  echo "✅ All translation links are consistent between README.md and docs/translations/."
elif [[ $exit_code -eq 0 ]]; then
  echo "✅ No broken links detected (see warnings above)."
fi

# Write structured output for GitHub Actions
if [[ -n "${GITHUB_OUTPUT:-}" ]]; then
  {
    if [[ ${#broken_links[@]} -gt 0 ]]; then
      echo "broken_links<<EOF"
      printf '%s\n' "${broken_links[@]}"
      echo "EOF"
      echo "coverage_check_failed=true"
    else
      echo "coverage_check_failed=false"
    fi
    echo "unreferenced_count=${#unreferenced_files[@]}"
    echo "broken_count=${#broken_links[@]}"
  } >> "$GITHUB_OUTPUT"
fi

exit $exit_code
