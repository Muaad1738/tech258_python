import os

# Directory

directory = "test_dir"

# parent directory
parent_directory = "c:/Users/abdul/Downloads"

#path
path = os.path.join(parent_directory, directory)

# file
filename = "test.txt"

# file path
filepath = os.path.join(path, filename)

# create file
with open(filepath, "w") as file1:
    toFile = "contents of the file to go here"
    file1.write(toFile)
print(f"file {filename} created in {directory} folder")



