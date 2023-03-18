# 0x01. Shell, permissions
Has shell permission commands






## 12-directory_permissions

mkdir -m 751 my_dir
This command uses the mkdir command to create a new directory named my_dir in the working directory. The -m option specifies the permissions to set on the new directory, with 751 indicating that the owner should have full access (7), the group should have read and execute access (5), and others should have execute access only (1).

When you run this command, a new directory named my_dir will be created in the current working directory with the specified permissions.

## 13-change_group

chgrp school hello
This command uses the chgrp command to change the group ownership of the file hello to the group named school. The new group ownership will apply to the file henllo only.

Note that to use this command, you must have permission to change the group ownership of the file. If you are not the owner of the file or a member of the existing group ownership, you may need to use sudo or obtain permission from the file owner or system administrator.

## 101-symbolic_link_permissions

chown -h vincent:staff _hello
In this command, the "-h" option is used to modify the ownership of the symbolic link itself rather than the file or directory it points to. Without the "-h" option, the ownership of the file or directory pointed to by the symbolic link would be modified instead.
