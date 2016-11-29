#!/usr/bin/python

#============================================
import os

path = "C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading"

# Check current working directory.
retval = os.getcwd()
print ("Current working directory %s" % retval)

# Now change the directory : 작업 폴더의 경로를 바꾸는 명령어
os.chdir( path )

# Check current working directory.
retval = os.getcwd()
print ("Directory changed successfully %s" % retval)



#============================================
# chmod()
'''
Description
The method chmod() changes the mode of path to the passed numeric mode. The mode may take one of the following values or bitwise ORed combinations of them:
stat.S_ISUID: Set user ID on execution.
stat.S_ISGID: Set group ID on execution.
stat.S_ENFMT: Record locking enforced.
stat.S_ISVTX: Save text image after execution.
stat.S_IREAD: Read by owner.
stat.S_IWRITE: Write by owner.
stat.S_IEXEC: Execute by owner.
stat.S_IRWXU: Read, write, and execute by owner.
stat.S_IRUSR: Read by owner.
stat.S_IWUSR: Write by owner.
stat.S_IXUSR: Execute by owner.
stat.S_IRWXG: Read, write, and execute by group.
stat.S_IRGRP: Read by group.
stat.S_IWGRP: Write by group.
stat.S_IXGRP: Execute by group.
stat.S_IRWXO: Read, write, and execute by others.
stat.S_IROTH: Read by others.
stat.S_IWOTH: Write by others.
stat.S_IXOTH: Execute by others.

Syntax
Following is the syntax for chmod() method:

os.chmod(path, mode);

Parameters
path -- This is the path for which mode would be set.
mode -- This may take one of the above mentioned values or bitwise ORed combinations of them.

Return Value
This method does not return any value.

Example
The following example shows the usage of chmod() method:

#!/usr/bin/python
'''
import os, stat

# Assuming /tmp/foo.txt exists, Set a file execute by the group.

os.chmod("/tmp/foo.txt", stat.S_IXGRP)

# Set a file write by others.
os.chmod("/tmp/foo.txt", stat.S_IWOTH)

print ("Changed mode successfully!!")
'''
When we run above program, it produces following result:

Changed mode successfully!!
'''
'''
#============================================
Description
The method chown() changes the owner and group id of path to the numeric uid and gid. To leave one of the ids unchanged, set it to -1.To set ownership, you would need super user privilege..

Syntax
Following is the syntax for chown() method:

os.chown(path, uid, gid);
Parameters
path -- This is the path for which owner id and group id need to be setup.

uid -- This is Owner ID to be set for the file.

gid -- This is Group ID to be set for the file.

Return Value
This method does not return any value.

Example
The following example shows the usage of chown() method.


When we run above program, it produces following result:

Changed ownership successfully!!
#============================================
'''
#!/usr/bin/python :os.chown()

import os

# Assuming /tmp/foo.txt exists.
# To set owner ID 100 following has to be done.
os.chown("/tmp/foo.txt", 100, -1)

print ("Changed ownership successfully!!")

#============================================

#!/usr/bin/python : os.listdir( path )

import os, sys

# Open a file
path = "C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print (file)

#============================================

# os.makedir() or  os.makedirs()
import os
path = "c:\\temp\\test python\\test2"
os.makedir(path)                     # 존재하는 경로에 폴더를 생성

import os
path = "c:\\temp\\test python\\test\\test"
os.makedirs(path)                    # 설정된 경로가 존재하지 않으면 경로까지 생성

#============================================
# link()  : 존재하는 파일의 복사 및 붙여 넣기

import os
'''
path = "c:\\temp\\test python\\test\\test.txt"
fd= os.open(path, os.O_RDWR|os.O_CREAT)
os.close(fd)
'''
path = "c:\\temp\\test python\\test\\test.txt"
dst = "c:\\temp\\test python\\test\\test\\test1.txt"
os.link(path, dst)

#============================================





#============================================






#============================================






#============================================





#============================================







