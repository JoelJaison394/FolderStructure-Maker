# Folder Structure Maker

This Python script reads a YAML file containing a folder structure and creates the specified folders and files accordingly. It is a handy tool for automating the creation of folder hierarchies based on a structured YAML configuration.

## Prerequisites

- Python 3
- PyYAML library

```bash
pip install pyyaml

## Usage

1. Create a YAML file (`folder_structure.yaml`) specifying the desired folder structure.
2. Run the script:

   ```bash
   python create_folders.py

## YAML File Format

The YAML file should have a list of dictionaries, where each dictionary represents a folder and its content. Example:

```yaml
- filename: folder1
  content:
    subfolder1_1:
      file1_1_1.txt: "content for file1_1_1"
      file1_1_2.txt: "content for file1_1_2"
    subfolder1_2:
      file1_2_1.txt: "content for file1_2_1"
- filename: folder2
  content:
    file2_1.txt: "content for file2_1"
    file2_2.txt: "content for file2_2"
- filename: folder3
  content: {}

## Features

- Creates folders and files based on a YAML configuration.
- Handles various error scenarios during folder creation.
- Supports nested folder structures.

## Additional Notes

- Ensure the YAML file is correctly formatted with proper indentation.
- Use caution when running the script, especially with elevated permissions, as it may create or modify folders on your system.

