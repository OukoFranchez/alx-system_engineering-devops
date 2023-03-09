0x01. Shell, permissions







12-directory_permissions
mkdir -m 751 my_dir
This command uses the mkdir command to create a new directory named my_dir in the working directory. The -m option specifies the permissions to set on the new directory, with 751 indicating that the owner should have full access (7), the group should have read and execute access (5), and others should have execute access only (1).

When you run this command, a new directory named my_dir will be created in the current working directory with the specified permissions.
