import json

with open("json_data.json", "r") as file:
    data = json.load(file)
    for student in data["students"]:
        print(student["name"])
