import re

with open('docs/translations/Translations.md', 'r') as f:
    translations_content = f.read()

# This regex will find all instances of README.anything.md
filenames = re.findall(r'README\.[a-zA-Z\._-]+\.md', translations_content)

for filename in sorted(set(filenames)):
    print(filename)
