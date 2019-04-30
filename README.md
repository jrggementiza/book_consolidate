# File Consolidate
## Description
A Simple Script that moves specified files from a target folder and subfolders to a destination folder.

## Usage
```
$ python consolidate.py /path/to/target_folder /path/to/destination_folder filetype_1 filetype_2 filetype_n
```

## Filetypes Tested on
- .pdf
- .epub

## Known Issues
- [Bug] - When moving locked files, creates an undeleteable copy to destination folder. Temporary solution:
``` $ sudo rm -rf path/to/locked_file.copy```

## TO DO
- [Bug] - Issue about locked files
- [Try] - on other filetypes
- [Add] - Tests (TDD yo)
- [Feature] - Log Files
- [Feature] - Better way to handle terminal arguements
- [Feature] - Progress Prompts
- [Feature] - Make it reusable to another machine
- [Feature] - Option to delete target_folder if empty

## Updates
- Cleaned up code
- Added a README (yey markdown!)
