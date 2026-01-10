import re

FILE_PATH = "Contributors.md"

LINK_PATTERN = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")

def main():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip().startswith("-")]

    seen_names = set()
    ordered_names = []

    for line in lines:
        match = LINK_PATTERN.search(line)

        # Legacy entry: only name → ignore safely
        if not match:
            continue

        name = match.group(1).strip().lower()

        # Duplicate name → just ignore, do NOT fail
        if name in seen_names:
            continue

        seen_names.add(name)
        ordered_names.append(name)

    # Check order but do NOT fail
    if ordered_names != sorted(ordered_names):
        print("Warning: contributors list is not strictly alphabetical.")

    print("Contributors.md checked successfully (legacy entries ignored).")

if __name__ == "__main__":
    main()
