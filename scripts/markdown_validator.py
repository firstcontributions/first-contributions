import os
import re
from datetime import datetime

LOG_FILE = "markdown_validation_log.txt"

def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def check_trailing_whitespace(line, line_num, file):
    if line.rstrip('\n').endswith(' '):
        log(f"[Trailing whitespace] {file}:{line_num}")

def check_empty_links(line, line_num, file):
    if re.search(r'\[\]\(\)', line):
        log(f"[Empty link] {file}:{line_num}")

def check_images_without_alt(line, line_num, file):
    if re.search(r'!\[\]\(', line):
        log(f"[Image missing alt text] {file}:{line_num}")

def check_heading_levels(prev_level, line, line_num, file):
    match = re.match(r'^(#+)', line)
    if match:
        level = len(match.group(1))
        if prev_level and level > prev_level + 1:
            log(f"[Skipped heading level] {file}:{line_num}")
        return level
    return prev_level

def scan_file(filepath):
    prev_heading = None

    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):

            check_trailing_whitespace(line, i, filepath)
            check_empty_links(line, i, filepath)
            check_images_without_alt(line, i, filepath)

            prev_heading = check_heading_levels(prev_heading, line, i, filepath)

def scan_markdown_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                scan_file(os.path.join(root, file))

if __name__ == "__main__":
    log(f"\n--- Validation Run: {datetime.now()} ---")
    scan_markdown_files(".")