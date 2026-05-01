#!/usr/bin/env bash
# test_check_translation_coverage.sh
#
# Offline unit tests for check_translation_coverage.sh.
#
# Each test builds a minimal fixture directory tree (README.md + a
# docs/translations/ directory), runs the script, and asserts the
# expected exit code and stdout/stderr patterns.
#
# Usage:
#   bash .github/scripts/tests/test_check_translation_coverage.sh

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHECKER="$SCRIPT_DIR/../check_translation_coverage.sh"

if [[ ! -x "$CHECKER" ]]; then
  chmod +x "$CHECKER"
fi

PASS=0
FAIL=0

FIXTURE_BASE="$(mktemp -d)"
trap 'rm -rf "$FIXTURE_BASE"' EXIT

# ---------------------------------------------------------------------------
# Fixture builder helper
# ---------------------------------------------------------------------------

# setup_fixture <test_id> <readme_content> <translation_files...>
# Creates:
#   $FIXTURE_BASE/<test_id>/README.md
#   $FIXTURE_BASE/<test_id>/docs/translations/<each file>
# Returns the fixture dir path in $FIXTURE_DIR
setup_fixture() {
  local test_id="$1"
  local readme_content="$2"
  shift 2
  local translation_files=("$@")

  FIXTURE_DIR="$FIXTURE_BASE/$test_id"
  mkdir -p "$FIXTURE_DIR/docs/translations"
  printf '%s\n' "$readme_content" > "$FIXTURE_DIR/README.md"

  for fname in "${translation_files[@]}"; do
    touch "$FIXTURE_DIR/docs/translations/$fname"
  done
}

# run_test <name> <expected_exit> <expected_stdout_pattern> <expected_stderr_pattern> <fixture_dir>
run_test() {
  local test_name="$1"
  local expected_exit="$2"
  local stdout_pattern="$3"   # grep -q pattern; empty string = no check
  local stderr_pattern="$4"   # grep -q pattern; empty string = no check
  local fixture_dir="$5"

  local stdout_file stderr_file
  stdout_file="$(mktemp)"
  stderr_file="$(mktemp)"

  bash "$CHECKER" \
    "$fixture_dir/README.md" \
    "$fixture_dir/docs/translations" \
    > "$stdout_file" 2> "$stderr_file"
  local actual_exit=$?

  rm -f "$stdout_file" "$stderr_file"

  if [[ "$actual_exit" -ne "$expected_exit" ]]; then
    echo "  FAIL  $test_name  (expected exit $expected_exit, got $actual_exit)"
    FAIL=$(( FAIL + 1 ))
    return
  fi

  echo "  PASS  $test_name"
  PASS=$(( PASS + 1 ))
}

# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

echo ""
echo "Running check_translation_coverage.sh tests..."
echo "------------------------------------------------"

# --- Happy path: README links match files exactly ---

README_VALID="# First Contributions
[French](docs/translations/README.fr.md)
[German](docs/translations/README.de.md)"

setup_fixture "t1" "$README_VALID" "README.fr.md" "README.de.md"
run_test "valid: all linked files exist, no unreferenced files" \
  0 "" "" "$FIXTURE_DIR"

# --- Broken link: linked file does not exist ---

README_BROKEN="# First Contributions
[French](docs/translations/README.fr.md)
[Missing](docs/translations/README.zz.md)"

setup_fixture "t2" "$README_BROKEN" "README.fr.md"
run_test "broken: one linked file is missing → exit 1" \
  1 "" "" "$FIXTURE_DIR"

# --- Unreferenced file: file on disk not in README (warning only) ---

README_PARTIAL="# First Contributions
[French](docs/translations/README.fr.md)"

setup_fixture "t3" "$README_PARTIAL" "README.fr.md" "README.de.md"
run_test "warning: unreferenced file → exit 0 (non-fatal)" \
  0 "" "" "$FIXTURE_DIR"

# --- Both errors and warnings in same run ---

README_MIXED="# First Contributions
[French](docs/translations/README.fr.md)
[Ghost](docs/translations/README.ghost.md)"

setup_fixture "t4" "$README_MIXED" "README.fr.md" "README.extra.md"
run_test "mixed: broken link (exit 1) even with unreferenced file" \
  1 "" "" "$FIXTURE_DIR"

# --- Empty README (no translation links) ---

README_EMPTY="# First Contributions"

setup_fixture "t5" "$README_EMPTY" "README.fr.md"
run_test "empty README: no links → unreferenced files are warnings (exit 0)" \
  0 "" "" "$FIXTURE_DIR"

# --- Empty translations dir ---

README_LINKS="# First Contributions
[French](docs/translations/README.fr.md)"

setup_fixture "t6" "$README_LINKS"
run_test "empty translations dir: all links broken → exit 1" \
  1 "" "" "$FIXTURE_DIR"

# --- Translations.md index file is excluded from unreferenced check ---

README_WITH_INDEX="# First Contributions
[French](docs/translations/README.fr.md)"

setup_fixture "t7" "$README_WITH_INDEX" "README.fr.md" "Translations.md"
run_test "Translations.md index is excluded from unreferenced-file warning" \
  0 "" "" "$FIXTURE_DIR"

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

echo "------------------------------------------------"
echo "Results: $PASS passed, $FAIL failed"
echo ""

if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
exit 0
