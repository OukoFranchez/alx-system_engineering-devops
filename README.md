# 👽alx-system_engineering-devops👽
## ♠️0x00-shell_basics♠️
Has command on shell basics
### 0. Where am I?
!/bin/bash
pwd

a script that prints the absolute path name of the current working directory.
### 1. What’s in there?
!/bin/bash
ls

Display the contents list of your current directory.
### 2. There is no place like home
!/bin/bash
cd

a script that changes the working directory to the user’s home directory.

### 3. The long format
!/bin/bash
ls -l

Display current directory contents in a long format
### 4. Hidden files
!/bin/bash
ls -la

Display current directory contents, including hidden files (starting with .). Using the long format.
### 5. I love numbers
!/bin/bash
ls -lan

Display current directory contents.

Long format
with user and group IDs displayed numerically
And hidden files (starting with .)
### 6. Welcome
!/bin/bash
mkdir /tmp/ my_first_directory

a script that creates a directory named my_first_directory in the /tmp/ directory.
### 7. Betty in my first directory
!/bin/bash
mv /tmp/betty /tmp/my_first_directory/

Move the file betty from /tmp/ to /tmp/my_first_directory
### 8. Bye bye Betty
!/bin/bash
rm /tmp/my_first_directory/betty

Delete the file betty.

The file betty is in /tmp/my_first_directory
### 9. Bye bye My first directory
!/bin/bash
rm -r /tmp/my_first_directory

Delete the directory my_first_directory that is in the /tmp directory.
### 10. Back to the future
!/bin/bash
cd -

script changing the working directory to the previous one
### 11. Lists
!/bin/bash
ls -la . .. /boot

a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
### 12. File type
!/bin/bash
file /tmp/iamafile

a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
### 13. We are symbols, and inhabit symbols
!/bin/bash
ln -s /bin/ls __ls__

The command "ln -s /bin/ls ls" creates a symbolic link from the file "ls" to the file "/bin/ls".

The "-s" option indicates that a symbolic link should be created, rather than a hard link. Symbolic links are similar to shortcuts in Windows; they are files that act as pointers to other files or directories.

So, when you type "ls" in the command line, it will actually execute the "/bin/ls" command because of the symbolic link created by this command.
### 14. Copy HTML files
!/bin/bash
cp -u --recursive --no-clobber --update *.html

The command "cp -u --recursive --no-clobber --update *.html .." copies all the HTML files (files with extension ".html") in the current directory and its subdirectories to the parent directory (denoted by "..").
"-u" or "--update" option copies only when the source file is newer than the destination file or when the destination file does not exist. This option ensures that only newer or missing files are copied to the destination directory.

"--recursive" option enables recursive copying of directories and their contents.

"--no-clobber" option prevents existing files in the destination directory from being overwritten. This option ensures that files in the destination directory are not accidentally overwritten by files with the same name from the source directory.

"*.html" specifies the pattern for files to be copied. In this case, only files with the ".html" extension will be copied.

".." specifies the destination directory. In this case, the copied files will be placed in the parent directory.

*So, the end result is that all the HTML files in the current directory and its subdirectories that are newer than their counterparts in the destination directory will be copied to the parent directory without overwriting any existing files.
### 15. Let’s move
!/bin/bash
mv [A-Z]* /tmp/u*

The command "mv [A-Z]* /tmp/u" moves all files in the current directory that start with an uppercase letter to the directory "/tmp/u".

Here's what each part of the command means:

"mv" stands for "move" and is the command used to move files.

"[A-Z]*" is a pattern that matches all files that start with an uppercase letter. The square brackets indicate a character set, and the dash between A and Z specifies a range of characters. The asterisk after the character set matches zero or more of any character.

"/tmp/u" is the destination directory where the matched files will be moved.

So, when you run this command, any file in the current directory that starts with an uppercase letter will be moved to the "/tmp/u" directory. Note that this command does not preserve the directory structure of the moved files, so any subdirectories containing uppercase files will be ignored.

### 16. Clean Emacs
!/bin/bash
rm *~

a script that deletes all files in the current working directory that end with the character ~.*

### 17. Tree
!/bin/bash
mkdir -p welcome/to/school

The command "mkdir -p welcome/to/school" creates a new directory called "welcome" and creates any necessary parent directories ("to" and "school") as needed.

Here's what each part of the command means:

"mkdir" stands for "make directory" and is the command used to create new directories.

"-p" is an option that tells mkdir to create the entire directory path, including any necessary parent directories. If the parent directories already exist, they will not be recreated.

"welcome/to/school" is the directory path to be created.

So, when you run this command, a directory named "welcome" will be created in the current directory, along with a subdirectory named "to" inside "welcome", and a subdirectory named "school" inside "to". If any of these directories already exist, they will not be recreated.

### 18. Life is a series of commas, not periods
!/bin/bash
ls -paxm

The command "ls -paxm" lists the files and directories in the current directory in a comma-separated, multiline format, including hidden files and directories.

Here's what each option means:

"ls" stands for "list" and is the command used to list the files and directories in a directory.

"-p" option adds a slash "/" to the end of directory names, making it easy to distinguish directories from files.

"-a" option lists all files and directories, including hidden ones (those that begin with a dot).

"-x" option lists the files and directories in a line rather than in columns.

"-m" option separates the entries with commas.

So, when you run this command, it will display a list of files and directories in the current directory in a comma-separated, multiline format. Directories will have a slash "/" at the end of their name, and hidden files and directories will also be included in the list.
### 19. File type: School
0 string SCHOOL School data
!:mime School

file -C -m school.mgc
These are two lines of code from a "magic" file.

The "magic" file is a configuration file used by the Unix file command to identify the type of a file based on its contents, rather than relying on its filename extension.

Here's what each line of the code means:

"0 string SCHOOL School data": This line specifies that the file is recognized as a "School" file if the first 6 bytes of the file (offset 0) contain the ASCII string "SCHOOL".

"!:mime School": This line specifies that if the file is recognized as a "School" file, it should be labeled with the MIME type "School". The exclamation mark before the colon indicates that this is a "soft" match, meaning that if the file matches the pattern but fails other tests, it will not be labeled with this MIME type.

So, if a file is recognized as a "School" file based on the contents of its first 6 bytes, the file command will label it with the MIME type "School"


## 0x01-shell_permissions
Has shell commands on permissions
Learning creating an alias 
