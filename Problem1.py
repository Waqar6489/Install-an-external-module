'''Write a python program to print the contents of a directory using the os module.
Search online for the function which does that.'''
import os

# Specify the directory you want to list
directory = '/'  # Current directory

# List all files and directories in the specified directory
contents = os.listdir(directory)

# Print the contents
for item in contents:
    print(item)