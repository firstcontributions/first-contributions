#!/usr/bin/env python3
"""
Validates contributions to Contributors.md file.
Checks for proper formatting, duplicates, and markdown syntax.
"""

import re
import sys
from typing import List, Set
from pathlib import Path


class ContributorValidator:
    def __init__(self, file_path: str = "Contributors.md"):
        self.file_path = Path(file_path)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def validate(self) -> bool:
        """Run all validation checks."""
        if not self.file_path.exists():
            self.errors.append(f"❌ File not found: {self.file_path}")
            return False
            
        content = self.file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        # Run validation checks
        self._check_file_structure(lines)
        self._check_contributor_format(lines)
        self._check_duplicates(lines)
        self._check_markdown_syntax(lines)
        self._check_common_mistakes(lines)
        
        return len(self.errors) == 0
    
    def _check_file_structure(self, lines: List[str]):
        """Ensure file has proper header structure."""
        if not lines:
            self.errors.append("❌ File is empty")
            return
            
        if not lines[0].strip().startswith("# Contributors"):
            self.errors.append("❌ File must start with '# Contributors' header")
    
    def _check_contributor_format(self, lines: List[str]):
        """Validate contributor entry format."""
        # Pattern: - [Name](https://github.com/username)
        contributor_pattern = re.compile(r'^-\s+\[.+?\]\(https://github\.com/[a-zA-Z0-9\-_]+/?\)\s*$')
        
        in_contributors_section = False
        line_num = 0
        
        for line in lines:
            line_num += 1
            stripped = line.strip()
            
            # Skip empty lines and headers
            if not stripped or stripped.startswith('#'):
                if stripped.startswith('# Contributors'):
                    in_contributors_section = True
                continue
            
            # Check lines that start with dash (list items)
            if stripped.startswith('-') and in_contributors_section:
                # Check for valid GitHub link format
                if not contributor_pattern.match(stripped):
                    # Allow entries that are reasonably formatted but give warnings for common issues
                    if 'github.com' not in stripped.lower() and 'http' not in stripped.lower():
                        self.warnings.append(
                            f"⚠️  Line {line_num}: Entry missing GitHub profile link\n"
                            f"   Found: `{stripped[:80]}{'...' if len(stripped) > 80 else ''}`\n"
                            f"   Expected format: `- [Your Name](https://github.com/yourusername)`"
                        )
                    elif not stripped.startswith('- ['):
                        self.errors.append(
                            f"❌ Line {line_num}: Invalid list format. Must start with `- [`\n"
                            f"   Found: `{stripped[:80]}{'...' if len(stripped) > 80 else ''}`"
                        )
    
    def _check_duplicates(self, lines: List[str]):
        """Check for duplicate contributor entries."""
        seen_usernames: Set[str] = set()
        seen_names: Set[str] = set()
        
        username_pattern = re.compile(r'https://github\.com/([a-zA-Z0-9\-_]+)')
        name_pattern = re.compile(r'\[(.+?)\]')
        
        line_num = 0
        for line in lines:
            line_num += 1
            stripped = line.strip()
            
            if not stripped.startswith('-'):
                continue
            
            # Check for duplicate GitHub usernames
            username_match = username_pattern.search(stripped)
            if username_match:
                username = username_match.group(1).lower()
                if username in seen_usernames and username not in ['your-github-username', 'yourusername']:
                    self.warnings.append(
                        f"⚠️  Line {line_num}: Duplicate GitHub username found: @{username}"
                    )
                seen_usernames.add(username)
            
            # Check for duplicate names (less strict)
            name_match = name_pattern.search(stripped)
            if name_match:
                name = name_match.group(1).strip().lower()
                # Filter out common placeholder names
                if name not in ['name', 'your name', 'the name', 'john cena'] and name in seen_names:
                    self.warnings.append(
                        f"⚠️  Line {line_num}: Duplicate name found: {name_match.group(1)}"
                    )
                seen_names.add(name)
    
    def _check_markdown_syntax(self, lines: List[str]):
        """Check for common Markdown syntax errors."""
        line_num = 0
        for line in lines:
            line_num += 1
            stripped = line.strip()
            
            if not stripped.startswith('-'):
                continue
            
            # Check for unmatched brackets
            open_brackets = stripped.count('[')
            close_brackets = stripped.count(']')
            if open_brackets != close_brackets:
                self.errors.append(
                    f"❌ Line {line_num}: Unmatched square brackets [ ]\n"
                    f"   Found: `{stripped[:80]}{'...' if len(stripped) > 80 else ''}`"
                )
            
            open_parens = stripped.count('(')
            close_parens = stripped.count(')')
            if open_parens != close_parens:
                self.errors.append(
                    f"❌ Line {line_num}: Unmatched parentheses ( )\n"
                    f"   Found: `{stripped[:80]}{'...' if len(stripped) > 80 else ''}`"
                )
            
            # Check for space between ]( in markdown links
            if '] (' in stripped:
                self.errors.append(
                    f"❌ Line {line_num}: Space found between `]` and `(` in markdown link\n"
                    f"   Should be `](` with no space\n"
                    f"   Found: `{stripped[:80]}{'...' if len(stripped) > 80 else ''}`"
                )
    
    def _check_common_mistakes(self, lines: List[str]):
        """Check for common mistakes in contributor entries."""
        line_num = 0
        for line in lines:
            line_num += 1
            stripped = line.strip()
            
            if not stripped.startswith('-'):
                continue
            
            # Check for placeholder text
            placeholders = ['<your-github-username>', '<yourusername>', 'your-username', 'yourusername']
            for placeholder in placeholders:
                if placeholder in stripped.lower():
                    self.errors.append(
                        f"❌ Line {line_num}: Contains placeholder text: `{placeholder}`\n"
                        f"   Please replace with your actual GitHub username"
                    )
            
            # Check for invalid URL schemes
            if 'github.com' in stripped and not 'https://github.com' in stripped:
                if 'http://github.com' in stripped:
                    self.warnings.append(
                        f"⚠️  Line {line_num}: Using http:// instead of https://\n"
                        f"   Please use: `https://github.com/...`"
                    )
                elif 'github.com/' in stripped and not '://' in stripped:
                    self.warnings.append(
                        f"⚠️  Line {line_num}: Missing https:// protocol\n"
                        f"   Found: `{stripped[:80]}{'...' if len(stripped) > 80 else ''}`\n"
                        f"   Should be: `https://github.com/...`"
                    )
            
            # Check for typos in domain names
            typos = ['gitbut.com', 'githb.com', 'gihub.com', 'gihtub.com']
            for typo in typos:
                if typo in stripped.lower():
                    self.errors.append(
                        f"❌ Line {line_num}: Typo in domain: `{typo}` should be `github.com`\n"
                        f"   Found: `{stripped[:80]}{'...' if len(stripped) > 80 else ''}`"
                    )
            
            # Check for trailing slashes in username URLs (acceptable but warn)
            github_url_with_trailing = re.search(r'https://github\.com/[a-zA-Z0-9\-_]+/\)', stripped)
            if github_url_with_trailing:
                # This is actually acceptable, so we won't warn
                pass
    
    def print_results(self):
        """Print validation results."""
        if self.errors:
            print("\n🔴 **Validation Errors:**\n")
            for error in self.errors:
                print(error)
                print()
        
        if self.warnings:
            print("\n🟡 **Validation Warnings:**\n")
            for warning in self.warnings:
                print(warning)
                print()
        
        if not self.errors and not self.warnings:
            print("\n✅ **Validation Passed!**")
            print("All entries in Contributors.md are properly formatted.")
        
        # Summary
        print("\n" + "="*60)
        print(f"📊 Summary: {len(self.errors)} errors, {len(self.warnings)} warnings")
        print("="*60)
    
    def save_results_to_file(self, output_file: str = "validation_errors.txt"):
        """Save validation results to a file for GitHub Actions."""
        if not self.errors and not self.warnings:
            # Don't create file if everything is OK
            return
        
        with open(output_file, 'w', encoding='utf-8') as f:
            if self.errors:
                f.write("## 🔴 Validation Errors\n\n")
                f.write("The following errors must be fixed before your contribution can be merged:\n\n")
                for error in self.errors:
                    f.write(f"{error}\n\n")
            
            if self.warnings:
                f.write("## 🟡 Validation Warnings\n\n")
                f.write("The following issues were found (these won't block your PR but should be addressed):\n\n")
                for warning in self.warnings:
                    f.write(f"{warning}\n\n")
            
            f.write("\n---\n\n")
            f.write("### 💡 Tips for fixing issues:\n\n")
            f.write("- Use the format: `- [Your Name](https://github.com/yourusername)`\n")
            f.write("- Make sure there's no space between `]` and `(`\n")
            f.write("- Use `https://` in your GitHub URL\n")
            f.write("- Replace any placeholder text with your actual information\n")
            f.write("- Check for typos in 'github.com'\n")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validate Contributors.md formatting and content'
    )
    parser.add_argument(
        '--file',
        default='Contributors.md',
        help='Path to Contributors.md file (default: Contributors.md)'
    )
    parser.add_argument(
        '--output',
        default='validation_errors.txt',
        help='Output file for validation results (default: validation_errors.txt)'
    )
    
    args = parser.parse_args()
    
    validator = ContributorValidator(args.file)
    is_valid = validator.validate()
    validator.print_results()
    
    # Save results to file for GitHub Actions
    validator.save_results_to_file(args.output)
    
    # Exit with appropriate code
    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
