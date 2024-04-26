
#File Handling: Opening, Reading, Writing, and CLosing Files

#Features:
#-- Data Persistence
#-- Data Exchange - Translating Data through languages
#-- Data Organization
#-- Automation of Data Manipulation



#Everything Starts by opening a file with open(file_path, mode)



#----- File Path is like the address to your to your file ------

#-- Relative Path : the path from the file you are in, to the file you are going to 
#(use \\ on windows)

#ex: .\\example\\example.py 

#mac: ./example/example.py

#-- Absolute Path : The complete directory path starting from the root drive 

#   C:\\Users\\Dylan\\Documents\\Backend-Core\\week-3\\day-4\\example\\example.py

#MacOS starts from root folder

# /Users/YourUsername/Documents/Backend-Core.week-3/day-3/example/example.py


#------ File Opening Modes ------

#-- 'r' : read only mode, lets you view the contents of a file. If the file doesn't
#exits will throw a FileNotFoundError

#-- 'w' : write only mode,creates file if one doesn't exist at the path
#WARNING: automatically overwrite file contents

#-- 'a' : append mode, let's you add to files without overwriting, if a file 
#doesnt exist it will create a fresh file.

#----- advanced modes -----

#-- 'r+' : Allows you to read and write to a file (writing to the file still overwrites)
#   Good for altering data

#-- 'w+' : Instantly overwrites file, allows you to write to file and also read the file
#   Good for starting fresh

#-- 'a+' : Opens file for both adding data and reading data
