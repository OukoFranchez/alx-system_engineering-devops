# 0x02-shell_directions
It has commands to do with shell redirections and filters
## 12. What’s new
Create a script that displays the 10 newest files in the current directory.

Requirements:

One file per line
Sorted from the newest to the oldest

ls -1t | head -n 10

This command uses the ls command with the -t option to sort the files by modification time, newest first. The -1 option is used to list one file per line. The head command is then used with the -n option to display only the first 10 files in the list, which are the newest files.

