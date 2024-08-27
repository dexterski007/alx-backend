#!/bin/bash

# Check if a directory is provided
if [ $# -eq 0 ]; then
    echo "Please provide a directory path"
    exit 1
fi

# Directory to check
DIR="$1"

# Function to check if a string is a sentence
is_sentence() {
    local str="$1"
    # Check if the string has at least 3 words and ends with a period
    [[ "$str" =~ ^[A-Z][a-zA-Z0-9\ \'\",.!?-]{20,}\.$ ]]
}

# Loop through all Python files in the directory
for file in "$DIR"/*.py; do
    if [ -f "$file" ]; then
        echo "Checking file: $file"
        
        # Check shebang
        if ! head -n 1 "$file" | grep -q "^#!/usr/bin/env python3$"; then
            echo "  ERROR: First line should be exactly '#!/usr/bin/env python3'"
        fi
        
        # Check if file is executable
        if [ ! -x "$file" ]; then
            echo "  ERROR: File is not executable"
        fi
        
        # Check module documentation, class documentation, function documentation, and type annotations
python3 << EOF
import ast
import re

def is_sentence(s):
    return bool(re.match(r'^[A-Z][a-zA-Z0-9\ \'\",.!?-]{20,}\.$', s))

def check_docstring(node):
    if not (isinstance(node, ast.ClassDef) or isinstance(node, ast.FunctionDef)):
        return
    if not ast.get_docstring(node) or not is_sentence(ast.get_docstring(node)):
        print(f"  ERROR: {'Class' if isinstance(node, ast.ClassDef) else 'Function'} documentation missing or invalid for {node.name}")

def check_type_annotations(node):
    if not isinstance(node, ast.FunctionDef):
        return
    if not node.returns or any(arg.annotation is None for arg in node.args.args):
        print(f"  ERROR: Function {node.name} is missing type annotations")

with open("$file", "r") as source:
    tree = ast.parse(source.read())

module_doc = ast.get_docstring(tree)
if not module_doc or not is_sentence(module_doc):
    print("  ERROR: Module documentation missing or invalid")

for node in ast.walk(tree):
    check_docstring(node)
    check_type_annotations(node)
EOF
        
        echo "Done checking $file"
        echo
    fi
done
