# Importing the os Module
import os

# Importing the subprocess Module
import subprocess

# Importing platform to identify the OS
import platform

# Determine the current operating system
current_os = platform.system()

# Define the appropriate command for listing directory contents
if current_os == "Windows":
    list_dir_command = ["cmd", "/c", "dir"]
else:
    list_dir_command = ["ls"]

# Running a directory listing command using os.system()
os.system(" ".join(list_dir_command))

# Running a directory listing command using subprocess.run()
subprocess.run(list_dir_command)

# Using subprocess.run() with an additional argument for long listing format
if current_os == "Windows":
    list_dir_long_command = ["cmd", "/c", "dir"]
else:
    list_dir_long_command = ["ls", "-l"]

subprocess.run(list_dir_long_command)

# Using subprocess.run() with two additional arguments to list a specific file
file_name = "README.md"
if current_os == "Windows":
    list_file_command = ["cmd", "/c", "dir", file_name]
else:
    list_file_command = ["ls", "-l", file_name]

subprocess.run(list_file_command)

# Running uname -a or equivalent command
if current_os == "Windows":
    uname_command = ["cmd", "/c", "ver"]
else:
    uname_command = ["uname", "-a"]

subprocess.run(uname_command)

# Running ps -x or equivalent command
if current_os == "Windows":
    ps_command = ["cmd", "/c", "tasklist"]
else:
    ps_command = ["ps", "-x"]

subprocess.run(ps_command)

# The os.system function executes the command as a string
# The subprocess.run function takes a list of command arguments
# The commands are conditionally defined to handle both Unix-like and Windows systems
