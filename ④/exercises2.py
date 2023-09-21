import json

data = {
    "country": "Japan",
    "cities": ["Tokyo", "Osaka", "Hokkaido"],
    "population": 126800000
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)
