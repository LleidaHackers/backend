import json
from utils import parseModule

if __name__ == "__main__":
    parsedObjects = []
    with open("data.json", "r") as file:
        data = json.load(file)
        nodes = data['nodes']
        for node in nodes:
            parsedObjects.append(parseModule(node))
    for obj in parsedObjects:
        print("Printing object: ")
        print(obj)

