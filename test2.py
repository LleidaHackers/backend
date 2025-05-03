import json
from utils import parseModule

if __name__ == "__main__":
    parsedObjects = []
    with open("data.json", "r") as file:
        data = json.load(file)
        for node in data[0].get("nodes"):
            parsedObjects.append(parseModule(node))
            print(parsedObjects[-1].name)