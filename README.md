This script re-formats text files by cutting the line length down (to approximately 110 characters by default).  
The script does not remove characters, it only inserts new lines at the next space after the character limit.  

Requirements:
Python 3
All python libraries used are pre-packaged with python as part of the os library

To use:
download the main.py file  
`py main.py`  
You will be prompted to specify a path for the script to work inside  
You will be prompted to specify if the script should look in subdirectories (Y/N)  
You will be prompted to specify if the script should delete the original files when it is finished (Y/N)  


To override the prompts, set the path, subdirectories and remove_files variables on line 8,9 and 10.  
By default, reformatted text files will be suffixed with `[text reformatted]` ,  this can be changed by editing line 46.
