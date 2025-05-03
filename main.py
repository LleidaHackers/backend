import json
from utils import parseModule

if __name__ == "__main__":
    parsedObjects = []
    with open("data.json", "r") as file:
        data = json.load(file)
        for node in data:
            parsedObjects.append(parseModule(node.get('nodes')[0]))
