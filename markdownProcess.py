import json
import os
from pathlib import Path

def process_line(line: str) -> str:
    """
    Process a single line according to the specified rules.
    Returns the modified line with appropriate formatting.
    """
    stripped_line = line.lstrip()
    if stripped_line.startswith(('#', '+', '-', '*')):
        return line
    processed = line.rstrip('\n') + '  \n'
    return processed

def main():
    """
    Main function that executes the file processing workflow.
    """
    # Load configuration
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    input_folder = Path(config['inputFolder'])
    output_folder = Path(config['outputFolder'])
    
    # Process all markdown files in input directory
    for md_file in input_folder.rglob('*.md'):
        # Skip specified files
        if md_file.stem in ['controller', 'Template']:
            continue
            
        # Create output path
        relative_path = md_file.relative_to(input_folder)
        output_path = output_folder / relative_path
        
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Read and process file
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        processed_lines = [process_line(line) for line in lines]
        
        # Write processed content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)

if __name__ == '__main__':
    main()