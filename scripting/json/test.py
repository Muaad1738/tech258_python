import json  # Import the json module to work with JSON data
import sys   # Import the sys module to access command-line arguments
import os    # Import the os module to check file existence and manipulate file paths
import yaml  # Import the yaml module to work with YAML data

# Check if command-line arguments are provided
if len(sys.argv) > 1:
    # Check if the file specified in the command-line argument exists
    if os.path.exists(sys.argv[1]):
        # Open the file specified in the command-line argument for reading
        with open(sys.argv[1], "r") as file:
            # Load JSON data from the file into a Python dictionary
            json_data = json.load(file)
            # Close the file after loading the JSON data
            file.close()
            # Print a message indicating that the JSON data is valid
            print("JSON is valid")

            # Convert the JSON data to YAML format
            yaml_data = yaml.dump(json_data)

            # Write the YAML data to a file named "output.yaml"
            with open("output.yaml", "w") as yaml_file:
                yaml_file.write(yaml_data)


    else:
        # Print an error message if the file specified in the command-line argument does not exist
        print(sys.argv[1] + " is not found")
else:
    # Print a usage message if no command-line argument is provided
    print("usage: python check_json.py <file>")
