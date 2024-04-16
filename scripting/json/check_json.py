
import sys, os, json

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is valid")
    else:
        print(sys.argv[1] + " is not found")
else:
    print("usage: python check_json.py <file>")
