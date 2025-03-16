# File Renamer Script

A simple Python script to batch rename files in a directory with a custom prefix. This tool is useful for organizing files, adding consistent naming conventions, or preparing files for processing.

## Features
- Renames all files in a specified directory.
- Adds a user-defined prefix to each file name.
- Preserves the original file extensions.
- Skips hidden files and subdirectories.
- Handles errors properly (e.g., permission issues or duplicate file names).

## Usage
1. Clone the repository or download the script.
2. Run the script:

   python rename_files.py
   
4. Enter the directory path and the desired prefix when prompted.
5. The script will rename all files in the directory and display the changes.

## Example

Input:
- Enter the folder path: /path/to/your/folder
- Enter the prefix for renaming: myfile
  
Output:
- Renamed: file1.txt -> myfile_1.txt
- Renamed: file2.jpg -> myfile_2.jpg
