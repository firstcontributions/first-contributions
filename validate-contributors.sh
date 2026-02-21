#!/usr/bin/env bash
#
# validate-contributors.sh - Validate your Contributors.md entry before submitting a PR
#
# Usage:
#   ./validate-contributors.sh              Check the whole file for issues
#   ./validate-contributors.sh --check      Same as above
#   ./validate-contributors.sh --add        Interactively add a properly formatted entry
#   ./validate-contributors.sh --help       Show usage information
#

set -euo pipefail

CONTRIBUTORS_FILE="Contributors.md"

# Colors (disabled if not a terminal)
if [ -t 1 ]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[0;33m'
    CYAN='\033[0;36m'
    BOLD='\033[1m'
    RESET='\033[0m'
else
    RED='' GREEN='' YELLOW='' CYAN='' BOLD='' RESET=''
fi

usage() {
    echo -e "${BOLD}validate-contributors.sh${RESET} - Validate your Contributors.md entry"
    echo ""
    echo "Usage:"
    echo "  ./validate-contributors.sh              Check the file for common issues"
    echo "  ./validate-contributors.sh --check      Same as above"
    echo "  ./validate-contributors.sh --add        Add a properly formatted entry"
    echo "  ./validate-contributors.sh --help       Show this help message"
    echo ""
    echo "Expected entry format:"
    echo "  - [Your Name](https://github.com/your-username)"
}

# --- Validation Functions ---

check_file_exists() {
    if [ ! -f "$CONTRIBUTORS_FILE" ]; then
        echo -e "${RED}Error:${RESET} $CONTRIBUTORS_FILE not found."
        echo "Make sure you're running this from the repository root."
        exit 1
    fi
}

validate_entry() {
    local line="$1"
    local line_num="$2"
    local errors=0

    # Skip header lines, blank lines, and non-entry lines
    if [[ "$line" =~ ^#  ]] || [[ -z "$line" ]] || [[ "$line" =~ ^[A-Z] && ! "$line" =~ ^\- ]]; then
        return 0
    fi

    # Check: missing dash prefix
    if [[ "$line" =~ ^\[.*\] && ! "$line" =~ ^- ]]; then
        echo -e "  ${YELLOW}Line $line_num:${RESET} Missing '- ' prefix"
        echo -e "    Got:      $line"
        echo -e "    Expected: - $line"
        errors=$((errors + 1))
    fi

    # Check: missing space after dash
    if [[ "$line" =~ ^-\[ ]]; then
        echo -e "  ${YELLOW}Line $line_num:${RESET} Missing space after '-'"
        echo -e "    Got:      $line"
        local fixed="${line/-[/- [}"
        echo -e "    Expected: $fixed"
        errors=$((errors + 1))
    fi

    # Check: space inside URL parentheses like "( https://..." or ".../ )"
    if [[ "$line" =~ \(\ https:// ]] || [[ "$line" =~ /\ \) ]]; then
        echo -e "  ${YELLOW}Line $line_num:${RESET} Extra space inside URL parentheses"
        echo -e "    Got: $line"
        errors=$((errors + 1))
    fi

    # Check: common URL typos
    if [[ "$line" =~ htps:// ]]; then
        echo -e "  ${RED}Line $line_num:${RESET} URL typo 'htps://' (missing 't' in https)"
        echo -e "    Got: $line"
        errors=$((errors + 1))
    fi
    if [[ "$line" =~ github\.c0m ]] || [[ "$line" =~ github\.con ]]; then
        echo -e "  ${RED}Line $line_num:${RESET} URL typo in domain (should be github.com)"
        echo -e "    Got: $line"
        errors=$((errors + 1))
    fi

    # Check: entry has a link (informational only)
    if [[ "$line" =~ ^-[[:space:]]?\[.*\]$ ]]; then
        if [[ ! "$line" =~ \(https?:// ]]; then
            echo -e "  ${CYAN}Line $line_num:${RESET} No GitHub link (optional but recommended)"
            echo -e "    Got:      $line"
            echo -e "    Suggest:  - [Name](https://github.com/username)"
        fi
    fi

    if [ "$errors" -gt 0 ]; then
        return 1
    fi
    return 0
}

# --- Commands ---

cmd_check() {
    check_file_exists

    echo -e "${BOLD}Checking $CONTRIBUTORS_FILE...${RESET}"
    echo ""

    local total_issues=0
    local line_num=0

    while IFS= read -r line || [ -n "$line" ]; do
        line_num=$((line_num + 1))
        if ! validate_entry "$line" "$line_num"; then
            total_issues=$((total_issues + 1))
        fi
    done < "$CONTRIBUTORS_FILE"

    # Check trailing newline
    if [ -s "$CONTRIBUTORS_FILE" ] && [ "$(tail -c 1 "$CONTRIBUTORS_FILE" | wc -l)" -eq 0 ]; then
        echo -e "  ${YELLOW}End of file:${RESET} Missing trailing newline"
        total_issues=$((total_issues + 1))
    fi

    echo ""
    if [ "$total_issues" -eq 0 ]; then
        echo -e "${GREEN}No issues found.${RESET}"
    else
        echo -e "${YELLOW}Found $total_issues issue(s).${RESET}"
        echo "These are suggestions to help you format your entry correctly."
    fi

    return 0
}

cmd_add() {
    check_file_exists

    echo -e "${BOLD}Add your entry to $CONTRIBUTORS_FILE${RESET}"
    echo ""
    echo "This will create a properly formatted entry for you."
    echo ""

    # Get display name
    read -rp "Your name (as you want it displayed): " display_name
    if [ -z "$display_name" ]; then
        echo -e "${RED}Error:${RESET} Name cannot be empty."
        exit 1
    fi

    # Get GitHub username
    local default_username=""
    if command -v git &>/dev/null; then
        default_username=$(git config user.name 2>/dev/null || true)
    fi

    read -rp "Your GitHub username: " github_user
    if [ -z "$github_user" ]; then
        echo -e "${RED}Error:${RESET} GitHub username cannot be empty."
        exit 1
    fi

    # Remove @ prefix if provided
    github_user="${github_user#@}"

    local entry="- [$display_name](https://github.com/$github_user)"

    # Check for duplicates
    if grep -qiF "github.com/$github_user)" "$CONTRIBUTORS_FILE"; then
        echo ""
        echo -e "${YELLOW}Warning:${RESET} An entry for '$github_user' may already exist:"
        grep -niF "github.com/$github_user)" "$CONTRIBUTORS_FILE" | head -3
        echo ""
        read -rp "Add anyway? (y/N): " confirm
        if [[ ! "$confirm" =~ ^[Yy] ]]; then
            echo "Aborted."
            exit 0
        fi
    fi

    # Ensure trailing newline before appending
    if [ -s "$CONTRIBUTORS_FILE" ] && [ "$(tail -c 1 "$CONTRIBUTORS_FILE" | wc -l)" -eq 0 ]; then
        echo "" >> "$CONTRIBUTORS_FILE"
    fi

    echo "$entry" >> "$CONTRIBUTORS_FILE"

    echo ""
    echo -e "${GREEN}Added:${RESET} $entry"
    echo ""
    echo -e "${BOLD}Next steps:${RESET}"
    echo "  1. git add Contributors.md"
    echo "  2. git commit -m \"Add $display_name to Contributors list\""
    echo "  3. git push -u origin your-branch-name"
    echo "  4. Open a pull request on GitHub"
}

# --- Main ---

case "${1:-}" in
    --help|-h)
        usage
        ;;
    --add|-a)
        cmd_add
        ;;
    --check|-c|"")
        cmd_check
        ;;
    *)
        echo -e "${RED}Unknown option:${RESET} $1"
        echo ""
        usage
        exit 1
        ;;
esac
