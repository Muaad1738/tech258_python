import os

# Directory

directory = "test_dir"

# parent directory
parent_directory = "c:/Users/abdul/Downloads"

#path
path = os.path.join(parent_directory, directory)

# create dir
os.mkdir(path)

