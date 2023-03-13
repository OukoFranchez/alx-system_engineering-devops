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
