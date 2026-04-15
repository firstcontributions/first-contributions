import re

with open('docs/translations/Translations.md', 'r') as f:
    translations_content = f.read()

correct_filenames = set(re.findall(r'README\.[a-z-]+\.md', translations_content))

with open('current_filenames.txt', 'r') as f:
    current_filenames = set(line.strip() for line in f)

incorrect_filenames = current_filenames - correct_filenames

for filename in incorrect_filenames:
    print(filename)
