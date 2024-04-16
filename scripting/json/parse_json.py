import json
#
with open("new_file.json") as jsonfile:
     car = json.load(jsonfile)
     print(type(car))
     print(car["name"])
     print(car["engine"])


path_to_json = "example.json"
json = json.load(open(path_to_json).read())
value = json["name"]

print(value)