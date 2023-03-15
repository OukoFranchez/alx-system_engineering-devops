# 0x02-shell_directions
It has commands to do with shell redirections and filters
## 12. What’s new
Create a script that displays the 10 newest files in the current directory.

Requirements:

One file per line
Sorted from the newest to the oldest

ls -1t | head -n 10

This command uses the ls command with the -t option to sort the files by modification time, newest first. The -1 option is used to list one file per line. The head command is then used with the -n option to display only the first 10 files in the list, which are the newest files.
## 13. Being unique is better than being perfect
Create a script that takes a list of words as input and prints only words that appear exactly once.

Input format: One line, one word
Output format: One line, one word
Words should be sorted

sort | uniq -u

This command uses the sort command to sort the input words in alphabetical order. The sorted list of words is then passed to the uniq command with the -u option to display only the unique words that appear exactly once.
## 14. It must be in that file
Display lines containing the pattern “root” from the file /etc/passwd

grep "root" /etc/passwd

This command searches for lines containing the pattern "root" in the file /etc/passwd.
## 15. Count that word
Display the number of lines that contain the pattern “bin” in the file /etc/passwd

grep -c "bin" /etc/passwd

The -c option of grep is used to count the number of matches. So, the command grep -c "bin" /etc/passwd will output the number of lines that contain the pattern "bin" in the file /etc/passwd.
## 16. What's next?
Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

grep -A 3 "root" /etc/passwd

This uses the -A option of grep to specify the number of lines after the matching pattern to include in the output. In this case, we specify 3 to include 3 lines after each line that contains the pattern "root" in the /etc/passwd file.
## 17. I hate bins
Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

grep -v "bin" /etc/passwd

## 18. Letters only please
Display all lines of the file /etc/ssh/sshd_config starting with a letter.

include capital letters as well

grep ^[[:alpha:]] /etc/ssh/sshd_config

The regular expression ^[[:alpha:]] is composed of two parts:

^ - This is the anchor for the beginning of the line. It tells the regular expression to match only at the beginning of the line.

[[:alpha:]] - This is a character class that matches any alphabetic character, both uppercase and lowercase. The character class is enclosed in square brackets, which tells the regular expression to match any character that falls within the class.

So when we combine these two parts, we get a regular expression that matches any line in the /etc/ssh/sshd_config file that begins with an alphabetic character, whether uppercase or lowercase. This is because the regular expression starts at the beginning of the line and matches any character that falls within the alphabetic character class.
## 19. A to Z
Replace all characters A and c from input to Z and e respectively.

tr 'Ac' 'Ze' 

## 20. Without C, you would live in hiago
Create a script that removes all letters c and C from input.

tr -d 'Cc'

The tr command can be used to remove characters from input.
Here, the -d option is used to delete (remove) characters. The characters to be deleted are specified as the argument to the option, in this case 'cC'.

## 21. esreveR
Write a script that reverse its input

rev

## 22. DJ Cut Killer
Write a script that displays all users and their home directories, sorted by users.

Based on the the /etc/passwd file

cut -f 1,6 -d ':' /etc/passwd | sort

The above command extracts the first and sixth fields from the /etc/passwd file using the cut command, where the fields are separated by colons (:). The first field is the username and the sixth field is the home directory. The output of cut is then piped to the sort command, which sorts the lines alphabetically by the first field (i.e., the username). The final output shows the list of all users and their home directories, sorted by the usernames.

## 23. Empty casks make the most noise
Write a command that finds all empty files and directories in the current directory and all sub-directories.

Only the names of the files and directories should be displayed (not the entire path)
Hidden files should be listed
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep

find . -empty -printf "%f\n"

This command uses the find command to search for all empty files and directories in the current directory and its sub-directories. The -empty option tells find to only include empty files and directories in the search. The -printf option specifies the format of the output. %P is used to print the name of the file or directory relative to the starting directory, and \n adds a new line after each result. The -printf option is more efficient than using -exec to execute a separate command for each result.

## 24. A gif is worth ten thousand words
Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

Hidden files should be listed
Only regular files (not directories) should be listed
The names of the files should be displayed without their extensions
The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep

find . -type f -name "*.gif" -printf "%f\n" | rev | cut -c 5- | rev | sort -f

*This command finds all files with the extension .gif in the current directory and all its subdirectories, prints their file name without the extension, sorts the names in a case-insensitive manner and then displays them.

Here is a breakdown of the command:

find .: starts a find command in the current directory and all subdirectories
-type f: limits the search to regular files (excluding directories, sockets, etc.)
-name "*.gif": *searches for files with the .gif extension
-printf "%f\n": prints only the file name (not the entire path) followed by a newline character
rev: reverses each line of output
cut -c 5-: removes the last four characters of each line (i.e., the .gif extension)
rev: reverses each line back to its original order
sort -f: sorts the lines in a case-insensitive manner



