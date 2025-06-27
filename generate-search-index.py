#!/usr/bin/env python3
"""
Tutorial Search Index Generator
Automatically scans the repository and generates a search index for tutorials.
"""

import os
import json
import re
from pathlib import Path

def extract_language_from_filename(filename):
    """Extract language code from filename patterns"""
    # Common language patterns in filenames
    patterns = {
        'zh-cn': 'chinese',
        'pt-br': 'portuguese',
        'pt_br': 'portuguese',
        'pt-pt': 'portuguese',
        'hi': 'hindi',
        'ur': 'urdu',
        'id': 'indonesian',
        'ta': 'tamil',
        'ml': 'malayalam',
        'fr': 'french',
        'es': 'spanish',
        'gr': 'greek',
        'ua': 'ukrainian',
        'marathi': 'marathi',
        'kannada': 'kannada',
        'gujarati': 'gujarati',
        'sinhala': 'sinhala',
        'francais': 'french',
        'Hindi': 'hindi',
        'Urdu': 'urdu',
        'ng_yo': 'yoruba',
        'ng_yr': 'yoruba',
        'np': 'nepali',
        'cn': 'chinese',
        'vn': 'vietnamese',
        'th': 'thai',
        'fa': 'persian'
    }
    
    filename_lower = filename.lower()
    for pattern, language in patterns.items():
        if pattern.lower() in filename_lower:
            return language
    
    return 'english'

def extract_tool_from_filename(filename):
    """Extract tool name from filename"""
    filename_lower = filename.lower()
    
    # Tool patterns
    if 'github-desktop' in filename_lower:
        return 'github-desktop'
    elif 'github-cli' in filename_lower:
        return 'github-cli'
    elif 'git-bash' in filename_lower:
        return 'git-bash'
    elif 'git-cli' in filename_lower:
        return 'git-cli'
    elif 'intellij' in filename_lower:
        return 'intellij'
    elif 'vs-code' in filename_lower or 'vscode' in filename_lower:
        return 'vscode'
    elif 'vs2017' in filename_lower:
        return 'visual-studio'
    elif 'gitkraken' in filename_lower:
        return 'gitkraken'
    elif 'sourcetree' in filename_lower:
        return 'sourcetree'
    elif 'sublime-merge' in filename_lower:
        return 'sublime-merge'
    else:
        return 'general'

def generate_title_from_filename(filename):
    """Generate a readable title from filename"""
    # Remove extension
    name = os.path.splitext(filename)[0]
    
    # Replace hyphens and underscores with spaces
    name = name.replace('-', ' ').replace('_', ' ')
    
    # Capitalize words
    words = name.split()
    title_words = []
    
    for word in words:
        if word.lower() in ['cli', 'gui', 'vs', 'ide', 'ui', 'os']:
            title_words.append(word.upper())
        elif word.lower() == 'github':
            title_words.append('GitHub')
        elif word.lower() == 'macos':
            title_words.append('macOS')
        elif word.lower() == 'windows':
            title_words.append('Windows')
        else:
            title_words.append(word.capitalize())
    
    return ' '.join(title_words)

def scan_tutorials():
    """Scan the repository for tutorial files"""
    tutorials = []
    base_path = Path('.')
    
    # Define directories to scan
    scan_dirs = [
        ('docs/cli-tool-tutorials', 'cli'),
        ('docs/gui-tool-tutorials', 'gui'),
        ('docs/additional-material', 'additional')
    ]
    
    for dir_path, category in scan_dirs:
        full_path = base_path / dir_path
        if not full_path.exists():
            continue
            
        # Scan all .md files recursively
        for md_file in full_path.rglob('*.md'):
            relative_path = md_file.relative_to(base_path)
            filename = md_file.name
            
            # Skip certain files
            if filename.lower() in ['readme.md', 'index.md']:
                continue
            
            # Extract information
            tool = extract_tool_from_filename(filename)
            language = extract_language_from_filename(filename)
            title = generate_title_from_filename(filename)
            
            # Generate description
            if category == 'cli':
                description = f"Command line tutorial using {tool.replace('-', ' ').title()}"
            elif category == 'gui':
                description = f"Graphical interface tutorial using {tool.replace('-', ' ').title()}"
            else:
                description = "Additional resources and guides for open source contribution"
            
            if language != 'english':
                description += f" (in {language.title()})"
            
            tutorial = {
                'title': title,
                'path': str(relative_path).replace('\\', '/'),  # Ensure forward slashes
                'category': category,
                'tool': tool,
                'language': language,
                'description': description
            }
            
            tutorials.append(tutorial)
    
    # Add main documentation files
    main_docs = [
        {
            'title': 'How to Contribute to Open Source Projects',
            'path': 'docs/how-to-contribute-to-open-source-projects.md',
            'category': 'additional',
            'tool': 'general',
            'language': 'english',
            'description': 'Comprehensive guide on contributing to open source projects'
        }
    ]
    
    tutorials.extend(main_docs)
    
    # Sort tutorials by title
    tutorials.sort(key=lambda x: x['title'])
    
    return tutorials

def update_search_html(tutorials):
    """Update the search.html file with new tutorial data"""
    search_file = Path('search.html')
    if not search_file.exists():
        print("search.html not found. Please create it first.")
        return
    
    # Read the current file
    with open(search_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate JavaScript array
    js_tutorials = "const tutorials = " + json.dumps(tutorials, indent=12) + ";"
    
    # Replace the tutorials array in the file
    # Find the start and end of the tutorials array
    start_pattern = r'const tutorials = \['
    end_pattern = r'\];'
    
    start_match = re.search(start_pattern, content)
    if not start_match:
        print("Could not find tutorials array in search.html")
        return
    
    # Find the matching closing bracket
    start_pos = start_match.start()
    bracket_count = 0
    end_pos = start_pos
    
    for i, char in enumerate(content[start_pos:], start_pos):
        if char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_pos = i + 1
                break
    
    # Replace the tutorials array
    new_content = content[:start_pos] + js_tutorials + content[end_pos + 1:]
    
    # Write the updated file
    with open(search_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated search.html with {len(tutorials)} tutorials")

def main():
    """Main function"""
    print("Scanning repository for tutorials...")
    tutorials = scan_tutorials()
    
    print(f"Found {len(tutorials)} tutorials")
    
    # Save to JSON file for reference
    with open('tutorials-index.json', 'w', encoding='utf-8') as f:
        json.dump(tutorials, f, indent=2, ensure_ascii=False)
    
    print("Saved tutorials index to tutorials-index.json")
    
    # Update search.html
    update_search_html(tutorials)
    
    # Print summary
    categories = {}
    tools = {}
    languages = {}
    
    for tutorial in tutorials:
        categories[tutorial['category']] = categories.get(tutorial['category'], 0) + 1
        tools[tutorial['tool']] = tools.get(tutorial['tool'], 0) + 1
        languages[tutorial['language']] = languages.get(tutorial['language'], 0) + 1
    
    print("\nSummary:")
    print(f"Categories: {dict(sorted(categories.items()))}")
    print(f"Tools: {dict(sorted(tools.items()))}")
    print(f"Languages: {len(languages)} different languages")

if __name__ == '__main__':
    main()