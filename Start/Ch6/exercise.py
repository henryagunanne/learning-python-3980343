# Count the size in bytes of text files in a directory
# There is a set of files in the "deps" directory, which is at the same directory level that your code is running in. There are no subdirectories within this "deps" folder.
# Your task: Calculate and return the total size in bytes of the text files within the
# "deps" directory. Only include text files that end with ".txt" in your calculation.
# Other files should be ignored.

# Parameters
# No parameters are passed to your function.

# Result
# [int: Total byte count of all the text files in the directory

# Want a hint?
# Check out the os and os.path modules in the Python standard library.
# Your code will need to:
# • List the contents of the "deps" folder.
# • Iterate over each file and determine the size of each file if it is a "txt" file.
# • Add the size to the total byte count if it is a text file.
# • Return the total bytes.


import os
from os import path

def file_info():
    # Your code goes here.
    totalbytes = 0
    folder = "deps"
    
    # get a list of all the files in the current directory
    dirlist = os.listdir(folder)
    for entry in dirlist:
        # make sure it's a file
        if os.path.isfile(folder + "/" + entry) and entry.endswith(".txt"):
            # add the file size to the total
            filesize = os.path.getsize(folder + "/" + entry)
            totalbytes += filesize  

    return totalbytes


