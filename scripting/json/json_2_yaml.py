# Check if JSON is valid JSON

import json  # Importing the json module to work with JSON data
import os    # Importing the os module to work with file paths and directories
import sys   # Importing the sys module to access command-line arguments
import yaml  # Importing the yaml module to work with YAML data


def check_json():
    # Define a function called check_json that checks if the provided JSON file is valid

    if len(sys.argv) > 2:  # Check if there are command-line arguments (excluding the script name)
        if os.path.exists(sys.argv[1]):  # Check if the provided file exists
            # Open the file for reading
            file = open(sys.argv[1], "r")
            # Try to load the JSON data from the file
            json.load(file)
            # Close the file
            file.close()
            # Print a message indicating that the JSON is valid
            print("JSON is Valid!")
            # Return True to indicate that the JSON is valid
            return True
        else:
            # Print an error message if the file does not exist
            print(sys.argv[1] + " not found")
    else:
        # Print usage instructions if no file is provided
        print("Usage: python check_json.py <file>")


if check_json():
    # Check if the JSON is valid by calling the check_json function
    # If the JSON is valid, proceed with converting it to YAML

    path = sys.argv[1]  # Get the file path from the command-line argument
    with open(path) as json_file:  # Open the JSON file for reading
        json_string = json.load(json_file)  # Load the JSON data from the file into a Python variable
    yaml_conversion = yaml.dump(json_string)  # Convert the JSON data to YAML format
    path_cwd = os.getcwd()  # Get the current working directory and save it to a string
    filename = "yaml_output2.yml"  # Define the output file name with the YAML extension
    filepath = os.path.join(path_cwd, filename)  # Create the full file path for the converted YAML file

    with open(filepath, "w") as file1:  # Open the intended file that the YAML will be saved to
        file1.write(yaml_conversion)  # Store the YAML conversion in the file we defined earlier
