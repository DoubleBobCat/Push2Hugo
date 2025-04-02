import json
import os
from pathlib import Path


def process_line(line: str) -> str:
    """
    Process a single line according to the specified rules.
    Returns the modified line with appropriate formatting.
    """
    callback = line
    if config["functionSwitcher"]["addDoubleSpace"]:
        callback = callback.rstrip('\n') + "  \n"
    if config["functionSwitcher"]["addLineBreak"]:
        callback = callback.rstrip('\n') + "\n\n"
    return callback


def main():
    """
    Main function that executes the file processing workflow.
    """
    global config

    # Load configuration
    with open('config.json', 'r') as c_f:
        config = json.load(c_f)

    input_folder = Path(config["inputFolder"])
    output_folder = Path(config["outputFolder"])

    # Process all markdown files in input directory
    for md_file in input_folder.rglob('*.md'):
        # Skip specified files
        if md_file.stem in config["ignoreFileName"]:
            continue
        # Create output path
        output_path = os.path.join(output_folder, os.path.basename(md_file))

        # Read and process file
        with open(md_file, 'r', encoding='utf-8') as i_f:
            lines = i_f.readlines()

        processed_lines = []
        special_flag = False
        for line in lines:
            stripped_line = line.lstrip()
            # print(special_flag, stripped_line, end="")
            if stripped_line[:3] in ["---", "```"]:
                if special_flag:
                    special_flag = False
                else:
                    special_flag = True
                processed_lines.append(line)
            elif special_flag:
                processed_lines.append(line)
            elif len(stripped_line) == 0:
                processed_lines.append(line)
            elif stripped_line[0] in ['#', '+', '-', '*', '|']:
                processed_lines.append(line)
            else:
                processed_lines.append(process_line(line))
        i_f.close()
        # Write processed content
        with open(output_path, 'w', encoding='utf-8') as o_f:
            o_f.writelines(processed_lines)
        o_f.close()


if __name__ == '__main__':
    main()
