#!/bin/bash

# Path to the cards directory and output file
CARDS_DIR="contributors"
OUTPUT_FILE="scripts/contributors.js"

# Check if the cards directory exists
if [ ! -d "$CARDS_DIR" ]; then
  echo "Error: Directory $CARDS_DIR does not exist."
  exit 1
fi

# Start generating the JavaScript array
echo "const contributorFiles = [" > "$OUTPUT_FILE"

# List all HTML files in the cards directory
find "$CARDS_DIR" -type f -name "*.html" | sed "s|^$CARDS_DIR/|  \"|; s|$|\",|" >> "$OUTPUT_FILE"

# Close the JavaScript array
echo "];" >> "$OUTPUT_FILE"

echo "$OUTPUT_FILE generated successfully with $(ls -1 $CARDS_DIR/*.html | wc -l | xargs) files."

