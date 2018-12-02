# file_formater
Formats original text files into proper csv

## Usage
The script takes a folder contaning raw text files and reformats then into a new files with proper csv format
The script creates the new files into a folder folder in the same relative localtion as the oiginal folder.

example: SubjectData25Nov -> new_SubjectData25Nov . 

Folder path of the raw files is relative to the the script location.
Original folder and files are preserved/not modified

## Using Command line
Option 1 : pass in argument of folder path conating raw files
python file_formatter.py <folder_path_raw_files> . 


Option 2:
update the FOLDER_PATH variable to correspnd to folder_path_raw_files
you don't need to include an argument in this case
python file_formatter.py 
